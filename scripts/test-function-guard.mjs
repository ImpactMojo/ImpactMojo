/**
 * Contract test for netlify/lib/guard.mjs and the functions that use it:
 * the Origin check, the Blobs rate limiter (with an in-memory store), the
 * constant-time comparison, and the limits on /api/translate,
 * /api/form-submit and the instructor-kit receipt in submission-created.
 *
 * Every one of these failures is silent in production: an open LLM proxy
 * still answers, an unlimited mail path still sends, a limiter that fails
 * open still returns 200. So each is asserted here.
 *
 * Run: node scripts/test-function-guard.mjs
 */
const guardUrl = new URL('../netlify/lib/guard.mjs', import.meta.url);
const G = await import(guardUrl);

let pass = 0, fail = 0;
const ck = (n, c) => { c ? (pass++, console.log('  PASS ' + n)) : (fail++, console.log('  FAIL ' + n)); };

// ---- in-memory Blobs ------------------------------------------------------
let mem = new Map();
let storeDown = false;
G.setStoreFactory(async () => {
  if (storeDown) throw new Error('blobs unavailable');
  return { get: async (k) => (mem.has(k) ? mem.get(k) : null), set: async (k, v) => { mem.set(k, v); } };
});
const reset = () => { mem = new Map(); storeDown = false; };

const req = (headers = {}, body = {}, url = 'https://www.impactmojo.in/api/x') =>
  new Request(url, { method: 'POST', headers: { 'Content-Type': 'application/json', ...headers }, body: JSON.stringify(body) });

// ---- originAllowed --------------------------------------------------------
console.log('originAllowed');
ck('www origin allowed', G.originAllowed(req({ Origin: 'https://www.impactmojo.in' })));
ck('apex origin allowed', G.originAllowed(req({ Origin: 'https://impactmojo.in' })));
ck('deploy preview allowed', G.originAllowed(req({ Origin: 'https://deploy-preview-1229--impactmojo.netlify.app' })));
ck('netlify production address allowed', G.originAllowed(req({ Origin: 'https://impactmojo.netlify.app' })));
ck('other site refused', !G.originAllowed(req({ Origin: 'https://evil.example' })));
ck('look-alike netlify site refused', !G.originAllowed(req({ Origin: 'https://impactmojo-evil.netlify.app' })));
ck('suffix trick refused', !G.originAllowed(req({ Origin: 'https://www.impactmojo.in.evil.example' })));
ck('http origin refused', !G.originAllowed(req({ Origin: 'http://www.impactmojo.in' })));
ck('null origin refused', !G.originAllowed(req({ Origin: 'null' })));
ck('localhost refused outside netlify dev', !G.originAllowed(req({ Origin: 'http://localhost:8888' })));
ck('no origin, same-origin fetch allowed', G.originAllowed(req({ 'Sec-Fetch-Site': 'same-origin' })));
ck('no origin, cross-site fetch refused', !G.originAllowed(req({ 'Sec-Fetch-Site': 'cross-site' })));
ck('no browser headers at all refused', !G.originAllowed(req()));

// ---- safeEqual ------------------------------------------------------------
console.log('safeEqual');
ck('equal strings match', G.safeEqual('k3y-value', 'k3y-value'));
ck('different strings do not', !G.safeEqual('k3y-value', 'k3y-valuf'));
ck('prefix does not match', !G.safeEqual('k3y', 'k3y-value'));
ck('empty does not match a key', !G.safeEqual('', 'k3y'));

// ---- rateLimit ------------------------------------------------------------
console.log('rateLimit');
reset();
const rl = (o) => G.rateLimit({ bucket: 't', id: '1.2.3.4', limit: 3, windowSec: 3600, ...o });
let r1 = await rl(), r2 = await rl(), r3 = await rl(), r4 = await rl();
ck('three calls inside the limit pass', r1.ok && r2.ok && r3.ok);
ck('fourth call is limited', !r4.ok && r4.reason === 'limited' && r4.retryAfter > 0);
ck('another caller has its own counter', (await G.rateLimit({ bucket: 't', id: '5.6.7.8', limit: 3, windowSec: 3600 })).ok);
ck('the store holds no raw address', [...mem.keys()].every((k) => !k.includes('1.2.3.4')));
reset();
ck('cost counts several units', (await rl({ cost: 3 })).ok && !(await rl()).ok);
reset(); storeDown = true;
const open = await rl();
ck('store down, fail open passes and says so', open.ok && open.degraded === true);
const closed = await rl({ failClosed: true });
ck('store down, fail closed refuses', !closed.ok && closed.reason === 'unavailable');

// ---- functions ------------------------------------------------------------
const ORIGIN = { Origin: 'https://www.impactmojo.in', 'x-nf-client-connection-ip': '203.0.113.9' };

console.log('/api/translate');
reset();
process.env.SARVAM_API_KEY = 's';
let sarvamCalls = 0;
global.fetch = async () => { sarvamCalls++; return { ok: true, status: 200, json: async () => ({ translated_text: 'अनुवाद' }) }; };
const { default: translate } = await import(new URL('../netlify/functions/translate.mjs', import.meta.url));
ck('cross-site request refused', (await translate(req({ Origin: 'https://evil.example' }, { lang: 'hi', q: ['Hello'] }))).status === 403);
let tr;
for (let i = 0; i < 60; i++) tr = await translate(req(ORIGIN, { lang: 'hi', q: ['String ' + i] }));
ck('60 uncached batches an hour translated', tr.status === 200);
const trOver = await translate(req(ORIGIN, { lang: 'hi', q: ['String new'] }));
ck('61st uncached batch is a 429', trOver.status === 429);
ck('no Sarvam call once limited', sarvamCalls === 60);
const before = sarvamCalls;
const long = await translate(req({ ...ORIGIN, 'x-nf-client-connection-ip': '198.51.100.1' }, { lang: 'hi', q: ['x'.repeat(5000)] }));
ck('over-long strings are dropped before Sarvam', (await long.json()).t && sarvamCalls === before);

console.log('/api/form-submit');
reset();
process.env.SUPABASE_SERVICE_ROLE_KEY = 'test-key';
let rows = 0;
global.fetch = async () => { rows++; return { ok: true, status: 201, json: async () => [{ id: 'r' }] }; };
const { default: formSubmit } = await import(new URL('../netlify/functions/form-submit.mjs', import.meta.url));
const form = { form_name: 'contact', data: { name: 'A', email: 'a@b.co' } };
ck('cross-site post refused', (await formSubmit(req({ Origin: 'https://evil.example' }, form))).status === 403);
let fs;
for (let i = 0; i < 30; i++) fs = await formSubmit(req(ORIGIN, form));
ck('30 rows an hour stored', fs.status === 200 && rows === 30);
ck('31st is a 429 and writes nothing', (await formSubmit(req(ORIGIN, form))).status === 429 && rows === 30);
reset(); storeDown = true;
ck('store down, a genuine submission is still stored', (await formSubmit(req(ORIGIN, form))).status === 200 && rows === 31);

console.log('submission-created (instructor-kit receipt)');
reset();
process.env.ADMIN_KEY = 'admin';
const mails = [];
global.fetch = async (u, o) => { if (String(u).includes('status-alert')) mails.push(JSON.parse(o.body).to); return { ok: true, status: 200, json: async () => ({ sent: true }) }; };
const { handler } = await import(new URL('../netlify/functions/submission-created.mjs', import.meta.url));
const kit = (email, ip = '192.0.2.7') => handler({ body: JSON.stringify({ payload: { form_name: 'instructor-kit', data: { email, name: 'N', course_name: 'C', ip } } }) });
await kit('victim@example.org'); await kit('victim@example.org'); await kit('victim@example.org');
ck('a recipient gets at most two receipts a day', mails.filter((m) => m === 'victim@example.org').length === 2);
ck('the admin brief is still sent every time', mails.filter((m) => m !== 'victim@example.org').length === 3);
reset();
mails.length = 0;
for (let i = 0; i < 7; i++) await kit(`p${i}@example.org`, '192.0.2.99');
ck('one caller triggers at most five receipts an hour', mails.filter((m) => /^p\d@/.test(m)).length === 5);
reset(); storeDown = true; mails.length = 0;
await kit('someone@example.org');
ck('store down, no receipt is sent (fail closed)', !mails.includes('someone@example.org') && mails.length === 1);

console.log('/api/advisor-panel');
// No Blobs environment exists in this test, which is exactly the
// "store unavailable" case: the quota must refuse rather than wave through.
process.env.SUPABASE_SERVICE_ROLE_KEY = 'test-key';
let modelCalls = 0;
global.fetch = async (u) => {
  const url = String(u);
  if (url.includes('/auth/v1/user')) return { ok: true, status: 200, json: async () => ({ id: 'u1' }) };
  if (url.includes('/rest/v1/profiles')) return { ok: true, status: 200, json: async () => [{ subscription_tier: 'professional', subscription_status: 'active' }] };
  modelCalls++; return { ok: true, status: 200, json: async () => ({ choices: [{ message: { content: 'x' } }] }) };
};
const AP = await import(new URL('../netlify/functions/advisor-panel.mjs', import.meta.url));
const apReq = new Request('https://www.impactmojo.in/api/advisor-panel', {
  method: 'POST', headers: { Authorization: 'Bearer t', 'Content-Type': 'application/json' },
  body: JSON.stringify({ topic: 'Cash transfers', transcript: [], advisorId: 'economist' }),
});
const apRes = await AP.default(apReq);
ck('quota store unavailable gives 503', apRes.status === 503);
ck('and no model is called', modelCalls === 0);
const hist = AP.buildHistory([
  { name: 'N'.repeat(500), lens: 'L', text: 'a'.repeat(10000) },
  ...Array.from({ length: 30 }, (_, i) => ({ name: 'Adv' + i, lens: 'L', text: 'b'.repeat(1900) })),
]);
ck('each transcript text clipped to 2,000 characters', !hist.includes('a'.repeat(2001)) && !hist.includes('N'.repeat(121)));
ck('total history capped at 24,000 characters', hist.length <= 24000);
ck('the most recent turn is kept', hist.includes('Adv29'));

console.log('\n' + pass + ' passed, ' + fail + ' failed');
console.log(fail ? 'FAIL - function guards broken' : 'PASS - origin checks, rate limits and key comparison hold');
process.exit(fail ? 1 : 0);
