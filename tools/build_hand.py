#!/usr/bin/env python3
"""Builds /faq/, /newsletter/ and /delete-account/ in the languages of tools/langs.py EXTRA, from their texts in
tools/i18n/pages/<lang>.py, with the same header, menu and footer as tools/build_pages.py. The English, Dutch and
Arabic pages stay written by hand; this only keeps their language menu and hreflang links up to date, and their FAQ
structured data in step with their questions.

Run it after changing those texts, then tools/build_pages.py (sitemap) and tools/build_home.py (home page links):

    python tools/build_hand.py && python tools/build_pages.py && python tools/build_home.py

In the texts, link to pages by their English address (/privacy/, /affiliate/#vip); a page that exists in the
language gets its address there.
"""
import html
import importlib.util
import json
import re
from pathlib import Path

import build_pages as bp
from langs import EXTRA, NAMES

ROOT = Path(__file__).resolve().parent.parent
TOOLS = Path(__file__).resolve().parent
SITE = "https://akhibrowser.com"
PATHS = ("faq/", "newsletter/", "delete-account/")
LOCAL = r"(?:blog|compare|affiliate|money|privacy|setup|kit|faq|newsletter|delete-account)/"


def scripts_of(path):
    """The page's own scripts after the footer in the English page (not the year and menu scripts every page has)."""
    text = (ROOT / path / "index.html").read_text(encoding="utf-8")
    after = text[text.index("</footer>"):]
    found = re.findall(r"<script[^>]*>.*?</script>", after, re.S)
    return [s for s in found if "data-year" not in s and "// the menu:" not in s]


def localize(markup, lang):
    """Links to the site's pages go to the page in this language when it exists; the home page's sections too."""
    def page(m):
        target = m.group(1).split("#")[0].split("?")[0]
        exists = (ROOT / lang / target / "index.html").exists() or target in PATHS
        return f'href="/{lang}/{m.group(1)}"' if exists else m.group(0)

    markup = re.sub(r'href="/(%s[^"]*)"' % LOCAL, page, markup)
    return markup.replace('href="/#', f'href="/{lang}/#')


def faq_ld(items):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": html.unescape(re.sub(r"<[^>]+>", "", q)).strip(),
                "acceptedAnswer": {"@type": "Answer", "text": html.unescape(re.sub(r"<[^>]+>", "", a)).strip()},
            }
            for q, a in items
        ],
    }


def faq_items(markup):
    return re.findall(r"<summary>(.*?)</summary>\s*<div>(.*?)</div>", markup, re.S)


def faq_page(lang, t):
    items = "\n".join(
        f"""      <details{" open" if i == 0 else ""}>
        <summary>{html.escape(q, quote=False)}</summary>
        <div><p>{a}</p></div>
      </details>"""
        for i, (q, a) in enumerate(t["items"])
    )
    body = f"""<article class="prose">
    <h1>{t["h1"]}</h1>
    <div class="faq-search" role="search"><label for="faq-q">{t["search_label"]}</label><input id="faq-q" type="search" placeholder="{html.escape(t["search_placeholder"])}" autocomplete="off"></div>
    <p class="faq-none" id="faq-none" role="status" hidden>{t["none"]}</p>
    <div class="faq">
{items}
    </div>
  </article>"""
    body = localize(body, lang)
    return bp.page(lang, "faq/", f'{t["h1"]} | AkhiBrowser', t["description"], body, faq_ld(t["items"]),
                   scripts=bp.TURNSTILE + "\n" + bp.FORM_CHECKS + "\n" + faq_search())


def faq_search():
    return next(s for s in scripts_of("faq/") if "the FAQ search" in s)


def newsletter_page(lang, t):
    body = f"""<article class="prose">
    <h1>{t["h1"]}</h1>
    <p class="lead">{t["lead"]}</p>
    <form class="affiliate" action="https://akhi-license.akhibrowser.workers.dev/newsletter" method="post">
      <input type="hidden" name="lang" value="{lang}">
      <label><span>{t["email"]}</span><input name="email" type="email" required maxlength="200" autocomplete="email"></label>
      <label class="check"><input type="checkbox" name="consent" value="yes" required> <span>{t["consent"]}</span></label>
      <label class="trap" aria-hidden="true">Website<input name="website" tabindex="-1" autocomplete="off"></label>
      <div class="cf-turnstile" data-sitekey="0x4AAAAAAF9TRz9CNNAJX1Cg" data-action="newsletter" data-theme="dark" data-language="auto"></div>
      <button class="btn" type="submit">{t["button"]}</button>
      <p class="note">{t["note"]}</p>
    </form>
  </article>"""
    confirmed = f"""<script>
// back from the confirm link in the mail (?confirmed=): the address is confirmed, so the page says so instead of the form
(function () {{
  if (new URLSearchParams(location.search).has("confirmed")) {{
    const article = document.querySelector("main article");
    article.querySelector("h1").textContent = {json.dumps(t["confirmed_h1"], ensure_ascii=False)};
    article.querySelector(".lead").textContent = {json.dumps(t["confirmed_lead"], ensure_ascii=False)};
    article.querySelector("form").remove();
  }}
}})();
</script>"""
    return bp.page(lang, "newsletter/", t["title"], t["description"], localize(body, lang),
                   scripts=confirmed + "\n" + bp.TURNSTILE + "\n" + bp.FORM_CHECKS)


def delete_page(lang, t):
    body = f'<div class="home">\n{t["main"]}\n</div>\n{bp.cta(lang)}'
    return bp.page(lang, "delete-account/", t["title"], t["description"], localize(body, lang))


def update_by_hand(lang, path, langs):
    """The language menu and hreflang links of a page written by hand, for every language it exists in; its FAQ
    structured data from its own questions."""
    target = ROOT / bp.url_of(lang, path).lstrip("/") / "index.html"
    text = target.read_text(encoding="utf-8")
    text = re.sub(r'<select class="lang" id="lang"[^>]*>.*?</select>', lambda _: bp.lang_menu(lang, path), text, count=1, flags=re.S)
    alternates = "\n".join(f'<link rel="alternate" hreflang="{code}" href="{SITE + bp.url_of(code, path)}">' for code in langs)
    text = re.sub(r'(<link rel="alternate" hreflang="[^"]+" href="[^"]*">\n)+(?=<link rel="alternate" hreflang="x-default")',
                  lambda _: alternates + "\n", text, count=1)
    if path == "faq/":
        main = re.search(r'<div class="faq">(.*?)</div>\s*</article>', text, re.S).group(1)
        ld = json.dumps(faq_ld(faq_items(main)), ensure_ascii=False)
        text = re.sub(r'<script type="application/ld\+json">.*?</script>',
                      lambda _: f'<script type="application/ld+json">{ld}</script>', text, count=1, flags=re.S)
    target.write_text(text, encoding="utf-8", newline="\n")


def main():
    bp.HOME_TEXTS, bp.HOME_MENU, bp.HOME_SECTIONS = bp.home()
    done = []
    for lang in EXTRA:
        if lang not in bp.LANGS or not (TOOLS / "i18n" / "pages" / f"{lang}.py").exists():
            continue
        spec = importlib.util.spec_from_file_location(f"pages_{lang}", TOOLS / "i18n" / "pages" / f"{lang}.py")
        texts = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(texts)
        for path, content in (
            ("faq/", faq_page(lang, texts.FAQ)),
            ("newsletter/", newsletter_page(lang, texts.NEWSLETTER)),
            ("delete-account/", delete_page(lang, texts.DELETE)),
        ):
            bp.write(lang, path, content)
        done.append(lang)
    # the language menus: only the languages a page exists in
    for path in PATHS:
        langs = [code for code in NAMES if (ROOT / bp.url_of(code, path).lstrip("/") / "index.html").exists()]
        saved = dict(bp.LANG_NAMES)
        bp.LANG_NAMES.clear()
        bp.LANG_NAMES.update({code: NAMES[code] for code in langs})
        for lang in ("en", "nl", "ar"):
            update_by_hand(lang, path, langs)
        for lang in done:
            bp.write(lang, path, re.sub(r'<select class="lang" id="lang"[^>]*>.*?</select>', lambda _: bp.lang_menu(lang, path),
                                        (ROOT / lang / path / "index.html").read_text(encoding="utf-8"), count=1, flags=re.S))
        bp.LANG_NAMES.clear()
        bp.LANG_NAMES.update(saved)
    print("built the FAQ, newsletter and account pages in: " + (", ".join(done) or "no other language"))


if __name__ == "__main__":
    main()
