/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package org.mozilla.fenix.components

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Test
import org.mozilla.fenix.components.AkhiPrayerWidget.Prayer

class AkhiPrayerWidgetTest {
    private val today = listOf(Prayer("Fajr", "06:00", 600), Prayer("Isha", "19:00", 1900))
    private val tomorrow = listOf(Prayer("Fajr", "06:01", 3000), Prayer("Isha", "19:01", 4300))

    @Test
    fun `nextOf gives the first prayer still to come, with its day`() {
        assertEquals(today to today[1], AkhiPrayerWidget.nextOf(listOf(today, tomorrow), 1000))
    }

    @Test
    fun `nextOf goes to the next day after the last prayer`() {
        assertEquals(tomorrow to tomorrow[0], AkhiPrayerWidget.nextOf(listOf(today, tomorrow), 2000))
    }

    @Test
    fun `nextOf is null when no prayer is left`() {
        assertNull(AkhiPrayerWidget.nextOf(listOf(today, tomorrow), 5000))
        assertNull(AkhiPrayerWidget.nextOf(emptyList(), 0))
    }
}
