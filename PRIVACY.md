# AkhiBrowser: privacy policy

Last updated: 14-11-2026

This policy covers the AkhiBrowser website, browser for Android and Windows, and extension for Firefox and Chrome.
AkhiBrowser is made by Halgurd Hussein. The browser and extensions have no account of their own and no ads. Their only
analytics is one anonymous count a day in the browser, without an id (see [What leaves your device](#what-leaves-your-device)).
We do not sell data.

The browser and extension do their work on your device, but they have to contact a few services. The website loads
Google Tag Manager. This page lists those services.

## The website (akhibrowser.com)

When you visit the website, it loads Google Tag Manager (`GTM-N2MF3XPS`) from Google. Google receives your IP address
and technical request information. Analytics tags enabled in the container may also collect page views and events,
depending on its configuration. Google's handling of this information is covered by
[Google's privacy policy](https://policies.google.com/privacy). The tag loads when the page loads; the website does not
currently show a consent prompt.

The forms to become an affiliate, sponsor or partner load Cloudflare Turnstile, a check against robots, once you start
filling one in. Cloudflare receives your IP address and information about your browser for that check, under
[Cloudflare's Turnstile privacy addendum](https://www.cloudflare.com/turnstile-privacy-policy/). What you type in the form
is emailed to us and used only to answer you. For affiliates, see [Affiliates](#affiliates).

If you open the website through an affiliate's link (`?ref=<code>`), the website keeps that code in your browser's
local storage and adds it to the checkout links, and asks our license server whether it is a VIP code, to show the VIP
price. The code is then kept on the subscription in Stripe, so the affiliate can be paid. Nothing else about you is
added.

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
- **AkhiBrowser's partner code, to a search engine we have a partner contract with**, in the address of a search you
  start in the browser. The engine pays us a small share of what it earns. The code says only that the search came from
  AkhiBrowser: we receive nothing about you or your searches. Firefox's own codes for Mozilla are taken out.
- **Requests to Mozilla's servers, without anything that identifies you beyond your IP address**, for add-ons
  (addons.mozilla.org, from which uBlock Origin is installed while ad blocking is on), and for security and block list
  updates (Remote Settings, Safe Browsing lists).
- **Ad block lists**, downloaded from the list providers set in uBlock Origin.
- **Video codecs (Windows)**, downloaded from Mozilla, Cisco and Google so that videos play.
- **An anonymous count, once a day, to our license server** (akhi-license.akhibrowser.workers.dev, on Cloudflare): the
  browser's version, its system, whether this is its first count of the week or month or after a new install, and
  whether Premium is on (free, Premium or Family). There is no id, and nothing of what you visit. The server only keeps
  the sums per day, so it can't tell two browsers apart; your IP address is only used against abuse and not kept. You
  can turn it off in the AkhiBrowser settings, under "Count me anonymously".
- **Update check (Windows, and the Android app from GitHub).** Once a day the browser asks GitHub whether a new release
  is out, and downloads it from GitHub. GitHub sees your IP address, under
  [GitHub's privacy statement](https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement).
  The Android app from Google Play is updated by Google Play instead.

### Only if you choose to

- **Premium, from Google Play.** Purchases go through Google Play, under
  [Google's privacy policy](https://policies.google.com/privacy). The app only asks Google Play whether Premium is active,
  and we receive no payment details. If you ask for a license key for your other devices, the app sends the Google Play
  purchase token and product to our license server, which asks Google Play whether that purchase is current, then and at
  each check of the key. The token says nothing about you; the server keeps it only inside the key it gives you.
- **Premium, with a license key** (Windows, and the Android app from GitHub): see [Premium license key](#premium-license-key).
- **Sync.** If you sign in with a Mozilla account, your email address and the data you choose to sync go to Mozilla,
  encrypted, under [Mozilla's privacy notice](https://www.mozilla.org/privacy/mozilla-accounts/). To delete that account,
  use Mozilla's account settings.
- **Usage data and crash reports to Mozilla.** These are off by default, and only go to Mozilla if you turn them on in
  Settings.
- **Support AkhiBrowser when you shop.** Off by default. If you turn it on and go to one of our partner shops yourself
  (typed, from a bookmark or from the start page), AkhiBrowser adds its partner code to that visit, so the shop pays us a
  small share of a purchase. The shop learns that you came through AkhiBrowser, nothing more; we receive nothing about
  you or what you buy. A link from another site keeps its own code. Tips on the start page with an affiliate link are
  labelled as such.
- **Parent report by email (Family).** Off by default. If a parent turns it on and enters an email address, it is sent
  with the license key to our license server, which mails a link to confirm it. Once confirmed, the server keeps a hash
  of the key, a hash of the address and the address encrypted (AES-256-GCM). The browser then sends, with the key, the
  address and a random install ID, what happened: a protection turned off, the parent PIN entered wrong too often or
  removed, the key removed, the phone filter stopped, and once a week the number of blocks by reason. Never an address
  or anything visited. The server keeps a hash of the install ID with when it last reported, so it can mail the parent
  once when a device hasn't reported for 8 days; a device silent for 60 days is forgotten. Each mail has a link that
  stops the reports and deletes the address.
- **Filter the whole phone (Android, Family).** Off by default. When a parent turns it on, every app's site lookups go
  through a local VPN on the phone to Cloudflare's family DNS, the same service as above. Nothing else goes through it,
  and nothing of it comes to us.
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

## Affiliates

This applies only to people who recommend AkhiBrowser for a commission (schools and mosques, and invited VIPs), not to
users of the browser:

- **Your application** (name, email address, organisation) is emailed to us. If we accept it, your name, email address
  and organisation are kept in our license server's database (on Cloudflare), with your code, to send you your code,
  what you earned each month, and when it is paid.
- **Your IBAN and account holder's name**, if you fill them in with the button in your welcome mail, are kept only
  encrypted (AES-256-GCM). We decrypt them only to make a transfer, on a page that shows them to us; they are never put
  in an email. Your bank and ours record the transfer, as with any payment.
- **Your commission** is counted from the Stripe payments that carry your code: their amounts and dates. You don't learn
  who bought, and buyers don't learn who you are.

When you stop, or if you ask us, we delete your name, email address and IBAN from the database. Records of the payments
we made to you are kept as long as the law requires for bookkeeping. To see, correct or delete your details, email us.

## Children

AkhiBrowser is meant for adults and for parents, who can use it to supervise a family device. It isn't directed at
children, and nothing in it collects information from them. Filters can miss things: a parent should not rely on them
alone.

## Contact

support@akhibrowser.com
