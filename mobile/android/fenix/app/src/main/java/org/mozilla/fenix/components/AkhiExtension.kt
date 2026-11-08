/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package org.mozilla.fenix.components

import android.content.Context
import kotlin.concurrent.thread
import mozilla.components.browser.state.state.searchEngines
import mozilla.components.browser.state.store.BrowserStore
import mozilla.components.concept.engine.webextension.WebExtensionRuntime
import mozilla.components.feature.search.SearchUseCases
import mozilla.components.feature.search.ext.waitForSelectedOrDefaultSearchEngine
import mozilla.components.support.base.log.logger.Logger

/**
 * The AkhiBrowser built-in extension (browser/extensions/akhi/): NoMusic, adult and haram content
 * blocking, and the installation of uBlock Origin.
 */
object AkhiExtension {
    private val logger = Logger("akhi")

    private const val EXTENSION_ID = "akhi@akhibrowser.org"
    private const val EXTENSION_URL = "resource://android/assets/extensions/akhi/"

    private const val PREFERENCES = "akhi"
    private const val SEARCH_ENGINE_SET = "default_search_engine_set"
    private const val DEFAULT_SEARCH_ENGINE = "DuckDuckGo"

    /** Installs the extension in the runtime, it is updated with the app. */
    fun install(runtime: WebExtensionRuntime, context: Context) {
        runtime.installBuiltInWebExtension(
            EXTENSION_ID,
            EXTENSION_URL,
            onSuccess = {
                logger.debug("Installed AkhiBrowser webextension: ${it.id}")
                it.registerBackgroundMessageHandler(AkhiStore.NATIVE_APP, AkhiStore(context))
            },
            onError = { throwable -> logger.error("Failed to install AkhiBrowser webextension", throwable) },
        )
    }

    /**
     * DuckDuckGo as the default search engine once, on a new install, as on desktop (the extension's
     * setDefaultSearchEngine doesn't reach Fenix's own search engines). The user can choose another one after that.
     */
    fun setDefaultSearchEngine(
        context: Context,
        store: BrowserStore,
        selectSearchEngine: SearchUseCases.SelectSearchEngineUseCase,
    ) {
        // once the search engines are loaded, and in a thread of its own: the preferences are never read on the main
        // thread at startup
        store.waitForSelectedOrDefaultSearchEngine {
            thread(name = "AkhiSearchEngine") {
                val preferences = context.getSharedPreferences(PREFERENCES, Context.MODE_PRIVATE)
                if (preferences.getBoolean(SEARCH_ENGINE_SET, false)) {
                    return@thread
                }
                val duckDuckGo = store.state.search.searchEngines.find { it.name == DEFAULT_SEARCH_ENGINE }
                if (duckDuckGo != null) {
                    selectSearchEngine(duckDuckGo)
                    preferences.edit().putBoolean(SEARCH_ENGINE_SET, true).apply()
                }
            }
        }
    }
}
