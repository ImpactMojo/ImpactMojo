/**
 * Contract test for the weekly open-items email and its "Mark as handled" link.
 *
 * The email must list every entry still "new", put junk last, and carry a link
 * per entry that /api/confirm accepts once. A link that fails to verify, or an
 * email that hides a real entry among spam, is the failure: somebody stays
 * waiting and the owner believes the list was complete.
 *
 * Run: node scripts/test-open-items.mjs
 */
process.env.ADMIN_KEY = 'test-admin-key';
process.env.SUPABASE_SERVICE_ROLE_KEY = 'test-service-key';
process.env.SUPABASE_URL = 'https://example.supabase.co';
process.env.STATUS_ALERT_EMAIL = 'owner@example.org';
process.env.URL = 'https://www.impactmojo.in';

let patched = [];
global.fetch = async (u, o) => {
  const url = String(u);
  if (url.includes('/rest/v1/form_submissions') && o && o.method === 'PATCH') { patched.push({ url, body: JSON.parse(o.body) }); return { ok: true, status: 200, json: async () => [{ id: 'x', form_name: 'contact' }] }; }
  return { ok: true, status: 200, json: async () => [], text: async () => '' };
};
const { buildEmail } = await import(new URL('../netlify/functions/weekly-open-items.mjs', import.meta.url));
const { default: confirm } = await import(new URL('../netlify/functions/confirm.mjs', import.meta.url));
const { looksLikeJunk } = await import(new URL('../netlify/lib/guard.mjs', import.meta.url));
let pass = 0, fail = 0;
const ck = (n, c) => { c ? (pass++, console.log('  PASS ' + n)) : (fail++, console.log('  FAIL ' + n)); };

const id1 = '11111111-1111-4111-8111-111111111111', id2 = '22222222-2222-4222-8222-222222222222';
const rows = [
  { id: id2, form_name: 'contact', email: 'x@example.org', submitted_at: '2026-11-13T05:00:00Z', data: { name: 'Yzoozg Rqcmy', message: '4159628894' } },
  { id: id1, form_name: 'contact', email: 'ngo@example.org', submitted_at: '2026-10-26T05:00:00Z', data: { name: 'A Person', subject: 'Partnership', message: 'We would like <b>to</b> talk.' } },
];
const mail = buildEmail(rows, Date.parse('2026-11-16T03:30:00Z'));

console.log('The email');
ck('counts the real entry only in the subject', mail.subject === 'ImpactMojo: 1 open form entry');
ck('lists the real entry before the junk', mail.html.indexOf('ngo@example.org') < mail.html.indexOf('x@example.org'));
ck('says how long the entry has waited', /waiting 20 days/.test(mail.html));
ck('escapes what the visitor typed', mail.html.includes('&lt;b&gt;to&lt;/b&gt;') && !mail.html.includes('<b>to</b>'));
ck('labels the junk', /looks like spam/.test(mail.html));

console.log('The junk rule');
ck('a bare phone-length number is junk', looksLikeJunk({ name: 'Abc Def', message: '9710693631' }));
ck('a Test User probe is junk', looksLikeJunk({ name: 'Test User', message: 'Test' }));
ck('a real message with a number in it is not', !looksLikeJunk({ name: 'A Person', message: 'Call me on 9710693631 after six.' }));
ck('an order with no message is not', !looksLikeJunk({ name: 'A Buyer', product: 'X', upi_ref: '617504915009' }));

console.log('The link');
const link = (mail.html.match(/href="([^"]*type=handled[^"]*)"/) || [])[1].replace(/&amp;/g, '&');
ck('names the entry', link.includes('key=' + id1));
let r = await confirm(new Request(link));
ck('marks the entry as handled', /Marked as handled/.test(await r.text()) && patched.length === 1 && patched[0].body.status === 'handled' && patched[0].url.includes(id1));
r = await confirm(new Request(link.replace(id1, id2)));
ck('is refused for any other entry', /Invalid link/.test(await r.text()) && patched.length === 1);

console.log(`\n${pass} passed, ${fail} failed`);
console.log(fail ? 'FAIL' : 'PASS - the open-items email lists what is open and its links close exactly one entry');
process.exit(fail ? 1 : 0);
