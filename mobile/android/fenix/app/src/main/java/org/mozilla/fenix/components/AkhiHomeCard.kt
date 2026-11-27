/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package org.mozilla.fenix.components

import android.Manifest
import android.content.Context
import android.hardware.GeomagneticField
import android.hardware.Sensor
import android.hardware.SensorEvent
import android.hardware.SensorEventListener
import android.hardware.SensorManager
import android.os.Build
import androidx.compose.foundation.Canvas
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
import androidx.compose.material3.Button
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.TextButton
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.DisposableEffect
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.produceState
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.rotate
import androidx.compose.ui.graphics.Path
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.semantics
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
import org.mozilla.fenix.ext.isDefaultBrowserPromptSupported
import org.mozilla.fenix.ext.openSetDefaultBrowserOption
import java.time.LocalDate
import kotlin.math.roundToInt

/**
 * The prayer times and the verse of the day on the home screen. The built-in extension works them out and sends them
 * (lib/home_card.js) whenever its settings change; they're kept for when the browser starts without it.
 */
internal object AkhiHomeCard {
    const val NATIVE_APP = "akhiHomeCard"

    private const val PREFERENCES = "akhi"
    private const val CONTENT = "home_card"
    private const val WELCOME_DONE = "welcome_done"
    private const val NOTIFICATIONS_ASKED = "prayer_notifications_asked"
    private const val NOTIFICATIONS_REQUEST = 7314
    private const val YOUTUBE = "https://m.youtube.com/"
    private const val MINUTE_MS = 60_000L
    private const val COLLAPSED_VERSE_LINES = 3
    private const val FULL_TURN = 360f
    private const val HALF_TURN = 180f

    // how much of each compass reading is taken, so the arrow turns smoothly instead of trembling
    private const val COMPASS_SMOOTHING = 0.15f

    private val content = MutableStateFlow<String?>(null)
    private var isLoaded = false

    /** Receives what the extension sends. */
    class Messages(context: Context) : MessageHandler {
        private val appContext = context.applicationContext

        override fun onMessage(message: Any, source: EngineSession?): Any {
            val text = message.toString()
            appContext.getSharedPreferences(PREFERENCES, Context.MODE_PRIVATE).edit().putString(CONTENT, text).apply()
            content.value = text
            AkhiPrayerReminder.schedule(appContext, text)
            AkhiWeeklySummary.schedule(appContext, text)
            AkhiPrayerWidget.update(appContext)
            return JSONObject().put("ok", true)
        }
    }

    /**
     * AkhiBrowser's language as the extension last sent it ("nl", "ar", "en-US"...): its language setting, else the
     * browser's. Null before the extension or the home screen has sent or loaded it.
     */
    fun language(): String? =
        content.value
            ?.let { runCatching { JSONObject(it).optString("language") }.getOrNull() }
            ?.takeIf { it.isNotEmpty() }

    private fun load(context: Context) {
        if (!isLoaded) {
            isLoaded = true
            if (content.value == null) {
                content.value = context.getSharedPreferences(PREFERENCES, Context.MODE_PRIVATE).getString(CONTENT, null)
            }
            AkhiPrayerReminder.schedule(context, content.value)
            AkhiWeeklySummary.schedule(context, content.value)
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
        card.optJSONObject("welcome")?.let { Welcome(it, modifier) }
        // the weekly summary asks only once a week has something to show, not at the first start
        if (card.optBoolean("reminder") || AkhiWeeklySummary.hasSomething(text)) {
            AskNotifications()
        }
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
            card.optJSONObject("qibla")?.let { qibla ->
                Qibla(
                    title = card.optString("qiblaTitle"),
                    fromNorth = card.optString("qiblaFromNorth"),
                    bearing = qibla.getDouble("bearing").toFloat(),
                    latitude = qibla.getDouble("lat"),
                    longitude = qibla.getDouble("lon"),
                )
            }
            if (verse != null) {
                Verse(card.getString("verseTitle"), verse) { open(null) }
            }
        }
    }

    private fun openTab(context: Context, url: String) {
        val activity = context.asActivity() as? HomeActivity ?: return
        activity.components.useCases.tabsUseCases.selectOrAddTab(
            url = url,
            private = activity.components.appStore.state.mode.isPrivate,
        )
        activity.openToBrowser(BrowserDirection.FromHome)
    }

    private fun needsNotificationPermission(context: Context) =
        Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU && !AkhiPrayerReminder.canNotify(context)

    private fun askNotificationPermission(context: Context) {
        val activity = context.asActivity() ?: return
        if (needsNotificationPermission(activity)) {
            activity.requestPermissions(arrayOf(Manifest.permission.POST_NOTIFICATIONS), NOTIFICATIONS_REQUEST)
        }
    }

    /**
     * Asks once for the notifications of the prayer reminder and the weekly summary, when one of them is on and Android
     * 13 or later doesn't allow them.
     */
    @Composable
    private fun AskNotifications() {
        val context = LocalContext.current
        LaunchedEffect(Unit) {
            val preferences = context.getSharedPreferences(PREFERENCES, Context.MODE_PRIVATE)
            if (needsNotificationPermission(context) && !preferences.getBoolean(NOTIFICATIONS_ASKED, false)) {
                preferences.edit().putBoolean(NOTIFICATIONS_ASKED, true).apply()
                askNotificationPermission(context)
            }
        }
    }

    /**
     * After a new install, what's on and where to start, until it's closed: YouTube without its music, AkhiBrowser as
     * the default browser so links from other apps open filtered, and the prayer times with their reminder.
     *
     * @param texts The welcome texts of the extension's language (lib/home_card.js).
     */
    @Composable
    private fun Welcome(texts: JSONObject, modifier: Modifier) {
        val context = LocalContext.current
        val preferences = remember { context.getSharedPreferences(PREFERENCES, Context.MODE_PRIVATE) }
        var isDone by remember { mutableStateOf(preferences.getBoolean(WELCOME_DONE, false)) }
        if (isDone) {
            return
        }
        val canAskDefault = remember { context.isDefaultBrowserPromptSupported() }
        Column(
            modifier = modifier
                .fillMaxWidth()
                .background(MaterialTheme.colorScheme.surfaceBright, RoundedCornerShape(16.dp))
                .padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(8.dp),
        ) {
            Text(
                text = texts.optString("welcomeTitle"),
                style = MaterialTheme.typography.titleMedium,
                color = MaterialTheme.colorScheme.onSurface,
            )
            Text(
                text = texts.optString("welcomeIntro"),
                style = MaterialTheme.typography.bodyMedium,
                color = MaterialTheme.colorScheme.onSurfaceVariant,
            )
            listOf("welcomeBlock", "welcomeBlur", "welcomeMusic", "welcomeAds").forEach { key ->
                Text(
                    text = "✓  ${texts.optString(key)}",
                    style = MaterialTheme.typography.bodyMedium,
                    color = MaterialTheme.colorScheme.onSurface,
                )
            }
            Button(onClick = { openTab(context, YOUTUBE) }, modifier = Modifier.fillMaxWidth()) {
                Text(texts.optString("welcomeYoutube"))
            }
            if (canAskDefault) {
                Button(
                    onClick = {
                        (context.asActivity() as? HomeActivity)?.openSetDefaultBrowserOption(
                            from = BrowserDirection.FromHome,
                        )
                    },
                    modifier = Modifier.fillMaxWidth(),
                ) {
                    Text(texts.optString("welcomeDefault"))
                }
                Text(
                    text = texts.optString("welcomeDefaultWhy"),
                    style = MaterialTheme.typography.bodySmall,
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                )
            }
            Button(
                onClick = {
                    askNotificationPermission(context)
                    val activity = context.asActivity() as? HomeActivity
                    if (activity != null && openSettings(activity, "prayer")) {
                        activity.openToBrowser(BrowserDirection.FromHome)
                    }
                },
                modifier = Modifier.fillMaxWidth(),
            ) {
                Text(texts.optString("welcomePrayer"))
            }
            TextButton(
                onClick = {
                    preferences.edit().putBoolean(WELCOME_DONE, true).apply()
                    isDone = true
                },
                modifier = Modifier.align(Alignment.End),
            ) {
                Text(texts.optString("welcomeDone"))
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

    /**
     * The phone's heading from true north in degrees, from its rotation sensor, while the card is shown; null on a
     * phone without one. Corrected for the magnetic declination of the prayer city.
     */
    @Composable
    private fun rememberHeading(latitude: Double, longitude: Double): Float? {
        val context = LocalContext.current
        val heading = remember { mutableStateOf<Float?>(null) }
        DisposableEffect(latitude, longitude) {
            val sensors = context.getSystemService(Context.SENSOR_SERVICE) as? SensorManager
            val sensor = sensors?.getDefaultSensor(Sensor.TYPE_ROTATION_VECTOR)
            val declination = GeomagneticField(
                latitude.toFloat(),
                longitude.toFloat(),
                0f,
                System.currentTimeMillis(),
            ).declination
            val rotation = FloatArray(9)
            val orientation = FloatArray(3)
            val listener = object : SensorEventListener {
                override fun onSensorChanged(event: SensorEvent) {
                    SensorManager.getRotationMatrixFromVector(rotation, event.values)
                    SensorManager.getOrientation(rotation, orientation)
                    val reading = (Math.toDegrees(orientation[0].toDouble()).toFloat() + declination + FULL_TURN) % FULL_TURN
                    val last = heading.value
                    heading.value = if (last == null) {
                        reading
                    } else {
                        // the short way round, so 359° to 1° doesn't spin the arrow
                        val change = ((reading - last + HALF_TURN + FULL_TURN) % FULL_TURN) - HALF_TURN
                        (last + change * COMPASS_SMOOTHING + FULL_TURN) % FULL_TURN
                    }
                }

                override fun onAccuracyChanged(sensor: Sensor?, accuracy: Int) = Unit
            }
            if (sensor != null) {
                sensors.registerListener(listener, sensor, SensorManager.SENSOR_DELAY_UI)
            }
            onDispose { sensors?.unregisterListener(listener) }
        }
        return heading.value
    }

    /**
     * The direction of the Kaaba from the prayer city: an arrow that points to it as the phone turns, or, without a
     * compass, its angle from north.
     */
    @Composable
    private fun Qibla(title: String, fromNorth: String, bearing: Float, latitude: Double, longitude: Double) {
        val heading = rememberHeading(latitude, longitude)
        val arrowColor = MaterialTheme.colorScheme.primary
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .semantics(mergeDescendants = true) { contentDescription = "$title · $fromNorth" },
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.spacedBy(8.dp),
        ) {
            Canvas(
                modifier = Modifier
                    .size(24.dp)
                    .rotate(bearing - (heading ?: 0f)),
            ) {
                val arrow = Path().apply {
                    moveTo(size.width / 2, 0f)
                    lineTo(size.width * 0.85f, size.height)
                    lineTo(size.width / 2, size.height * 0.72f)
                    lineTo(size.width * 0.15f, size.height)
                    close()
                }
                drawPath(arrow, arrowColor)
            }
            Text(
                text = "$title · ${if (heading == null) fromNorth else "${bearing.roundToInt()}°"}",
                style = MaterialTheme.typography.titleSmall,
                color = MaterialTheme.colorScheme.onSurface,
                maxLines = 1,
                overflow = TextOverflow.Ellipsis,
            )
        }
    }

}
