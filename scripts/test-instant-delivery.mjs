/**
 * Contract test for instant delivery in netlify/functions/submission-created.mjs.
 *
 * A single file goes to the buyer the moment a payment reference arrives; the
 * owner is told afterwards. Bundles, the Kit, a reference that is not one, a
 * reused reference and a failed delivery must all fall back to the owner's
 * "Confirm payment" email, because the failure this guards is a paying buyer
 * who gets nothing and an owner who is told nothing.
 *
 * Run: node scripts/test-instant-delivery.mjs
 */
process.env.ADMIN_KEY = 'test-admin-key';
process.env.SUPABASE_SERVICE_ROLE_KEY = 'test-service-key';
process.env.SUPABASE_URL = 'https://example.supabase.co';
process.env.URL = 'https://www.impactmojo.in';

const guard = await import(new URL('../netlify/lib/guard.mjs', import.meta.url));
let mem = new Map(), storeDown = false;
guard.setStoreFactory(async () => { if (storeDown) throw new Error('down'); return { get: async (k) => mem.get(k) || null, set: async (k, v) => { mem.set(k, v); } }; });

let mails = [], confirmCalls = [], confirmOk = true;
global.fetch = async (u, o) => {
  const url = String(u);
  if (url.includes('/api/confirm')) { confirmCalls.push(url); return { ok: true, status: 200, text: async () => (confirmOk ? '<h1>Delivered ✓</h1>' : '<h1>Email not sent</h1>') }; }
  if (url.includes('/functions/v1/status-alert')) { mails.push(JSON.parse(o.body)); return { ok: true, status: 200, json: async () => ({ sent: true }) }; }
  return { ok: true, status: 201, json: async () => [], text: async () => '' };
};
const { handler } = await import(new URL('../netlify/functions/submission-created.mjs', import.meta.url));
let pass = 0, fail = 0;
const ck = (n, c) => { c ? (pass++, console.log('  PASS ' + n)) : (fail++, console.log('  FAIL ' + n)); };
const order = async (product, upi_ref, email = 'buyer@example.org', ip = '1.2.3.4') => {
  mails = []; confirmCalls = [];
  await handler({ body: JSON.stringify({ payload: { form_name: 'product-order', data: { product, email, upi_ref, ip } } }) });
  return { subjects: mails.map((m) => m.subject), to: mails.map((m) => m.to), confirms: confirmCalls.length };
};

console.log('A single file with a plausible reference');
let r = await order('Theory of Change 101, Course Notes (₹149)', 'T2610221249323297752807');
ck('the delivery link is opened once', r.confirms === 1);
ck('the owner is told it was delivered', r.subjects.length === 1 && /^Delivered, please check payment/.test(r.subjects[0]));

console.log('The same reference again');
r = await order('Logframe 101, Course Notes (₹149)', 'T2610221249323297752807');
ck('nothing is delivered automatically', r.confirms === 0);
ck('the owner gets the one-click email', /^Confirm payment/.test(r.subjects[0]));

console.log('A reference that is not one');
r = await order('Logframe 101, Course Notes (₹149)', 'paid yesterday');
ck('nothing is delivered automatically', r.confirms === 0);
ck('the owner gets the one-click email', /^Confirm payment/.test(r.subjects[0]));

console.log('A bundle');
r = await order('Commission an Evaluation: Bundle (₹399)', 'CICAgLimyvDhRQ');
ck('nothing is delivered automatically', r.confirms === 0);
ck('the owner gets the one-click email', /^Confirm payment/.test(r.subjects[0]));

console.log('The Kit, even when the page claims a low price');
r = await order('Evaluation Essentials Kit (₹99)', '617504915009');
ck('nothing is delivered automatically', r.confirms === 0);
ck('the owner gets the one-click email', /^Confirm payment/.test(r.subjects[0]));

console.log('The delivery itself fails');
confirmOk = false;
r = await order('MEL Basics 101, Course Notes (₹149)', '617525917679', 'other@example.org', '5.6.7.8');
ck('the delivery was attempted', r.confirms === 1);
ck('the owner still gets the one-click email', /^Confirm payment/.test(r.subjects[0]));
confirmOk = true;

console.log('A fourth order to one address in a day');
mem = new Map();
for (const ref of ['AAAAAAAAAA01', 'AAAAAAAAAA02', 'AAAAAAAAAA03']) await order('MEL Basics 101, Course Notes (₹149)', ref, 'many@example.org', '');
r = await order('MEL Basics 101, Course Notes (₹149)', 'AAAAAAAAAA04', 'many@example.org', '');
ck('is held for the owner', r.confirms === 0 && /^Confirm payment/.test(r.subjects[0]));

console.log('The counter store is down');
storeDown = true;
r = await order('MEL Basics 101, Course Notes (₹149)', 'BBBBBBBBBB01', 'new@example.org', '9.9.9.9');
ck('nothing is delivered automatically', r.confirms === 0);
ck('the owner gets the one-click email', /^Confirm payment/.test(r.subjects[0]));
storeDown = false;

console.log('An order with no reference is still only a lead');
r = await order('MEL Basics 101, Course Notes (₹149)', '');
ck('no mail and no delivery', r.subjects.length === 0 && r.confirms === 0);

console.log('A form whose page keeps no copy of its own');
let stored = [], existing = [];
const realFetch = global.fetch;
global.fetch = async (u, o) => {
  const url = String(u);
  if (url.includes('/rest/v1/form_submissions') && (!o || !o.method)) return { ok: true, status: 200, json: async () => existing };
  if (url.includes('/rest/v1/form_submissions') && o.method === 'POST') { stored.push(JSON.parse(o.body)); return { ok: true, status: 201, json: async () => [] }; }
  return realFetch(u, o);
};
await handler({ body: JSON.stringify({ payload: { form_name: 'grievance', data: { name: 'A Person', email: 'p@example.org', description: 'I cannot save my profile.', ip: '1.1.1.1', user_agent: 'x' } } }) });
ck('a copy is stored as new', stored.length === 1 && stored[0].form_name === 'grievance' && stored[0].status === 'new' && stored[0].source === 'netlify');
ck('without the caller address', !('ip' in stored[0].data) && !('user_agent' in stored[0].data));
stored = []; existing = [{ id: 'x' }];
await handler({ body: JSON.stringify({ payload: { form_name: 'contact', data: { name: 'A Person', email: 'p@example.org', message: 'Hello there.' } } }) });
ck('no second copy when the browser already stored one', stored.length === 0);
stored = []; existing = [];
await handler({ body: JSON.stringify({ payload: { form_name: 'contact', data: { name: 'Qwzx Plm', email: 'q@example.org', message: '4159628894' } } }) });
ck('junk is stored as spam', stored.length === 1 && stored[0].status === 'spam');
global.fetch = realFetch;

console.log(`\n${pass} passed, ${fail} failed`);
console.log(fail ? 'FAIL' : 'PASS - instant delivery sends single files and holds everything else for the owner');
process.exit(fail ? 1 : 0);
