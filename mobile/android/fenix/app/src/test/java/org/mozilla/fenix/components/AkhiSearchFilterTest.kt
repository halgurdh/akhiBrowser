/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package org.mozilla.fenix.components

import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class AkhiSearchFilterTest {
    @Test
    fun `getting it is blocked`() {
        assertTrue(AkhiSearchFilter.isBlocked("beer"))
        assertTrue(AkhiSearchFilter.isBlocked("buy alcohol"))
        assertTrue(AkhiSearchFilter.isBlocked("casino near me"))
        assertTrue(AkhiSearchFilter.isBlocked("porn addiction videos"))
        assertTrue(AkhiSearchFilter.isBlocked("bier kopen"))
        assertTrue(AkhiSearchFilter.isBlocked("jeux d'argent"))
        assertTrue(AkhiSearchFilter.isBlocked("free slot machine"))
        assertTrue(AkhiSearchFilter.isBlocked("vapes"))
        assertTrue(AkhiSearchFilter.isBlocked("الخمر"))
    }

    @Test
    fun `learning about it is allowed`() {
        assertFalse(AkhiSearchFilter.isBlocked("why is alcohol haram"))
        assertFalse(AkhiSearchFilter.isBlocked("dangers of gambling"))
        assertFalse(AkhiSearchFilter.isBlocked("porn addiction help"))
        assertFalse(AkhiSearchFilter.isBlocked("حكم الخمر"))
        assertFalse(AkhiSearchFilter.isBlocked("weather amsterdam"))
    }

    @Test
    fun `suggestions don't bring up what wasn't typed`() {
        assertFalse(AkhiSearchFilter.allowsSuggestion("be", "beer"))
        assertTrue(AkhiSearchFilter.allowsSuggestion("be", "best phones"))
        assertTrue(AkhiSearchFilter.allowsSuggestion("is alcohol", "is alcohol haram"))
        assertFalse(AkhiSearchFilter.allowsSuggestion("why alcohol", "buy alcohol online"))
        assertFalse(AkhiSearchFilter.allowsSuggestion("", "casino bonus"))
    }
}
