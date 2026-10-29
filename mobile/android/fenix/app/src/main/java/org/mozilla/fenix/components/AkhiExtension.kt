/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package org.mozilla.fenix.components

import mozilla.components.concept.engine.webextension.WebExtensionRuntime
import mozilla.components.support.base.log.logger.Logger

/**
 * The AkhiBrowser built-in extension (browser/extensions/akhi/): NoMusic, adult and haram content
 * blocking, and the installation of uBlock Origin.
 */
object AkhiExtension {
    private val logger = Logger("akhi")

    private const val EXTENSION_ID = "akhi@akhibrowser.org"
    private const val EXTENSION_URL = "resource://android/assets/extensions/akhi/"

    /** Installs the extension in the runtime, it is updated with the app. */
    fun install(runtime: WebExtensionRuntime) {
        runtime.installBuiltInWebExtension(
            EXTENSION_ID,
            EXTENSION_URL,
            onSuccess = { logger.debug("Installed AkhiBrowser webextension: ${it.id}") },
            onError = { throwable -> logger.error("Failed to install AkhiBrowser webextension", throwable) },
        )
    }
}
