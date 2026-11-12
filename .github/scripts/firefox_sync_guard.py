#!/usr/bin/env python3
"""Fails when a Firefox merge brought back what AkhiBrowser removed, and lists what it newly turned on.

Usage: firefox_sync_guard.py <commit before the merge>
"""

import re
import subprocess
import sys
from pathlib import Path

FENIX = "mobile/android/fenix/app"
JAVA = f"{FENIX}/src/main/java/org/mozilla/fenix"
# file, text that must stay, what it keeps away
MUST_STAY = [
    (f"{JAVA}/FeatureFlags.kt", "onboardingFeatureEnabled = false", "Firefox's onboarding"),
    (f"{FENIX}/proguard-rules.pro", "-keepnames class org.mozilla.** { *; }", "the crash at startup"),
    (f"{JAVA}/components/AkhiExtension.kt", "installBuiltInWebExtension", "the built-in extension"),
    (f"{JAVA}/home/ui/Homepage.kt", "AkhiHomeCard.Card", "the prayer times and verse on the home screen"),
    (f"{FENIX}/src/main/res/drawable/ic_firefox.xml", "M26.00,26.00", "the shield instead of the fox"),
]
SETTINGS = f"{JAVA}/utils/Settings.kt"
# Android's privacy defaults: a marker comment and the default right after it
PRIVACY = [
    ("telemetry goes to Mozilla's servers, also the default of the usage ping and experiments", "default = false,",
     "telemetry, the usage ping and experiments off"),
    ("crash reports go to Mozilla's servers", "default = CrashReportOption.Never.toString(),", "crash reports off"),
    ("no stories on the homepage, as on desktop", "defaultValue = { false },", "Pocket stories off"),
    ("no AI page summaries, the page would be sent to an AI service", "default = { false },", "AI page summaries off"),
    ("secure by default", "default = true,", "HTTPS-only"),
    ("private by default", "true,", "private by default"),
    ("strict tracking protection by default", "false,", "strict tracking protection"),
]
SPONSORED_OFF = 3
WATCHED_PREFS = ["browser/app/profile/firefox.js", "mobile/android/app/geckoview-prefs.js"]


def main():
    before = sys.argv[1]
    failures = []
    for path, text, keeps in MUST_STAY:
        file = Path(path)
        if not file.exists() or text not in file.read_text(encoding="utf-8"):
            failures.append(f"- `{path}` lost `{text}`: {keeps}")
    settings = Path(SETTINGS).read_text(encoding="utf-8") if Path(SETTINGS).exists() else ""
    for marker, default, keeps in PRIVACY:
        if not re.search(r"// AkhiBrowser: " + re.escape(marker) + r"\n\s*" + re.escape(default), settings):
            failures.append(f"- `{SETTINGS}` lost `{marker}` / `{default}`: {keeps}")
    sponsored = len(re.findall(r"// AkhiBrowser: no sponsored content\n\s*default(Value)? = (\{ )?false", settings))
    if sponsored < SPONSORED_OFF:
        failures.append(f"- `{SETTINGS}` has {sponsored} of {SPONSORED_OFF} sponsored content defaults off")
    diff = subprocess.run(
        ["git", "diff", before, "HEAD", "--", *WATCHED_PREFS],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    ).stdout
    turned_on = re.findall(r'^\+\s*pref\("([^"]+)",\s*true', diff, re.M)
    print("### What the merge turned on, to look at")
    print("\n".join(f"- `{name}`" for name in turned_on) or "Nothing.")
    if failures:
        print("### Brought back or lost, the merge stops here")
        print("\n".join(failures))
        sys.exit(1)


if __name__ == "__main__":
    main()
