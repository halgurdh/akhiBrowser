/* Mega menu (desktop only): a top-level menu item opens a wide panel under the header, with its links on the left and
   featured cards (two by default, window.MEGA.maxCards) on the right. Configured by window.MEGA before this script (see the site's snippet). */
(function () {
  var M = window.MEGA;
  if (!M || !M.panels) return;
  var desktop = window.matchMedia("(min-width: " + (M.minWidth || 1024) + "px) and (hover: hover)");
  var lang = (document.documentElement.lang || "en").split("-")[0].toLowerCase();
  var MAX = M.maxCards || 2;
  var T = function (v) { return v && typeof v === "object" && !Array.isArray(v) ? (v[lang] || v.en || "") : v || ""; };
  // card texts: with fallback:false a language without its own text gets no cards (links only) instead of English
  var TC = M.fallback === false ? function (v) { return v && typeof v === "object" && !Array.isArray(v) ? v[lang] || "" : v || ""; } : T;

  function decode(html) {
    var d = document.createElement("textarea");
    d.innerHTML = String(html || "").replace(/<[^>]*>/g, "");
    return d.value.trim();
  }
  function cut(text, n) { text = decode(text); return text.length > n ? text.slice(0, n - 1).replace(/\s+\S*$/, "") + "…" : text; }
  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }

  var cache = {};
  function getJSON(url) {
    if (!cache[url]) cache[url] = fetch(url, { credentials: "same-origin" }).then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); });
    return cache[url];
  }
  function price(p) {
    if (!p || !p.prices) return "";
    var n = parseInt(p.prices.price, 10) / Math.pow(10, p.prices.currency_minor_unit || 2);
    if (!n) return T(M.texts.free) || "Free";
    return (p.prices.currency_symbol || "€") + n.toFixed(n % 1 ? 2 : 0).replace(".", lang === "en" ? "." : ",");
  }

  // cards the page already holds (window.MEGA_DATA, written by the site, e.g. a WordPress snippet): no request needed
  function given(src) { var d = window.MEGA_DATA, k = src && T(src.key); return d && k && Array.isArray(d[k]) ? d[k] : null; }

  // cards: [{img, badge, title, text, href, button}]
  function loadCards(src) {
    if (Array.isArray(src)) return Promise.resolve(src.map(function (c) { return Object.assign({}, c, { badge: TC(c.badge), title: TC(c.title), text: TC(c.text), button: TC(c.button), href: T(c.href) }); }).filter(function (c) { return c.title; }).slice(0, MAX));
    var n = Math.min(src.count || MAX, MAX);
    var pre = given(src);
    if (pre) return Promise.resolve(pre.slice(0, n).map(function (c) {
      return Object.assign({}, c, { badge: T(src.badge) || c.badge || (c.free ? T(M.texts && M.texts.free) || "Free" : ""), button: T(src.button) });
    }));
    if (src.type === "posts" || src.type === "cpt") {
      var base = src.type === "posts" ? "posts" : src.restBase;
      var url = "/wp-json/wp/v2/" + base + "?per_page=" + (src.fetch || n) + "&_embed=wp:featuredmedia,wp:term" + (T(src.query) ? "&" + T(src.query) : "");
      return getJSON(url).then(function (list) {
        if (src.filter) list = list.filter(function (p) { return src.filter(p, lang); });
        return list.slice(0, n).map(function (p) {
          var media = p._embedded && p._embedded["wp:featuredmedia"] && p._embedded["wp:featuredmedia"][0];
          var terms = (p._embedded && p._embedded["wp:term"] && p._embedded["wp:term"][0]) || [];
          var term = terms.filter(function (t) { return !src.skipTerms || src.skipTerms.indexOf(t.name) < 0; })[0];
          var size = media && media.media_details && media.media_details.sizes;
          return {
            img: (size && (size.medium_large || size.medium || size.large) || {}).source_url || (media && media.source_url),
            srcset: size ? Object.keys(size).filter(function (k) { return size[k].width >= 280 && size[k].width <= 1600 && !/^(woocommerce_gallery|shop_single)/.test(k); }).map(function (k) { return size[k].source_url + " " + size[k].width + "w"; }).join(", ") : "",
            badge: T(src.badge) || (term && decode(term.name)) || "",
            title: decode(p.title && p.title.rendered),
            text: cut(p.excerpt && p.excerpt.rendered, 80),
            href: p.link,
            button: T(src.button),
          };
        });
      });
    }
    if (src.type === "products") {
      return getJSON("/wp-json/wc/store/v1/products?per_page=" + (src.fetch || n) + (T(src.query) ? "&" + T(src.query) : "")).then(function (list) {
        if (src.filter) list = list.filter(function (p) { return src.filter(p, lang); });
        return list.slice(0, n).map(function (p) {
          var img = p.images && p.images[0];
          return { img: img && (img.thumbnail || img.src), srcset: img && img.srcset, badge: price(p), title: decode(p.name), text: cut(p.short_description || p.description, 80), href: p.permalink, button: T(src.button) };
        });
      });
    }
    return Promise.resolve([]);
  }

  function card(c) {
    var a = el("a", "mega-card");
    a.href = c.href || "#";
    if (/^https?:/.test(a.href) && a.host !== location.host) { a.target = "_blank"; a.rel = "noopener"; }
    var pic = el("div", "mega-pic");
    if (c.img) {
      var im = el("img");
      im.alt = ""; im.decoding = "async";
      if (c.full) im.onerror = function () { im.onerror = null; im.removeAttribute("srcset"); im.src = c.full; };
      if (c.srcset) { im.sizes = "(min-width: 1400px) 330px, 24vw"; im.srcset = c.srcset; }
      im.src = c.img;
      pic.appendChild(im);
    } else pic.classList.add("mega-noimg");
    if (c.badge) pic.appendChild(el("span", "mega-badge", c.badge));
    a.appendChild(pic);
    a.appendChild(el("strong", "mega-title", c.title));
    if (c.text) a.appendChild(el("span", "mega-text", c.text));
    if (c.button) a.appendChild(el("span", "mega-btn", c.button + " →"));
    return a;
  }

  var header = document.querySelector(M.header || "header");
  var topItems = Array.prototype.slice.call(document.querySelectorAll(M.items));
  if (!header || !topItems.length) return;

  var panel = el("div", "mega-panel");
  panel.setAttribute("role", "region");
  panel.hidden = true;
  document.body.appendChild(panel);

  var open = null, hideTimer = null, built = {};

  function position() {
    var bar = (open && open.closest(M.header || "header")) || header;
    var r = bar.getBoundingClientRect();
    panel.style.top = Math.max(0, r.bottom) + "px";
  }

  function build(i, cfg, li) {
    if (built[i]) return built[i];
    var box = el("div", "mega-inner");
    var left = el("div", "mega-left");
    var h = el("div", "mega-h");
    if (cfg.title === "item") { var head = li.querySelector("summary") || li.firstElementChild; h.textContent = head ? head.textContent.trim() : ""; } else h.innerHTML = T(cfg.title);
    left.appendChild(h);
    var ul = el("ul", "mega-links");
    var links = cfg.links === "submenu" || !cfg.links
      ? Array.prototype.slice.call(li.querySelectorAll(M.submenu || ":scope > ul a, :scope > .sub-menu a")).map(function (a) { return { text: a.textContent.trim(), href: a.href }; })
      : cfg.links.map(function (l) { return { text: T(l.text), href: T(l.href) }; });
    links.forEach(function (l) {
      var a = el("a", null, l.text);
      a.href = l.href;
      if (a.host !== location.host) { a.target = "_blank"; a.rel = "noopener"; }
      var item = el("li");
      item.appendChild(a);
      ul.appendChild(item);
    });
    left.appendChild(ul);
    box.appendChild(left);
    var right = el("div", "mega-right");
    right.appendChild(el("div", "mega-h", T(M.texts.featured)));
    var grid = el("div", "mega-cards");
    if (cfg.ratio) grid.style.setProperty("--mega-ratio", cfg.ratio);
    var nCards = Math.min(Array.isArray(cfg.cards) ? cfg.cards.length : cfg.cards.count || MAX, MAX);
    for (var k = 0; k < nCards; k++) grid.appendChild(el("div", "mega-card mega-skeleton"));
    right.appendChild(grid);
    box.appendChild(right);
    // cards fetched on an earlier visit (last 12 hours) show at once; a fresh copy is fetched in the background for next time
    var key = "mega2:" + lang + ":" + i, saved = null, live = !Array.isArray(cfg.cards) && !given(cfg.cards);
    try { saved = live && JSON.parse(localStorage.getItem(key) || "null"); } catch (e) {}
    if (saved && Date.now() - saved.t > 12 * 3600e3) saved = null;
    var recent = saved && Date.now() - saved.t < 3600e3;
    var fresh = recent ? null : live ? loadCards(cfg.cards).then(function (cards) { try { localStorage.setItem(key, JSON.stringify({ t: Date.now(), cards: cards })); } catch (e) {} return cards; }) : loadCards(cfg.cards);
    if (saved && fresh) fresh.catch(function () {});
    (saved ? Promise.resolve(saved.cards) : fresh).then(function (cards) {
      grid.innerHTML = "";
      if (!cards.length) { right.remove(); box.classList.add("mega-only-links"); return; }
      cards.forEach(function (c) { grid.appendChild(card(c)); });
    }).catch(function () { right.remove(); box.classList.add("mega-only-links"); });
    built[i] = box;
    return box;
  }

  function show(i, cfg, li) {
    clearTimeout(hideTimer);
    if (!desktop.matches) return;
    // a page that switches language in place: build the panels again in the new language
    var now = (document.documentElement.lang || "en").split("-")[0].toLowerCase();
    if (now !== lang) { lang = now; built = {}; }
    if (open === li) return;
    if (open) open.classList.remove("mega-open");
    open = li;
    li.classList.add("mega-open");
    panel.innerHTML = "";
    panel.appendChild(build(i, cfg, li));
    position();
    panel.hidden = false;
  }
  function hide(now) {
    clearTimeout(hideTimer);
    hideTimer = setTimeout(function () {
      panel.hidden = true;
      if (open) open.classList.remove("mega-open");
      open = null;
    }, now ? 0 : 160);
  }

  // which panel a top-level item opens; delegated, so copies of the menu made later (a sticky header) work too
  function panelOf(li) {
    if (li.dataset.mega !== undefined) return li.dataset.mega === "" ? -1 : +li.dataset.mega;
    var a = li.querySelector("a"), found = -1;
    if (a && !(M.exclude && li.matches(M.exclude))) {
      var text = a.textContent.trim().toLowerCase(), href = (a.getAttribute("href") || "").replace(/^https?:\/\/[^/]+/, "");
      M.panels.forEach(function (cfg, i) {
        if (found < 0 && [].concat(cfg.match).some(function (m) { m = String(m); return /^[\/#]/.test(m) ? href === m || href.replace(/^\/[a-z]{2,3}\//, "/") === m : text === m.toLowerCase(); })) found = i;
      });
    }
    li.dataset.mega = found < 0 ? "" : found;
    if (found >= 0) li.classList.add("mega-has");
    return found;
  }
  topItems.forEach(panelOf);

  // build the panels (and so fetch their cards and pictures) once the page has loaded, so the first hover is instant
  function prebuild() {
    if (!desktop.matches) return;
    var go = function () {
      topItems.forEach(function (li) { var i = panelOf(li); if (i >= 0 && !built[i]) build(i, M.panels[i], li); });
    };
    if (window.requestIdleCallback) requestIdleCallback(go, { timeout: 800 }); else setTimeout(go, 300);
  }
  prebuild();
  // the pointer heading for the menu: build now, without waiting for an idle moment
  header.addEventListener("pointerenter", function () { topItems.forEach(function (li) { var i = panelOf(li); if (i >= 0 && !built[i]) build(i, M.panels[i], li); }); }, { once: true });
  document.addEventListener("mouseover", function (e) {
    if (!desktop.matches) return;
    var li = e.target.closest && e.target.closest(M.items);
    var i = li ? panelOf(li) : -1;
    if (i >= 0) { show(i, M.panels[i], li); return; }
    if (open && !panel.contains(e.target) && !open.contains(e.target)) hide();
  });
  document.addEventListener("focusin", function (e) {
    var li = e.target.closest && e.target.closest(M.items);
    var i = li ? panelOf(li) : -1;
    if (i >= 0) show(i, M.panels[i], li);
  });
  document.addEventListener("pointerover", function (e) {
    var li = e.target.closest && e.target.closest(M.items);
    var i = li ? panelOf(li) : -1;
    if (i >= 0 && !Array.isArray(M.panels[i].cards)) loadCards(M.panels[i].cards).catch(function () {});
  }, { passive: true });
  panel.addEventListener("mouseenter", function () { clearTimeout(hideTimer); });
  panel.addEventListener("focusout", function (e) { if (!panel.contains(e.relatedTarget) && (!open || !open.contains(e.relatedTarget))) hide(true); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") hide(true); });
  window.addEventListener("scroll", function () { if (!panel.hidden) position(); }, { passive: true });
  window.addEventListener("resize", function () { if (!desktop.matches) hide(true); else if (!panel.hidden) position(); });
  document.documentElement.classList.add("mega-on");
})();
