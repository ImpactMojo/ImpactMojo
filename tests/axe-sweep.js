/**
 * Accessibility sweep over every page on the site.
 *
 * tests/axe-accessibility.js audits a short list of pages in four variants on
 * every pull request. A list kept by hand is how pages escaped every audit
 * here: the law guides, the 24 pages whose heading the site chrome removed and
 * the 99 pages with a serious contrast failure found on 2026-10-13 were in no
 * list. This script finds the pages itself, so a page is audited because it
 * exists.
 *
 * What it checks, per page, in two variants (light at 390x844, dark at
 * 1280x900, which covers both themes and both widths):
 *   - axe-core WCAG 2.1 AA, serious and critical only
 *   - horizontal overflow on a phone (the page scrolls sideways)
 *
 * The site carried known failures when this was written, so the result is
 * compared against tests/a11y-baseline.json, one entry per page, variant and
 * rule. A failure not in the baseline fails the run. A baseline entry that no
 * longer fails is reported, and `--update` rewrites the baseline, so the list
 * only shrinks. Never add an entry by hand to make a run pass.
 *
 * Usage:
 *   node tests/axe-sweep.js                    # every page, server on :8080
 *   AXE_SHARD=2/8 node tests/axe-sweep.js      # the second of eight shards
 *   node tests/axe-sweep.js --update           # rewrite the baseline (whole run only)
 *   AXE_PAGES="a.html b/c.html" node tests/axe-sweep.js
 */
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const puppeteer = require('puppeteer');

const ROOT = path.resolve(__dirname, '..');
const BASE_URL = process.env.AXE_SERVER_URL || 'http://localhost:8080';
const BASELINE = path.join(__dirname, 'a11y-baseline.json');
const UPDATE = process.argv.includes('--update');
const CONCURRENCY = Number(process.env.AXE_CONCURRENCY || 4);
const SERIOUS = new Set(['serious', 'critical']);

// Pages that are not reader-facing, or are not ours to fix.
const SKIP = [
  /^Backups\//, /^node_modules\//, /^docs\//, /^tests\//, /^scripts\//,
  /^supabase\//, /^netlify\//, /^mcp-server\//, /^\.github\//,
  /^admin\//,                 // Decap CMS and internal dashboards
  /^templates?\//, /PAGE-TEMPLATE\.html$/,
  /^google[0-9a-f]+\.html$/,  // search console verification
  /^email-templates\//,       // read by mail clients, not browsers
];

const VARIANTS = [
  { name: 'light-390', theme: 'light', width: 390, height: 844 },
  { name: 'dark-1280', theme: 'dark', width: 1280, height: 900 },
];

function allPages() {
  if (process.env.AXE_PAGES) return process.env.AXE_PAGES.split(/\s+/).filter(Boolean);
  const out = execSync('git ls-files -z -- "*.html"', { cwd: ROOT, maxBuffer: 64 << 20 }).toString();
  return out.split('\0').filter(Boolean).filter((p) => !SKIP.some((re) => re.test(p))).sort();
}

function shard(list) {
  const m = /^(\d+)\/(\d+)$/.exec(process.env.AXE_SHARD || '');
  if (!m) return list;
  const [i, n] = [Number(m[1]), Number(m[2])];
  return list.filter((_, k) => k % n === i - 1);
}

const urlFor = (p) => BASE_URL + '/' + p.split('/').map(encodeURIComponent).join('/');

async function audit(browser, pagePath, variant) {
  const page = await browser.newPage();
  try {
    await page.setViewport({ width: variant.width, height: variant.height });
    const go = async (waitUntil) => {
      let res = await page.goto(urlFor(pagePath), { waitUntil, timeout: 45000 });
      await page.evaluate((t) => { try { localStorage.setItem('im-theme', t); } catch (e) {} }, variant.theme);
      res = await page.reload({ waitUntil, timeout: 45000 });
      if (res && res.status() >= 400) throw new Error('HTTP ' + res.status());
    };
    try { await go('networkidle2'); } catch (e) {
      if (/HTTP \d+/.test(e.message)) throw e;
      await go('domcontentloaded');
    }
    await new Promise((r) => setTimeout(r, 600));
    await page.evaluate(require('axe-core').source);
    const res = await page.evaluate(() => axe.run(
      { exclude: [['[class^="userway_"]'], ['#uwy'], ['.introjs-tooltip'], ['.introjs-overlay'], ['.introjs-helperLayer']] },
      { runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'] }, resultTypes: ['violations'] },
    ));
    const fails = {};
    for (const v of res.violations) {
      if (!SERIOUS.has(v.impact)) continue;
      fails[v.id] = { n: v.nodes.length, help: v.help, target: v.nodes[0] && v.nodes[0].target.join(' ') };
    }
    if (variant.width < 500) {
      const over = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
      if (over > 2) fails['horizontal-overflow'] = { n: 1, help: `page is ${over}px wider than a 390px phone`, target: 'html' };
    }
    return { fails };
  } catch (e) {
    return { error: e.message.slice(0, 160) };
  } finally {
    await page.close().catch(() => {});
  }
}

async function main() {
  const pages = shard(allPages());
  const baseline = fs.existsSync(BASELINE) ? JSON.parse(fs.readFileSync(BASELINE, 'utf8')) : {};
  const launch = { headless: true, args: ['--no-sandbox', '--disable-setuid-sandbox'] };
  if (process.env.AXE_CHROME) launch.executablePath = process.env.AXE_CHROME;
  if (process.env.AXE_PROXY) launch.args.push('--proxy-server=' + process.env.AXE_PROXY, '--proxy-bypass-list=localhost;127.0.0.1', '--ignore-certificate-errors');
  const browser = await puppeteer.launch(launch);

  const jobs = [];
  for (const p of pages) for (const v of VARIANTS) jobs.push([p, v]);
  console.log(`Accessibility sweep: ${pages.length} pages, ${jobs.length} renders${process.env.AXE_SHARD ? ', shard ' + process.env.AXE_SHARD : ''}`);

  const found = {}; const errors = [];
  let next = 0, done = 0;
  async function worker() {
    while (next < jobs.length) {
      const [p, v] = jobs[next++];
      const r = await audit(browser, p, v);
      done++;
      if (done % 100 === 0) console.log(`  ${done} / ${jobs.length}`);
      if (r.error) { errors.push(`${p} [${v.name}]: ${r.error}`); continue; }
      for (const [rule, info] of Object.entries(r.fails)) {
        ((found[p] = found[p] || {})[v.name] = found[p][v.name] || {})[rule] = info;
      }
    }
  }
  await Promise.all(Array.from({ length: CONCURRENCY }, worker));
  await browser.close();

  const fresh = []; const cleared = [];
  for (const [p, vs] of Object.entries(found)) for (const [v, rules] of Object.entries(vs)) for (const rule of Object.keys(rules)) {
    if (!(baseline[p] && baseline[p][v] && baseline[p][v].includes(rule))) fresh.push([p, v, rule, rules[rule]]);
  }
  const inRun = new Set(pages);
  for (const [p, vs] of Object.entries(baseline)) {
    if (!inRun.has(p)) continue;
    for (const [v, rules] of Object.entries(vs)) for (const rule of rules) {
      if (!(found[p] && found[p][v] && found[p][v][rule])) cleared.push([p, v, rule]);
    }
  }

  if (errors.length) {
    console.log(`\n${errors.length} render(s) could not be audited:`);
    errors.slice(0, 40).forEach((e) => console.log('  ' + e));
  }
  if (cleared.length) {
    console.log(`\n${cleared.length} known failure(s) no longer fail. Run with --update to take them off the baseline:`);
    cleared.slice(0, 60).forEach(([p, v, r]) => console.log(`  ${p} [${v}] ${r}`));
  }
  if (fresh.length) {
    console.log(`\n${fresh.length} NEW failure(s), not in tests/a11y-baseline.json:`);
    fresh.forEach(([p, v, r, i]) => console.log(`  ${p} [${v}] ${r} (${i.n}): ${i.help}${i.target ? '  e.g. ' + i.target : ''}`));
  }

  if (UPDATE) {
    if (process.env.AXE_SHARD || process.env.AXE_PAGES) { console.error('--update needs a whole run, not a shard or a page list'); process.exit(2); }
    if (errors.length) { console.error('--update refused: some pages could not be audited, so the baseline would be incomplete'); process.exit(2); }
    const out = {};
    for (const p of Object.keys(found).sort()) {
      out[p] = {};
      for (const v of Object.keys(found[p]).sort()) out[p][v] = Object.keys(found[p][v]).sort();
    }
    fs.writeFileSync(BASELINE, JSON.stringify(out, null, 1) + '\n');
    const n = Object.values(out).reduce((a, vs) => a + Object.values(vs).reduce((b, r) => b + r.length, 0), 0);
    console.log(`\nWrote ${BASELINE}: ${Object.keys(out).length} pages, ${n} known failures.`);
    return;
  }
  // A page that could not be rendered was not audited; that is a failure, not a pass.
  const bad = fresh.length + errors.length;
  console.log(bad ? `\nFAIL - ${fresh.length} new failure(s), ${errors.length} page(s) not audited` : `\nPASS - no new failures across ${jobs.length} renders`);
  process.exit(bad ? 1 : 0);
}

main().catch((e) => { console.error(e); process.exit(1); });
