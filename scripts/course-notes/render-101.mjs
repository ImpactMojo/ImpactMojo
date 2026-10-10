// Print a 101 deck as A4 course notes: a cover, then the slides two to a page.
//
//   node scripts/course-notes/render-101.mjs OUT_DIR slug [slug ...]
//
// The deck is served from the repository by a local server and printed in
// the light theme, with every slide shown as a fixed 1280x720 frame and
// scaled into the page, so text stays text and diagrams stay vector.
// Chart.js and ECharts load from a CDN in the decks; the sandbox cannot reach
// it, so LIBS maps those requests to local copies (set CHARTJS and ECHARTS).
import fs from "node:fs";
import path from "node:path";
import http from "node:http";
import { execFileSync } from "node:child_process";

const [out, ...slugs] = process.argv.slice(2);
if (!out || !slugs.length) { console.error("usage: render-101.mjs OUT_DIR slug [slug ...]"); process.exit(2); }
const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), "../..");
const PW = process.env.PLAYWRIGHT_CORE || "/opt/node-tools/node_modules/playwright-core/index.mjs";
const CHROME = process.env.CHROME || "/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell";
const LIBS = { "chart.js": process.env.CHARTJS, "echarts": process.env.ECHARTS };
const { chromium } = await import(PW);
const decks = JSON.parse(fs.readFileSync(path.join(ROOT, "data/decks.json"), "utf8")).decks;

const TYPES = { ".html": "text/html", ".css": "text/css", ".js": "text/javascript", ".svg": "image/svg+xml", ".png": "image/png", ".woff2": "font/woff2", ".json": "application/json" };
const server = http.createServer((req, res) => {
  const p = path.join(ROOT, decodeURIComponent(new URL(req.url, "http://x").pathname));
  if (!p.startsWith(ROOT) || !fs.existsSync(p) || fs.statSync(p).isDirectory()) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { "Content-Type": TYPES[path.extname(p)] || "application/octet-stream" });
  fs.createReadStream(p).pipe(res);
}).listen(0);
const base = `http://localhost:${server.address().port}`;

const SCALE = 0.56, MARGIN = { top: "8mm", bottom: "12mm", left: "9mm", right: "9mm" };
// Printable height 297 - 20 = 277 mm = 1047 px at 96 dpi; in layout px that is 1047 / SCALE.
const SHEET = Math.floor(1047 / SCALE) - 8;
const PRINT = `
html,body{background:#fff!important;margin:0!important;overflow:visible!important;height:auto!important}
#progress-bar,#fs-hint,.nav-controls,.deck-nav,#nav,.slide-nav,.im-topbar,.mobile-nav,.skip-link,.controls,#controls,.kbd-hint,button.theme-toggle{display:none!important}
#deck{position:static!important;display:block!important;min-height:0!important}
.slide-viewport{width:1280px!important;height:auto!important;transform:none!important;position:static!important;margin:0 auto!important}
.slide{display:flex!important;flex-direction:column;position:relative!important;inset:auto!important;width:1280px!important;height:720px!important;min-height:0!important;margin:0!important;flex:none!important;box-shadow:0 0 0 1px #CBD5E1!important;overflow:hidden!important}
/* One A4 page per sheet: two slides and ruled space to write in. */
.sheet{width:1280px;height:SHEETpx;margin:0 auto;display:flex;flex-direction:column;gap:22px;break-after:page;page-break-after:always;overflow:hidden}
.sheet:last-child{break-after:auto;page-break-after:auto}
.sheet .lines{flex:1;min-height:0;border-top:2px solid #0369A1;padding-top:6px;font:600 15px Inter,Arial,sans-serif;letter-spacing:.12em;color:#0369A1;background:repeating-linear-gradient(to bottom,transparent 0,transparent 43px,#CBD5E1 43px,#CBD5E1 44px);background-position:0 30px}
.slide-content{position:absolute!important;top:var(--header-h)!important;bottom:var(--footer-h)!important;left:0!important;right:0!important;height:auto!important;overflow:hidden!important;zoom:1!important}
.notes-cover{width:1280px;height:SHEETpx;margin:0 auto;display:flex;flex-direction:column;justify-content:center;text-align:center;font-family:Inter,Arial,sans-serif;color:#0F172A;page-break-after:always;break-after:page;position:relative}
.notes-cover .brand{position:absolute;top:40px;left:0;right:0;font-size:20px;letter-spacing:.14em;font-weight:700;color:#0369A1}
.notes-cover .series{font-size:22px;letter-spacing:.18em;text-transform:uppercase;color:#475569}
.notes-cover h1{font-size:72px;line-height:1.1;margin:.3em 0}
.notes-cover .kind{font-size:30px;color:#0369A1;font-weight:600}
.notes-cover .meta{font-size:24px;color:#475569;margin-top:.5em}
.notes-cover .blurb{font-size:24px;line-height:1.5;color:#334155;max-width:900px;margin:1.4em auto 0}
.notes-cover ol{text-align:left;max-width:900px;margin:1.4em auto 0;font-size:22px;line-height:1.6;color:#334155;columns:2;column-gap:48px}
.notes-cover .legal{position:absolute;bottom:40px;left:0;right:0;font-size:18px;color:#64748B}
`.replace(/SHEET/g, SHEET);

const browser = await chromium.launch({ executablePath: CHROME });
const manifest = [];
let failed = 0;
for (const slug of slugs) {
  const meta = decks.find((d) => d.slug === slug);
  if (!meta) { console.error("no deck " + slug); failed++; continue; }
  let ctx;
  try {
  ctx = await browser.newContext({ viewport: { width: 1400, height: 900 }, colorScheme: "light" });
  const page = await ctx.newPage();
  page.setDefaultTimeout(60000);
  const step = (m) => process.env.DEBUG && console.error(`  ${slug}: ${m}`);
  await page.route("**/*", (r) => {
    const u = r.request().url();
    if (u.startsWith(base)) return r.continue();
    for (const [lib, file] of Object.entries(LIBS))
      if (file && u.includes(`/npm/${lib}@`)) return r.fulfill({ path: file, contentType: "text/javascript" });
    return r.abort();
  });
  await page.addInitScript(() => { try { localStorage.setItem("theme", "light"); } catch (e) {} });
  step("goto"); await page.goto(`${base}/101-courses/${slug}.html`, { waitUntil: "load" }); step("loaded");
  const n = await page.evaluate(() => document.querySelectorAll(".slide").length);
  // Visit every slide so decks that draw charts on arrival get to draw them.
  for (let i = 0; i < n; i++) { await page.keyboard.press("ArrowRight"); }
  step("visited slides"); await page.waitForTimeout(800);
  await page.addStyleTag({ content: PRINT });
  const sections = meta.sections || [];
  await page.evaluate(({ meta, sections }) => {
    document.documentElement.setAttribute("data-theme", "light");
    document.body.classList.add("light"); document.body.classList.remove("dark-mode");
    const esc = (t) => String(t).replace(/[&<>]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c]));
    const cover = document.createElement("section");
    cover.className = "notes-cover";
    cover.innerHTML = `<div class="brand">IMPACTMOJO · IMPACTMOJO.IN</div><div class="series">ImpactMojo 101 Series</div><h1>${esc(meta.title)}</h1><div class="kind">Course Notes</div><div class="meta">${meta.slides} slides · ${sections.length} sections</div><p class="blurb">${esc(meta.desc)} Every slide of the course, two to a page, ready to print, annotate and keep.</p>${sections.length ? "<ol>" + sections.map((s) => `<li>${esc(s)}</li>`).join("") + "</ol>" : ""}<div class="legal">© 2026 ImpactMojo · CC BY-NC-ND 4.0 · For the personal use of the purchaser</div>`;
    const deck = document.getElementById("deck") || document.body;
    deck.parentNode.insertBefore(cover, deck);
    // Anything fixed to the viewport (chat bubble, nav pills) would repeat on every page.
    for (const el of document.querySelectorAll("body *")) if (getComputedStyle(el).position === "fixed") el.style.setProperty("display", "none", "important");
    const slides = [...document.querySelectorAll(".slide")];
    const host = slides[0].parentNode;
    for (let i = 0; i < slides.length; i += 2) {
      const sheet = document.createElement("div"); sheet.className = "sheet";
      host.appendChild(sheet);
      sheet.appendChild(slides[i]); if (slides[i + 1]) sheet.appendChild(slides[i + 1]);
      const lines = document.createElement("div"); lines.className = "lines"; lines.textContent = "NOTES"; sheet.appendChild(lines);
    }
    window.dispatchEvent(new Event("resize"));
    if (window.Chart && Chart.instances) Object.values(Chart.instances).forEach((c) => { try { c.resize(); c.update("none"); } catch (e) {} });
    if (window.echarts) document.querySelectorAll("[_echarts_instance_]").forEach((el) => { try { echarts.getInstanceByDom(el).resize(); } catch (e) {} });
  }, { meta, sections });
  await page.waitForTimeout(600);
  // A chart that never drew prints as an empty box and nothing else says so.
  const charts = await page.evaluate(() => {
    let total = 0, blank = 0;
    for (const c of document.querySelectorAll(".slide canvas")) {
      if (c.width < 20 || c.height < 20) continue;
      total++;
      try {
        const d = c.getContext("2d").getImageData(0, 0, c.width, c.height).data;
        let ink = 0; for (let i = 3; i < d.length; i += 4 * 7) if (d[i] > 0) ink++;
        if (ink < 50) blank++;
      } catch (e) {}
    }
    return { total, blank };
  });
  await page.emulateMedia({ media: "print", colorScheme: "light" });
  const file = path.join(out, `ImpactMojo-101-Notes-${slug}.pdf`);
  const foot = `<div style="font-size:7pt;color:#64748B;width:100%;padding:0 9mm;display:flex;justify-content:space-between;font-family:Arial"><span>${meta.title.replace(/&/g, "&amp;")}: ImpactMojo Course Notes</span><span class="pageNumber"></span></div>`;
  step("printing"); await page.pdf({ path: file, format: "A4", scale: SCALE, printBackground: true, displayHeaderFooter: true, headerTemplate: "<span></span>", footerTemplate: foot, margin: MARGIN });
  const pages = Number(execFileSync("pdfinfo", [file]).toString().match(/Pages:\s+(\d+)/)[1]);
  const want = 1 + Math.ceil(n / 2);
  const ok = pages === want && charts.blank === 0;
  if (!ok) failed++;
  console.log(`${ok ? "ok  " : "FAIL"} ${path.basename(file)}: ${n} slides, ${pages} pages, ${charts.total} charts${charts.blank ? ", " + charts.blank + " BLANK" : ""}${pages === want ? "" : " (expected " + want + " pages)"}`);
  manifest.push({ slug, title: meta.title, slides: n, pages, charts: charts.total, pdf: path.basename(file) });
  } catch (e) {
    failed++;
    console.log(`FAIL ${slug}: ${e.message.split("\n")[0]}`);
  } finally {
    if (ctx) await ctx.close().catch(() => {});
  }
}
fs.writeFileSync(path.join(out, "manifest-101.json"), JSON.stringify(manifest, null, 1));
await browser.close(); server.close();
process.exit(failed ? 1 : 0);
