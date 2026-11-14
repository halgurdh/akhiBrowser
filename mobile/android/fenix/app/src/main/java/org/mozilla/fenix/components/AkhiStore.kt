/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package org.mozilla.fenix.components

import android.app.Activity
import android.app.Application
import android.content.Context
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import com.android.billingclient.api.AcknowledgePurchaseParams
import com.android.billingclient.api.BillingClient
import com.android.billingclient.api.BillingClientStateListener
import com.android.billingclient.api.BillingFlowParams
import com.android.billingclient.api.BillingResult
import com.android.billingclient.api.ConsumeParams
import com.android.billingclient.api.PendingPurchasesParams
import com.android.billingclient.api.Purchase
import com.android.billingclient.api.PurchasesUpdatedListener
import com.android.billingclient.api.QueryProductDetailsParams
import com.android.billingclient.api.QueryPurchasesParams
import com.android.installreferrer.api.InstallReferrerClient
import com.android.installreferrer.api.InstallReferrerStateListener
import mozilla.components.concept.engine.EngineSession
import mozilla.components.concept.engine.webextension.MessageHandler
import mozilla.components.concept.engine.webextension.Port
import org.json.JSONObject
import org.mozilla.fenix.BuildConfig
import java.lang.ref.WeakReference

/**
 * The native side of lib/premium.js in the built-in extension. It tells the extension which store this build is for,
 * and on a Google Play build sells and checks Premium with Play Billing. Each message is {id, type, ...}, answered with
 * {id, ...} on the port. Play keeps the purchases. The status says the product and purchase token too: the extension
 * sends them to the license server only when the buyer asks for a key for their other devices (lib/premium.js).
 */
internal class AkhiStore(context: Context) : MessageHandler, PurchasesUpdatedListener {
    private val appContext = context.applicationContext
    private val mainHandler = Handler(Looper.getMainLooper())
    private var port: Port? = null
    private var resumedActivity = WeakReference<Activity>(null)
    private var pendingBuyId: Int? = null
    private var isConnecting = false
    private val waitingForBilling = mutableListOf<Pair<() -> Unit, () -> Unit>>()

    private val billingClient: BillingClient by lazy {
        BillingClient.newBuilder(appContext)
            .setListener(this)
            .enablePendingPurchases(PendingPurchasesParams.newBuilder().enableOneTimeProducts().build())
            .enableAutoServiceReconnection()
            .build()
    }

    init {
        (appContext as Application).registerActivityLifecycleCallbacks(
            object : Application.ActivityLifecycleCallbacks {
                override fun onActivityResumed(activity: Activity) {
                    resumedActivity = WeakReference(activity)
                }

                override fun onActivityCreated(activity: Activity, savedInstanceState: Bundle?) = Unit
                override fun onActivityStarted(activity: Activity) = Unit
                override fun onActivityPaused(activity: Activity) = Unit
                override fun onActivityStopped(activity: Activity) = Unit
                override fun onActivitySaveInstanceState(activity: Activity, outState: Bundle) = Unit
                override fun onActivityDestroyed(activity: Activity) = Unit
            },
        )
    }

    override fun onPortConnected(port: Port) {
        this.port = port
    }

    override fun onPortDisconnected(port: Port) {
        if (this.port === port) {
            this.port = null
        }
    }

    override fun onPortMessage(message: Any, port: Port) {
        val request = message as? JSONObject ?: return
        val id = request.optInt("id")
        mainHandler.post {
            when (request.optString("type")) {
                "store" -> reply(id, JSONObject().put("store", if (BuildConfig.AKHI_PLAY_STORE) "play" else "direct"))
                "status" -> if (BuildConfig.AKHI_PLAY_STORE) status(id) else replyError(id)
                "buy" -> if (BuildConfig.AKHI_PLAY_STORE) {
                    buy(id, request.optString("plan"), request.optString("offer"))
                } else {
                    replyError(id)
                }
                "referrer" -> if (BuildConfig.AKHI_PLAY_STORE) referrer(id) else replyError(id)
                "gifts" -> if (BuildConfig.AKHI_PLAY_STORE) gifts(id) else replyError(id)
                "consume" -> if (BuildConfig.AKHI_PLAY_STORE) consumeGift(id, request.optString("purchaseToken")) else replyError(id)
                else -> replyError(id)
            }
        }
    }

    override fun onMessage(message: Any, source: EngineSession?): Any? = null

    private fun reply(id: Int, answer: JSONObject) {
        port?.postMessage(answer.put("id", id))
    }

    private fun replyError(id: Int) = reply(id, JSONObject().put("error", true))

    private fun withBilling(onError: () -> Unit, action: () -> Unit) {
        if (billingClient.isReady) {
            action()
            return
        }
        waitingForBilling.add(action to onError)
        if (isConnecting) {
            return
        }
        isConnecting = true
        billingClient.startConnection(
            object : BillingClientStateListener {
                override fun onBillingSetupFinished(result: BillingResult) {
                    mainHandler.post {
                        isConnecting = false
                        val waiting = waitingForBilling.toList()
                        waitingForBilling.clear()
                        waiting.forEach { (waitingAction, waitingError) ->
                            if (result.isOk()) waitingAction() else waitingError()
                        }
                    }
                }

                override fun onBillingServiceDisconnected() = Unit
            },
        )
    }

    private fun purchasesOf(productType: String, onError: () -> Unit, onResult: (List<Purchase>) -> Unit) {
        billingClient.queryPurchasesAsync(
            QueryPurchasesParams.newBuilder().setProductType(productType).build(),
        ) { result, purchases ->
            mainHandler.post {
                if (result.isOk()) {
                    onResult(purchases.filter { it.purchaseState == Purchase.PurchaseState.PURCHASED })
                } else {
                    onError()
                }
            }
        }
    }

    private fun status(id: Int) {
        val onError = { replyError(id) }
        withBilling(onError) {
            purchasesOf(BillingClient.ProductType.SUBS, onError) { subscriptions ->
                purchasesOf(BillingClient.ProductType.INAPP, onError) { oneTime ->
                    val ownedOneTime = oneTime.filter { LIFETIME_PRODUCT in it.products }
                    val ownedFamily = subscriptions.filter { FAMILY_PRODUCT in it.products }
                    val ownedSubscriptions = subscriptions.filter { SUBSCRIPTION_PRODUCT in it.products }
                    // a year of Family from a gift's promo code: once the year is over it's consumed, so that the
                    // next gift's code can be redeemed on the same account
                    val (ownedYear, endedYear) = oneTime
                        .filter { FAMILY_YEAR_PRODUCT in it.products }
                        .partition { System.currentTimeMillis() < it.purchaseTime + YEAR_MS }
                    endedYear.forEach(::consume)
                    (ownedOneTime + ownedFamily + ownedSubscriptions + ownedYear).forEach(::acknowledge)
                    val (plan, purchase, product) = when {
                        ownedFamily.isNotEmpty() -> Triple("family", ownedFamily.first(), FAMILY_PRODUCT)
                        ownedYear.isNotEmpty() -> Triple("family", ownedYear.first(), FAMILY_YEAR_PRODUCT)
                        ownedOneTime.isNotEmpty() -> Triple("lifetime", ownedOneTime.first(), LIFETIME_PRODUCT)
                        ownedSubscriptions.isNotEmpty() ->
                            Triple("subscription", ownedSubscriptions.first(), SUBSCRIPTION_PRODUCT)
                        else -> Triple(null, null, null)
                    }
                    reply(
                        id,
                        JSONObject()
                            .put("isActive", plan != null)
                            .put("plan", plan ?: JSONObject.NULL)
                            .put("product", product ?: JSONObject.NULL)
                            .put("purchaseToken", purchase?.purchaseToken ?: JSONObject.NULL),
                    )
                }
            }
        }
    }

    // the gifts bought that the extension hasn't turned into a Play code yet: it asks the license server, then consumes them
    private fun gifts(id: Int) {
        val onError = { replyError(id) }
        withBilling(onError) {
            purchasesOf(BillingClient.ProductType.INAPP, onError) { oneTime ->
                val tokens = oneTime.filter { GIFT_PRODUCT in it.products }.map { it.purchaseToken }
                reply(id, JSONObject().put("purchaseTokens", org.json.JSONArray(tokens)))
            }
        }
    }

    private fun consumeGift(id: Int, purchaseToken: String) {
        if (purchaseToken.isEmpty()) {
            replyError(id)
            return
        }
        withBilling({ replyError(id) }) {
            billingClient.consumeAsync(ConsumeParams.newBuilder().setPurchaseToken(purchaseToken).build()) { result, _ ->
                mainHandler.post { reply(id, JSONObject().put("consumed", result.isOk())) }
            }
        }
    }

    // the referrer of the Play Store link this was installed from, like "ref=<affiliate code>": the extension keeps its
    // code, for a VIP's Family offer and their commission (lib/premium.js)
    private fun referrer(id: Int) {
        val client = InstallReferrerClient.newBuilder(appContext).build()
        client.startConnection(
            object : InstallReferrerStateListener {
                override fun onInstallReferrerSetupFinished(responseCode: Int) {
                    val referrer = if (responseCode == InstallReferrerClient.InstallReferrerResponse.OK) {
                        runCatching { client.installReferrer.installReferrer }.getOrNull()
                    } else {
                        null
                    }
                    runCatching { client.endConnection() }
                    mainHandler.post { reply(id, JSONObject().put("referrer", referrer ?: JSONObject.NULL)) }
                }

                override fun onInstallReferrerServiceDisconnected() = Unit
            },
        )
    }

    private fun buy(id: Int, plan: String, offer: String = "") {
        val isLifetime = plan == "lifetime"
        val isGift = plan == "gift"
        if (!isLifetime && !isGift && plan != "monthly" && plan != "yearly" && plan != "family") {
            replyError(id)
            return
        }
        val isOneTime = isLifetime || isGift
        val productType = if (isOneTime) BillingClient.ProductType.INAPP else BillingClient.ProductType.SUBS
        val product = QueryProductDetailsParams.Product.newBuilder()
            .setProductId(
                when (plan) {
                    "lifetime" -> LIFETIME_PRODUCT
                    "gift" -> GIFT_PRODUCT
                    "family" -> FAMILY_PRODUCT
                    else -> SUBSCRIPTION_PRODUCT
                },
            )
            .setProductType(productType)
            .build()
        withBilling({ replyError(id) }) {
            billingClient.queryProductDetailsAsync(
                QueryProductDetailsParams.newBuilder().setProductList(listOf(product)).build(),
            ) { result, details ->
                mainHandler.post {
                    val productDetails = details.productDetailsList.firstOrNull()
                    val offerToken = if (isOneTime) {
                        productDetails?.oneTimePurchaseOfferDetailsList?.firstOrNull()?.offerToken
                    } else {
                        // a VIP's Family offer when asked for and set up in the Play Console, else the base plan
                        val offers = productDetails?.subscriptionOfferDetails.orEmpty()
                        (offers.firstOrNull { offer.isNotEmpty() && it.basePlanId == plan && it.offerId == offer }
                            ?: offers.firstOrNull { it.basePlanId == plan && it.offerId == null })
                            ?.offerToken
                    }
                    val activity = resumedActivity.get()
                    if (!result.isOk() || productDetails == null || offerToken == null || activity == null) {
                        replyError(id)
                        return@post
                    }
                    val params = BillingFlowParams.newBuilder()
                        .setProductDetailsParamsList(
                            listOf(
                                BillingFlowParams.ProductDetailsParams.newBuilder()
                                    .setProductDetails(productDetails)
                                    .setOfferToken(offerToken)
                                    .build(),
                            ),
                        )
                        .build()
                    pendingBuyId = id
                    if (!billingClient.launchBillingFlow(activity, params).isOk()) {
                        pendingBuyId = null
                        replyError(id)
                    }
                }
            }
        }
    }

    override fun onPurchasesUpdated(result: BillingResult, purchases: List<Purchase>?) {
        mainHandler.post {
            val bought = purchases.orEmpty().filter { it.purchaseState == Purchase.PurchaseState.PURCHASED }
            bought.forEach(::acknowledge)
            val id = pendingBuyId ?: return@post
            pendingBuyId = null
            val answer = when {
                result.isOk() && bought.isNotEmpty() -> "active"
                result.isOk() -> "pending"
                result.responseCode == BillingClient.BillingResponseCode.ITEM_ALREADY_OWNED -> "active"
                result.responseCode == BillingClient.BillingResponseCode.USER_CANCELED -> "cancelled"
                else -> "error"
            }
            reply(id, JSONObject().put("result", answer))
        }
    }

    // Play refunds a purchase that isn't acknowledged within three days
    private fun acknowledge(purchase: Purchase) {
        if (!purchase.isAcknowledged) {
            billingClient.acknowledgePurchase(
                AcknowledgePurchaseParams.newBuilder().setPurchaseToken(purchase.purchaseToken).build(),
            ) { }
        }
    }

    private fun consume(purchase: Purchase) {
        billingClient.consumeAsync(ConsumeParams.newBuilder().setPurchaseToken(purchase.purchaseToken).build()) { _, _ -> }
    }

    private fun BillingResult.isOk() = responseCode == BillingClient.BillingResponseCode.OK

    companion object {
        const val NATIVE_APP = "akhiStore"

        // As set up in the Play Console. Family is its own product because a purchase doesn't say its base plan.
        private const val SUBSCRIPTION_PRODUCT = "akhi_premium"
        private const val FAMILY_PRODUCT = "akhi_family"
        private const val LIFETIME_PRODUCT = "akhi_premium_lifetime"

        // Given only with promo codes, for gifts (the license server's /redeem): a year of Family from redeeming it
        private const val FAMILY_YEAR_PRODUCT = "akhi_family_year"
        private const val YEAR_MS = 365L * 24 * 3600 * 1000

        // A consumable: a year of Family for someone else, as a Play code of FAMILY_YEAR_PRODUCT (/play/gift)
        private const val GIFT_PRODUCT = "akhi_family_gift"
    }
}
