/**
 * Text contrast over every course page, light and dark, read from the browser.
 *
 * Course text is stored in Supabase and shells write their own colours, so no
 * stylesheet check sees the pairings that result. This loads each page, waits
 * for the module text, and measures every text element against the solid
 * colour behind it. It prints one line per distinct failure.
 *
 *   node scripts/audit-course-contrast.mjs [baseUrl]    (default https://www.impactmojo.in)
 *
 * Needs playwright-core and a Chromium (CHROME=/path, else the sandbox default).
 * Known false positives: elements on a gradient or colour() background are
 * read as the nearest solid colour and can report white on white. Look at a
 * screenshot before changing anything that shows only 1.0:1.
 */
import { chromium } from 'playwright-core';
import fs from 'node:fs';
import path from 'node:path';

const base = process.argv[2] || 'https://www.impactmojo.in';
const root = new URL('../courses/', import.meta.url).pathname;
const pages = fs.readdirSync(root).flatMap((d) => {
  const dir = path.join(root, d);
  if (!fs.statSync(dir).isDirectory()) return [];
  return fs.readdirSync(dir).filter((f) => /^(index|powerbi)\.html$/.test(f)).map((f) => `/courses/${d}/${f}`);
});
const browser = await chromium.launch({ executablePath: process.env.CHROME || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const agg = {};
for (const pg of pages) for (const dark of [false, true]) {
  const ctx = await browser.newContext({ viewport: { width: 1280, height: 900 }, colorScheme: dark ? 'dark' : 'light' });
  await ctx.addInitScript((d) => { try { localStorage.setItem('theme', d ? 'dark' : 'light'); } catch (e) {} }, dark);
  const p = await ctx.newPage();
  try {
    await p.goto(base + pg, { waitUntil: 'networkidle', timeout: 45000 });
    await p.evaluate((d) => { document.documentElement.dataset.theme = d ? 'dark' : 'light'; document.body.classList.toggle('dark-mode', d); }, dark);
    await p.waitForTimeout(2500);
    const found = await p.evaluate(() => {
      const num = (s) => (s.match(/[\d.]+/g) || []).map(Number);
      const L = (c) => { const [r, g, b] = c.map((v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; }); return 0.2126 * r + 0.7152 * g + 0.0722 * b; };
      const bg = (e) => { while (e) { const v = num(getComputedStyle(e).backgroundColor); if (v.length >= 3 && (v.length < 4 || v[3] > 0.5)) return v.slice(0, 3).map(Math.round); e = e.parentElement; } return [255, 255, 255]; };
      const out = {};
      for (const e of document.querySelectorAll('body *')) {
        if (e.closest('script,style,svg,.katex')) continue;
        if (![...e.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim().length > 2)) continue;
        const r = e.getBoundingClientRect(); if (!r.width || !r.height) continue;
        const cs = getComputedStyle(e); if (cs.visibility === 'hidden' || cs.opacity === '0') continue;
        const f = num(cs.color).slice(0, 3).map(Math.round), g = bg(e);
        const a = L(f), b = L(g), cr = (Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05);
        const fs = parseFloat(cs.fontSize), need = (fs >= 24 || (fs >= 18.6 && +cs.fontWeight >= 700)) ? 3 : 4.5;
        if (cr < need) { const k = e.tagName + '.' + String(e.className.baseVal ?? e.className).trim().split(/\s+/).join('.') + ' | ' + f + ' on ' + g; out[k] = { cr: +cr.toFixed(2), t: e.textContent.trim().slice(0, 28) }; }
      }
      return out;
    });
    for (const [k, v] of Object.entries(found)) { const kk = (dark ? 'DARK ' : 'LIGHT ') + k; (agg[kk] ||= { cr: v.cr, t: v.t, pages: new Set() }).pages.add(pg.split('/')[2]); }
  } catch (e) { console.log('ERR', pg, e.message.slice(0, 80)); }
  await ctx.close();
}
await browser.close();
const rows = Object.entries(agg).sort((a, b) => b[1].pages.size - a[1].pages.size);
console.log(rows.length + ' distinct failures');
for (const [k, v] of rows) console.log(v.cr, k, '[' + [...v.pages].join(',') + ']', JSON.stringify(v.t));
