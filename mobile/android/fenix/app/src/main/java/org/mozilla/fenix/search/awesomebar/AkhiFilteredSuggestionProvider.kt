/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package org.mozilla.fenix.search.awesomebar

import mozilla.components.concept.awesomebar.AwesomeBar
import org.mozilla.fenix.components.AkhiSearchFilter

/**
 * AkhiBrowser: the suggestions of [delegate] without the adult and haram ones (AkhiSearchFilter), whatever the search
 * engine. On computers the extension leaves them out of its start page; on Android this does it for the address bar.
 */
class AkhiFilteredSuggestionProvider(
    val delegate: AwesomeBar.SuggestionProvider,
) : AwesomeBar.SuggestionProvider {
    override val id: String = delegate.id

    override fun groupTitle(): String? = delegate.groupTitle()

    override fun displayGroupTitle(): Boolean = delegate.displayGroupTitle()

    override fun onInputStarted(): List<AwesomeBar.Suggestion> =
        delegate.onInputStarted().mapNotNull { allowed("", it) }

    override suspend fun onInputChanged(text: String): List<AwesomeBar.SuggestionItem> =
        delegate.onInputChanged(text).mapNotNull { item ->
            if (item is AwesomeBar.Suggestion) allowed(text, item) else item
        }

    override fun onInputCancelled() = delegate.onInputCancelled()

    private fun allowed(typed: String, suggestion: AwesomeBar.Suggestion): AwesomeBar.Suggestion? {
        val title = suggestion.title ?: return suggestion.copy(provider = this)
        return if (AkhiSearchFilter.allowsSuggestion(typed, title)) suggestion.copy(provider = this) else null
    }
}
