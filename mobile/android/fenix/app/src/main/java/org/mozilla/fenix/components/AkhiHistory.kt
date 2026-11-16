/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package org.mozilla.fenix.components

import android.content.Context
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.SupervisorJob
import kotlinx.coroutines.launch
import mozilla.components.concept.engine.EngineSession
import mozilla.components.concept.engine.webextension.MessageHandler
import org.json.JSONObject
import org.mozilla.fenix.ext.components

/**
 * A site the extension blocked stays out of the history, and so out of the top sites and the shortcuts of the home
 * screen: background.js sends {forget: [the site, its blocked page]} (on desktop the extension removes it itself).
 */
internal object AkhiHistory {
    const val NATIVE_APP = "akhiHistory"

    private val scope = CoroutineScope(SupervisorJob() + Dispatchers.IO)

    class Messages(context: Context) : MessageHandler {
        private val appContext = context.applicationContext

        override fun onMessage(message: Any, source: EngineSession?): Any {
            val urls = runCatching { JSONObject(message.toString()).getJSONArray("forget") }.getOrNull()
            if (urls != null) {
                val storage = appContext.components.core.historyStorage
                scope.launch {
                    for (i in 0 until urls.length()) {
                        val url = urls.optString(i)
                        if (url.isNotEmpty()) {
                            runCatching { storage.deleteVisitsFor(url) }
                        }
                    }
                }
            }
            return JSONObject().put("ok", true)
        }
    }
}
