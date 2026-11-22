"""The Turkish text of the blog and comparison pages. content.py merges it in; see build_pages.py and langs.py.

Each key in ARTICLES is an article slug from content.py. {YEAR} stands for the current year."""

UI = {
    "nav_label": "Ana menü",
    "blog": "Blog",
    "compare": "Karşılaştır",
    "download": "AkhiBrowser'ı al",
    "blog_title": "Helal gezinme rehberleri",
    "blog_lead": "Web'de daha az reklamla, daha az haram içerikle ve daha fazla kontrolle, kendi cihazında gezinmek için pratik rehberler.",
    "cta_title": "AkhiBrowser'ı al",
    "cta_text": "Müslümanlar için Firefox tabanlı, gizliliğe saygılı bir tarayıcı. Windows için Microsoft Store'da, Android için Google Play'de. Korumalar ücretsizdir.",
    "footer": "AkhiBrowser <a href=\"https://www.firefox.com/\">Firefox</a> tabanlıdır ve Mozilla tarafından yapılmamış veya onaylanmamıştır. Filtreler bazı şeyleri kaçırabilir ve bir ebeveynin ilgisinin yerini tutmaz. <a href=\"/tr/\">Ana sayfa</a> · <a href=\"/tr/faq/\">Sık sorulan sorular</a> · <a href=\"mailto:support@akhibrowser.com\">support@akhibrowser.com</a>",
}

ARTICLES = {
    "what-is-a-halal-browser": {
        "title": "Helal tarayıcı nedir ve sana gerekli mi?",
        "description": "Helal bir tarayıcının ne yaptığı, neyi yapamadığı ve nasıl seçileceği: site engelleme, SafeSearch, görsel bulanıklaştırma ve gizlilik açıklandı.",
        "body": """<p>Helal tarayıcı, normal bir tarayıcının sana bıraktığı şeyleri filtreleyen bir web tarayıcısıdır. Yetişkin içerik, alkol ve kumar gibi şeylerin sitelerini ve aramalarını engeller ve istenmeyen görselleri ekranından uzak tutar.</p>
<h2>Helal bir tarayıcı genellikle ne yapar</h2>
<ul>
<li><strong>Siteleri engeller.</strong> Yetişkin, kumar, alkol ve uyuşturucu siteleri yüklenmeden durur.</li>
<li><strong>SafeSearch'ü zorunlu kılar.</strong> Arama motorları müstehcen sonuçları gizler, senin ayarlamana gerek kalmadan.</li>
<li><strong>Görselleri filtreler.</strong> Çıplaklık içeren resimler bulanıklaştırılır.</li>
<li><strong>Reklamları ve izleyicileri engeller.</strong> Birçok istenmeyen görsel reklamlarla gelir, bu yüzden bu iki kat yardımcı olur.</li>
</ul>
<h2>Neyi yapamaz</h2>
<p>Hiçbir filtre kusursuz değildir. Bazı sayfalar geçer, bazı zararsız sayfalar engellenir. Bir tarayıcı ayrıca yalnızca kendi içinde olanları korur: aynı cihazdaki diğer uygulamalar ve tarayıcılar kapsam dışıdır. Niyete ve alışkanlığa yardım eder ama onların yerini tutmaz, bir ebeveynin ilgisinin de.</p>
<h2>Nasıl seçilir</h2>
<ul>
<li><strong>Kontrol nerede yapılıyor?</strong> Kendi cihazında filtrelemek, görsellerinin cihazdan çıkmak zorunda olmadığı anlamına gelir.</li>
<li><strong>Cihazından ne çıkıyor?</strong> Açık bir liste ara. "Hiçbir şey" diyen bir tarayıcı, siteleri nasıl engellediğini ve kendini nasıl güncellediğini açıklayabilmeli.</li>
<li><strong>Onu kontrol edebiliyor musun?</strong> Her korumayı görebilmeli ve değiştirebilmelisin.</li>
<li><strong>Cihazlarında çalışıyor mu?</strong> Karar vermeden önce kontrol et, özellikle iPhone veya Mac'te.</li>
</ul>
<h2>Helal tarayıcı, tarayıcı uzantısı mı, DNS filtresi mi?</h2>
<p>Web'i filtrelemenin üç yaygın yolu var ve birlikte en iyi şekilde çalışırlar:</p>
<ul>
<li><strong>Helal bir tarayıcı</strong> tarayıcının kendi içinde filtreler: siteler, aramalar, görseller ve videolar. Korumaları ilk sayfadan itibaren açıktır ve bir PIN ile kilitlenebilir.</li>
<li><strong>Bir tarayıcı uzantısı</strong> zaten kullandığın bir tarayıcıya, örneğin Chrome'a, filtre ekler. Denemesi hızlıdır ama genellikle kaldırılabilir veya kapatılabilir ve tarayıcının kendisinin nasıl çalıştığını değiştiremez.</li>
<li><strong>Bir DNS veya modem filtresi</strong> bir cihazdaki veya ağdaki her uygulama için siteleri tamamen engeller. Bir sayfanın içine bakamaz, bu yüzden bir görseli bulanıklaştıramaz veya bir videodan müziği kaldıramaz.</li>
</ul>
<p>Bir aile için yaygın kurulum, modemde bir aile DNS'i artı her cihazda bir helal tarayıcıdır; diğer tarayıcılar kaldırılır veya engellenir. Tam kurulum için <a href="/tr/blog/block-haram-content/">telefonunda ve bilgisayarında haram içeriği nasıl engellersin</a> yazısını oku.</p>
<h2>Helal tarayıcı seçmek için bir kontrol listesi</h2>
<ul>
<li>Yetişkin, kumar, alkol ve uyuşturucu siteleri ilk sayfadan itibaren, kurulum olmadan engelleniyor mu?</li>
<li>SafeSearch, YouTube dahil her arama motorunda zorunlu mu?</li>
<li>Görseller cihazında mı kontrol ediliyor, yoksa bir sunucuya mı gönderiliyor?</li>
<li>Bir ebeveyn ayarları PIN ile kilitleyebiliyor mu?</li>
<li>Cihazından neyin çıktığını açıkça söylüyor mu?</li>
<li>Hâlâ güncelleniyor mu? Güncelleme almayan bir tarayıcı güvenlik düzeltmelerini de almaz. İlk helal tarayıcılardan biri olan SalamWeb 2021'de kapatıldı.</li>
</ul>
<p>Seçenekleri <a href="/tr/blog/best-halal-browsers/">{YEAR} yılının en iyi helal tarayıcıları</a> yazısında karşılaştırıyoruz.</p>
<h2>Sık sorulan sorular</h2>
<h3>Helal tarayıcı yalnızca Müslümanlar için mi?</h3>
<p>Hayır. Daha az reklam, yetişkin içerik olmaması ve görseller üzerinde daha fazla kontrol isteyen herkes kullanabilir. Ad, üzerine kurulduğu değerleri anlatır.</p>
<h3>Helal tarayıcı ücretsiz mi?</h3>
<p>Birçoğu öyle. AkhiBrowser'ın korumaları ücretsizdir; ek görsel ayarları ve ebeveyn araçları için isteğe bağlı Premium vardır.</p>
<h3>Helal tarayıcı ebeveyn denetimlerinin yerini tutar mı?</h3>
<p>Tarayıcıyı kapsar. Uygulamalar ve diğer tarayıcılar için onu Google Family Link veya Microsoft Family Safety gibi cihaz denetimleriyle birleştir. <a href="/tr/blog/parental-controls-for-muslim-families/">Basit bir ebeveyn denetimi kurulumuna</a> bak.</p>
<h3>Helal tarayıcı videolardan müziği kaldırabilir mi?</h3>
<p>Bazıları kaldırabilir. AkhiBrowser <a href="/tr/blog/remove-background-music-from-videos/">arka plan müziğini cihazında kaldırır</a>, böylece sesler kalır ve müzik gider.</p>
<p>AkhiBrowser, Windows ve Android için Firefox tabanlı bir seçenektir. Korumaları ilk sayfadan itibaren açıktır ve <a href="/tr/privacy/">sitesi cihazından neyin çıktığını listeler</a>. <a href="/tr/compare/kahf-browser/">Kahf Browser ile karşılaştırmasını</a> da okuyabilirsin.</p>""",
    },
    "block-haram-content": {
        "title": "Telefonunda ve bilgisayarında haram içerik nasıl engellenir",
        "description": "Yetişkin, kumar ve alkol içeriğini engellemenin adım adım yolu: tarayıcı filtreleri, SafeSearch, aile DNS'i ve cihaz denetimleri, ve her birinin neyi kaçırdığı.",
        "body": """<p>Tek bir ayar her şeyi engellemez. İşe yarayan, her biri diğerlerinin kaçırdığını kapatan birkaç katmandır.</p>
<h2>1. Varsayılan olarak filtreleyen bir tarayıcı kullan</h2>
<p>Filtreleyen bir tarayıcı, kurulum olmadan siteleri engeller, aramaları filtreler ve görselleri bulanıklaştırır. AkhiBrowser'da yetişkin, alkol, uyuşturucu, elektronik sigara ve kumar siteleri ilk sayfadan itibaren engellenir.</p>
<h2>2. SafeSearch'ü zorunlu kıl</h2>
<p>SafeSearch arama motorlarında müstehcen sonuçları gizler. Her arama motorunun ayarlarından açabilirsin, ama kolayca tekrar kapatılır ve yalnızca o tarayıcı için geçerlidir. Filtreleyen bir tarayıcı onu zorunlu kılabilir: AkhiBrowser bunu Google, Bing, DuckDuckGo ve Yahoo'da yapar ve YouTube'un Kısıtlı Modu'nu açar.</p>
<h2>3. Bir aile DNS'i ekle</h2>
<p>Bir aile DNS hizmeti, o ağdaki veya cihazdaki her şey için yetişkin siteleri aramayı reddeder. Cloudflare'in 1.1.1.3'ü ve CleanBrowsing bilinen seçeneklerdir. Site adına göre çalışır, bu yüzden izin verilen bir sitede ne olduğunu göremez ve onu işleten, ziyaret ettiğin sitelerin adlarını görebilir.</p>
<h2>4. Yan kapıları kapat</h2>
<p>Bir tarayıcı filtresi diğer uygulamaları kapsamaz. Bir çocuğun cihazında, hangi uygulama ve tarayıcıların yüklenebileceğini kontrol etmek için Android'de Google Family Link'i veya Windows'ta Microsoft Family Safety'yi kullan. AkhiBrowser'da Family Premium ayrıca ayarları PIN ile kilitleyebilir ve gizli sekmeleri kapatabilir.</p>
<h2>5. Konuşmayı sürdür</h2>
<p>Filtreler bazı şeyleri kaçırır ve bir arkadaşın telefonunda çalışmaz. Çocuklar için, ekranda bir şey belirdiğinde ne yapacaklarını bilmek her ayardan daha önemlidir.</p>""",
    },
    "remove-background-music-from-videos": {
        "title": "Tarayıcında videolardan arka plan müziği nasıl kaldırılır",
        "description": "Cihazdaki ses ayırmanın çevrimiçi videolardan arka plan müziğini nasıl kaldırıp konuşmayı koruduğu, nerede iyi çalıştığı ve nerede zorlandığı.",
        "body": """<p>Birçok sohbet, belgesel ve haber klibinde duymamayı tercih edebileceğin arka plan müziği vardır. Konuşmayı duymak istediğinde sesi kapatmak bir seçenek değildir. Ses ayırma bunu çözer: küçük bir konuşma modeli sesleri korur ve gerisini kaldırır.</p>
<p>Âlimler müzik konusunda farklı görüşlere sahiptir ve bu yazı bunu çözmeye çalışmaz. Yalnızca, isteyenler için teknolojinin neler yapabildiğini açıklar.</p>
<h2>Nasıl çalışır</h2>
<p>Bir konuşma modeli bir videonun sesini kısa parçalar halinde dinler ve hangi kısmın insan sesi olduğunu tahmin eder. Geri kalanı hoparlörlerine ulaşmadan çıkarılır. Cihazında çalışması, sesin hiçbir yere gönderilmesi gerekmediği anlamına gelir.</p>
<h2>AkhiBrowser'da nasıl kullanılır</h2>
<ol>
<li>AkhiBrowser'ı Windows'a veya Android'e yükle.</li>
<li>Bir video oynat. No music varsayılan olarak açıktır.</li>
<li>Kapatmak için araç çubuğundaki AkhiBrowser kalkanını aç. Android'de: menü, sonra Uzantılar, sonra AkhiBrowser.</li>
</ol>
<p>Telefonlar ve daha yavaş bilgisayarlar, yetişebilmek için daha hafif bir model kullanır.</p>
<h2>Nerede daha az iyi çalışır</h2>
<ul>
<li><strong>Şarkı söyleme.</strong> Şarkı söyleyen bir ses yine de bir sestir, bu yüzden model onunla ne yapacağına karar vermek zorundadır.</li>
<li><strong>Sessiz konuşmanın üzerinde yüksek müzik.</strong> Biraz müzik kalabilir ve ses daha ince çıkabilir.</li>
<li><strong>Seslerine erişimi engelleyen siteler.</strong> Bazı korumalı videolar işlenemez.</li>
</ul>
<p>Özellik, <a href="https://github.com/mohamedsadiqaguenaou/NoMusic">Mohamed Sadiq'in NoMusic</a> projesine dayanır.</p>""",
    },
    "parental-controls-for-muslim-families": {
        "title": "Müslüman aileler için ebeveyn denetimi: basit bir kurulum",
        "description": "Ebeveynler için basit bir kurulum: filtreleyen bir tarayıcı, bir PIN, küçük çocuklar için onaylı siteler, yatma ve okul saatleri, ve hiçbir tarayıcının kontrol edemediği şeyler.",
        "body": """<p>İyi ebeveyn denetimi çocuğun yaşına uyar. Bunlar, AkhiBrowser'daki Family Premium denetimlerini kullanan makul başlangıç noktalarıdır. Her biri sen açana kadar kapalıdır ve veriler cihazda kalır.</p>
<h2>Önce, her yaş için</h2>
<ol>
<li>Bir ebeveyn PIN'i belirle, böylece korumalar o olmadan kapatılamaz.</li>
<li>Gezinmenin denetim altında kalması için <strong>Gizli sekme yok</strong>'u aç.</li>
<li>Diğer tarayıcıları cihazdan kaldır veya Google Family Link ya da Microsoft Family Safety ile engelle. Bir tarayıcı kendi dışında olanları kontrol edemez.</li>
</ol>
<h2>Küçük çocuklar</h2>
<p><strong>Yalnızca onaylı sitelere izin ver</strong>'i kullan ve kullandıkları birkaç siteyi ekle. Geri kalan her şey kapalı kalır; bu, web'in kötü kısımlarını engellemeye çalışmaktan çok daha güçlüdür.</p>
<h2>Daha büyük çocuklar</h2>
<p>Web'i aç ama sınırlar koy. <strong>Seçilen siteleri engelle</strong> sorun çıkaran belirli siteleri kapsar ve <strong>Zaman sınırları</strong> günlük bir sınır, yatma ve okul saatleri belirler. <strong>Akış sınırı</strong> kısa video akışlarını gizler ve sosyal web sitelerini belirli bir süreden sonra durdurur. AkhiBrowser'daki web sitelerinde çalışır, sosyal medya uygulamalarında değil.</p>
<h2>Gençler</h2>
<p>Güven yaşla büyür. <strong>Etkinlik özeti</strong>, kaç sayfanın engellendiğini ve nedenini, adresleri olmadan gösterir. Bir sohbetin başlangıcıdır, gözetim değil.</p>
<h2>Bir molaya ihtiyacın olduğunda</h2>
<p><strong>İnterneti duraklat</strong> gezinmeyi hemen durdurur, devam etmek için PIN gerekir. Yemek saatlerinde ve namaz vakitlerinde işe yarar.</p>
<p><a href="/tr/#premium">Planlara ve fiyatlara</a> bak. Ücretsiz korumalar bunların hiçbiri olmadan çalışır.</p>""",
    },
    "why-prayer-times-differ": {
        "title": "Namaz vakitleri neden uygulamalar ve camiler arasında farklı",
        "description": "Sabah ve yatsı vakitleri neden uygulamalar arasında yarım saatten fazla farklı olabilir: hesaplama yöntemleri, Hollanda'daki Almere'den gerçek bir örnekle açıklandı.",
        "body": """<p>İki uygulama aynı şehirde aynı namaz için farklı vakitler gösterebilir. Genellikle hiçbiri bozuk değildir: farklı bir hesaplama yöntemi kullanırlar.</p>
<h2>Ne aynı kalır, ne değişir</h2>
<p>Öğle ve akşam güneşin konumunu takip eder, bu yüzden yöntemler çoğunlukla bunlarda anlaşır. Sabah ve yatsı, güneşin ufkun belirli bir açı altında olduğu alacakaranlığa bağlıdır ve yöntemler farklı açılar seçer. İkindi de mezhebe göre değişir: Hanefi vakti standart olandan daha geçtir.</p>
<h2>Gerçek bir örnek</h2>
<p>Bunlar, kamuya açık <a href="https://aladhan.com/prayer-times-api">Aladhan hesaplama hizmetine</a> göre 8 Kasım 2026'da Hollanda'nın Almere şehri için vakitlerdir:</p>
<div class="table"><table>
<thead><tr><th scope="col">Yöntem</th><th scope="col">Sabah</th><th scope="col">Yatsı</th></tr></thead>
<tbody>
<tr><th scope="row">Fas</th><td>05:43</td><td>18:48</td></tr>
<tr><th scope="row">Dünya Müslüman Birliği</th><td>05:50</td><td>18:48</td></tr>
<tr><th scope="row">Karaçi</th><td>05:50</td><td>18:55</td></tr>
<tr><th scope="row">Moonsighting Committee</th><td>06:09</td><td>18:26</td></tr>
<tr><th scope="row">ISNA</th><td>06:10</td><td>18:35</td></tr>
<tr><th scope="row">Fransa (UOIF)</th><td>06:30</td><td>18:15</td></tr>
</tbody>
</table></div>
<p>En erken ve en geç sabah arasında 47 dakika var. Ekvatordan uzakta farklar mevsimlere göre değişir ve yazın gerçek alacakaranlık hiç olmayabilir, bu yüzden yöntemlerin yüksek enlemler için de kurallara ihtiyacı vardır.</p>
<h2>Hangisini kullanmalısın?</h2>
<p>Bir uygulama sorusu için yerel camine veya güvendiğin bir âlime sor ve cemaatinin kullandığını takip et. Bir uygulama yalnızca hesap yapabilir.</p>
<h2>AkhiBrowser'da namaz vakitleri</h2>
<p>AkhiBrowser namaz vakitlerini seçtiğin şehirden, konumunu kullanmadan, cihazında hesaplar. Ülkeye göre bir yöntem seçer ve seçeneklerinde yöntemi ve ikindi vaktini değiştirebilirsin.</p>""",
    },
    "best-halal-browsers": {
        "title": "{YEAR} yılının en iyi helal tarayıcıları, karşılaştırmalı",
        "description": "{YEAR} yılında kullanabileceğin helal tarayıcıların dürüst bir karşılaştırması: AkhiBrowser, Kahf Browser ve Tahir Browser, ve SalamWeb'e ne oldu. Platformlar, fiyat ve özellikler.",
        "body": """<p>Helal bir tarayıcı haram siteleri engeller, SafeSearch'ü zorunlu kılar ve istenmeyen görselleri ekranından uzak tutar. {YEAR} yılında bilinmeye değer üç aktif seçenek var. Bunlardan birini, AkhiBrowser'ı, biz yapıyoruz; bu yüzden bu sayfa her tarayıcının kendi sayfalarında belirttiklerine bağlı kalır ve her birinin en iyi nereye uyduğunu açıkça söyler.</p>
<h2>Kısa cevap</h2>
<ul>
<li><strong>Windows'ta veya ebeveyn denetimleri için:</strong> AkhiBrowser. Ücretsiz korumalar, arka plan müziği kaldırma ve PIN, site listeleri ve zaman sınırlarıyla Family Premium.</li>
<li><strong>Mac'te veya her platformda tamamen ücretsiz bir tarayıcı için:</strong> Kahf Browser. Windows, macOS, Android ve iOS, uygulama içi satın alma olmadan ücretsiz.</li>
<li><strong>iPhone'da:</strong> Tahir Browser veya Kahf Browser. AkhiBrowser henüz iOS'ta yok.</li>
</ul>
<h2>AkhiBrowser</h2>
<p>Windows ve Android için Firefox tabanlı bir helal tarayıcı. Yetişkin, alkol, uyuşturucu, elektronik sigara ve kumar siteleri ilk sayfadan itibaren engellenir, SafeSearch Google, Bing, DuckDuckGo, Yahoo ve YouTube'da zorunludur ve görseller cihazında kontrol edilene kadar bulanık kalır. Üçünün içinde videolardan arka plan müziğini, cihazında, kaldıran tek tarayıcıdır. Korumalar ücretsizdir; Premium kimin bulanıklaştırılacağını seçmeyi, Family Premium ise ebeveyn PIN'i, site listeleri, zaman sınırları ve bir duraklatma düğmesi ekler.</p>
<h2>Kahf Browser</h2>
<p>Windows, macOS, Android ve iOS'ta Müslümanlar için Chromium tabanlı bir tarayıcı. Sitesine göre tüm platformlarda abonelik veya uygulama içi satın alma olmadan ücretsizdir, reklamları, yetişkin ve haram siteleri yapay zekâ filtresi ve bir veritabanıyla engeller, SafeSearch ve Safe YouTube'u zorunlu kılar, çıplaklığı gerçek zamanlı bulanıklaştırır ve namaz vakitleri ile kıbleyi içerir. Çoğu Chrome uzantısı onda çalışır.</p>
<h2>Tahir Browser</h2>
<p>Ihya Tech'in iPhone ve iPad tarayıcısı. App Store sayfası, tüm görselleri bulanıklaştırmayı veya yapay zekâyla karşı cinsi bulanıklaştırmayı, dokunarak açmayı, haram siteleri, reklamları ve izleyicileri engellemeyi, İslami hatırlatmaları, zorunlu SafeSearch'ü ve kalkanında şifre veya biyometrik kilidi anlatır. İndirmesi ücretsizdir, isteğe bağlı aylık ve yıllık planlar vardır.</p>
<h2>SalamWeb'e ne oldu?</h2>
<p>SalamWeb ilk helal tarayıcılardan biriydi ve 2019'da basında geniş yer buldu. 2021'de kapatıldı ve web sitesi yok, bu yüzden artık bir seçenek değil. Hâlâ güncellenen bir tarayıcı seçmek için iyi bir hatırlatma, çünkü güncellemeler güvenlik düzeltmeleri getirir.</p>
<h2>Yan yana</h2>
<div class="table"><table>
<thead><tr><th scope="col"></th><th scope="col">AkhiBrowser</th><th scope="col">Kahf Browser</th><th scope="col">Tahir Browser</th></tr></thead>
<tbody>
<tr><th scope="row">Platformlar</th><td>Windows, Android</td><td>Windows, macOS, Android, iOS</td><td>iPhone, iPad</td></tr>
<tr><th scope="row">Fiyat</th><td>Korumalar ücretsiz; isteğe bağlı Premium</td><td>Ücretsiz</td><td>Ücretsiz; isteğe bağlı planlar</td></tr>
<tr><th scope="row">Temeli</th><td>Firefox</td><td>Chromium</td><td>iOS WebKit</td></tr>
<tr><th scope="row">Haram siteler engellenir</th><td>Evet</td><td>Evet</td><td>Evet</td></tr>
<tr><th scope="row">SafeSearch zorunlu</th><td>Evet, YouTube dahil</td><td>Evet, YouTube dahil</td><td>Evet</td></tr>
<tr><th scope="row">Görsel bulanıklaştırma</th><td>Kontrol edilene kadar, cihazında</td><td>Gerçek zamanlı</td><td>Tüm görseller veya cinsiyete göre yapay zekâ</td></tr>
<tr><th scope="row">Arka plan müziği kaldırma</th><td>Evet</td><td>Belirtilmemiş</td><td>Belirtilmemiş</td></tr>
<tr><th scope="row">Ebeveyn PIN'i ve zaman sınırları</th><td>Family Premium</td><td>Belirtilmemiş</td><td>Kalkan kilidi</td></tr>
</tbody>
</table></div>
<p>&quot;Belirtilmemiş&quot;, tarayıcının kendi sayfalarında bulamadığımız anlamına gelir, var olmadığı değil. Daha uzun bir tablo için <a href="/tr/compare/kahf-browser/">AkhiBrowser ve Kahf Browser karşılaştırması</a> ile <a href="/tr/compare/browsers/">AkhiBrowser, Kahf, Brave, Firefox ve Chrome karşılaştırmasına</a> bak. Konuya yeni misin? <a href="/tr/blog/what-is-a-halal-browser/">Helal tarayıcı nedir</a> yazısıyla başla.</p>
<p>10 Kasım 2026'da her tarayıcının kendi sayfalarıyla kontrol edildi. Eskimiş bir şey mi gördün? Bize <a href="mailto:support@akhibrowser.com">support@akhibrowser.com</a> adresinden yaz.</p>""",
    },
}

_NS = "Belirtilmemiş"

COMPARE = {
    "seo_title": "AkhiBrowser ve Kahf Browser: özellikler, fiyat ve platformlar karşılaştırması",
    "title": "AkhiBrowser ve Kahf Browser karşılaştırması",
    "description": "AkhiBrowser ve Kahf Browser yan yana: fiyat, platformlar, filtreleme, görseller, müzik kaldırma, namaz vakitleri ve ebeveyn denetimleri, her tarayıcının kendi sayfalarından.",
    "lead": "İkisi de Müslümanlar için tarayıcılar. Bu tablo, her birinin kendi web sitesinde belirttiklerini listeler; Kahf Browser için 8 Kasım 2026, AkhiBrowser için 22 Kasım 2026 itibarıyla. Kahf Browser'ı kendimiz test etmedik. &quot;Belirtilmemiş&quot;, okuduğumuz sayfalarda bulamadığımız anlamına gelir, özelliğin olmadığı değil.",
    "head": ["", "AkhiBrowser", "Kahf Browser"],
    "rows": [
        ["Fiyat", "Korumalar ücretsiz. İsteğe bağlı Premium ayda 3,99 €, yılda 39 € veya bir kez 119 €; Family Premium yılda 59,99 €", "Tüm platformlarda ücretsiz, abonelik veya uygulama içi satın alma yok"],
        ["Platformlar", "Windows (Microsoft Store), Android (Google Play). iOS ve macOS: <a href=\"/tr/#roadmap\">yol haritasında</a>, henüz tarih yok", "Windows, macOS, Android, iOS. Linux: SSS'si listeler, indirme sayfası yakında der"],
        ["Yetişkin ve haram siteler", "Engellenir: yetişkin, alkol, uyuşturucu, elektronik sigara ve kumar", "Engellenir, yapay zekâ filtresi ve bir veritabanıyla"],
        ["Haram aramalar", "11 dilde engellenir; bunlar hakkındaki sorulara izin verilir", "Safe Search, arama önerileri dahil"],
        ["Görsellerde çıplaklık", "Cihazında kontrol edilene kadar bulanık: görseller, arka planlar, video ve tuvaller; videolarda gerçek zamanlı: her yeni sahne anında bulanıklaştırılıp kontrol edilir", "Gerçek zamanlı bulanıklaştırılır"],
        ["SafeSearch", "Google, Bing, DuckDuckGo ve Yahoo'da zorunlu, artı YouTube Kısıtlı Modu", "Büyük arama motorlarında zorunlu; Safe YouTube"],
        ["Ebeveyn PIN'i, site listeleri, zaman sınırları", "Family Premium: PIN, engellenen veya yalnızca onaylı siteler, yatma ve okul saatleri, günlük sınır", _NS],
        ["Ebeveyn raporu ve etkinlik özeti", "Family Premium: bir koruma veya PIN kapatıldığında e-posta, engellerin nedene göre haftalık özeti ve cihazda 7 günlük özet", _NS],
        ["İnterneti duraklatma", "Family Premium, PIN ile; ebeveyn denetimleri PIN ile kilitli bir dosyayla başka bir cihaza taşınabilir", _NS],
        ["Sosyal akışlar ve uygulamalar", "Family Premium: kısa video akışları gizli, sosyal sitelere günlük sınır, Android'de uygulamalar engelli", _NS],
        ["Videolardan arka plan müziğini kaldırma", "Ücretsiz, cihazında", _NS],
        ["Reklamlar ve izleyiciler", "Engellenir, uBlock Origin ve yerleşik bir engelleyiciyle", "Yerleşik engelleyici"],
        ["Kimlik avı ve dolandırıcılık siteleri", "Engellenir", "Engellenir"],
        ["Kimin bulanık olacağını seçme (kadınlar, erkekler)", "Premium", _NS],
        ["Başörtüsünü tanıma", "Premium", _NS],
        ["Sıkı mod", "Premium: her görsel ve video sen dokunana kadar bulanık kalır", _NS],
        ["YouTube", "Kısıtlı Mod, ücretsiz. Premium: öneri, Shorts veya otomatik oynatma yok. Family Premium: Deen Time, yalnızca seçtiğin kanallar", "Safe YouTube"],
        ["Namaz vakitleri", "Ücretsiz, seçtiğin bir şehir için, konumun olmadan; bilgisayarlarda hatırlatmalar", "Namaz vakitleri ve bildirimler"],
        ["Namaz molası", "Family Premium: sosyal, video ve oyun siteleri her namaz vaktinden sonra birkaç dakika duraklar", _NS],
        ["Helal kontrolü ve helal mekânlar", "Family Premium: domuz, alkol, jelatin veya şüpheli E-kodları içeren ürün sayfalarında uyarı; Google Haritalar ve yemek siparişi sitelerinde helal mekânlar", _NS],
        ["Faiz uyarısı, ganimet kutuları", "Family Premium: faizli kredi, kredi kartı ve \"şimdi al sonra öde\" sayfalarında uyarı; kasa açma ve skin kumarı siteleri engelli", _NS],
        ["Kur'an tilaveti, güvenilir kaynaklar", "Family Premium: YouTube'da bir tilaveti anlamıyla ayet ayet takip etme; İslam hakkında aramada önce âlimlerin kaynakları", _NS],
        ["Günün ayeti", "Ücretsiz", _NS],
        ["Kıble", "Evet, Android'de: namaz vakitlerinin altında bir pusula", "Evet"],
        ["Diller", "12, Arapça, Urduca, Farsça, Kürtçe ve Türkçe dahil", _NS],
        ["Renk körlüğü düzeltmesi", "Ücretsiz, cihazında", _NS],
        ["Hesap gerekli mi", "Hayır", "Hayır; oturum açmak mümkün"],
        ["Temeli", "Firefox", "Chromium; çoğu Chrome uzantısı çalışır"],
        ["Kaynak kodu", "Firefox değişiklikleri ve MPL dosyaları herkese açık; kendi uzantısı özel", "SSS'sine göre henüz herkese açık değil"],
    ],
    "after": """<h2>Hangisi sana uygun?</h2>
<p><strong>Kahf Browser</strong>, iPhone veya Mac kullanıyorsan ya da her şeyin ücretsiz olmasını istiyorsan uygundur.</p>
<p><strong>AkhiBrowser</strong>, arka plan müziğinin kaldırılmasını, kimin bulanıklaştırılacağını seçmeyi istiyorsan ya da Windows veya Android'de PIN, zaman sınırları ve e-postayla rapor gibi ebeveyn denetimlerine ihtiyacın varsa uygundur. Family Premium, Kahf'ın listelemediklerini ekler: alışveriş yaparken helal kontrolü, faiz uyarısı ve her namazdan sonra bir mola.</p>
<p>İkisi de denemek için ücretsiz, bu yüzden en iyi test kendi kullanımın. AkhiBrowser'ın Kahf ile bir bağı yoktur. Eskimiş bir şey mi gördün? Bize <a href="mailto:support@akhibrowser.com">support@akhibrowser.com</a> adresinden yaz, düzeltelim.</p>""",
    "sources_label": "Okuduğumuz Kahf Browser sayfaları:",
}

_CWS = "https://chromewebstore.google.com/detail/akhibrowser/ghkpflipnhahpjdnpoclaakbecnopamk"
_AMO = "https://addons.mozilla.org/en-US/firefox/addon/akhibrowser/"
_ALL5 = "Windows, macOS, Linux, Android, iOS"

COMPARE_BROWSERS = {
    "seo_title": "Helal tarayıcı karşılaştırması: AkhiBrowser, Kahf Browser, Brave, Firefox ve Chrome",
    "title": "AkhiBrowser, Kahf Browser, Brave, Firefox ve Chrome karşılaştırması",
    "description": "Hangi tarayıcı haram içeriği filtreler, görselleri bulanıklaştırır, arka plan müziğini kaldırır ve ebeveyn denetimine sahiptir? AkhiBrowser, Kahf Browser, Brave, Firefox ve Chrome yan yana.",
    "lead": "Her tarayıcının kutudan çıktığı gibi, ek uzantı olmadan yaptıkları, her birinin kendi sayfalarında anlattığı şekilde; 9 Kasım 2026 ve AkhiBrowser için 15 Kasım 2026 itibarıyla. Kahf Browser'ı kendimiz test etmedik; <a href=\"/tr/compare/kahf-browser/\">Kahf Browser ile ayrıntılı karşılaştırmaya</a> bak.",
    "head": ["", "AkhiBrowser", "Kahf Browser", "Brave", "Firefox", "Chrome"],
    "rows": [
        ["Fiyat", "Korumalar ücretsiz; isteğe bağlı Premium ve Family Premium", "Ücretsiz", "Ücretsiz", "Ücretsiz", "Ücretsiz"],
        ["Platformlar", f"Windows (Microsoft Store), Android (Google Play); <a href=\"{_CWS}\">Chrome</a> ve <a href=\"{_AMO}\">Firefox</a> için daha hafif ücretsiz uzantılar", "Windows, macOS, Android, iOS", _ALL5, _ALL5, _ALL5],
        ["Yetişkin ve haram siteler", "Engellenir, ilk sayfadan itibaren", "Engellenir", "Hayır", "Hayır", "Hayır"],
        ["Haram aramalar engellenir", "Evet, 11 dilde", "Safe Search, öneriler dahil", "Hayır", "Hayır", "Hayır"],
        ["Görsellerde çıplaklık", "Cihazında kontrol edilene kadar bulanık", "Bulanık", "Hayır", "Hayır", "Hayır"],
        ["SafeSearch ve YouTube Kısıtlı Modu zorunlu", "Evet", "Evet", "Hayır", "Hayır", "Family Link denetimiyle"],
        ["Ebeveyn denetimleri (PIN, site listeleri, zaman sınırları)", "Family Premium", _NS, "Hayır", "Hayır", "Google Family Link ile"],
        ["Ebeveynlere rapor", "Family Premium, e-postayla", _NS, "Hayır", "Hayır", "Google Family Link ile"],
        ["Korumalar bir çocuk tarafından kapatılabilir", "Ebeveyn PIN'i varken hayır", _NS, "Evet", "Evet", "Family Link'e bağlı"],
        ["Videolardan arka plan müziğini kaldırma", "Ücretsiz, cihazında", _NS, "Hayır", "Hayır", "Hayır"],
        ["Reklamlar ve izleyiciler", "Engellenir, uBlock Origin yerleşik", "Engellenir", "Engellenir (Shields)", "İzleyiciler engellenir; reklamlar için uzantı gerekir", "Engellenmez; reklam engelleyiciler sınırlı"],
        ["Kimin bulanık olacağını seçme, başörtüsünü tanıma", "Premium", _NS, "Hayır", "Hayır", "Hayır"],
        ["Daha sakin YouTube", "Premium: öneri, Shorts veya otomatik oynatma yok", "Safe YouTube", "Hayır", "Hayır", "Hayır"],
        ["Namaz vakitleri ve günün ayeti", "Ücretsiz", "Namaz vakitleri", "Hayır", "Hayır", "Hayır"],
        ["Helal kontrolü, faiz uyarısı, namaz molası", "Family Premium", _NS, "Hayır", "Hayır", "Hayır"],
        ["Temeli", "Firefox", "Chromium", "Chromium", "Firefox'un kendi motoru", "Chromium"],
    ],
    "after": """<h2>Kısacası</h2>
<p><strong>Brave, Firefox ve Chrome</strong> iyi genel tarayıcılardır, ama hiçbiri kendi başına haram içeriği filtrelemez veya görselleri bulanıklaştırmaz. Bir çocuğun kaldırabileceği uzantılara ihtiyacın olur.</p>
<p><strong>Kahf Browser ve AkhiBrowser</strong> Müslümanlar için yapılmıştır ve baştan filtreler. AkhiBrowser bunlara arka plan müziği kaldırmayı, kimin bulanıklaştırılacağını seçmeyi, PIN'li ve e-postayla raporlu ebeveyn denetimlerini, ayrıca helal kontrolü, faiz uyarısı ve namaz molasını ekler.</p>
<p>Eskimiş bir şey mi gördün? Bize <a href="mailto:support@akhibrowser.com">support@akhibrowser.com</a> adresinden yaz, düzeltelim. AkhiBrowser'ın bu tarayıcıların hiçbiriyle bağı yoktur.</p>""",
    "sources_label": "Okuduğumuz sayfalar:",
}
