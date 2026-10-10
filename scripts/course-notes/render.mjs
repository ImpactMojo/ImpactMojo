// Print the course-notes HTML written by build.py to A4 PDF.
//
//   node scripts/course-notes/render.mjs OUT_DIR
//
// Reads OUT_DIR/manifest.json, prints each document with page numbers in the
// footer, and refuses to keep a PDF with a near-empty page: on 2026-10-10 the
// sold PDFs carried 249 pages holding one oversized icon and nothing else,
// and a page count alone never showed it. Needs playwright-core and a
// Chromium (PLAYWRIGHT_CORE and CHROME override the defaults below).
import fs from "node:fs";
import path from "node:path";
import { execFileSync } from "node:child_process";

const out = process.argv[2];
if (!out) { console.error("usage: render.mjs OUT_DIR"); process.exit(2); }
const PW = process.env.PLAYWRIGHT_CORE || "/opt/node-tools/node_modules/playwright-core/index.mjs";
const CHROME = process.env.CHROME || "/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell";
const { chromium } = await import(PW);

const manifest = JSON.parse(fs.readFileSync(path.join(out, "manifest.json"), "utf8"));
const browser = await chromium.launch({ executablePath: CHROME });
const page = await browser.newPage();
// The sandbox has no network; anything not on disk is dropped rather than waited on.
await page.route("**/*", (r) => r.request().url().startsWith("file:") ? r.continue() : r.abort());
let failed = 0;
for (const m of manifest) {
  await page.goto("file://" + path.resolve(m.html), { waitUntil: "load" });
  const file = path.join(out, m.pdf);
  const foot = `<div style="font-size:7pt;color:#64748B;width:100%;padding:0 17mm;display:flex;justify-content:space-between;font-family:Arial">` +
    `<span>${m.title.replace(/&/g, "&amp;")}: ImpactMojo Course Notes</span><span class="pageNumber"></span></div>`;
  await page.pdf({ path: file, format: "A4", printBackground: true, displayHeaderFooter: true,
    headerTemplate: "<span></span>", footerTemplate: foot, margin: { top: "18mm", bottom: "20mm", left: "17mm", right: "17mm" } });
  const pages = Number(execFileSync("pdfinfo", [file]).toString().match(/Pages:\s+(\d+)/)[1]);
  const thin = [];
  for (let i = 2; i <= pages; i++) { // page 1 is the cover
    const words = execFileSync("pdftotext", ["-f", String(i), "-l", String(i), file, "-"]).toString().split(/\s+/).filter(Boolean).length;
    if (words < 25) thin.push(i);
  }
  const ok = thin.length === 0;
  if (!ok) failed++;
  console.log(`${ok ? "ok  " : "FAIL"} ${m.pdf}: ${pages} pages, ${m.modules} modules${ok ? "" : ", near-empty pages " + thin.join(",")}`);
}
await browser.close();
process.exit(failed ? 1 : 0);
