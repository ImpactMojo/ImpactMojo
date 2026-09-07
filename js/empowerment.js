/* =============================================================================
   ImpactMojo — Fundamentals: Resources, Agency, Achievements
   Four Indian series, each drawn beside the companion series that changes how
   it reads. Depends on /js/empowerment-data.js.

   The pairing is the page. A single line going the right way is what a report
   quotes; the argument only appears when the second series is drawn on the same
   axes, so the renderer never draws one without the other.
   ============================================================================= */

window.FEmpowerment = (function () {
  "use strict";
  var D = window.EMPOWERMENT;
  var state = { indicator: null };

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function byId(id) {
    return D.indicators.filter(function (i) { return i.id === id; })[0];
  }
  function dim(id) {
    return D.dimensions.filter(function (d) { return d.id === id; })[0];
  }

  /* ------------------------------------------------------------ sparkline */
  /* Fixed 0-100 scale on every chart, headline and companion alike. A chart
     scaled to its own data would make a two-point drift look like a collapse,
     which is the visual version of the mistake this page is about. */
  function spark(points, colour, w, h) {
    if (!points.length) return "";
    var PAD = 4;
    var span = points.length > 1 ? (w - PAD * 2) / (points.length - 1) : 0;
    var y = function (v) { return h - PAD - (h - PAD * 2) * (v / 100); };
    var d = points.map(function (p, i) {
      return (i ? "L" : "M") + (PAD + i * span).toFixed(1) + "," + y(p.value).toFixed(1);
    }).join(" ");
    var dots = points.map(function (p, i) {
      return '<circle cx="' + (PAD + i * span).toFixed(1) + '" cy="' + y(p.value).toFixed(1) +
             '" r="2.2" fill="' + colour + '"/>';
    }).join("");
    return '<svg viewBox="0 0 ' + w + " " + h + '" class="em-spark" aria-hidden="true">' +
           '<path d="' + d + '" fill="none" stroke="' + colour + '" stroke-width="1.8" ' +
           'stroke-linecap="round" stroke-linejoin="round"/>' + dots + "</svg>";
  }

  /* --------------------------------------------------------- the big chart */
  /* Width of the column the figures render into, so the SVG can be drawn 1:1.
     A fixed 620-unit viewBox is squeezed into whatever the column actually is,
     and every font size inside is multiplied by that ratio: measured at 0.55 in
     a 340px phone column, which turned 9.5px axis labels into 5.2px, and 0.795
     even on desktop, which made them 7.55px. Drawing at the real width makes a
     declared size a true size. */
  function chartWidth() {
    var box = document.getElementById("emChart");
    var w = box ? box.clientWidth - 32 : 0;          // figure padding either side
    return Math.max(300, Math.min(620, Math.round(w || 620)));
  }

  function bigChart(ind) {
    var d = dim(ind.dimension);
    var W = chartWidth(), H = 306, L = 58, R = 18, T = 24, B = 78;
    // Labels drawn at their true size are large enough to collide, which the
    // old squeezed rendering hid by making them unreadable. Measured on the
    // seven education categories: at -32 degrees, three pairs overlapped at
    // 340px and one at 493px. More categories in less width need a steeper
    // tilt and more room beneath; upright is the only angle that cannot
    // collide, since each label then occupies its own text height.
    var many = Math.max(ind.series.length, ind.companion.length) > 5;
    var TILT = -32;
    // Upright labels need real room: "Higher secondary" is about 80px of it,
    // and at B=108 it was clipping out of the bottom of the box. Give that
    // case a taller canvas rather than squeezing the plot to pay for it.
    if (many && W < 460) { TILT = -90; B = 118; H = 340; }
    else if (many) { TILT = -50; B = 92; }
    var plotW = W - L - R, plotH = H - T - B;
    var y = function (v) { return T + plotH - plotH * (v / 100); };
    var out = ['<svg viewBox="0 0 ' + W + " " + H + '" class="em-svg" role="img" aria-label="' +
               esc(ind.name + ": " + ind.series.map(function (p) { return p.label + " " + p.value + "%"; }).join(", ")) + '">'];

    for (var g = 0; g <= 100; g += 25) {
      out.push('<line class="em-grid" x1="' + L + '" x2="' + (W - R) + '" y1="' + y(g) + '" y2="' + y(g) + '"/>');
      out.push('<text class="em-axis" x="' + (L - 8) + '" y="' + (y(g) + 3.5) + '" text-anchor="end">' + g + "</text>");
    }

    function drawSeries(points, colour, cls, dash) {
      var span = points.length > 1 ? plotW / (points.length - 1) : 0;
      var path = points.map(function (p, i) {
        return (i ? "L" : "M") + (L + i * span).toFixed(1) + "," + y(p.value).toFixed(1);
      }).join(" ");
      out.push('<path class="' + cls + '" d="' + path + '" fill="none" stroke="' + colour +
               '" stroke-width="2.4"' + (dash ? ' stroke-dasharray="6 4"' : "") + "/>");
      points.forEach(function (p, i) {
        var px = L + i * span;
        out.push('<circle cx="' + px.toFixed(1) + '" cy="' + y(p.value).toFixed(1) +
                 '" r="4" fill="' + colour + '"/>');
        out.push('<text class="em-val" x="' + px.toFixed(1) + '" y="' + (y(p.value) - 10).toFixed(1) +
                 '" text-anchor="middle">' + p.value.toFixed(1) + "</text>");
        out.push('<text class="em-tick" x="' + px.toFixed(1) + '" y="' + (H - B + 18) +
                 '" text-anchor="end" transform="rotate(' + TILT + " " + px.toFixed(1) + " " + (H - B + 18) + ')">' +
                 esc(p.label) + "</text>");
      });
    }

    drawSeries(ind.series, d.colour, "em-line", false);
    out.push("</svg>");

    var comp = ['<svg viewBox="0 0 ' + W + " " + H + '" class="em-svg" role="img" aria-label="' +
                esc(ind.companionTitle + ": " + ind.companion.map(function (p) { return p.label + " " + p.value + "%"; }).join(", ")) + '">'];
    var save = out;
    out = comp;
    for (var g2 = 0; g2 <= 100; g2 += 25) {
      out.push('<line class="em-grid" x1="' + L + '" x2="' + (W - R) + '" y1="' + y(g2) + '" y2="' + y(g2) + '"/>');
      out.push('<text class="em-axis" x="' + (L - 8) + '" y="' + (y(g2) + 3.5) + '" text-anchor="end">' + g2 + "</text>");
    }
    drawSeries(ind.companion, "#be123c", "em-line em-line--comp", true);
    out.push("</svg>");
    comp = out;
    out = save;

    return '<div class="em-pair">' +
           '<figure><figcaption>' + esc(ind.name) + ' <span>' + esc(ind.unit) + '</span></figcaption>' +
             out.join("") + "</figure>" +
           '<figure><figcaption>' + esc(ind.companionTitle) + " <span>same source</span></figcaption>" +
             comp.join("") + "</figure>" +
           "</div>";
  }

  /* ------------------------------------------------------------- the bands */
  /* --------------------------------------------------------- the sequence */
  /* Kabeer's three parts are a sequence, not a menu: resources are the
     pre-conditions, agency is the process, achievements are the outcomes, and a
     measurement of any one alone can move for reasons the framework would not
     count. The page said so in prose and then drew three stacked cards, which
     is a menu. See issue #1070.

     HTML rather than SVG, following js/ladder.js. Text inside an SVG is scaled
     by the ratio of rendered width to viewBox, so a declared size is not a
     rendered size (#1068); nothing here has that problem, and each stage gets
     real button semantics without being given them. */
  function drawChain() {
    var host = document.getElementById("emChain");
    if (!host) return;
    var parts = [];
    D.dimensions.forEach(function (d, i) {
      if (i) parts.push('<span class="fw-conn" aria-hidden="true"></span>');
      var n = D.indicators.filter(function (x) { return x.dimension === d.id; }).length;
      parts.push('<button type="button" class="em-stage" data-dim="' + esc(d.id) + '"' +
        ' aria-pressed="false" style="--em:' + esc(d.colour) + '">' +
        '<span class="em-stage-i">' + (i + 1) + "</span>" +
        "<b>" + esc(d.name) + "</b>" +
        '<span class="em-stage-gloss">' + esc(d.gloss) + "</span>" +
        // "series" is its own plural, so there is nothing to agree with.
        '<span class="em-stage-n">' + n + " series below</span>" +
        "</button>");
    });
    host.innerHTML =
      '<div class="fw-chain" role="group" aria-label="' +
        esc("Kabeer's three parts, in sequence: resources, then agency, then achievements") +
      '">' + parts.join("") + "</div>" +
      '<p class="em-chain-note" id="emChainNote" role="status"></p>';

    host.querySelectorAll("[data-dim]").forEach(function (b) {
      b.addEventListener("click", function () {
        var first = D.indicators.filter(function (x) {
          return x.dimension === b.getAttribute("data-dim");
        })[0];
        if (first) select(first.id);
      });
    });
  }

  /* Which part the open indicator measures, and what Kabeer says that part
     cannot settle on its own. This is the argument of the page, and until now
     it was only reachable by reading a card the reader had already scrolled
     past. */
  function markChain(ind) {
    var d = dim(ind.dimension);
    document.querySelectorAll("#emChain [data-dim]").forEach(function (b) {
      var on = b.getAttribute("data-dim") === ind.dimension;
      b.classList.toggle("is-on", on);
      b.setAttribute("aria-pressed", on ? "true" : "false");
    });
    var note = document.getElementById("emChainNote");
    if (note) {
      note.innerHTML =
        "<b>" + esc(ind.name) + "</b> measures <b>" + esc(d.name.toLowerCase()) + "</b>. " +
        esc(d.caution);
    }
  }

  function drawBands() {
    var box = document.getElementById("emBands");
    if (!box) return;
    box.innerHTML = D.dimensions.map(function (d) {
      var mine = D.indicators.filter(function (i) { return i.dimension === d.id; });
      return '<section class="em-band" style="--em:' + d.colour + '">' +
        "<h3>" + esc(d.name) + "</h3>" +
        '<p class="em-gloss">' + esc(d.gloss) + "</p>" +
        '<p class="em-caution"><b>Kabeer&rsquo;s caution.</b> ' + esc(d.caution) + "</p>" +
        '<div class="em-inds">' + mine.map(function (i) {
          return '<button type="button" class="em-ind" data-ind="' + esc(i.id) + '" aria-pressed="false">' +
                 spark(i.series, d.colour, 92, 30) +
                 "<span><b>" + esc(i.name) + "</b><em>" +
                 // The arrow is markup, so it is concatenated outside esc().
                 // Passing it through escaped the ampersand and printed "&rarr;".
                 esc(i.series[0].label + " " + i.series[0].value.toFixed(1)) + " &rarr; " +
                 esc(i.series[i.series.length - 1].label + " " +
                     i.series[i.series.length - 1].value.toFixed(1)) +
                 "</em></span></button>";
        }).join("") + "</div></section>";
    }).join("");
    box.addEventListener("click", function (e) {
      var b = e.target.closest("button[data-ind]");
      if (b) select(b.getAttribute("data-ind"));
    });
  }

  function select(id) {
    var ind = byId(id);
    if (!ind) return;
    state.indicator = id;
    markChain(ind);
    document.querySelectorAll("#emBands .em-ind").forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.getAttribute("data-ind") === id));
    });
    var chart = document.getElementById("emChart");
    if (chart) chart.innerHTML = bigChart(ind);
    var panel = document.getElementById("emPanel");
    if (panel) {
      var d = dim(ind.dimension);
      panel.innerHTML =
        '<span class="em-eyebrow" style="border-color:' + d.colour + ';color:' + d.colour + '">' +
          esc(d.name) + "</span>" +
        "<h3>" + esc(ind.name) + "</h3>" +
        '<p class="em-def">' + esc(ind.definition) + "</p>" +
        '<p class="em-headline"><b>As reported.</b> ' + esc(ind.headline) + "</p>" +
        '<p class="em-comp"><b>Beside it.</b> ' + esc(ind.complication) + "</p>" +
        '<div class="em-test"><h4>Kabeer&rsquo;s test</h4><p>' + esc(ind.test) + "</p></div>" +
        '<p class="em-src">' + esc(ind.source) + "</p>";
    }
  }

  function init() {
    if (!D) return;
    drawChain();
    drawBands();
    select("violence");

    // The chart is drawn at the column's real width, so it has to be redrawn
    // when that width changes. Debounced, and only on an actual change, so a
    // mobile browser collapsing its address bar does not rebuild the SVGs.
    var lastW = chartWidth(), t = null;
    window.addEventListener("resize", function () {
      clearTimeout(t);
      t = setTimeout(function () {
        var now = chartWidth();
        if (Math.abs(now - lastW) < 8) return;
        lastW = now;
        if (state.indicator) select(state.indicator);
      }, 150);
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();

  return { select: select };
})();
