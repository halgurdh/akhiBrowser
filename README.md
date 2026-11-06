# AkhiBrowser

A privacy-focused browser for Muslims, built on [Firefox](https://www.firefox.com/), for Windows, macOS, Linux
and Android.

Thanks to [Mohamed Sadiq](https://github.com/mohamedsadiqaguenaou): the background music removal builds on his
[NoMusic](https://github.com/mohamedsadiqaguenaou/NoMusic), and his [Safaa](https://github.com/mohamedsadiqaguenaou/safaa)
and [NoHaram](https://github.com/mohamedsadiqaguenaou/NoHaram) inspired the image filter. Give them a star.

📲 Available for Android (8.0+) and Windows (64-bit)
📥 [More info](https://halgurdh.github.io/akhiBrowser/)

(Insha'Allah, it will also be available soon as a standalone extension for Firefox and Chrome.)

Please note:
On Windows, SmartScreen may display a warning; if so, click "More info" → "Run anyway."

On Android: Tap the downloaded file → Enable "Allow from this source" if prompted → Tap Install.

## Free features

All protections below are free, built in, and run on your device. Your history, pages and images stay on your device; no
telemetry, studies or crash reports go to Mozilla. To block adult sites at the network level, the desktop browser looks up
site names through Cloudflare's family DNS, so Cloudflare sees the names of the sites you visit. It also fetches ad block
lists, and video codecs from Mozilla, Cisco and Google. A Premium license key is checked with the license server, with a random install id: a key works on 3 devices at a time. Once a day the browser asks GitHub whether a new release is out, as it has no automatic updates.

- **Ad, tracker and malware blocking (on by default):** [uBlock Origin](https://github.com/gorhill/uBlock) is
  installed from addons.mozilla.org and kept on while ad blocking is on, with a built-in blocker of ad, tracker and
  malware domains underneath it (from the first page, and the empty ad slots it leaves are hidden). On a site that
  refuses ad blockers, its ads are let through, with a button to block them again.
- **No music:** removes background music from videos and keeps the voices
  ([NoMusic](https://github.com/mohamedsadiqaguenaou/NoMusic): FastEnhancer, then RNNoise). The Lite model on phones
  and slow computers. (slightly re-written to work on lightweight devices)
- **Nudity blur:** images, CSS backgrounds, videos and canvases stay blurred until an on-device model
  ([NSFWJS](https://github.com/infinitered/nsfwjs)) has checked them, so nothing flashes. Unsafe ones stay blurred,
  or only their persons are. One that can't be checked, like a video another site won't let pages read, is shown.
  Works with srcset and `<picture>`, lazy loading, carousels, shadow DOM, iframes and `blob:` images, down to 24 px
  thumbnails. The same rule for everyone, of any age. (slightly re-written to work on lightweight devices)
- **Choose who to blur:** for women (the default), men, or both, a person is blurred by what is seen of
  them, not the whole image: a woman when her hair or body shows (her face and hands may), a man from the navel to
  the knees. A woman too small to judge stays blurred. A person whose gender is unclear can be judged as a woman, which is off by
  default.
- **Adult and haram blocking:** adult, alcohol, drugs, vaping and gambling sites are blocked, and so are pages that
  label themselves adult. SafeSearch is forced on Google, Bing, DuckDuckGo and Yahoo, and so is YouTube Restricted
  Mode.
- **Search blocking:** searches for adult or haram content are blocked in 11 languages. Questions about them stay
  allowed ("why is alcohol haram").
- **12 languages:** English, Arabic, Persian, Kurdish (Sorani), Urdu, Turkish, French, German, Dutch, Spanish,
  Indonesian and Malay, right to left where needed.

## Premium

Premium adds **Recognize hijab**, which shows a woman who is covered instead of blurring every woman; the option to set
a parental PIN; and optional parent controls to block chosen sites, allow only approved sites, set time limits with
bedtime and school hours, and see a summary of blocked pages without addresses. Parent controls are off until enabled,
and their data stays on the device. An active Premium license is needed to set a PIN, but a PIN that's already set keeps
working without Premium.

Premium is a monthly, yearly or lifetime purchase: through Google Play in a Google Play build, or through Stripe with a
license key and no account.

The free protections are on by default. Each can be turned off in the AkhiBrowser shield of the toolbar (on Android:
menu, **Extensions**, **AkhiBrowser**), which also chooses who to blur. A parental PIN can lock these off.

**Parental PIN:** turning a protection off, or changing or removing the PIN, requires it; turning a protection on does
not. Only a salted hash of the PIN is kept, and five wrong tries make it wait a minute.

## Light on old devices

Only what's on the screen is checked. Images seen before are answered from a cache, without reading their pixels
again. The face and body models (6 MB) only run when a gender is chosen, on the largest persons of an image (one on
phones). The model loads only when it's needed, in its own thread, so page loads never wait on it. It runs on the GPU
(WebGL) on computers, and on WebAssembly SIMD on phones and computers with few cores. Videos and canvases are only looked at while a page has them.

## Building

Set up your machine with [Mozilla's build instructions](https://firefox-source-docs.mozilla.org/setup/index.html)
first. Then pull the two private parts (see [Public and private](#public-and-private)), with a GitHub account that
has access to them:

```sh
git submodule update --init
```

Every build uses a config from `browser/branding/akhi/mozconfigs/`:

| Platform | Config | Commands |
| --- | --- | --- |
| Windows, macOS, Linux | `akhi-desktop` | `./mach build`, `./mach run`, `./mach package` |
| Windows ARM | `akhi-windows-arm64` | `./mach build`, `./mach package` |
| Android 64-bit ARM | `akhi-android-arm64` | `./mach build`, `./mach gradle :fenix:assembleRelease` |

Run each with the config, for example `MOZCONFIG=browser/branding/akhi/mozconfigs/akhi-desktop ./mach build`. For
front-end only work, `akhi-desktop-debug` downloads prebuilt C++ and Rust.

- **macOS:** build `akhi-desktop` on a Mac with Xcode installed. `./mach package` makes the `.dmg`. Sign it with
  `codesign` and notarize it with `xcrun notarytool`, or Gatekeeper blocks it on other Macs.
- **Windows:** `./mach package` makes the installer. Without an Authenticode signature, SmartScreen shows "Windows
  protected your PC". Sign the installer and `AkhiBrowser.exe` with `signtool`, using a code signing certificate
  ([SignPath Foundation](https://signpath.org/) is free for open source, Azure Trusted Signing is low cost).
  SmartScreen trusts a new certificate after enough people have installed with it.
- **Android:** to sign a release, set `AKHI_SIGNING_PROPERTIES` to a properties file with `storeFile`, `storePassword`,
  `keyAlias` and `keyPassword`. Android is 64-bit only. The APKs are split per ABI (`arm64-v8a`, `x86_64`), plus a
  universal one.
- **Google Play:** after `./mach build`, run the command below. It writes the `.aab` to upload and a universal APK of the
  same build to test with to `artifacts/play-<version>/`, and fails on what Play would refuse. A Play build sells Premium
  with Play Billing instead of Stripe, has no updater, is arm64 only, and has no advertising ID or install permission.
  `browser/branding/akhi/play/CONSOLE.md` has the answers for the Play Console.

  ```sh
  python browser/branding/akhi/tools/build_play.py --signing <signing.properties>
  ```

- **iOS:** not available. Outside the EU, Apple only allows browsers built on WebKit, not on Firefox's engine (Gecko).
  This tree only has Mozilla's prototype of Gecko on iOS (`mobile/ios`, for the simulator). An iOS version would be built on
  WebKit: a Safari web extension, or a browser with these protections built in, as Safari web extensions only run in
  Safari. A first test of the Safari one is in `browser/extensions/akhi/safari/` (private).

### Releasing an update

Windows and the APK from GitHub update themselves from the latest GitHub release. Google Play updates its own builds, and
macOS only shows a notice.

1. Set the new version in `browser/config/akhi_version.txt` and `CURRENT_VERSION` in
   `browser/extensions/akhi/lib/updates.js`, and build.
2. Windows: after `./mach package`, run this, which writes the signed `.mar` and `update-<target>.xml` to
   `<objdir>/dist/update/`:

   ```sh
   python browser/branding/akhi/tools/make_update.py --objdir obj-akhi-desktop --keys <folder of the primary key>
   ```

3. Android: sign with the same key as before, or Android refuses the update. Name the APK
   `AkhiBrowser-<version>-android-<abi>.apk`, and list it in `SHA256SUMS.txt`.
4. Upload all of it to a GitHub release tagged `v<version>`, and mark it as the latest.

The public certificates built into the updater are in `browser/branding/akhi/update/`. Keep the private keys out of every
repository and backed up: without them, installed browsers can't take another update.

To update the domain lists, or to make the icons again from the logo (needs Pillow):

```sh
python browser/extensions/akhi/tools/make_filter_lists.py
python browser/extensions/akhi/tools/make_gender_model.py
python browser/extensions/akhi/tools/make_body_model.py
python browser/branding/akhi/tools/make_icons.py
```

## Public and private

AkhiBrowser's own code is in two private repositories, pulled into this one as git submodules:

| Path | Private repository | What's in it |
| --- | --- | --- |
| `browser/extensions/akhi/` | `halgurdh/akhi-extension` | The built-in extension, shared by desktop and Android: no music, the content filters, the built-in ad blocker, the image and face checks, colour-blindness correction, the settings and parental PIN. It can't be removed. |
| `browser/branding/akhi/` | `halgurdh/akhi-branding` | Names, installer and icons in TV Akhi's colors, the icon tool, and the build configs (`mozconfigs/`). |

What stays public here is Firefox itself and AkhiBrowser's changes to Firefox's own files: the Android app
([mobile/android/fenix/](mobile/android/fenix/), package `org.akhibrowser`, with `AkhiExtension.kt` that installs the
extension, and its launcher icons), the Windows file properties and the build settings. These are under the
[Mozilla Public License 2.0](LICENSE), which asks that their source stays available to everyone who gets the browser.
Without access to the private repositories this tree doesn't build AkhiBrowser.

The extension is plain JavaScript inside the installed browser, so keeping its repository private hides its history
and tools, not the code itself.

For Android TV, see [TV Akhi](https://github.com/halgurdh/tv-akhi), with the same no music and content filters.

## Contact

- Website: [akhibrowser.com](https://akhibrowser.com)
- Support: [support@akhibrowser.com](mailto:support@akhibrowser.com)

## Credits and licenses

Based on Firefox by Mozilla, under the [Mozilla Public License 2.0](LICENSE). It also uses
[NoMusic](https://github.com/mohamedsadiqaguenaou/NoMusic) (ISC), [FastEnhancer](https://github.com/aask1357/fastenhancer)
(MIT), [RNNoise](https://github.com/xiph/rnnoise) (BSD), [NSFWJS](https://github.com/infinitered/nsfwjs) (MIT),
[TensorFlow.js](https://github.com/tensorflow/tfjs) with its COCO-SSD and BlazeFace models (Apache 2.0), Intel's
[age-gender-recognition-retail-0013](https://github.com/openvinotoolkit/open_model_zoo) (Apache 2.0), and the
[StevenBlack/hosts](https://github.com/StevenBlack/hosts) (MIT) and
[Block List Project](https://github.com/blocklistproject/Lists) (Unlicense) domain lists.

The source of the MPL-covered files is available to anyone who receives an AkhiBrowser build; see
[SOURCE.md](SOURCE.md).

AkhiBrowser isn't affiliated with or endorsed by Mozilla. Firefox is a trademark of the Mozilla Foundation.
