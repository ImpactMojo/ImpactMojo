/**
 * Contract test for /api/pack-content and the split that feeds it.
 *
 * The paid Practice Pack modules are served by netlify/functions/pack-content.mjs
 * and nowhere else. Two failures would be silent: a page that still carries a
 * paid panel (the content is free again, and every check on the function
 * passes), and a function that answers without checking the profile on the
 * server. Both are asserted here, against a mocked Supabase.
 *
 * Run: node scripts/test-pack-content.mjs
 */
import fs from 'node:fs';
import { execFileSync } from 'node:child_process';
import vm from 'node:vm';

process.env.SUPABASE_SERVICE_ROLE_KEY = 'service-key-for-tests';
const G = await import(new URL('../netlify/lib/guard.mjs', import.meta.url));
G.setStoreFactory(async () => { const m = new Map(); return { get: async (k) => m.get(k) ?? null, set: async (k, v) => { m.set(k, v); } }; });
const F = await import(new URL('../netlify/functions/pack-content.mjs', import.meta.url));

let pass = 0, fail = 0;
const ck = (n, c) => { c ? (pass++, console.log('  PASS ' + n)) : (fail++, console.log('  FAIL ' + n)); };

console.log('hasAccess');
ck('no profile is refused', !F.hasAccess(null, 'tor-writing'));
ck('explorer is refused', !F.hasAccess({ subscription_tier: 'explorer' }, 'tor-writing'));
ck('practitioner is allowed', F.hasAccess({ subscription_tier: 'practitioner', subscription_status: 'active' }, 'tor-writing'));
ck('organization is allowed', F.hasAccess({ subscription_tier: 'organization' }, 'tor-writing'));
ck('lapsed practitioner is refused', !F.hasAccess({ subscription_tier: 'practitioner', subscription_status: 'cancelled' }, 'tor-writing'));
ck('per-pack grant (array) is allowed', F.hasAccess({ subscription_tier: 'explorer', resource_grants: ['tor-writing'] }, 'tor-writing'));
ck('grant for another pack is refused', !F.hasAccess({ subscription_tier: 'explorer', resource_grants: ['donor-reporting'] }, 'tor-writing'));
ck('per-pack grant (object) is allowed', F.hasAccess({ resource_grants: { 'tor-writing': true } }, 'tor-writing'));
ck('site admin is allowed', F.hasAccess({ role: 'admin', subscription_tier: 'explorer' }, 'tor-writing'));

// ---- handler, against a mocked Supabase ----------------------------------
let profile = null, userOk = true, storageOk = true, calls = [];
globalThis.fetch = async (url, opts = {}) => {
  url = String(url); calls.push(url);
  if (url.endsWith('/auth/v1/user')) return userOk ? new Response(JSON.stringify({ id: 'u-1' }), { status: 200 }) : new Response('{}', { status: 401 });
  if (url.includes('/rest/v1/profiles')) return new Response(JSON.stringify(profile ? [profile] : []), { status: 200 });
  if (url.includes('/storage/v1/object/products/practice-packs/')) return storageOk ? new Response(JSON.stringify({ panels: { 2: '<p>paid</p>' } }), { status: 200 }) : new Response('no', { status: 404 });
  return new Response('unexpected', { status: 500 });
};
const call = (slug, headers = {}) => F.default(new Request('https://www.impactmojo.in/api/pack-content?slug=' + slug, { headers: { Origin: 'https://www.impactmojo.in', ...headers } }), { ip: '1.2.3.4' });
const AUTH = { Authorization: 'Bearer token-1' };

console.log('handler');
let r = await call('tor-writing');
ck('no token is 401', r.status === 401);
r = await call('not-a-pack', AUTH);
ck('unknown slug is 404', r.status === 404);
r = await F.default(new Request('https://www.impactmojo.in/api/pack-content?slug=tor-writing', { headers: { Origin: 'https://evil.example', ...AUTH } }), { ip: '1.2.3.4' });
ck('other origin is 403', r.status === 403);
userOk = false; r = await call('tor-writing', AUTH);
ck('invalid session is 401', r.status === 401);
userOk = true; profile = { subscription_tier: 'explorer' }; calls = [];
r = await call('tor-writing', AUTH);
ck('explorer gets 403', r.status === 403);
ck('storage not read for a refused reader', !calls.some((u) => u.includes('/storage/')));
profile = { subscription_tier: 'practitioner', subscription_status: 'active' };
r = await call('tor-writing', AUTH);
const body = await r.json();
ck('practitioner gets 200', r.status === 200);
ck('panels returned', body.panels && body.panels['2'] === '<p>paid</p>');
ck('response is not cached', (r.headers.get('cache-control') || '').includes('no-store'));
storageOk = false; r = await call('tor-writing', AUTH);
ck('missing content is 502, not 200', r.status === 502);

// ---- the pages carry no paid panel ---------------------------------------
console.log('pages');
const out = execFileSync('python3', ['scripts/practice-packs/split-gated.py', '--check'], { encoding: 'utf8' });
ck('split-gated --check passes', out.startsWith('PASS'));
const dirs = fs.readdirSync('practice-packs', { withFileTypes: true }).filter((d) => d.isDirectory()).map((d) => d.name);
ck('function allowlist matches the pack folders', dirs.length === F.PACKS.size && dirs.every((d) => F.PACKS.has(d)));
for (const d of dirs) {
  const s = fs.readFileSync(`practice-packs/${d}/index.html`, 'utf8');
  if (!s.includes('type="text/x-im-pack"') || !s.includes('/js/practice-pack-gate.js')) ck(`${d} defers its script to the gate`, false);
  // check-inline-js.mjs skips this script type, so parse it here.
  const m = s.match(/<script type="text\/x-im-pack" id="im-pack-js">([\s\S]*?)<\/script>/);
  try { new vm.Script(m ? m[1] : 'throw 0'); } catch (e) { ck(`${d} pack script parses (${e.message})`, false); }
}
ck('every pack defers its script to the gate', true);

console.log(`\n${fail ? 'FAIL' : 'PASS'} - ${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
