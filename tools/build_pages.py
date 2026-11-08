#!/usr/bin/env python3
"""Builds the blog and comparison pages, the sitemap and robots.txt from tools/content.py.

To add an article: add an entry to ARTICLES in content.py with its English and Dutch text, then run

    python tools/build_pages.py
"""
import html
import json
from pathlib import Path

from content import ARTICLES, COMPARE, UI

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://akhibrowser.com"
GTM = """<script async src="https://www.googletagmanager.com/gtm.js?id=GTM-N2MF3XPS"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
</script>"""


def url_of(lang, path):
    return f"/{path}" if lang == "en" else f"/nl/{path}"


def page(lang, path, title, description, body, json_ld=None):
    ui = UI[lang]
    other = "nl" if lang == "en" else "en"
    canonical = SITE + url_of(lang, path)
    ld = f'<script type="application/ld+json">{json.dumps(json_ld, ensure_ascii=False)}</script>\n' if json_ld else ""
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en" href="{SITE + url_of('en', path)}">
<link rel="alternate" hreflang="nl" href="{SITE + url_of('nl', path)}">
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
    <a class="brand" href="/"><img src="/assets/akhi.svg" alt="" width="32" height="32"><span><b>Akhi</b>Browser</span></a>
    <span class="links">
      <a href="{url_of(lang, 'blog/')}">{ui['blog']}</a>
      <a href="{url_of(lang, 'compare/kahf-browser/')}">{ui['compare']}</a>
      <a href="/#download">{ui['download']}</a>
      <a href="{url_of(other, path)}" hreflang="{other}" lang="{other}">{other.upper()}</a>
    </span>
  </nav>
</header>
<main class="wrap">
{body}
</main>
<footer class="wrap">
  <p>{ui['footer']}</p>
</footer>
</body>
</html>
"""


def cta(lang):
    ui = UI[lang]
    return f"""<aside class="cta"><h2>{ui['cta_title']}</h2><p>{ui['cta_text']}</p><a class="btn" href="/#download">{ui['download']}</a></aside>"""


def article_page(lang, article):
    text = article[lang]
    path = f"blog/{article['slug']}/"
    ld = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": text["title"],
        "description": text["description"],
        "datePublished": article["date"],
        "dateModified": article["date"],
        "inLanguage": lang,
        "image": f"{SITE}/assets/og.png",
        "author": {"@type": "Organization", "name": "AkhiBrowser", "url": SITE},
        "publisher": {"@type": "Organization", "name": "AkhiBrowser", "url": SITE},
        "mainEntityOfPage": SITE + url_of(lang, path),
    }
    body = f"""<article>
<p class="crumb"><a href="{url_of(lang, 'blog/')}">{UI[lang]['blog']}</a></p>
<h1>{text['title']}</h1>
<p class="date"><time datetime="{article['date']}">{article['date']}</time></p>
{text['body']}
</article>
{cta(lang)}"""
    return path, page(lang, path, f"{text['title']} | AkhiBrowser", text["description"], body, ld)


def index_page(lang):
    ui = UI[lang]
    items = "\n".join(
        f"""<li><a href="{url_of(lang, 'blog/' + a['slug'] + '/')}"><h2>{a[lang]['title']}</h2></a><p>{a[lang]['description']}</p></li>"""
        for a in sorted(ARTICLES, key=lambda a: a["date"], reverse=True)
    )
    compare = COMPARE[lang]
    items += f"""\n<li><a href="{url_of(lang, 'compare/kahf-browser/')}"><h2>{compare['title']}</h2></a><p>{compare['description']}</p></li>"""
    body = f"""<h1>{ui['blog_title']}</h1>\n<p class="lead">{ui['blog_lead']}</p>\n<ul class="posts">\n{items}\n</ul>"""
    return "blog/", page(lang, "blog/", f"{ui['blog_title']} | AkhiBrowser", ui["blog_lead"], body)


def compare_page(lang):
    text = COMPARE[lang]
    rows = "\n".join(
        f"<tr><th scope=\"row\">{row[0]}</th><td>{row[1]}</td><td>{row[2]}</td></tr>" for row in text["rows"]
    )
    sources = " ".join(f'<a href="{url}">{name}</a>' for name, url in COMPARE["sources"])
    body = f"""<article>
<h1>{text['title']}</h1>
<p class="lead">{text['lead']}</p>
<div class="table"><table>
<thead><tr><th scope="col">{text['head'][0]}</th><th scope="col">{text['head'][1]}</th><th scope="col">{text['head'][2]}</th></tr></thead>
<tbody>
{rows}
</tbody>
</table></div>
{text['after']}
<p class="note">{text['sources_label']} {sources}</p>
</article>
{cta(lang)}"""
    return "compare/kahf-browser/", page(lang, "compare/kahf-browser/", text["seo_title"], text["description"], body)


def write(lang, path, content):
    target = ROOT / url_of(lang, path).lstrip("/") / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8", newline="\n")


def main():
    paths = []
    for lang in ("en", "nl"):
        builders = [index_page(lang), compare_page(lang)] + [article_page(lang, a) for a in ARTICLES]
        for path, content in builders:
            write(lang, path, content)
            paths.append(url_of(lang, path))
    urls = ["/"] + paths
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
