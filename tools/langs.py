"""The website's languages, in one place for tools/build_home.py and tools/build_pages.py.

English is index.html itself; Dutch and Arabic are its const NL and const AR. The other languages' home page texts are
in tools/i18n/home/<lang>.txt: one line per text, its key, a tab, and the text (HTML as in index.html, with {NAME} and
{KEY} kept). A key that's missing shows the English text. Their blog and comparison pages are in tools/content_<lang>.py,
and /faq/, /newsletter/ and /delete-account/ are written by hand in each language's folder.

The release line under the features (data-t="f9") is made here for those languages, from the English line that
tools/update_release.py keeps current.
"""
import re
from pathlib import Path

TOOLS = Path(__file__).resolve().parent

# in the order of the language menu
LANGS = ("en", "nl", "ar", "de", "fr", "es", "tr", "id", "ms", "ur", "fa", "ckb")
# the languages whose home page texts are in tools/i18n/home/
EXTRA = tuple(lang for lang in LANGS if lang not in ("en", "nl", "ar"))
RTL = {"ar", "ur", "fa", "ckb"}
NAMES = {
    "en": "English",
    "nl": "Nederlands",
    "ar": "العربية",
    "de": "Deutsch",
    "fr": "Français",
    "es": "Español",
    "tr": "Türkçe",
    "id": "Bahasa Indonesia",
    "ms": "Bahasa Melayu",
    "ur": "اردو",
    "fa": "فارسی",
    "ckb": "کوردی",
}
LABEL = {
    "en": "Language",
    "nl": "Taal",
    "ar": "اللغة",
    "de": "Sprache",
    "fr": "Langue",
    "es": "Idioma",
    "tr": "Dil",
    "id": "Bahasa",
    "ms": "Bahasa",
    "ur": "زبان",
    "fa": "زبان",
    "ckb": "زمان",
}


def direction(lang):
    return ' dir="rtl"' if lang in RTL else ""


def home_texts(lang):
    """The home page texts of a language in tools/i18n/home/."""
    words = {}
    for line in (TOOLS / "i18n" / "home" / f"{lang}.txt").read_text(encoding="utf-8").splitlines():
        if line.strip():
            key, _, text = line.partition("\t")
            words[key] = text
    return words


MONTHS = {
    "en": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
           "November", "December"],
    "de": ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November",
           "Dezember"],
    "fr": ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre",
           "décembre"],
    "es": ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre",
           "noviembre", "diciembre"],
    "tr": ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım",
           "Aralık"],
    "id": ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober",
           "November", "Desember"],
    "ms": ["Januari", "Februari", "Mac", "April", "Mei", "Jun", "Julai", "Ogos", "September", "Oktober", "November",
           "Disember"],
    "ur": ["جنوری", "فروری", "مارچ", "اپریل", "مئی", "جون", "جولائی", "اگست", "ستمبر", "اکتوبر", "نومبر", "دسمبر"],
    "fa": ["ژانویه", "فوریه", "مارس", "آوریل", "مه", "ژوئن", "ژوئیه", "اوت", "سپتامبر", "اکتبر", "نوامبر", "دسامبر"],
    "ckb": ["کانوونی دووەم", "شوبات", "ئازار", "نیسان", "ئایار", "حوزەیران", "تەمووز", "ئاب", "ئەیلوول",
            "تشرینی یەکەم", "تشرینی دووەم", "کانوونی یەکەم"],
}
RELEASE = {
    "de": 'Neueste Version: <a href="{url}">AkhiBrowser {version}</a>, {date}. <a href="{url}">Was ist neu</a>.',
    "fr": 'Dernière version : <a href="{url}">AkhiBrowser {version}</a>, {date}. <a href="{url}">Nouveautés</a>.',
    "es": 'Última versión: <a href="{url}">AkhiBrowser {version}</a>, {date}. <a href="{url}">Novedades</a>.',
    "tr": 'Son sürüm: <a href="{url}">AkhiBrowser {version}</a>, {date}. <a href="{url}">Yenilikler</a>.',
    "id": 'Versi terbaru: <a href="{url}">AkhiBrowser {version}</a>, {date}. <a href="{url}">Yang baru</a>.',
    "ms": 'Versi terkini: <a href="{url}">AkhiBrowser {version}</a>, {date}. <a href="{url}">Apa yang baharu</a>.',
    "ur": 'تازہ ترین ورژن: <a href="{url}">AkhiBrowser {version}</a>، {date}۔ <a href="{url}">نیا کیا ہے</a>۔',
    "fa": 'آخرین نسخه: <a href="{url}">AkhiBrowser {version}</a>، {date}. <a href="{url}">تازه‌ها</a>.',
    "ckb": 'نوێترین وەشان: <a href="{url}">AkhiBrowser {version}</a>، {date}. <a href="{url}">چی نوێیە</a>.',
}


def release_line(english, lang):
    """The release line in another language, from the English one, or None if it doesn't look as expected."""
    match = re.search(
        r'<a href="([^"]+)">AkhiBrowser ([\d.]+)</a>, (\d{1,2}) (\w+) (\d{4})', english or ""
    )
    if not match or match.group(4) not in MONTHS["en"]:
        return None
    url, version, day, month, year = match.groups()
    when = f"{day} {MONTHS[lang][MONTHS['en'].index(month)]} {year}"
    return RELEASE[lang].format(url=url, version=version, date=when)


# the forms' messages (tools/build_pages.py FORM_CHECKS)
FORMS = {
    "de": {
        "name": "Bitte gib deinen Namen ein.",
        "email": "Bitte gib eine gültige E-Mail-Adresse ein, etwa name@beispiel.de.",
        "site": "Bitte prüfe die Adresse deiner Website, etwa deinname.de, oder lass das Feld leer.",
        "organisation": "Bitte gib den Namen deiner Schule, Moschee, Organisation oder deines Kanals ein.",
        "robot": "Einen Moment: Wir prüfen noch, dass du kein Roboter bist. Warte ein paar Sekunden und drück die Schaltfläche erneut.",
        "sending": "Wird gesendet…",
    },
    "fr": {
        "name": "Merci d'indiquer ton nom.",
        "email": "Merci d'indiquer une adresse e-mail valide, comme nom@exemple.fr.",
        "site": "Vérifie l'adresse de ton site, comme tonnom.fr, ou laisse le champ vide.",
        "organisation": "Merci d'indiquer le nom de ton école, ta mosquée, ton organisation ou ta chaîne.",
        "robot": "Un instant : nous vérifions encore que tu n'es pas un robot. Attends quelques secondes et appuie de nouveau sur le bouton.",
        "sending": "Envoi…",
    },
    "es": {
        "name": "Escribe tu nombre.",
        "email": "Escribe un correo electrónico válido, como nombre@ejemplo.com.",
        "site": "Revisa la dirección de tu web, como tunombre.com, o déjala vacía.",
        "organisation": "Escribe el nombre de tu escuela, mezquita, organización o canal.",
        "robot": "Un momento: aún estamos comprobando que no eres un robot. Espera unos segundos y vuelve a pulsar el botón.",
        "sending": "Enviando…",
    },
    "tr": {
        "name": "Lütfen adını yaz.",
        "email": "Lütfen geçerli bir e-posta adresi yaz, örneğin ad@ornek.com.",
        "site": "Lütfen web sitenin adresini kontrol et, örneğin adin.com, ya da boş bırak.",
        "organisation": "Lütfen okulunun, caminin, kuruluşunun veya kanalının adını yaz.",
        "robot": "Bir saniye: robot olmadığını hâlâ kontrol ediyoruz. Birkaç saniye bekle ve düğmeye tekrar bas.",
        "sending": "Gönderiliyor…",
    },
    "id": {
        "name": "Silakan isi namamu.",
        "email": "Silakan isi alamat email yang valid, seperti nama@contoh.com.",
        "site": "Silakan periksa alamat situs webmu, seperti namamu.com, atau biarkan kosong.",
        "organisation": "Silakan isi nama sekolah, masjid, organisasi, atau saluranmu.",
        "robot": "Sebentar: kami masih memeriksa bahwa kamu bukan robot. Tunggu beberapa detik lalu tekan tombolnya lagi.",
        "sending": "Mengirim…",
    },
    "ms": {
        "name": "Sila isi nama anda.",
        "email": "Sila isi alamat e-mel yang sah, seperti nama@contoh.com.",
        "site": "Sila semak alamat laman web anda, seperti namaanda.com, atau biarkan kosong.",
        "organisation": "Sila isi nama sekolah, masjid, organisasi atau saluran anda.",
        "robot": "Sebentar: kami masih menyemak bahawa anda bukan robot. Tunggu beberapa saat dan tekan butang sekali lagi.",
        "sending": "Menghantar…",
    },
    "ur": {
        "name": "براہ کرم اپنا نام لکھیں۔",
        "email": "براہ کرم درست ای میل پتہ لکھیں، جیسے name@example.com۔",
        "site": "براہ کرم اپنی ویب سائٹ کا پتہ جانچیں، جیسے yourname.com، یا اسے خالی چھوڑ دیں۔",
        "organisation": "براہ کرم اپنے اسکول، مسجد، ادارے یا چینل کا نام لکھیں۔",
        "robot": "ایک لمحہ: ہم ابھی جانچ رہے ہیں کہ آپ روبوٹ نہیں ہیں۔ چند سیکنڈ انتظار کریں اور بٹن دوبارہ دبائیں۔",
        "sending": "بھیجا جا رہا ہے…",
    },
    "fa": {
        "name": "لطفاً نامت را بنویس.",
        "email": "لطفاً یک نشانی ایمیل درست بنویس، مثل name@example.com.",
        "site": "لطفاً نشانی وب‌سایتت را بررسی کن، مثل yourname.com، یا خالی بگذار.",
        "organisation": "لطفاً نام مدرسه، مسجد، سازمان یا کانالت را بنویس.",
        "robot": "یک لحظه: هنوز داریم بررسی می‌کنیم که ربات نیستی. چند ثانیه صبر کن و دوباره دکمه را بزن.",
        "sending": "در حال ارسال…",
    },
    "ckb": {
        "name": "تکایە ناوت بنووسە.",
        "email": "تکایە ناونیشانێکی ئیمەیڵی دروست بنووسە، وەک name@example.com.",
        "site": "تکایە ناونیشانی ماڵپەڕەکەت بپشکنە، وەک yourname.com، یان بە بەتاڵی بیهێڵەرەوە.",
        "organisation": "تکایە ناوی قوتابخانە، مزگەوت، ڕێکخراو یان کەناڵەکەت بنووسە.",
        "robot": "ساتێک: هێشتا دەپشکنین کە ڕۆبۆت نیت. چەند چرکەیەک چاوەڕێ بکە و دووبارە دوگمەکە دابگرە.",
        "sending": "دەنێردرێت…",
    },
}

# the home page's title and description in each of the EXTRA languages
META = {
    "de": {
        "title": "AkhiBrowser: Halal-Browser für Muslime, blockiert Haram",
        "description": "AkhiBrowser ist ein kostenloser Halal-Browser für Muslime auf Basis von Firefox, der Werbung, 18+- und haram Seiten blockiert, Bilder unscharf hält, bis sie geprüft sind, und die Musik aus Videos entfernt. Alles passiert auf deinem eigenen Gerät.",
    },
    "fr": {
        "title": "AkhiBrowser : navigateur halal pour musulmans, bloque le haram",
        "description": "AkhiBrowser est un navigateur halal gratuit pour les musulmans, basé sur Firefox, qui bloque les publicités, les sites 18+ et haram, floute les images jusqu'à leur vérification et retire la musique des vidéos. Tout se passe sur ton propre appareil.",
    },
    "es": {
        "title": "AkhiBrowser: navegador halal para musulmanes, bloquea lo haram",
        "description": "AkhiBrowser es un navegador halal gratuito para musulmanes, basado en Firefox, que bloquea anuncios, sitios +18 y haram, difumina las imágenes hasta comprobarlas y quita la música de los vídeos. Todo ocurre en tu propio dispositivo.",
    },
    "tr": {
        "title": "AkhiBrowser: Müslümanlar için helal tarayıcı, haramı engeller",
        "description": "AkhiBrowser, Müslümanlar için Firefox tabanlı ücretsiz bir helal tarayıcıdır: reklamları, +18 ve haram siteleri engeller, görselleri kontrol edilene kadar bulanık tutar ve videolardaki müziği kaldırır. Her şey kendi cihazında olur.",
    },
    "id": {
        "title": "AkhiBrowser: browser halal untuk Muslim, memblokir yang haram",
        "description": "AkhiBrowser adalah browser halal gratis untuk Muslim, berbasis Firefox, yang memblokir iklan, situs 18+ dan haram, memburamkan gambar sampai diperiksa, dan menghapus musik dari video. Semuanya terjadi di perangkatmu sendiri.",
    },
    "ms": {
        "title": "AkhiBrowser: pelayar halal untuk umat Islam, menyekat yang haram",
        "description": "AkhiBrowser ialah pelayar halal percuma untuk umat Islam, berasaskan Firefox, yang menyekat iklan, laman 18+ dan haram, mengaburkan gambar sehingga diperiksa dan membuang muzik daripada video. Semuanya berlaku pada peranti anda sendiri.",
    },
    "ur": {
        "title": "AkhiBrowser: مسلمانوں کے لیے حلال براؤزر، حرام کو روکتا ہے",
        "description": "AkhiBrowser مسلمانوں کے لیے Firefox پر مبنی ایک مفت حلال براؤزر ہے، جو اشتہارات، 18+ اور حرام سائٹس روکتا ہے، تصاویر کو جانچ ہونے تک دھندلا رکھتا ہے اور ویڈیوز سے موسیقی نکالتا ہے۔ سب کچھ آپ کے اپنے آلے پر ہوتا ہے۔",
    },
    "fa": {
        "title": "AkhiBrowser: مرورگر حلال برای مسلمانان، حرام را مسدود می‌کند",
        "description": "AkhiBrowser مرورگری حلال و رایگان برای مسلمانان بر پایهٔ Firefox است که تبلیغات و سایت‌های +۱۸ و حرام را مسدود می‌کند، تصاویر را تا بررسی‌شدن تار نگه می‌دارد و موسیقی را از ویدیوها حذف می‌کند. همه‌چیز روی دستگاه خودت انجام می‌شود.",
    },
    "ckb": {
        "title": "AkhiBrowser: وێبگەڕی حەڵاڵ بۆ موسڵمانان، حەرام ڕادەگرێت",
        "description": "AkhiBrowser وێبگەڕێکی حەڵاڵی بەخۆڕاییە بۆ موسڵمانان، لەسەر بنەمای Firefox، کە ڕیکلام و ماڵپەڕی +18 و حەرام ڕادەگرێت، وێنەکان تا پشکنین لێڵ دەهێڵێتەوە و مۆسیقا لە ڤیدیۆکان لادەبات. هەموو شتێک لەسەر ئامێرەکەی خۆت ڕوودەدات.",
    },
}
