/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package org.mozilla.fenix.components

import android.app.Activity
import android.content.Context
import android.content.Intent
import android.net.VpnService
import android.os.Build
import android.os.Bundle
import android.os.ParcelFileDescriptor
import android.provider.Settings
import mozilla.components.concept.engine.EngineSession
import mozilla.components.concept.engine.webextension.MessageHandler
import org.json.JSONObject
import org.mozilla.fenix.BuildConfig
import java.io.FileInputStream
import java.io.FileOutputStream
import java.io.IOException
import java.net.DatagramPacket
import java.net.DatagramSocket
import java.net.InetAddress
import java.util.concurrent.ExecutorService
import java.util.concurrent.LinkedBlockingQueue
import java.util.concurrent.RejectedExecutionException
import java.util.concurrent.ThreadPoolExecutor
import java.util.concurrent.TimeUnit

/**
 * Family: the whole phone looks up sites through Cloudflare's family DNS, like the browser does, so adult and malware
 * sites are blocked in every app. A local VPN that only carries DNS: the other traffic doesn't go through it. The APK
 * only, taken out for Google Play in src/play/AndroidManifest.xml. The settings are in the extension
 * (pages/family_tools.js); turning it off there needs the parent's PIN.
 */
internal object AkhiPhoneFilter {
    const val NATIVE_APP = "akhiPhoneFilter"
    const val ACTION_STOP = "org.mozilla.fenix.AKHI_PHONE_FILTER_STOP"

    private const val PREFERENCES = "akhi_phone_filter"
    private const val WANTED = "wanted"

    /** Whether the service runs in this process now */
    @Volatile
    var isRunning = false

    /** Whether the parent turned it on: it stays wanted when Android or someone stops it, for the parent report */
    fun isWanted(context: Context): Boolean =
        context.getSharedPreferences(PREFERENCES, Context.MODE_PRIVATE).getBoolean(WANTED, false)

    fun setWanted(context: Context, isWanted: Boolean) {
        context.getSharedPreferences(PREFERENCES, Context.MODE_PRIVATE).edit().putBoolean(WANTED, isWanted).apply()
    }

    fun start(context: Context) {
        context.startService(Intent(context, AkhiPhoneFilterService::class.java))
    }

    fun stop(context: Context) {
        context.startService(Intent(context, AkhiPhoneFilterService::class.java).setAction(ACTION_STOP))
    }

    /** After a restart of the device, when the parent turned it on and Android still allows it */
    fun startAfterBoot(context: Context) {
        if (!BuildConfig.AKHI_PLAY_STORE && isWanted(context) && VpnService.prepare(context) == null) {
            start(context)
        }
    }

    /** Receives the messages of the settings: {type: "status" | "on" | "off" | "vpnSettings"} */
    class Messages(context: Context) : MessageHandler {
        private val appContext = context.applicationContext

        override fun onMessage(message: Any, source: EngineSession?): Any {
            val request = message as? JSONObject ?: return JSONObject()
            if (BuildConfig.AKHI_PLAY_STORE) {
                return JSONObject().put("available", false)
            }
            when (request.optString("type")) {
                "on" -> {
                    setWanted(appContext, true)
                    if (VpnService.prepare(appContext) == null) {
                        start(appContext)
                    } else {
                        // Android asks the user once whether AkhiBrowser may set up a VPN
                        appContext.startActivity(
                            Intent(appContext, AkhiPhoneFilterActivity::class.java)
                                .addFlags(Intent.FLAG_ACTIVITY_NEW_TASK),
                        )
                    }
                }
                "off" -> {
                    setWanted(appContext, false)
                    stop(appContext)
                }
                "vpnSettings" -> appContext.startActivity(
                    Intent(Settings.ACTION_VPN_SETTINGS).addFlags(Intent.FLAG_ACTIVITY_NEW_TASK),
                )
            }
            return JSONObject()
                .put("available", true)
                .put("wanted", isWanted(appContext))
                .put("running", isRunning)
        }
    }
}

/**
 * The DNS packets of the local VPN: IPv4 UDP queries in, replies out. No other packet comes in, as the VPN routes
 * only its DNS address.
 */
@Suppress("MagicNumber") // the offsets and values of the IPv4 and UDP headers
internal object AkhiDns {
    private const val IPV4_HEADER = 20
    private const val UDP_HEADER = 8
    private const val UDP = 17
    const val PORT = 53

    /** A DNS query: who asked (address and port), the address it was sent to, and the DNS message */
    class Query(val source: ByteArray, val sourcePort: Int, val destination: ByteArray, val message: ByteArray)

    private fun u16(bytes: ByteArray, offset: Int) =
        ((bytes[offset].toInt() and 0xff) shl 8) or (bytes[offset + 1].toInt() and 0xff)

    private fun put16(bytes: ByteArray, offset: Int, value: Int) {
        bytes[offset] = (value shr 8).toByte()
        bytes[offset + 1] = value.toByte()
    }

    /** The query in an IPv4 packet, or null when it is anything else */
    fun queryOf(packet: ByteArray, length: Int = packet.size): Query? {
        if (length < IPV4_HEADER + UDP_HEADER || (packet[0].toInt() shr 4) and 0xf != 4) {
            return null
        }
        val headerLength = (packet[0].toInt() and 0xf) * 4
        if (packet[9].toInt() != UDP || length < headerLength + UDP_HEADER || u16(packet, headerLength + 2) != PORT) {
            return null
        }
        val end = minOf(length, headerLength + u16(packet, headerLength + 4))
        if (end <= headerLength + UDP_HEADER) {
            return null
        }
        return Query(
            source = packet.copyOfRange(12, 16),
            sourcePort = u16(packet, headerLength),
            destination = packet.copyOfRange(16, 20),
            message = packet.copyOfRange(headerLength + UDP_HEADER, end),
        )
    }

    /** The IPv4 packet that answers the query with this DNS message, from the address it was sent to */
    fun replyOf(query: Query, message: ByteArray): ByteArray {
        val packet = ByteArray(IPV4_HEADER + UDP_HEADER + message.size)
        packet[0] = 0x45
        put16(packet, 2, packet.size)
        packet[6] = 0x40
        packet[8] = 64
        packet[9] = UDP.toByte()
        query.destination.copyInto(packet, 12)
        query.source.copyInto(packet, 16)
        put16(packet, 10, checksum(packet, IPV4_HEADER))
        put16(packet, IPV4_HEADER, PORT)
        put16(packet, IPV4_HEADER + 2, query.sourcePort)
        put16(packet, IPV4_HEADER + 4, UDP_HEADER + message.size)
        // a UDP checksum of 0: none, which IPv4 allows
        message.copyInto(packet, IPV4_HEADER + UDP_HEADER)
        return packet
    }

    /** The internet checksum of the first length bytes */
    fun checksum(bytes: ByteArray, length: Int): Int {
        var sum = 0L
        for (offset in 0 until length - 1 step 2) {
            sum += u16(bytes, offset)
        }
        while (sum shr 16 != 0L) {
            sum = (sum and 0xffff) + (sum shr 16)
        }
        return sum.inv().toInt() and 0xffff
    }
}

/** The local VPN: answers each DNS query of the phone by asking Cloudflare's family DNS. */
class AkhiPhoneFilterService : VpnService() {
    @Volatile
    private var tunnel: ParcelFileDescriptor? = null

    @Volatile
    private var workers: ExecutorService? = null

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        if (intent?.action == AkhiPhoneFilter.ACTION_STOP) {
            close()
            stopSelf()
            return START_NOT_STICKY
        }
        if (tunnel == null && !open()) {
            stopSelf()
            return START_NOT_STICKY
        }
        return START_STICKY
    }

    private fun open(): Boolean {
        val builder = Builder()
            .setSession("AkhiBrowser")
            .addAddress(TUNNEL_ADDRESS, ADDRESS_BITS)
            .addDnsServer(DNS_ADDRESS)
            .addRoute(DNS_ADDRESS, ADDRESS_BITS)
            .setBlocking(true)
        // a VPN is metered by default since Android 10: Wi-Fi would stop counting as Wi-Fi for updates and backups
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
            builder.setMetered(false)
        }
        val established = builder.establish() ?: return false
        // its own threads for each tunnel, with a bounded queue: a query that waits too long is dropped
        val pool = ThreadPoolExecutor(
            WORKERS,
            WORKERS,
            KEEP_ALIVE_S,
            TimeUnit.SECONDS,
            LinkedBlockingQueue(MAX_QUEUED),
            ThreadPoolExecutor.DiscardOldestPolicy(),
        )
        tunnel = established
        workers = pool
        AkhiPhoneFilter.isRunning = true
        Thread({ read(established, pool) }, "AkhiPhoneFilter").start()
        return true
    }

    private fun read(established: ParcelFileDescriptor, pool: ExecutorService) {
        val input = FileInputStream(established.fileDescriptor)
        val output = FileOutputStream(established.fileDescriptor)
        val buffer = ByteArray(MAX_PACKET)
        try {
            while (tunnel === established) {
                val length = input.read(buffer)
                if (length < 0) {
                    break
                }
                val query = AkhiDns.queryOf(buffer, length) ?: continue
                pool.execute { answer(query, output) }
            }
        } catch (e: IOException) {
            // the tunnel was closed
        } catch (e: RejectedExecutionException) {
            // the tunnel was closed while a query came in
        }
    }

    private fun answer(query: AkhiDns.Query, output: FileOutputStream) {
        val reply = UPSTREAMS.firstNotNullOfOrNull { ask(it, query.message) } ?: return
        synchronized(output) {
            try {
                output.write(AkhiDns.replyOf(query, reply))
            } catch (e: IOException) {
                // the tunnel was closed meanwhile
            }
        }
    }

    // a socket kept out of the VPN, to Cloudflare's family DNS by its address
    private fun ask(server: String, message: ByteArray): ByteArray? = try {
        DatagramSocket().use { socket ->
            protect(socket)
            socket.soTimeout = TIMEOUT_MS
            socket.send(DatagramPacket(message, message.size, InetAddress.getByName(server), AkhiDns.PORT))
            val buffer = ByteArray(MAX_ANSWER)
            val response = DatagramPacket(buffer, buffer.size)
            socket.receive(response)
            buffer.copyOf(response.length)
        }
    } catch (e: IOException) {
        null
    }

    private fun close() {
        AkhiPhoneFilter.isRunning = false
        workers?.shutdownNow()
        workers = null
        try {
            tunnel?.close()
        } catch (e: IOException) {
            // already closed
        }
        tunnel = null
    }

    // turned off in Android's VPN settings, or another VPN took over: still wanted, so the parent report tells
    override fun onRevoke() {
        close()
        super.onRevoke()
    }

    override fun onDestroy() {
        close()
        super.onDestroy()
    }

    private companion object {
        const val TUNNEL_ADDRESS = "10.111.222.1"
        const val DNS_ADDRESS = "10.111.222.2"
        const val ADDRESS_BITS = 32
        val UPSTREAMS = listOf("1.1.1.3", "1.0.0.3")
        const val MAX_PACKET = 32767
        const val MAX_ANSWER = 4096
        const val TIMEOUT_MS = 2000
        const val WORKERS = 8
        const val MAX_QUEUED = 64
        const val KEEP_ALIVE_S = 30L
    }
}

/** Asks Android once whether AkhiBrowser may set up its VPN, then starts it. */
class AkhiPhoneFilterActivity : Activity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val consent = VpnService.prepare(this)
        if (consent == null) {
            done(true)
        } else {
            @Suppress("DEPRECATION") // the Activity Result API needs a ComponentActivity
            startActivityForResult(consent, REQUEST)
        }
    }

    @Deprecated("Its replacement needs a ComponentActivity")
    @Suppress("OVERRIDE_DEPRECATION")
    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        done(resultCode == RESULT_OK)
    }

    private fun done(isAllowed: Boolean) {
        if (isAllowed) {
            AkhiPhoneFilter.start(this)
        } else {
            AkhiPhoneFilter.setWanted(this, false)
        }
        finish()
    }

    private companion object {
        const val REQUEST = 1
    }
}
