/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package org.mozilla.fenix.components

import android.Manifest
import android.app.AlarmManager
import android.app.Notification
import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.PendingIntent
import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.content.pm.PackageManager
import android.os.Build
import org.json.JSONObject
import org.mozilla.fenix.R

/**
 * The prayer reminder of the settings (prayerReminder), also while the browser is closed: the built-in extension sends
 * two weeks of prayer times with the home screen card (lib/home_card.js), and an alarm at the next one shows its
 * notification and sets the one after. The extension itself doesn't remind on Android (background.js).
 */
internal object AkhiPrayerReminder {
    private const val PREFERENCES = "akhi"
    private const val CONTENT = "home_card"
    private const val CHANNEL = "akhi_prayer"
    private const val NOTIFICATION_ID = 7313
    private const val REQUEST_CODE = 7313
    private const val EXTRA_AT = "at"
    private const val EXTRA_NAME = "name"
    private const val EXTRA_TEXT = "text"

    // a reminder that comes later than this (the phone was off) is left out: the prayer has long begun
    private const val LATE_MS = 30 * 60_000L

    private class Next(val at: Long, val name: String, val text: String)

    /** The first prayer after [now] in the card's times, when the reminder is on. */
    private fun next(card: JSONObject, now: Long): Next? {
        if (!card.optBoolean("reminder")) {
            return null
        }
        val days = card.optJSONArray("days") ?: return null
        for (d in 0 until days.length()) {
            val day = days.getJSONArray(d)
            for (t in 0 until day.length()) {
                val time = day.getJSONObject(t)
                val at = time.getLong("at")
                if (at > now) {
                    return Next(at, time.getString("name"), time.optString("text", time.getString("name")))
                }
            }
        }
        return null
    }

    private fun alarmIntent(context: Context, next: Next?): PendingIntent {
        val intent = Intent(context, AkhiPrayerReminderAlarm::class.java)
        if (next != null) {
            intent.putExtra(EXTRA_AT, next.at).putExtra(EXTRA_NAME, next.name).putExtra(EXTRA_TEXT, next.text)
        }
        return PendingIntent.getBroadcast(
            context,
            REQUEST_CODE,
            intent,
            PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE,
        )
    }

    /** Sets the alarm of the next prayer from [cardText], the card the extension sent, or clears it. */
    fun schedule(context: Context, cardText: String?) {
        val appContext = context.applicationContext
        val alarms = appContext.getSystemService(AlarmManager::class.java) ?: return
        val card = cardText?.let { runCatching { JSONObject(it) }.getOrNull() }
        val next = card?.let { next(it, System.currentTimeMillis()) }
        if (next == null) {
            alarms.cancel(alarmIntent(appContext, null))
            return
        }
        // inexact but allowed while the phone dozes, and without the exact alarm permission: a few minutes late at most
        alarms.setAndAllowWhileIdle(AlarmManager.RTC_WAKEUP, next.at, alarmIntent(appContext, next))
    }

    /** Sets the alarm again from the card kept on the phone: after a restart of the phone. */
    fun reschedule(context: Context) {
        schedule(
            context,
            context.getSharedPreferences(PREFERENCES, Context.MODE_PRIVATE).getString(CONTENT, null),
        )
    }

    /** Whether the reminder's notifications may show: asked for from Android 13. */
    fun canNotify(context: Context): Boolean =
        Build.VERSION.SDK_INT < Build.VERSION_CODES.TIRAMISU ||
            context.checkSelfPermission(Manifest.permission.POST_NOTIFICATIONS) == PackageManager.PERMISSION_GRANTED

    internal fun remind(context: Context, intent: Intent) {
        val at = intent.getLongExtra(EXTRA_AT, 0L)
        val name = intent.getStringExtra(EXTRA_NAME)
        val text = intent.getStringExtra(EXTRA_TEXT)
        if (name != null && text != null && System.currentTimeMillis() - at < LATE_MS && canNotify(context)) {
            val manager = context.getSystemService(NotificationManager::class.java)
            val title = context.getSharedPreferences(PREFERENCES, Context.MODE_PRIVATE).getString(CONTENT, null)
                ?.let { runCatching { JSONObject(it).optString("prayerTitle") }.getOrNull() }
                ?.takeIf { it.isNotEmpty() }
                ?: "AkhiBrowser"
            manager.createNotificationChannel(
                NotificationChannel(CHANNEL, title, NotificationManager.IMPORTANCE_DEFAULT),
            )
            val open = context.packageManager.getLaunchIntentForPackage(context.packageName)?.let {
                PendingIntent.getActivity(context, REQUEST_CODE, it, PendingIntent.FLAG_IMMUTABLE)
            }
            val notification = Notification.Builder(context, CHANNEL)
                .setSmallIcon(R.drawable.ic_status_logo)
                .setContentTitle(name)
                .setContentText(text)
                .setAutoCancel(true)
                .apply { if (open != null) setContentIntent(open) }
                .build()
            manager.notify(NOTIFICATION_ID, notification)
        }
        reschedule(context)
    }
}

/** The alarm at a prayer time (AkhiPrayerReminder). */
class AkhiPrayerReminderAlarm : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        AkhiPrayerReminder.remind(context, intent)
    }
}
