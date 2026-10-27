/**
 * Contract test for the buyer's file email in netlify/functions/confirm.mjs.
 *
 * "Confirm & deliver" signs the file, emails the buyer, then marks the
 * one-use link as used and tells the owner "Delivered". The email goes through
 * the status-alert function, which answers {sent:true} only when the provider
 * accepted the message. Before this test the helper ignored the answer, so a
 * refused or skipped email still produced a "Delivered" page and burnt the link.
 *
 * Run: node scripts/test-order-mail.mjs
 */
import crypto from 'node:crypto';

process.env.ADMIN_KEY = 'test-admin-key';
process.env.SUPABASE_SERVICE_ROLE_KEY = 'test-service-key';
process.env.SUPABASE_URL = 'https://example.supabase.co';

let mailCalls = 0, mailPlan = [];
global.fetch = async (u) => {
  const url = String(u);
  if (url.includes('/storage/v1/object/sign/')) return { ok: true, status: 200, json: async () => ({ signedURL: '/object/sign/products/f.docx?token=t' }), text: async () => '' };
  if (url.includes('/functions/v1/status-alert')) {
    mailCalls++;
    const step = mailPlan.shift() || { status: 200, body: { sent: true } };
    if (step.throw) throw new Error('network');
    return { ok: step.status >= 200 && step.status < 300, status: step.status, json: async () => step.body };
  }
  return { ok: true, status: 200, json: async () => [], text: async () => '' };
};

const { default: handler } = await import(new URL('../netlify/functions/confirm.mjs', import.meta.url));
let pass = 0, fail = 0;
const ck = (n, c) => { c ? (pass++, console.log('  PASS ' + n)) : (fail++, console.log('  FAIL ' + n)); };

let seq = 0;
const link = () => {
  const ts = String(Date.now() + (seq++)), email = 'buyer@example.org', key = 'f' + seq + '.docx';
  const sig = crypto.createHmac('sha256', 'test-admin-key').update(['product', email, key, ts].join('|')).digest('hex').slice(0, 32);
  return `https://www.impactmojo.in/api/confirm?type=product&email=${encodeURIComponent(email)}&key=${encodeURIComponent(key)}&ts=${ts}&sig=${sig}`;
};
const run = async (plan) => { mailCalls = 0; mailPlan = plan; const r = await handler(new Request(link())); return { text: await r.text(), calls: mailCalls }; };

console.log('Accepted on the first try');
let r = await run([{ status: 200, body: { sent: true } }]);
ck('page says Delivered', /Delivered/.test(r.text));
ck('one mail attempt', r.calls === 1);

console.log('Refused once, accepted on the retry');
r = await run([{ status: 502, body: { error: 'resend failed' } }, { status: 200, body: { sent: true } }]);
ck('page says Delivered', /Delivered/.test(r.text));
ck('two mail attempts', r.calls === 2);

console.log('Refused both times');
r = await run([{ status: 502, body: { error: 'resend failed' } }, { status: 502, body: { error: 'resend failed' } }]);
ck('page does NOT say Delivered', !/Delivered/.test(r.text));
ck('page says the email was not sent', /Email not sent/.test(r.text));
ck('tells the owner the link is still usable', /not been used up/.test(r.text));
ck('two mail attempts', r.calls === 2);

console.log('Provider key missing (status-alert answers 200 {skipped:true})');
r = await run([{ status: 200, body: { skipped: true } }, { status: 200, body: { skipped: true } }]);
ck('page does NOT say Delivered', !/Delivered/.test(r.text));
ck('page says the email was not sent', /Email not sent/.test(r.text));

console.log('Network error both times');
r = await run([{ throw: true }, { throw: true }]);
ck('page does NOT say Delivered', !/Delivered/.test(r.text));

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
