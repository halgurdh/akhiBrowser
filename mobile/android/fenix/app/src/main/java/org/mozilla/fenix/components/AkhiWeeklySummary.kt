/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package org.mozilla.fenix.components

import android.app.AlarmManager
import android.app.Notification
import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.PendingIntent
import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import org.json.JSONObject
import org.mozilla.fenix.R
import java.time.DayOfWeek
import java.time.LocalDate
import java.time.LocalTime
import java.time.ZoneId
import java.time.ZonedDateTime
import java.time.temporal.TemporalAdjusters

/**
 * The weekly summary of the settings (weeklySummary), also while the browser is closed: on Sunday evening, how many
 * unsafe pages were blocked in the last seven days. The built-in extension counts them per day on the device and sends
 * the counts with the home screen card (lib/home_card.js, lib/weekly.js); nothing is shown in a week without any.
 */
internal object AkhiWeeklySummary {
    private const val PREFERENCES = "akhi"
    private const val CONTENT = "home_card"
    private const val CHANNEL = "akhi_weekly"
    private const val NOTIFICATION_ID = 7315
    private const val REQUEST_CODE = 7315
    private const val WEEK_DAYS = 7
    private const val HOUR = 18

    /** The pages blocked in the [WEEK_DAYS] days up to [today], its epoch day, from [counts] by epoch day. */
    fun weekTotal(counts: Map<Long, Int>, today: Long): Int =
        counts.filterKeys { it > today - WEEK_DAYS && it <= today }.values.sum()

    /** The next Sunday at [HOUR]:00 after [now], in its time zone. */
    fun nextTime(now: ZonedDateTime): ZonedDateTime {
        val thisWeek = now.with(TemporalAdjusters.nextOrSame(DayOfWeek.SUNDAY)).with(LocalTime.of(HOUR, 0))
        return if (thisWeek.isAfter(now)) thisWeek else thisWeek.plusWeeks(1)
    }

    private fun weeklyOf(cardText: String?): JSONObject? =
        cardText?.let { runCatching { JSONObject(it).optJSONObject("weekly") }.getOrNull() }

    private fun countsOf(weekly: JSONObject): Map<Long, Int> {
        val days = weekly.optJSONObject("days") ?: return emptyMap()
        return days.keys().asSequence()
            .mapNotNull { day -> day.toLongOrNull()?.let { it to days.optInt(day) } }
            .toMap()
    }

    private fun alarmIntent(context: Context): PendingIntent =
        PendingIntent.getBroadcast(
            context,
            REQUEST_CODE,
            Intent(context, AkhiWeeklySummaryAlarm::class.java),
            PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE,
        )

    /** Sets the alarm of the next Sunday when the summary is on in [cardText], the card the extension sent, or clears it. */
    fun schedule(context: Context, cardText: String?) {
        val appContext = context.applicationContext
        val alarms = appContext.getSystemService(AlarmManager::class.java) ?: return
        if (weeklyOf(cardText)?.optBoolean("on") != true) {
            alarms.cancel(alarmIntent(appContext))
            return
        }
        val at = nextTime(ZonedDateTime.now(ZoneId.systemDefault())).toInstant().toEpochMilli()
        // inexact but allowed while the phone dozes, and without the exact alarm permission
        alarms.setAndAllowWhileIdle(AlarmManager.RTC_WAKEUP, at, alarmIntent(appContext))
    }

    /** Sets the alarm again from the card kept on the phone: after a restart of the phone. */
    fun reschedule(context: Context) {
        schedule(context, context.getSharedPreferences(PREFERENCES, Context.MODE_PRIVATE).getString(CONTENT, null))
    }

    /** Whether the summary has something to show: it's on and the week has blocked pages. */
    fun hasSomething(cardText: String?): Boolean {
        val weekly = weeklyOf(cardText) ?: return false
        return weekly.optBoolean("on") && weekTotal(countsOf(weekly), LocalDate.now().toEpochDay()) > 0
    }

    internal fun show(context: Context) {
        val cardText = context.getSharedPreferences(PREFERENCES, Context.MODE_PRIVATE).getString(CONTENT, null)
        val weekly = weeklyOf(cardText)
        val total = weekly?.let { weekTotal(countsOf(it), LocalDate.now().toEpochDay()) } ?: 0
        if (weekly != null && weekly.optBoolean("on") && total > 0 && AkhiPrayerReminder.canNotify(context)) {
            val manager = context.getSystemService(NotificationManager::class.java)
            manager.createNotificationChannel(
                NotificationChannel(
                    CHANNEL,
                    weekly.optString("channel").ifEmpty { "AkhiBrowser" },
                    NotificationManager.IMPORTANCE_LOW,
                ),
            )
            val open = context.packageManager.getLaunchIntentForPackage(context.packageName)?.let {
                PendingIntent.getActivity(context, REQUEST_CODE, it, PendingIntent.FLAG_IMMUTABLE)
            }
            val notification = Notification.Builder(context, CHANNEL)
                .setSmallIcon(R.drawable.ic_status_logo)
                .setContentTitle(weekly.optString("title").ifEmpty { "AkhiBrowser" })
                .setContentText(weekly.optString("text").replace("{count}", total.toString()))
                .setAutoCancel(true)
                .apply { if (open != null) setContentIntent(open) }
                .build()
            manager.notify(NOTIFICATION_ID, notification)
        }
        schedule(context, cardText)
    }
}

/** The alarm on Sunday evening (AkhiWeeklySummary). */
class AkhiWeeklySummaryAlarm : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        AkhiWeeklySummary.show(context)
    }
}
