/* akhibrowser.com: Google Analytics, and a Reddit ad's purchase reported to Reddit, only after consent (Consent Mode v2, set to denied in each page's head), the
 * clicks that matter as events (downloads, plans), the visitor's GA id passed to the checkout so the purchase the
 * license server reports is theirs, and the website as the source of Google Play installs. */
(function () {
  "use strict";
  var KEY = "akhi-consent";
  var TEXT = {
    en: ["We'd like to count visits and downloads with Google Analytics, and tell Reddit when one of its ads led to a purchase. No ads here, nothing sold.", "Allow", "No thanks", "Privacy"],
    nl: ["We tellen graag bezoeken en downloads met Google Analytics, en laten Reddit weten wanneer een advertentie tot een aankoop leidde. Geen advertenties hier, niets verkocht.", "Toestaan", "Nee, bedankt", "Privacy"],
    ar: ["نود أن نحسب الزيارات والتنزيلات باستخدام Google Analytics، وأن نخبر Reddit عندما يؤدي أحد إعلاناته إلى عملية شراء. لا إعلانات هنا ولا بيع لبياناتك.", "سماح", "لا، شكرًا", "الخصوصية"],
    de: ["Wir würden Besuche und Downloads gern mit Google Analytics zählen und Reddit mitteilen, wenn eine seiner Anzeigen zu einem Kauf geführt hat. Keine Werbung hier, nichts wird verkauft.", "Erlauben", "Nein, danke", "Datenschutz"],
    fr: ["Nous aimerions compter les visites et les téléchargements avec Google Analytics, et indiquer à Reddit quand l'une de ses annonces a mené à un achat. Pas de pub ici, rien n'est vendu.", "Autoriser", "Non merci", "Confidentialité"],
    es: ["Nos gustaría contar visitas y descargas con Google Analytics, y avisar a Reddit cuando uno de sus anuncios lleve a una compra. Sin anuncios aquí, no vendemos nada.", "Permitir", "No, gracias", "Privacidad"],
    tr: ["Ziyaretleri ve indirmeleri Google Analytics ile saymak ve bir Reddit reklamı satın almaya yol açtığında Reddit'e bildirmek istiyoruz. Burada reklam yok, hiçbir şey satılmaz.", "İzin ver", "Hayır, teşekkürler", "Gizlilik"],
    id: ["Kami ingin menghitung kunjungan dan unduhan dengan Google Analytics, dan memberi tahu Reddit saat salah satu iklannya menghasilkan pembelian. Tanpa iklan di sini, tidak ada yang dijual.", "Izinkan", "Tidak, terima kasih", "Privasi"],
    ms: ["Kami ingin mengira lawatan dan muat turun dengan Google Analytics, dan memberitahu Reddit apabila salah satu iklannya membawa kepada pembelian. Tiada iklan di sini, tiada yang dijual.", "Benarkan", "Tidak, terima kasih", "Privasi"],
    ur: ["ہم Google Analytics سے وزٹ اور ڈاؤن لوڈ گننا چاہتے ہیں، اور Reddit کو بتانا چاہتے ہیں جب اس کا کوئی اشتہار خریداری تک لے جائے۔ یہاں کوئی اشتہار نہیں، کچھ فروخت نہیں ہوتا۔", "اجازت دیں", "نہیں، شکریہ", "رازداری"],
    fa: ["می‌خواهیم بازدیدها و دانلودها را با Google Analytics بشماریم و وقتی یکی از تبلیغات Reddit به خرید منجر شد به Reddit اطلاع دهیم. اینجا تبلیغی نیست، چیزی فروخته نمی‌شود.", "اجازه", "نه، ممنون", "حریم خصوصی"],
    ckb: ["دەمانەوێت سەردان و داگرتنەکان بە Google Analytics بژمێرین، و ئاگاداری Reddit بکەینەوە کاتێک یەکێک لە ڕیکلامەکانی بووە هۆی کڕین. لێرە هیچ ڕیکلامێک نییە، هیچ شتێک نافرۆشرێت.", "ڕێگەدان", "نەخێر، سوپاس", "تایبەتمەندی"],
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
  function choose(granted) {
    try {
      localStorage.setItem(KEY, granted ? "granted" : "denied");
    } catch (e) {}
    gtag("consent", "update", { analytics_storage: granted ? "granted" : "denied" });
    if (granted) {
      window.dataLayer.push({ event: "consent_granted" });
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
      ".akhi-consent .yes{background:#f4be34;color:#03282e}.akhi-consent .no{background:transparent;color:#fff}";
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

  function track(link) {
    var href = link.href || "";
    var lang = (document.documentElement.lang || "en").split("-")[0];
    for (var i = 0; i < STORES.length; i++) {
      if (STORES[i][0].test(href)) {
        window.dataLayer.push({ event: "download_click", store: STORES[i][1], page_language: lang });
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

  document.addEventListener(
    "click",
    function (event) {
      var link = event.target && event.target.closest ? event.target.closest("a[href]") : null;
      if (link) {
        track(link);
      }
    },
    true
  );

  function start() {
    redditClick();
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
