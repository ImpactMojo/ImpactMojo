/* =============================================================================
   ImpactMojo — Fundamentals: The Results Chain
   Six Indian programmes drawn as small multiples of the same five-link chain,
   with each link's height set by how it is actually measured.
   Depends on /js/results-chain-data.js.

   The small multiples are the argument. One programme's staircase could be a
   quirk of that ministry; six identical staircases, all stepping down between
   the same two links, is a property of the way the chain is built.
   ============================================================================= */

window.FResultsChain = (function () {
  "use strict";
  var D = window.RESULTSCHAIN;
  var state = { programme: null, link: null };

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  /* Pick the ink that actually contrasts better against a fill, rather than
     testing luminance against a constant. rules/testing.md item 12 records a
     fixed cutoff putting white on #d97706 at 3.19:1; comparing the two
     candidate ratios is self-correcting for any colour added later. */
  function ink(hex) {
    function lum(h) {
      h = h.replace("#", "");
      var c = [0, 2, 4].map(function (i) {
        var v = parseInt(h.slice(i, i + 2), 16) / 255;
        return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
      });
      return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2];
    }
    function ratio(a, b) {
      var x = lum(a), y = lum(b), hi = Math.max(x, y), lo = Math.min(x, y);
      return (hi + 0.05) / (lo + 0.05);
    }
    return ratio("#1a1420", hex) > ratio("#ffffff", hex) ? "#1a1420" : "#ffffff";
  }

  function programmeById(id) {
    return D.programmes.filter(function (p) { return p.id === id; })[0];
  }

  /* ------------------------------------------------------------ the chain */
  /* Below this width the chain is drawn top to bottom instead of left to right.
     Five bars across a 343px phone leaves each about 55px, which is not enough
     for "Activities" to be legible: a 9.5px label inside a 560-unit viewBox
     scaled into a 337px column renders at 5.7 CSS px, and at 360px it is 5.2.
     The short bars were unusable as targets too -- an "absent" bar is 8% of the
     plot height, roughly 7px tall, well under the 24px minimum. Turning the
     chain vertical fixes both at once, and the argument survives the rotation:
     the step down the page reads the same as the step across it. */
  var NARROW_MAX = 640;

  function isNarrow() {
    return !!(window.matchMedia && window.matchMedia('(max-width:' + NARROW_MAX + 'px)').matches);
  }

  function svgOpen(p, w, h, interactive) {
    /* role="img" only on the static small multiples. The interactive copy holds
       focusable bars, and role="img" declares its content atomic, which axe
       reports as nested-interactive and a screen reader would honour by hiding
       the buttons. The interactive one is a group. */
    return '<svg viewBox="0 0 ' + w + ' ' + h + '" class="rc-svg" role="' +
           (interactive ? 'group' : 'img') + '" aria-label="' +
           esc(p.name + ': how each link of the results chain is measured') + '">';
  }

  function barAttrs(link, cell, st, p, interactive, isBreak) {
    var cls = 'rc-bar rc-bar--' + cell.state + (isBreak ? ' rc-bar--break' : '');
    return '<g class="' + cls + '" data-link="' + esc(link.id) + '"' +
           (interactive ? ' tabindex="0" role="button" aria-label="' +
             esc(link.name + ': ' + st.label) + '"' : '') + '>';
  }

  /* Wide: five bars side by side, height carrying the measurement weight. */
  function chartWide(p, interactive) {
    var W = 560, H = 128, PAD_B = 26, PAD_T = 8;
    var slot = W / D.links.length;
    var barW = slot - 14;
    var parts = [svgOpen(p, W, H, interactive)];

    D.links.forEach(function (link, i) {
      var cell = p.chain[link.id];
      var st = D.states[cell.state];
      var h = Math.round((H - PAD_B - PAD_T) * (st.weight / 100));
      var x = Math.round(i * slot + 7);
      var y = H - PAD_B - h;

      parts.push(barAttrs(link, cell, st, p, interactive, p.breaks === link.id));
      parts.push('<rect x="' + x + '" y="' + y + '" width="' + Math.round(barW) +
                 '" height="' + h + '" rx="4" fill="' + p.colour + '"' +
                 ' fill-opacity="' + (0.28 + 0.72 * st.weight / 100).toFixed(2) + '"/>');
      parts.push('<text class="rc-tick" x="' + Math.round(x + barW / 2) + '" y="' + (H - 9) +
                 '" text-anchor="middle">' + esc(link.name) + '</text>');
      parts.push('<title>' + esc(link.name + ' — ' + st.label) + '</title>');
      parts.push('</g>');

      // The step down, drawn between this bar and the next.
      if (i < D.links.length - 1) {
        var next = D.states[p.chain[D.links[i + 1].id].state];
        if (next.weight < st.weight - 20) {
          var mx = Math.round((i + 1) * slot);
          parts.push('<path class="rc-step" d="M' + mx + ',' + (PAD_T + 2) +
                     ' L' + mx + ',' + (H - PAD_B) + '"/>');
        }
      }
    });
    parts.push('</svg>');
    return parts.join('');
  }

  /* Narrow: five rows down the page, length carrying the same weight. The
     viewBox is close to the rendered pixel width, so a 12-unit label is a 12px
     label, and each row is a full-width target rather than a 7px sliver. */
  function chartNarrow(p, interactive) {
    var W = 340, LABEL_W = 86, ROW_H = 30, GAP = 7, PAD_T = 6, PAD_B = 6;
    var barX = LABEL_W + 8;
    var maxBar = W - barX - 8;
    var H = PAD_T + D.links.length * ROW_H + (D.links.length - 1) * GAP + PAD_B;
    var parts = [svgOpen(p, W, H, interactive)];

    D.links.forEach(function (link, i) {
      var cell = p.chain[link.id];
      var st = D.states[cell.state];
      var y = PAD_T + i * (ROW_H + GAP);
      var len = Math.max(6, Math.round(maxBar * (st.weight / 100)));

      parts.push(barAttrs(link, cell, st, p, interactive, p.breaks === link.id));
      // A transparent full-width hit area, so the row is tappable even where
      // the bar itself is short. Without it "Not measured" is a 6px target.
      parts.push('<rect class="rc-hit" x="0" y="' + y + '" width="' + W +
                 '" height="' + ROW_H + '" rx="6" fill="transparent"/>');
      parts.push('<text class="rc-rlabel" x="' + LABEL_W + '" y="' + (y + ROW_H / 2 + 4) +
                 '" text-anchor="end">' + esc(link.name) + '</text>');
      parts.push('<rect x="' + barX + '" y="' + (y + 5) + '" width="' + len +
                 '" height="' + (ROW_H - 10) + '" rx="4" fill="' + p.colour + '"' +
                 ' fill-opacity="' + (0.28 + 0.72 * st.weight / 100).toFixed(2) + '"/>');
      parts.push('<title>' + esc(link.name + ' — ' + st.label) + '</title>');
      parts.push('</g>');

      if (i < D.links.length - 1) {
        var next = D.states[p.chain[D.links[i + 1].id].state];
        if (next.weight < st.weight - 20) {
          var my = y + ROW_H + Math.round(GAP / 2);
          parts.push('<path class="rc-step" d="M' + barX + ',' + my + ' L' + (W - 8) + ',' + my + '"/>');
        }
      }
    });
    parts.push('</svg>');
    return parts.join('');
  }

  function chartFor(p, interactive) {
    return isNarrow() ? chartNarrow(p, interactive) : chartWide(p, interactive);
  }

  function drawSmallMultiples() {
    var box = document.getElementById("smallMultiples");
    if (!box) return;
    box.innerHTML = D.programmes.map(function (p) {
      return '<figure class="rc-sm">' +
             '<figcaption><b>' + esc(p.name) + "</b> <span>since " + esc(p.since) + "</span></figcaption>" +
             chartFor(p, false) +
             '<p class="rc-sm-break">Breaks after <b>' +
               esc(D.links.filter(function (l) {
                 var i = D.links.map(function (x) { return x.id; }).indexOf(p.breaks);
                 return l.id === D.links[Math.max(0, i - 1)].id;
               })[0].name.toLowerCase()) + "</b></p>" +
             "</figure>";
    }).join("");
  }

  /* ------------------------------------------------------------- the panel */
  function drawPicker() {
    var box = document.getElementById("rcPicker");
    if (!box) return;
    box.innerHTML = D.programmes.map(function (p) {
      return '<button type="button" class="chip" data-prog="' + esc(p.id) + '" aria-pressed="false">' +
             '<span class="sw" style="background:' + p.colour + '"></span>' + esc(p.name) + "</button>";
    }).join("");
    box.addEventListener("click", function (e) {
      var btn = e.target.closest("button[data-prog]");
      if (btn) select(btn.getAttribute("data-prog"), null);
    });
  }

  function select(progId, linkId) {
    state.programme = progId;
    state.link = linkId || "outputs";
    var p = programmeById(progId);
    if (!p) return;

    document.querySelectorAll("#rcPicker .chip").forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.getAttribute("data-prog") === progId));
    });

    var chart = document.getElementById("rcChart");
    if (chart) {
      chart.innerHTML = chartFor(p, true);
      chart.querySelectorAll("[data-link]").forEach(function (g) {
        function go() { select(progId, g.getAttribute("data-link")); }
        g.addEventListener("click", go);
        g.addEventListener("keydown", function (e) {
          if (e.key === "Enter" || e.key === " ") { e.preventDefault(); go(); }
        });
      });
      chart.querySelectorAll("[data-link]").forEach(function (g) {
        g.classList.toggle("is-on", g.getAttribute("data-link") === state.link);
      });
    }
    renderPanel(p);
  }

  function renderPanel(p) {
    var box = document.getElementById("rcPanel");
    if (!box) return;
    var link = D.links.filter(function (l) { return l.id === state.link; })[0];
    var cell = p.chain[link.id];
    var st = D.states[cell.state];

    box.innerHTML =
      '<span class="rc-eyebrow" style="background:' + p.colour + ';color:' + ink(p.colour) + '">' +
        esc(p.name) + "</span>" +
      "<h3>" + esc(link.name) + "</h3>" +
      '<p class="rc-gloss">' + esc(link.gloss) + " <b>" + esc(link.question) + "</b></p>" +
      '<p class="rc-state rc-state--' + cell.state + '"><b>' + esc(st.label) + ".</b> " + esc(st.note) + "</p>" +
      "<p>" + esc(cell.detail) + "</p>" +
      '<p class="rc-src">' + esc(cell.instrument) + " &middot; " + esc(cell.source) +
        " &middot; " + esc(cell.year) + "</p>" +
      (p.breaks === link.id
        ? '<div class="rc-break"><h4>This is where the chain breaks</h4><p>' +
          esc(p.breakNote) + "</p></div>"
        : "") +
      '<p class="rc-what">' + esc(p.what) + "</p>";
  }

  function drawLegend() {
    var box = document.getElementById("rcLegend");
    if (!box) return;
    box.innerHTML = Object.keys(D.states).map(function (k) {
      var s = D.states[k];
      return '<li><span class="rc-key rc-key--' + k + '"></span><b>' + esc(s.label) + "</b> " +
             esc(s.note) + "</li>";
    }).join("");
  }

  function init() {
    if (!D) return;
    drawSmallMultiples();
    drawLegend();
    drawPicker();
    select(D.programmes[0].id, "outputs");

    // Redraw when the viewport crosses the breakpoint -- rotating a phone, or
    // dragging a desktop window narrow. Debounced, and only when the
    // orientation actually changed, so a scroll-driven resize on mobile
    // browsers (the address bar collapsing) does not rebuild the SVGs.
    var wasNarrow = isNarrow(), t = null;
    window.addEventListener("resize", function () {
      clearTimeout(t);
      t = setTimeout(function () {
        var now = isNarrow();
        if (now === wasNarrow) return;
        wasNarrow = now;
        drawSmallMultiples();
        select(state.programme, state.link);
      }, 150);
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();

  return { select: select };
})();
