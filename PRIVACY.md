# AkhiBrowser: privacy policy

Last updated: 07-11-2026

This policy covers the AkhiBrowser browser for Android and Windows, and the AkhiBrowser extension for Firefox and
Chrome. AkhiBrowser is made by Halgurd Hussein. It has no account of its own, no ads and no analytics. We do not sell or
share data. We, the makers, receive nothing about you or the sites you visit.

The browser and the extension do their work on your device, but they have to contact a few services. This page lists
them all.

## The browser (Android and Windows)

AkhiBrowser is a web browser built on Firefox.

### What leaves your device

- **Sites you visit.** Like any browser, AkhiBrowser connects to the sites you open, and they can see your IP address and
  what you do there. Their own privacy policies apply.
- **Names of the sites you visit, to Cloudflare.** To block adult and malware sites at the network level, AkhiBrowser
  looks up site names through Cloudflare's family DNS (family.cloudflare-dns.com), over an encrypted connection.
  Cloudflare sees the names of the sites and your IP address, under
  [its policy for this service](https://developers.cloudflare.com/1.1.1.1/privacy/public-dns-resolver/). You can change
  or turn this off in Settings, under DNS over HTTPS.
- **Your search terms, to the search engine you use**, as you type them when search suggestions are on.
- **Requests to Mozilla's servers, without anything that identifies you beyond your IP address**, for add-ons
  (addons.mozilla.org, from which uBlock Origin is installed while ad blocking is on), and for security and block list
  updates (Remote Settings, Safe Browsing lists).
- **Ad block lists**, downloaded from the list providers set in uBlock Origin.
- **Video codecs (Windows)**, downloaded from Mozilla, Cisco and Google so that videos play.
- **Update check (Windows, and the Android app from GitHub).** Once a day the browser asks GitHub whether a new release
  is out, and downloads it from GitHub. GitHub sees your IP address, under
  [GitHub's privacy statement](https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement).
  The Android app from Google Play is updated by Google Play instead.

### Only if you choose to

- **Premium, from Google Play.** Purchases go through Google Play, under
  [Google's privacy policy](https://policies.google.com/privacy). The app only asks Google Play whether Premium is active,
  and we receive no payment details.
- **Premium, with a license key** (Windows, and the Android app from GitHub): see [Premium license key](#premium-license-key).
- **Sync.** If you sign in with a Mozilla account, your email address and the data you choose to sync go to Mozilla,
  encrypted, under [Mozilla's privacy notice](https://www.mozilla.org/privacy/mozilla-accounts/). To delete that account,
  use Mozilla's account settings.
- **Usage data and crash reports to Mozilla.** These are off by default, and only go to Mozilla if you turn them on in
  Settings.
- **Camera, microphone and location.** Your device asks you first when a site you are on wants them. They go only to
  that site, and only if you allow it.

### What stays on your device

Your history, bookmarks, passwords, open tabs and settings stay on your device unless you turn on Sync. To check pages:

- Page addresses are compared with block lists on the device.
- Images and video frames are checked for nudity, and for the persons in them, by models that run on the device. Faces
  and bodies are looked at to decide what to blur. Nothing about them is kept or sent. To check an image, the browser may
  download it again from the site that already shows it, without your cookies.
- Audio is cleaned of music on the device.

Parent controls, the parental PIN (only a salted hash of it), the activity summary (blocks counted by day and reason,
with no addresses) and the time on social sites for the feed limit (minutes counted for today, with no addresses) stay
on the device.

Uninstalling the browser deletes all of this. You can also clear it in Settings, under Delete browsing data.

## The extension (Firefox and Chrome)

The extension checks page addresses, images, audio and your settings on your device, and sends none of them to us.

- **Images.** To check an image, the extension may download it again from the site that already shows it, without your
  cookies.
- **Premium.** Nothing else leaves your device unless you enter a Premium key: see
  [Premium license key](#premium-license-key). In Firefox, you are asked first, and you can turn this off in the
  add-on's settings, which stops the checks and ends Premium when its current token runs out.

Settings, your license key, the parental PIN and the activity summary (blocks counted by day and reason, with no
addresses) stay in the extension's local storage. So does the time on social sites for the feed limit, when it's on:
minutes counted for today, with no addresses. Removing the extension deletes them.

## Premium license key

This applies to the extension, to Windows and to the Android app from GitHub, only if you enter a license key:

- **Your license key and a random install ID** go to our license server (akhi-license.akhibrowser.workers.dev, on
  Cloudflare) to check the key and limit it to 3 devices. The check repeats every few days. The server keeps hashes of
  the key and of the install ID, not your name, email or browsing data. A device unused for 30 days is released.
- **Your license key** goes to the same server if you open "manage subscription", to get a Stripe link.

Buying Premium happens on a Stripe page, under [Stripe's privacy policy](https://stripe.com/privacy). We do not see your
payment details.

## Children

AkhiBrowser is meant for adults and for parents, who can use it to supervise a family device. It isn't directed at
children, and nothing in it collects information from them. Filters can miss things: a parent should not rely on them
alone.

## Contact

support@akhibrowser.com
