"""Tells Bing, Yandex, Seznam, Naver and Yep (IndexNow) which pages of the site changed, after a push to gh-pages.

python tools/indexnow.py              pages changed in the last commit
python tools/indexnow.py <from>       pages changed since commit <from>, e.g. origin/gh-pages before the push
python tools/indexnow.py --all        every page in sitemap.xml
python tools/indexnow.py --dry-run    only print them
"""

import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOST = "akhibrowser.com"
SITE = f"https://{HOST}"
KEY = "47ce7c845e7d40c3872dbf7c46505ecd"


def sitemap_urls():
    return re.findall(r"<loc>([^<]+)</loc>", (ROOT / "sitemap.xml").read_text(encoding="utf-8"))


def changed_urls(since):
    files = subprocess.run(
        ["git", "diff", "--name-only", since, "HEAD"], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout.split()
    known = set(sitemap_urls())
    urls = []
    for name in files:
        if name == "index.html" or name.endswith("/index.html"):
            url = f"{SITE}/{name[: -len('index.html')]}"
            if url in known:
                urls.append(url)
    return urls


def main(args):
    dry = "--dry-run" in args
    args = [a for a in args if a != "--dry-run"]
    if args == ["--all"]:
        urls = sitemap_urls()
    else:
        urls = changed_urls(args[0] if args else "HEAD~1")
    if not urls:
        print("No changed pages.")
        return
    print("\n".join(urls))
    if dry:
        return
    body = json.dumps(
        {"host": HOST, "key": KEY, "keyLocation": f"{SITE}/{KEY}.txt", "urlList": urls}
    ).encode()
    request = urllib.request.Request(
        "https://api.indexnow.org/indexnow",
        data=body,
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            print(f"IndexNow: {response.status}, {len(urls)} pages")
    except urllib.error.HTTPError as error:
        sys.exit(f"IndexNow: {error.code} {error.read().decode(errors='replace')}")


if __name__ == "__main__":
    main(sys.argv[1:])
