/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package org.mozilla.fenix.search.awesomebar

import android.graphics.Bitmap
import mozilla.components.browser.state.search.SearchEngine
import mozilla.components.concept.awesomebar.AwesomeBar
import mozilla.components.feature.search.SearchUseCases
import java.text.Normalizer

private const val MAX_SUGGESTIONS = 4

/**
 * AkhiBrowser: Islamic searches above the search engine's suggestions, as the start page of the AkhiBrowser extension
 * shows them on computers (pages/newtab_suggest.js in akhi-extension; keep the list in step). The ones starting with
 * what was typed come first. A tap searches with [searchEngine], or the default one.
 *
 * Give it the same [suggestionsHeader] as the search engine's suggestions: it joins their group, ranked just under the
 * search for what was typed and above the engine's own suggestions.
 */
class AkhiIslamicSuggestionProvider(
    private val searchUseCase: SearchUseCases.SearchUseCase,
    private val icon: Bitmap? = null,
    private val searchEngine: SearchEngine? = null,
    private val suggestionsHeader: String? = null,
) : AwesomeBar.SuggestionProvider {
    override val id: String = java.util.UUID.randomUUID().toString()

    override fun groupTitle(): String? = suggestionsHeader

    override suspend fun onInputChanged(text: String): List<AwesomeBar.Suggestion> =
        matching(text).mapIndexed { index, search ->
            AwesomeBar.Suggestion(
                provider = this,
                id = "akhi-islamic-$search",
                title = search,
                icon = icon,
                score = Int.MAX_VALUE - 2 - index,
                onSuggestionClicked = { searchUseCase.invoke(search, searchEngine) },
            )
        }

    companion object {
        internal val ISLAMIC = listOf(
        "Quran",
        "Quran recitation",
        "Quran translation",
        "Quran tafsir",
        "Surah Al-Fatiha",
        "Surah Al-Baqarah",
        "Surah Al-Kahf",
        "Surah Yasin",
        "Surah Ar-Rahman",
        "Surah Al-Waqiah",
        "Surah Al-Mulk",
        "Surah Al-Ikhlas",
        "Ayatul Kursi",
        "Prayer times",
        "Prayer times today",
        "Qibla direction",
        "Mosque near me",
        "Halal food near me",
        "Halal restaurants near me",
        "How to pray salah",
        "How to perform wudu",
        "Dua for anxiety",
        "Dua for travel",
        "Dua before sleeping",
        "Dua after salah",
        "Morning and evening adhkar",
        "Istikhara dua",
        "99 names of Allah",
        "Hadith of the day",
        "Sahih al-Bukhari",
        "Sahih Muslim",
        "Riyad as-Salihin",
        "40 Hadith Nawawi",
        "Seerah of the Prophet Muhammad ﷺ",
        "Stories of the prophets",
        "Hijri calendar",
        "Hijri date today",
        "Ramadan",
        "Ramadan timetable",
        "Suhoor and iftar times",
        "Laylat al-Qadr",
        "Eid al-Fitr",
        "Eid al-Adha",
        "Zakat calculator",
        "Zakat al-Fitr",
        "Sadaqah",
        "Hajj guide",
        "Umrah guide",
        "Jumuah khutbah",
        "Islamic lectures",
        "Nasheeds without music",
        "Islamic names for boys",
        "Islamic names for girls",
        "Arabic for beginners",
        "Tajweed rules",
        "Learn Quran online",
        "Islamic finance",
        "Is it halal",
        "القرآن الكريم",
        "مواقيت الصلاة",
        "اتجاه القبلة",
        "أذكار الصباح والمساء",
        "تفسير القرآن",
        "حديث اليوم",
        "التقويم الهجري",
        "Gebedstijden",
        "Moskee in de buurt",
        "Halal eten in de buurt",
        "Gebetszeiten",
        "Moschee in der Nähe",
        "Horaires de prière",
        "Mosquée près de moi",
        "Horarios de oración",
        "Namaz vakitleri",
        "Kıble yönü",
        "Kuran-ı Kerim",
        "Jadwal sholat",
        "Arah kiblat",
        "Waktu solat",
        "اوقات شرعی",
        "اوقات نماز",
        "کاتەکانی نوێژ",
        )

        private val INDEX = ISLAMIC.map { it to plain(it) }

        internal fun plain(text: String): String =
            Normalizer.normalize(text.lowercase(), Normalizer.Form.NFD)
                .replace(Regex("[\\p{Mn}ـ]"), "")
                .replace(Regex("[أإآٱ]"), "ا")
                .replace(Regex("[-'’]"), " ")
                .replace(Regex("\\s+"), " ")
                .trim()

        /** The Islamic searches that match what was typed, the ones starting with it first. */
        internal fun matching(typed: String, max: Int = MAX_SUGGESTIONS): List<String> {
            val want = plain(typed)
            if (want.isEmpty()) return emptyList()
            val typedWords = want.split(" ")
            val starts = mutableListOf<String>()
            val words = mutableListOf<String>()
            for ((text, key) in INDEX) {
                if (key == want) continue
                val keyWords = key.split(" ")
                if (key.startsWith(want)) {
                    starts.add(text)
                } else if (typedWords.all { t -> keyWords.any { it.startsWith(t) } }) {
                    words.add(text)
                }
            }
            return (starts + words).take(max)
        }
    }
}
