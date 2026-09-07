/**
 * Guard: site search is reachable on a phone.
 *
 * Why this exists
 * ---------------
 * js/search.js injected its button into `.nav-buttons`, and css/imx-main.css
 * sets that container to `display: none !important` below 768px. The button was
 * therefore created, inserted, and invisible: present in the DOM at 0x0, with
 * the right class and a working click handler, on every page using the legacy
 * navigation. The hamburger menu carried no search entry either, and Ctrl+K is
 * not something a phone offers. Site-wide search was unreachable on mobile and
 * nothing said so (#1062).
 *
 * Every desktop check passed throughout, which is the point. axe and pa11y
 * would not report it either: a zero-size element with a valid aria-label is a
 * layout outcome, not a WCAG violation. So this test does the one thing that
 * catches it — measures the affordance at a phone viewport and clicks it.
 *
 * It also asserts the two buttons are never both on screen. The desktop one and
 * the mobile one are shown by complementary media queries, and a mistake there
 * puts two search buttons in one bar rather than none.
 *
 * Usage:
 *   node tests/mobile-search.js                     # expects a server on :8080
 *   MS_SERVER_URL=http://localhost:8199 node tests/mobile-search.js
 */

const puppeteer = require('puppeteer');

const BASE = process.env.MS_SERVER_URL || 'http://localhost:8080';
const MOBILE = { width: 390, height: 800 };
const DESKTOP = { width: 1280, height: 900 };
const MIN_TAP = 32;      // tap-target floor, applied at the mobile viewport
const MIN_VISIBLE = 24;  // desktop: a pointer is precise, so only assert it is really there

// One page per navigation shape the site actually ships. index.html is the
// legacy nav (the one that broke); the others load js/site-chrome.js and get
// its own .im-sc-search.
const PAGES = [
  { path: '/index.html', nav: 'legacy' },
  { path: '/catalog.html', nav: 'chrome' },
  { path: '/theories/', nav: 'chrome' },
  { path: '/fundamentals/wheel.html', nav: 'chrome' },
];

const SEARCH_SELECTORS = ['.ims-nav-btn--m', '.ims-nav-btn:not(.ims-nav-btn--m)', '.im-sc-search'];

function box(page, selector) {
  return page.evaluate((sel) => {
    const el = document.querySelector(sel);
    if (!el) return null;
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const visible = cs.display !== 'none' && cs.visibility !== 'hidden' &&
                    parseFloat(cs.opacity) > 0.01 && r.width >= 1 && r.height >= 1;
    return { visible, w: Math.round(r.width), h: Math.round(r.height) };
  }, selector);
}

async function visibleSearchButtons(page) {
  const found = [];
  for (const sel of SEARCH_SELECTORS) {
    const b = await box(page, sel);
    if (b && b.visible) found.push({ sel, ...b });
  }
  return found;
}

(async () => {
  const failures = [];
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
  });

  for (const { path, nav } of PAGES) {
    for (const [label, viewport] of [['mobile', MOBILE], ['desktop', DESKTOP]]) {
      const page = await browser.newPage();
      await page.setViewport(viewport);
      // domcontentloaded, not load: these pages pull fonts and libraries from a
      // CDN, and waiting on those makes the test fail for the wrong reason on
      // any runner without outbound network.
      await page.goto(BASE + path, { waitUntil: 'domcontentloaded', timeout: 30000 });
      await new Promise((r) => setTimeout(r, 2000));   // search.js injects on DOMContentLoaded

      const shown = await visibleSearchButtons(page);

      if (shown.length === 0) {
        failures.push(`${path} at ${label}: no visible search button. ` +
                      `This is #1062: search unreachable.`);
      } else if (shown.length > 1) {
        failures.push(`${path} at ${label}: ${shown.length} search buttons visible at once ` +
                      `(${shown.map((s) => s.sel).join(', ')}). The media queries have drifted.`);
      } else {
        const b = shown[0];
        const floor = label === 'mobile' ? MIN_TAP : MIN_VISIBLE;
        if (b.w < floor || b.h < floor) {
          failures.push(`${path} at ${label}: search button is ${b.w}x${b.h}, ` +
                        `below the ${floor}px floor. A control that shrinks to a sliver ` +
                        `when its icon fails to load is the same defect as one that is hidden.`);
        }
        // The button existing is not the feature. Opening the modal is.
        //
        // Poll rather than sleep. On pages with the shared top bar, search.js is
        // not loaded until the button is clicked, so the modal appears after a
        // script fetch plus the search index; a fixed wait passes or fails by
        // how fast the runner is, which is a flaky test pretending to be a real
        // one. Eight seconds is generous and only ever spent on a genuine
        // failure.
        await page.click(b.sel);
        const deadline = Date.now() + 8000;
        let state = 'no modal in the DOM';
        while (Date.now() < deadline) {
          state = await page.evaluate(() => {
            const m = document.getElementById('impactmojo-search-modal');
            if (!m) return 'no modal in the DOM';
            if (!m.classList.contains('ims-open')) return 'modal did not open';
            const input = m.querySelector('input');
            if (!input) return 'modal has no input';
            return document.activeElement === input ? 'ok' : 'modal open but input not focused';
          });
          if (state === 'ok') break;
          await new Promise((r) => setTimeout(r, 250));
        }
        if (state !== 'ok') {
          failures.push(`${path} at ${label}: clicking ${b.sel} -> ${state}`);
        }
      }

      console.log(`  ${label.padEnd(7)} ${path.padEnd(28)} ` +
                  (shown.length ? shown.map((s) => `${s.sel} ${s.w}x${s.h}`).join(' + ') : 'NONE'));
      await page.close();
    }
    void nav;
  }

  await browser.close();

  if (failures.length) {
    console.error(`\nFAIL - ${failures.length} problem(s):`);
    failures.forEach((f) => console.error(`  - ${f}`));
    process.exit(1);
  }
  console.log(`\nPASS - one reachable search button on ${PAGES.length} page(s) at both viewports.`);
})().catch((err) => {
  console.error('FAIL - ' + err.message);
  process.exit(1);
});
