/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package org.mozilla.fenix.components

import android.app.AlarmManager
import android.app.PendingIntent
import android.appwidget.AppWidgetManager
import android.appwidget.AppWidgetProvider
import android.content.ComponentName
import android.content.Context
import android.content.Intent
import android.view.View
import android.widget.RemoteViews
import org.json.JSONObject
import org.mozilla.fenix.R

/**
 * The prayer times on the phone's home screen: the next prayer, and the others of its day. They come from the card the
 * built-in extension sends (lib/home_card.js, AkhiHomeCard.kt); the widget changes at each prayer time, and when the
 * card does.
 */
class AkhiPrayerWidget : AppWidgetProvider() {

    /** A prayer of the card: its name, its time as shown, and when it is. */
    data class Prayer(val name: String, val label: String, val at: Long)

    override fun onUpdate(context: Context, appWidgetManager: AppWidgetManager, appWidgetIds: IntArray) {
        update(context)
    }

    override fun onReceive(context: Context, intent: Intent) {
        if (intent.action == ACTION_REFRESH) {
            update(context)
        } else {
            super.onReceive(context, intent)
        }
    }

    override fun onDisabled(context: Context) {
        context.getSystemService(AlarmManager::class.java)?.cancel(refreshIntent(context))
    }

    companion object {
        private const val PREFERENCES = "akhi"
        private const val CONTENT = "home_card"
        private const val ACTION_REFRESH = "org.mozilla.fenix.components.AkhiPrayerWidget.REFRESH"
        private const val REQUEST_CODE = 7316
        private const val SEPARATOR = "  ·  "

        /** The day of [days] with the first prayer after [now], and that prayer; null when none is left. */
        fun nextOf(days: List<List<Prayer>>, now: Long): Pair<List<Prayer>, Prayer>? {
            for (day in days) {
                val next = day.firstOrNull { it.at > now }
                if (next != null) {
                    return day to next
                }
            }
            return null
        }

        private fun daysOf(card: JSONObject): List<List<Prayer>> {
            val days = card.optJSONArray("days") ?: return emptyList()
            return (0 until days.length()).map { d ->
                val day = days.getJSONArray(d)
                (0 until day.length()).map { t ->
                    val time = day.getJSONObject(t)
                    Prayer(time.getString("name"), time.getString("label"), time.getLong("at"))
                }
            }
        }

        private fun refreshIntent(context: Context): PendingIntent =
            PendingIntent.getBroadcast(
                context,
                REQUEST_CODE,
                Intent(context, AkhiPrayerWidget::class.java).setAction(ACTION_REFRESH),
                PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE,
            )

        /** Shows the card kept on the phone in every widget, and sets the refresh at the next prayer. */
        fun update(context: Context) {
            val appContext = context.applicationContext
            val manager = AppWidgetManager.getInstance(appContext) ?: return
            val ids = manager.getAppWidgetIds(ComponentName(appContext, AkhiPrayerWidget::class.java))
            if (ids.isEmpty()) {
                return
            }
            val card = appContext.getSharedPreferences(PREFERENCES, Context.MODE_PRIVATE).getString(CONTENT, null)
                ?.let { runCatching { JSONObject(it) }.getOrNull() }
            val next = card?.let { runCatching { nextOf(daysOf(it), System.currentTimeMillis()) }.getOrNull() }
            val views = RemoteViews(appContext.packageName, R.layout.akhi_prayer_widget)
            val title = card?.optString("prayerTitle").orEmpty().ifEmpty { "AkhiBrowser" }
            val city = card?.optString("city").orEmpty()
            views.setTextViewText(R.id.akhi_widget_title, if (city.isEmpty()) title else "$title · $city")
            if (next != null) {
                val (day, prayer) = next
                views.setTextViewText(R.id.akhi_widget_next, "${prayer.name}  ${prayer.label}")
                views.setTextViewText(R.id.akhi_widget_day, day.joinToString(SEPARATOR) { "${it.name} ${it.label}" })
                views.setViewVisibility(R.id.akhi_widget_day, View.VISIBLE)
            } else {
                views.setTextViewText(
                    R.id.akhi_widget_next,
                    card?.optString("widgetNoCity").orEmpty().ifEmpty { title },
                )
                views.setViewVisibility(R.id.akhi_widget_day, View.GONE)
            }
            appContext.packageManager.getLaunchIntentForPackage(appContext.packageName)?.let {
                views.setOnClickPendingIntent(
                    R.id.akhi_widget,
                    PendingIntent.getActivity(appContext, REQUEST_CODE, it, PendingIntent.FLAG_IMMUTABLE),
                )
            }
            manager.updateAppWidget(ids, views)

            val alarms = appContext.getSystemService(AlarmManager::class.java) ?: return
            if (next != null) {
                alarms.setAndAllowWhileIdle(AlarmManager.RTC, next.second.at + 1000, refreshIntent(appContext))
            } else {
                alarms.cancel(refreshIntent(appContext))
            }
        }
    }
}
