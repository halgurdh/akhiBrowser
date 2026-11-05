/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package org.mozilla.fenix.components

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

class AkhiUpdaterTest {
    @Test
    fun `isNewer compares each part as a number`() {
        assertTrue(AkhiUpdater.isNewer("1.0.1", "1.0.0"))
        assertTrue(AkhiUpdater.isNewer("v1.10.0", "1.9.9"))
        assertTrue(AkhiUpdater.isNewer("2.0.0", "1.99.99"))
        assertFalse(AkhiUpdater.isNewer("1.0.0", "1.0.0"))
        assertFalse(AkhiUpdater.isNewer("1.0.0", "1.0.1"))
    }

    @Test
    fun `isNewer is false for anything but a release version`() {
        assertFalse(AkhiUpdater.isNewer("0.2.1-beta", "0.1.0"))
        assertFalse(AkhiUpdater.isNewer("latest", "1.0.0"))
        assertFalse(AkhiUpdater.isNewer("1.0.1", ""))
        assertFalse(AkhiUpdater.isNewer("99999999999999999999.0.0", "1.0.0"))
    }

    @Test
    fun `checksumOf finds the file in either format of sha256sum`() {
        val sums = "ABC123  AkhiBrowser-1.0.1-android-arm64-v8a.apk\r\ndef456 *AkhiBrowser-1.0.1-setup.exe\n"
        assertEquals("abc123", AkhiUpdater.checksumOf(sums, "AkhiBrowser-1.0.1-android-arm64-v8a.apk"))
        assertEquals("def456", AkhiUpdater.checksumOf(sums, "AkhiBrowser-1.0.1-setup.exe"))
        assertNull(AkhiUpdater.checksumOf(sums, "other.apk"))
    }
}
