/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package org.mozilla.fenix.components

import android.content.Context
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.produceState
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.MutableStateFlow
import mozilla.components.concept.engine.EngineSession
import mozilla.components.concept.engine.webextension.MessageHandler
import org.json.JSONArray
import org.json.JSONObject
import org.mozilla.fenix.BrowserDirection
import org.mozilla.fenix.HomeActivity
import org.mozilla.fenix.R
import org.mozilla.fenix.ext.asActivity
import org.mozilla.fenix.ext.components
import java.time.LocalDate

/**
 * The prayer times and the verse of the day on the home screen. The built-in extension works them out and sends them
 * (lib/home_card.js) whenever its settings change; they're kept for when the browser starts without it.
 */
internal object AkhiHomeCard {
    const val NATIVE_APP = "akhiHomeCard"

    private const val PREFERENCES = "akhi"
    private const val CONTENT = "home_card"
    private const val MINUTE_MS = 60_000L
    private const val COLLAPSED_VERSE_LINES = 3

    private val content = MutableStateFlow<String?>(null)
    private var isLoaded = false

    /** Receives what the extension sends. */
    class Messages(context: Context) : MessageHandler {
        private val appContext = context.applicationContext

        override fun onMessage(message: Any, source: EngineSession?): Any {
            val text = message.toString()
            appContext.getSharedPreferences(PREFERENCES, Context.MODE_PRIVATE).edit().putString(CONTENT, text).apply()
            content.value = text
            return JSONObject().put("ok", true)
        }
    }

    private fun load(context: Context) {
        if (!isLoaded) {
            isLoaded = true
            if (content.value == null) {
                content.value = context.getSharedPreferences(PREFERENCES, Context.MODE_PRIVATE).getString(CONTENT, null)
            }
        }
    }

    /**
     * Opens AkhiBrowser's settings page in a tab, at [section] (a group of settings.html) when given. The home screen
     * has no tab for the extension's popup, so its card and menu open the page itself.
     *
     * @return false while the extension hasn't sent the page's address yet.
     */
    fun openSettings(context: Context, section: String? = null): Boolean {
        load(context)
        val url = content.value
            ?.let { runCatching { JSONObject(it).optString("settingsUrl") }.getOrNull() }
            ?.takeIf { it.isNotEmpty() }
            ?: return false
        context.components.useCases.tabsUseCases.selectOrAddTab(
            url = if (section != null) "$url#$section" else url,
            private = context.components.appStore.state.mode.isPrivate,
            ignoreFragment = true,
        )
        return true
    }

    private class Time(val name: String, val label: String, val at: Long)

    private fun List<JSONObject>.toTimes() = map { Time(it.getString("name"), it.getString("label"), it.getLong("at")) }

    private fun JSONArray.objects() = (0 until length()).map { getJSONObject(it) }

    /** The times of the day with the next prayer, the first one still to come. */
    private fun currentDay(card: JSONObject, now: Long): List<Time>? {
        val days = card.getJSONArray("days")
        return (0 until days.length())
            .map { days.getJSONArray(it).objects().toTimes() }
            .firstOrNull { day -> day.any { it.at > now } }
    }

    private fun currentVerse(card: JSONObject): JSONObject? {
        val today = LocalDate.now().toEpochDay()
        return card.getJSONArray("verses").objects().firstOrNull { it.getLong("day") == today }
    }

    /**
     * Nothing when there's neither a city nor a verse.
     *
     * @param modifier The padding of the home screen.
     */
    @Composable
    fun Card(modifier: Modifier = Modifier) {
        val context = LocalContext.current
        val text by remember {
            load(context)
            content
        }.collectAsState()
        val now by produceState(System.currentTimeMillis()) {
            while (true) {
                delay(MINUTE_MS)
                value = System.currentTimeMillis()
            }
        }
        val card = remember(text) { text?.let { runCatching { JSONObject(it) }.getOrNull() } } ?: return
        val day = currentDay(card, now)
        val verse = currentVerse(card)
        if (day == null && verse == null) {
            return
        }
        Column(
            modifier = modifier
                .fillMaxWidth()
                .background(MaterialTheme.colorScheme.surfaceBright, RoundedCornerShape(16.dp))
                .padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(12.dp),
        ) {
            val open = { section: String? ->
                val activity = context.asActivity() as? HomeActivity
                if (activity != null && openSettings(activity, section)) {
                    activity.openToBrowser(BrowserDirection.FromHome)
                }
            }
            if (day != null) {
                Times(card.getString("prayerTitle"), card.getString("city"), day, now) { open("prayer") }
            }
            if (verse != null) {
                Verse(card.getString("verseTitle"), verse) { open(null) }
            }
        }
    }

    @Composable
    private fun Title(icon: Int, text: String) {
        Row(verticalAlignment = Alignment.CenterVertically, horizontalArrangement = Arrangement.spacedBy(8.dp)) {
            Image(painterResource(icon), contentDescription = null, modifier = Modifier.size(24.dp))
            Text(
                text = text,
                style = MaterialTheme.typography.titleSmall,
                color = MaterialTheme.colorScheme.onSurface,
                maxLines = 1,
                overflow = TextOverflow.Ellipsis,
            )
        }
    }

    /** A tap opens the prayer times in the extension's settings. */
    @Composable
    private fun Times(title: String, city: String, day: List<Time>, now: Long, onClick: () -> Unit) {
        Column(
            modifier = Modifier
                .fillMaxWidth()
                .clickable(onClick = onClick),
            verticalArrangement = Arrangement.spacedBy(8.dp),
        ) {
            Title(R.drawable.akhi_salah_mosque, "$title · $city")
            val next = day.firstOrNull { it.at > now }
            Row(modifier = Modifier.fillMaxWidth()) {
                day.forEach { time ->
                    val isNext = time === next
                    val color = if (isNext) MaterialTheme.colorScheme.primary else MaterialTheme.colorScheme.onSurface
                    val weight = if (isNext) FontWeight.Bold else FontWeight.Normal
                    Column(modifier = Modifier.weight(1f), horizontalAlignment = Alignment.CenterHorizontally) {
                        Text(
                            text = time.name,
                            style = MaterialTheme.typography.labelSmall,
                            color = color,
                            fontWeight = weight,
                            maxLines = 1,
                            overflow = TextOverflow.Ellipsis,
                        )
                        Text(
                            text = time.label,
                            style = MaterialTheme.typography.bodyMedium,
                            color = color,
                            fontWeight = weight,
                            maxLines = 1,
                        )
                    }
                }
            }
        }
    }

    /** A tap opens the settings, which show the whole verse with its Arabic: the Quran is never left cut off. */
    @Composable
    private fun Verse(title: String, verse: JSONObject, onClick: () -> Unit) {
        Column(
            modifier = Modifier
                .fillMaxWidth()
                .clickable(onClick = onClick),
            verticalArrangement = Arrangement.spacedBy(4.dp),
        ) {
            Title(R.drawable.akhi_salah_mushaf, "$title · ${verse.getString("ref")}")
            Text(
                text = verse.getString("meaning"),
                style = MaterialTheme.typography.bodyMedium,
                color = MaterialTheme.colorScheme.onSurfaceVariant,
                maxLines = COLLAPSED_VERSE_LINES,
                overflow = TextOverflow.Ellipsis,
            )
        }
    }
}
