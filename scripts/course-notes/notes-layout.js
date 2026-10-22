/* Browser-side layout for the course notes. Loaded into a deck page by render-101.mjs, after rough.js.
   window.NotesLayout.build({ meta, notes, deck }) rebuilds the page as: a cover, then for every section
   two hand-written pages (idea, diagram, terms; worked example, mistakes, recall), then the section's
   slides two to a page with a note under each. It returns { problems: [] } listing anything that overflowed. */
(function () {
  const NS = "http://www.w3.org/2000/svg";
  const COLORS = ["#fde2e0", "#dbeafe", "#d1fae5", "#fef3c7", "#ede9fe", "#fce7f3"];
  const INK = "#1f2a44";
  const esc = (t) => String(t).replace(/[&<>]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c]));
  // **text** becomes a highlighter mark; nothing else is markup.
  const rich = (t) => esc(t).replace(/\*\*(.+?)\*\*/g, "<mark>$1</mark>");
  const h = (tag, cls, html) => { const e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; };
  const sv = (tag, attrs) => { const e = document.createElementNS(NS, tag); for (const k in attrs) e.setAttribute(k, attrs[k]); return e; };

  let measureCtx;
  function measure(font, text) { if (!measureCtx) measureCtx = document.createElement("canvas").getContext("2d"); measureCtx.font = font; return measureCtx.measureText(text).width; }
  function wrap(font, text, maxW) {
    const words = String(text).split(/\s+/); const lines = []; let cur = "";
    for (const w of words) { const t = cur ? cur + " " + w : w; if (cur && measure(font, t) > maxW) { lines.push(cur); cur = w; } else cur = t; }
    if (cur) lines.push(cur); return lines;
  }
  function seedOf(s) { let x = 7; for (const c of String(s)) x = (x * 31 + c.charCodeAt(0)) % 99991; return x + 1; }

  // text block centred at (cx, y top); returns height used
  function textBlock(svg, lines, cx, y, size, weight, fill, lh) {
    const t = sv("text", { "text-anchor": "middle", "font-family": "NCaveat,cursive", "font-size": size, "font-weight": weight, fill });
    lines.forEach((ln, i) => { const s = sv("tspan", { x: cx, y: y + size * 0.85 + i * (lh || size * 1.05) }); s.textContent = ln; t.appendChild(s); });
    svg.appendChild(t); return lines.length * (lh || size * 1.05);
  }
  function arrow(rc, svg, x1, y1, x2, y2, o) {
    svg.appendChild(rc.line(x1, y1, x2, y2, Object.assign({ stroke: INK, strokeWidth: 2.6, roughness: 1.4 }, o)));
    const a = Math.atan2(y2 - y1, x2 - x1), L = 15;
    for (const d of [0.5, -0.5]) svg.appendChild(rc.line(x2, y2, x2 - L * Math.cos(a - d), y2 - L * Math.sin(a - d), { stroke: INK, strokeWidth: 2.6, roughness: 1 }));
  }
  function box(rc, svg, x, y, w, hgt, i, label, sub, size) {
    size = size || 28;
    svg.appendChild(rc.rectangle(x, y, w, hgt, { stroke: INK, strokeWidth: 2.4, roughness: 1.5, fill: COLORS[i % COLORS.length], fillStyle: "solid", seed: seedOf(label) }));
    const font = `700 ${size}px NCaveat`;
    const ll = wrap(font, label, w - 24), sl = sub ? wrap(`400 ${size - 6}px NCaveat`, sub, w - 24) : [];
    const total = ll.length * size * 1.05 + (sl.length ? sl.length * (size - 6) * 1.05 + 4 : 0);
    let yy = y + (hgt - total) / 2;
    yy += textBlock(svg, ll, x + w / 2, yy, size, 700, INK);
    if (sl.length) textBlock(svg, sl, x + w / 2, yy + 4, size - 6, 400, "#475569");
  }
  function boxH(label, sub, w, size) {
    size = size || 28;
    const ll = wrap(`700 ${size}px NCaveat`, label, w - 24), sl = sub ? wrap(`400 ${size - 6}px NCaveat`, sub, w - 24) : [];
    return Math.max(70, ll.length * size * 1.05 + (sl.length ? sl.length * (size - 6) * 1.05 + 4 : 0) + 30);
  }

  const DIAGRAMS = {
    flow(rc, svg, s, W) {
      const n = s.nodes.length, cols = n <= 4 ? n : Math.ceil(n / 2), gap = 56;
      const w = (W - 40 - gap * (cols - 1)) / cols;
      const rows = Math.ceil(n / cols), rh = [];
      for (let r = 0; r < rows; r++) rh.push(Math.max(...s.nodes.slice(r * cols, r * cols + cols).map((nd) => boxH(nd.label, nd.sub, w))));
      let y = 20; const pos = [];
      for (let r = 0; r < rows; r++) { for (let c = 0; c < cols && r * cols + c < n; c++) pos.push({ x: 20 + c * (w + gap), y, w, h: rh[r], r, c }); y += rh[r] + 64; }
      s.nodes.forEach((nd, i) => box(rc, svg, pos[i].x, pos[i].y, w, pos[i].h, i, nd.label, nd.sub));
      for (let i = 0; i < n - 1; i++) {
        const a = pos[i], b = pos[i + 1];
        if (a.r === b.r) arrow(rc, svg, a.x + a.w + 6, a.y + a.h / 2, b.x - 6, b.y + b.h / 2);
        else {
          const x1 = a.x + a.w / 2, y1 = a.y + a.h + 4, y2 = b.y - 6, ym = y1 + 28;
          svg.appendChild(rc.linearPath([[x1, y1], [x1, ym], [b.x + b.w / 2, ym]], { stroke: INK, strokeWidth: 2.6, roughness: 1.3 }));
          arrow(rc, svg, b.x + b.w / 2, ym, b.x + b.w / 2, y2);
        }
      }
      return y - 64 + 20;
    },
    cycle(rc, svg, s, W) {
      const n = s.nodes.length, cx = W / 2, rx = W / 2 - 190, ry = 190, bw = 270; const H = ry * 2 + 150;
      const cy = H / 2, pts = s.nodes.map((_, i) => { const a = -Math.PI / 2 + (i * 2 * Math.PI) / n; return [cx + rx * Math.cos(a), cy + ry * Math.sin(a)]; });
      s.nodes.forEach((nd, i) => { const bh = boxH(nd.label, nd.sub, bw); box(rc, svg, pts[i][0] - bw / 2, pts[i][1] - bh / 2, bw, bh, i, nd.label, nd.sub); });
      if (s.center) textBlock(svg, wrap("700 34px NCaveat", s.center, 300), cx, cy - 30, 34, 700, "#b42318");
      for (let i = 0; i < n; i++) {
        const a = pts[i], b = pts[(i + 1) % n]; const dx = b[0] - a[0], dy = b[1] - a[1], d = Math.hypot(dx, dy);
        const shrinkA = Math.abs(dx) > Math.abs(dy) ? bw / 2 + 8 : 60, shrinkB = Math.abs(dx) > Math.abs(dy) ? bw / 2 + 12 : 66;
        const x1 = a[0] + (dx / d) * shrinkA, y1 = a[1] + (dy / d) * shrinkA, x2 = b[0] - (dx / d) * shrinkB, y2 = b[1] - (dy / d) * shrinkB;
        arrow(rc, svg, x1, y1, x2, y2, { roughness: 1.6 });
      }
      return H;
    },
    tree(rc, svg, s, W) {
      const kids = s.children, n = kids.length, gap = 24, w = (W - 40 - gap * (n - 1)) / n;
      const rootW = 420, rootH = boxH(s.root, "", rootW, 32);
      box(rc, svg, (W - rootW) / 2, 20, rootW, rootH, 0, s.root, "", 32);
      const y2 = 20 + rootH + 80; let maxB = 0;
      kids.forEach((k, i) => {
        const x = 20 + i * (w + gap), bh = boxH(k.label, "", w);
        svg.appendChild(rc.line(W / 2, 20 + rootH, x + w / 2, y2, { stroke: INK, strokeWidth: 2.4, roughness: 1.4 }));
        box(rc, svg, x, y2, w, bh, i + 1, k.label, "");
        let yy = y2 + bh + 16;
        (k.items || []).forEach((it) => { const ll = wrap("400 24px NCaveat", "• " + it, w - 10); const t = sv("text", { "font-family": "NCaveat,cursive", "font-size": 24, fill: "#334155" }); ll.forEach((ln, j) => { const sp = sv("tspan", { x: x + 6, y: yy + 20 + j * 25 }); sp.textContent = ln; t.appendChild(sp); }); svg.appendChild(t); yy += ll.length * 25 + 6; });
        maxB = Math.max(maxB, yy);
      });
      return maxB + 10;
    },
    compare(rc, svg, s, W) {
      const colW = (W - 120) / 2; let H = 0; const hs = [];
      for (const side of [s.left, s.right]) {
        let hh = 70; for (const it of side.items) hh += wrap("400 26px NCaveat", "• " + it, colW - 30).length * 27 + 8; hs.push(hh + 16);
      }
      H = Math.max(...hs) + 40;
      [s.left, s.right].forEach((side, k) => {
        const x = 20 + k * (colW + 80);
        svg.appendChild(rc.rectangle(x, 20, colW, H - 30, { stroke: INK, strokeWidth: 2.4, roughness: 1.6, fill: COLORS[k === 0 ? 1 : 3], fillStyle: "solid", seed: seedOf(side.title) }));
        textBlock(svg, [side.title], x + colW / 2, 30, 36, 700, "#b42318");
        let yy = 84; side.items.forEach((it) => { const ll = wrap("400 26px NCaveat", "• " + it, colW - 30); const t = sv("text", { "font-family": "NCaveat,cursive", "font-size": 26, fill: INK }); ll.forEach((ln, j) => { const sp = sv("tspan", { x: x + 16, y: yy + 22 + j * 27 }); sp.textContent = ln; t.appendChild(sp); }); svg.appendChild(t); yy += ll.length * 27 + 8; });
      });
      textBlock(svg, [s.vs || "vs"], W / 2, H / 2 - 20, 44, 700, "#b42318");
      return H;
    },
    formula(rc, svg, s, W) {
      const parts = s.parts, size = 40; let total = 0; const items = parts.map((p) => { const wd = p.op ? measure(`700 54px NCaveat`, p.op) + 30 : Math.max(measure(`700 ${size}px NCaveat`, p.t) + 36, 150); total += wd; return { p, wd }; });
      let scale = Math.min(1, (W - 40) / total); const gapx = 0; let x = (W - total * scale) / 2; const y = 60; let maxHint = 0;
      items.forEach(({ p, wd }, i) => {
        const w = wd * scale;
        if (p.op) { textBlock(svg, [p.op], x + w / 2, y + 6, 54, 700, "#b42318"); }
        else {
          svg.appendChild(rc.rectangle(x + 4, y, w - 8, 76, { stroke: INK, strokeWidth: 2.4, roughness: 1.5, fill: COLORS[i % COLORS.length], fillStyle: "solid", seed: seedOf(p.t) }));
          const ll = wrap(`700 ${size}px NCaveat`, p.t, w - 20); textBlock(svg, ll, x + w / 2, y + 38 - (ll.length * size * 1.05) / 2, size, 700, INK);
          if (p.hint) { svg.appendChild(rc.line(x + w / 2, y + 80, x + w / 2, y + 112, { stroke: "#b42318", strokeWidth: 2, roughness: 1.2 })); const hl = wrap("600 26px NCaveat", p.hint, Math.max(w, 170) - 10); const hh = textBlock(svg, hl, x + w / 2, y + 116, 26, 600, "#b42318"); maxHint = Math.max(maxHint, hh); }
        }
        x += w;
      });
      let H = y + 116 + maxHint + 20;
      if (s.note) { const nl = wrap("600 30px NCaveat", s.note, W - 100); textBlock(svg, nl, W / 2, H, 30, 600, "#0f766e"); H += nl.length * 32 + 16; }
      return H;
    },
    timeline(rc, svg, s, W) {
      const n = s.events.length, lo = 150, hi = W - 150, xs = (i) => lo + (i * (hi - lo)) / Math.max(1, n - 1);
      const cw = Math.min(280, ((hi - lo) / Math.max(1, n - 1)) * 1.9);
      const blocks = s.events.map((e) => { const wl = wrap("700 34px NCaveat", e.when, cw), tl = wrap("400 28px NCaveat", e.what, cw); return { wl, tl, hh: wl.length * 36 + tl.length * 30 + 8 }; });
      const maxUp = Math.max(0, ...blocks.filter((_, i) => i % 2 === 0).map((b) => b.hh)), maxDown = Math.max(0, ...blocks.filter((_, i) => i % 2 === 1).map((b) => b.hh));
      const y0 = maxUp + 50;
      svg.appendChild(rc.line(30, y0, W - 30, y0, { stroke: INK, strokeWidth: 3.2, roughness: 1.6 }));
      s.events.forEach((e, i) => {
        const x = xs(i), up = i % 2 === 0, b = blocks[i];
        svg.appendChild(rc.circle(x, y0, 22, { stroke: INK, strokeWidth: 2.4, fill: COLORS[i % COLORS.length], fillStyle: "solid", roughness: 1.2 }));
        const yy = up ? y0 - 28 - b.hh : y0 + 28;
        svg.appendChild(rc.line(x, up ? y0 - 12 : y0 + 12, x, up ? y0 - 26 : y0 + 26, { stroke: INK, strokeWidth: 2, roughness: 1 }));
        const a = textBlock(svg, b.wl, x, yy, 34, 700, "#b42318", 36); textBlock(svg, b.tl, x, yy + a + 2, 28, 400, INK, 30);
      });
      return y0 + 28 + maxDown + 30;
    },
    stack(rc, svg, s, W) {
      const n = s.levels.length, lh = 92; const H = n * lh + 40;
      s.levels.forEach((lv, i) => {
        const wTop = 260 + (i * (W - 260 - 160)) / Math.max(1, n - 1), x = (W - wTop) / 2, y = 20 + i * lh;
        box(rc, svg, x, y, wTop, lh - 10, i, lv.label, lv.sub, 28);
      });
      return H;
    },
    hub(rc, svg, s, W) {
      const n = s.spokes.length, cx = W / 2, H = 460, cy = H / 2, rx = W / 2 - 170, ry = 170, bw = 270;
      const pts = s.spokes.map((_, i) => { const a = -Math.PI / 2 + (i * 2 * Math.PI) / n; return [cx + rx * Math.cos(a), cy + ry * Math.sin(a)]; });
      pts.forEach((p) => svg.appendChild(rc.line(cx, cy, p[0], p[1], { stroke: "#94a3b8", strokeWidth: 2.2, roughness: 1.6 })));
      const cw = 300, ch = boxH(s.center, "", cw, 34); box(rc, svg, cx - cw / 2, cy - ch / 2, cw, ch, 3, s.center, "", 34);
      s.spokes.forEach((sp, i) => { const bh = boxH(sp.label, sp.sub, bw); box(rc, svg, pts[i][0] - bw / 2, pts[i][1] - bh / 2, bw, bh, i, sp.label, sp.sub); });
      return H;
    },
  };

  // Diagrams are drawn on a narrower canvas and scaled up, so type and lines grow together.
  const ZOOM = 1.28;
  function drawDiagram(spec, Wout) {
    const W = Math.round(Wout / ZOOM);
    const svg = sv("svg", { xmlns: NS, width: Wout, height: 100 });
    const rc = rough.svg(svg); const fn = DIAGRAMS[spec.type];
    if (!fn) throw new Error("unknown diagram type " + spec.type);
    const H = Math.ceil(fn(rc, svg, spec, W));
    svg.setAttribute("viewBox", `0 0 ${W} ${H}`); svg.setAttribute("height", Math.ceil(H * ZOOM));
    return svg;
  }

  function numberBadge(n) {
    const d = h("div", "num"); const svg = sv("svg", { viewBox: "0 0 92 92" }); const rc = rough.svg(svg);
    svg.appendChild(rc.circle(46, 46, 78, { stroke: "#b42318", strokeWidth: 3.2, roughness: 2, fill: "#fff1f0", fillStyle: "solid", seed: n * 13 }));
    d.appendChild(svg); d.appendChild(h("b", "", String(n))); return d;
  }

  function noteBox(text, n) {
    const d = h("div", "nnote");
    const svg = sv("svg", { class: "edge", viewBox: "0 0 26 100", preserveAspectRatio: "none" }); const rc = rough.svg(svg);
    svg.appendChild(rc.line(13, 4, 13, 96, { stroke: "#b42318", strokeWidth: 3, roughness: 2.4, seed: n }));
    d.appendChild(svg); d.appendChild(h("span", "tag", "slide " + n)); d.appendChild(h("span", "body", rich(text))); return d;
  }

  function sectionPages(sec, total, title, SHEET) {
    const pages = [];
    // page 1: the idea, a diagram, the terms
    let p = h("div", "nsheet spage");
    const top = h("div", "top"); top.appendChild(numberBadge(sec.n));
    const tt = h("div"); tt.appendChild(h("div", "kicker", `section ${sec.n} of ${total}`)); tt.appendChild(h("h2", "", esc(sec.title))); top.appendChild(tt); p.appendChild(top);
    p.appendChild(h("div", "idea", rich(sec.big_idea)));
    for (const para of sec.in_plain_words) p.appendChild(h("p", "", rich(para)));
    const dg = h("div", "diagram"); dg.appendChild(drawDiagram(sec.diagram, 1190)); p.appendChild(dg);
    if (sec.diagram.caption) p.appendChild(h("div", "cap", esc(sec.diagram.caption)));
    p.appendChild(h("h3", "", "Words to know"));
    const terms = h("div", "terms"); for (const t of sec.key_terms) terms.appendChild(h("div", "", `<b>${esc(t.term)}</b><span>${rich(t.meaning)}</span>`)); p.appendChild(terms);
    p.appendChild(h("div", "mynotes", "<span>my notes</span>"));
    p.appendChild(h("div", "foot", `<span>${esc(title)}</span><span>section ${sec.n}</span>`)); pages.push(p);
    // page 2: worked example, mistakes, recall
    p = h("div", "nsheet spage");
    const top2 = h("div", "top"); top2.appendChild(numberBadge(sec.n)); const t2 = h("div"); t2.appendChild(h("div", "kicker", "now work with it")); t2.appendChild(h("h2", "", esc(sec.title))); top2.appendChild(t2); p.appendChild(top2);
    if (sec.worked_example) {
      const we = sec.worked_example; const b = h("div", "box"); b.appendChild(h("h3", "", esc(we.title)));
      if (we.setup) b.appendChild(h("p", "", rich(we.setup)));
      const ol = h("ol"); for (const st of we.steps) ol.appendChild(h("li", "", rich(st))); b.appendChild(ol);
      b.appendChild(h("p", "ans", "Answer: " + esc(we.answer))); p.appendChild(b);
    }
    p.appendChild(h("h3", "", "Mistakes people make"));
    const ul = h("ul"); for (const m of sec.mistakes) ul.appendChild(h("li", "", rich(m))); p.appendChild(ul);
    p.appendChild(h("h3", "", "Check yourself (cover the answers first)"));
    for (const qa of sec.recall) p.appendChild(h("div", "qa", `<div class="q">${rich(qa.q)}</div><div class="a"><b>Answer:</b> ${rich(qa.a)}</div>`));
    p.appendChild(h("div", "mynotes", "<span>my notes</span>"));
    p.appendChild(h("div", "foot", `<span>${esc(title)}</span><span>section ${sec.n}</span>`)); pages.push(p);
    return pages;
  }

  // Section pages are fitted: the content sits in .sin, whose zoom steps down until nothing overflows.
  function wrapInner(pg) {
    const foot = pg.querySelector(":scope > .foot"); const inner = h("div", "sin");
    [...pg.childNodes].forEach((c) => { if (c !== foot) inner.appendChild(c); });
    pg.insertBefore(inner, foot); return inner;
  }
  function fitPage(pg, SHEET, problems, label) {
    const inner = pg.querySelector(":scope > .sin"); const avail = SHEET - 34 - 56; let z = 1;
    const apply = () => { inner.style.zoom = z; inner.style.height = avail / z + "px"; };
    apply();
    while (inner.scrollHeight > inner.clientHeight + 1 && z > 0.74) { z = Math.round((z - 0.03) * 100) / 100; apply(); }
    if (inner.scrollHeight > inner.clientHeight + 1) problems.push(`${label} still overflows at zoom ${z}`);
    return z;
  }
  function fitNote(nn) {
    const body = nn.querySelector(".body"); let z = 1;
    while (nn.scrollHeight > nn.clientHeight + 1 && z > 0.72) { z = Math.round((z - 0.04) * 100) / 100; body.style.zoom = z; }
    return z;
  }

  function build({ meta, notes, deck, slideEls, host, SHEET }) {
    const problems = [];
    const title = meta.title;
    const frag = [];
    // cover
    const cover = h("section", "ncover");
    cover.innerHTML = `<div class="brand">IMPACTMOJO · IMPACTMOJO.IN</div><div class="series">ImpactMojo 101 series</div><h1>${esc(title)}</h1><div class="kind">Course notes</div>
      <div class="intro">${rich(notes.intro)}</div>
      <h3>What is in these notes</h3><ul><li>Every slide of the course, two to a page, each with a note written for it.</li><li>For each of the ${notes.sections.length} sections, two pages by hand: the idea, a diagram, the words to know, a worked example, common mistakes and questions to check yourself.</li><li>Room in the margin: the notes are written to be argued with, so add your own.</li></ul>
      <h3>Contents</h3><ol class="contents">${notes.sections.map((s) => `<li>${esc(s.title)}</li>`).join("")}</ol>
      <div class="legal">© 2026 ImpactMojo · CC BY-NC-ND 4.0 · For the personal use of the purchaser</div>`;
    frag.push(cover);
    const slideKinds = deck.slides;
    const bySec = new Map(); // section number -> slide numbers
    for (const s of slideKinds) { (bySec.get(s.section) || bySec.set(s.section, []).get(s.section)).push(s.n); }
    const pairPages = (nums) => {
      for (let i = 0; i < nums.length; i += 2) {
        const sheet = h("div", "nsheet");
        for (const n of nums.slice(i, i + 2)) {
          sheet.appendChild(slideEls[n - 1]);
          const kind = slideKinds[n - 1].kind;
          if (notes.notes[String(n)]) sheet.appendChild(noteBox(notes.notes[String(n)], n));
          else if (kind === "content") problems.push("no note for slide " + n);
          else if (nums.length > 1) { const sp = h("div"); sp.style.flex = "0 0 8px"; sheet.appendChild(sp); }
        }
        frag.push(sheet);
      }
    };
    // front matter: slides before the first section divider
    if (bySec.has(0)) pairPages(bySec.get(0));
    notes.sections.forEach((sec, i) => {
      for (const pg of sectionPages(sec, notes.sections.length, title, SHEET)) { wrapInner(pg); frag.push(pg); }
      if (bySec.has(i + 1)) pairPages(bySec.get(i + 1));
    });
    for (const f of frag) host.appendChild(f);
    frag.forEach((f, i) => {
      if (f.classList.contains("spage")) fitPage(f, SHEET, problems, `page ${i + 1}`);
      f.querySelectorAll(".nnote").forEach((nn) => fitNote(nn));
    });
    return { problems, frag };
  }

  window.NotesLayout = { build, drawDiagram };
})();
