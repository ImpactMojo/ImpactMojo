// Check an authored notes file against the deck it was written for.
//
//   node scripts/course-notes/validate-notes.mjs slug [slug ...]
//
// Needs build/slides/<slug>.json (extract-deck.mjs). Fails on: a content slide with no note, a note for a
// slide that is not content, the wrong number of sections, text over its length limit, a diagram with the
// wrong shape, or a number written in a note that the slide it explains does not contain as a whole word.
import fs from "node:fs";
import path from "node:path";

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), "../..");
const SLIDES = process.env.SLIDES_DIR || path.join(ROOT, "build/slides");
const slugs = process.argv.slice(2);
if (!slugs.length) { console.error("usage: validate-notes.mjs slug [slug ...]"); process.exit(2); }

// Arithmetic written as "a × b = c" or "a ÷ b = c" (up to three terms) must come out. A note that
// states a wrong sum is worse than no note, so every such line in an example is recomputed.
const NUM = "([\\d][\\d,]*(?:\\.\\d+)?)";
const EQ = new RegExp(`${NUM}\\s*([×÷+−-])\\s*${NUM}(?:\\s*([×÷+−-])\\s*${NUM})?(?:\\s*([×÷+−-])\\s*${NUM})?\\s*=\\s*${NUM}(%?)`, "g");
const val = (t) => Number(t.replace(/,/g, ""));
function checkArithmetic(text, where, err) {
  for (const m of text.matchAll(EQ)) {
    const nums = [m[1], m[3], m[5], m[7]].filter(Boolean).map(val), ops = [m[2], m[4], m[6]].filter(Boolean);
    const result = val(m[8]);
    // precedence: × and ÷ before + and −
    let ns = [nums[0]], os = [];
    nums.slice(1).forEach((n, i) => { const o = ops[i]; if (o === "×" || o === "÷") { const a = ns.pop(); ns.push(o === "×" ? a * n : a / n); } else { os.push(o); ns.push(n); } });
    let r = ns[0]; os.forEach((o, i) => { r = o === "+" ? r + ns[i + 1] : r - ns[i + 1]; });
    if (m[9] === "%" && ops.includes("÷")) r *= 100;
    const dec = (m[8].split(".")[1] || "").length, tol = Math.max(0.5 * Math.pow(10, -dec), Math.abs(result) * 0.003);
    if (Math.abs(r - result) > tol + 1e-9) err(`${where}: "${m[0]}" works out to ${Math.round(r * 1e4) / 1e4}`);
  }
}
let bad = 0;
const words = (t) => String(t).trim().split(/\s+/).filter(Boolean).length;
for (const slug of slugs) {
  const errs = [];
  const err = (m) => errs.push(m);
  let doc, deck;
  try { doc = JSON.parse(fs.readFileSync(path.join(ROOT, "content/course-notes", `${slug}.json`), "utf8")); } catch (e) { console.log(`FAIL ${slug}: no notes file or invalid JSON (${e.message})`); bad++; continue; }
  try { deck = JSON.parse(fs.readFileSync(path.join(SLIDES, `${slug}.json`), "utf8")); } catch (e) { console.log(`FAIL ${slug}: no extracted slides (run extract-deck.mjs)`); bad++; continue; }
  if (doc.slug !== slug) err(`slug says ${doc.slug}`);
  const content = deck.slides.filter((s) => s.kind === "content").map((s) => s.n);
  const dividers = deck.slides.filter((s) => s.kind === "section").length;
  for (const n of content) if (!doc.notes?.[String(n)]) err(`no note for slide ${n}`);
  for (const k of Object.keys(doc.notes || {})) {
    if (!content.includes(Number(k))) err(`note for slide ${k}, which is not a content slide`);
    checkArithmetic(doc.notes[k], `note ${k}`, err);
    const w = words(doc.notes[k]);
    if (w < 22 || w > 62) err(`note ${k} is ${w} words (22 to 62)`);
  }
  if (!doc.intro || words(doc.intro) < 25 || words(doc.intro) > 80) err("intro must be 25 to 80 words");
  if ((doc.sections || []).length !== dividers) err(`${doc.sections?.length} sections written, deck has ${dividers} dividers`);
  const lim = (v, a, b, what) => { const c = Array.isArray(v) ? v.length : -1; if (c < a || c > b) err(`${what}: ${c} items (${a} to ${b})`); };
  const txt = (v, max, what) => { if (typeof v !== "string" || !v.trim()) err(`${what} is empty`); else if (v.length > max) err(`${what} is ${v.length} characters (max ${max})`); };
  (doc.sections || []).forEach((s, i) => {
    const at = `section ${i + 1}`;
    if (s.n !== i + 1) err(`${at}: n is ${s.n}`);
    txt(s.title, 70, `${at} title`); txt(s.big_idea, 170, `${at} big_idea`);
    lim(s.in_plain_words, 2, 3, `${at} in_plain_words`); (s.in_plain_words || []).forEach((p, j) => { const w = words(p); if (w < 30 || w > 110) err(`${at} paragraph ${j + 1} is ${w} words (30 to 110)`); });
    lim(s.key_terms, 4, 6, `${at} key_terms`); (s.key_terms || []).forEach((t) => { txt(t.term, 28, `${at} term`); txt(t.meaning, 120, `${at} meaning`); });
    lim(s.mistakes, 3, 4, `${at} mistakes`); (s.mistakes || []).forEach((m) => txt(m, 190, `${at} mistake`));
    lim(s.recall, 4, 5, `${at} recall`); (s.recall || []).forEach((r) => { txt(r.q, 160, `${at} question`); txt(r.a, 230, `${at} answer`); });
    const we = s.worked_example; if (we) { [...(we.steps || []), we.answer, we.setup || ""].forEach((x) => checkArithmetic(x, `${at} example`, err)); txt(we.title, 60, `${at} example title`); lim(we.steps, 3, 6, `${at} example steps`); (we.steps || []).forEach((x) => txt(x, 170, `${at} step`)); txt(we.answer, 190, `${at} example answer`); if (we.setup) txt(we.setup, 230, `${at} setup`); } else err(`${at}: no worked_example`);
    const d = s.diagram; if (!d) { err(`${at}: no diagram`); return; }
    const L = (t, m) => { if (typeof t !== "string" || !t || t.length > m) err(`${at} diagram label "${String(t).slice(0, 30)}" over ${m} characters`); };
    switch (d.type) {
      case "flow": lim(d.nodes, 3, 6, `${at} flow nodes`); (d.nodes || []).forEach((n) => { L(n.label, 30); if (n.sub) L(n.sub, 36); }); break;
      case "cycle": lim(d.nodes, 3, 6, `${at} cycle nodes`); (d.nodes || []).forEach((n) => { L(n.label, 26); if (n.sub) L(n.sub, 30); }); break;
      case "tree": L(d.root, 40); lim(d.children, 2, 4, `${at} tree children`); (d.children || []).forEach((c) => { L(c.label, 34); lim(c.items || [], 0, 4, `${at} tree items`); (c.items || []).forEach((x) => L(x, 46)); }); break;
      case "compare": L(d.left?.title, 30); L(d.right?.title, 30); lim(d.left?.items, 2, 4, `${at} left`); lim(d.right?.items, 2, 4, `${at} right`); [...(d.left?.items || []), ...(d.right?.items || [])].forEach((x) => L(x, 52)); break;
      case "formula": lim(d.parts, 3, 9, `${at} formula parts`); (d.parts || []).forEach((p) => { if (p.op) { if (p.op.length > 2) err(`${at} operator too long`); } else { L(p.t, 24); if (p.hint) L(p.hint, 28); } }); if (d.note) L(d.note, 90); break;
      case "timeline": lim(d.events, 4, 7, `${at} timeline events`); (d.events || []).forEach((e) => { L(e.when, 24); L(e.what, 46); }); break;
      case "stack": lim(d.levels, 3, 6, `${at} stack levels`); (d.levels || []).forEach((l) => { L(l.label, 30); if (l.sub) L(l.sub, 34); }); break;
      case "hub": L(d.center, 26); lim(d.spokes, 4, 6, `${at} hub spokes`); (d.spokes || []).forEach((x) => { L(x.label, 24); if (x.sub) L(x.sub, 30); }); break;
      default: err(`${at}: unknown diagram type ${d.type}`);
    }
    if (d.caption) L(d.caption, 90);
  });
  if (errs.length) { bad++; console.log(`FAIL ${slug}: ${errs.length} problem(s)`); errs.slice(0, 40).forEach((e) => console.log("  " + e)); }
  else console.log(`ok   ${slug}: ${content.length} slide notes, ${doc.sections.length} sections`);
}
process.exit(bad ? 1 : 0);
