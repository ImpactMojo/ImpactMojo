/**
 * Guard: no bare text node stranded in a grid or flex container.
 *
 * Why this exists
 * ---------------
 * A text node written directly inside a grid container is not part of any
 * element, so CSS wraps it in an *anonymous grid item* and auto-places it like
 * any other cell. On /fundamentals/results-chain.html the legend was emitted as
 *
 *     <li><span class="rc-key"></span><b>Counted continuously</b> A public
 *     management information system, updated daily or monthly, at the level of
 *     the individual transaction.</li>
 *
 * inside `.rc-legend li { display: grid; grid-template-columns: 26px 1fr }`.
 * That is three grid items, not two: the note went to row 2, column 1 — the
 * 26px swatch track, stretched to the longest unbreakable word — and rendered
 * about 75px wide and up to 535px tall. One word per line, four rows of it, at
 * every viewport width, live from the day the page shipped (#1072).
 *
 * Nothing caught it and nothing was going to. The markup is valid, the text is
 * all present and in the right order, the contrast is fine and so are the tap
 * targets, so axe passed 64 of 64 variants over it and pa11y 23 of 23 pages,
 * twice. Neither has an opinion about a paragraph laid out four words tall. It
 * was found by a person looking at the page on a phone.
 *
 * What is and is not a fault
 * --------------------------
 * A bare text node beside an element is *usually fine* and this repo is full of
 * deliberate cases: `.chip`, `.cat` and `#rcOrder li` all put a swatch or a
 * number next to a bare label in a flex row, and the anonymous item lands
 * beside it on one line, which is what was wanted. So the mere presence of one
 * is not the signal, and a lint rule on the markup would be noise.
 *
 * What separates the two is measurable. A stranded item is narrow relative to
 * its container *and* many line-heights tall, because it has been squeezed into
 * a track sized for something else. The deliberate ones are a single line and
 * take most of their container's width. The thresholds below sit far from both
 * populations: measured, the four broken rows were 7% of container width and
 * 8 to 17 lines tall; every deliberate case on the site is 1 line and 60% or
 * more of its container.
 *
 * The page list is read from the filesystem rather than hardcoded, because a
 * page that joins the site should join its guards without anyone remembering
 * to add it. rules/testing.md item 15 records what a fixed list costs.
 *
 * Usage:
 *   node tests/stray-grid-text.js                    # expects a server on :8080
 *   SGT_SERVER_URL=http://localhost:8199 node tests/stray-grid-text.js
 */

const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

const BASE = process.env.SGT_SERVER_URL || 'http://localhost:8080';
const ROOT = path.resolve(__dirname, '..');

// A stranded item is narrow AND tall. Both must hold, so a one-line label that
// happens to be short does not trip it, and neither does a wide paragraph.
const MAX_WIDTH_SHARE = 0.5;   // of the container's content width
const MAX_LINES = 3;           // rendered height, in multiples of its line-height

// Two widths. The defect that prompted this was width-independent, but a track
// collapse can easily be one or the other, and both runs are cheap.
const VIEWPORTS = [
  { label: 'mobile', width: 390, height: 900 },
  { label: 'desktop', width: 1280, height: 1000 },
];

function pagesUnder(dir) {
  return fs.readdirSync(path.join(ROOT, dir))
    .filter((f) => f.endsWith('.html'))
    .sort()
    .map((f) => `/${dir}/${f}`);
}

// The JS-rendered diagram libraries. These are the pages that build their own
// markup at runtime, which is where this mistake is made: a template string is
// a very easy place to leave a text node loose.
const PAGES = [...pagesUnder('fundamentals'), ...pagesUnder('theories')];

async function strandedOn(page) {
  return page.evaluate((cfg) => {
    const out = [];
    for (const el of document.querySelectorAll('*')) {
      const cs = getComputedStyle(el);
      if (!/grid|flex/.test(cs.display)) continue;
      if (!el.children.length) continue;              // no elements to be placed against

      for (const node of el.childNodes) {
        if (node.nodeType !== 3 || !node.textContent.trim()) continue;

        const range = document.createRange();
        range.selectNodeContents(node);
        const r = range.getBoundingClientRect();
        if (r.width < 1 || r.height < 1) continue;    // not rendered; nothing to judge

        const host = el.getBoundingClientRect();
        const inner = host.width -
          parseFloat(cs.paddingLeft || 0) - parseFloat(cs.paddingRight || 0);
        if (inner < 1) continue;

        // line-height resolves to "normal" on some elements; fall back to the
        // usual ~1.2x rather than dividing by NaN and reporting nonsense.
        let lh = parseFloat(cs.lineHeight);
        if (!isFinite(lh) || lh <= 0) lh = parseFloat(cs.fontSize) * 1.2;

        const share = r.width / inner;
        const lines = r.height / lh;
        if (share < cfg.MAX_WIDTH_SHARE && lines > cfg.MAX_LINES) {
          out.push({
            sel: el.tagName.toLowerCase() +
                 (el.className ? '.' + String(el.className).trim().split(/\s+/).join('.') : ''),
            display: cs.display,
            text: node.textContent.trim().slice(0, 48),
            w: Math.round(r.width),
            h: Math.round(r.height),
            inner: Math.round(inner),
            share: +share.toFixed(2),
            lines: +lines.toFixed(1),
          });
        }
      }
    }
    return out;
  }, { MAX_WIDTH_SHARE, MAX_LINES });
}

(async () => {
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-dev-shm-usage'],
  });
  const failures = [];
  let checked = 0;

  for (const p of PAGES) {
    for (const vp of VIEWPORTS) {
      const page = await browser.newPage();
      await page.setViewport({ width: vp.width, height: vp.height });

      // Serve nothing but our own origin. The only off-site requests these
      // pages make are Supabase and the analytics tag, and neither can move a
      // box; the fonts are self-hosted under /assets/fonts, so the text this
      // measures is laid out in the real typeface either way. Cutting them out
      // makes the guard deterministic and independent of third-party latency,
      // which matters: an unreachable CDN hangs rather than fails, so without
      // this the run times out on a network problem and reports it as a layout
      // problem.
      await page.setRequestInterception(true);
      page.on('request', (req) => {
        if (req.url().startsWith(BASE)) req.continue();
        else req.abort();
      });

      try {
        // domcontentloaded, not load: nothing this measures waits on `load`.
        await page.goto(BASE + p, { waitUntil: 'domcontentloaded', timeout: 30000 });
        await new Promise((r) => setTimeout(r, 1200));   // renderers draw on DOMContentLoaded
        await page.evaluate(() => (document.fonts ? document.fonts.ready : null)).catch(() => {});

        for (const s of await strandedOn(page)) {
          failures.push(
            `${p} at ${vp.label}: text stranded in ${s.sel} (display:${s.display}) — ` +
            `rendered ${s.w}x${s.h}, ${Math.round(s.share * 100)}% of the container's ${s.inner}px and ` +
            `${s.lines} lines tall: "${s.text}…". ` +
            `A bare text node in a grid or flex container becomes an anonymous item and is ` +
            `placed like a cell. Wrap it in an element of its own.`
          );
        }
        checked++;
      } finally {
        await page.close();
      }
    }
  }

  await browser.close();

  if (failures.length) {
    console.error('\nFAIL — text stranded in a grid or flex container\n');
    failures.forEach((f) => console.error('  ' + f));
    console.error('');
    process.exit(1);
  }
  console.log(`PASS — no stranded text across ${PAGES.length} pages x ${VIEWPORTS.length} widths ` +
              `(${checked} renders).`);
})().catch((err) => {
  console.error('FAIL — ' + (err && err.stack ? err.stack : err));
  process.exit(1);
});
