"""The Malay text of the blog and comparison pages. content.py merges it in; see build_pages.py and langs.py.

Each key in ARTICLES is an article slug from content.py. {YEAR} stands for the current year."""

UI = {
    "nav_label": "Menu utama",
    "blog": "Blog",
    "compare": "Bandingkan",
    "download": "Dapatkan AkhiBrowser",
    "blog_title": "Panduan melayari secara halal",
    "blog_lead": "Panduan praktikal untuk melayari web dengan kurang iklan, kurang kandungan haram dan lebih kawalan, pada peranti anda sendiri.",
    "cta_title": "Dapatkan AkhiBrowser",
    "cta_text": "Pelayar peribadi untuk umat Islam, dibina atas Firefox. Di Microsoft Store untuk Windows dan di Google Play untuk Android. Perlindungannya percuma.",
    "footer": "AkhiBrowser dibina atas <a href=\"https://www.firefox.com/\">Firefox</a>, dan tidak dibuat atau disokong oleh Mozilla. Penapis boleh terlepas sesuatu, dan ia tidak menggantikan penjagaan ibu bapa. <a href=\"/ms/\">Utama</a> · <a href=\"/ms/faq/\">Soalan lazim</a> · <a href=\"mailto:support@akhibrowser.com\">support@akhibrowser.com</a>",
}

ARTICLES = {
    "what-is-a-halal-browser": {
        "title": "Apakah pelayar halal, dan adakah anda memerlukannya?",
        "description": "Apa yang dilakukan pelayar halal, apa yang tidak dapat dilakukannya dan cara memilihnya: sekatan laman, SafeSearch, pengaburan gambar dan privasi diterangkan.",
        "body": """<p>Pelayar halal ialah pelayar web yang menapis apa yang dibiarkan oleh pelayar biasa kepada anda. Ia menyekat laman dan carian untuk perkara seperti kandungan dewasa, arak dan judi, dan menjauhkan gambar yang tidak diingini dari skrin anda.</p>
<h2>Apa yang biasanya dilakukan pelayar halal</h2>
<ul>
<li><strong>Menyekat laman.</strong> Laman dewasa, judi, arak dan dadah berhenti sebelum dimuatkan.</li>
<li><strong>Memaksa SafeSearch.</strong> Enjin carian menyembunyikan hasil yang lucah, tanpa anda perlu menetapkannya.</li>
<li><strong>Menapis gambar.</strong> Gambar yang menunjukkan kebogelan dikaburkan.</li>
<li><strong>Menyekat iklan dan penjejak.</strong> Banyak gambar yang tidak diingini datang melalui iklan, jadi ini membantu dua kali.</li>
</ul>
<h2>Apa yang tidak dapat dilakukannya</h2>
<p>Tiada penapis yang sempurna. Sesetengah halaman terlepas, dan sesetengah halaman yang tidak berbahaya disekat. Pelayar juga hanya melindungi apa yang berlaku di dalamnya: aplikasi dan pelayar lain pada peranti yang sama tidak dilindungi. Ia membantu niat dan tabiat, tetapi tidak menggantikannya, atau penjagaan ibu bapa.</p>
<h2>Cara memilihnya</h2>
<ul>
<li><strong>Di mana pemeriksaan dilakukan?</strong> Menapis pada peranti anda sendiri bermakna gambar anda tidak perlu meninggalkannya.</li>
<li><strong>Apa yang keluar dari peranti anda?</strong> Cari senarai yang jelas. Pelayar yang berkata "tiada" sepatutnya dapat menerangkan cara ia menyekat laman dan mengemas kini dirinya.</li>
<li><strong>Bolehkah anda mengawalnya?</strong> Anda sepatutnya dapat melihat dan mengubah setiap perlindungan.</li>
<li><strong>Adakah ia berjalan pada peranti anda?</strong> Semak sebelum membuat keputusan, terutamanya pada iPhone atau Mac.</li>
</ul>
<h2>Pelayar halal, sambungan pelayar atau penapis DNS?</h2>
<p>Ada tiga cara biasa untuk menapis web, dan ketiganya berfungsi paling baik bersama:</p>
<ul>
<li><strong>Pelayar halal</strong> menapis di dalam pelayar itu sendiri: laman, carian, gambar dan video. Perlindungannya aktif dari halaman pertama dan boleh dikunci dengan PIN.</li>
<li><strong>Sambungan pelayar</strong> menambah penapis pada pelayar yang sudah anda gunakan, seperti Chrome. Ia cepat dicuba, tetapi biasanya boleh dibuang atau dimatikan, dan tidak dapat mengubah cara pelayar itu sendiri berfungsi.</li>
<li><strong>Penapis DNS atau penghala</strong> menyekat keseluruhan laman untuk setiap aplikasi pada peranti atau rangkaian. Ia tidak dapat melihat ke dalam halaman, jadi ia tidak dapat mengaburkan gambar atau membuang muzik daripada video.</li>
</ul>
<p>Untuk keluarga, susunan biasa ialah DNS keluarga pada penghala serta pelayar halal pada setiap peranti, dengan pelayar lain dibuang atau disekat. Baca <a href="/ms/blog/block-haram-content/">cara menyekat kandungan haram pada telefon dan komputer anda</a> untuk persediaan penuh.</p>
<h2>Senarai semak untuk memilih pelayar halal</h2>
<ul>
<li>Adakah laman dewasa, judi, arak dan dadah disekat dari halaman pertama, tanpa persediaan?</li>
<li>Adakah SafeSearch dipaksa pada setiap enjin carian, termasuk YouTube?</li>
<li>Adakah gambar diperiksa pada peranti anda, atau dihantar ke pelayan?</li>
<li>Bolehkah ibu bapa mengunci tetapan dengan PIN?</li>
<li>Adakah ia menyatakan dengan jelas apa yang keluar dari peranti anda?</li>
<li>Adakah ia masih dikemas kini? Pelayar yang berhenti menerima kemas kini juga berhenti menerima pembaikan keselamatan. SalamWeb, salah satu pelayar halal terawal, dihentikan pada 2021.</li>
</ul>
<p>Kami membandingkan pilihan dalam <a href="/ms/blog/best-halal-browsers/">pelayar halal terbaik {YEAR}</a>.</p>
<h2>Soalan lazim</h2>
<h3>Adakah pelayar halal hanya untuk umat Islam?</h3>
<p>Tidak. Sesiapa yang mahukan kurang iklan, tiada kandungan dewasa dan lebih kawalan ke atas gambar boleh menggunakannya. Namanya menggambarkan nilai yang menjadi asasnya.</p>
<h3>Adakah pelayar halal percuma?</h3>
<p>Banyak yang percuma. Perlindungan AkhiBrowser percuma, dengan Premium pilihan untuk tetapan gambar tambahan dan alat ibu bapa.</p>
<h3>Adakah pelayar halal menggantikan kawalan ibu bapa?</h3>
<p>Ia meliputi pelayar. Untuk aplikasi dan pelayar lain, gabungkannya dengan kawalan peranti, seperti Google Family Link atau Microsoft Family Safety. Lihat <a href="/ms/blog/parental-controls-for-muslim-families/">persediaan kawalan ibu bapa yang mudah</a>.</p>
<h3>Bolehkah pelayar halal membuang muzik daripada video?</h3>
<p>Sesetengahnya boleh. AkhiBrowser <a href="/ms/blog/remove-background-music-from-videos/">membuang muzik latar pada peranti anda</a>, supaya suara kekal dan muzik hilang.</p>
<p>AkhiBrowser ialah satu pilihan, dibina atas Firefox untuk Windows dan Android. Perlindungannya aktif dari halaman pertama, dan <a href="/ms/privacy/">lamannya menyenaraikan apa yang keluar dari peranti anda</a>. Anda juga boleh membaca <a href="/ms/compare/kahf-browser/">perbandingannya dengan Kahf Browser</a>.</p>""",
    },
    "block-haram-content": {
        "title": "Cara menyekat kandungan haram pada telefon dan komputer anda",
        "description": "Langkah demi langkah untuk menyekat kandungan dewasa, judi dan arak: penapis pelayar, SafeSearch, DNS keluarga dan kawalan peranti, serta apa yang terlepas oleh setiap satu.",
        "body": """<p>Tiada satu tetapan yang menyekat semuanya. Yang berkesan ialah beberapa lapisan, setiap satu menutup apa yang terlepas oleh yang lain.</p>
<h2>1. Gunakan pelayar yang menapis secara lalai</h2>
<p>Pelayar yang menapis menyekat laman, menapis carian dan mengaburkan gambar tanpa persediaan. Dalam AkhiBrowser, laman dewasa, arak, dadah, vape dan judi disekat dari halaman pertama.</p>
<h2>2. Paksa SafeSearch</h2>
<p>SafeSearch menyembunyikan hasil lucah dalam enjin carian. Anda boleh menghidupkannya dalam tetapan setiap enjin carian, tetapi ia mudah dimatikan semula, dan hanya untuk satu pelayar. Pelayar yang menapis boleh memaksanya: AkhiBrowser melakukannya pada Google, Bing, DuckDuckGo dan Yahoo, dan menghidupkan Mod Terhad YouTube.</p>
<h2>3. Tambah DNS keluarga</h2>
<p>Perkhidmatan DNS keluarga enggan mencari laman dewasa, untuk semua yang ada pada rangkaian atau peranti itu. 1.1.1.3 daripada Cloudflare dan CleanBrowsing ialah pilihan yang terkenal. Ia berfungsi mengikut nama laman, jadi ia tidak dapat melihat apa yang ada pada laman yang dibenarkan, dan pengendalinya boleh melihat nama laman yang anda lawati.</p>
<h2>4. Tutup pintu belakang</h2>
<p>Penapis pelayar tidak meliputi aplikasi lain. Pada peranti kanak-kanak, gunakan Google Family Link pada Android atau Microsoft Family Safety pada Windows untuk mengawal aplikasi dan pelayar mana yang boleh dipasang. Dalam AkhiBrowser, Family Premium juga boleh mengunci tetapan dengan PIN dan mematikan tab peribadi.</p>
<h2>5. Teruskan perbualan</h2>
<p>Penapis boleh terlepas sesuatu, dan ia tidak berfungsi pada telefon kawan. Bagi kanak-kanak, tahu apa yang perlu dilakukan apabila sesuatu muncul di skrin lebih penting daripada sebarang tetapan.</p>""",
    },
    "remove-background-music-from-videos": {
        "title": "Cara membuang muzik latar daripada video dalam pelayar anda",
        "description": "Bagaimana pemisahan suara pada peranti membuang muzik latar daripada video dalam talian dan mengekalkan pertuturan, di mana ia berfungsi dengan baik dan di mana ia sukar.",
        "body": """<p>Banyak ceramah, dokumentari dan klip berita mempunyai muzik latar yang mungkin anda lebih suka tidak dengar. Membisukan bunyi bukan pilihan apabila anda mahu mendengar pertuturan. Pemisahan suara menyelesaikannya: model pertuturan kecil mengekalkan suara dan membuang yang lain.</p>
<p>Ulama berbeza pendapat tentang muzik, dan artikel ini tidak cuba memutuskannya. Ia hanya menerangkan apa yang boleh dilakukan teknologi ini, bagi yang mahukannya.</p>
<h2>Cara ia berfungsi</h2>
<p>Model pertuturan mendengar bunyi video dalam keratan pendek dan menganggar bahagian mana yang merupakan suara manusia. Yang selebihnya dikeluarkan sebelum sampai ke pembesar suara anda. Menjalankannya pada peranti anda bermakna audio tidak perlu dihantar ke mana-mana.</p>
<h2>Cara menggunakannya dalam AkhiBrowser</h2>
<ol>
<li>Pasang AkhiBrowser pada Windows atau Android.</li>
<li>Mainkan video. No music hidup secara lalai.</li>
<li>Untuk mematikannya, buka perisai AkhiBrowser di bar alat. Pada Android: menu, kemudian Sambungan, kemudian AkhiBrowser.</li>
</ol>
<p>Telefon dan komputer yang lebih perlahan menggunakan model yang lebih ringan, supaya dapat mengikutinya.</p>
<h2>Di mana ia kurang berkesan</h2>
<ul>
<li><strong>Nyanyian.</strong> Suara yang menyanyi tetap suara, jadi model perlu memutuskan apa yang dilakukan dengannya.</li>
<li><strong>Muzik kuat di atas pertuturan perlahan.</strong> Sedikit muzik mungkin kekal, dan suara mungkin kedengaran lebih nipis.</li>
<li><strong>Laman yang menyekat akses kepada audionya.</strong> Sesetengah video yang dilindungi tidak dapat diproses.</li>
</ul>
<p>Ciri ini dibina daripada <a href="https://github.com/mohamedsadiqaguenaou/NoMusic">NoMusic oleh Mohamed Sadiq</a>.</p>""",
    },
    "parental-controls-for-muslim-families": {
        "title": "Kawalan ibu bapa untuk keluarga Islam: persediaan mudah",
        "description": "Persediaan mudah untuk ibu bapa: pelayar yang menapis, PIN, laman yang diluluskan untuk kanak-kanak kecil, waktu tidur dan waktu sekolah, dan apa yang tidak dapat dikawal oleh mana-mana pelayar.",
        "body": """<p>Kawalan ibu bapa yang baik sepadan dengan umur anak. Ini ialah titik permulaan yang munasabah, menggunakan kawalan Family Premium dalam AkhiBrowser. Setiap satu mati sehingga anda menghidupkannya, dan datanya kekal pada peranti.</p>
<h2>Pertama, untuk semua umur</h2>
<ol>
<li>Tetapkan PIN ibu bapa, supaya perlindungan tidak boleh dimatikan tanpanya.</li>
<li>Hidupkan <strong>Tiada tab peribadi</strong>, supaya pelayaran kekal di bawah kawalan.</li>
<li>Buang pelayar lain dari peranti, atau sekat dengan Google Family Link atau Microsoft Family Safety. Pelayar tidak dapat mengawal apa yang berlaku di luarnya.</li>
</ol>
<h2>Kanak-kanak kecil</h2>
<p>Gunakan <strong>Benarkan hanya laman yang diluluskan</strong> dan tambah beberapa laman yang mereka gunakan. Yang lain kekal tertutup, yang jauh lebih kukuh daripada cuba menyekat bahagian buruk web.</p>
<h2>Kanak-kanak yang lebih besar</h2>
<p>Buka web, tetapi tetapkan had. <strong>Sekat laman pilihan</strong> meliputi laman tertentu yang menimbulkan masalah, dan <strong>Had masa</strong> menetapkan had harian, waktu tidur dan waktu sekolah. <strong>Had suapan</strong> menyembunyikan suapan video pendek dan menghentikan laman media sosial selepas masa yang ditetapkan. Ia berfungsi pada laman web dalam AkhiBrowser, bukan dalam aplikasi media sosial.</p>
<h2>Remaja</h2>
<p>Kepercayaan bertambah dengan umur. <strong>Ringkasan aktiviti</strong> menunjukkan berapa banyak halaman disekat dan sebabnya, tanpa alamatnya. Ia permulaan perbualan, bukan pengawasan.</p>
<h2>Apabila anda perlukan rehat</h2>
<p><strong>Jeda internet</strong> menghentikan pelayaran serta-merta, dengan PIN untuk menyambung. Ia berguna semasa makan dan sekitar waktu solat.</p>
<p>Lihat <a href="/ms/#premium">pelan dan harga</a>. Perlindungan percuma berfungsi tanpa semua ini.</p>""",
    },
    "why-prayer-times-differ": {
        "title": "Mengapa waktu solat berbeza antara aplikasi dan masjid",
        "description": "Mengapa Subuh dan Isyak boleh berbeza lebih setengah jam antara aplikasi: kaedah pengiraan diterangkan, dengan contoh sebenar dari Almere di Belanda.",
        "body": """<p>Dua aplikasi boleh menunjukkan waktu berbeza untuk solat yang sama di bandar yang sama. Biasanya tiada yang rosak: ia menggunakan kaedah pengiraan yang berbeza.</p>
<h2>Apa yang sama, dan apa yang berubah</h2>
<p>Zuhur dan Maghrib mengikut kedudukan matahari, jadi kebanyakan kaedah bersetuju tentangnya. Subuh dan Isyak bergantung pada fajar dan senja, apabila matahari berada pada sudut tertentu di bawah ufuk, dan kaedah memilih sudut yang berbeza. Asar juga berbeza mengikut mazhab: waktu Hanafi lebih lewat daripada yang biasa.</p>
<h2>Contoh sebenar</h2>
<p>Ini ialah waktu untuk Almere, Belanda, pada 8 November 2026, daripada <a href="https://aladhan.com/prayer-times-api">perkhidmatan pengiraan awam Aladhan</a>:</p>
<div class="table"><table>
<thead><tr><th scope="col">Kaedah</th><th scope="col">Subuh</th><th scope="col">Isyak</th></tr></thead>
<tbody>
<tr><th scope="row">Maghribi</th><td>05:43</td><td>18:48</td></tr>
<tr><th scope="row">Liga Muslim Sedunia</th><td>05:50</td><td>18:48</td></tr>
<tr><th scope="row">Karachi</th><td>05:50</td><td>18:55</td></tr>
<tr><th scope="row">Moonsighting Committee</th><td>06:09</td><td>18:26</td></tr>
<tr><th scope="row">ISNA</th><td>06:10</td><td>18:35</td></tr>
<tr><th scope="row">Perancis (UOIF)</th><td>06:30</td><td>18:15</td></tr>
</tbody>
</table></div>
<p>Itu 47 minit antara Subuh paling awal dan paling lewat. Jauh dari khatulistiwa, perbezaannya berubah mengikut musim, dan pada musim panas fajar sebenar mungkin tidak berlaku langsung, jadi kaedah juga memerlukan peraturan untuk latitud tinggi.</p>
<h2>Yang mana patut anda gunakan?</h2>
<p>Untuk soalan amalan, tanya masjid tempatan anda atau ulama yang anda percayai, dan ikut apa yang digunakan komuniti anda. Aplikasi hanya boleh mengira.</p>
<h2>Waktu solat dalam AkhiBrowser</h2>
<p>AkhiBrowser mengira waktu solat pada peranti anda daripada bandar yang anda pilih, tanpa menggunakan lokasi anda. Ia memilih kaedah mengikut negara, dan anda boleh mengubah kaedah dan waktu Asar dalam pilihannya.</p>""",
    },
    "best-halal-browsers": {
        "title": "Pelayar halal terbaik {YEAR}, dibandingkan",
        "description": "Perbandingan jujur pelayar halal yang boleh anda gunakan pada {YEAR}: AkhiBrowser, Kahf Browser dan Tahir Browser, serta apa yang berlaku kepada SalamWeb. Platform, harga dan ciri.",
        "body": """<p>Pelayar halal menyekat laman haram, memaksa SafeSearch dan menjauhkan gambar yang tidak diingini dari skrin anda. Pada {YEAR} ada tiga pilihan aktif yang patut diketahui. Salah satunya, AkhiBrowser, kami buat sendiri, jadi halaman ini berpegang pada apa yang dinyatakan setiap pelayar di halamannya sendiri, dan menyatakan dengan jelas di mana setiap satu paling sesuai.</p>
<h2>Jawapan ringkas</h2>
<ul>
<li><strong>Pada Windows, atau untuk kawalan ibu bapa:</strong> AkhiBrowser. Perlindungan percuma, pembuangan muzik latar, dan Family Premium dengan PIN, senarai laman dan had masa.</li>
<li><strong>Pada Mac, atau untuk pelayar serba percuma pada semua platform:</strong> Kahf Browser. Windows, macOS, Android dan iOS, percuma tanpa pembelian dalam aplikasi.</li>
<li><strong>Pada iPhone:</strong> Tahir Browser atau Kahf Browser. AkhiBrowser belum ada pada iOS.</li>
</ul>
<h2>AkhiBrowser</h2>
<p>Pelayar halal yang dibina atas Firefox, untuk Windows dan Android. Laman dewasa, arak, dadah, vape dan judi disekat dari halaman pertama, SafeSearch dipaksa pada Google, Bing, DuckDuckGo, Yahoo dan YouTube, dan gambar kekal kabur sehingga diperiksa pada peranti anda. Ia satu-satunya daripada tiga yang membuang muzik latar daripada video, pada peranti anda. Perlindungannya percuma; Premium menambah pilihan siapa yang dikaburkan, dan Family Premium menambah PIN ibu bapa, senarai laman, had masa dan butang jeda.</p>
<h2>Kahf Browser</h2>
<p>Pelayar berasaskan Chromium untuk umat Islam pada Windows, macOS, Android dan iOS. Lamannya menyatakan ia percuma pada semua platform tanpa langganan atau pembelian dalam aplikasi, menyekat iklan, laman dewasa dan haram dengan penapisan AI dan pangkalan data, memaksa SafeSearch dan Safe YouTube, mengaburkan kebogelan secara masa nyata, dan menyertakan waktu solat dan arah kiblat. Kebanyakan sambungan Chrome berfungsi di dalamnya.</p>
<h2>Tahir Browser</h2>
<p>Pelayar untuk iPhone dan iPad oleh Ihya Tech. Halaman App Store-nya menerangkan pengaburan semua gambar atau menggunakan AI untuk mengaburkan jantina berlawanan, ketik untuk melihat, menyekat laman haram, iklan dan penjejak, peringatan Islam, SafeSearch yang dipaksa dan kunci kata laluan atau biometrik pada perisainya. Ia percuma dimuat turun, dengan pelan bulanan dan tahunan pilihan.</p>
<h2>Apa yang berlaku kepada SalamWeb?</h2>
<p>SalamWeb ialah salah satu pelayar halal terawal dan mendapat liputan akhbar yang luas pada 2019. Ia dihentikan pada 2021 dan laman webnya sudah tiada, jadi ia bukan lagi pilihan. Ini peringatan yang baik untuk memilih pelayar yang masih dikemas kini, kerana kemas kini membawa pembaikan keselamatan.</p>
<h2>Sebelah-menyebelah</h2>
<div class="table"><table>
<thead><tr><th scope="col"></th><th scope="col">AkhiBrowser</th><th scope="col">Kahf Browser</th><th scope="col">Tahir Browser</th></tr></thead>
<tbody>
<tr><th scope="row">Platform</th><td>Windows, Android</td><td>Windows, macOS, Android, iOS</td><td>iPhone, iPad</td></tr>
<tr><th scope="row">Harga</th><td>Perlindungan percuma; Premium pilihan</td><td>Percuma</td><td>Percuma; pelan pilihan</td></tr>
<tr><th scope="row">Dibina atas</th><td>Firefox</td><td>Chromium</td><td>iOS WebKit</td></tr>
<tr><th scope="row">Laman haram disekat</th><td>Ya</td><td>Ya</td><td>Ya</td></tr>
<tr><th scope="row">SafeSearch dipaksa</th><td>Ya, termasuk YouTube</td><td>Ya, termasuk YouTube</td><td>Ya</td></tr>
<tr><th scope="row">Pengaburan gambar</th><td>Sehingga diperiksa, pada peranti anda</td><td>Masa nyata</td><td>Semua gambar, atau AI mengikut jantina</td></tr>
<tr><th scope="row">Pembuangan muzik latar</th><td>Ya</td><td>Tidak dinyatakan</td><td>Tidak dinyatakan</td></tr>
<tr><th scope="row">PIN ibu bapa dan had masa</th><td>Family Premium</td><td>Tidak dinyatakan</td><td>Kunci perisai</td></tr>
</tbody>
</table></div>
<p>&quot;Tidak dinyatakan&quot; bermakna kami tidak menemuinya di halaman pelayar itu sendiri, bukan bermakna ia tiada. Untuk jadual yang lebih panjang, lihat <a href="/ms/compare/kahf-browser/">perbandingan AkhiBrowser dan Kahf Browser</a> dan <a href="/ms/compare/browsers/">perbandingan AkhiBrowser, Kahf, Brave, Firefox dan Chrome</a>. Baru dengan topik ini? Mulakan dengan <a href="/ms/blog/what-is-a-halal-browser/">apakah pelayar halal</a>.</p>
<p>Disemak dengan halaman setiap pelayar pada 10 November 2026. Nampak sesuatu yang sudah lapuk? Beritahu kami di <a href="mailto:support@akhibrowser.com">support@akhibrowser.com</a>.</p>""",
    },
}

_NS = "Tidak dinyatakan"

COMPARE = {
    "seo_title": "AkhiBrowser lwn Kahf Browser: perbandingan ciri, harga dan platform",
    "title": "Perbandingan AkhiBrowser dan Kahf Browser",
    "description": "AkhiBrowser dan Kahf Browser sebelah-menyebelah: harga, platform, penapisan, gambar, pembuangan muzik, waktu solat dan kawalan ibu bapa, daripada halaman setiap pelayar.",
    "lead": "Kedua-duanya pelayar untuk umat Islam. Jadual ini menyenaraikan apa yang dinyatakan setiap satu di laman webnya sendiri, setakat 8 November 2026 untuk Kahf Browser dan 22 November 2026 untuk AkhiBrowser. Kami belum menguji Kahf Browser sendiri. &quot;Tidak dinyatakan&quot; bermakna kami tidak menemuinya di halaman yang kami baca, bukan bermakna ciri itu tiada.",
    "head": ["", "AkhiBrowser", "Kahf Browser"],
    "rows": [
        ["Harga", "Perlindungan percuma. Premium pilihan €3.99 sebulan, €39 setahun atau €119 sekali; Family Premium €59.99 setahun", "Percuma pada semua platform, tanpa langganan atau pembelian dalam aplikasi"],
        ["Platform", "Windows (Microsoft Store), Android (Google Play). iOS dan macOS: <a href=\"/ms/#roadmap\">dalam pelan hala tuju</a>, belum ada tarikh", "Windows, macOS, Android, iOS. Linux: disenaraikan dalam FAQ-nya, halaman muat turunnya kata akan datang"],
        ["Laman dewasa dan haram", "Disekat: dewasa, arak, dadah, vape dan judi", "Disekat, dengan penapisan AI dan pangkalan data"],
        ["Carian haram", "Disekat dalam 11 bahasa; soalan tentangnya tetap dibenarkan", "Safe Search, termasuk cadangan carian"],
        ["Kebogelan dalam gambar", "Kabur sehingga diperiksa pada peranti anda: gambar, latar belakang, video dan kanvas; dalam video secara masa nyata: setiap babak baharu terus dikaburkan dan diperiksa", "Dikaburkan secara masa nyata"],
        ["SafeSearch", "Dipaksa pada Google, Bing, DuckDuckGo dan Yahoo, serta Mod Terhad YouTube", "Dikuatkuasakan pada enjin carian utama; Safe YouTube"],
        ["PIN ibu bapa, senarai laman, had masa", "Family Premium: PIN, laman disekat atau hanya yang diluluskan, waktu tidur dan waktu sekolah, had harian", _NS],
        ["Laporan ibu bapa dan ringkasan aktiviti", "Family Premium: e-mel apabila perlindungan atau PIN dimatikan, ringkasan mingguan sekatan mengikut sebab, dan ringkasan 7 hari pada peranti", _NS],
        ["Jeda internet", "Family Premium, dengan PIN; kawalan ibu bapa boleh dipindahkan ke peranti lain dalam fail yang dikunci dengan PIN", _NS],
        ["Suapan media sosial dan aplikasi", "Family Premium: suapan video pendek disembunyikan, had harian untuk laman media sosial, aplikasi disekat pada Android", _NS],
        ["Buang muzik latar daripada video", "Percuma, pada peranti anda", _NS],
        ["Iklan dan penjejak", "Disekat, dengan uBlock Origin dan penyekat terbina dalam", "Penyekat terbina dalam"],
        ["Laman pancingan data dan penipuan", "Disekat", "Disekat"],
        ["Pilih siapa yang dikaburkan (wanita, lelaki)", "Premium", _NS],
        ["Mengenali tudung", "Premium", _NS],
        ["Mod ketat", "Premium: setiap gambar dan video kekal kabur sehingga anda mengetiknya", _NS],
        ["YouTube", "Mod Terhad, percuma. Premium: tiada cadangan, Shorts atau main automatik. Family Premium: Deen Time, hanya saluran pilihan anda", "Safe YouTube"],
        ["Waktu solat", "Percuma, untuk bandar pilihan anda, tanpa lokasi anda; peringatan pada komputer", "Waktu solat dan pemberitahuan"],
        ["Jeda solat", "Family Premium: laman media sosial, video dan permainan dijeda beberapa minit selepas setiap waktu solat", _NS],
        ["Semakan halal dan tempat halal", "Family Premium: amaran pada halaman produk dengan babi, arak, gelatin atau nombor E yang meragukan; tempat halal di Google Maps dan laman penghantaran", _NS],
        ["Amaran riba, loot box", "Family Premium: amaran pada halaman pinjaman berfaedah, kad kredit dan beli sekarang bayar kemudian; laman buka peti dan judi skin disekat", _NS],
        ["Bacaan al-Quran, sumber dipercayai", "Family Premium: ikuti bacaan di YouTube ayat demi ayat dengan maknanya; sumber ulama dahulu apabila mencari tentang Islam", _NS],
        ["Ayat hari ini", "Percuma", _NS],
        ["Kiblat", "Ya, di Android: kompas di bawah waktu solat", "Ya"],
        ["Bahasa", "12, termasuk Arab, Urdu, Parsi, Kurdi dan Turki", _NS],
        ["Pembetulan buta warna", "Percuma, pada peranti anda", _NS],
        ["Perlu akaun", "Tidak", "Tidak; log masuk tersedia"],
        ["Dibina atas", "Firefox", "Chromium; kebanyakan sambungan Chrome berfungsi"],
        ["Kod sumber", "Perubahan Firefox dan fail MPL terbuka kepada umum; sambungannya sendiri tertutup", "Belum terbuka, menurut FAQ-nya"],
    ],
    "after": """<h2>Yang mana sesuai untuk anda?</h2>
<p><strong>Kahf Browser</strong> sesuai jika anda menggunakan iPhone atau Mac, atau mahukan semuanya percuma.</p>
<p><strong>AkhiBrowser</strong> sesuai jika anda mahu muzik latar dibuang, mahu memilih siapa yang dikaburkan, atau memerlukan kawalan ibu bapa seperti PIN, had masa dan laporan melalui e-mel, pada Windows atau Android. Family Premium menambah apa yang tidak disenaraikan Kahf: semakan halal semasa membeli-belah, amaran riba dan jeda selepas setiap solat.</p>
<p>Kedua-duanya percuma untuk dicuba, jadi ujian terbaik ialah penggunaan anda sendiri. AkhiBrowser tidak bergabung dengan Kahf. Nampak sesuatu yang sudah lapuk? Beritahu kami di <a href="mailto:support@akhibrowser.com">support@akhibrowser.com</a> dan kami akan membetulkannya.</p>""",
    "sources_label": "Halaman Kahf Browser yang kami baca:",
}

_CWS = "https://chromewebstore.google.com/detail/akhibrowser/ghkpflipnhahpjdnpoclaakbecnopamk"
_AMO = "https://addons.mozilla.org/en-US/firefox/addon/akhibrowser/"
_ALL5 = "Windows, macOS, Linux, Android, iOS"

COMPARE_BROWSERS = {
    "seo_title": "Perbandingan pelayar halal: AkhiBrowser, Kahf Browser, Brave, Firefox dan Chrome",
    "title": "Perbandingan AkhiBrowser, Kahf Browser, Brave, Firefox dan Chrome",
    "description": "Pelayar mana yang menapis kandungan haram, mengaburkan gambar, membuang muzik latar dan mempunyai kawalan ibu bapa? AkhiBrowser, Kahf Browser, Brave, Firefox dan Chrome sebelah-menyebelah.",
    "lead": "Apa yang dilakukan setiap pelayar secara asal, tanpa sambungan tambahan, seperti yang diterangkan setiap satu di halamannya sendiri, setakat 9 November 2026, dan 15 November 2026 untuk AkhiBrowser. Kami belum menguji Kahf Browser sendiri; lihat <a href=\"/ms/compare/kahf-browser/\">perbandingan terperinci dengan Kahf Browser</a>.",
    "head": ["", "AkhiBrowser", "Kahf Browser", "Brave", "Firefox", "Chrome"],
    "rows": [
        ["Harga", "Perlindungan percuma; Premium dan Family Premium pilihan", "Percuma", "Percuma", "Percuma", "Percuma"],
        ["Platform", f"Windows (Microsoft Store), Android (Google Play); sambungan percuma yang lebih ringan untuk <a href=\"{_CWS}\">Chrome</a> dan <a href=\"{_AMO}\">Firefox</a>", "Windows, macOS, Android, iOS", _ALL5, _ALL5, _ALL5],
        ["Laman dewasa dan haram", "Disekat, dari halaman pertama", "Disekat", "Tidak", "Tidak", "Tidak"],
        ["Carian haram disekat", "Ya, dalam 11 bahasa", "Safe Search, termasuk cadangan", "Tidak", "Tidak", "Tidak"],
        ["Kebogelan dalam gambar", "Kabur sehingga diperiksa pada peranti anda", "Dikaburkan", "Tidak", "Tidak", "Tidak"],
        ["SafeSearch dan Mod Terhad YouTube dipaksa", "Ya", "Ya", "Tidak", "Tidak", "Dengan pengawasan Family Link"],
        ["Kawalan ibu bapa (PIN, senarai laman, had masa)", "Family Premium", _NS, "Tidak", "Tidak", "Dengan Google Family Link"],
        ["Laporan untuk ibu bapa", "Family Premium, melalui e-mel", _NS, "Tidak", "Tidak", "Dengan Google Family Link"],
        ["Perlindungan boleh dimatikan oleh kanak-kanak", "Tidak dengan PIN ibu bapa", _NS, "Ya", "Ya", "Bergantung pada Family Link"],
        ["Buang muzik latar daripada video", "Percuma, pada peranti anda", _NS, "Tidak", "Tidak", "Tidak"],
        ["Iklan dan penjejak", "Disekat, uBlock Origin terbina dalam", "Disekat", "Disekat (Shields)", "Penjejak disekat; iklan memerlukan sambungan", "Tidak disekat; penyekat iklan terhad"],
        ["Pilih siapa yang dikaburkan, mengenali tudung", "Premium", _NS, "Tidak", "Tidak", "Tidak"],
        ["YouTube yang lebih tenang", "Premium: tiada cadangan, Shorts atau main automatik", "Safe YouTube", "Tidak", "Tidak", "Tidak"],
        ["Waktu solat dan ayat hari ini", "Percuma", "Waktu solat", "Tidak", "Tidak", "Tidak"],
        ["Semakan halal, amaran riba, jeda solat", "Family Premium", _NS, "Tidak", "Tidak", "Tidak"],
        ["Dibina atas", "Firefox", "Chromium", "Chromium", "Enjin Firefox sendiri", "Chromium"],
    ],
    "after": """<h2>Ringkasnya</h2>
<p><strong>Brave, Firefox dan Chrome</strong> ialah pelayar umum yang baik, tetapi tiada satu pun yang menapis kandungan haram atau mengaburkan gambar dengan sendirinya. Anda memerlukan sambungan, yang boleh dibuang oleh kanak-kanak.</p>
<p><strong>Kahf Browser dan AkhiBrowser</strong> dibuat untuk umat Islam dan menapis dari awal. AkhiBrowser menambah pembuangan muzik latar, pilihan siapa yang dikaburkan, kawalan ibu bapa dengan PIN dan laporan melalui e-mel, serta semakan halal, amaran riba dan jeda solat.</p>
<p>Nampak sesuatu yang sudah lapuk? Beritahu kami di <a href="mailto:support@akhibrowser.com">support@akhibrowser.com</a> dan kami akan membetulkannya. AkhiBrowser tidak bergabung dengan mana-mana pelayar ini.</p>""",
    "sources_label": "Halaman yang kami baca:",
}
