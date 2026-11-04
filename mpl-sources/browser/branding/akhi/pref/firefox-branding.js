/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

// This file contains branding-specific prefs.

pref("startup.homepage_override_url", "");
pref("startup.homepage_welcome_url", "");
pref("startup.homepage_welcome_url.additional", "");
// The time interval between checks for a new version (in seconds)
pref("app.update.interval", 86400); // 24 hours
// Give the user x seconds to react before showing the big UI. default=24 hours
pref("app.update.promptWaitTime", 86400);
// URL user can browse to manually if for some reason all update installation
// attempts fail.
pref("app.update.url.manual", "https://github.com/halgurdh/akhiBrowser/releases");
// A default value for the "More information about this update" link
// supplied in the "An update is available" page of the update wizard.
pref("app.update.url.details", "https://github.com/halgurdh/akhiBrowser/releases");

// The number of days a binary is permitted to be old
// without checking for an update.  This assumes that
// app.update.checkInstallTime is true.
pref("app.update.checkInstallTime.days", 2);

// Give the user x seconds to reboot before showing a badge on the hamburger
// button. default=immediately
pref("app.update.badgeWaitTime", 0);

// Number of usages of the web console.
// If this is less than 5, then pasting code into the web console is disabled
pref("devtools.selfxss.count", 5);

// AkhiBrowser: no Mozilla privacy notice, terms of use notice or data collection
pref("datareporting.policy.dataSubmissionEnabled", false);
pref("datareporting.policy.firstRunURL", "");
pref("datareporting.healthreport.uploadEnabled", false);
pref("datareporting.usage.uploadEnabled", false);
pref("toolkit.telemetry.unified", false);
pref("termsofuse.bypassNotification", true);
pref("app.shield.optoutstudies.enabled", false);
pref("app.normandy.enabled", false);
pref("nimbus.rollouts.enabled", false);
pref("browser.discovery.enabled", false);
pref("browser.newtabpage.activity-stream.feeds.telemetry", false);
pref("browser.newtabpage.activity-stream.telemetry", false);

// AkhiBrowser: the new tab has the search box and the user's shortcuts, without stories, widgets, weather or
// sponsored shortcuts. The default shortcuts are Islamic sites.
pref("browser.newtabpage.activity-stream.feeds.section.topstories", false);
pref("browser.newtabpage.activity-stream.showSponsored", false);
pref("browser.newtabpage.activity-stream.system.showSponsored", false);
pref("browser.newtabpage.activity-stream.showSponsoredTopSites", false);
pref("browser.newtabpage.activity-stream.showWeather", false);
pref("browser.newtabpage.activity-stream.system.showWeather", false);
pref("browser.newtabpage.activity-stream.widgets.enabled", false);
pref("browser.newtabpage.activity-stream.widgets.system.enabled", false);
pref("browser.newtabpage.activity-stream.unifiedAds.tiles.enabled", false);
pref("browser.newtabpage.activity-stream.unifiedAds.spocs.enabled", false);
pref("browser.newtabpage.activity-stream.asrouter.userprefs.cfr.addons", false);
pref("browser.newtabpage.activity-stream.asrouter.userprefs.cfr.features", false);
pref("browser.topsites.contile.enabled", false);
pref("browser.topsites.useRemoteSetting", false);
pref("browser.newtabpage.activity-stream.default.sites", "https://quran.com/,https://sunnah.com/,https://www.islamicfinder.org/");

// AkhiBrowser: no sponsored or trending suggestions in the address bar
pref("browser.urlbar.quicksuggest.enabled", false);
pref("browser.urlbar.suggest.quicksuggest.sponsored", false);
pref("browser.urlbar.suggest.quicksuggest.nonsponsored", false);
pref("browser.urlbar.sponsoredTopSites", false);
pref("browser.urlbar.suggest.trending", false);
pref("browser.urlbar.trending.featureGate", false);
pref("browser.urlbar.suggest.yelp", false);
pref("browser.urlbar.suggest.weather", false);
pref("browser.preferences.moreFromMozilla", false);
pref("browser.vpn_promo.enabled", false);
pref("extensions.htmlaboutaddons.recommendations.enabled", false);

// AkhiBrowser: secure and private by default. Strict tracking protection is set by the built-in extension on the
// first run (browser/extensions/akhi/background.js).
pref("dom.security.https_only_mode", true);
pref("privacy.globalprivacycontrol.enabled", true);
// DNS over HTTPS, with Cloudflare's family DNS, which also blocks adult and malware sites
pref("network.trr.mode", 2);
pref("network.trr.uri", "https://family.cloudflare-dns.com/dns-query");
pref("network.trr.custom_uri", "https://family.cloudflare-dns.com/dns-query");
// WebRTC doesn't reveal the local IP addresses
pref("media.peerconnection.ice.default_address_only", true);
// no connections to sites before they are opened
pref("network.prefetch-next", false);
pref("network.dns.disablePrefetch", true);
pref("network.http.speculative-parallel-limit", 0);
pref("browser.urlbar.speculativeConnect.enabled", false);
pref("browser.places.speculativeConnect.enabled", false);
// Mozilla Monitor
pref("signon.management.page.breach-alerts.enabled", false);

// AkhiBrowser: no Mozilla account or Sync (no sign-in, no device pairing, no send-tab)
pref("identity.fxaccounts.enabled", false);
pref("identity.fxaccounts.pairing.enabled", false);
pref("identity.fxaccounts.toolbar.enabled", false);
pref("identity.fxaccounts.telemetry.clientAssociationPing.enabled", false);
pref("identity.fxaccounts.telemetry.clientInfoPing.enabled", false);

// AkhiBrowser: all telemetry off, nothing sent to Mozilla (the master switches are above)
pref("toolkit.telemetry.enabled", false);
pref("toolkit.telemetry.server", "data:,");
pref("toolkit.telemetry.archive.enabled", false);
pref("toolkit.telemetry.newProfilePing.enabled", false);
pref("toolkit.telemetry.shutdownPingSender.enabled", false);
pref("toolkit.telemetry.updatePing.enabled", false);
pref("toolkit.telemetry.bhrPing.enabled", false);
pref("toolkit.telemetry.firstShutdownPing.enabled", false);
pref("toolkit.telemetry.coverage.opt-out", true);
pref("toolkit.coverage.opt-out", true);
pref("toolkit.coverage.endpoint.base", "");
pref("browser.ping-centre.telemetry", false);

// AkhiBrowser: no experiments or remote experiment configuration (Normandy and Nimbus)
pref("app.normandy.api_url", "");
pref("messaging-system.rsexperimentloader.enabled", false);

// AkhiBrowser: no web push notifications, and no Monitor/VPN promos in the protections dashboard
pref("dom.push.enabled", false);
pref("dom.push.connection.enabled", false);
pref("browser.contentblocking.report.monitor.enabled", false);
pref("browser.contentblocking.report.lockwise.enabled", false);
pref("browser.contentblocking.report.hide_vpn_banner", true);
