#!/usr/bin/env node
// The Dataverse Spotlight picks three entries a day. This runs the page's own
// pickSpotlight() (cut out between the spotlight markers) against the real
// data, so the rules cannot drift from the code that ships.
import fs from 'node:fs';
import vm from 'node:vm';
const page = fs.readFileSync('dataverse.html', 'utf8');
const m = page.match(/\/\* spotlight:begin \*\/([\s\S]*?)\/\* spotlight:end \*\//);
if (!m) { console.error('FAIL: spotlight markers not found in dataverse.html'); process.exit(1); }
const ctx = {};
vm.createContext(ctx);
vm.runInContext(m[1] + ';this.pickSpotlight=pickSpotlight;this.istDay=istDay;', ctx);
const dv = JSON.parse(fs.readFileSync('data/dataverse.json', 'utf8'));
const all = dv.categories.flatMap(c => c.items);
const fails = [];
const ok = (c, msg) => { if (!c) fails.push(msg); };
const DAY = 86400000;
const t0 = Date.parse('2026-11-19T06:00:00Z');

// 1. Every day of a year: three distinct live entries, same answer on a repeat call.
const seenAll = new Set();
for (let d = 0; d < 365; d++) {
  const now = t0 + d * DAY;
  const a = ctx.pickSpotlight(all, now), b = ctx.pickSpotlight(all, now + 3600000);
  ok(a.length === 3, `day ${d}: ${a.length} picks`);
  ok(new Set(a.map(x => x.item.id)).size === a.length, `day ${d}: duplicate pick`);
  ok(a.every(x => x.item.status === 'live'), `day ${d}: a non-live entry was picked`);
  ok(JSON.stringify(a.map(x => x.item.id)) === JSON.stringify(b.map(x => x.item.id)), `day ${d}: not stable within the day`);
  a.forEach(x => seenAll.add(x.item.id));
}
// 2. The rotation reaches a large share of the catalogue over a year.
ok(seenAll.size > 200, `only ${seenAll.size} distinct entries in a year`);
// 3. New entries lead while they are recent, and stop leading after the window.
const fresh = all.filter(i => i.added && i.added >= '2026-11-13');
const today = ctx.pickSpotlight(all, t0);
ok(today.slice(0, 2).every(x => x.fresh && x.item.added), 'the first two picks today are not recent additions');
const later = ctx.pickSpotlight(all, t0 + 120 * DAY);
ok(later.every(x => !x.fresh), 'an entry is still marked New 120 days later');
// 4. No dated entries at all: still three picks from the rest.
const undated = all.map(i => { const c = { ...i }; delete c.added; return c; });
ok(ctx.pickSpotlight(undated, t0).length === 3, 'no picks when nothing is dated');
// 5. A bad date never counts as recent.
const bad = all.map(i => ({ ...i, added: 'soon' }));
ok(ctx.pickSpotlight(bad, t0).every(x => !x.fresh), 'a malformed date counted as recent');
// 6. Every `added` value is a real date, not in the future.
for (const i of all) if (i.added) {
  ok(/^\d{4}-\d{2}-\d{2}$/.test(i.added) && !isNaN(Date.parse(i.added)), `${i.id}: bad added date ${i.added}`);
  ok(i.added <= '2026-11-19' || Date.parse(i.added) <= Date.now() + DAY, `${i.id}: added date in the future`);
}
if (fails.length) { console.log('FAIL: Dataverse spotlight'); fails.slice(0, 20).forEach(f => console.log('  ' + f)); process.exit(1); }
console.log(`PASS: Dataverse spotlight (${all.length} entries, ${fresh.length} recent, ${seenAll.size} reached in 365 days)`);
