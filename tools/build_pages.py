#!/usr/bin/env python3
"""Builds the blog and comparison pages, the sitemap and robots.txt from tools/content.py.

The menu, and the pages /affiliate/ and /money/, come from index.html: its menu (div.links), the sections in its
<template id="pages">, and its Dutch and Arabic texts (const NL and const AR). Change them there, then build.

To add an article: add an entry to ARTICLES in content.py with its English and Dutch text, and its Arabic
text to content_ar.py, then run

    python tools/build_pages.py

The pages it writes are its output: change their text here, in content.py, content_ar.py or index.html, not in
the pages themselves, or the next build undoes it. /faq/, /newsletter/ and /delete-account/ are written by hand.
"""
import html
import json
import re
from pathlib import Path

from content import ARTICLES, COMPARE, COMPARE_BROWSERS, LANGS, UI
from langs import EXTRA, FORMS, LABEL as LANG_LABEL, NAMES, direction, home_texts

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://akhibrowser.com"
GTM = """<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('consent', 'default', {analytics_storage: 'denied', ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied', wait_for_update: 500});
  try { if (localStorage.getItem('akhi-consent') === 'granted') gtag('consent', 'update', {analytics_storage: 'granted'}); } catch (e) {}
  dataLayer.push({'gtm.start': new Date().getTime(), event: 'gtm.js'});
</script>
<script src="/assets/analytics.js" defer></script>"""


# the languages these pages are built in: English, Dutch, Arabic and each language with a tools/content_<lang>.py
LANG_NAMES = {lang: NAMES[lang] for lang in LANGS}
YEAR = "2026"
# keeps the year current; a choice in the language menu opens that page and is remembered for the home page
SCRIPT = """<script>
document.querySelectorAll("[data-year]").forEach(n => n.textContent = new Date().getFullYear());
document.title = document.title.replace("%s", new Date().getFullYear());
const menu = document.getElementById("lang");
menu.addEventListener("change", () => {
  try { localStorage.setItem("lang", menu.selectedOptions[0].lang); } catch (err) {}
  location.href = menu.value;
});
// coming back with the Back button shows this page's language again
addEventListener("pageshow", () => { menu.value = menu.querySelector("[selected]").value; });
</script>""" % YEAR


MENU_SCRIPT = (Path(__file__).resolve().parent.parent / "index.html").read_text(encoding="utf-8")
MENU_SCRIPT = re.search(r"<script>\n(// the menu: .*?)</script>", MENU_SCRIPT, re.S).group(1)
TURNSTILE = """<script>
// Cloudflare Turnstile, the check against robots on the forms: loaded once someone starts filling one in
(function () {
  let loaded = false;
  function load() {
    if (!loaded) {
      loaded = true;
      const script = document.createElement("script");
      script.src = "https://challenges.cloudflare.com/turnstile/v0/api.js";
      script.async = true;
      document.head.append(script);
    }
  }
  for (const form of document.querySelectorAll("form.affiliate")) {
    form.addEventListener("focusin", load);
    form.addEventListener("pointerdown", load);
  }
})();
</script>"""
# the forms: plain-language feedback, for the pages that have forms
FORM_CHECKS = """<script>
// the forms: plain-language feedback in the page's language instead of the browser's own warnings, which are easy to miss
(function () {
  const lang = (document.documentElement.lang || "en").slice(0, 2);
  const words = {
    en: {
      name: "Please fill in your name.",
      email: "Please fill in a valid email address, like name@example.com.",
      site: "Please check your website address, like yourname.com, or leave it empty.",
      organisation: "Please fill in the name of your school, mosque, organisation or channel.",
      robot: "One moment: we're still checking that you're not a robot. Wait a few seconds and press the button again.",
      sending: "Sending…",
    },
    nl: {
      name: "Vul je naam in.",
      email: "Vul een geldig e-mailadres in, zoals naam@voorbeeld.nl.",
      site: "Controleer het adres van je website, zoals jouwnaam.nl, of laat het leeg.",
      organisation: "Vul de naam van je school, moskee, organisatie of kanaal in.",
      robot: "Even geduld: we controleren nog of je geen robot bent. Wacht een paar seconden en druk dan opnieuw op de knop.",
      sending: "Bezig met versturen…",
    },
    ar: {
      name: "يرجى كتابة اسمك.",
      email: "يرجى كتابة بريد إلكتروني صحيح، مثل name@example.com.",
      site: "يرجى التحقق من عنوان موقعك، مثل yourname.com، أو تركه فارغًا.",
      organisation: "يرجى كتابة اسم مدرستك أو مسجدك أو مؤسستك أو قناتك.",
      robot: "لحظة من فضلك: ما زلنا نتحقق من أنك لست روبوتًا. انتظر بضع ثوانٍ ثم اضغط الزر مرة أخرى.",
      sending: "جارٍ الإرسال…",
    },
    EXTRA_FORMS
  }[lang] ?? null;
  if (!words) {
    return;
  }
  // the same checks as the license server: a domain that ends in a top-level domain of letters
  const HOST = /^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\\.)+(?:[a-z]{2,63}|xn--[a-z0-9-]{2,59})$/;
  const isEmail = text => /^[^@\\s<>,;"]+@[^@\\s<>,;"]+$/.test(text) && HOST.test(text.slice(text.lastIndexOf("@") + 1).toLowerCase());
  const isSite = text => {
    try {
      const url = new URL(/^https?:\\/\\//i.test(text) ? text : `https://${text}`);
      return /^https?:$/.test(url.protocol) && !url.username && !url.password && HOST.test(url.hostname);
    } catch (e) {
      return false;
    }
  };
  for (const form of document.querySelectorAll("form.affiliate")) {
    form.noValidate = true;
    // the license server's page after sending, in this page's language
    if (!form.elements.namedItem("lang")) {
      const input = document.createElement("input");
      input.type = "hidden";
      input.name = "lang";
      input.value = lang;
      form.append(input);
    }
    const message = document.createElement("p");
    message.className = "form-error";
    message.setAttribute("role", "alert");
    message.hidden = true;
    form.querySelector('button[type="submit"]').before(message);
    form.addEventListener("input", () => {
      message.hidden = true;
    });
    form.addEventListener("submit", event => {
      const field = name => form.elements.namedItem(name);
      const problem =
        (!field("name").value.trim() && ["name", words.name]) ||
        (!isEmail(field("email").value.trim()) ? ["email", words.email] : null) ||
        (field("site")?.value.trim() && !isSite(field("site").value.trim()) ? ["site", words.site] : null) ||
        (field("organisation")?.required && !field("organisation").value.trim() && ["organisation", words.organisation]) ||
        (!form.querySelector('[name="cf-turnstile-response"]')?.value && [null, words.robot]) ||
        null;
      if (problem) {
        event.preventDefault();
        message.textContent = problem[1];
        message.hidden = false;
        if (problem[0]) {
          field(problem[0]).focus();
        }
        return;
      }
      const button = form.querySelector('button[type="submit"]');
      button.disabled = true;
      button.textContent = words.sending;
    });
  }
  // coming back with the Back button: the button works again
  addEventListener("pageshow", () => {
    for (const button of document.querySelectorAll('form.affiliate button[type="submit"]')) {
      button.disabled = false;
      button.textContent = button.dataset.label ?? button.textContent;
    }
  });
  for (const button of document.querySelectorAll('form.affiliate button[type="submit"]')) {
    button.dataset.label = button.textContent;
  }
})();
</script>""".replace("EXTRA_FORMS", "\n    ".join(f"{lang}: {json.dumps(FORMS[lang], ensure_ascii=False)}," for lang in EXTRA))


SPONSORS_SCRIPT = """<script>
// the approved sponsors and partners who agreed to be listed, from the license server; their kind as the form names it
(async function () {
  const box = document.getElementById("sponsors");
  if (!box) {
    return;
  }
  try {
    const response = await fetch("https://akhi-license.akhibrowser.workers.dev/sponsors");
    const { sponsors = [] } = response.ok ? await response.json() : {};
    const kinds = Object.fromEntries([...document.querySelectorAll('select[name="kind"] option')].map(o => [o.value, o.textContent.split(":")[0]]));
    for (const { name, kind, url } of sponsors) {
      const item = document.createElement("li");
      const label = url && /^https?:\\/\\//.test(url) ? Object.assign(document.createElement("a"), { href: url, rel: "noopener sponsored" }) : document.createElement("strong");
      label.textContent = name;
      item.append(label);
      if (kinds[kind]) {
        item.append(` · ${kinds[kind]}`);
      }
      box.querySelector("ul").append(item);
    }
    box.hidden = !sponsors.length;
  } catch (e) {}
})();
</script>
"""

KIT_SCRIPT = """<script src="https://cdnjs.cloudflare.com/ajax/libs/qrcode-generator/1.4.4/qrcode.min.js"></script>
<script>
// the kit for schools and mosques: the message and the poster are made here, the key isn't sent anywhere
(function () {
  const $ = id => document.getElementById(id);
  const download = "https://akhibrowser.com/#download";
  function update() {
    const key = $("kit-key").value.trim();
    const name = $("kit-name").value.trim() || $("kit-org").textContent;
    const text = $("kit-text").textContent.replace("{NAME}", name).replace("{KEY}", key || "AKHI-...");
    $("kit-msg").value = text;
    $("kit-wa").href = "https://wa.me/?text=" + encodeURIComponent(text);
    $("kit-title").textContent = $("kit-title").dataset.template.replace("{NAME}", name);
    $("kit-poster-key").textContent = key;
    $("kit-scan").hidden = Boolean(key);
  }
  $("kit-title").dataset.template = $("kit-title").textContent;
  if (window.qrcode) {
    const qr = qrcode(0, "M");
    qr.addData(download);
    qr.make();
    $("kit-qr").innerHTML = qr.createSvgTag({ cellSize: 6, margin: 2, scalable: true });
  }
  $("kit-key").addEventListener("input", update);
  $("kit-name").addEventListener("input", update);
  $("kit-copy").addEventListener("click", () => navigator.clipboard.writeText($("kit-msg").value));
  $("kit-print").addEventListener("click", () => print());
  update();
  // questions from schools and mosques: sent to the lead agent, which mails us; we answer by email
  const ask = $("kit-ask");
  if (ask) ask.addEventListener("submit", async e => {
    e.preventDefault();
    const d = Object.fromEntries(new FormData(ask));
    const ok = d.name && d.name.trim() && /^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(d.email || "");
    $("ka-err").hidden = Boolean(ok);
    if (!ok) return;
    d.page = location.pathname;
    d.message = d.message || "School / Mosque question";
    ask.querySelector("button").disabled = true;
    try { await fetch("https://akhi-leads.akhibrowser.workers.dev/lead", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(d) }); } catch (err) {}
    for (const el of ask.querySelectorAll("label, input, textarea, .kit-actions")) el.hidden = true;
    $("ka-ok").hidden = false;
  });
})();
</script>"""


def home():
    """The menu, the sections for their own pages, and the Dutch and Arabic texts, from index.html."""
    text = (ROOT / "index.html").read_text(encoding="utf-8")
    dicts = {"en": {}}
    for lang, name in (("nl", "NL"), ("ar", "AR")):
        block = re.search(r"const %s = \{\n(.*?)\n\};" % name, text, re.S).group(1)
        dicts[lang] = {k: json.loads(v) for k, v in re.findall(r'^"([\w-]+)": (".*"),?$', block, re.M)}
    for lang in EXTRA:
        dicts[lang] = home_texts(lang)
    menu = re.search(r'<div class="links" id="menu">.*?</div><!-- /links -->', text, re.S).group(0)
    template = re.search(r'<template id="pages">(.*?)</template>', text, re.S).group(1)
    sections = dict(re.findall(r'<section id="(\w+)">\s*<div class="wrap">(.*?)</div>\s*</section>', template, re.S))
    return dicts, menu, sections


HOME_TEXTS, HOME_MENU, HOME_SECTIONS = None, None, None


def translated(markup, lang):
    """The markup with each element's data-t text in this language, as index.html's script shows it."""
    words = HOME_TEXTS[lang]

    def swap(match):
        return match.group(1) + words[match.group(3)] + match.group(4) if match.group(3) in words else match.group(0)

    markup = re.sub(r'(<(\w+)\b[^>]*\bdata-t="([\w-]+)"[^>]*>).*?(</\2>)', swap, markup, flags=re.S)

    def attribute(match):
        # data-a="name:key": the attribute in this language; the page is built per language, so data-a itself goes
        tag, name, key = match.group(0), match.group(1), match.group(2)
        tag = tag.replace(f' data-a="{name}:{key}"', "")
        if key in words:
            tag = re.sub(r'\b%s="[^"]*"' % re.escape(name), lambda m: f'{name}="{html.escape(words[key])}"', tag, count=1)
        return tag

    return re.sub(r'<[^>]*\bdata-a="([\w-]+):([\w-]+)"[^>]*>', attribute, markup)


def menu_of(lang):
    markup = translated(HOME_MENU, lang)
    # the home page's sections, on the home page in this language
    markup = re.sub(r'href="#', 'href="%s#' % url_of(lang, ""), markup)
    markup = re.sub(r'href="/((?:blog|compare|affiliate|money|privacy|setup|kit|faq|newsletter|delete-account)/[^"]*)"', lambda m: f'href="{url_of(lang, m.group(1))}"', markup)
    return markup


def url_of(lang, path):
    return f"/{path}" if lang == "en" else f"/{lang}/{path}"


def live(text):
    """Text shown on the page, with the year kept current by the script."""
    return text.replace("{YEAR}", f"<span data-year>{YEAR}</span>")


def plain(text):
    """Text for the title, meta tags and structured data."""
    return text.replace("{YEAR}", YEAR)


def lang_menu(lang, path):
    options = "".join(
        f'<option value="{url_of(code, path)}" lang="{code}"{" selected" if code == lang else ""}>{name}</option>'
        for code, name in LANG_NAMES.items()
    )
    return f'<select class="lang" id="lang" aria-label="{LANG_LABEL[lang]}">{options}</select>'


def page(lang, path, title, description, body, json_ld=None, scripts="", early_scripts=""):
    ui = UI[lang]
    title, description = plain(title), plain(description)
    canonical = SITE + url_of(lang, path)
    ld = f'<script type="application/ld+json">{json.dumps(json_ld, ensure_ascii=False)}</script>\n' if json_ld else ""
    alternates = "\n".join(f'<link rel="alternate" hreflang="{code}" href="{SITE + url_of(code, path)}">' for code in LANGS)
    return f"""<!doctype html>
<html lang="{lang}"{direction(lang)}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<link rel="canonical" href="{canonical}">
{alternates}
<link rel="alternate" hreflang="x-default" href="{SITE + url_of('en', path)}">
<meta name="theme-color" content="#03282e">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:image" content="{SITE}/assets/og.png">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="article">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/akhi.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/pages.css">
{ld}{GTM}
</head>
<body>
<header>
  <nav class="wrap" aria-label="{ui['nav_label']}">
    <a class="brand" href="{url_of(lang, '')}"><img src="/assets/akhi.svg" alt="" width="32" height="32"><span><b>Akhi</b>Browser</span></a>
    <div class="nav-end"><button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu">{HOME_TEXTS[lang].get('nv0', 'Menu')}</button>
      {menu_of(lang)}
      {lang_menu(lang, path)}
    </div>
  </nav>
</header>
<main class="wrap">
{body}
</main>
<footer class="wrap">
  <p>{ui['footer']}</p>
  <p>&copy; <span data-year>{YEAR}</span> AkhiBrowser</p>
</footer>
{early_scripts}{SCRIPT}
<script>
{MENU_SCRIPT}</script>
{scripts}
</body>
</html>
"""


def cta(lang):
    ui = UI[lang]
    return f"""<aside class="cta"><h2>{ui['cta_title']}</h2><p>{ui['cta_text']}</p><a class="btn" href="{url_of(lang, '')}#download">{ui['download']}</a></aside>"""


def article_page(lang, article):
    text = article[lang]
    path = f"blog/{article['slug']}/"
    ld = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": plain(text["title"]),
        "description": plain(text["description"]),
        "datePublished": article["date"],
        "dateModified": article.get("modified", article["date"]),
        "inLanguage": lang,
        "image": f"{SITE}/assets/og.png",
        "author": {"@type": "Organization", "name": "AkhiBrowser", "url": SITE},
        "publisher": {"@type": "Organization", "name": "AkhiBrowser", "url": SITE},
        "mainEntityOfPage": SITE + url_of(lang, path),
    }
    body = f"""<article>
<p class="crumb"><a href="{url_of(lang, 'blog/')}">{UI[lang]['blog']}</a></p>
<h1>{live(text['title'])}</h1>
<p class="date"><time datetime="{article['date']}">{article['date']}</time></p>
{live(text['body'])}
</article>
{cta(lang)}"""
    return path, page(lang, path, f"{text['title']} | AkhiBrowser", text["description"], body, ld)


def index_page(lang):
    ui = UI[lang]
    items = "\n".join(
        f"""<li><a href="{url_of(lang, 'blog/' + a['slug'] + '/')}"><h2>{live(a[lang]['title'])}</h2></a><p>{live(a[lang]['description'])}</p></li>"""
        for a in sorted(ARTICLES, key=lambda a: a["date"], reverse=True)
    )
    for data, path in ((COMPARE_BROWSERS, "compare/browsers/"), (COMPARE, "compare/kahf-browser/")):
        items += f"""\n<li><a href="{url_of(lang, path)}"><h2>{data[lang]['title']}</h2></a><p>{data[lang]['description']}</p></li>"""
    body = f"""<h1>{ui['blog_title']}</h1>\n<p class="lead">{ui['blog_lead']}</p>\n<ul class="posts">\n{items}\n</ul>"""
    return "blog/", page(lang, "blog/", f"{ui['blog_title']} | AkhiBrowser", ui["blog_lead"], body)


def compare_page(lang, data, path):
    text = data[lang]
    rows = "\n".join(
        f"<tr><th scope=\"row\">{row[0]}</th>" + "".join(f"<td>{cell}</td>" for cell in row[1:]) + "</tr>"
        for row in text["rows"]
    )
    head = "".join(f'<th scope="col">{name}</th>' for name in text["head"])
    sources = " ".join(f'<a href="{url}">{name}</a>' for name, url in data["sources"])
    body = f"""<article>
<h1>{text['title']}</h1>
<p class="lead">{text['lead']}</p>
<div class="table"><table>
<thead><tr>{head}</tr></thead>
<tbody>
{rows}
</tbody>
</table></div>
{text['after']}
<p class="note">{text['sources_label']} {sources}</p>
</article>
{cta(lang)}"""
    return path, page(lang, path, text["seo_title"], text["description"], body)


def home_page(lang, section, path, extra="", scripts=TURNSTILE + "\n" + FORM_CHECKS, early_scripts=""):
    """A section of index.html as its own page: its h2 is the page's title."""
    words = HOME_TEXTS[lang]
    markup = translated(HOME_SECTIONS[section], lang).replace("<h2", "<h1", 1).replace("</h2>", "</h1>", 1)
    title = html.unescape(re.sub(r"<[^>]+>", "", re.search(r"<h1[^>]*>(.*?)</h1>", markup, re.S).group(1)))
    intro = html.unescape(re.sub(r"<[^>]+>", "", re.search(r'<p class="intro"[^>]*>(.*?)</p>', markup, re.S).group(1)))
    if lang != "en":
        # the license server answers in the page's language, also without the forms' script
        markup = re.sub(r'(<form class="affiliate"[^>]*>)', r'\1\n        <input type="hidden" name="lang" value="%s">' % lang, markup)
    body = f'<div class="home">\n{markup}\n{extra}</div>\n{cta(lang)}'
    return path, page(lang, path, f"{title} | AkhiBrowser", intro, body, scripts=scripts, early_scripts=early_scripts)


def write(lang, path, content):
    target = ROOT / url_of(lang, path).lstrip("/") / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8", newline="\n")


def main():
    global HOME_TEXTS, HOME_MENU, HOME_SECTIONS
    HOME_TEXTS, HOME_MENU, HOME_SECTIONS = home()
    paths = []
    for lang in LANGS:
        builders = [
            index_page(lang),
            home_page(lang, "affiliate", "affiliate/"),
            home_page(lang, "money", "money/", early_scripts=SPONSORS_SCRIPT),
            home_page(lang, "privacy", "privacy/", scripts=TURNSTILE),
            home_page(lang, "setup", "setup/", scripts=TURNSTILE),
            home_page(lang, "kit", "kit/", scripts=KIT_SCRIPT),
            compare_page(lang, COMPARE_BROWSERS, "compare/browsers/"),
            compare_page(lang, COMPARE, "compare/kahf-browser/"),
        ] + [article_page(lang, a) for a in ARTICLES]
        for path, content in builders:
            write(lang, path, content)
            paths.append(url_of(lang, path))
    # a link to a page that doesn't exist in that language yet (say, its FAQ) goes to the English page
    for url in paths:
        target = ROOT / url.lstrip("/") / "index.html"
        lang = url.split("/")[1] if url.split("/")[1] in LANGS else "en"
        if lang == "en":
            continue

        def local(m, lang=lang):
            rest = m.group(1)
            page = rest.split("#")[0].split("?")[0]
            return m.group(0) if not page or (ROOT / lang / page / "index.html").exists() else f'href="/{rest}"'

        text = target.read_text(encoding="utf-8")
        fixed = re.sub(r'href="/%s/([^"]*)"' % lang, local, text)
        if fixed != text:
            target.write_text(fixed, encoding="utf-8", newline="\n")
    # the home pages: tools/build_home.py, run after this, which links to these pages; the account deletion, newsletter and FAQ pages are written by hand
    by_hand = [
        url_of(lang, path)
        for path in ("delete-account/", "newsletter/", "faq/")
        for lang in LANGS
        if (ROOT / url_of(lang, path).lstrip("/") / "index.html").exists()
    ]
    homes = ["/"] + [f"/{lang}/" for lang in NAMES if lang != "en" and (ROOT / lang / "index.html").exists()]
    urls = homes + paths + by_hand
    sitemap = "\n".join(f"  <url><loc>{SITE}{u}</loc></url>" for u in urls)
    (ROOT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{sitemap}\n</urlset>\n',
        encoding="utf-8", newline="\n",
    )
    (ROOT / "robots.txt").write_text(
        f"User-agent: *\nDisallow: /tools/\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8", newline="\n"
    )
    print(f"{len(paths)} pages, sitemap with {len(urls)} addresses")


if __name__ == "__main__":
    main()
