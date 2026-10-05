/**
 * Contract test for the breached-password check in js/auth.js (imxPwnedCount).
 *
 * Supabase's own leaked-password protection is a Pro-plan setting, so the site does the check in the
 * browser against the Have I Been Pwned range API. Two properties matter and neither is visible when it
 * breaks: the password (or its full hash) must never leave the browser, and a failed lookup must never
 * block a sign-up. A check that sent the whole hash would still work and would be a privacy defect; a
 * check that threw on a network error would lock people out whenever HIBP is down.
 *
 * Run: node scripts/test-password-check.mjs
 */
import fs from 'node:fs';
import crypto from 'node:crypto';

const src = fs.readFileSync(new URL('../js/auth.js', import.meta.url), 'utf8');
const m = src.match(/async function imxPwnedCount\(password\) \{[\s\S]*?\n\}\nwindow\.imxPwnedCount/);
if (!m) { console.log('FAIL imxPwnedCount not found in js/auth.js'); process.exit(1); }
const fnSrc = m[0].replace(/\nwindow\.imxPwnedCount$/, '');

let pass = 0, fail = 0;
const check = (n, c) => { c ? (pass++, console.log('  PASS', n)) : (fail++, console.log('  FAIL', n)); };
const sha1 = (s) => crypto.createHash('sha1').update(s).digest('hex').toUpperCase();

function make(fetchImpl) {
  const win = { crypto: crypto.webcrypto };
  globalThis.window = win; globalThis.fetch = fetchImpl;
  globalThis.AbortController = AbortController;
  return new Function('window', 'fetch', 'TextEncoder', 'AbortController', 'setTimeout', 'clearTimeout', fnSrc + '; return imxPwnedCount;')
    (win, fetchImpl, TextEncoder, AbortController, setTimeout, clearTimeout);
}

const pw = 'correct horse battery staple 1';
const h = sha1(pw);
let urls = [], headers = [];
let fn = make(async (u, o) => { urls.push(u); headers.push(o && o.headers); return { ok: true, text: async () => `0000000000000000000000000000000000A:3\n${h.slice(5)}:42\nFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF:1` }; });
check('a breached password returns its count', (await fn(pw)) === 42);
check('only the five-character hash prefix is sent', urls.length === 1 && urls[0].endsWith('/range/' + h.slice(0, 5)));
check('the password and the rest of the hash never appear in the request', !urls[0].includes(pw) && !urls[0].includes(h.slice(5)) && !urls[0].toUpperCase().includes(h.slice(5, 12)));
check('responses are padded', headers[0] && headers[0]['Add-Padding'] === 'true');

fn = make(async () => ({ ok: true, text: async () => 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA:5\n' }));
check('a password not in the list returns 0', (await fn(pw)) === 0);

fn = make(async () => { throw new Error('offline'); });
check('a network failure returns null and does not throw', (await fn(pw)) === null);

fn = make(async () => ({ ok: false, status: 503, text: async () => '' }));
check('a non-200 answer returns null', (await fn(pw)) === null);

fn = make(async () => ({ ok: true, text: async () => '' }));
check('an empty password is not looked up', (await fn('')) === null);

// Wiring: the check must run before the Supabase call in signUp and updatePassword.
function before(fnName, anchor) {
  const i = src.indexOf('async ' + fnName + '(');
  const a = src.indexOf('imxPwnedCount(', i), b = src.indexOf(anchor, i);
  return i > -1 && a > -1 && b > -1 && a < b;
}
check('signUp checks the password before calling Supabase', before('signUp', 'supabaseClient.auth.signUp('));
check('updatePassword checks the password before calling Supabase', before('updatePassword', 'supabaseClient.auth.updateUser('));
check('signIn nudges, and does not block, on a breached password', /imxPwnedCount\(password\)\.then\(function \(n\) \{ if \(n > 0\) imxShowPwnedNotice\(\); \}\)/.test(src));

// The pages must agree with Supabase Auth's minimum length.
const signup = fs.readFileSync(new URL('../signup.html', import.meta.url), 'utf8');
const reset = fs.readFileSync(new URL('../reset-password.html', import.meta.url), 'utf8');
check('signup requires 12 characters', /password\.length < 12/.test(signup) && !/password\.length < 8\b/.test(signup));
check('password reset requires 12 characters', /pw\.length < 12/.test(reset) && !/pw\.length < 8\b/.test(reset));

console.log(`\n${pass} passed, ${fail} failed`);
console.log(fail ? 'FAIL - breached-password check' : 'PASS - breached-password check');
process.exit(fail ? 1 : 0);
