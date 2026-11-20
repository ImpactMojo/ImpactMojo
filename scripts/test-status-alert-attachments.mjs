/**
 * Contract test for the optional `attachments` field of the status-alert Edge
 * Function (supabase/functions/status-alert/index.ts).
 *
 * The order function sends the owner the file an order would deliver. This
 * function is deployed by hand and has no other test, so a mistake here shows
 * up as an order email that silently loses its file or is refused outright.
 * It must pass attachments to Resend untouched, send nothing different when
 * there are none, and refuse a malformed or oversize field rather than relay it.
 *
 * It loads the real .ts file with a Deno shim and Node's type stripping.
 * Run: node scripts/test-status-alert-attachments.mjs
 */
import { spawnSync } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const src = fileURLToPath(new URL('../supabase/functions/status-alert/index.ts', import.meta.url));
const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'status-alert-'));
const ts = fs.readFileSync(src, 'utf8').replace(/^import \{ serve \} from "[^"]+";/m, 'const serve = globalThis.__serve;');
if (ts.includes('deno.land')) { console.log('FAIL the serve import was not replaced'); process.exit(1); }
fs.writeFileSync(path.join(dir, 'status-alert.ts'), ts);
fs.writeFileSync(path.join(dir, 'run.mjs'), `
globalThis.Deno = { env: { get: (k) => ({ SUPABASE_SERVICE_ROLE_KEY: 'svc', RESEND_API_KEY: 'rk' })[k] } };
let handler; globalThis.__serve = (h) => { handler = h; };
await import('./status-alert.ts');
let resendBodies = [];
globalThis.fetch = async (u, o) => { resendBodies.push(JSON.parse(o.body)); return { ok: true, status: 200, text: async () => '' }; };
const call = async (body) => {
  const r = await handler(new Request('http://x', { method: 'POST', headers: { Authorization: 'Bearer svc', 'Content-Type': 'application/json' }, body: JSON.stringify(body) }));
  return r.status;
};
const base = { to: 'owner@example.org', subject: 's', html: '<p>h</p>' };
const out = {};
out.plain = [await call(base), resendBodies.length ? Object.keys(resendBodies.at(-1)).sort().join() : ''];
resendBodies = [];
const att = [{ filename: 'a.pdf', content: 'QUJD' }, { filename: 'b.zip', content: 'REVG' }];
out.withAtt = [await call({ ...base, attachments: att }), JSON.stringify(resendBodies.at(-1)?.attachments)];
resendBodies = [];
out.empty = [await call({ ...base, attachments: [] }), resendBodies.length];
out.notArray = [await call({ ...base, attachments: 'x' }), resendBodies.length];
out.noName = [await call({ ...base, attachments: [{ content: 'QUJD' }] }), resendBodies.length];
out.noContent = [await call({ ...base, attachments: [{ filename: 'a.pdf' }] }), resendBodies.length];
out.eleven = [await call({ ...base, attachments: Array.from({ length: 11 }, (_, i) => ({ filename: i + '.pdf', content: 'QUJD' })) }), resendBodies.length];
out.huge = [await call({ ...base, attachments: [{ filename: 'big.pdf', content: 'A'.repeat(31 * 1024 * 1024) }] }), resendBodies.length];
console.log(JSON.stringify(out));
`);
const r = spawnSync(process.execPath, ['--experimental-strip-types', '--no-warnings', path.join(dir, 'run.mjs')], { encoding: 'utf8' });
fs.rmSync(dir, { recursive: true, force: true });
if (r.status !== 0) { console.log('FAIL the Edge Function could not be loaded\n' + r.stderr.slice(0, 600)); process.exit(1); }
const o = JSON.parse(r.stdout.trim().split('\n').pop());

let pass = 0, fail = 0;
const ck = (n, c) => { c ? (pass++, console.log('  PASS ' + n)) : (fail++, console.log('  FAIL ' + n)); };
ck('a message with no attachments is sent exactly as before', o.plain[0] === 200 && o.plain[1] === 'from,html,subject,to');
ck('attachments reach Resend untouched', o.withAtt[0] === 200 && o.withAtt[1] === JSON.stringify([{ filename: 'a.pdf', content: 'QUJD' }, { filename: 'b.zip', content: 'REVG' }]));
ck('an empty list is refused', o.empty[0] === 400 && o.empty[1] === 0);
ck('something that is not a list is refused', o.notArray[0] === 400 && o.notArray[1] === 0);
ck('an item with no filename is refused', o.noName[0] === 400 && o.noName[1] === 0);
ck('an item with no content is refused', o.noContent[0] === 400 && o.noContent[1] === 0);
ck('more than ten items are refused', o.eleven[0] === 400 && o.eleven[1] === 0);
ck('more than 30 MB is refused', o.huge[0] === 400 && o.huge[1] === 0);
console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
