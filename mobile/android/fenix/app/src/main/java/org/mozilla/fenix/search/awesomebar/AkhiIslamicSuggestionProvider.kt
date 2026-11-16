/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package org.mozilla.fenix.search.awesomebar

import android.graphics.Bitmap
import mozilla.components.browser.state.search.SearchEngine
import mozilla.components.concept.awesomebar.AwesomeBar
import mozilla.components.feature.search.SearchUseCases
import org.mozilla.fenix.components.AkhiHomeCard
import java.text.Normalizer
import java.util.Locale

private const val MAX_SUGGESTIONS = 4

/**
 * AkhiBrowser: Islamic searches above the search engine's suggestions, as the start page of the AkhiBrowser extension
 * shows them on computers (pages/newtab_suggest.js in akhi-extension; keep the lists in step), in AkhiBrowser's
 * language: the extension's language setting, which it sends with the home card, else the phone's. The ones starting
 * with what was typed come first. A tap searches with [searchEngine], or the default one.
 *
 * Give it the same [suggestionsHeader] as the search engine's suggestions: it joins their group, ranked just under the
 * search for what was typed and above the engine's own suggestions.
 */
class AkhiIslamicSuggestionProvider(
    private val searchUseCase: SearchUseCases.SearchUseCase,
    private val icon: Bitmap? = null,
    private val searchEngine: SearchEngine? = null,
    private val suggestionsHeader: String? = null,
    private val language: () -> String? = { AkhiHomeCard.language() ?: Locale.getDefault().language },
) : AwesomeBar.SuggestionProvider {
    override val id: String = java.util.UUID.randomUUID().toString()

    override fun groupTitle(): String? = suggestionsHeader

    override suspend fun onInputChanged(text: String): List<AwesomeBar.Suggestion> =
        matching(text, language()).mapIndexed { index, search ->
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
        /**
         * Per language of AkhiBrowser's texts: English, Dutch and Arabic in full, the other languages their own few
         * first, then English.
         */
        internal val ISLAMIC: Map<String, List<String>> = mapOf(
            "en" to listOf(
                "Quran", "Quran recitation", "Quran translation", "Quran tafsir", "Surah Al-Fatiha",
                "Surah Al-Baqarah", "Surah Al-Kahf", "Surah Yasin", "Surah Ar-Rahman", "Surah Al-Waqiah",
                "Surah Al-Mulk", "Surah Al-Ikhlas", "Ayatul Kursi", "Prayer times", "Prayer times today",
                "Qibla direction", "Mosque near me", "Halal food near me", "Halal restaurants near me",
                "How to pray salah", "How to perform wudu", "Dua for anxiety", "Dua for travel",
                "Dua before sleeping", "Dua after salah", "Morning and evening adhkar", "Istikhara dua",
                "99 names of Allah", "Hadith of the day", "Sahih al-Bukhari", "Sahih Muslim", "Riyad as-Salihin",
                "40 Hadith Nawawi", "Seerah of the Prophet Muhammad ﷺ", "Stories of the prophets", "Hijri calendar",
                "Hijri date today", "Ramadan", "Ramadan timetable", "Suhoor and iftar times", "Laylat al-Qadr",
                "Eid al-Fitr", "Eid al-Adha", "Zakat calculator", "Zakat al-Fitr", "Sadaqah", "Hajj guide",
                "Umrah guide", "Jumuah khutbah", "Islamic lectures", "Nasheeds without music",
                "Islamic names for boys", "Islamic names for girls", "Arabic for beginners", "Tajweed rules",
                "Learn Quran online", "Islamic finance", "Is it halal",
            ),
            "nl" to listOf(
                "Koran", "Koranrecitatie", "Koran vertaling", "Koran tafsir", "Soera Al-Fatiha", "Soera Al-Baqarah",
                "Soera Al-Kahf", "Soera Yasin", "Soera Ar-Rahman", "Soera Al-Waqiah", "Soera Al-Mulk",
                "Soera Al-Ikhlas", "Ayatul Kursi", "Gebedstijden", "Gebedstijden vandaag", "Qibla richting",
                "Moskee in de buurt", "Halal eten in de buurt", "Halal restaurants in de buurt", "Hoe bid je salah",
                "Hoe doe je wudu", "Dua tegen angst", "Dua voor op reis", "Dua voor het slapen", "Dua na het gebed",
                "Ochtend- en avondadhkar", "Istikhara dua", "99 namen van Allah", "Hadith van de dag",
                "Sahih al-Bukhari", "Sahih Muslim", "Riyad as-Salihin", "40 hadith van Nawawi",
                "Seerah van de Profeet Mohammed ﷺ", "Verhalen van de profeten", "Islamitische kalender",
                "Islamitische datum vandaag", "Ramadan", "Ramadan rooster", "Suhoor en iftar tijden",
                "Laylat al-Qadr", "Suikerfeest", "Offerfeest", "Zakat berekenen", "Zakat al-Fitr", "Sadaqah",
                "Hajj gids", "Umrah gids", "Vrijdagpreek", "Islamitische lezingen", "Nasheeds zonder muziek",
                "Islamitische jongensnamen", "Islamitische meisjesnamen", "Arabisch voor beginners",
                "Tajweed regels", "Koran leren online", "Islamitisch bankieren", "Is het halal",
            ),
            "ar" to listOf(
                "القرآن الكريم", "تلاوة القرآن", "ترجمة معاني القرآن", "تفسير القرآن", "سورة الفاتحة", "سورة البقرة",
                "سورة الكهف", "سورة يس", "سورة الرحمن", "سورة الواقعة", "سورة الملك", "سورة الإخلاص", "آية الكرسي",
                "مواقيت الصلاة", "مواقيت الصلاة اليوم", "اتجاه القبلة", "أقرب مسجد", "مطاعم حلال قريبة",
                "أكل حلال قريب", "كيفية الصلاة", "كيفية الوضوء", "دعاء القلق", "دعاء السفر", "دعاء النوم",
                "الأذكار بعد الصلاة", "أذكار الصباح والمساء", "دعاء الاستخارة", "أسماء الله الحسنى", "حديث اليوم",
                "صحيح البخاري", "صحيح مسلم", "رياض الصالحين", "الأربعون النووية", "السيرة النبوية ﷺ", "قصص الأنبياء",
                "التقويم الهجري", "التاريخ الهجري اليوم", "رمضان", "إمساكية رمضان", "مواعيد السحور والإفطار",
                "ليلة القدر", "عيد الفطر", "عيد الأضحى", "حاسبة الزكاة", "زكاة الفطر", "الصدقة", "دليل الحج",
                "دليل العمرة", "خطبة الجمعة", "محاضرات إسلامية", "أناشيد بدون موسيقى", "أسماء أولاد إسلامية",
                "أسماء بنات إسلامية", "تعلم العربية للمبتدئين", "أحكام التجويد", "تعلم القرآن أونلاين",
                "التمويل الإسلامي", "هل هو حلال",
            ),
            "de" to listOf(
                "Gebetszeiten", "Moschee in der Nähe",
            ),
            "fr" to listOf(
                "Horaires de prière", "Mosquée près de moi",
            ),
            "es" to listOf(
                "Horarios de oración",
            ),
            "tr" to listOf(
                "Namaz vakitleri", "Kıble yönü", "Kuran-ı Kerim",
            ),
            "id" to listOf(
                "Jadwal sholat", "Arah kiblat",
            ),
            "ms" to listOf(
                "Waktu solat",
            ),
            "fa" to listOf(
                "اوقات شرعی", "اوقات نماز",
            ),
            "ckb" to listOf(
                "کاتەکانی نوێژ",
            ),
            "ur" to emptyList(),
        )
        private val FULL = setOf("en", "nl", "ar")
        private val indexes = java.util.concurrent.ConcurrentHashMap<String, List<Pair<String, String>>>()

        /** The searches in [language], with their keys for matching. */
        internal fun indexOf(language: String?): List<Pair<String, String>> {
            val code = language.orEmpty().lowercase().split('-', '_').first()
            val lang = if (code in ISLAMIC) code else "en"
            return indexes.getOrPut(lang) {
                val list = if (lang in FULL) ISLAMIC.getValue(lang) else ISLAMIC.getValue(lang) + ISLAMIC.getValue("en")
                list.map { it to plain(it) }
            }
        }

        internal fun plain(text: String): String =
            Normalizer.normalize(text.lowercase(), Normalizer.Form.NFD)
                .replace(Regex("[\\p{Mn}ـ]"), "")
                .replace(Regex("[أإآٱ]"), "ا")
                .replace(Regex("[-'’]"), " ")
                .replace(Regex("\\s+"), " ")
                .trim()

        /** The Islamic searches that match what was typed, the ones starting with it first. */
        internal fun matching(typed: String, language: String?, max: Int = MAX_SUGGESTIONS): List<String> {
            val want = plain(typed)
            if (want.isEmpty()) return emptyList()
            val typedWords = want.split(" ")
            val starts = mutableListOf<String>()
            val words = mutableListOf<String>()
            for ((text, key) in indexOf(language)) {
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
