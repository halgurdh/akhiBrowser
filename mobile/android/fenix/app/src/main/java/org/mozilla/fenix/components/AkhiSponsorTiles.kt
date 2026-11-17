/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package org.mozilla.fenix.components

import android.content.Context
import android.content.SharedPreferences
import androidx.core.content.edit
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import mozilla.components.concept.engine.EngineSession
import mozilla.components.concept.engine.webextension.MessageHandler
import mozilla.components.concept.fetch.Client
import mozilla.components.concept.fetch.Request
import mozilla.components.concept.fetch.Request.CookiePolicy
import mozilla.components.concept.fetch.isSuccess
import mozilla.components.feature.top.sites.TopSite
import mozilla.components.feature.top.sites.TopSitesProvider
import mozilla.components.support.base.log.logger.Logger
import org.json.JSONException
import org.json.JSONObject
import java.io.IOException
import java.util.concurrent.TimeUnit

/**
 * The shortcuts of AkhiBrowser's own sponsors on the home screen, for free users only, in place of Mozilla's sponsored
 * shortcuts: from the license server's /tiles, in the format of Firefox's sponsored shortcuts. A tile opens the sponsor
 * through the server's click counter (akhi_url), which keeps only the sponsor, the day and a count; nothing else is
 * sent, no impressions and nothing to Mozilla. Off with the Sponsored shortcuts setting, and with Premium, which the
 * built-in extension sends to [NATIVE_APP] whenever it starts or ends.
 */
class AkhiSponsorTiles(
    context: Context,
    private val client: Client,
) : TopSitesProvider {
    private val logger = Logger("AkhiSponsorTiles")
    private val preferences = context.applicationContext.getSharedPreferences(PREFERENCES, Context.MODE_PRIVATE)

    override suspend fun getTopSites(allowCache: Boolean): List<TopSite> =
        withContext(Dispatchers.IO) {
            if (isPremium(preferences)) {
                return@withContext emptyList()
            }
            val cached = preferences.getString(CACHE, null)
            val text = if (allowCache && cached != null && !isExpired()) cached else fetch() ?: cached
            text?.let(::tilesOf).orEmpty()
        }

    override suspend fun refreshTopSitesIfCacheExpired() {
        withContext(Dispatchers.IO) {
            if (!isPremium(preferences) && isExpired()) {
                fetch()
            }
        }
    }

    private fun isExpired() = System.currentTimeMillis() - preferences.getLong(CACHE_TIME, 0) > CACHE_MS

    private fun fetch(): String? =
        try {
            val request = Request(
                url = TILES_URL,
                connectTimeout = TIMEOUT_SECONDS to TimeUnit.SECONDS,
                readTimeout = TIMEOUT_SECONDS to TimeUnit.SECONDS,
                cookiePolicy = CookiePolicy.OMIT,
                private = true,
            ).apply { conservative = true }
            client.fetch(request).use { response ->
                if (response.isSuccess) {
                    response.body.string().also { text ->
                        preferences.edit {
                            putString(CACHE, text)
                            putLong(CACHE_TIME, System.currentTimeMillis())
                        }
                    }
                } else {
                    null
                }
            }
        } catch (e: IOException) {
            logger.warn("The sponsor shortcuts couldn't be fetched", e)
            null
        }

    /** Receives whether Premium is active from the built-in extension (background.js, syncPremiumActive). */
    class Messages(context: Context) : MessageHandler {
        private val appContext = context.applicationContext

        override fun onMessage(message: Any, source: EngineSession?): Any {
            val isActive = runCatching { JSONObject(message.toString()).optBoolean("isActive", false) }.getOrDefault(false)
            appContext.getSharedPreferences(PREFERENCES, Context.MODE_PRIVATE).edit { putBoolean(PREMIUM, isActive) }
            return JSONObject().put("ok", true)
        }
    }

    companion object {
        const val NATIVE_APP = "akhiPremium"

        private const val TILES_URL = "https://akhi-license.akhibrowser.workers.dev/tiles"
        private const val PREFERENCES = "akhi"
        private const val PREMIUM = "premium_active"
        private const val CACHE = "sponsor_tiles"
        private const val CACHE_TIME = "sponsor_tiles_time"
        private const val CACHE_MS = 3 * 60 * 60 * 1000L
        private const val TIMEOUT_SECONDS = 10L
        private const val MAX_TILES = 2

        /** Whether the built-in extension last said Premium is active: then no sponsor shortcuts. */
        fun isPremium(context: Context) =
            isPremium(context.applicationContext.getSharedPreferences(PREFERENCES, Context.MODE_PRIVATE))

        private fun isPremium(preferences: SharedPreferences) = preferences.getBoolean(PREMIUM, false)

        /** The tiles of the server's answer, with an https click address, a name and an image; at most [MAX_TILES]. */
        internal fun tilesOf(text: String): List<TopSite> =
            try {
                val tiles = JSONObject(text).optJSONArray("tiles") ?: return emptyList()
                (0 until tiles.length())
                    .mapNotNull { index -> tiles.optJSONObject(index) }
                    .mapNotNull { tile ->
                        val url = tile.optString("akhi_url")
                        val name = tile.optString("name")
                        val image = tile.optString("image_url")
                        if (url.startsWith("https://") && name.isNotEmpty() && image.startsWith("https://")) {
                            TopSite.Provided(
                                id = tile.optLong("id"),
                                title = name,
                                url = url,
                                // empty: TopSiteController sends no click or impression callbacks for these tiles
                                clickUrl = "",
                                imageUrl = image,
                                impressionUrl = "",
                                createdAt = null,
                            )
                        } else {
                            null
                        }
                    }
                    .take(MAX_TILES)
            } catch (e: JSONException) {
                emptyList()
            }
    }
}
