/* =============================================================================
   ImpactMojo — Theories of Development: catalogue filtering.

   Everything is already in the HTML: each card carries data-tradition,
   data-era, data-topics and a lower-cased data-search blob. This file only
   hides and shows, so the catalogue is complete and readable with JavaScript
   off, and a search engine sees every card.

   Filters within a group are OR (two traditions means either), and across
   groups they are AND. That is the combination people expect and almost nobody
   states, so it is stated here.
   ============================================================================= */

(function () {
  "use strict";

  function init() {
    var grid = document.getElementById("thGrid");
    if (!grid) return;

    var cards = Array.prototype.slice.call(grid.querySelectorAll(".th-card"));
    var buttons = Array.prototype.slice.call(document.querySelectorAll(".fbtn[data-filter]"));
    var search = document.getElementById("thSearch");
    var count = document.getElementById("thCount");
    var empty = document.getElementById("thEmpty");
    var active = { tradition: [], topics: [], era: [] };

    function matches(card) {
      var q = (search.value || "").trim().toLowerCase();
      if (q && card.getAttribute("data-search").indexOf(q) === -1) return false;
      if (active.tradition.length && active.tradition.indexOf(card.getAttribute("data-tradition")) === -1) return false;
      if (active.era.length && active.era.indexOf(card.getAttribute("data-era")) === -1) return false;
      if (active.topics.length) {
        var topics = card.getAttribute("data-topics").split("|");
        var hit = active.topics.some(function (t) { return topics.indexOf(t) !== -1; });
        if (!hit) return false;
      }
      return true;
    }

    function apply() {
      var shown = 0;
      cards.forEach(function (card) {
        var ok = matches(card);
        card.hidden = !ok;
        if (ok) shown += 1;
      });
      var filtering = shown !== cards.length;
      count.textContent = filtering
        ? shown + " of " + cards.length + " theories"
        : cards.length + " theories, oldest first";
      empty.hidden = shown !== 0;
      // Keep the state in the URL so a filtered view can be sent to someone.
      var params = new URLSearchParams();
      ["tradition", "topics", "era"].forEach(function (k) {
        if (active[k].length) params.set(k, active[k].join("|"));
      });
      if (search.value.trim()) params.set("q", search.value.trim());
      var qs = params.toString();
      history.replaceState(null, "", qs ? "?" + qs : location.pathname);
    }

    buttons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var key = btn.getAttribute("data-filter");
        var value = btn.getAttribute("data-value");
        var i = active[key].indexOf(value);
        if (i === -1) active[key].push(value); else active[key].splice(i, 1);
        btn.classList.toggle("active", i === -1);
        apply();
      });
    });

    search.addEventListener("input", apply);

    function reset() {
      active = { tradition: [], topics: [], era: [] };
      buttons.forEach(function (b) { b.classList.remove("active"); });
      search.value = "";
      apply();
    }
    ["thReset", "thResetInline"].forEach(function (id) {
      var b = document.getElementById(id);
      if (b) b.addEventListener("click", reset);
    });

    // Restore a shared view.
    var params = new URLSearchParams(location.search);
    ["tradition", "topics", "era"].forEach(function (k) {
      var raw = params.get(k);
      if (!raw) return;
      active[k] = raw.split("|");
      buttons.forEach(function (b) {
        if (b.getAttribute("data-filter") === k && active[k].indexOf(b.getAttribute("data-value")) !== -1) {
          b.classList.add("active");
        }
      });
    });
    if (params.get("q")) search.value = params.get("q");

    apply();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
