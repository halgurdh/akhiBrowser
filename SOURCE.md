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
extension (`browser/extensions/akhi/`, see its `LICENSE`), the branding's own images and the build configurations.
They do not contain Firefox source code. The exceptions are the few files of those two private repositories with an MPL
header, which stay under the MPL and are published in [mpl-sources/](mpl-sources/).

## How to get the source of the MPL files

They are public: this repository, at the tag of each release, with [mpl-sources/](mpl-sources/) for the ones that live
in the private repositories. If you can't get them there, ask at
[github.com/halgurdh/akhiBrowser/issues](https://github.com/halgurdh/akhiBrowser/issues).

AkhiBrowser isn't affiliated with or endorsed by Mozilla. Firefox is a trademark of the Mozilla Foundation.
