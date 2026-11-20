/**
 * Contract test for the owner's side of an order in
 * netlify/functions/submission-created.mjs.
 *
 * Three things, each a failure nobody would see until a buyer waited:
 *
 *  1. Automatic delivery is OFF by default. The owner looks at each file before
 *     it goes to a buyer, so every order waits for the "Confirm & deliver" click.
 *  2. After the confirm email, the owner gets a second email carrying the file
 *     or files that click would send (a link when a file is too big to attach),
 *     and a file missing from the bucket is named. It never replaces the confirm
 *     email, and a storage failure never costs the owner that email.
 *  3. The function connects Netlify Blobs. It is written in the Lambda-compatible
 *     style, where Blobs works only after connectLambda(event). Until 2026-11-20
 *     nothing called it, every rate-limit counter failed closed, and a paying
 *     buyer's order said "instant-ref: unavailable". The other tests swap in an
 *     in-memory store, so this one uses the real library.
 *
 * Needs @netlify/blobs (CI installs it for this step).
 * Run: node scripts/test-owner-preview.mjs
 */
process.env.ADMIN_KEY = 'test-admin-key';
process.env.SUPABASE_SERVICE_ROLE_KEY = 'test-service-key';
process.env.SUPABASE_URL = 'https://example.supabase.co';
process.env.URL = 'https://www.impactmojo.in';
delete process.env.INSTANT_DELIVERY;

const guard = await import(new URL('../netlify/lib/guard.mjs', import.meta.url));
const mem = new Map();
guard.setStoreFactory(async () => ({ get: async (k) => mem.get(k) || null, set: async (k, v) => { mem.set(k, v); } }));

// The bucket: name -> size in bytes. Anything not listed is missing.
const MB = 1048576;
let bucket = {}, storageDown = false, mails = [], confirmCalls = 0;
const bytesOf = (name) => Buffer.from('FILE:' + name);
global.fetch = async (u, o = {}) => {
  const url = String(u);
  if (url.includes('/api/confirm')) { confirmCalls++; return { ok: true, status: 200, text: async () => '<h1>Delivered ✓</h1>' }; }
  if (url.includes('/functions/v1/status-alert')) { mails.push(JSON.parse(o.body)); return { ok: true, status: 200, json: async () => ({ sent: true }) }; }
  const m = url.match(/\/storage\/v1\/object\/(info|authenticated|sign)\/products\/(.+)$/);
  if (m) {
    if (storageDown) throw new Error('storage down');
    const name = decodeURIComponent(m[2]);
    if (!(name in bucket)) return { ok: false, status: 400, json: async () => ({}) };
    if (m[1] === 'info') return { ok: true, status: 200, json: async () => ({ name, size: bucket[name] }) };
    if (m[1] === 'sign') return { ok: true, status: 200, json: async () => ({ signedURL: `/object/sign/products/${encodeURIComponent(name)}?token=T` }) };
    const b = bytesOf(name);
    return { ok: true, status: 200, arrayBuffer: async () => b.buffer.slice(b.byteOffset, b.byteOffset + b.byteLength) };
  }
  return { ok: true, status: 201, json: async () => [], text: async () => '' };
};
const { handler } = await import(new URL('../netlify/functions/submission-created.mjs', import.meta.url));
let pass = 0, fail = 0;
const ck = (n, c) => { c ? (pass++, console.log('  PASS ' + n)) : (fail++, console.log('  FAIL ' + n)); };
const send = async (form, data, event = {}) => {
  mails = []; confirmCalls = 0;
  await handler({ ...event, body: JSON.stringify({ payload: { form_name: form, data: { email: 'buyer@example.org', ip: '1.2.3.4', ...data } } }) });
};
const order = (product, ref = '669019445961') => send('product-order', { product, upi_ref: ref });
const subjects = () => mails.map((m) => m.subject);
const preview = () => mails.find((m) => /^Check before you click/.test(m.subject));

console.log('A single file with a plausible reference, automatic delivery left off');
bucket = { 'ImpactMojo-101-Notes-brsr-reporting.pdf': 3 * MB };
await order('BRSR & Sustainability Reporting 101, Course Notes (₹149)');
ck('nothing is delivered automatically', confirmCalls === 0);
ck('the owner gets the confirm email first', /^Confirm payment/.test(subjects()[0]));
ck('then a second email to check the file', /^Check before you click/.test(subjects()[1]));
ck('both go to the owner, never to the buyer', mails.every((m) => m.to !== 'buyer@example.org'));
let p = preview();
ck('the file is attached under its own name', p && p.attachments && p.attachments.length === 1 && p.attachments[0].filename === 'ImpactMojo-101-Notes-brsr-reporting.pdf');
ck('and its bytes are intact', p && Buffer.from(p.attachments[0].content, 'base64').equals(bytesOf('ImpactMojo-101-Notes-brsr-reporting.pdf')));
ck('the confirm email carries no attachment', !mails[0].attachments);

console.log('A bundle');
bucket = new Proxy({}, { has: () => true, get: (_, k) => (typeof k === 'string' ? 1 * MB : undefined) });
await order('Commission an Evaluation: Bundle (₹399)', '617504915009');
ck('nothing is delivered automatically', confirmCalls === 0);
p = preview();
ck('every file of the bundle is attached', p && p.attachments && p.attachments.length === 4);
ck('the file names are distinct', p && new Set(p.attachments.map((a) => a.filename)).size === 4);

console.log('Files too big to attach together');
bucket = new Proxy({}, { has: () => true, get: (_, k) => (typeof k === 'string' ? 3 * MB : undefined) });
await order('Prepare for Field Data Collection: Bundle (₹449)', '617525917679');
p = preview();
ck('what fits in 12 MB is attached', p && p.attachments && p.attachments.length === 4);
ck('the two that do not fit come as three-day links', p && (p.html.match(/object\/sign\/products\//g) || []).length === 2 && /3 days/.test(p.html));
bucket = { 'ImpactMojo-Refresher-Sampling.pdf': 20 * MB };
await order('Sampling & Sample Size: Refresher (₹99)', '617525917680');
p = preview();
ck('a single file over the limit is a link, not an attachment', p && !p.attachments && /object\/sign\/products\/ImpactMojo-Refresher-Sampling\.pdf\?token=T/.test(p.html));
ck('the confirm email still went', /^Confirm payment/.test(subjects()[0]));

console.log('A file that is not in the bucket');
bucket = {};
await order('BRSR & Sustainability Reporting 101, Course Notes (₹149)', '617525917681');
p = preview();
ck('the owner is told before the buyer finds out', p && /not found in the products bucket/.test(p.html));
ck('the confirm email still went', /^Confirm payment/.test(subjects()[0]));

console.log('Storage is down');
storageDown = true;
await order('BRSR & Sustainability Reporting 101, Course Notes (₹149)', '617525917682');
ck('the owner still gets the confirm email', /^Confirm payment/.test(subjects()[0]));
ck('nothing throws and nothing is delivered', confirmCalls === 0);
storageDown = false;

console.log('A subscription');
await send('subscription-payment', { plan: 'Practitioner', reference: 'SUB-123' });
ck('the owner gets the confirm email', subjects().length === 1 && /^Confirm payment/.test(subjects()[0]));
ck('there is no file, so no second email', !preview());

console.log('Automatic delivery can still be switched on');
process.env.INSTANT_DELIVERY = 'on';
bucket = { 'ImpactMojo-101-Notes-brsr-reporting.pdf': 3 * MB };
await order('BRSR & Sustainability Reporting 101, Course Notes (₹149)', 'T9999999999999');
ck('with INSTANT_DELIVERY=on a single file is delivered at once', confirmCalls === 1);
delete process.env.INSTANT_DELIVERY;

console.log('Netlify Blobs is connected');
const blobs = await import('@netlify/blobs');
const real = async () => blobs.getStore({ name: 'rate-limits', consistency: 'strong' }).get('probe');
let before = '';
try { await real(); before = 'no error'; } catch (e) { before = e.name; }
ck('without connectLambda the real library cannot reach its store', before === 'MissingBlobsEnvironmentError');
const blobsContext = Buffer.from(JSON.stringify({ url: 'http://127.0.0.1:9', token: 'test-token' })).toString('base64');
await send('product-order', { product: 'BRSR & Sustainability Reporting 101, Course Notes (₹149)', upi_ref: '' }, { blobs: blobsContext, headers: { 'x-nf-deploy-id': 'd1', 'x-nf-site-id': 's1' } });
let after = '';
try { await real(); after = 'no error'; } catch (e) { after = e.name; }
ck('after the handler runs, the library is configured', after !== 'MissingBlobsEnvironmentError');

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
