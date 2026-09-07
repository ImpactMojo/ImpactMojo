/* =============================================================================
   ImpactMojo — Fundamentals: The Results Chain
   Depends on /js/results-chain-data.js.

   The page argues that the chain breaks one link before the claim a programme
   is defended with, and that it breaks in the same place in all six. So the
   chain has to be on the screen: five links, four connectors, and the broken
   one drawn broken. An earlier version of this file drew five bars whose
   heights encoded the measurement state, which could show that the fourth
   number was smaller than the third but could not show a severed link, because
   there was no link. See issue #1070.

   Two renderings of the same object:

     - the interactive chain is HTML, not SVG, following js/ladder.js. Text in
       an SVG is multiplied by the ratio between the rendered width and the
       viewBox, so a size declared in the source is not a size on the screen
       (#1068). HTML has no such scaling, wraps by itself, stacks by itself in
       a media query, and gives every node real button semantics for free.

     - the small multiples are SVG and carry no text at all. Six shapes side by
       side is the argument; naming every node six times over is not. The five
       links are named once, in HTML, above the grid, and each figure carries a
       full sentence as its accessible name.
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

  function linkAt(i) { return D.links[i]; }

  function linkIndex(id) {
    for (var i = 0; i < D.links.length; i++) if (D.links[i].id === id) return i;
    return -1;
  }

  /* The break is recorded on the link the chain fails to reach, so the link it
     survives to is the one before. "Breaks after outputs" and "breaks at
     outcomes" name the same connector. */
  function lastGoodLink(p) {
    return linkAt(Math.max(0, linkIndex(p.breaks) - 1));
  }

  /* ------------------------------------------------- the chain, as HTML */
  function nodeHTML(p, link, i, interactive) {
    var cell = p.chain[link.id];
    var st = D.states[cell.state];
    var tag = interactive ? "button" : "div";
    return "<" + tag + ' class="rc-node rc-node--' + esc(cell.state) + '"' +
      ' style="--rc:' + esc(p.colour) + '"' +
      (interactive
        ? ' type="button" data-link="' + esc(link.id) + '" aria-pressed="false"'
        : "") +
      "><span class=\"rc-node-i\">" + (i + 1) + "</span>" +
      "<b>" + esc(link.name) + "</b>" +
      "<em>" + esc(st.short) + "</em>" +
      "</" + tag + ">";
  }

  /* The connector into link i. Severed when that link is where the chain
     stops carrying weight, which is the one thing this page is about, so it
     is labelled in text rather than left to the reader to infer from a
     dashed line. */
  function connHTML(p, i) {
    var cut = p.breaks === linkAt(i).id;
    if (!cut) return '<span class="fw-conn" aria-hidden="true"></span>';
    return '<span class="fw-conn fw-conn--cut">' +
             '<i aria-hidden="true"></i>' +
             '<span class="fw-cut-note">breaks here</span>' +
           "</span>";
  }

  function drawChain(p) {
    var host = document.getElementById("rcChart");
    if (!host) return;
    var parts = [];
    D.links.forEach(function (link, i) {
      if (i) parts.push(connHTML(p, i));
      parts.push(nodeHTML(p, link, i, true));
    });
    host.innerHTML = '<div class="fw-chain" role="group" aria-label="' +
      esc(p.name + ": the five links, and how each one is measured") + '">' +
      parts.join("") + "</div>";

    host.querySelectorAll("[data-link]").forEach(function (b) {
      b.addEventListener("click", function () {
        select(p.id, b.getAttribute("data-link"));
      });
    });
    markChain();
  }

  function markChain() {
    document.querySelectorAll("#rcChart [data-link]").forEach(function (b) {
      var on = b.getAttribute("data-link") === state.link;
      b.classList.toggle("is-on", on);
      b.setAttribute("aria-pressed", on ? "true" : "false");
    });
  }

  /* ------------------------------------- the same chain, as a small multiple */
  /* Fixed geometry, no text. A node is a shape whose fill says how it is
     measured; the reader learns the five positions once from the key above the
     grid and then reads six shapes without reading six sets of labels. */
  var NW = 44, NH = 34, GAP = 26, PAD = 8;

  /* Kept in step with .rc-key and .rc-node-sw in css/fundamentals.css. Opacity
     of the programme colour is the one channel this page uses for "how is this
     measured", so the three places it appears have to agree. */
  var RAMP = { continuous: "1", periodic: "0.66", research: "0.4" };

  function nodeX(i) { return PAD + i * (NW + GAP); }

  /* One sentence naming every link and its state, plus where the chain breaks.
     The figure carries no text, so this is the whole of it for a screen
     reader, and it should read as prose rather than as a list of fragments. */
  function multipleLabel(p) {
    var says = D.links.map(function (l) {
      return l.name.toLowerCase() + " " + D.states[p.chain[l.id].state].label.toLowerCase();
    }).join(", ");
    return p.name + ": " + says + ". The chain breaks after " +
           lastGoodLink(p).name.toLowerCase() + ".";
  }

  function multipleSVG(p) {
    var n = D.links.length;
    var W = PAD * 2 + n * NW + (n - 1) * GAP;
    var H = NH + PAD * 2;
    var mid = PAD + NH / 2;
    var parts = ['<svg viewBox="0 0 ' + W + " " + H + '" class="rc-svg" role="img" aria-label="' +
                 esc(multipleLabel(p)) + '">'];

    for (var i = 0; i < n - 1; i++) {
      var x0 = nodeX(i) + NW, x1 = nodeX(i + 1);
      var cut = p.breaks === linkAt(i + 1).id;
      var cls = cut ? "rc-flow rc-flow--cut" : "rc-flow";
      if (cut) {
        var c = (x0 + x1) / 2;
        // Two stubs with a gap between them, and the conventional pair of
        // slashes across the gap. A dashed line alone reads as "weaker", which
        // is not the claim: the claim is that it stops.
        parts.push('<path class="' + cls + '" d="M' + x0 + "," + mid + " L" + (x0 + 6) + "," + mid + '"/>');
        parts.push('<path class="' + cls + '" d="M' + (x1 - 12) + "," + mid + " L" + (x1 - 6) + "," + mid + '"/>');
        parts.push('<path class="rc-cut" d="M' + (c - 5) + "," + (mid - 7) + " L" + (c - 1) + "," + (mid + 7) +
                   " M" + (c + 1) + "," + (mid - 7) + " L" + (c + 5) + "," + (mid + 7) + '"/>');
      } else {
        parts.push('<path class="' + cls + '" d="M' + x0 + "," + mid + " L" + (x1 - 6) + "," + mid + '"/>');
      }
      parts.push('<path class="rc-head' + (cut ? " rc-head--cut" : "") + '" d="M' + (x1 - 6) + "," + (mid - 4) +
                 " L" + x1 + "," + mid + " L" + (x1 - 6) + "," + (mid + 4) + ' Z"/>');
    }

    D.links.forEach(function (link, i) {
      var cellState = p.chain[link.id].state;
      var st = D.states[cellState];
      parts.push('<g class="rc-mnode rc-mnode--' + esc(cellState) + '">');
      // The same four-step ramp the legend and the chain nodes use: opacity of
      // the programme colour, and an empty dashed outline for "not measured",
      // which is a different thing from a faint version of measured.
      parts.push(cellState === "absent"
        ? '<rect x="' + nodeX(i) + '" y="' + PAD + '" width="' + NW + '" height="' + NH +
          '" rx="7" fill="none"/>'
        : '<rect x="' + nodeX(i) + '" y="' + PAD + '" width="' + NW + '" height="' + NH +
          '" rx="7" fill="' + p.colour + '" fill-opacity="' + RAMP[cellState] + '"/>');
      parts.push("<title>" + esc(link.name + " — " + st.label) + "</title>");
      parts.push("</g>");
    });

    parts.push("</svg>");
    return parts.join("");
  }

  function drawSmallMultiples() {
    var box = document.getElementById("smallMultiples");
    if (!box) return;
    box.innerHTML = D.programmes.map(function (p) {
      return '<figure class="rc-sm">' +
             "<figcaption><b>" + esc(p.name) + "</b> <span>since " + esc(p.since) + "</span></figcaption>" +
             multipleSVG(p) +
             '<p class="rc-sm-break">Breaks after <b>' +
               esc(lastGoodLink(p).name.toLowerCase()) + "</b></p>" +
             "</figure>";
    }).join("");
  }

  /* The five links named once, in HTML, above the grid. In the figures the
     nodes carry no text, so this is where a reader learns the order. */
  function drawMultiplesKey() {
    var box = document.getElementById("rcOrder");
    if (!box) return;
    box.innerHTML = D.links.map(function (l, i) {
      return "<li><span>" + (i + 1) + "</span>" + esc(l.name) + "</li>";
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
    var p = programmeById(progId);
    if (!p) return;
    var changedProgramme = state.programme !== progId;
    state.programme = progId;
    state.link = linkId || "outputs";

    document.querySelectorAll("#rcPicker .chip").forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.getAttribute("data-prog") === progId));
    });

    // Only rebuild the chain when the programme changed. Re-rendering it on
    // every link click would destroy the button the reader just pressed, which
    // takes the focus ring with it.
    if (changedProgramme || !document.querySelector("#rcChart .fw-chain")) drawChain(p);
    else markChain();
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
    drawMultiplesKey();
    drawSmallMultiples();
    drawLegend();
    drawPicker();
    select(D.programmes[0].id, "outputs");
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();

  return { select: select };
})();
