/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package org.mozilla.fenix.components

import org.junit.Assert.assertArrayEquals
import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Test

class AkhiDnsTest {
    private val message = byteArrayOf(0x12, 0x34, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0)

    // an IPv4 UDP packet from 10.111.222.1:40000 to 10.111.222.2:53
    private fun query(protocol: Int = 17, port: Int = 53): ByteArray {
        val packet = ByteArray(28 + message.size)
        packet[0] = 0x45
        packet[3] = packet.size.toByte()
        packet[9] = protocol.toByte()
        byteArrayOf(10, 111, 222.toByte(), 1).copyInto(packet, 12)
        byteArrayOf(10, 111, 222.toByte(), 2).copyInto(packet, 16)
        packet[20] = (40000 shr 8).toByte()
        packet[21] = 40000.toByte()
        packet[22] = (port shr 8).toByte()
        packet[23] = port.toByte()
        packet[25] = (8 + message.size).toByte()
        message.copyInto(packet, 28)
        return packet
    }

    @Test
    fun `a DNS query is read with who asked`() {
        val query = AkhiDns.queryOf(query())!!
        assertEquals(40000, query.sourcePort)
        assertArrayEquals(byteArrayOf(10, 111, 222.toByte(), 1), query.source)
        assertArrayEquals(message, query.message)
    }

    @Test
    fun `other packets are left alone`() {
        assertNull(AkhiDns.queryOf(query(protocol = 6)))
        assertNull(AkhiDns.queryOf(query(port = 443)))
        assertNull(AkhiDns.queryOf(ByteArray(10)))
        assertNull(AkhiDns.queryOf(query().also { it[0] = 0x60 }))
    }

    @Test
    fun `the reply goes back from the DNS address to the asker, with a valid header checksum`() {
        val reply = AkhiDns.replyOf(AkhiDns.queryOf(query())!!, message)
        assertArrayEquals(byteArrayOf(10, 111, 222.toByte(), 2), reply.copyOfRange(12, 16))
        assertArrayEquals(byteArrayOf(10, 111, 222.toByte(), 1), reply.copyOfRange(16, 20))
        assertEquals(53, ((reply[20].toInt() and 0xff) shl 8) or (reply[21].toInt() and 0xff))
        assertEquals(40000, ((reply[22].toInt() and 0xff) shl 8) or (reply[23].toInt() and 0xff))
        assertEquals(reply.size, ((reply[2].toInt() and 0xff) shl 8) or (reply[3].toInt() and 0xff))
        assertEquals(0, AkhiDns.checksum(reply, 20))
        assertArrayEquals(message, reply.copyOfRange(28, reply.size))
    }
}
