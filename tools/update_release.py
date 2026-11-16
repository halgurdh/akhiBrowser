"""Puts AkhiBrowser's latest GitHub release on the home page: its number in the structured data, and the line under
the features ("Latest version: AkhiBrowser 1.3.0, 13 November 2026. What's new") linking to its release notes, in
English, Dutch and Arabic. Run before tools/build_home.py, which carries it to /nl/ and /ar/.

The latest release is the one GitHub marks as latest (not a draft or pre-release). GITHUB_TOKEN, when set, is used
for the request, so that it isn't rate limited.
"""
import json
import os
import re
import sys
import urllib.request
from datetime import date
from pathlib import Path

REPO = "halgurdh/akhiBrowser"
ROOT = Path(__file__).resolve().parent.parent

MONTHS = {
    "en": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
           "November", "December"],
    "nl": ["januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus", "september", "oktober",
           "november", "december"],
    "ar": ["يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو", "يوليو", "أغسطس", "سبتمبر", "أكتوبر", "نوفمبر",
           "ديسمبر"],
}
LINE = {
    "en": 'Latest version: <a href="{url}">AkhiBrowser {version}</a>, {date}. <a href="{url}">What\'s new</a>.',
    "nl": 'Nieuwste versie: <a href="{url}">AkhiBrowser {version}</a>, {date}. <a href="{url}">Wat is er nieuw</a>.',
    "ar": 'أحدث إصدار: <a href="{url}">AkhiBrowser {version}</a>، {date}. <a href="{url}">ما الجديد</a>.',
}


def latest():
    request = urllib.request.Request(
        f"https://api.github.com/repos/{REPO}/releases/latest",
        headers={"Accept": "application/vnd.github+json", "User-Agent": "akhibrowser.com"},
    )
    if os.environ.get("GITHUB_TOKEN"):
        request.add_header("Authorization", f"Bearer {os.environ['GITHUB_TOKEN']}")
    with urllib.request.urlopen(request, timeout=30) as response:
        release = json.load(response)
    version = release["tag_name"].lstrip("v")
    published = date.fromisoformat(release["published_at"][:10])
    return version, published, release["html_url"]


def line(lang, version, published, url):
    when = f"{published.day} {MONTHS[lang][published.month - 1]} {published.year}"
    return LINE[lang].format(url=url, version=version, date=when)


def update(page, version, published, url):
    page, n = re.subn(r'"softwareVersion": "[^"]*"', f'"softwareVersion": "{version}"', page, count=1)
    assert n == 1, "softwareVersion not found"
    page, n = re.subn(r'(<p class="note" data-t="f9">).*?(</p>)',
                      lambda m: m.group(1) + line("en", version, published, url) + m.group(2), page, count=1)
    assert n == 1, "the f9 note not found"
    # the Dutch and Arabic texts, in that order in the page; "</" as "<\/" in a script
    for lang in ("nl", "ar"):
        text = json.dumps(line(lang, version, published, url), ensure_ascii=False).replace("</", "<\\/")
        page, n = re.subn(r'^"f9": ".*",$', lambda _: f'"f9": {text},', page, count=1, flags=re.M)
        assert n == 1, f"the {lang} f9 text not found"
        # the next one: mark the done line until both are replaced
        page = page.replace(f'"f9": {text},', f'"f9-done": {text},', 1)
    return page.replace('"f9-done": ', '"f9": ')


def main():
    version, published, url = latest()
    path = ROOT / "index.html"
    page = path.read_text(encoding="utf-8")
    new = update(page, version, published, url)
    if new != page:
        path.write_text(new, encoding="utf-8", newline="\n")
        print(f"Latest release on the home page: {version}")
    else:
        print(f"Already up to date: {version}")


if __name__ == "__main__":
    sys.exit(main())
