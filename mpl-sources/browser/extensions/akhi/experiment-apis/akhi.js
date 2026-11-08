/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

"use strict";

/* global Ci, ExtensionAPI, ExtensionCommon, IOUtils, PathUtils, Services */

const lazy = {};
ChromeUtils.defineESModuleGetters(lazy, {
  AddonManager: "resource://gre/modules/AddonManager.sys.mjs",
  AppConstants: "resource://gre/modules/AppConstants.sys.mjs",
  ExtensionPermissions: "resource://gre/modules/ExtensionPermissions.sys.mjs",
  ExtensionStorageIDB: "resource://gre/modules/ExtensionStorageIDB.sys.mjs",
  SearchService: "moz-src:///toolkit/components/search/SearchService.sys.mjs",
});

const PRIVATE_ALLOWED_PERMISSION = "internal:privateBrowsingAllowed";
const HARDWARE_VIDEO_PREFS = ["media.hardware-video-decoding.enabled", "media.ffvpx-hw.enabled"];
const HOME_PAGE_PREF = "browser.startup.homepage";

// next to the profiles, not in one: it stays when the browser is installed again and gets a new profile
function donatedNotePath() {
  return PathUtils.join(Services.dirsvc.get("UAppData", Ci.nsIFile).path, "donated");
}

this.akhi = class extends ExtensionAPI {
  getAPI(context) {
    const EventManager = ExtensionCommon.EventManager;
    const prefBranch = "extensions.akhi.";

    return {
      akhi: {
        onPrefChange: new EventManager({
          context,
          name: "akhi.onPrefChange",
          register: (fire, name) => {
            const prefName = `${prefBranch}${name}`;
            const callback = () => {
              fire.async(name).catch(() => {});
            };
            Services.prefs.addObserver(prefName, callback);
            return () => {
              Services.prefs.removeObserver(prefName, callback);
            };
          },
        }).api(),

        async getPref(name, defaultValue) {
          return Services.prefs.getBoolPref(
            `${prefBranch}${name}`,
            defaultValue
          );
        },

        async isDebugBuild() {
          return lazy.AppConstants.DEBUG;
        },

        async setPref(name, value) {
          Services.prefs.setBoolPref(`${prefBranch}${name}`, value);
        },

        // Android: a video decoded by the graphics chip reads as black in a page (canvas, VideoFrame), the image check
        // can't see it and it stays blurred. Decoded by the processor while videos are checked.
        async setReadableVideos(readable) {
          if (lazy.AppConstants.platform !== "android") {
            return;
          }
          for (const name of HARDWARE_VIDEO_PREFS) {
            if (readable) {
              Services.prefs.setBoolPref(name, false);
            } else {
              Services.prefs.clearUserPref(name);
            }
          }
        },

        // like choosing "Strict" in the privacy settings: all its prefs follow (ContentBlockingPrefs, desktop)
        async setStrictTrackingProtection() {
          Services.prefs.setStringPref("browser.contentblocking.category", "strict");
        },

        // The page of new tabs and the home page, like chrome_url_overrides.newtab and chrome_settings_overrides,
        // without their "keep or disable the add-on" doorhangers, which would disable AkhiBrowser's own extension.
        // A home page the user chose is kept. Desktop only; null brings Firefox's pages back.
        async setStartPage(url) {
          if (lazy.AppConstants.platform === "android") {
            return;
          }
          const { AboutNewTab } = ChromeUtils.importESModule(
            "resource:///modules/AboutNewTab.sys.mjs"
          );
          const homePage = Services.prefs.getStringPref(HOME_PAGE_PREF, "");
          const isOurs = homePage.startsWith(context.extension.baseURI.spec);
          if (url) {
            AboutNewTab.newTabURL = url;
            if (isOurs || !Services.prefs.prefHasUserValue(HOME_PAGE_PREF)) {
              Services.prefs.setStringPref(HOME_PAGE_PREF, url);
            }
          } else {
            if (AboutNewTab.newTabURLOverridden) {
              AboutNewTab.resetNewTabURL();
            }
            if (isOurs) {
              Services.prefs.clearUserPref(HOME_PAGE_PREF);
            }
          }
        },

        // SessionStore is desktop only
        async whenSessionRestored() {
          try {
            const { SessionStore } = ChromeUtils.importESModule(
              "moz-src:///browser/components/sessionstore/SessionStore.sys.mjs"
            );
            await SessionStore.promiseAllWindowsRestored;
          } catch (e) {}
        },

        async isDonatedOnDevice() {
          return IOUtils.exists(donatedNotePath());
        },

        async noteDonatedOnDevice() {
          await IOUtils.writeUTF8(donatedNotePath(), "");
        },

        async setDefaultSearchEngine(id, name) {
          const search = lazy.SearchService;
          await search.init();
          const engine = search.getEngineById(id) ?? search.getEngineByName(name);
          if (!engine) {
            return false;
          }
          await search.setDefault(engine, search.CHANGE_REASON.USER);
          return true;
        },

        // uBlock Origin has no API for its trusted sites: they are in its storage (netWhitelist), which it reads
        // when it starts
        async setTrustedSite(id, hostname, trusted) {
          const extension = WebExtensionPolicy.getByID(id)?.extension;
          if (!extension) {
            return false;
          }
          const db = await lazy.ExtensionStorageIDB.open(
            lazy.ExtensionStorageIDB.getStoragePrincipal(extension),
            extension.hasPermission("unlimitedStorage")
          );
          const { netWhitelist } = await db.get(["netWhitelist"]);
          const sites = Array.isArray(netWhitelist) ? netWhitelist : [];
          if (sites.includes(hostname) === trusted) {
            return false;
          }
          await db.set({
            netWhitelist: trusted
              ? [...sites, hostname]
              : sites.filter(site => site !== hostname),
          });
          await (await lazy.AddonManager.getAddonByID(id)).reload();
          return true;
        },

        async keepAddonInstalled(id, url) {
          const addon = await lazy.AddonManager.getAddonByID(id);
          if (!addon) {
            await installAddon(id, url);
          } else if (addon.userDisabled) {
            await addon.enable();
          }
          if (keptAddons.has(id)) {
            return;
          }
          const listener = {
            onDisabled(disabled) {
              if (disabled.id === id) {
                disabled.enable().catch(console.error);
              }
            },
            onUninstalled(uninstalled) {
              if (uninstalled.id === id) {
                installAddon(id, url).catch(console.error);
              }
            },
          };
          keptAddons.set(id, listener);
          lazy.AddonManager.addAddonListener(listener);
          context.callOnClose({
            close: () => {
              lazy.AddonManager.removeAddonListener(listener);
              keptAddons.delete(id);
            },
          });
        },

        async releaseAddon(id) {
          const listener = keptAddons.get(id);
          if (listener) {
            lazy.AddonManager.removeAddonListener(listener);
            keptAddons.delete(id);
          }
          await (await lazy.AddonManager.getAddonByID(id))?.disable();
        },
      },
    };
  }
};

// id: the AddonManager listener that keeps it installed and enabled
const keptAddons = new Map();

async function installAddon(id, url) {
  const install = await lazy.AddonManager.getInstallForURL(url, {
    telemetryInfo: { source: "akhi" },
  });
  const addon = await install.install();
  await lazy.ExtensionPermissions.add(id, {
    permissions: [PRIVATE_ALLOWED_PERMISSION],
    origins: [],
  });
  await addon.reload();
}
