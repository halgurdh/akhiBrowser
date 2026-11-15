/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package org.mozilla.fenix.search.awesomebar

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class AkhiIslamicSuggestionProviderTest {
    @Test
    fun `the searches starting with what was typed come first`() {
        assertEquals("Mosque near me", AkhiIslamicSuggestionProvider.matching("mos").first())
        assertTrue(AkhiIslamicSuggestionProvider.matching("moskee").contains("Moskee in de buurt"))
    }

    @Test
    fun `every typed word can match`() {
        assertTrue(AkhiIslamicSuggestionProvider.matching("near me").contains("Mosque near me"))
    }

    @Test
    fun `nothing typed, nothing shown, and at most four`() {
        assertTrue(AkhiIslamicSuggestionProvider.matching("").isEmpty())
        assertTrue(AkhiIslamicSuggestionProvider.matching("s").size <= 4)
    }
}
