/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package org.mozilla.fenix.components

import android.app.Activity
import android.app.AppOpsManager
import android.app.Notification
import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.Service
import android.app.usage.UsageEvents
import android.app.usage.UsageStatsManager
import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.content.pm.PackageManager
import android.content.pm.ServiceInfo
import android.net.Uri
import android.os.Build
import android.os.Bundle
import android.os.Handler
import android.os.IBinder
import android.os.Looper
import android.os.Process
import android.provider.Settings
import android.view.Gravity
import android.widget.Button
import android.widget.LinearLayout
import android.widget.TextView
import mozilla.components.concept.engine.EngineSession
import mozilla.components.concept.engine.webextension.MessageHandler
import org.json.JSONArray
import org.json.JSONObject
import org.mozilla.fenix.R

/**
 * Family: the apps a parent chose can't be opened, in the APK and on Google Play. The settings are in the extension
 * (pages/family_tools.js), each message is {type, ...}; it asks the parent's PIN before it sends a change.
 */
internal object AkhiAppBlock {
    const val NATIVE_APP = "akhiAppBlock"
    const val NOTIFICATION_ID = 7310

    private const val PREFERENCES = "akhi_app_block"
    private const val BLOCKED = "blocked"
    private const val TEXT = "text"
    private const val OPEN_TEXT = "open"
    private const val CHANNEL = "akhi_app_block"

    fun blocked(context: Context): Set<String> =
        context.getSharedPreferences(PREFERENCES, Context.MODE_PRIVATE).getStringSet(BLOCKED, emptySet()).orEmpty()

    fun text(context: Context): String =
        context.getSharedPreferences(PREFERENCES, Context.MODE_PRIVATE).getString(TEXT, null).orEmpty()

    fun openText(context: Context): String =
        context.getSharedPreferences(PREFERENCES, Context.MODE_PRIVATE).getString(OPEN_TEXT, null).orEmpty()

    /** The website of a blocked app, opened in AkhiBrowser where its images are checked */
    fun siteOf(app: String?): String? = when (app) {
        "com.instagram.android", "com.instagram.lite" -> "https://www.instagram.com/"
        "com.instagram.barcelona" -> "https://www.threads.net/"
        "com.zhiliaoapp.musically", "com.ss.android.ugc.trill", "com.zhiliaoapp.musically.go" ->
            "https://www.tiktok.com/"
        "com.facebook.katana", "com.facebook.lite" -> "https://m.facebook.com/"
        "com.twitter.android" -> "https://x.com/"
        "com.reddit.frontpage" -> "https://www.reddit.com/"
        "com.pinterest" -> "https://www.pinterest.com/"
        "com.tumblr" -> "https://www.tumblr.com/"
        "com.google.android.youtube" -> "https://m.youtube.com/"
        else -> null
    }

    @Suppress("DEPRECATION") // its replacement is newer than our oldest Android
    private fun hasUsageAccess(context: Context): Boolean {
        val appOps = context.getSystemService(AppOpsManager::class.java)
        return appOps.checkOpNoThrow(
            AppOpsManager.OPSTR_GET_USAGE_STATS,
            Process.myUid(),
            context.packageName,
        ) == AppOpsManager.MODE_ALLOWED
    }

    private fun apps(context: Context): JSONArray {
        val launcher = Intent(Intent.ACTION_MAIN).addCategory(Intent.CATEGORY_LAUNCHER)
        val manager = context.packageManager
        val result = JSONArray()
        manager.queryIntentActivities(launcher, PackageManager.MATCH_ALL)
            .map { it.activityInfo.packageName to it.loadLabel(manager).toString() }
            .filter { it.first != context.packageName }
            .distinctBy { it.first }
            .sortedBy { it.second.lowercase() }
            .forEach { (id, label) -> result.put(JSONObject().put("id", id).put("label", label)) }
        return result
    }

    /** Starts the watch when there are apps to block and it's allowed to, stops it otherwise. */
    fun applyWatch(context: Context) {
        val service = Intent(context, AkhiAppBlockService::class.java)
        val canWatch = hasUsageAccess(context) && Settings.canDrawOverlays(context)
        if (blocked(context).isNotEmpty() && canWatch) {
            context.startForegroundService(service)
        } else {
            context.stopService(service)
        }
    }

    fun notification(context: Context): Notification {
        val manager = context.getSystemService(NotificationManager::class.java)
        manager.createNotificationChannel(
            NotificationChannel(CHANNEL, "AkhiBrowser", NotificationManager.IMPORTANCE_MIN),
        )
        return Notification.Builder(context, CHANNEL)
            .setSmallIcon(R.drawable.ic_status_logo)
            .setContentTitle("AkhiBrowser")
            .setContentText(text(context))
            .setOngoing(true)
            .build()
    }

    /** Receives the messages of the settings. */
    class Messages(context: Context) : MessageHandler {
        private val appContext = context.applicationContext

        override fun onMessage(message: Any, source: EngineSession?): Any {
            val request = message as? JSONObject ?: return JSONObject()
            when (request.optString("type")) {
                "set" -> {
                    val list = request.optJSONArray("blocked") ?: JSONArray()
                    appContext.getSharedPreferences(PREFERENCES, Context.MODE_PRIVATE).edit()
                        .putStringSet(BLOCKED, (0 until list.length()).map { list.getString(it) }.toSet())
                        .putString(TEXT, request.optString("text"))
                        .putString(OPEN_TEXT, request.optString("open"))
                        .apply()
                    applyWatch(appContext)
                }
                "usage" -> openSettings(Intent(Settings.ACTION_USAGE_ACCESS_SETTINGS))
                "overlay" -> openSettings(
                    Intent(Settings.ACTION_MANAGE_OVERLAY_PERMISSION, Uri.parse("package:${appContext.packageName}")),
                )
            }
            return JSONObject()
                .put("available", true)
                .put("usage", hasUsageAccess(appContext))
                .put("overlay", Settings.canDrawOverlays(appContext))
                .put("apps", if (request.optString("type") == "status") apps(appContext) else JSONArray())
                .put("blocked", JSONArray(blocked(appContext).toList()))
        }

        private fun openSettings(intent: Intent) {
            appContext.startActivity(intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK))
        }
    }
}

/** Watches which app is in front, and covers a blocked one. */
class AkhiAppBlockService : Service() {
    private val handler = Handler(Looper.getMainLooper())
    private val watch = object : Runnable {
        override fun run() {
            val app = appInFront()
            if (app != null && app in AkhiAppBlock.blocked(this@AkhiAppBlockService)) {
                startActivity(
                    Intent(this@AkhiAppBlockService, AkhiAppBlockActivity::class.java)
                        .putExtra(AkhiAppBlockActivity.EXTRA_APP, app)
                        .addFlags(Intent.FLAG_ACTIVITY_NEW_TASK),
                )
            }
            handler.postDelayed(this, WATCH_EVERY_MS)
        }
    }

    private fun appInFront(): String? {
        val now = System.currentTimeMillis()
        val events = getSystemService(UsageStatsManager::class.java).queryEvents(now - LOOK_BACK_MS, now)
        val event = UsageEvents.Event()
        var app: String? = null
        while (events.hasNextEvent()) {
            events.getNextEvent(event)
            if (event.eventType == UsageEvents.Event.ACTIVITY_RESUMED) {
                app = event.packageName
            }
        }
        return app
    }

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        val notification = AkhiAppBlock.notification(this)
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.UPSIDE_DOWN_CAKE) {
            startForeground(AkhiAppBlock.NOTIFICATION_ID, notification, ServiceInfo.FOREGROUND_SERVICE_TYPE_SPECIAL_USE)
        } else {
            startForeground(AkhiAppBlock.NOTIFICATION_ID, notification)
        }
        handler.removeCallbacks(watch)
        handler.post(watch)
        return START_STICKY
    }

    override fun onDestroy() {
        handler.removeCallbacks(watch)
        super.onDestroy()
    }

    override fun onBind(intent: Intent?): IBinder? = null

    private companion object {
        const val WATCH_EVERY_MS = 1500L
        const val LOOK_BACK_MS = 10_000L
    }
}

/** Shown over a blocked app: the way on is the home screen, or the app's website in AkhiBrowser. */
class AkhiAppBlockActivity : Activity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val padding = (PADDING_DP * resources.displayMetrics.density).toInt()
        val message = TextView(this).apply {
            text = AkhiAppBlock.text(this@AkhiAppBlockActivity)
            textSize = TEXT_SP
            gravity = Gravity.CENTER
        }
        val home = Button(this).apply {
            text = getString(android.R.string.ok)
            setOnClickListener { goHome() }
        }
        val site = AkhiAppBlock.siteOf(intent.getStringExtra(EXTRA_APP))
        val openText = AkhiAppBlock.openText(this)
        setContentView(
            LinearLayout(this).apply {
                orientation = LinearLayout.VERTICAL
                gravity = Gravity.CENTER
                setPadding(padding, padding, padding, padding)
                addView(message)
                if (site != null && openText.isNotEmpty()) {
                    addView(
                        Button(this@AkhiAppBlockActivity).apply {
                            text = openText
                            setOnClickListener { openSite(site) }
                        },
                    )
                }
                addView(home)
            },
        )
    }

    private fun openSite(site: String) {
        startActivity(
            Intent(Intent.ACTION_VIEW, Uri.parse(site))
                .setPackage(packageName)
                .addFlags(Intent.FLAG_ACTIVITY_NEW_TASK),
        )
        finish()
    }

    override fun onNewIntent(intent: Intent) {
        super.onNewIntent(intent)
        setIntent(intent)
        recreate()
    }

    private fun goHome() {
        startActivity(
            Intent(Intent.ACTION_MAIN).addCategory(Intent.CATEGORY_HOME).addFlags(Intent.FLAG_ACTIVITY_NEW_TASK),
        )
        finish()
    }

    @Deprecated("Back goes to the home screen too")
    @Suppress("OVERRIDE_DEPRECATION", "MissingSuperCall")
    override fun onBackPressed() = goHome()

    companion object {
        const val EXTRA_APP = "app"
        private const val PADDING_DP = 32
        private const val TEXT_SP = 20f
    }
}

/** The watch, and the phone filter (AkhiPhoneFilter.kt), again after a restart of the device. */
class AkhiAppBlockBoot : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        if (intent.action == Intent.ACTION_BOOT_COMPLETED) {
            AkhiAppBlock.applyWatch(context)
            AkhiPhoneFilter.startAfterBoot(context)
        }
    }
}
