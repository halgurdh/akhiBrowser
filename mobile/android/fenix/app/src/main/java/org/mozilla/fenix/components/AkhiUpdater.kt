/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package org.mozilla.fenix.components

import android.app.Activity
import android.app.Application
import android.content.ActivityNotFoundException
import android.content.Context
import android.content.Intent
import android.content.SharedPreferences
import android.content.pm.PackageInfo
import android.content.pm.PackageManager
import android.content.pm.Signature
import android.os.Build
import android.os.Bundle
import androidx.appcompat.app.AlertDialog
import androidx.core.content.FileProvider
import androidx.core.content.edit
import androidx.lifecycle.LifecycleOwner
import androidx.lifecycle.lifecycleScope
import androidx.work.Constraints
import androidx.work.CoroutineWorker
import androidx.work.ExistingPeriodicWorkPolicy
import androidx.work.NetworkType
import androidx.work.PeriodicWorkRequestBuilder
import androidx.work.WorkManager
import androidx.work.WorkerParameters
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.currentCoroutineContext
import kotlinx.coroutines.ensureActive
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import mozilla.components.support.base.log.logger.Logger
import org.json.JSONObject
import org.mozilla.fenix.BuildConfig
import org.mozilla.fenix.HomeActivity
import org.mozilla.fenix.R
import java.io.File
import java.io.FileOutputStream
import java.io.IOException
import java.net.HttpURLConnection
import java.net.URL
import java.security.MessageDigest
import java.util.concurrent.TimeUnit

/**
 * Keeps an APK from GitHub up to date. Once a day, on an unmetered network, a newer release is downloaded and checked
 * against the release's SHA256SUMS.txt and this app's signing key. The app then offers to install it, and Android asks
 * the user to confirm. A Google Play build leaves this to Play.
 */
object AkhiUpdater {
    internal const val PREFERENCES = "akhi_updates"
    internal const val READY_VERSION = "ready_version"
    internal const val READY_FILE = "ready_file"
    internal const val SNOOZED_UNTIL = "snoozed_until"
    internal const val UPDATES_FOLDER = "updates"

    private const val WORK_NAME = "akhi_update_check"
    private const val CHECK_EVERY_DAYS = 1L
    private const val SNOOZE_MS = 24 * 60 * 60 * 1000L

    private val logger = Logger("akhi-updater")

    /** Whether [version] (a.b.c, with or without a leading v) is newer than [than]. False for anything else. */
    fun isNewer(version: String, than: String): Boolean {
        val parts = { text: String ->
            Regex("""^v?(\d+)\.(\d+)\.(\d+)$""").find(text)?.destructured?.toList()?.map { it.toLongOrNull() }
        }
        val first = parts(version) ?: return false
        val second = parts(than) ?: return false
        if (first.any { it == null } || second.any { it == null }) {
            return false
        }
        val index = first.indices.firstOrNull { first[it] != second[it] } ?: return false
        return first[index]!! > second[index]!!
    }

    /** The hash of [fileName] in the text of a SHA256SUMS.txt, in lower case. */
    fun checksumOf(sums: String, fileName: String): String? =
        sums.lineSequence()
            .map { it.trim().split(Regex("""\s+"""), limit = 2) }
            .firstOrNull { it.size == 2 && it[1].removePrefix("*") == fileName }
            ?.get(0)
            ?.lowercase()

    fun start(application: Application) {
        if (BuildConfig.AKHI_PLAY_STORE) {
            return
        }
        val constraints = Constraints.Builder()
            .setRequiredNetworkType(NetworkType.UNMETERED)
            .setRequiresBatteryNotLow(true)
            .setRequiresStorageNotLow(true)
            .build()
        val work = PeriodicWorkRequestBuilder<AkhiUpdateWorker>(CHECK_EVERY_DAYS, TimeUnit.DAYS)
            .setConstraints(constraints)
            .build()
        WorkManager.getInstance(application)
            .enqueueUniquePeriodicWork(WORK_NAME, ExistingPeriodicWorkPolicy.KEEP, work)
        application.registerActivityLifecycleCallbacks(OfferOnResume())
    }

    private class OfferOnResume : Application.ActivityLifecycleCallbacks {
        private var dialog: AlertDialog? = null

        override fun onActivityResumed(activity: Activity) {
            if (activity !is HomeActivity || dialog != null) {
                return
            }
            (activity as LifecycleOwner).lifecycleScope.launch {
                val ready = withContext(Dispatchers.IO) { readyUpdate(activity) } ?: return@launch
                if (!activity.isFinishing && dialog == null) {
                    dialog = offer(activity, ready.first, ready.second)
                }
            }
        }

        override fun onActivityDestroyed(activity: Activity) {
            if (dialog?.context?.let { it === activity } == true) {
                dialog?.dismiss()
                dialog = null
            }
        }

        override fun onActivityCreated(activity: Activity, savedInstanceState: Bundle?) = Unit
        override fun onActivityStarted(activity: Activity) = Unit
        override fun onActivityPaused(activity: Activity) = Unit
        override fun onActivityStopped(activity: Activity) = Unit
        override fun onActivitySaveInstanceState(activity: Activity, outState: Bundle) = Unit

        private fun offer(activity: Activity, version: String, apk: File): AlertDialog =
            AlertDialog.Builder(activity)
                .setTitle(activity.getString(R.string.akhi_update_ready_title, version))
                .setMessage(R.string.akhi_update_ready_message)
                .setPositiveButton(R.string.akhi_update_install) { _, _ -> install(activity, apk) }
                .setNegativeButton(R.string.akhi_update_later) { _, _ ->
                    preferencesOf(activity).edit {
                        putLong(SNOOZED_UNTIL, System.currentTimeMillis() + SNOOZE_MS)
                    }
                }
                .setOnDismissListener { dialog = null }
                .show()
    }

    private fun preferencesOf(context: Context): SharedPreferences =
        context.getSharedPreferences(PREFERENCES, Context.MODE_PRIVATE)

    // The version and file of a downloaded update to offer now. Null, and the file removed, once it has been installed.
    private fun readyUpdate(context: Context): Pair<String, File>? {
        val preferences = preferencesOf(context)
        val version = preferences.getString(READY_VERSION, null) ?: return null
        val apk = File(File(context.cacheDir, UPDATES_FOLDER), preferences.getString(READY_FILE, null) ?: return null)
        if (!isNewer(version, BuildConfig.AKHI_VERSION) || !apk.exists()) {
            apk.delete()
            preferences.edit {
                remove(READY_VERSION)
                remove(READY_FILE)
            }
            return null
        }
        return if (System.currentTimeMillis() < preferences.getLong(SNOOZED_UNTIL, 0L)) null else version to apk
    }

    private fun install(activity: Activity, apk: File) {
        val uri = FileProvider.getUriForFile(activity, "${activity.packageName}.fileprovider", apk)
        val intent = Intent(Intent.ACTION_VIEW)
            .setDataAndType(uri, "application/vnd.android.package-archive")
            .addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
        try {
            activity.startActivity(intent)
        } catch (e: ActivityNotFoundException) {
            logger.error("No installer for the update", e)
        }
    }
}

/** One check for a new release, resumed by the next run if it's stopped while downloading. */
internal class AkhiUpdateWorker(
    context: Context,
    params: WorkerParameters,
) : CoroutineWorker(context, params) {
    override suspend fun doWork(): Result = withContext(Dispatchers.IO) {
        try {
            check()
            Result.success()
        } catch (e: IOException) {
            logger.warn("Update check failed", e)
            Result.retry()
        } catch (e: org.json.JSONException) {
            logger.warn("Unexpected answer about the latest release", e)
            Result.success()
        }
    }

    private suspend fun check() {
        val release = JSONObject(readText(LATEST_RELEASE))
        val version = release.getString("tag_name").removePrefix("v")
        if (!AkhiUpdater.isNewer(version, BuildConfig.AKHI_VERSION)) {
            return
        }
        val preferences = applicationContext.getSharedPreferences(AkhiUpdater.PREFERENCES, Context.MODE_PRIVATE)
        if (preferences.getString(AkhiUpdater.READY_VERSION, null) == version) {
            return
        }
        val assets = release.getJSONArray("assets")
        val urls = (0 until assets.length()).map { assets.getJSONObject(it) }
            .associate { it.getString("name") to it.getString("browser_download_url") }
        val abi = Build.SUPPORTED_ABIS.firstOrNull { abi -> urls.keys.any { it.endsWith("-android-$abi.apk") } }
            ?: return
        val name = urls.keys.first { it.endsWith("-android-$abi.apk") }
        val sums = urls["SHA256SUMS.txt"] ?: return
        val expected = AkhiUpdater.checksumOf(readText(sums), name) ?: return

        val folder = File(applicationContext.cacheDir, AkhiUpdater.UPDATES_FOLDER).apply { mkdirs() }
        folder.listFiles()?.filter { !it.name.startsWith(name) }?.forEach { it.delete() }
        val part = File(folder, "$name.part")
        download(urls.getValue(name), part)
        if (sha256Of(part) != expected || !isFromThisApp(part)) {
            logger.warn("The downloaded update isn't valid")
            part.delete()
            return
        }
        val apk = File(folder, name)
        if (!part.renameTo(apk)) {
            throw IOException("Couldn't keep the update")
        }
        preferences.edit {
            putString(AkhiUpdater.READY_VERSION, version)
            putString(AkhiUpdater.READY_FILE, name)
            remove(AkhiUpdater.SNOOZED_UNTIL)
        }
    }

    private fun connect(url: String, offset: Long = 0): HttpURLConnection {
        if (!url.startsWith("https://")) {
            throw IOException("Not https: $url")
        }
        return (URL(url).openConnection() as HttpURLConnection).apply {
            connectTimeout = TIMEOUT_MS
            readTimeout = TIMEOUT_MS
            setRequestProperty("User-Agent", "AkhiBrowser")
            if (offset > 0) {
                setRequestProperty("Range", "bytes=$offset-")
            }
        }
    }

    private fun readText(url: String): String {
        val connection = connect(url)
        try {
            if (connection.responseCode != HttpURLConnection.HTTP_OK) {
                throw IOException("HTTP ${connection.responseCode} for $url")
            }
            return connection.inputStream.bufferedReader().use { it.readText() }
        } finally {
            connection.disconnect()
        }
    }

    private suspend fun download(url: String, part: File) {
        val connection = connect(url, part.length())
        try {
            val isResumed = when (connection.responseCode) {
                HttpURLConnection.HTTP_PARTIAL -> true
                HttpURLConnection.HTTP_OK -> false
                else -> throw IOException("HTTP ${connection.responseCode} for $url")
            }
            connection.inputStream.use { input ->
                FileOutputStream(part, isResumed).use { output ->
                    val buffer = ByteArray(BUFFER_SIZE)
                    while (true) {
                        currentCoroutineContext().ensureActive()
                        val read = input.read(buffer)
                        if (read < 0) {
                            break
                        }
                        output.write(buffer, 0, read)
                    }
                }
            }
        } finally {
            connection.disconnect()
        }
    }

    private fun sha256Of(file: File): String {
        val digest = MessageDigest.getInstance("SHA-256")
        file.inputStream().use { input ->
            val buffer = ByteArray(BUFFER_SIZE)
            while (true) {
                val read = input.read(buffer)
                if (read < 0) {
                    break
                }
                digest.update(buffer, 0, read)
            }
        }
        return digest.digest().joinToString("") { "%02x".format(it) }
    }

    // Android refuses an update with another key anyway: this avoids offering one it will refuse.
    private fun isFromThisApp(apk: File): Boolean {
        val manager = applicationContext.packageManager
        val packageName = applicationContext.packageName
        val update = manager.getPackageArchiveInfo(apk.path, SIGNATURES_FLAG) ?: return false
        val installed = manager.getPackageInfo(packageName, SIGNATURES_FLAG)
        return update.packageName == packageName &&
            signaturesOf(update).isNotEmpty() &&
            signaturesOf(update).toSet() == signaturesOf(installed).toSet()
    }

    @Suppress("DEPRECATION")
    private fun signaturesOf(info: PackageInfo): List<Signature> =
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.P) {
            info.signingInfo?.apkContentsSigners?.toList().orEmpty()
        } else {
            info.signatures?.toList().orEmpty()
        }

    private companion object {
        const val LATEST_RELEASE = "https://api.github.com/repos/halgurdh/akhiBrowser/releases/latest"
        const val TIMEOUT_MS = 30_000
        const val BUFFER_SIZE = 64 * 1024

        @Suppress("DEPRECATION")
        val SIGNATURES_FLAG = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.P) {
            PackageManager.GET_SIGNING_CERTIFICATES
        } else {
            PackageManager.GET_SIGNATURES
        }

        val logger = Logger("akhi-updater")
    }
}
