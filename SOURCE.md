# Source availability (MPL 2.0)

AkhiBrowser is built on [Mozilla Firefox](https://www.mozilla.org/firefox/), which is licensed under the
[Mozilla Public License 2.0](LICENSE). The MPL is a file-level license: the files that come from Firefox, and
AkhiBrowser's own changes to those files, stay under the MPL, and their source is available to anyone who receives
an AkhiBrowser build.

## What is covered by the MPL

- Every unmodified file that comes from Firefox.
- AkhiBrowser's changes to Firefox's own files. These are small, and are only branding, preference defaults and
  build wiring: for example the app name, colors, vendor and copyright strings, the lines that register the built-in
  extension (`browser/extensions/moz.build`, `browser/moz.configure`), the Android `build.gradle` and
  `Core.kt`/`Settings.kt`, and the Windows version files (`browser/app/module.ver`, `config/create_rc.py`).

## What is not covered by the MPL

AkhiBrowser's own new files are separate works under their own terms, not covered by the MPL: the built-in
extension (`browser/extensions/akhi/`), the branding (`browser/branding/akhi/`) and the build configurations. They
do not contain Firefox source code.

## How to get the source of the MPL files

If you have an AkhiBrowser build and want the source of the MPL-covered files, request it from the author:

> **Contact:** _(add your source-request address here, for example a GitHub repository, a web page or an email.)_

The source will be provided by reasonable means, at no more than the cost of distribution, as the MPL requires.

AkhiBrowser isn't affiliated with or endorsed by Mozilla. Firefox is a trademark of the Mozilla Foundation.
