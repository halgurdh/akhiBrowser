/* akhibrowser.com: Google Analytics, the Reddit pixel (visits and download clicks from a Reddit ad) and a Reddit ad's download, sign-up, application or purchase reported to Reddit by the license server, only after consent (Google Tag Manager itself loads only then; Consent Mode v2 is set to denied in each page's head), the
 * clicks that matter as events (downloads, plans), a newsletter sign-up or an application from a Reddit ad, the visitor's GA id passed to the checkout so the purchase the
 * license server reports is theirs, and the website as the source of Google Play installs. */
(function () {
  "use strict";
  var KEY = "akhi-consent";
  var TEXT = {
    en: ["Can we see how people find AkhiBrowser? Google Analytics and Reddit help us count visits and downloads, and which of our ads work. We never sell your data.", "Allow", "No thanks", "Privacy"],
    nl: ["Mogen we zien hoe mensen AkhiBrowser vinden? Google Analytics en Reddit helpen ons bezoeken en downloads te tellen, en welke advertenties werken. We verkopen je gegevens nooit.", "Toestaan", "Nee, bedankt", "Privacy"],
    ar: ["هل تسمح لنا بمعرفة كيف يجد الناس AkhiBrowser؟ يساعدنا Google Analytics وReddit على عدّ الزيارات والتنزيلات ومعرفة أي إعلاناتنا تنجح. لا نبيع بياناتك أبدًا.", "سماح", "لا، شكرًا", "الخصوصية"],
    de: ["Dürfen wir sehen, wie Menschen AkhiBrowser finden? Google Analytics und Reddit helfen uns, Besuche und Downloads zu zählen und zu sehen, welche unserer Anzeigen wirken. Wir verkaufen deine Daten nie.", "Erlauben", "Nein, danke", "Datenschutz"],
    fr: ["Pouvons-nous voir comment les gens trouvent AkhiBrowser ? Google Analytics et Reddit nous aident à compter les visites et les téléchargements, et à savoir quelles annonces fonctionnent. Nous ne vendons jamais vos données.", "Autoriser", "Non merci", "Confidentialité"],
    es: ["¿Podemos ver cómo la gente encuentra AkhiBrowser? Google Analytics y Reddit nos ayudan a contar visitas y descargas, y a saber qué anuncios funcionan. Nunca vendemos tus datos.", "Permitir", "No, gracias", "Privacidad"],
    tr: ["İnsanların AkhiBrowser'ı nasıl bulduğunu görebilir miyiz? Google Analytics ve Reddit, ziyaretleri ve indirmeleri saymamıza ve hangi reklamlarımızın işe yaradığını görmemize yardımcı olur. Verilerinizi asla satmayız.", "İzin ver", "Hayır, teşekkürler", "Gizlilik"],
    id: ["Bolehkah kami melihat bagaimana orang menemukan AkhiBrowser? Google Analytics dan Reddit membantu kami menghitung kunjungan dan unduhan, serta iklan mana yang berhasil. Kami tidak pernah menjual data Anda.", "Izinkan", "Tidak, terima kasih", "Privasi"],
    ms: ["Bolehkah kami melihat bagaimana orang menemui AkhiBrowser? Google Analytics dan Reddit membantu kami mengira lawatan dan muat turun, serta iklan mana yang berkesan. Kami tidak pernah menjual data anda.", "Benarkan", "Tidak, terima kasih", "Privasi"],
    ur: ["کیا ہم دیکھ سکتے ہیں کہ لوگ AkhiBrowser کیسے ڈھونڈتے ہیں؟ Google Analytics اور Reddit وزٹ اور ڈاؤن لوڈ گننے اور یہ جاننے میں مدد کرتے ہیں کہ ہمارے کون سے اشتہار کام کرتے ہیں۔ ہم آپ کا ڈیٹا کبھی نہیں بیچتے۔", "اجازت دیں", "نہیں، شکریہ", "رازداری"],
    fa: ["اجازه می‌دهید ببینیم مردم چگونه AkhiBrowser را پیدا می‌کنند؟ Google Analytics و Reddit به ما کمک می‌کنند بازدیدها و دانلودها را بشماریم و ببینیم کدام تبلیغات ما مؤثرند. ما هرگز داده‌های شما را نمی‌فروشیم.", "اجازه", "نه، ممنون", "حریم خصوصی"],
    ckb: ["دەتوانین ببینین خەڵک چۆن AkhiBrowser دەدۆزنەوە؟ Google Analytics و Reddit یارمەتیمان دەدەن سەردان و داگرتنەکان بژمێرین و بزانین کام ڕیکلامەکانمان کاریگەرن. هەرگیز زانیارییەکانت نافرۆشین.", "ڕێگەدان", "نەخێر، سوپاس", "تایبەتمەندی"],
  };

  function gtag() {
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push(arguments);
  }
  function stored() {
    try {
      return localStorage.getItem(KEY);
    } catch (e) {
      return null;
    }
  }
  // Google Tag Manager only after consent: before it nothing of Google loads
  function googleTags() {
    if (!document.querySelector('script[src*="googletagmanager.com/gtm.js"]')) {
      var script = document.createElement("script");
      script.async = true;
      script.src = "https://www.googletagmanager.com/gtm.js?id=GTM-PW3SL6DM";
      document.head.appendChild(script);
    }
  }

  function choose(granted) {
    try {
      localStorage.setItem(KEY, granted ? "granted" : "denied");
    } catch (e) {}
    gtag("consent", "update", { analytics_storage: granted ? "granted" : "denied" });
    if (granted) {
      googleTags();
      window.dataLayer.push({ event: "consent_granted" });
      reddit();
      confirmedSignUp();
    }
  }

  // the Reddit pixel, loaded only after consent: a page visit, and a download click as the custom event "Download",
  // so Reddit Ads can show which ad, headline and country led to downloads
  var PIXEL = "a2_jyyhv3ol4pme";
  function reddit() {
    if (!window.rdt) {
      var p = (window.rdt = function () {
        p.sendEvent ? p.sendEvent.apply(p, arguments) : p.callQueue.push(arguments);
      });
      p.callQueue = [];
      var script = document.createElement("script");
      script.src = "https://www.redditstatic.com/ads/pixel.js";
      script.async = true;
      document.head.appendChild(script);
      window.rdt("init", PIXEL);
      window.rdt("track", "PageVisit");
    }
    return window.rdt;
  }

  // the newsletter page after its confirm link (?confirmed=<the sign-up's event id>): the pixel's SignUp, with the id
  // the license server used, so Reddit counts it once; also when Allow is pressed on this page only now
  function confirmedSignUp() {
    var id = new URLSearchParams(location.search).get("confirmed");
    if (id && /^[A-Za-z0-9-]{8,64}$/.test(id) && /\/newsletter\/$/.test(location.pathname) && stored() === "granted") {
      reddit()("track", "SignUp", { conversionId: id });
    }
  }

  function showBanner() {
    var lang = (document.documentElement.lang || "en").toLowerCase().split("-")[0];
    var t = TEXT[lang] || TEXT.en;
    var bar = document.createElement("div");
    bar.className = "akhi-consent";
    bar.setAttribute("role", "dialog");
    bar.setAttribute("aria-live", "polite");
    bar.dir = /^(ar|ur|fa|ckb)$/.test(lang) ? "rtl" : "ltr";
    var style = document.createElement("style");
    style.textContent =
      ".akhi-consent{position:fixed;left:12px;right:12px;bottom:12px;z-index:9999;max-width:640px;margin:0 auto;" +
      "display:flex;flex-wrap:wrap;gap:10px;align-items:center;padding:14px 16px;border:1px solid #1c5a58;" +
      "border-radius:14px;background:#03282e;color:#fff;font:14px/1.45 system-ui,sans-serif;box-shadow:0 8px 30px #0008}" +
      ".akhi-consent p{flex:1 1 260px;margin:0}.akhi-consent a{color:#f4be34}" +
      ".akhi-consent button{font:inherit;font-weight:600;border-radius:999px;padding:8px 16px;cursor:pointer;border:1px solid #f4be34}" +
      ".akhi-consent button{background:#f4be34;color:#03282e;min-width:120px}" +
      ".akhi-consent button.no{background:transparent;color:#fff;border-color:#ffffff80}" +
      ".akhi-consent button.no:hover{border-color:#fff;background:#ffffff14}";
    var text = document.createElement("p");
    text.textContent = t[0] + " ";
    var link = document.createElement("a");
    link.href = (lang === "nl" ? "/nl" : lang === "ar" ? "/ar" : "") + "/privacy/";
    link.textContent = t[3];
    text.appendChild(link);
    var yes = document.createElement("button");
    yes.type = "button";
    yes.className = "yes";
    yes.textContent = t[1];
    var no = document.createElement("button");
    no.type = "button";
    no.className = "no";
    no.textContent = t[2];
    yes.onclick = function () {
      choose(true);
      bar.remove();
    };
    no.onclick = function () {
      choose(false);
      bar.remove();
    };
    bar.append(style, text, no, yes);
    document.body.appendChild(bar);
  }

  // the Reddit ad click a visit came from (?rdt_cid=), kept for the visit; it goes to the checkout only after consent
  function redditClick() {
    var value = new URLSearchParams(location.search).get("rdt_cid");
    try {
      if (value && /^[A-Za-z0-9._~-]{8,200}$/.test(value)) {
        sessionStorage.setItem("akhi-rdt", value);
        return value;
      }
      return sessionStorage.getItem("akhi-rdt");
    } catch (e) {
      return value;
    }
  }

  // an id for one event, given to the pixel and to the license server alike, so Reddit counts the event once
  function eventId() {
    return window.crypto && crypto.randomUUID ? crypto.randomUUID() : String(Date.now()) + "-" + Math.random().toString(36).slice(2, 12);
  }

  // the visitor's GA client id ("GA1.1.123.456" → "123.456"), only there after consent
  function gaClientId() {
    var match = /(?:^|;\s*)_ga=GA\d\.\d\.(\d+\.\d+)/.exec(document.cookie);
    return match ? match[1] : null;
  }

  var STORES = [
    [/play\.google\.com/, "play"],
    [/apps\.microsoft\.com/, "ms_store"],
    [/get\.microsoft\.com\/installer/, "exe"],
    [/chromewebstore\.google\.com/, "chrome"],
    [/addons\.mozilla\.org/, "firefox"],
  ];

  // a store that can install on this device: Google Play on Android, the Windows stores on Windows, the browser
  // extensions on a computer. Nothing on an iPhone or iPad, where none of these installs anything.
  function fitsDevice(store) {
    var ua = navigator.userAgent || "";
    if (/Android/i.test(ua)) {
      return store === "play";
    }
    if (/iPhone|iPad|iPod/i.test(ua) || (/Macintosh/i.test(ua) && navigator.maxTouchPoints > 1)) {
      return false;
    }
    if (/Windows/i.test(ua)) {
      return store !== "play";
    }
    return store === "chrome" || store === "firefox";
  }
  // Reddit hears of a download once per visitor (30 days), so clicking every button, or one button ten times, is
  // still one; Google Analytics keeps counting every click
  var SENT = "akhi-download-sent";
  function firstDownload() {
    try {
      var last = Number(localStorage.getItem(SENT) || 0);
      if (Date.now() - last < 30 * 864e5) {
        return false;
      }
      localStorage.setItem(SENT, String(Date.now()));
    } catch (e) {}
    return true;
  }

  // the Reddit ad click in the Play link's referrer (rdt=), next to the UTM tags: the app reads it once after installing
  // and has the license server tell Reddit about the install (POST /reddit/install), so ads are judged by installs
  function addPlayClick(link, click) {
    try {
      var url = new URL(link.href);
      var referrer = new URLSearchParams(url.searchParams.get("referrer") || "");
      if (!referrer.has("rdt")) {
        referrer.set("rdt", click);
        url.searchParams.set("referrer", referrer.toString());
        link.href = url.href;
      }
    } catch (e) {}
  }

  function track(link) {
    var href = link.href || "";
    var lang = (document.documentElement.lang || "en").split("-")[0];
    for (var i = 0; i < STORES.length; i++) {
      if (STORES[i][0].test(href)) {
        window.dataLayer.push({ event: "download_click", store: STORES[i][1], page_language: lang });
        if (stored() === "granted") {
          var adClick = STORES[i][1] === "play" ? redditClick() : null;
          if (adClick) {
            addPlayClick(link, adClick);
          }
          if (fitsDevice(STORES[i][1]) && firstDownload()) {
            // the same id to the pixel and the license server, so Reddit counts it once, also when the pixel is blocked
            var id = eventId();
            reddit()("track", "Custom", { customEventName: "Download", conversionId: id });
            var click = redditClick();
            if (click && navigator.sendBeacon) {
              navigator.sendBeacon(
                "https://akhi-license.akhibrowser.workers.dev/reddit/download",
                new URLSearchParams({ rdt: click, store: STORES[i][1], id: id })
              );
            }
          }
          return true;
        }
        return;
      }
    }
    var buy = /akhi-license\.akhibrowser\.workers\.dev\/buy\/([a-z-]+)/.exec(href);
    if (buy) {
      window.dataLayer.push({ event: "begin_checkout", plan: buy[1], page_language: lang });
      var extra = [];
      var id = gaClientId();
      if (id && !/[?&]ga=/.test(href)) {
        extra.push("ga=" + encodeURIComponent(id));
      }
      var click = stored() === "granted" ? redditClick() : null;
      if (click && !/[?&]rdt=/.test(href)) {
        extra.push("rdt=" + encodeURIComponent(click));
      }
      if (extra.length) {
        link.href = href + (href.indexOf("?") < 0 ? "?" : "&") + extra.join("&");
      }
      return;
    }
    if (/akhi-license\.akhibrowser\.workers\.dev\/(school|redeem)/.test(href)) {
      window.dataLayer.push({ event: "generate_lead", form: RegExp.$1, page_language: lang });
    }
  }

  // Google Play installs from the site, in Play Console under where the visitor came from: the campaign's UTM tags
  // when they came with some (kept for the visit in sessionStorage, so a later page still has them), else
  // akhibrowser.com. The app reads only ref= of the referrer, so these don't touch an affiliate's code.
  var UTM = ["utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term"];
  function campaignOf() {
    var params = new URLSearchParams(location.search);
    var found = {};
    var any = false;
    UTM.forEach(function (name) {
      var value = params.get(name);
      if (value && /^[\w.\-~ ]{1,100}$/.test(value)) {
        found[name] = value;
        any = true;
      }
    });
    try {
      if (any) {
        sessionStorage.setItem("akhi-utm", JSON.stringify(found));
        return found;
      }
      return JSON.parse(sessionStorage.getItem("akhi-utm") || "null");
    } catch (e) {
      return any ? found : null;
    }
  }
  function tagPlayLinks() {
    var links = document.querySelectorAll('a[href*="play.google.com/store/apps/details?id=org.akhibrowser"]');
    var lang = (document.documentElement.lang || "en").split("-")[0];
    var campaign = campaignOf() || {
      utm_source: "akhibrowser.com",
      utm_medium: "website",
      utm_campaign: lang + location.pathname,
    };
    var referrer = Object.keys(campaign)
      .map(function (name) {
        return name + "=" + encodeURIComponent(campaign[name]);
      })
      .join("&");
    for (var i = 0; i < links.length; i++) {
      if (!/[?&]referrer=/.test(links[i].href)) {
        links[i].href += "&referrer=" + encodeURIComponent(referrer);
      }
    }
  }

  // an affiliate or partner application (Lead) or a newsletter sign-up (SignUp), after consent: an event id, and the
  // Reddit ad click when there is one, go with the form, so the license server sends it to Reddit. An application is
  // also the pixel's Lead with the same id, so Reddit counts it once. A sign-up counts only once the address is
  // confirmed: the confirm link leads back to the newsletter page with the id (confirmedSignUp).
  var FORMS = /akhi-license\.akhibrowser\.workers\.dev\/(newsletter|affiliate|partner)$/;
  function hidden(form, name, value) {
    var input = form.querySelector('input[type="hidden"][name="' + name + '"]');
    if (!input) {
      input = document.createElement("input");
      input.type = "hidden";
      input.name = name;
      form.appendChild(input);
    }
    input.value = value;
  }
  document.addEventListener("submit", function (event) {
    var form = event.target;
    var match = form && FORMS.exec(form.action || "");
    if (!match || event.defaultPrevented || stored() !== "granted" || form.dataset.reddit) {
      return;
    }
    form.dataset.reddit = "1";
    var id = eventId();
    var click = redditClick();
    hidden(form, "rdt_id", id);
    if (click) {
      hidden(form, "rdt", click);
    }
    if (match[1] === "newsletter") {
      return;
    }
    reddit()("track", "Lead", { conversionId: id });
    // a moment for the pixel's event to leave before the page goes
    event.preventDefault();
    setTimeout(function () {
      form.submit();
    }, 300);
  });

  document.addEventListener(
    "click",
    function (event) {
      var link = event.target && event.target.closest ? event.target.closest("a[href]") : null;
      if (link && track(link) && !event.defaultPrevented && event.button === 0 && !event.metaKey && !event.ctrlKey &&
          !event.shiftKey && !event.altKey && (!link.target || link.target === "_self")) {
        // the store opens in this tab: a moment for the Reddit event to leave before the page goes
        event.preventDefault();
        var href = link.href;
        setTimeout(function () {
          location.href = href;
        }, 300);
      }
    },
    true
  );

  function start() {
    redditClick();
    if (stored() === "granted") {
      googleTags();
      reddit();
    }
    confirmedSignUp();
    tagPlayLinks();
    if (!stored()) {
      showBanner();
    }
    // a way back to the choice: any link to #cookies
    document.addEventListener("click", function (event) {
      var link = event.target && event.target.closest ? event.target.closest('a[href="#cookies"]') : null;
      if (link) {
        event.preventDefault();
        try {
          localStorage.removeItem(KEY);
        } catch (e) {}
        if (!document.querySelector(".akhi-consent")) {
          showBanner();
        }
      }
    });
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start);
  } else {
    start();
  }
})();

// The lead agent (akhi-leads): sends what someone types in a contact or partner form, so it can be answered
// personally. Not newsletter, search or checkout forms; nothing is sent until a form is submitted.
(function () {
  var s = document.createElement("script");
  s.src = "https://akhi-leads.akhibrowser.workers.dev/capture.js";
  s.async = true;
  document.head.appendChild(s);
})();
