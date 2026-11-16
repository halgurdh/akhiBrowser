/* Fly3D: page sections tilt in from below and recede on their way out, like a landing page flying past in 3D.
   <script src="fly3d.js" data-targets="main > section" defer></script>  (defaults to [data-fly3d]) */
(function () {
  var script = document.currentScript;
  var selector = (script && script.dataset.targets) || "[data-fly3d]";
  if (!window.requestAnimationFrame || !window.IntersectionObserver) return;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)");

  function ease(t) { return 1 - Math.pow(1 - t, 3); }
  function clamp(v) { return v < 0 ? 0 : v > 1 ? 1 : v; }

  function start() {
    var els = Array.prototype.slice.call(document.querySelectorAll(selector));
    if (!els.length) return;
    var live = new Set();
    var queued = false;

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) live.add(e.target);
        else { live.delete(e.target); }
      });
      queue();
    }, { rootMargin: "25% 0px 25% 0px" });

    function reset(el) {
      el.style.transform = "";
      el.style.opacity = "";
      el.style.transformOrigin = "";
      el.style.willChange = "";
    }

    function paint() {
      queued = false;
      if (reduce.matches) { els.forEach(reset); return; }
      var vh = window.innerHeight;
      var small = window.innerWidth < 720;
      var tilt = small ? 16 : 26;
      var depth = small ? 120 : 240;
      live.forEach(function (el) {
        var r = el.getBoundingClientRect();
        var enter = ease(clamp((r.top - vh * 0.55) / (vh * 0.45)));
        var exit = ease(clamp((vh * 0.3 - r.bottom) / (vh * 0.3)));
        if (enter === 0 && exit === 0) {
          if (el.style.transform) reset(el);
          return;
        }
        el.style.willChange = "transform, opacity";
        if (enter > 0) {
          el.style.transformOrigin = "50% 0%";
          el.style.transform = "perspective(1400px) translate3d(0," + (enter * 70).toFixed(1) + "px," + (-enter * depth).toFixed(1) + "px) rotateX(" + (enter * tilt).toFixed(2) + "deg)";
          el.style.opacity = (1 - enter * 0.65).toFixed(3);
        } else {
          el.style.transformOrigin = "50% 100%";
          el.style.transform = "perspective(1400px) translate3d(0,0," + (-exit * depth * 1.2).toFixed(1) + "px) rotateX(" + (-exit * tilt * 0.85).toFixed(2) + "deg)";
          el.style.opacity = (1 - exit * 0.75).toFixed(3);
        }
      });
    }

    function queue() {
      if (!queued) { queued = true; requestAnimationFrame(paint); }
    }

    els.forEach(function (el) { io.observe(el); });
    window.addEventListener("scroll", queue, { passive: true });
    window.addEventListener("resize", queue);
    if (reduce.addEventListener) reduce.addEventListener("change", queue);
    queue();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start);
  else start();
})();
