/* Field Talkies — video explainers for ImpactMojo.
   Plays films from /data/field-talkies.json (one after another), with track
   filtering, deep links (#film-id) and a transcript panel. Handles both 16:9
   films and vertical shorts. No external dependencies. */
(function () {
  "use strict";

  var TRACK_COLORS = {
    "MEL & Research": "#3182ce",
    "Data & Technology": "#38a169",
    "Policy & Economics": "#d69e2e",
    "Gender & Equity": "#d53f8c",
    "Health & Communication": "#e53e3e",
    "Philosophy & Governance": "#805ad5"
  };

  var els = {}, films = [], all = [], idx = 0, video = null;

  function $(id) { return document.getElementById(id); }
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) {
    return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function color(t) { return TRACK_COLORS[t] || "#0EA5E9"; }

  function boot() {
    ["screen", "now-title", "now-meta", "prev", "next", "count", "transcript", "transcript-body", "filters", "list", "total"]
      .forEach(function (k) { els[k] = $("ft-" + k); });
    els.prev.addEventListener("click", function () { load(idx - 1, true); });
    els.next.addEventListener("click", function () { load(idx + 1, true); });

    fetch("/data/field-talkies.json", { cache: "no-cache" })
      .then(function (r) { return r.json(); })
      .then(function (data) {
        var c = (data && data.cinema) || {};
        if (c.name) $("ft-name").textContent = c.name;
        if (c.tagline) $("ft-tagline").textContent = c.tagline;
        all = (data && Array.isArray(data.films)) ? data.films : [];
        var want = (location.hash || "").replace(/^#/, "");   // read before the first load rewrites it
        renderFilters();
        applyFilter("all");
        fromHash(want);
        window.addEventListener("hashchange", fromHash);
      })
      .catch(function () {
        els.screen.innerHTML = '<p class="fr-empty" style="color:#96A3B8">Field Talkies is setting up. Check back shortly.</p>';
      });
  }

  function renderFilters() {
    var tracks = [];
    all.forEach(function (f) { if (f.track && tracks.indexOf(f.track) < 0) tracks.push(f.track); });
    var html = '<button class="fr-chip is-on" data-track="all" type="button">All films</button>';
    tracks.forEach(function (t) {
      html += '<button class="fr-chip" data-track="' + esc(t) + '" style="--chip:' + color(t) + '" type="button">' + esc(t) + "</button>";
    });
    els.filters.innerHTML = html;
    els.filters.querySelectorAll(".fr-chip").forEach(function (b) {
      b.addEventListener("click", function () { applyFilter(b.getAttribute("data-track")); });
    });
  }

  function applyFilter(track) {
    els.filters.querySelectorAll(".fr-chip").forEach(function (b) {
      b.classList.toggle("is-on", b.getAttribute("data-track") === track);
    });
    films = track === "all" ? all.slice() : all.filter(function (f) { return f.track === track; });
    els.total.textContent = films.length + (films.length === 1 ? " film" : " films");
    renderList();
    if (films.length) { load(0, false); }
    else { stop(); els.screen.innerHTML = '<p class="fr-empty" style="color:#96A3B8">No films on this track yet.</p>'; }
  }

  function renderList() {
    var html = "";
    films.forEach(function (f, i) {
      html += '<button class="fr-item" data-i="' + i + '" type="button">' +
        '<span class="fr-item-ic" style="--tc:' + color(f.track) + '">&#9654;</span>' +
        '<span class="fr-item-b">' +
          '<span class="fr-item-t">' + esc(f.title || "Untitled") + "</span>" +
          '<span class="fr-item-m">' + esc(f.speaker || "") + (f.track ? " &middot; " + esc(f.track) : "") +
            (f.narration ? ' &middot; <span class="ft-badge">Narrated</span>' : "") + "</span>" +
        "</span>" +
        '<span class="fr-item-d">' + esc(f.duration || "") + "</span>" +
      "</button>";
    });
    els.list.innerHTML = html;
    els.list.querySelectorAll(".fr-item").forEach(function (b) {
      b.addEventListener("click", function () { load(parseInt(b.getAttribute("data-i"), 10), true); });
    });
  }

  function stop() {
    if (video) {
      try { video.pause(); } catch (e) {}
      video.removeEventListener("error", onError);
      video.removeAttribute("src");
      video = null;
    }
  }

  function load(i, autoplay) {
    if (!films.length) return;
    stop();
    idx = ((i % films.length) + films.length) % films.length;
    var f = films[idx], col = color(f.track);

    els["now-title"].textContent = f.title || "Untitled";
    els["now-meta"].innerHTML = (f.speaker ? "<b>" + esc(f.speaker) + "</b>" : "") +
      (f.role ? " &middot; " + esc(f.role) : "") +
      (f.track ? ' &middot; <span class="fr-track-dot" style="background:' + col + '"></span>' + esc(f.track) : "") +
      (f.duration ? " &middot; " + esc(f.duration) : "") +
      (f.narration ? ' &middot; <span class="ft-badge">Narrated</span>' : "");
    els.count.textContent = (idx + 1) + " / " + films.length;

    var tr = f.transcript ? "<p>" + esc(f.transcript).replace(/\n+/g, "</p><p>") + "</p>"
                          : '<p class="fr-no-tr">No transcript for this film yet.</p>';
    if (Array.isArray(f.sources) && f.sources.length) {
      tr += "<h3>Sources</h3><ul>" + f.sources.map(function (s) { return "<li>" + esc(s) + "</li>"; }).join("") + "</ul>";
    }
    els["transcript-body"].innerHTML = tr;

    els.screen.className = "ft-screen";
    els.screen.innerHTML =
      '<video id="ft-video" controls playsinline preload="metadata" ' +
        (f.poster ? 'poster="' + esc(f.poster) + '" ' : "") + 'src="' + esc(f.src) + '"></video>' +
      '<div class="ft-err" hidden>This film is on its way. Please try another from the programme.</div>';
    video = $("ft-video");
    video.addEventListener("loadedmetadata", function () {
      if (video && video.videoHeight > video.videoWidth) els.screen.classList.add("is-tall");
    });
    video.addEventListener("ended", function () { load(idx + 1, true); });
    video.addEventListener("error", onError);

    els.list.querySelectorAll(".fr-item").forEach(function (b, k) { b.classList.toggle("is-playing", k === idx); });
    document.documentElement.style.setProperty("--fr-accent", col);
    if (f.id && history.replaceState) { try { history.replaceState(null, "", "#" + f.id); } catch (e) {} }

    if (autoplay) { var p = video.play(); if (p && p.catch) p.catch(function () {}); }
  }

  function onError(e) {
    if (e && e.target !== video) return;
    var box = els.screen.querySelector(".ft-err");
    if (box) box.hidden = false;
  }

  function fromHash(given) {
    var id = typeof given === "string" ? given : (location.hash || "").replace(/^#/, "");
    if (!id) return;
    for (var i = 0; i < films.length; i++) { if (films[i].id === id) { if (i !== idx) load(i, false); return; } }
  }

  if (document.readyState === "loading") { document.addEventListener("DOMContentLoaded", boot); } else { boot(); }
})();
