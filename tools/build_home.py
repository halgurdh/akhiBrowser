#!/usr/bin/env python3
"""Builds /nl/ and /ar/: the home page (index.html) with its Dutch and Arabic texts already in the HTML, so search
engines find a Dutch and an Arabic home page of their own. Change index.html (its texts, const NL and const AR, and
META), then run

    python tools/build_home.py

It also keeps /nl/ and /ar/ in sitemap.xml.
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://akhibrowser.com"
# pages that have a Dutch and an Arabic version at /nl/... and /ar/...
PAGES = r"(?:blog|compare|affiliate|money|privacy|setup|kit|faq|newsletter|delete-account)/"


def texts(source, name):
    block = re.search(r"const %s = \{\n(.*?)\n\};" % name, source, re.S).group(1)
    return {k: json.loads(v) for k, v in re.findall(r'^"([\w-]+)": (".*"),?$', block, re.M)}


def meta(source, lang):
    block = re.search(r"\n    %s: \{\n(.*?)\n    \}," % lang, source, re.S).group(1)
    return {k: json.loads(v) for k, v in re.findall(r'^\s+(title|description): (".*"),$', block, re.M)}


def build(source, lang, words, info):
    page = source
    # the texts: each element's data-t text, as the page's script shows it
    page = re.sub(
        r'(<(\w+)\b[^>]*\bdata-t="([\w-]+)"[^>]*>).*?(</\2>)',
        lambda m: m.group(1) + words[m.group(3)] + m.group(4) if m.group(3) in words else m.group(0),
        page,
        flags=re.S,
    )
    # translated attributes: data-a="name:key"
    def attribute(m):
        tag, name, key = m.group(0), m.group(1), m.group(2)
        if key not in words:
            return tag
        value = html.escape(words[key], quote=True)
        return re.sub(r'\b%s="[^"]*"' % re.escape(name), lambda _: f'{name}="{value}"', tag, count=1)

    page = re.sub(r'<[^>]*\bdata-a="([\w-]+):([\w-]+)"[^>]*>', attribute, page)
    title, description = html.escape(info["title"]), html.escape(info["description"], quote=True)
    url = f"{SITE}/{lang}/"
    head = [
        ('<html lang="en">', '<html lang="%s"%s data-home="%s">' % (lang, ' dir="rtl"' if lang == "ar" else "", lang)),
        (re.search(r"<title>.*?</title>", page).group(0), f"<title>{title}</title>"),
        (re.search(r'<meta name="description" content="[^"]*">', page).group(0), f'<meta name="description" content="{description}">'),
        ('<link rel="canonical" href="https://akhibrowser.com/">', f'<link rel="canonical" href="{url}">'),
        (re.search(r'<meta property="og:title" content="[^"]*">', page).group(0), f'<meta property="og:title" content="{title}">'),
        (re.search(r'<meta property="og:description" content="[^"]*">', page).group(0), f'<meta property="og:description" content="{description}">'),
        ('<meta property="og:url" content="https://akhibrowser.com/">', f'<meta property="og:url" content="{url}">'),
    ]
    for old, new in head:
        assert page.count(old) >= 1, old
        page = page.replace(old, new, 1)
    # the page lives one folder down: pictures and videos from /assets/, links to the pages in this language
    page = re.sub(r'(\b(?:src|href|poster|srcset)="|, )assets/', r"\1/assets/", page)
    page = re.sub(r'href="/(%s[^"]*)"' % PAGES, rf'href="/{lang}/\1"', page)
    page = page.replace('href="/#', f'href="/{lang}/#')
    return page


def main():
    source = (ROOT / "index.html").read_text(encoding="utf-8")
    for lang, name in (("nl", "NL"), ("ar", "AR")):
        target = ROOT / lang / "index.html"
        target.write_text(build(source, lang, texts(source, name), meta(source, lang)), encoding="utf-8", newline="\n")
    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    for lang in ("ar", "nl"):
        line = f"  <url><loc>{SITE}/{lang}/</loc></url>"
        if line not in sitemap:
            sitemap = sitemap.replace(f"  <url><loc>{SITE}/</loc></url>\n", f"  <url><loc>{SITE}/</loc></url>\n{line}\n", 1)
    # in order: /, /nl/, /ar/
    (ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8", newline="\n")
    print("built /nl/ and /ar/")


if __name__ == "__main__":
    main()
