#!/usr/bin/env node
/**
 * AI-assisted rewrite pipeline for ImpactLex terms.
 *
 * Reads seed-snapshot.json, for each term with status: 'seed' calls an LLM
 * (Gemini primary → Grok → DeepSeek fallbacks) to produce an ImpactMojo-voice
 * definition + South Asian example + related terms. Writes back to the
 * snapshot with status: 'ai-draft' and preserves the original in seedDefinition.
 *
 * Usage:
 *   node scripts/impactlex-ai-rewrite.mjs                    # rewrite all seed terms
 *   node scripts/impactlex-ai-rewrite.mjs --limit 5          # rewrite first 5 seed terms
 *   node scripts/impactlex-ai-rewrite.mjs --only attribution,theory-of-change
 *   node scripts/impactlex-ai-rewrite.mjs --provider grok
 *   node scripts/impactlex-ai-rewrite.mjs --push             # also push drafts to InstantDB
 *
 * Env (one of these must be set):
 *   GEMINI_API_KEY, GROK_API_KEY, DEEPSEEK_API_KEY
 * For --push:
 *   INSTANTDB_APP_ID, INSTANTDB_ADMIN_TOKEN
 */

import { readFileSync, writeFileSync, appendFileSync, existsSync, mkdirSync } from 'node:fs';
import { resolve, join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createHash } from 'node:crypto';

/** Same deterministic UUID derivation used by the migration script. */
function slugToUuid(slug, namespace = 'impactlex') {
  const h = createHash('sha256').update(`${namespace}:${slug}`).digest('hex');
  const variant = (parseInt(h.slice(16, 17), 16) & 0x3 | 0x8).toString(16);
  return `${h.slice(0, 8)}-${h.slice(8, 12)}-4${h.slice(13, 16)}-${variant}${h.slice(17, 20)}-${h.slice(20, 32)}`;
}

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(__dirname, '..');
const SNAPSHOT = join(ROOT, 'impactlex/data/seed-snapshot.json');
const PROMPT_FILE = join(ROOT, 'scripts/prompts/impactlex-rewrite.md');
const LOG_DIR = join(ROOT, 'scripts/logs');

const args = process.argv.slice(2);
const hasFlag = (f) => args.includes(f);
const argVal = (f) => { const i = args.indexOf(f); return i >= 0 ? args[i + 1] : null; };

const LIMIT = parseInt(argVal('--limit') || '0', 10) || Infinity;
const ONLY = (argVal('--only') || '').split(',').map((s) => s.trim()).filter(Boolean);
const FORCE_PROVIDER = argVal('--provider'); // gemini | grok | deepseek

if (!existsSync(LOG_DIR)) mkdirSync(LOG_DIR, { recursive: true });
const LOG = join(LOG_DIR, `impactlex-rewrite-${new Date().toISOString().slice(0, 10)}.jsonl`);
function log(entry) { appendFileSync(LOG, JSON.stringify(entry) + '\n'); }

function fillPrompt(term, allTerms) {
  const tpl = readFileSync(PROMPT_FILE, 'utf8');
  // Offer up to 40 neighbours as candidates for relatedTerms.
  const others = allTerms
    .filter((t) => t.id !== term.id)
    .slice(0, 40)
    .map((t) => t.term)
    .join(', ');
  return tpl
    .replaceAll('{{term}}', term.term || '')
    .replaceAll('{{acronym}}', term.acronym || 'none')
    .replaceAll('{{category}}', term.category || '')
    .replaceAll('{{courses}}', (term.courses || []).join(', ') || 'none')
    .replaceAll('{{seedDefinition}}', term.definition || '')
    .replaceAll('{{seedExample}}', term.example || '')
    .replaceAll('{{availableTerms}}', others);
}

// ─── Provider adapters ─────────────────────────────────────────────────────

async function callGemini(prompt) {
  const key = process.env.GEMINI_API_KEY;
  if (!key) throw new Error('GEMINI_API_KEY not set');
  const model = process.env.GEMINI_MODEL || 'gemini-2.5-flash';
  const endpoint = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${key}`;
  const res = await fetch(endpoint, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      contents: [{ parts: [{ text: prompt }] }],
      generationConfig: { temperature: 0.4, responseMimeType: 'application/json' },
    }),
  });
  if (!res.ok) throw new Error(`Gemini ${res.status}: ${await res.text()}`);
  const data = await res.json();
  return data.candidates?.[0]?.content?.parts?.[0]?.text || '';
}

async function callGrok(prompt) {
  const key = process.env.GROK_API_KEY;
  if (!key) throw new Error('GROK_API_KEY not set');
  const res = await fetch('https://api.x.ai/v1/chat/completions', {
    method: 'POST',
    headers: { 'Authorization': `Bearer ${key}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      model: 'grok-2-latest',
      messages: [{ role: 'user', content: prompt }],
      temperature: 0.4,
      response_format: { type: 'json_object' },
    }),
  });
  if (!res.ok) throw new Error(`Grok ${res.status}: ${await res.text()}`);
  const data = await res.json();
  return data.choices?.[0]?.message?.content || '';
}

async function callGroq(prompt) {
  const key = process.env.GROQ_API_KEY;
  if (!key) throw new Error('GROQ_API_KEY not set');
  const model = process.env.GROQ_MODEL || 'llama-3.3-70b-versatile';
  const res = await fetch('https://api.groq.com/openai/v1/chat/completions', {
    method: 'POST',
    headers: { 'Authorization': `Bearer ${key}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      model,
      messages: [{ role: 'user', content: prompt }],
      temperature: 0.4,
      response_format: { type: 'json_object' },
    }),
  });
  if (!res.ok) throw new Error(`Groq ${res.status}: ${await res.text()}`);
  const data = await res.json();
  return data.choices?.[0]?.message?.content || '';
}

async function callDeepSeek(prompt) {
  const key = process.env.DEEPSEEK_API_KEY;
  if (!key) throw new Error('DEEPSEEK_API_KEY not set');
  const res = await fetch('https://api.deepseek.com/chat/completions', {
    method: 'POST',
    headers: { 'Authorization': `Bearer ${key}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      model: 'deepseek-chat',
      messages: [{ role: 'user', content: prompt }],
      temperature: 0.4,
      response_format: { type: 'json_object' },
    }),
  });
  if (!res.ok) throw new Error(`DeepSeek ${res.status}: ${await res.text()}`);
  const data = await res.json();
  return data.choices?.[0]?.message?.content || '';
}

const PROVIDERS = {
  gemini: { name: 'gemini', call: callGemini, envKey: 'GEMINI_API_KEY' },
  groq: { name: 'groq', call: callGroq, envKey: 'GROQ_API_KEY' },
  grok: { name: 'grok', call: callGrok, envKey: 'GROK_API_KEY' },
  deepseek: { name: 'deepseek', call: callDeepSeek, envKey: 'DEEPSEEK_API_KEY' },
};

function providerChain() {
  if (FORCE_PROVIDER) return [PROVIDERS[FORCE_PROVIDER]].filter(Boolean);
  return [PROVIDERS.gemini, PROVIDERS.groq, PROVIDERS.grok, PROVIDERS.deepseek].filter((p) => process.env[p.envKey]);
}

async function generate(prompt) {
  const chain = providerChain();
  if (!chain.length) throw new Error('No provider API key set. Set GEMINI_API_KEY, GROK_API_KEY, or DEEPSEEK_API_KEY.');
  let lastErr;
  for (const provider of chain) {
    try {
      const raw = await provider.call(prompt);
      return { provider: provider.name, raw };
    } catch (err) {
      lastErr = err;
      console.warn(`[warn] ${provider.name} failed: ${err.message}`);
    }
  }
  throw lastErr;
}

function parseJsonResponse(raw) {
  // Some providers wrap the JSON in code fences even with json response_format.
  const cleaned = raw.trim().replace(/^```(?:json)?\s*/, '').replace(/\s*```$/, '');
  try { return JSON.parse(cleaned); }
  catch (err) {
    // Try to extract the first JSON object substring.
    const m = cleaned.match(/\{[\s\S]*\}/);
    if (m) return JSON.parse(m[0]);
    throw err;
  }
}

// ─── InstantDB push ────────────────────────────────────────────────────────

async function pushDrafts(terms) {
  const appId = process.env.INSTANTDB_APP_ID;
  const token = process.env.INSTANTDB_ADMIN_TOKEN;
  if (!appId || !token) throw new Error('--push requires INSTANTDB_APP_ID and INSTANTDB_ADMIN_TOKEN');
  const endpoint = 'https://api.instantdb.com/admin/transact';
  for (let i = 0; i < terms.length; i += 50) {
    const chunk = terms.slice(i, i + 50);
    const steps = chunk.map((t) => {
      const slug = t.id;
      const uuid = slugToUuid(`terms:${slug}`);
      const { id, ...rest } = t;
      return ['update', 'terms', uuid, { ...rest, slug }];
    });
    const res = await fetch(endpoint, {
      method: 'POST',
      headers: { 'Authorization': `Bearer ${token}`, 'App-Id': appId, 'Content-Type': 'application/json' },
      body: JSON.stringify({ steps }),
    });
    if (!res.ok) throw new Error(`push ${res.status}: ${await res.text()}`);
    console.log(`[push] ${i + chunk.length}/${terms.length}`);
  }
}

// ─── Main ──────────────────────────────────────────────────────────────────

async function main() {
  const snapshot = JSON.parse(readFileSync(SNAPSHOT, 'utf8'));
  const allTerms = snapshot.terms || [];

  const seedsAll = allTerms.filter((t) => t.status === 'seed');
  const seeds = (ONLY.length
    ? seedsAll.filter((t) => ONLY.includes(t.id))
    : seedsAll
  ).slice(0, LIMIT);

  console.log(`[info] ${allTerms.length} total terms · ${seedsAll.length} in seed state · rewriting ${seeds.length}`);
  if (!seeds.length) { console.log('[info] nothing to rewrite'); return; }

  const drafts = [];
  let completed = 0;
  for (const term of seeds) {
    const prompt = fillPrompt(term, allTerms);
    try {
      const { provider, raw } = await generate(prompt);
      const parsed = parseJsonResponse(raw);
      const draft = {
        ...term,
        seedDefinition: term.definition,
        seedExample: term.example,
        definition: parsed.definition || term.definition,
        example: parsed.example || term.example,
        related: Array.isArray(parsed.relatedTerms) ? parsed.relatedTerms : term.related,
        editorNotes: parsed.notes || null,
        status: 'ai-draft',
        aiProvider: provider,
        aiDraftedAt: new Date().toISOString(),
        updatedAt: new Date().toISOString(),
      };
      // Replace in the snapshot.
      const idx = allTerms.findIndex((t) => t.id === term.id);
      if (idx >= 0) allTerms[idx] = draft;
      drafts.push(draft);
      log({ id: term.id, status: 'ok', provider });
      completed++;
      if (completed % 10 === 0) {
        writeFileSync(SNAPSHOT, JSON.stringify(snapshot, null, 2));
        console.log(`[progress] ${completed}/${seeds.length} — snapshot saved`);
      }
      // Soft rate-limit: ~30 req/min per provider.
      await new Promise((r) => setTimeout(r, 2000));
    } catch (err) {
      console.error(`[err] ${term.id}: ${err.message}`);
      log({ id: term.id, status: 'error', error: err.message });
    }
  }

  writeFileSync(SNAPSHOT, JSON.stringify(snapshot, null, 2));
  console.log(`[ok] rewrote ${drafts.length} terms → ${SNAPSHOT}`);

  if (hasFlag('--push') && drafts.length) {
    await pushDrafts(drafts);
    console.log(`[ok] pushed ${drafts.length} drafts to InstantDB`);
  }
}

main().catch((err) => { console.error(err); process.exit(1); });
