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
  function bigChart(ind) {
    var d = dim(ind.dimension);
    var W = 620, H = 306, L = 58, R = 18, T = 24, B = 78;
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
                 '" text-anchor="end" transform="rotate(-32 ' + px.toFixed(1) + " " + (H - B + 18) + ')">' +
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
                 esc(i.series[0].label + " " + i.series[0].value + " &rarr; " +
                     i.series[i.series.length - 1].label + " " + i.series[i.series.length - 1].value) +
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
    drawBands();
    select("violence");
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();

  return { select: select };
})();
