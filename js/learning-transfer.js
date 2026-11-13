/* =============================================================================
   ImpactMojo - Fundamentals: Wheel of Learning Transfer
   Renders ten factors x three rings as SVG, with keyboard and deep-link
   support, an optional "rate my programme" mode, and a text list of the same
   data. Depends on /js/learning-transfer-data.js (window.LTRANSFER).
   ============================================================================= */

window.FTransfer = (function () {
  "use strict";

  var D = window.LTRANSFER;
  var NS = "http://www.w3.org/2000/svg";
  var CX = 380, CY = 380;
  var R = { hub: 70, r1: 160, r2: 245, r3: 320, label: 336 };
  var RING_R = { stick: [R.hub, R.r1], risk: [R.r1, R.r2], drop: [R.r2, R.r3] };
  var N = D.factors.length, SPAN = 360 / N;
  var KEY = "im-learning-transfer-ratings";

  var state = { factor: null, ring: null, rating: false, marks: {} };

  /* ------------------------------------------------------------- colours */
  function rgb(h) { h = h.replace("#", ""); return [0, 2, 4].map(function (i) { return parseInt(h.slice(i, i + 2), 16); }); }
  function hex(c) {
    return "#" + c.map(function (v) { var s = Math.max(0, Math.min(255, Math.round(v))).toString(16); return s.length === 1 ? "0" + s : s; }).join("");
  }
  function mix(a, b, t) { var x = rgb(a), y = rgb(b); return hex([0, 1, 2].map(function (i) { return x[i] + (y[i] - x[i]) * t; })); }
  function ringFill(base, ring) {
    if (ring === "stick") return mix(base, "#000000", 0.30);
    if (ring === "risk") return base;
    return mix(base, "#ffffff", 0.42);
  }
  /* Compare the two candidate inks instead of using a luminance cutoff. */
  function lum(h) {
    var c = rgb(h).map(function (v) { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); });
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2];
  }
  function ratio(a, b) { var x = lum(a), y = lum(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); }
  function ink(h) { return ratio("#1a1420", h) > ratio("#ffffff", h) ? "#1a1420" : "#ffffff"; }

  /* ------------------------------------------------------------ geometry */
  function pt(r, deg) { var a = (deg - 90) * Math.PI / 180; return [CX + r * Math.cos(a), CY + r * Math.sin(a)]; }
  function annulus(a0, a1, rIn, rOut) {
    var p1 = pt(rOut, a0), p2 = pt(rOut, a1), p3 = pt(rIn, a1), p4 = pt(rIn, a0);
    return ["M", p1[0].toFixed(2), p1[1].toFixed(2), "A", rOut, rOut, 0, 0, 1, p2[0].toFixed(2), p2[1].toFixed(2),
            "L", p3[0].toFixed(2), p3[1].toFixed(2), "A", rIn, rIn, 0, 0, 0, p4[0].toFixed(2), p4[1].toFixed(2), "Z"].join(" ");
  }
  function textArc(a0, a1, r) {
    var mid = (a0 + a1) / 2, flip = mid > 90 && mid < 270;
    var s = flip ? a1 : a0, e = flip ? a0 : a1, rr = flip ? r + 6 : r;
    var p1 = pt(rr, s), p2 = pt(rr, e);
    return ["M", p1[0].toFixed(2), p1[1].toFixed(2), "A", rr, rr, 0, 0, flip ? 0 : 1, p2[0].toFixed(2), p2[1].toFixed(2)].join(" ");
  }
  function el(name, attrs, text) {
    var n = document.createElementNS(NS, name);
    for (var k in attrs) if (Object.prototype.hasOwnProperty.call(attrs, k)) n.setAttribute(k, attrs[k]);
    if (text != null) n.textContent = text;
    return n;
  }
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; });
  }
  function fac(id) { return D.factors.filter(function (f) { return f.id === id; })[0]; }

  /* ------------------------------------------------------------- storage */
  function load() { try { state.marks = JSON.parse(localStorage.getItem(KEY) || "{}") || {}; } catch (e) { state.marks = {}; } }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(state.marks)); } catch (e) { /* private window */ } }

  /* --------------------------------------------------------------- wheel */
  function buildWheel() {
    var svg = document.getElementById("wheel");
    if (!svg) return;
    svg.setAttribute("viewBox", "0 0 760 760");
    svg.setAttribute("role", "group");
    svg.setAttribute("aria-label", "Interactive wheel of ten learning transfer factors, each with three rings. The centre ring is likely to stick, the middle ring is at risk, and the outer ring is unlikely to stick. Select a ring to read it.");
    var defs = el("defs", {}); svg.appendChild(defs);

    D.factors.forEach(function (f, i) {
      var a0 = i * SPAN, a1 = a0 + SPAN, g = el("g", { "data-factor": f.id });
      D.RING_ORDER.forEach(function (ring) {
        var rr = RING_R[ring];
        var fill_ = ringFill(f.color, ring);
        var path = el("path", {
          d: annulus(a0 + 0.35, a1 - 0.35, rr[0], rr[1]), fill: fill_, "class": "seg",
          role: "button", tabindex: "0", "data-factor": f.id, "data-ring": ring, "aria-pressed": "false",
          "aria-label": f.name + ", " + D.RINGS[ring].label
        });
        path.addEventListener("click", function () { select(f.id, ring); });
        path.addEventListener("keydown", function (e) {
          if (e.key === "Enter" || e.key === " ") { e.preventDefault(); select(f.id, ring); }
          else if (e.key === "ArrowRight" || e.key === "ArrowLeft") { e.preventDefault(); stepFactor(e.key === "ArrowRight" ? 1 : -1, ring); }
          else if (e.key === "ArrowUp" || e.key === "ArrowDown") { e.preventDefault(); stepRing(e.key === "ArrowUp" ? -1 : 1, f.id); }
        });
        g.appendChild(path);
        /* short label inside the ring, set along the spoke */
        var th = (a0 + a1) / 2, c0 = pt((rr[0] + rr[1]) / 2, th);
        var ang = th - 90 + (th > 180 ? 180 : 0);
        var tg = el("text", { "class": "seg-tag", "aria-hidden": "true", transform: "translate(" + c0[0].toFixed(1) + " " + c0[1].toFixed(1) + ") rotate(" + ang.toFixed(1) + ")", fill: ink(fill_) });
        var lines = f.tags[ring].split("|");
        lines.forEach(function (ln, k) { tg.appendChild(el("tspan", { x: 0, y: ((k - (lines.length - 1) / 2) * 12.5 + 4).toFixed(1), "text-anchor": "middle" }, ln)); });
        g.appendChild(tg);
        /* a dot marks the ring chosen in rating mode */
        var mid = pt((rr[0] + rr[1]) / 2, (a0 + a1) / 2);
        g.appendChild(el("circle", { cx: mid[0].toFixed(1), cy: mid[1].toFixed(1), r: 9, "class": "mark-dot", "data-mark": f.id + ":" + ring, "aria-hidden": "true" }));
      });
      svg.appendChild(g);

      var id = "ltarc-" + i;
      defs.appendChild(el("path", { id: id, d: textArc(a0 + 2, a1 - 2, R.label) }));
      var t = el("text", { "class": "lt-label", "aria-hidden": "true" });
      var tp = el("textPath", { href: "#" + id, startOffset: "50%", "text-anchor": "middle" }, f.name);
      t.appendChild(tp); svg.appendChild(t);
      var np = pt(350, (a0 + a1) / 2);
      svg.appendChild(el("text", { x: np[0].toFixed(1), y: np[1].toFixed(1), "class": "lt-num", "aria-hidden": "true" }, String(i + 1)));
    });

    svg.appendChild(el("circle", { cx: CX, cy: CY, r: R.hub, "class": "hub" }));
    var ht = el("text", { x: CX, y: CY - 10, "text-anchor": "middle", "class": "hub-text" });
    ["Closer to", "the centre,", "more likely", "to stick"].forEach(function (line, k) {
      ht.appendChild(el("tspan", { x: CX, dy: k === 0 ? 0 : 15 }, line));
    });
    svg.appendChild(ht);
  }

  function stepFactor(d, ring) {
    var i = D.factors.map(function (f) { return f.id; }).indexOf(state.factor || D.factors[0].id);
    var f = D.factors[(i + d + N) % N];
    focusSeg(f.id, ring);
  }
  function stepRing(d, fid) {
    var i = D.RING_ORDER.indexOf(state.ring || "stick");
    focusSeg(fid, D.RING_ORDER[Math.max(0, Math.min(2, i + d))]);
  }
  function focusSeg(fid, ring) {
    var s = document.querySelector('#wheel .seg[data-factor="' + fid + '"][data-ring="' + ring + '"]');
    if (s) { select(fid, ring); s.focus(); }
  }

  /* -------------------------------------------------------------- select */
  function select(fid, ring, opts) {
    opts = opts || {};
    var f = fac(fid); if (!f) return;
    state.factor = fid; state.ring = ring || "stick";
    paint();
    renderPanel(f);
    if (!opts.silent) history.replaceState(null, "", "#" + fid + (ring ? "/" + ring : ""));
  }

  function paint() {
    document.querySelectorAll("#wheel .seg").forEach(function (s) {
      var on = s.getAttribute("data-factor") === state.factor;
      s.setAttribute("aria-pressed", String(on && s.getAttribute("data-ring") === state.ring));
    });
    document.querySelectorAll("#wheel .mark-dot").forEach(function (d) {
      var p = d.getAttribute("data-mark").split(":");
      d.classList.toggle("on", state.rating && state.marks[p[0]] === p[1]);
    });
    document.querySelectorAll("#factorLegend .fl-btn").forEach(function (b) { b.setAttribute("aria-pressed", String(b.getAttribute("data-factor") === state.factor)); });
    document.getElementById("wheelFrame").classList.toggle("is-rating", state.rating);
    setCaption();
  }

  function setCaption() {
    var box = document.getElementById("factorCaption"); if (!box) return;
    if (!state.factor) { box.className = "wheel-caption is-empty"; box.innerHTML = '<span class="cap-t">Nothing selected yet. Pick a ring on the wheel.</span>'; return; }
    var f = fac(state.factor);
    box.className = "wheel-caption";
    box.innerHTML = '<span class="cap-sw" style="background:' + esc(f.color) + '"></span><span><span class="cap-s">' +
      esc(D.BANDS[f.band].label) + ' &middot; ' + esc(D.RINGS[state.ring].label) + '</span><span class="cap-t">' + esc(f.name) + '</span></span>';
  }

  /* --------------------------------------------------------------- panel */
  function renderPanel(f) {
    var h = [];
    h.push('<div class="panel-axis"><span class="swatch" style="background:' + esc(f.color) + '"></span>' + esc(D.BANDS[f.band].label) + '</div>');
    h.push('<h3>' + esc(f.name) + '</h3>');
    h.push('<p class="axis-q">' + esc(f.asks) + '</p>');
    h.push('<div class="lt-levels" role="group" aria-label="The three positions for ' + esc(f.name) + '">');
    D.RING_ORDER.forEach(function (ring) {
      var picked = state.marks[f.id] === ring;
      h.push('<div class="lt-level lt-' + ring + (state.ring === ring ? " is-current" : "") + '">' +
        '<span class="lt-badge lt-badge-' + ring + '">' + esc(D.RINGS[ring].label) + '</span>' +
        '<p>' + esc(f.levels[ring]) + '</p>' +
        (state.rating ? '<button type="button" class="btn-ghost lt-pick" data-pick="' + ring + '" aria-pressed="' + picked + '">' + (picked ? "This is us (chosen)" : "This is us") + '</button>' : '') +
        '</div>');
    });
    h.push('</div>');
    h.push('<ul class="ev-list">');
    f.research.forEach(function (r) {
      h.push('<li class="ev"><div class="fig">' + esc(r.year) + '</div><div class="txt">' + esc(r.detail) + '<span class="src">' + esc(r.ref) + ', ' + esc(r.year) + '</span></div></li>');
    });
    h.push('</ul>');
    h.push('<p class="who"><b>What to do:</b> ' + esc(f.do) + '</p>');
    h.push('<p class="who"><b>Ask in your own programme:</b> ' + esc(f.ask) + '</p>');
    h.push('<div class="caveat"><b>Limits of this factor</b><p>' + esc(f.limits) + '</p></div>');
    h.push('<div class="panel-nav"><button class="btn-ghost" data-nav="prev">&larr; Previous factor</button>' +
           '<button class="btn-ghost" data-nav="next">Next factor &rarr;</button><button class="btn-ghost" data-nav="clear">Clear</button></div>');
    var p = document.getElementById("panel");
    p.innerHTML = h.join("");
    p.querySelectorAll("[data-nav]").forEach(function (b) {
      b.addEventListener("click", function () {
        var dir = b.getAttribute("data-nav");
        if (dir === "clear") { state.factor = null; state.ring = null; paint(); renderEmpty(); history.replaceState(null, "", location.pathname); return; }
        stepFactor(dir === "next" ? 1 : -1, state.ring || "stick");
      });
    });
    p.querySelectorAll("[data-pick]").forEach(function (b) {
      b.addEventListener("click", function () {
        var ring = b.getAttribute("data-pick");
        if (state.marks[f.id] === ring) delete state.marks[f.id]; else state.marks[f.id] = ring;
        save(); state.ring = ring; paint(); renderPanel(f); renderSummary();
        var again = document.querySelector('#panel [data-pick="' + ring + '"]'); if (again) again.focus();
      });
    });
  }

  function renderEmpty() {
    document.getElementById("panel").innerHTML =
      '<div class="panel-empty"><h3>Pick a ring</h3><p>Ten factors decide whether a trainee changes how they work. Each has three positions, and the closer a position sits to the centre, the more likely the learning is to stick.</p>' +
      '<ol><li>Select any ring to read what it looks like, the research behind the factor, and what to do about it.</li>' +
      '<li>Turn on <b>Rate my programme</b> to say which ring describes your own training for each factor.</li>' +
      '<li>Arrow keys move around the wheel: left and right between factors, up and down between rings.</li></ol></div>';
  }

  /* ------------------------------------------------------- rating summary */
  function renderSummary() {
    var box = document.getElementById("summary"); if (!box) return;
    var rated = D.factors.filter(function (f) { return state.marks[f.id]; });
    if (!state.rating) { box.hidden = true; return; }
    box.hidden = false;
    if (!rated.length) {
      box.innerHTML = '<h3>Your reading</h3><p class="muted">Choose a ring for each factor in the panel. Your answers stay in this browser.</p>';
      return;
    }
    var by = { drop: [], risk: [], stick: [] };
    rated.forEach(function (f) { by[state.marks[f.id]].push(f); });
    var score = rated.reduce(function (a, f) { return a + D.RINGS[state.marks[f.id]].score; }, 0);
    var h = ['<h3>Your reading</h3>',
      '<p>' + rated.length + ' of ' + N + ' factors rated. ' + score + ' of ' + (rated.length * 2) + ' possible points. This is a prompt for a team conversation and has not been validated as a measure.</p>'];
    [["drop", "Unlikely to stick: start here"], ["risk", "At risk"], ["stick", "Likely to stick"]].forEach(function (g) {
      if (!by[g[0]].length) return;
      h.push('<div class="sum-group"><span class="lt-badge lt-badge-' + g[0] + '">' + esc(g[1]) + '</span><ul>' +
        by[g[0]].map(function (f) { return '<li><button type="button" class="linklike" data-jump="' + esc(f.id) + '">' + esc(f.name) + '</button>' + (g[0] !== "stick" ? ' &middot; ' + esc(f.do) : '') + '</li>'; }).join("") + '</ul></div>');
    });
    var unrated = N - rated.length;
    if (unrated) h.push('<p class="muted">' + unrated + ' factor' + (unrated === 1 ? "" : "s") + ' not yet rated.</p>');
    h.push('<div class="panel-nav"><button class="btn-ghost" id="copySummary">Copy as text</button><button class="btn-ghost" id="resetRatings">Clear my ratings</button></div>');
    box.innerHTML = h.join("");
    box.querySelectorAll("[data-jump]").forEach(function (b) {
      b.addEventListener("click", function () { select(b.getAttribute("data-jump"), state.marks[b.getAttribute("data-jump")]); document.getElementById("wheel").scrollIntoView({ block: "center", behavior: "smooth" }); });
    });
    document.getElementById("resetRatings").addEventListener("click", function () { state.marks = {}; save(); paint(); if (state.factor) renderPanel(fac(state.factor)); renderSummary(); });
    document.getElementById("copySummary").addEventListener("click", function () {
      var lines = ["Learning transfer reading (ImpactMojo, impactmojo.in/fundamentals/learning-transfer.html)"];
      D.RING_ORDER.slice().reverse().forEach(function (r) {
        by[r].forEach(function (f) { lines.push(D.RINGS[r].label + ": " + f.name); });
      });
      var done = function () { var b = document.getElementById("copySummary"); b.textContent = "Copied"; };
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(lines.join("\n")).then(done, function () {});
    });
  }

  /* ----------------------------------------------------------- text list */
  function buildList() {
    var box = document.getElementById("textList"); if (!box) return;
    box.innerHTML = D.factors.map(function (f) {
      return '<section class="tl-item"><h4><span class="swatch" style="background:' + esc(f.color) + '"></span>' + esc(f.name) + ' <small>' + esc(D.BANDS[f.band].label) + '</small></h4><p>' + esc(f.asks) + '</p><dl>' +
        D.RING_ORDER.map(function (r) { return '<dt>' + esc(D.RINGS[r].label) + '</dt><dd>' + esc(f.levels[r]) + '</dd>'; }).join("") + '</dl></section>';
    }).join("");
  }

  function buildLegend() {
    var ol = document.getElementById("factorLegend"); if (!ol) return;
    ol.innerHTML = D.factors.map(function (f, i) {
      return '<li><button type="button" class="fl-btn" data-factor="' + esc(f.id) + '" aria-pressed="false">' +
        '<span class="fl-num" style="background:' + esc(f.color) + ';color:' + ink(f.color) + '">' + (i + 1) + '</span>' + esc(f.name) + '</button></li>';
    }).join("");
    ol.querySelectorAll(".fl-btn").forEach(function (b) {
      b.addEventListener("click", function () {
        select(b.getAttribute("data-factor"), state.marks[b.getAttribute("data-factor")] || "stick");
        var p = document.getElementById("panel"); if (p && p.scrollIntoView) p.scrollIntoView({ block: "start", behavior: "smooth" });
      });
    });
  }

  function buildSources() {
    var ul = document.getElementById("sourceList"); if (!ul) return;
    ul.innerHTML = D.SOURCES.map(function (s) { return "<li>" + esc(s) + "</li>"; }).join("");
  }

  /* ---------------------------------------------------------------- hash */
  function fromHash() {
    var p = (location.hash || "").replace("#", "").split("/");
    if (p[0] && fac(p[0])) { select(p[0], D.RINGS[p[1]] ? p[1] : "stick", { silent: true }); return true; }
    return false;
  }

  function init() {
    if (!D || !D.factors) return;
    load(); buildWheel(); buildLegend(); buildList(); buildSources();
    var tog = document.getElementById("rateToggle");
    if (tog) tog.addEventListener("change", function () {
      state.rating = tog.checked; paint(); renderSummary();
      if (state.factor) renderPanel(fac(state.factor));
    });
    if (!fromHash()) { renderEmpty(); paint(); }
    renderSummary();
    window.addEventListener("hashchange", fromHash);
  }

  return { init: init, select: select };
})();
