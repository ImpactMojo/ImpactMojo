// Dump the text of every slide of a 101 deck, so notes can be written against what the slide says.
//
//   node scripts/course-notes/extract-deck.mjs OUT_DIR slug [slug ...]
//
// Writes OUT_DIR/<slug>.json: { slug, title, sections[], slides: [{ n, kind, section, text }] }.
// kind is "title", "section" (a divider), "end" or "content". A chart is a canvas, so its
// words are not in the text; the slide says "[chart]" where one sits.
import fs from "node:fs";
import path from "node:path";
import http from "node:http";

const [out, ...slugs] = process.argv.slice(2);
if (!out || !slugs.length) { console.error("usage: extract-deck.mjs OUT_DIR slug [slug ...]"); process.exit(2); }
const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), "../..");
const PW = process.env.PLAYWRIGHT_CORE || "/opt/node-tools/node_modules/playwright-core/index.mjs";
const CHROME = process.env.CHROME || "/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell";
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
fs.mkdirSync(out, { recursive: true });
const browser = await chromium.launch({ executablePath: CHROME });
for (const slug of slugs) {
  const meta = decks.find((d) => d.slug === slug);
  if (!meta) { console.error("no deck " + slug); continue; }
  const ctx = await browser.newContext({ viewport: { width: 1400, height: 900 } });
  const page = await ctx.newPage();
  await page.route("**/*", (r) => (r.request().url().startsWith(base) ? r.continue() : r.abort()));
  await page.goto(`${base}/101-courses/${slug}.html`, { waitUntil: "load" });
  const slides = await page.evaluate(() => {
    const clean = (t) => t.replace(/[ \t]+/g, " ").replace(/\n\s*\n+/g, "\n").trim();
    return [...document.querySelectorAll(".slide")].map((el, i) => {
      const c = el.cloneNode(true);
      c.querySelectorAll(".slide-header,.slide-footer,svg.sprites,script,style,.notes-buy,.title-geo").forEach((x) => x.remove());
      c.querySelectorAll("canvas").forEach((x) => x.replaceWith(document.createTextNode(" [chart] ")));
      c.querySelectorAll("tr").forEach((tr) => { tr.append(document.createTextNode("\n")); });
      c.querySelectorAll("td,th").forEach((td) => { td.append(document.createTextNode(" | ")); });
      c.querySelectorAll("p,li,h1,h2,h3,h4,div.card,div.step,.section-label,.callout,.stat,.big-number,.takeaway,.key,[class*=\"title\"],[class*=\"head\"]").forEach((x) => x.append(document.createTextNode("\n")));
      const text = clean(c.textContent);
      let kind = "content";
      if (el.querySelector(".title-screen")) kind = "title";
      else if (el.querySelector(".section-divider")) kind = "section";
      else if (i === document.querySelectorAll(".slide").length - 1) kind = "end";
      return { n: i + 1, kind, text };
    });
  });
  let section = 0;
  for (const s of slides) {
    if (s.kind === "section") section++;
    s.section = section;
  }
  fs.writeFileSync(path.join(out, `${slug}.json`), JSON.stringify({ slug, title: meta.title, sections: meta.sections || [], slides }, null, 1));
  const kinds = slides.reduce((a, s) => ((a[s.kind] = (a[s.kind] || 0) + 1), a), {});
  console.log(`${slug}: ${slides.length} slides`, JSON.stringify(kinds), `${slides.reduce((a, s) => a + s.text.length, 0)} chars`);
  await ctx.close();
}
await browser.close(); server.close();
