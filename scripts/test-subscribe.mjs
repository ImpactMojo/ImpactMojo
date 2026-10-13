/**
 * Contract test for netlify/functions/subscribe.mjs (POST /api/subscribe).
 *
 * The endpoint is unauthenticated and sends mail from the ImpactMojo sender
 * to an address the caller chooses, so three things are the whole boundary:
 * every value in the email is escaped, the plan and amount come from the
 * server's price table, and each caller and each recipient can trigger only a
 * few emails (with no mail at all when the counter store is down).
 *
 * Run: node scripts/test-subscribe.mjs
 */
const G = await import(new URL('../netlify/lib/guard.mjs', import.meta.url));
let mem = new Map(), storeDown = false;
G.setStoreFactory(async () => {
  if (storeDown) throw new Error('blobs unavailable');
  return { get: async (k) => (mem.has(k) ? mem.get(k) : null), set: async (k, v) => { mem.set(k, v); } };
});
const reset = () => { mem = new Map(); storeDown = false; mails = []; inserts = []; };

process.env.SUPABASE_SERVICE_ROLE_KEY = 'test-key';
let mails = [], inserts = [];
global.fetch = async (u, o) => {
  const url = String(u), body = o && o.body ? JSON.parse(o.body) : null;
  if (url.includes('/functions/v1/status-alert')) { mails.push(body); return { ok: true, status: 200 }; }
  if (url.endsWith('/rest/v1/subscriptions')) { inserts.push(body); return { ok: true, status: 201, json: async () => [{ id: 'abcdef12-0000' }] }; }
  return { ok: true, status: 201, json: async () => [] };
};
const S = await import(new URL('../netlify/functions/subscribe.mjs', import.meta.url));
const h = S.default;

let pass = 0, fail = 0;
const ck = (n, c) => { c ? (pass++, console.log('  PASS ' + n)) : (fail++, console.log('  FAIL ' + n)); };
let ip = 0;
const post = (b, headers = {}) => h(new Request('https://www.impactmojo.in/api/subscribe', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json', Origin: 'https://www.impactmojo.in', 'x-nf-client-connection-ip': '203.0.113.' + (++ip % 250), ...headers },
  body: JSON.stringify(b),
}));
const good = { name: 'Asha', email: 'asha@example.org', plan: 'Practitioner', cadence: 'monthly', amount: 399 };

console.log('price table');
ck('Practitioner monthly 399', S.priceFor('Practitioner', 'monthly', 399).amount === 399);
ck('Practitioner annual 3990', S.priceFor('practitioner', 'annual', 3990).amount === 3990);
ck('Professional monthly 999', S.priceFor('Professional', 'monthly', 999).amount === 999);
ck('Professional annual 9990', S.priceFor('Professional', 'annual', 9990).amount === 9990);
ck('Professional as /subscribe/ sells it (999)', S.priceFor('Professional', 'monthly', 999).amount === 999);
ck('retired Organisation plan refused', !!S.priceFor('Organisation', 'monthly', 999).error);
ck('Team 1,499 a seat', S.priceFor('Team', 'monthly', 1499 * 4).amount === 5996);
ck('Team annual refused', !!S.priceFor('Team', 'annual', 1499).error);
ck('Team partial seat refused', !!S.priceFor('Team', 'monthly', 2000).error);
ck('unknown plan refused', !!S.priceFor('Platinum', 'monthly', 1).error);
ck('a rupee for Practitioner refused', !!S.priceFor('Practitioner', 'monthly', 1).error);
ck('annual plan at the monthly price refused', !!S.priceFor('Professional', 'annual', 999).error);
ck('amount omitted takes the server price', S.priceFor('Professional', 'annual').amount === 9990);

console.log('requests');
reset();
let r = await post(good);
ck('a valid subscription is accepted', r.status === 200 && (await r.json()).payUrl.includes('amt=399'));
ck('the stored amount is the server price', inserts[0] && inserts[0].amount === 399 && inserts[0].plan === 'Practitioner');
ck('one invoice email sent', mails.length === 1 && mails[0].to === 'asha@example.org');
reset();
ck('cross-site request refused', (await post(good, { Origin: 'https://evil.example' })).status === 403 && mails.length === 0);
ck('client-chosen amount refused', (await post({ ...good, amount: 1 })).status === 400 && inserts.length === 0);
ck('invented plan refused', (await post({ ...good, plan: '<b>Free</b>' })).status === 400 && mails.length === 0);
ck('malformed email refused', (await post({ ...good, email: 'x@y' })).status === 400);
ck('markup in email refused', (await post({ ...good, email: '<img src=x>@e.io' })).status === 400);

console.log('escaping');
reset();
await post({ ...good, name: '<a href="https://evil.example">Your account is suspended</a>' });
const html = mails[0] && mails[0].html;
ck('name is escaped in the email', html && !html.includes('<a href="https://evil.example"') && html.includes('&lt;a href=&quot;https://evil.example&quot;&gt;'));
const inv = S.invoiceHtml('<script>x</script>', 'Pro<b>', '9"9', 'https://www.impactmojo.in/x?a=1&b="2"', '2026-10');
ck('every field in invoiceHtml is escaped', !/<script>|Pro<b>|9"9|b="2"/.test(inv) && inv.includes('&amp;b=&quot;2&quot;'));

console.log('rate limits');
reset();
const fixedIp = { 'x-nf-client-connection-ip': '198.51.100.20' };
for (let i = 0; i < 5; i++) await post({ ...good, email: `p${i}@example.org` }, fixedIp);
r = await post({ ...good, email: 'p9@example.org' }, fixedIp);
ck('sixth request from one caller in an hour is a 429', r.status === 429 && r.headers.get('Retry-After'));
ck('and sends no mail', mails.length === 5);
reset();
for (let i = 0; i < 3; i++) await post(good);
r = await post(good);
ck('fourth invoice to one address in a day is a 429', r.status === 429 && mails.length === 3);
reset(); storeDown = true;
r = await post(good);
ck('store down, mail path fails closed (503, nothing sent)', r.status === 503 && mails.length === 0 && inserts.length === 0);

console.log('errors');
reset();
global.fetch = async (u) => String(u).endsWith('/rest/v1/subscriptions')
  ? { ok: false, status: 409, text: async () => 'duplicate key value violates unique constraint "subscriptions_email_key"' }
  : { ok: true, status: 200 };
r = await post(good);
const body = await r.json();
ck('database error text is not returned', r.status === 502 && !JSON.stringify(body).includes('constraint'));

console.log('\n' + pass + ' passed, ' + fail + ' failed');
console.log(fail ? 'FAIL - /api/subscribe contract broken' : 'PASS - /api/subscribe escapes, prices from the server and limits mail');
process.exit(fail ? 1 : 0);
