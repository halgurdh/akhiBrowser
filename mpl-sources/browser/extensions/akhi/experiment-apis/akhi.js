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

        // like choosing "Strict" in the privacy settings: all its prefs follow (ContentBlockingPrefs, desktop)
        async setStrictTrackingProtection() {
          Services.prefs.setStringPref("browser.contentblocking.category", "strict");
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
