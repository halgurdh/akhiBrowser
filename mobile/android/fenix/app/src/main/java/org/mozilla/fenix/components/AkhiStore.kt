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
import com.android.billingclient.api.PendingPurchasesParams
import com.android.billingclient.api.Purchase
import com.android.billingclient.api.PurchasesUpdatedListener
import com.android.billingclient.api.QueryProductDetailsParams
import com.android.billingclient.api.QueryPurchasesParams
import mozilla.components.concept.engine.EngineSession
import mozilla.components.concept.engine.webextension.MessageHandler
import mozilla.components.concept.engine.webextension.Port
import org.json.JSONObject
import org.mozilla.fenix.BuildConfig
import java.lang.ref.WeakReference

/**
 * The native side of lib/premium.js in the built-in extension. It tells the extension which store this build is for,
 * and on a Google Play build sells and checks Premium with Play Billing. Each message is {id, type, ...}, answered with
 * {id, ...} on the port. Play keeps the purchases, so nothing about them leaves the device from here.
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
                "buy" -> if (BuildConfig.AKHI_PLAY_STORE) buy(id, request.optString("plan")) else replyError(id)
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
                    val ownedSubscriptions = subscriptions.filter { SUBSCRIPTION_PRODUCT in it.products }
                    (ownedOneTime + ownedSubscriptions).forEach(::acknowledge)
                    val plan = when {
                        ownedOneTime.isNotEmpty() -> "lifetime"
                        ownedSubscriptions.isNotEmpty() -> "subscription"
                        else -> JSONObject.NULL
                    }
                    reply(id, JSONObject().put("isActive", plan != JSONObject.NULL).put("plan", plan))
                }
            }
        }
    }

    private fun buy(id: Int, plan: String) {
        val isLifetime = plan == "lifetime"
        if (!isLifetime && plan != "monthly" && plan != "yearly" && plan != "family") {
            replyError(id)
            return
        }
        val productType = if (isLifetime) BillingClient.ProductType.INAPP else BillingClient.ProductType.SUBS
        val product = QueryProductDetailsParams.Product.newBuilder()
            .setProductId(if (isLifetime) LIFETIME_PRODUCT else SUBSCRIPTION_PRODUCT)
            .setProductType(productType)
            .build()
        withBilling({ replyError(id) }) {
            billingClient.queryProductDetailsAsync(
                QueryProductDetailsParams.newBuilder().setProductList(listOf(product)).build(),
            ) { result, details ->
                mainHandler.post {
                    val productDetails = details.productDetailsList.firstOrNull()
                    val offerToken = if (isLifetime) {
                        productDetails?.oneTimePurchaseOfferDetailsList?.firstOrNull()?.offerToken
                    } else {
                        productDetails?.subscriptionOfferDetails
                            ?.firstOrNull { it.basePlanId == plan && it.offerId == null }
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

    private fun BillingResult.isOk() = responseCode == BillingClient.BillingResponseCode.OK

    companion object {
        const val NATIVE_APP = "akhiStore"

        // One subscription with monthly, yearly, and family base plans, as set up in the Play Console
        private const val SUBSCRIPTION_PRODUCT = "akhi_premium"
        private const val LIFETIME_PRODUCT = "akhi_premium_lifetime"
    }
}
