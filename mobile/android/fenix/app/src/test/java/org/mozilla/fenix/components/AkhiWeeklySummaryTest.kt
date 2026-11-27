/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package org.mozilla.fenix.components

import org.junit.Assert.assertEquals
import org.junit.Test
import java.time.DayOfWeek
import java.time.ZoneId
import java.time.ZonedDateTime

class AkhiWeeklySummaryTest {
    private val zone = ZoneId.of("Europe/Amsterdam")

    @Test
    fun `weekTotal counts today and the six days before`() {
        val today = 20_000L
        val counts = mapOf(today - 7 to 100, today - 6 to 2, today to 3, today + 1 to 50)
        assertEquals(5, AkhiWeeklySummary.weekTotal(counts, today))
        assertEquals(0, AkhiWeeklySummary.weekTotal(emptyMap(), today))
    }

    @Test
    fun `nextTime is the coming Sunday at six in the evening`() {
        val friday = ZonedDateTime.of(2026, 11, 27, 12, 0, 0, 0, zone)
        val next = AkhiWeeklySummary.nextTime(friday)
        assertEquals(DayOfWeek.SUNDAY, next.dayOfWeek)
        assertEquals(29, next.dayOfMonth)
        assertEquals(18, next.hour)
    }

    @Test
    fun `nextTime on Sunday evening is a week later`() {
        val sundayMorning = ZonedDateTime.of(2026, 11, 29, 9, 0, 0, 0, zone)
        assertEquals(29, AkhiWeeklySummary.nextTime(sundayMorning).dayOfMonth)
        val sundayEvening = ZonedDateTime.of(2026, 11, 29, 18, 0, 0, 0, zone)
        assertEquals(6, AkhiWeeklySummary.nextTime(sundayEvening).dayOfMonth)
    }
}
