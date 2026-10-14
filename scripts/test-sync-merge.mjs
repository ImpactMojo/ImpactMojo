/**
 * Contract test for the account sync merge in js/auth.js and the streak read
 * in js/state-manager.js.
 *
 * Both defects were silent. A sync rebuilt the streak from four fields and
 * emptied the streak calendar (#1265). Notes were merged on `updatedAt` and
 * `timestamp`, which notes do not carry, so a conflict was decided by array
 * order and the list reordered on every sync (#1266).
 *
 * Run: node scripts/test-sync-merge.mjs
 */
import fs from 'node:fs';
import vm from 'node:vm';

let pass = 0, fail = 0;
const check = (n, c) => { c ? (pass++, console.log('  PASS', n)) : (fail++, console.log('  FAIL', n)); };

// --- the pure merge helpers, taken from js/auth.js -------------------------
const auth = fs.readFileSync(new URL('../js/auth.js', import.meta.url), 'utf8');
const m = auth.match(/\/\/ imx-merge-helpers:start([\s\S]*?)\/\/ imx-merge-helpers:end/);
if (!m) { console.log('FAIL merge helpers not found in js/auth.js'); process.exit(1); }
const { imxMergeStreak, imxMergeNotes } = new Function(m[1] + '; return { imxMergeStreak, imxMergeNotes };')();
check('mergeData uses imxMergeStreak', /merged\.streak_data = imxMergeStreak\(localData\.streak_data, cloudData\.streak_data\)/.test(auth));
check('mergeData uses imxMergeNotes', /merged\.notes = imxMergeNotes\(localData\.notes, cloudData\.notes\)/.test(auth));

// --- streak (#1265) --------------------------------------------------------
const local = { currentStreak: 3, longestStreak: 9, totalDays: 20, lastVisit: '2026-10-14',
  visitDates: ['2026-10-01', '2026-10-12', '2026-10-13', '2026-10-14'], celebratedMilestone: 3 };
// What an old sync left in the cloud: four fields, no dates.
const cloudOld = { currentStreak: 2, longestStreak: 5, lastVisit: '2026-10-13', totalVisits: 7 };
let s = imxMergeStreak(local, cloudOld);
check('visitDates survive a merge with a dateless cloud copy', JSON.stringify(s.visitDates) === JSON.stringify(local.visitDates));
check('totalDays survives', s.totalDays === 20);
check('celebratedMilestone survives', s.celebratedMilestone === 3);
check('best streak is the larger', s.longestStreak === 9);
check('current streak comes from the later visit', s.currentStreak === 3 && s.lastVisit === '2026-10-14');
check('totalVisits kept', s.totalVisits === 7);

// Two devices, each with part of the calendar.
const devA = { currentStreak: 2, longestStreak: 2, totalDays: 2, lastVisit: '2026-10-14', visitDates: ['2026-10-13', '2026-10-14'] };
const devB = { currentStreak: 3, longestStreak: 4, totalDays: 6, lastVisit: '2026-10-12', visitDates: ['2026-10-10', '2026-10-11', '2026-10-12', '2026-09-01'] };
s = imxMergeStreak(devA, devB);
check('visit dates are combined, unique and sorted',
  JSON.stringify(s.visitDates) === JSON.stringify(['2026-09-01', '2026-10-10', '2026-10-11', '2026-10-12', '2026-10-13', '2026-10-14']));
check('current streak counts the combined run of days', s.currentStreak === 5);
check('best streak is at least the current streak', s.longestStreak === 5);
check('total days is the larger of the stored totals and the dates', s.totalDays === 6);
check('the merge is symmetric in its counts', (() => { const r = imxMergeStreak(devB, devA); return r.currentStreak === 5 && r.longestStreak === 5 && r.totalDays === 6 && r.visitDates.length === 6; })());

// A broken streak stays broken.
s = imxMergeStreak({ currentStreak: 1, longestStreak: 8, lastVisit: '2026-10-14', visitDates: ['2026-10-14'] },
                   { currentStreak: 8, longestStreak: 8, lastVisit: '2026-10-05', visitDates: [] });
check('a later reset is not overridden by an older long run', s.currentStreak === 1 && s.longestStreak === 8);

// Old field names and empty input.
s = imxMergeStreak({ current: 4, longest: 6, lastDate: '2026-10-14' }, null);
check('old field names are normalised', s.currentStreak === 4 && s.longestStreak === 6 && s.lastVisit === '2026-10-14' && !('current' in s) && !('lastDate' in s));
s = imxMergeStreak(undefined, undefined);
check('empty input gives an empty streak', s.currentStreak === 0 && s.longestStreak === 0 && s.lastVisit === null && s.visitDates.length === 0);
check('visit dates are capped at 365',
  imxMergeStreak({ visitDates: Array.from({ length: 400 }, (_, i) => new Date(Date.UTC(2025, 0, 1) + i * 864e5).toISOString().slice(0, 10)) }, {}).visitDates.length === 365);

// --- notes (#1266) ---------------------------------------------------------
const nLocal = [
  { id: 'n1', title: 'Edited here', content: 'new', created: 1000, updated: 5000 },
  { id: 'n2', title: 'Local only', content: 'x', created: 3000, updated: 3000 },
  { id: 'n3', title: 'Older here', content: 'old', created: 1500, updated: 1500 }
];
const nCloud = [
  { id: 'n3', title: 'Edited on the other device', content: 'newer', created: 1500, updated: 6000 },
  { id: 'n1', title: 'Stale', content: 'old', created: 1000, updated: 2000 },
  { id: 'n4', title: 'Cloud only', content: 'y', created: 4000, updated: 4000 }
];
let n = imxMergeNotes(nLocal, nCloud);
check('newer local copy wins', n.find(x => x.id === 'n1').title === 'Edited here');
check('newer cloud copy wins', n.find(x => x.id === 'n3').title === 'Edited on the other device');
check('notes from both sides are kept, once each', n.length === 4);
check('ordered newest first by updated', n.map(x => x.id).join(',') === 'n3,n1,n4,n2');
check('the order is the same with the arguments swapped', imxMergeNotes(nCloud, nLocal).map(x => x.id).join(',') === 'n3,n1,n4,n2');
check('merging the result again changes nothing', JSON.stringify(imxMergeNotes(n, n)) === JSON.stringify(n));
n = imxMergeNotes([{ id: 'n1', title: 'local', updated: 10 }], [{ id: 'n1', title: 'cloud', updated: 10 }]);
check('on a tie the local copy wins', n.length === 1 && n[0].title === 'local');
n = imxMergeNotes([{ id: 'a', title: 'iso', updatedAt: '2026-10-14T00:00:00Z' }], [{ id: 'a', title: 'ms', updated: Date.parse('2026-10-01T00:00:00Z') }]);
check('an ISO updatedAt is compared as a time', n[0].title === 'iso');
n = imxMergeNotes([{ id: 'p', updated: 7 }, { id: 'q', updated: 7 }, { id: 'o', updated: 7 }], []);
check('equal times fall back to a fixed order', n.map(x => x.id).join(',') === 'o,p,q');
n = imxMergeNotes({ k1: { title: 'object format', updated: 2 } }, null);
check('the old object-keyed format is read', n.length === 1 && n[0].id === 'k1');

// --- js/state-manager.js keeps every streak field ---------------------------
const store = new Map();
const localStorage = {
  getItem: k => (store.has(k) ? store.get(k) : null), setItem: (k, v) => store.set(k, String(v)),
  removeItem: k => store.delete(k), key: i => Array.from(store.keys())[i], get length() { return store.size; }
};
const ctx = { window: {}, localStorage, console };
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(new URL('../js/state-manager.js', import.meta.url), 'utf8'), ctx);
const IMState = ctx.window.IMState;
store.set('impactmojo_streak', JSON.stringify(local));
let g = IMState.streak.get();
check('IMState.streak.get keeps visitDates, totalDays and celebratedMilestone',
  g.visitDates.length === 4 && g.totalDays === 20 && g.celebratedMilestone === 3 && g.currentStreak === 3);
check('getSyncableData carries the whole streak', IMState.getSyncableData().streak_data.visitDates.length === 4);
store.set('impactmojo_streak', JSON.stringify({ current: 2, longest: 4, lastDate: '2026-10-01' }));
g = IMState.streak.get();
check('IMState.streak.get still normalises old field names', g.currentStreak === 2 && g.longestStreak === 4 && g.lastVisit === '2026-10-01' && !('current' in g));
store.delete('impactmojo_streak');
check('IMState.streak.get with nothing stored gives the default', IMState.streak.get().currentStreak === 0);

console.log(`\n${pass} passed, ${fail} failed`);
console.log(fail ? 'FAIL - sync merge' : 'PASS - sync merge');
process.exit(fail ? 1 : 0);
