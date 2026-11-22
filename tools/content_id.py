"""The Indonesian text of the blog and comparison pages. content.py merges it in; see build_pages.py and langs.py.

Each key in ARTICLES is an article slug from content.py. {YEAR} stands for the current year."""

UI = {
    "nav_label": "Menu utama",
    "blog": "Blog",
    "compare": "Bandingkan",
    "download": "Dapatkan AkhiBrowser",
    "blog_title": "Panduan menjelajah secara halal",
    "blog_lead": "Panduan praktis untuk menjelajah web dengan lebih sedikit iklan, lebih sedikit konten haram, dan lebih banyak kendali, di perangkatmu sendiri.",
    "cta_title": "Dapatkan AkhiBrowser",
    "cta_text": "Browser pribadi untuk Muslim, dibangun di atas Firefox. Di Microsoft Store untuk Windows dan di Google Play untuk Android. Perlindungannya gratis.",
    "footer": "AkhiBrowser dibangun di atas <a href=\"https://www.firefox.com/\">Firefox</a>, dan tidak dibuat atau didukung oleh Mozilla. Filter bisa melewatkan sesuatu, dan tidak menggantikan perhatian orang tua. <a href=\"/id/\">Beranda</a> · <a href=\"/id/faq/\">Pertanyaan umum</a> · <a href=\"mailto:support@akhibrowser.com\">support@akhibrowser.com</a>",
}

ARTICLES = {
    "what-is-a-halal-browser": {
        "title": "Apa itu browser halal, dan apakah kamu membutuhkannya?",
        "description": "Apa yang dilakukan browser halal, apa yang tidak bisa dilakukannya, dan cara memilihnya: pemblokiran situs, SafeSearch, pemburaman gambar, dan privasi dijelaskan.",
        "body": """<p>Browser halal adalah browser web yang menyaring apa yang dibiarkan browser biasa kepadamu. Browser ini memblokir situs dan pencarian untuk hal-hal seperti konten dewasa, alkohol, dan judi, serta menjauhkan gambar yang tidak diinginkan dari layarmu.</p>
<h2>Yang biasanya dilakukan browser halal</h2>
<ul>
<li><strong>Memblokir situs.</strong> Situs dewasa, judi, alkohol, dan narkoba berhenti sebelum dimuat.</li>
<li><strong>Memaksakan SafeSearch.</strong> Mesin pencari menyembunyikan hasil yang vulgar, tanpa kamu perlu mengaturnya.</li>
<li><strong>Menyaring gambar.</strong> Gambar yang menampilkan ketelanjangan diburamkan.</li>
<li><strong>Memblokir iklan dan pelacak.</strong> Banyak gambar yang tidak diinginkan datang lewat iklan, jadi ini membantu dua kali.</li>
</ul>
<h2>Yang tidak bisa dilakukannya</h2>
<p>Tidak ada filter yang sempurna. Beberapa halaman lolos, dan beberapa halaman yang tidak berbahaya terblokir. Browser juga hanya melindungi apa yang terjadi di dalamnya: aplikasi dan browser lain di perangkat yang sama tidak tercakup. Browser membantu niat dan kebiasaan, tetapi tidak menggantikannya, juga tidak menggantikan perhatian orang tua.</p>
<h2>Cara memilihnya</h2>
<ul>
<li><strong>Di mana pemeriksaan dilakukan?</strong> Menyaring di perangkatmu sendiri berarti gambarmu tidak perlu keluar darinya.</li>
<li><strong>Apa yang keluar dari perangkatmu?</strong> Cari daftar yang jelas. Browser yang mengatakan "tidak ada" harus bisa menjelaskan bagaimana ia memblokir situs dan memperbarui dirinya.</li>
<li><strong>Bisakah kamu mengendalikannya?</strong> Kamu harus bisa melihat dan mengubah setiap perlindungan.</li>
<li><strong>Apakah berjalan di perangkatmu?</strong> Periksa sebelum memutuskan, terutama di iPhone atau Mac.</li>
</ul>
<h2>Browser halal, ekstensi browser, atau filter DNS?</h2>
<p>Ada tiga cara umum untuk menyaring web, dan ketiganya bekerja paling baik bersama-sama:</p>
<ul>
<li><strong>Browser halal</strong> menyaring di dalam browser itu sendiri: situs, pencarian, gambar, dan video. Perlindungannya aktif sejak halaman pertama dan bisa dikunci dengan PIN.</li>
<li><strong>Ekstensi browser</strong> menambahkan filter ke browser yang sudah kamu pakai, seperti Chrome. Cepat dicoba, tetapi biasanya bisa dihapus atau dimatikan, dan tidak bisa mengubah cara kerja browser itu sendiri.</li>
<li><strong>Filter DNS atau router</strong> memblokir seluruh situs untuk setiap aplikasi di perangkat atau jaringan. Filter ini tidak bisa melihat isi halaman, jadi tidak bisa memburamkan gambar atau menghapus musik dari video.</li>
</ul>
<p>Untuk keluarga, pengaturan yang umum adalah DNS keluarga di router ditambah browser halal di setiap perangkat, dengan browser lain dihapus atau diblokir. Baca <a href="/id/blog/block-haram-content/">cara memblokir konten haram di ponsel dan komputermu</a> untuk pengaturan lengkapnya.</p>
<h2>Daftar periksa untuk memilih browser halal</h2>
<ul>
<li>Apakah situs dewasa, judi, alkohol, dan narkoba diblokir sejak halaman pertama, tanpa pengaturan?</li>
<li>Apakah SafeSearch dipaksakan di setiap mesin pencari, termasuk YouTube?</li>
<li>Apakah gambar diperiksa di perangkatmu, atau dikirim ke server?</li>
<li>Bisakah orang tua mengunci pengaturan dengan PIN?</li>
<li>Apakah browser itu menyatakan dengan jelas apa yang keluar dari perangkatmu?</li>
<li>Apakah masih diperbarui? Browser yang berhenti mendapat pembaruan juga berhenti mendapat perbaikan keamanan. SalamWeb, salah satu browser halal pertama, dihentikan pada 2021.</li>
</ul>
<p>Kami membandingkan pilihannya di <a href="/id/blog/best-halal-browsers/">browser halal terbaik {YEAR}</a>.</p>
<h2>Pertanyaan umum</h2>
<h3>Apakah browser halal hanya untuk Muslim?</h3>
<p>Tidak. Siapa saja yang ingin lebih sedikit iklan, tanpa konten dewasa, dan lebih banyak kendali atas gambar bisa memakainya. Namanya menggambarkan nilai-nilai yang menjadi dasarnya.</p>
<h3>Apakah browser halal gratis?</h3>
<p>Banyak yang gratis. Perlindungan AkhiBrowser gratis, dengan Premium opsional untuk pengaturan gambar tambahan dan alat untuk orang tua.</p>
<h3>Apakah browser halal menggantikan kontrol orang tua?</h3>
<p>Browser ini mencakup browser. Untuk aplikasi dan browser lain, gabungkan dengan kontrol perangkat, seperti Google Family Link atau Microsoft Family Safety. Lihat <a href="/id/blog/parental-controls-for-muslim-families/">pengaturan kontrol orang tua yang sederhana</a>.</p>
<h3>Bisakah browser halal menghapus musik dari video?</h3>
<p>Beberapa bisa. AkhiBrowser <a href="/id/blog/remove-background-music-from-videos/">menghapus musik latar di perangkatmu</a>, jadi suara tetap ada dan musiknya hilang.</p>
<p>AkhiBrowser adalah salah satu pilihan, dibangun di atas Firefox untuk Windows dan Android. Perlindungannya aktif sejak halaman pertama, dan <a href="/id/privacy/">situsnya mencantumkan apa yang keluar dari perangkatmu</a>. Kamu juga bisa membaca <a href="/id/compare/kahf-browser/">perbandingannya dengan Kahf Browser</a>.</p>""",
    },
    "block-haram-content": {
        "title": "Cara memblokir konten haram di ponsel dan komputermu",
        "description": "Langkah demi langkah memblokir konten dewasa, judi, dan alkohol: filter browser, SafeSearch, DNS keluarga, dan kontrol perangkat, serta apa yang terlewat oleh masing-masing.",
        "body": """<p>Tidak ada satu pengaturan yang memblokir semuanya. Yang berhasil adalah beberapa lapisan, masing-masing menutup apa yang terlewat oleh yang lain.</p>
<h2>1. Gunakan browser yang menyaring secara bawaan</h2>
<p>Browser yang menyaring memblokir situs, menyaring pencarian, dan memburamkan gambar tanpa pengaturan. Di AkhiBrowser, situs dewasa, alkohol, narkoba, vape, dan judi diblokir sejak halaman pertama.</p>
<h2>2. Paksakan SafeSearch</h2>
<p>SafeSearch menyembunyikan hasil vulgar di mesin pencari. Kamu bisa menyalakannya di pengaturan setiap mesin pencari, tetapi mudah dimatikan lagi, dan hanya berlaku per browser. Browser yang menyaring bisa memaksakannya: AkhiBrowser melakukannya di Google, Bing, DuckDuckGo, dan Yahoo, serta menyalakan Mode Terbatas YouTube.</p>
<h2>3. Tambahkan DNS keluarga</h2>
<p>Layanan DNS keluarga menolak mencari situs dewasa, untuk semua yang ada di jaringan atau perangkat itu. 1.1.1.3 dari Cloudflare dan CleanBrowsing adalah pilihan yang dikenal. Layanan ini bekerja berdasarkan nama situs, jadi tidak bisa melihat isi situs yang diizinkan, dan pengelolanya bisa melihat nama situs yang kamu kunjungi.</p>
<h2>4. Tutup pintu samping</h2>
<p>Filter browser tidak mencakup aplikasi lain. Di perangkat anak, gunakan Google Family Link di Android atau Microsoft Family Safety di Windows untuk mengatur aplikasi dan browser mana yang boleh dipasang. Di AkhiBrowser, Family Premium juga bisa mengunci pengaturan dengan PIN dan mematikan tab pribadi.</p>
<h2>5. Terus berbicara</h2>
<p>Filter bisa melewatkan sesuatu, dan tidak berlaku di ponsel teman. Bagi anak-anak, tahu apa yang harus dilakukan saat sesuatu muncul di layar lebih penting daripada pengaturan apa pun.</p>""",
    },
    "remove-background-music-from-videos": {
        "title": "Cara menghapus musik latar dari video di browsermu",
        "description": "Bagaimana pemisahan suara di perangkat menghapus musik latar dari video online dan mempertahankan ucapan, di mana bekerja dengan baik, dan di mana kesulitan.",
        "body": """<p>Banyak kajian, dokumenter, dan klip berita punya musik latar yang mungkin lebih suka tidak kamu dengar. Membisukan suara bukan pilihan saat kamu ingin mendengar ucapannya. Pemisahan suara menyelesaikan ini: model ucapan kecil mempertahankan suara orang dan menghapus sisanya.</p>
<p>Para ulama berbeda pendapat tentang musik, dan artikel ini tidak berusaha memutuskannya. Artikel ini hanya menjelaskan apa yang bisa dilakukan teknologinya, bagi yang menginginkannya.</p>
<h2>Cara kerjanya</h2>
<p>Model ucapan mendengarkan suara video dalam potongan pendek dan memperkirakan bagian mana yang merupakan suara manusia. Sisanya dikeluarkan sebelum sampai ke speakermu. Menjalankannya di perangkatmu berarti audio tidak perlu dikirim ke mana pun.</p>
<h2>Cara memakainya di AkhiBrowser</h2>
<ol>
<li>Pasang AkhiBrowser di Windows atau Android.</li>
<li>Putar video. No music aktif secara bawaan.</li>
<li>Untuk mematikannya, buka perisai AkhiBrowser di bilah alat. Di Android: menu, lalu Ekstensi, lalu AkhiBrowser.</li>
</ol>
<p>Ponsel dan komputer yang lebih lambat memakai model yang lebih ringan, agar tetap bisa mengikuti.</p>
<h2>Di mana kurang berhasil</h2>
<ul>
<li><strong>Nyanyian.</strong> Suara yang bernyanyi tetaplah suara, jadi model harus memutuskan apa yang dilakukan dengannya.</li>
<li><strong>Musik keras di atas ucapan pelan.</strong> Sebagian musik bisa tersisa, dan suara bisa terdengar lebih tipis.</li>
<li><strong>Situs yang memblokir akses ke audionya.</strong> Beberapa video yang dilindungi tidak bisa diproses.</li>
</ul>
<p>Fitur ini dibangun dari <a href="https://github.com/mohamedsadiqaguenaou/NoMusic">NoMusic karya Mohamed Sadiq</a>.</p>""",
    },
    "parental-controls-for-muslim-families": {
        "title": "Kontrol orang tua untuk keluarga Muslim: pengaturan sederhana",
        "description": "Pengaturan sederhana untuk orang tua: browser yang menyaring, PIN, situs yang disetujui untuk anak kecil, jam tidur dan jam sekolah, serta apa yang tidak bisa dikendalikan browser mana pun.",
        "body": """<p>Kontrol orang tua yang baik sesuai dengan usia anak. Ini adalah titik awal yang masuk akal, memakai kontrol Family Premium di AkhiBrowser. Masing-masing mati sampai kamu menyalakannya, dan datanya tetap di perangkat.</p>
<h2>Pertama, untuk segala usia</h2>
<ol>
<li>Atur PIN orang tua, agar perlindungan tidak bisa dimatikan tanpanya.</li>
<li>Nyalakan <strong>Tanpa tab pribadi</strong>, agar penjelajahan tetap di bawah kontrol.</li>
<li>Hapus browser lain dari perangkat, atau blokir dengan Google Family Link atau Microsoft Family Safety. Browser tidak bisa mengendalikan apa yang terjadi di luarnya.</li>
</ol>
<h2>Anak kecil</h2>
<p>Gunakan <strong>Izinkan hanya situs yang disetujui</strong> dan tambahkan beberapa situs yang mereka pakai. Semua yang lain tetap tertutup, yang jauh lebih kuat daripada mencoba memblokir bagian buruk dari web.</p>
<h2>Anak yang lebih besar</h2>
<p>Buka web, tetapi tetapkan batas. <strong>Blokir situs pilihan</strong> mencakup situs tertentu yang menimbulkan masalah, dan <strong>Batas waktu</strong> menetapkan batas harian, jam tidur, dan jam sekolah. <strong>Batas feed</strong> menyembunyikan feed video pendek dan menghentikan situs media sosial setelah waktu tertentu. Fitur ini berlaku untuk situs web di AkhiBrowser, bukan di aplikasi media sosial.</p>
<h2>Remaja</h2>
<p>Kepercayaan tumbuh seiring usia. <strong>Ringkasan aktivitas</strong> menunjukkan berapa banyak halaman yang diblokir dan alasannya, tanpa alamatnya. Ini awal percakapan, bukan pengawasan.</p>
<h2>Saat kamu butuh jeda</h2>
<p><strong>Jeda internet</strong> menghentikan penjelajahan seketika, dengan PIN untuk melanjutkan. Berguna saat makan dan di sekitar waktu salat.</p>
<p>Lihat <a href="/id/#premium">paket dan harga</a>. Perlindungan gratis tetap berfungsi tanpa semua ini.</p>""",
    },
    "why-prayer-times-differ": {
        "title": "Mengapa waktu salat berbeda antara aplikasi dan masjid",
        "description": "Mengapa Subuh dan Isya bisa berbeda lebih dari setengah jam antar-aplikasi: metode perhitungan dijelaskan, dengan contoh nyata dari Almere di Belanda.",
        "body": """<p>Dua aplikasi bisa menampilkan waktu berbeda untuk salat yang sama di kota yang sama. Biasanya tidak ada yang rusak: keduanya memakai metode perhitungan yang berbeda.</p>
<h2>Apa yang sama, dan apa yang berubah</h2>
<p>Zuhur dan Magrib mengikuti posisi matahari, jadi metode-metode umumnya sepakat. Subuh dan Isya bergantung pada fajar dan senja, saat matahari berada pada sudut tertentu di bawah cakrawala, dan metode memilih sudut yang berbeda. Asar juga berbeda menurut mazhab: waktu Hanafi lebih lambat dari yang standar.</p>
<h2>Contoh nyata</h2>
<p>Ini adalah waktu untuk Almere, Belanda, pada 8 November 2026, dari <a href="https://aladhan.com/prayer-times-api">layanan perhitungan publik Aladhan</a>:</p>
<div class="table"><table>
<thead><tr><th scope="col">Metode</th><th scope="col">Subuh</th><th scope="col">Isya</th></tr></thead>
<tbody>
<tr><th scope="row">Maroko</th><td>05:43</td><td>18:48</td></tr>
<tr><th scope="row">Liga Muslim Dunia</th><td>05:50</td><td>18:48</td></tr>
<tr><th scope="row">Karachi</th><td>05:50</td><td>18:55</td></tr>
<tr><th scope="row">Moonsighting Committee</th><td>06:09</td><td>18:26</td></tr>
<tr><th scope="row">ISNA</th><td>06:10</td><td>18:35</td></tr>
<tr><th scope="row">Prancis (UOIF)</th><td>06:30</td><td>18:15</td></tr>
</tbody>
</table></div>
<p>Selisihnya 47 menit antara Subuh paling awal dan paling akhir. Jauh dari khatulistiwa, selisihnya berubah menurut musim, dan di musim panas fajar yang sebenarnya mungkin tidak terjadi sama sekali, jadi metode juga butuh aturan untuk lintang tinggi.</p>
<h2>Mana yang sebaiknya kamu pakai?</h2>
<p>Untuk pertanyaan amalan, tanyakan kepada masjid setempat atau ulama yang kamu percaya, dan ikuti yang dipakai komunitasmu. Aplikasi hanya bisa berhitung.</p>
<h2>Waktu salat di AkhiBrowser</h2>
<p>AkhiBrowser menghitung waktu salat di perangkatmu dari kota yang kamu pilih, tanpa memakai lokasimu. Ia memilih metode berdasarkan negara, dan kamu bisa mengubah metode dan waktu Asar di opsinya.</p>""",
    },
    "best-halal-browsers": {
        "title": "Browser halal terbaik {YEAR}, dibandingkan",
        "description": "Perbandingan jujur browser halal yang bisa kamu pakai di {YEAR}: AkhiBrowser, Kahf Browser, dan Tahir Browser, serta apa yang terjadi pada SalamWeb. Platform, harga, dan fitur.",
        "body": """<p>Browser halal memblokir situs haram, memaksakan SafeSearch, dan menjauhkan gambar yang tidak diinginkan dari layarmu. Di {YEAR} ada tiga pilihan aktif yang perlu diketahui. Salah satunya, AkhiBrowser, kami buat sendiri, jadi halaman ini berpegang pada apa yang dinyatakan setiap browser di halamannya sendiri, dan mengatakan dengan jelas di mana masing-masing paling cocok.</p>
<h2>Jawaban singkatnya</h2>
<ul>
<li><strong>Di Windows, atau untuk kontrol orang tua:</strong> AkhiBrowser. Perlindungan gratis, penghapusan musik latar, dan Family Premium dengan PIN, daftar situs, dan batas waktu.</li>
<li><strong>Di Mac, atau untuk browser serba gratis di semua platform:</strong> Kahf Browser. Windows, macOS, Android, dan iOS, gratis tanpa pembelian dalam aplikasi.</li>
<li><strong>Di iPhone:</strong> Tahir Browser atau Kahf Browser. AkhiBrowser belum ada di iOS.</li>
</ul>
<h2>AkhiBrowser</h2>
<p>Browser halal yang dibangun di atas Firefox, untuk Windows dan Android. Situs dewasa, alkohol, narkoba, vape, dan judi diblokir sejak halaman pertama, SafeSearch dipaksakan di Google, Bing, DuckDuckGo, Yahoo, dan YouTube, dan gambar tetap buram sampai diperiksa di perangkatmu. Ini satu-satunya dari ketiganya yang menghapus musik latar dari video, di perangkatmu. Perlindungannya gratis; Premium menambahkan pilihan siapa yang diburamkan, dan Family Premium menambahkan PIN orang tua, daftar situs, batas waktu, dan tombol jeda.</p>
<h2>Kahf Browser</h2>
<p>Browser berbasis Chromium untuk Muslim di Windows, macOS, Android, dan iOS. Situsnya menyatakan browser ini gratis di semua platform tanpa langganan atau pembelian dalam aplikasi, memblokir iklan, situs dewasa, dan situs haram dengan penyaringan AI dan basis data, memaksakan SafeSearch dan Safe YouTube, memburamkan ketelanjangan secara real time, serta menyertakan waktu salat dan arah kiblat. Sebagian besar ekstensi Chrome berfungsi di dalamnya.</p>
<h2>Tahir Browser</h2>
<p>Browser untuk iPhone dan iPad dari Ihya Tech. Halaman App Store-nya menjelaskan pemburaman semua gambar atau memakai AI untuk memburamkan lawan jenis, ketuk untuk melihat, pemblokiran situs haram, iklan, dan pelacak, pengingat Islami, SafeSearch yang dipaksakan, dan kunci kata sandi atau biometrik pada perisainya. Gratis diunduh, dengan paket bulanan dan tahunan opsional.</p>
<h2>Apa yang terjadi pada SalamWeb?</h2>
<p>SalamWeb adalah salah satu browser halal pertama dan banyak diberitakan pada 2019. Browser ini dihentikan pada 2021 dan situsnya sudah hilang, jadi tidak lagi menjadi pilihan. Ini pengingat yang baik untuk memilih browser yang masih diperbarui, karena pembaruan membawa perbaikan keamanan.</p>
<h2>Berdampingan</h2>
<div class="table"><table>
<thead><tr><th scope="col"></th><th scope="col">AkhiBrowser</th><th scope="col">Kahf Browser</th><th scope="col">Tahir Browser</th></tr></thead>
<tbody>
<tr><th scope="row">Platform</th><td>Windows, Android</td><td>Windows, macOS, Android, iOS</td><td>iPhone, iPad</td></tr>
<tr><th scope="row">Harga</th><td>Perlindungan gratis; Premium opsional</td><td>Gratis</td><td>Gratis; paket opsional</td></tr>
<tr><th scope="row">Dibangun di atas</th><td>Firefox</td><td>Chromium</td><td>iOS WebKit</td></tr>
<tr><th scope="row">Situs haram diblokir</th><td>Ya</td><td>Ya</td><td>Ya</td></tr>
<tr><th scope="row">SafeSearch dipaksakan</th><td>Ya, termasuk YouTube</td><td>Ya, termasuk YouTube</td><td>Ya</td></tr>
<tr><th scope="row">Pemburaman gambar</th><td>Sampai diperiksa, di perangkatmu</td><td>Real time</td><td>Semua gambar, atau AI menurut jenis kelamin</td></tr>
<tr><th scope="row">Penghapusan musik latar</th><td>Ya</td><td>Tidak disebutkan</td><td>Tidak disebutkan</td></tr>
<tr><th scope="row">PIN orang tua dan batas waktu</th><td>Family Premium</td><td>Tidak disebutkan</td><td>Kunci perisai</td></tr>
</tbody>
</table></div>
<p>&quot;Tidak disebutkan&quot; berarti kami tidak menemukannya di halaman browser itu sendiri, bukan berarti tidak ada. Untuk tabel yang lebih panjang, lihat <a href="/id/compare/kahf-browser/">perbandingan AkhiBrowser dan Kahf Browser</a> dan <a href="/id/compare/browsers/">perbandingan AkhiBrowser, Kahf, Brave, Firefox, dan Chrome</a>. Baru mengenal topik ini? Mulailah dengan <a href="/id/blog/what-is-a-halal-browser/">apa itu browser halal</a>.</p>
<p>Diperiksa dengan halaman masing-masing browser pada 10 November 2026. Melihat sesuatu yang sudah usang? Beri tahu kami di <a href="mailto:support@akhibrowser.com">support@akhibrowser.com</a>.</p>""",
    },
}

_NS = "Tidak disebutkan"

COMPARE = {
    "seo_title": "AkhiBrowser vs Kahf Browser: perbandingan fitur, harga, dan platform",
    "title": "Perbandingan AkhiBrowser dan Kahf Browser",
    "description": "AkhiBrowser dan Kahf Browser berdampingan: harga, platform, penyaringan, gambar, penghapusan musik, waktu salat, dan kontrol orang tua, dari halaman masing-masing browser.",
    "lead": "Keduanya adalah browser untuk Muslim. Tabel ini mencantumkan apa yang dinyatakan masing-masing di situsnya sendiri, per 8 November 2026 untuk Kahf Browser dan 22 November 2026 untuk AkhiBrowser. Kami belum menguji Kahf Browser sendiri. &quot;Tidak disebutkan&quot; berarti kami tidak menemukannya di halaman yang kami baca, bukan berarti fiturnya tidak ada.",
    "head": ["", "AkhiBrowser", "Kahf Browser"],
    "rows": [
        ["Harga", "Perlindungan gratis. Premium opsional €3,99 per bulan, €39 per tahun, atau €119 sekali bayar; Family Premium €59,99 per tahun", "Gratis di semua platform, tanpa langganan atau pembelian dalam aplikasi"],
        ["Platform", "Windows (Microsoft Store), Android (Google Play). iOS dan macOS: <a href=\"/id/#roadmap\">dalam peta jalan</a>, belum ada tanggal", "Windows, macOS, Android, iOS. Linux: tercantum di FAQ-nya, halaman unduhnya bilang segera hadir"],
        ["Situs dewasa dan haram", "Diblokir: dewasa, alkohol, narkoba, vape, dan judi", "Diblokir, dengan penyaringan AI dan basis data"],
        ["Pencarian haram", "Diblokir dalam 11 bahasa; pertanyaan tentangnya tetap diizinkan", "Safe Search, termasuk saran pencarian"],
        ["Ketelanjangan dalam gambar", "Buram sampai diperiksa di perangkatmu: gambar, latar belakang, video, dan kanvas; di video secara real time: setiap adegan baru langsung diburamkan dan diperiksa", "Diburamkan secara real time"],
        ["SafeSearch", "Dipaksakan di Google, Bing, DuckDuckGo, dan Yahoo, plus Mode Terbatas YouTube", "Diterapkan di mesin pencari besar; Safe YouTube"],
        ["PIN orang tua, daftar situs, batas waktu", "Family Premium: PIN, situs diblokir atau hanya yang disetujui, jam tidur dan jam sekolah, batas harian", _NS],
        ["Laporan orang tua dan ringkasan aktivitas", "Family Premium: email saat perlindungan atau PIN dimatikan, ringkasan mingguan pemblokiran menurut alasan, dan ringkasan 7 hari di perangkat", _NS],
        ["Jeda internet", "Family Premium, dengan PIN; kontrol orang tua bisa dipindah ke perangkat lain dalam file yang dikunci dengan PIN", _NS],
        ["Feed media sosial dan aplikasi", "Family Premium: feed video pendek disembunyikan, batas harian untuk situs media sosial, aplikasi diblokir di Android", _NS],
        ["Hapus musik latar dari video", "Gratis, di perangkatmu", _NS],
        ["Iklan dan pelacak", "Diblokir, dengan uBlock Origin dan pemblokir bawaan", "Pemblokir bawaan"],
        ["Situs phishing dan penipuan", "Diblokir", "Diblokir"],
        ["Pilih siapa yang diburamkan (perempuan, laki-laki)", "Premium", _NS],
        ["Mengenali hijab", "Premium", _NS],
        ["Mode ketat", "Premium: setiap gambar dan video tetap buram sampai kamu mengetuknya", _NS],
        ["YouTube", "Mode Terbatas, gratis. Premium: tanpa rekomendasi, Shorts, atau putar otomatis. Family Premium: Deen Time, hanya saluran pilihanmu", "Safe YouTube"],
        ["Waktu salat", "Gratis, untuk kota pilihanmu, tanpa lokasimu; pengingat di komputer", "Waktu salat dan notifikasi"],
        ["Jeda salat", "Family Premium: situs media sosial, video, dan game berhenti beberapa menit setelah setiap waktu salat", _NS],
        ["Cek halal dan tempat halal", "Family Premium: peringatan di halaman produk dengan babi, alkohol, gelatin, atau nomor E yang meragukan; tempat halal di Google Maps dan situs pesan antar", _NS],
        ["Peringatan riba, loot box", "Family Premium: peringatan di halaman pinjaman berbunga, kartu kredit, dan paylater; situs buka peti dan judi skin diblokir", _NS],
        ["Tilawah Al-Qur'an, sumber tepercaya", "Family Premium: ikuti tilawah di YouTube ayat demi ayat dengan maknanya; sumber ulama lebih dulu saat mencari tentang Islam", _NS],
        ["Ayat hari ini", "Gratis", _NS],
        ["Kiblat", "Ya, di Android: kompas di bawah waktu salat", "Ya"],
        ["Bahasa", "12, termasuk Arab, Urdu, Persia, Kurdi, dan Turki", _NS],
        ["Koreksi buta warna", "Gratis, di perangkatmu", _NS],
        ["Perlu akun", "Tidak", "Tidak; bisa masuk akun"],
        ["Dibangun di atas", "Firefox", "Chromium; sebagian besar ekstensi Chrome berfungsi"],
        ["Kode sumber", "Perubahan Firefox dan file MPL terbuka untuk umum; ekstensinya sendiri tertutup", "Belum terbuka, menurut FAQ-nya"],
    ],
    "after": """<h2>Mana yang cocok untukmu?</h2>
<p><strong>Kahf Browser</strong> cocok jika kamu memakai iPhone atau Mac, atau ingin semuanya gratis.</p>
<p><strong>AkhiBrowser</strong> cocok jika kamu ingin musik latar dihapus, ingin memilih siapa yang diburamkan, atau butuh kontrol orang tua seperti PIN, batas waktu, dan laporan lewat email, di Windows atau Android. Family Premium menambahkan yang tidak disebutkan Kahf: cek halal saat berbelanja, peringatan riba, dan jeda setelah setiap salat.</p>
<p>Keduanya gratis dicoba, jadi ujian terbaik adalah pemakaianmu sendiri. AkhiBrowser tidak berafiliasi dengan Kahf. Melihat sesuatu yang sudah usang? Beri tahu kami di <a href="mailto:support@akhibrowser.com">support@akhibrowser.com</a> dan kami akan memperbaikinya.</p>""",
    "sources_label": "Halaman Kahf Browser yang kami baca:",
}

_CWS = "https://chromewebstore.google.com/detail/akhibrowser/ghkpflipnhahpjdnpoclaakbecnopamk"
_AMO = "https://addons.mozilla.org/en-US/firefox/addon/akhibrowser/"
_ALL5 = "Windows, macOS, Linux, Android, iOS"

COMPARE_BROWSERS = {
    "seo_title": "Perbandingan browser halal: AkhiBrowser, Kahf Browser, Brave, Firefox, dan Chrome",
    "title": "Perbandingan AkhiBrowser, Kahf Browser, Brave, Firefox, dan Chrome",
    "description": "Browser mana yang menyaring konten haram, memburamkan gambar, menghapus musik latar, dan punya kontrol orang tua? AkhiBrowser, Kahf Browser, Brave, Firefox, dan Chrome berdampingan.",
    "lead": "Apa yang dilakukan setiap browser tanpa pengaturan, tanpa ekstensi tambahan, seperti yang dijelaskan masing-masing di halamannya sendiri, per 9 November 2026, dan 15 November 2026 untuk AkhiBrowser. Kami belum menguji Kahf Browser sendiri; lihat <a href=\"/id/compare/kahf-browser/\">perbandingan rinci dengan Kahf Browser</a>.",
    "head": ["", "AkhiBrowser", "Kahf Browser", "Brave", "Firefox", "Chrome"],
    "rows": [
        ["Harga", "Perlindungan gratis; Premium dan Family Premium opsional", "Gratis", "Gratis", "Gratis", "Gratis"],
        ["Platform", f"Windows (Microsoft Store), Android (Google Play); ekstensi gratis yang lebih ringan untuk <a href=\"{_CWS}\">Chrome</a> dan <a href=\"{_AMO}\">Firefox</a>", "Windows, macOS, Android, iOS", _ALL5, _ALL5, _ALL5],
        ["Situs dewasa dan haram", "Diblokir, sejak halaman pertama", "Diblokir", "Tidak", "Tidak", "Tidak"],
        ["Pencarian haram diblokir", "Ya, dalam 11 bahasa", "Safe Search, termasuk saran", "Tidak", "Tidak", "Tidak"],
        ["Ketelanjangan dalam gambar", "Buram sampai diperiksa di perangkatmu", "Diburamkan", "Tidak", "Tidak", "Tidak"],
        ["SafeSearch dan Mode Terbatas YouTube dipaksakan", "Ya", "Ya", "Tidak", "Tidak", "Dengan pengawasan Family Link"],
        ["Kontrol orang tua (PIN, daftar situs, batas waktu)", "Family Premium", _NS, "Tidak", "Tidak", "Dengan Google Family Link"],
        ["Laporan untuk orang tua", "Family Premium, lewat email", _NS, "Tidak", "Tidak", "Dengan Google Family Link"],
        ["Perlindungan bisa dimatikan anak", "Tidak dengan PIN orang tua", _NS, "Ya", "Ya", "Tergantung Family Link"],
        ["Hapus musik latar dari video", "Gratis, di perangkatmu", _NS, "Tidak", "Tidak", "Tidak"],
        ["Iklan dan pelacak", "Diblokir, uBlock Origin bawaan", "Diblokir", "Diblokir (Shields)", "Pelacak diblokir; iklan perlu ekstensi", "Tidak diblokir; pemblokir iklan terbatas"],
        ["Pilih siapa yang diburamkan, mengenali hijab", "Premium", _NS, "Tidak", "Tidak", "Tidak"],
        ["YouTube yang lebih tenang", "Premium: tanpa rekomendasi, Shorts, atau putar otomatis", "Safe YouTube", "Tidak", "Tidak", "Tidak"],
        ["Waktu salat dan ayat hari ini", "Gratis", "Waktu salat", "Tidak", "Tidak", "Tidak"],
        ["Cek halal, peringatan riba, jeda salat", "Family Premium", _NS, "Tidak", "Tidak", "Tidak"],
        ["Dibangun di atas", "Firefox", "Chromium", "Chromium", "Mesin milik Firefox sendiri", "Chromium"],
    ],
    "after": """<h2>Singkatnya</h2>
<p><strong>Brave, Firefox, dan Chrome</strong> adalah browser umum yang bagus, tetapi tidak satu pun yang menyaring konten haram atau memburamkan gambar dengan sendirinya. Kamu akan butuh ekstensi, yang bisa dihapus oleh anak.</p>
<p><strong>Kahf Browser dan AkhiBrowser</strong> dibuat untuk Muslim dan menyaring sejak awal. AkhiBrowser menambahkan penghapusan musik latar, pilihan siapa yang diburamkan, kontrol orang tua dengan PIN dan laporan lewat email, serta cek halal, peringatan riba, dan jeda salat.</p>
<p>Melihat sesuatu yang sudah usang? Beri tahu kami di <a href="mailto:support@akhibrowser.com">support@akhibrowser.com</a> dan kami akan memperbaikinya. AkhiBrowser tidak berafiliasi dengan browser mana pun di sini.</p>""",
    "sources_label": "Halaman yang kami baca:",
}
