#!/usr/bin/env node
// Draw the share cards listed in data/social-cards.json that are not on disk yet.
//
//   python3 scripts/build-social-tags.py      # decides what each card says
//   node scripts/render-social-cards.mjs      # draws the missing ones, deletes orphans
//
// Needs playwright-core and a Chromium. In the agent sandbox:
//   CHROME=/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell
// Each card is 1200x630, the size every platform crops to. The file name
// carries a hash of what is drawn, so this only ever draws cards whose text
// changed, and a stale card can never be served under a current name.
import { chromium } from 'playwright-core';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const MANIFEST = path.join(ROOT, 'data', 'social-cards.json');
const OUT = path.join(ROOT, 'assets', 'og');
const CHROME = process.env.CHROME || '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell';
const FONTS = pathToFileURL(path.join(ROOT, 'assets', 'fonts')).href;

const cards = Object.values(JSON.parse(fs.readFileSync(MANIFEST, 'utf8')));
fs.mkdirSync(OUT, { recursive: true });
const wanted = new Set(cards.map(c => path.basename(c.card)));
let removed = 0;
for (const f of fs.readdirSync(OUT)) {
  if (f.endsWith('.jpg') && !wanted.has(f)) { fs.unlinkSync(path.join(OUT, f)); removed++; }
}
let todo = cards.filter(c => !fs.existsSync(path.join(ROOT, c.card)));
if (process.env.ONLY) { const re = new RegExp(process.env.ONLY); todo = todo.filter(c => re.test(c.card)); }
if (!todo.length) { console.log(`all ${cards.length} cards present; ${removed} orphans removed`); process.exit(0); }

const page_html = `<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:Inter;src:url('${FONTS}/inter-var.woff2') format('woff2');font-weight:100 900}
@font-face{font-family:Inter;src:url('${FONTS}/inter-var-ext.woff2') format('woff2');font-weight:100 900;unicode-range:U+0100-024F,U+1E00-1EFF,U+20A0-20CF}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1200px;height:630px;background:#12141c;overflow:hidden}
#c{position:relative;width:1200px;height:630px;font-family:Inter,sans-serif;color:#f8fafc;padding:64px 72px 56px;display:flex;flex-direction:column}
#bar{position:absolute;left:0;top:0;right:0;height:12px}
#glow{position:absolute;right:-180px;top:-220px;width:620px;height:620px;border-radius:50%;opacity:.16}
#top{display:flex;justify-content:space-between;align-items:center;position:relative}
#brand{font-size:30px;font-weight:800;letter-spacing:-.5px}
#site{font-size:24px;color:#a0aec0;font-weight:500}
#mid{margin:auto 0;position:relative;display:flex;flex-direction:column}
#label{align-self:flex-start;font-size:24px;font-weight:700;letter-spacing:1.6px;text-transform:uppercase;padding:9px 18px;border-radius:8px;position:relative}
#title{margin-top:26px;font-weight:800;line-height:1.12;letter-spacing:-1px;max-width:1056px;position:relative}
#sub{margin-top:18px;font-size:28px;color:#cbd5e1;font-weight:500;position:relative}
</style></head><body><div id="c"><div id="bar"></div><div id="glow"></div>
<div id="top"><div id="brand">ImpactMojo</div><div id="site">impactmojo.in</div></div>
<div id="mid"><div id="label"></div><div id="title"></div><div id="sub"></div></div></div></body></html>`;
const tmp = path.join(OUT, '_template.html');
fs.writeFileSync(tmp, page_html);

const browser = await chromium.launch({ executablePath: CHROME });
const page = await browser.newPage({ viewport: { width: 1200, height: 630 } });
await page.goto(pathToFileURL(tmp).href);
await page.evaluate(() => document.fonts.ready);

let n = 0;
for (const c of todo) {
  await page.evaluate(({ label, title, sub, colour }) => {
    const lum = h => { const v = [1, 3, 5].map(i => parseInt(h.slice(i, i + 2), 16) / 255).map(x => x <= .03928 ? x / 12.92 : ((x + .055) / 1.055) ** 2.4); return .2126 * v[0] + .7152 * v[1] + .0722 * v[2]; };
    const ratio = (a, b) => { const [x, y] = [lum(a), lum(b)].sort((p, q) => q - p); return (x + .05) / (y + .05); };
    const ink = ratio(colour, '#ffffff') >= ratio(colour, '#12141c') ? '#ffffff' : '#12141c';
    const L = document.getElementById('label'); L.textContent = label; L.style.background = colour; L.style.color = ink;
    document.getElementById('bar').style.background = `linear-gradient(90deg, ${colour}, #764ba2)`;
    document.getElementById('glow').style.background = colour;
    document.getElementById('sub').textContent = sub || '';
    const T = document.getElementById('title'); T.textContent = title;
    const room = sub ? 250 : 300;
    for (let size = 76; size >= 36; size -= 2) {
      T.style.fontSize = size + 'px';
      if (T.scrollHeight <= room) break;
    }
    if (T.scrollHeight > room) {          // still too long at the smallest size: trim on a word
      let words = title.split(' ');
      while (words.length > 3 && T.scrollHeight > room) { words.pop(); T.textContent = words.join(' ') + '…'; }
    }
  }, c);
  await page.screenshot({ path: path.join(ROOT, c.card), type: 'jpeg', quality: 84 });
  if (++n % 100 === 0) console.log(`  ${n} / ${todo.length}`);
}
await browser.close();
fs.unlinkSync(tmp);
console.log(`drew ${n} cards; ${cards.length} in all; ${removed} orphans removed`);
