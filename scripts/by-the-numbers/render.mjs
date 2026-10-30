#!/usr/bin/env node
// Draw the By the numbers cards listed in data/by-the-numbers/cards.json.
//
//   python3 scripts/by-the-numbers/build.py   # computes what each card says
//   node scripts/by-the-numbers/render.mjs    # draws the missing ones, deletes orphans
//
// Each card is 1080x1350, the portrait size LinkedIn and Instagram show whole
// in a feed. The file name carries a hash of what the card shows, so this only
// draws a card whose figures changed, and a stale image is never served under
// a current name. Needs playwright-core and a Chromium (CHROME, as in
// render-social-cards.mjs).
import { chromium } from 'playwright-core';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const cards = JSON.parse(fs.readFileSync(path.join(ROOT, 'data', 'by-the-numbers', 'cards.json'), 'utf8'));
const OUT = path.join(ROOT, 'assets', 'by-the-numbers');
const CHROME = process.env.CHROME || '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell';
const FONTS = pathToFileURL(path.join(ROOT, 'assets', 'fonts')).href;
const LOGO = pathToFileURL(path.join(ROOT, 'assets', 'images', 'ImpactMojo Logo.png')).href;

fs.mkdirSync(OUT, { recursive: true });
const wanted = new Set(cards.map(c => path.basename(c.image)));
let removed = 0;
for (const f of fs.readdirSync(OUT)) {
  if (f.endsWith('.png') && !wanted.has(f)) { fs.unlinkSync(path.join(OUT, f)); removed++; }
}
const todo = cards.filter(c => process.env.FORCE || !fs.existsSync(path.join(ROOT, c.image)));
if (!todo.length) { console.log(`all ${cards.length} cards present; ${removed} orphans removed`); process.exit(0); }

const esc = s => String(s).replace(/[&<>"]/g, ch => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[ch]));

function bars(chart) {
  // One bar per item, in the card's order, height on a shared scale. The
  // highlighted items are named in a row above the bars, with a line down to
  // their bar, so a short bar's label never sits on its neighbours. A chart of
  // eight bars or fewer names every bar underneath instead, with its value.
  const fmt = v => (chart.prefix || '') + Number(v).toFixed(chart.decimals ?? 0).replace(/\B(?=(\d{3})+(?!\d))/g, ',') + (chart.suffix || '');
  const few = chart.bars.length <= 8;
  const W = 920, TOP = few ? 10 : 40, H = 290, n = chart.bars.length, gap = few ? 28 : 6;
  const bw = (W - gap * (n - 1)) / n;
  const max = Math.max(...chart.bars.map(b => b[1]));
  const hi = new Set(chart.highlight);
  let g = '', labels = '';
  chart.bars.forEach(([name, v], i) => {
    const h = Math.max(3, (v / max) * (H - TOP - 20));
    const x = i * (bw + gap), y = H - h;
    const on = hi.has(name);
    g += `<rect x="${x.toFixed(1)}" y="${y.toFixed(1)}" width="${bw.toFixed(1)}" height="${h.toFixed(1)}" rx="3" fill="${on ? '#B45309' : '#94A3B8'}"/>`;
    const cx = x + bw / 2;
    if (few) {
      labels += `<text x="${cx.toFixed(1)}" y="${(y - 10).toFixed(1)}" text-anchor="middle" font-size="24" font-weight="700" fill="${on ? '#7C2D12' : '#334155'}">${esc(fmt(v))}</text>`;
      labels += `<text x="${cx.toFixed(1)}" y="${H + 30}" text-anchor="middle" font-size="20" font-weight="600" fill="#475569">${esc(name)}</text>`;
    } else if (on) {
      const anchor = i < n / 2 ? 'start' : 'end';
      const lx = anchor === 'start' ? x : x + bw;
      labels += `<text x="${lx.toFixed(1)}" y="24" text-anchor="${anchor}" font-size="22" font-weight="700" fill="#7C2D12">${esc(name + ' ' + fmt(v))}</text>`;
      labels += `<line x1="${cx.toFixed(1)}" y1="34" x2="${cx.toFixed(1)}" y2="${(y - 4).toFixed(1)}" stroke="#7C2D12" stroke-width="2"/>`;
    }
  });
  const SH = few ? H + 40 : H;
  return `<svg width="${W}" height="${SH}" viewBox="0 0 ${W} ${SH}" xmlns="http://www.w3.org/2000/svg" font-family="Inter">${g}${labels}
    <line x1="0" y1="${H}" x2="${W}" y2="${H}" stroke="#CBD5E1" stroke-width="2"/></svg>`;
}

// Keep a year range such as 2022-23 on one line.
const keep = s => esc(s).replace(/(\d{4}-\d{2})/g, '<span style="white-space:nowrap">$1</span>');

function card(c) {
  const [a, b] = c.pair;
  const src = c.sources.map(s => s.short || s.name.split(',')[0]).join('; ');
  return `<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:Inter;src:url('${FONTS}/inter-var.woff2') format('woff2');font-weight:100 900}
@font-face{font-family:Inter;src:url('${FONTS}/inter-var-ext.woff2') format('woff2');font-weight:100 900;unicode-range:U+0100-024F,U+20A0-20CF}
@font-face{font-family:Amaranth;src:url('${FONTS}/amaranth-700.woff2') format('woff2');font-weight:700}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;background:#FBF8F3;overflow:hidden}
#c{position:relative;width:1080px;height:1350px;font-family:Inter,sans-serif;color:#0F172A;padding:70px 80px 56px;display:flex;flex-direction:column}
#bar{position:absolute;left:0;top:0;right:0;height:14px;background:linear-gradient(90deg,#667eea,#764ba2)}
#top{display:flex;justify-content:space-between;align-items:center}
#label{font-size:24px;font-weight:800;letter-spacing:3px;text-transform:uppercase;color:#4C1D95;border:3px solid #4C1D95;border-radius:10px;padding:10px 18px}
#topic{font-size:24px;font-weight:600;color:#475569}
h1{font-family:Amaranth,Inter,sans-serif;font-weight:700;font-size:56px;line-height:1.12;margin-top:44px;letter-spacing:-.5px;text-wrap:balance}
#sub{font-size:28px;line-height:1.4;color:#334155;margin-top:22px}
#pair{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:40px}
.p{border-radius:16px;padding:24px 26px}
.p1{background:#FEF3C7}.p2{background:#E0E7FF}
.p .l{font-size:22px;font-weight:600;line-height:1.3;color:#334155}
.p .v{font-family:Amaranth,Inter,sans-serif;font-weight:700;font-size:84px;line-height:1;margin-top:14px}
.p1 .v{color:#92400E}.p2 .v{color:#3730A3}
.p .u{font-size:22px;color:#475569;margin-top:6px}
#chart{margin-top:34px}
#chart .t{font-size:20px;font-weight:600;color:#475569;margin-bottom:14px}
#chart .ax{display:flex;justify-content:space-between;font-size:18px;color:#64748B;margin-top:8px}
#note{font-size:19px;line-height:1.45;color:#475569;margin-top:auto;padding-top:18px}
#foot{display:flex;justify-content:space-between;align-items:center;margin-top:20px;padding-top:18px;border-top:2px solid #E2E8F0}
#src{font-size:16px;color:#64748B;max-width:640px;line-height:1.4}
#brand{display:flex;align-items:center;gap:12px;font-size:24px;font-weight:800}
#brand img{width:44px;height:44px}
#brand span{display:block;font-size:17px;font-weight:600;color:#4C1D95}
</style></head><body><div id="c"><div id="bar"></div>
<div id="top"><div id="label">${esc(c.series)}</div><div id="topic">${esc(c.topic)}</div></div>
<h1>${keep(c.headline)}</h1>
<div id="sub">${keep(c.sub)}</div>
<div id="pair">
 <div class="p p1"><div class="l">${esc(a.label)}</div><div class="v">${esc(a.value)}</div><div class="u">${esc(a.unit)}</div></div>
 <div class="p p2"><div class="l">${esc(b.label)}</div><div class="v">${esc(b.value)}</div><div class="u">${esc(b.unit)}</div></div>
</div>
<div id="chart"><div class="t">${esc(c.chart.title)}</div>${bars(c.chart)}
 ${c.chart.axis ? `<div class="ax"><span>${esc(c.chart.axis[0])}</span><span>${esc(c.chart.axis[1])}</span></div>` : ''}</div>
<div id="note">${esc(c.note)}</div>
<div id="foot"><div id="src">Sources: ${esc(src)}. Working and every state at impactmojo.in/by-the-numbers/</div>
<div id="brand"><img src="${LOGO}" alt=""><div>ImpactMojo<span>impactmojo.in</span></div></div></div>
</div></body></html>`;
}

const browser = await chromium.launch({ executablePath: CHROME });
const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
const tmp = path.join(OUT, '_card.html');
for (const c of todo) {
  fs.writeFileSync(tmp, card(c));
  await page.goto(pathToFileURL(tmp).href);
  await page.evaluate(() => document.fonts.ready);
  const over = await page.evaluate(() => {
    const el = document.getElementById('c');
    return el.scrollHeight > 1350 || [...el.children].some(n => n.getBoundingClientRect().bottom > 1350);
  });
  if (over) { console.error(`FAIL - ${c.id}: the content runs past the bottom of the card`); process.exitCode = 1; continue; }
  await page.screenshot({ path: path.join(ROOT, c.image), type: 'png' });
  console.log(`drew ${c.image}`);
}
fs.unlinkSync(tmp);
await browser.close();
console.log(`${removed} orphans removed`);
