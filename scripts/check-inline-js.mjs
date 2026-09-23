#!/usr/bin/env node
// Every inline <script> on every page must parse.
//
// An HTML parser ends a <script> element at the first literal `</script` in the
// source, whatever the JavaScript around it thinks it is doing, and a block that
// throws SyntaxError is not partially executed: NOTHING in it runs. The page
// renders exactly as designed and the only evidence is one console line.
//
// This is not hypothetical here. On 2026-09-23 `index.html` carried
//
//     ['What's Premium?','What is Premium?'],
//
// inside a single-quoted string, so the whole 86-line Mojini block — the
// placeholder text, the greeting, and every knowledge-base chip — had never run
// on the homepage. Nothing errored in CI, nothing looked broken.
//
// The check cuts each inline script where the browser would cut it and asks
// node to parse the remainder. No browser, no network.
import { readdirSync, statSync, readFileSync, writeFileSync, unlinkSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { tmpdir } from 'node:os';
import path from 'node:path';
import vm from 'node:vm';

// `vm.Script` parses as a classic script, so a legitimate `type="module"` body
// using top-level `import` or `await` fails there and nowhere else. `node
// --check` on a .mjs file gets it right, so anything vm rejects is re-checked
// that way before it is called a failure.
function parses(body, file) {
  try { new vm.Script(body, { filename: file }); return null; } catch (e) {
    const tmp = path.join(tmpdir(), `inline-${process.pid}-${Math.random().toString(36).slice(2)}.mjs`);
    try {
      writeFileSync(tmp, body);
      execFileSync(process.execPath, ['--check', tmp], { stdio: 'pipe' });
      return null;                       // valid as a module
    } catch { return e.message; }
    finally { try { unlinkSync(tmp); } catch {} }
  }
}

const ROOT = process.cwd();
const SKIP = new Set(['.git', 'node_modules', 'Backups', 'backups', '.claude']);

// Template sources, not pages. Their scripts carry {{placeholders}} that are
// substituted at generation time and are not JavaScript until they are. A page
// that is actually served never belongs here.
const EXEMPT = new Map([
  ['DataNotes/_template.html', 'generator template; the script body holds {{...}} placeholders'],
  ['scripts/templates/book-companion.template.html', 'generator template; same reason'],
]);

function walk(dir, acc = []) {
  for (const name of readdirSync(dir)) {
    if (SKIP.has(name)) continue;
    const f = path.join(dir, name);
    const st = statSync(f);
    if (st.isDirectory()) walk(f, acc);
    else if (name.endsWith('.html')) acc.push(f);
  }
  return acc;
}

const OPEN = /<script\b([^>]*)>/gi;
let files = 0, scripts = 0;
const failures = [];
const exempted = [];

for (const file of walk(ROOT)) {
  const rel = path.relative(ROOT, file);
  if (EXEMPT.has(rel)) { exempted.push(rel); continue; }
  const src = readFileSync(file, 'utf8');
  if (!/<script/i.test(src)) continue;
  files++;
  const lower = src.toLowerCase();
  let n = 0;
  let pos = 0;
  for (;;) {
    OPEN.lastIndex = pos;
    const m = OPEN.exec(src);
    if (!m) break;
    const start = m.index + m[0].length;
    const close = lower.indexOf('</script', start);
    // A `<script` sitting inside an already-open script element is text to the
    // HTML parser, not a new element. Resume the scan after this element's end,
    // or the minified bundles here report false failures.
    pos = close === -1 ? src.length : close + 8;
    const attrs = m[1];
    if (/\ssrc\s*=/i.test(attrs)) continue;              // external
    const type = (attrs.match(/type\s*=\s*["']?([^"'\s>]+)/i) || [])[1];
    if (type && !/javascript|module/i.test(type)) continue; // JSON-LD, templates
    n++;
    const body = src.slice(start, close === -1 ? src.length : close);
    if (!body.trim()) continue;
    scripts++;
    const why = parses(body, file);
    if (why) {
      const line = src.slice(0, start).split('\n').length;
      failures.push(`${path.relative(ROOT, file)}: inline script #${n} (opens line ${line}) \u2014 ${why}`);
    }
  }
}

const stale = [...EXEMPT.keys()].filter(r => !exempted.includes(r));
if (stale.length) {
  console.error('FAIL — exemptions naming files that no longer exist:\n');
  for (const r of stale) console.error('  ' + r);
  process.exit(1);
}

if (failures.length) {
  console.error('FAIL — inline scripts that do not parse:\n');
  for (const f of failures) console.error('  ' + f);
  console.error(`\n${failures.length} of ${scripts} inline scripts across ${files} pages.`);
  process.exit(1);
}
console.log(`PASS — ${scripts} inline scripts across ${files} pages all parse (${exempted.length} template files exempt).`);
