/**
 * ImpactLex app logic.
 *
 * Data flow:
 *   Load seed-snapshot.json and render. The snapshot is the dictionary: it is
 *   edited by pull request, so there is no second copy to fall behind it.
 *
 * The page is a deck of flashcards with two modes:
 *   Browse  a grid of cards, drawn a batch at a time, with search, an A to Z
 *           jump and filters for kind, course and how the entry was written.
 *   Study   one large card at a time from the same filtered set, with
 *           previous, next, shuffle and "mark as known" (kept on this device).
 *
 * Also here:
 *   - Term of the day (deterministic by date)
 *   - Bookmarks (localStorage)
 *   - Deep links: ?term=<slug> opens the full entry; ?q=, ?course=, ?category=,
 *     ?prov=, ?letter= and ?mode=study restore a view
 *   - Suggest-a-term form (writes to the Supabase table impactlex_contributions)
 *   - term.html (body[data-lex-page="term"]) renders one entry in full
 *
 * The shared top bar, footer and theme switch come from js/site-chrome.js.
 */

(() => {
  'use strict';

  const CONFIG = window.IMPACTLEX_CONFIG || {};
  const SNAPSHOT_URL = CONFIG.snapshotUrl || '/impactlex/data/seed-snapshot.json';
  const PAGE = (document.body && document.body.getAttribute('data-lex-page')) || 'index';
  const $ = (id) => document.getElementById(id);
  const BATCH = 24;

  // localStorage can throw (private windows, blocked site data), so every read
  // and write goes through these and the page works without it.
  function readStore(key, fallback) {
    try {
      const raw = localStorage.getItem(key);
      return raw == null ? fallback : JSON.parse(raw);
    } catch (e) { return fallback; }
  }
  function writeStore(key, value) {
    try { localStorage.setItem(key, JSON.stringify(value)); } catch (e) { /* not saved; the page carries on */ }
  }
  const asSet = (v) => new Set(Array.isArray(v) ? v : []);

  // ─── State ──────────────────────────────────────────────────────────────
  const state = {
    terms: [],
    byId: new Map(),
    caseStudies: [],
    formulae: [],
    filter: { category: 'all', course: 'all', provenance: 'all', letter: 'all', saved: 'all', query: '' },
    mode: 'browse',
    shown: BATCH,
    bookmarks: asSet(readStore('impactlex:bookmarks', [])),
    known: asSet(readStore('impactlex:known', [])),
    study: { order: [], index: 0, shuffle: false, hideKnown: false },
    openTermId: null,
    lastFocus: null,
    checked: {}, // slug -> corrections from impactlex/data/reviewed.json
  };

  // ─── Data loading ───────────────────────────────────────────────────────
  /* impactlex/data/reviewed.json holds entries that were checked against a
     cited source in the repository. They win over the snapshot for the fields
     they carry. A checked entry says so; it does not claim an editor's review. */
  async function loadChecked() {
    try {
      const res = await fetch(CONFIG.reviewedUrl || '/impactlex/data/reviewed.json');
      if (!res.ok) return;
      const data = await res.json();
      state.checked = data.terms || {};
    } catch (err) { /* the page works without it */ }
  }
  function applyChecked(terms) {
    return terms.map((t) => {
      const c = state.checked[t.id];
      if (!c) return t;
      const out = { ...t, checkedAt: c.checkedAt };
      ['definition', 'example', 'sources'].forEach((k) => { if (c[k] !== undefined) out[k] = c[k]; });
      return out;
    });
  }

  async function loadSnapshot() {
    await loadChecked();
    const res = await fetch(SNAPSHOT_URL);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
    state.terms = applyChecked((data.terms || []).filter((t) => t.status !== 'rejected'))
      .sort((a, b) => String(a.term).localeCompare(String(b.term), 'en', { sensitivity: 'base' }));
    state.byId = new Map(state.terms.map((t) => [t.id, t]));
    state.caseStudies = data.caseStudies || [];
    state.formulae = data.formulae || [];
  }

  // ─── Search ─────────────────────────────────────────────────────────────
  function matches(term, query) {
    if (!query) return true;
    const q = query.toLowerCase();
    const hay = [
      term.term,
      term.acronym,
      ...(term.aliases || []),
      term.definition,
      term.example,
      term.category,
      term.seedCategory,
      ...(term.courses || []),
    ].filter(Boolean).join(' ').toLowerCase();
    return hay.includes(q);
  }

  /* How an entry came to exist, read off the record and never inferred.
   *
   * Measured over the 494 terms in the committed snapshot on 2026-09-23:
   *   335 published, 159 still `seed`
   *   226 drafted by a model (groq or gemini), 268 written by hand
   *    34 carry a source; 460 do not
   *
   * All three used to look the same to a reader. A dictionary that a
   * practitioner quotes from should say which of its entries a person has
   * reviewed and which carry a citation, and it says so on every card, on the
   * front, where the uncomfortable answers are as visible as the good ones.
   * `rejected` entries never render at all; that is unchanged.
   */
  function provenanceOf(t) {
    return {
      reviewed: t.status === 'published',
      checked: Boolean(t.checkedAt),
      aiDrafted: Boolean(t.aiProvider),
      sourced: Boolean(t.sources && t.sources.length),
    };
  }

  const PROVENANCE_FILTERS = {
    all: { label: 'All entries', test: () => true },
    reviewed: { label: 'Reviewed', test: (t) => provenanceOf(t).reviewed },
    unreviewed: { label: 'Not yet reviewed', test: (t) => !provenanceOf(t).reviewed },
    sourced: { label: 'With a source', test: (t) => provenanceOf(t).sourced },
    checked: { label: 'Checked against a source', test: (t) => provenanceOf(t).checked },
  };

  // The lines the full entry prints under "How this entry was written".
  function provenanceLines(t) {
    const prov = provenanceOf(t);
    return [
      prov.reviewed
        ? ['ok', 'Reviewed by an editor and published.']
        : ['warn', 'Not yet reviewed. It is published so the term is findable, and an editor has not checked it.'],
      ...(prov.checked
        ? [['ok', `Definition checked against the source cited above on ${escapeHtml(String(t.checkedAt))}.`]]
        : []),
      prov.aiDrafted
        ? ['warn', `First draft written by a language model (${escapeHtml(String(t.aiProvider))}), then edited.`]
        : ['ok', 'Written by hand.'],
      prov.sourced
        ? ['ok', 'Carries a citation, listed above.']
        : ['warn', 'No citation. Check it against a primary source before quoting it.'],
    ].map(([kind, text]) => `<li class="prov-${kind}">${text}</li>`).join('');
  }

  // The short labels on the front of a card. Same facts, fewer words.
  function provenanceTags(t) {
    const prov = provenanceOf(t);
    const tags = [
      prov.reviewed ? ['ok', 'Reviewed'] : ['warn', 'Not yet reviewed'],
      prov.sourced ? ['ok', 'Has a source'] : ['warn', 'No source'],
    ];
    if (prov.aiDrafted) tags.push(['warn', 'Model draft']);
    return tags.map(([kind, text]) => `<span class="lx-tag lx-tag--${kind}">${text}</span>`).join('');
  }

  /* A source is plain text, optionally ending in an address, which is turned
     into a link. Everything is escaped first. An entry with no source says
     so: an absent citation is information. */
  function sourcesHtml(t) {
    if (!(t.sources && t.sources.length)) return 'No source recorded for this entry.';
    return t.sources.map((src) => {
      const text = escapeHtml(String(src));
      return text.replace(/(https?:\/\/[^\s<]+)/g, (u) => `<a href="${u}" target="_blank" rel="noopener noreferrer">${u}</a>`);
    }).join('<br>');
  }

  function firstLetter(t) {
    const c = String(t.term || '').trim().charAt(0).toUpperCase();
    return /[A-Z]/.test(c) ? c : '#';
  }

  // Every filter except the ones named in `skip`, so a chip can show how many
  // cards it would leave.
  function passes(t, skip) {
    const f = state.filter;
    if (skip !== 'category' && f.category !== 'all' && t.category !== f.category) return false;
    if (skip !== 'course' && f.course !== 'all' && !(t.courses || []).includes(f.course)) return false;
    if (skip !== 'provenance') {
      const prov = PROVENANCE_FILTERS[f.provenance];
      if (prov && !prov.test(t)) return false;
    }
    if (skip !== 'letter' && f.letter !== 'all' && firstLetter(t) !== f.letter) return false;
    if (skip !== 'saved') {
      if (f.saved === 'bookmarked' && !state.bookmarks.has(t.id)) return false;
      if (f.saved === 'known' && !state.known.has(t.id)) return false;
      if (f.saved === 'unknown' && state.known.has(t.id)) return false;
    }
    if (!matches(t, f.query)) return false;
    return true;
  }
  function visibleTerms() { return state.terms.filter((t) => passes(t)); }

  function filtersActive() {
    const f = state.filter;
    return ['category', 'course', 'provenance', 'letter', 'saved'].filter((k) => f[k] !== 'all').length;
  }

  // ─── Labels ─────────────────────────────────────────────────────────────
  const CAT_ORDER = ['all', 'concept', 'acronym', 'framework', 'method', 'formula', 'institution'];
  const CAT_PLURAL = { all: 'All', concept: 'Concepts', acronym: 'Acronyms', framework: 'Frameworks', method: 'Methods', formula: 'Formulae', institution: 'Institutions' };
  const CAT_ONE = { concept: 'Concept', acronym: 'Acronym', framework: 'Framework', method: 'Method', formula: 'Formula', institution: 'Institution' };
  const COURSE_LABEL = { SEL: 'SEL', dataviz: 'DataViz', devai: 'DevAI', devecon: 'DevEcon', gandhi: 'Gandhi', gender: 'Gender', law: 'Law', mel: 'MEL', poa: 'PoA', pubpol: 'PubPol' };
  const catClass = (t) => (CAT_ONE[t.category] ? `fc--${t.category}` : 'fc--concept');
  const catName = (t) => CAT_ONE[t.category] || String(t.category || 'Term');
  const courseName = (c) => COURSE_LABEL[c] || c;

  const ICON = {
    bm: '<svg class="lx-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>',
    turn: '<svg class="lx-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 12a9 9 0 0 1 15.5-6.2L21 8"/><path d="M21 3v5h-5"/><path d="M21 12a9 9 0 0 1-15.5 6.2L3 16"/><path d="M3 21v-5h5"/></svg>',
  };

  // ─── Stats ──────────────────────────────────────────────────────────────
  function setStat(name, value) {
    document.querySelectorAll(`[data-stat="${name}"]`).forEach((el) => { el.textContent = value; });
  }
  function updateStats() {
    // Every count is derived from the data, never typed into the markup.
    const courses = new Set();
    state.terms.forEach((t) => (t.courses || []).forEach((c) => courses.add(c)));
    setStat('terms', state.terms.length);
    setStat('courses', courses.size);
    setStat('formulae', state.formulae.length);
    setStat('cases', state.caseStudies.length);

    const about = $('about-counts');
    if (about) {
      const n = state.terms.length;
      const reviewed = state.terms.filter((t) => provenanceOf(t).reviewed).length;
      const drafted = state.terms.filter((t) => provenanceOf(t).aiDrafted).length;
      const sourced = state.terms.filter((t) => provenanceOf(t).sourced).length;
      about.textContent = `Of the ${n} entries, an editor has reviewed ${reviewed}, a language model wrote the first draft of ${drafted}, and ${sourced} carry a source. Every card says which of these apply to it, and the filters let you see only the reviewed or the sourced entries.`;
    }
  }

  // ─── Filters ────────────────────────────────────────────────────────────
  function chip(type, value, label, count, active) {
    const n = count == null ? '' : `<span class="count">${count}</span>`;
    return `<button class="filter-chip" type="button" aria-pressed="${active ? 'true' : 'false'}" data-filter-type="${type}" data-filter-value="${escapeHtml(value)}">${escapeHtml(label)}${n}</button>`;
  }

  function renderFilters() {
    const f = state.filter;
    const catCounts = {};
    const courseCounts = {};
    const letterCounts = {};
    for (const t of state.terms) {
      if (passes(t, 'category')) catCounts[t.category] = (catCounts[t.category] || 0) + 1;
      if (passes(t, 'course')) for (const c of (t.courses || [])) courseCounts[c] = (courseCounts[c] || 0) + 1;
      if (passes(t, 'letter')) { const l = firstLetter(t); letterCounts[l] = (letterCounts[l] || 0) + 1; }
    }
    const allCats = new Set(state.terms.map((t) => t.category));
    const allCourses = new Set();
    state.terms.forEach((t) => (t.courses || []).forEach((c) => allCourses.add(c)));

    $('category-filters').innerHTML = CAT_ORDER
      .filter((c) => c === 'all' || allCats.has(c))
      .map((c) => chip('category', c, CAT_PLURAL[c],
        c === 'all' ? state.terms.filter((t) => passes(t, 'category')).length : (catCounts[c] || 0),
        f.category === c)).join('');

    $('course-filters').innerHTML = [chip('course', 'all', 'All courses', null, f.course === 'all')]
      .concat([...allCourses].sort((a, b) => courseName(a).localeCompare(courseName(b), 'en', { sensitivity: 'base' }))
        .map((c) => chip('course', c, courseName(c), courseCounts[c] || 0, f.course === c))).join('');

    const provEl = $('provenance-filters');
    if (provEl) {
      provEl.innerHTML = Object.keys(PROVENANCE_FILTERS).map((key) => {
        const { label, test } = PROVENANCE_FILTERS[key];
        const count = state.terms.filter((t) => passes(t, 'provenance') && test(t)).length;
        return chip('provenance', key, label, count, f.provenance === key);
      }).join('');
    }

    const savedCount = (v) => state.terms.filter((t) => passes(t, 'saved') && (
      v === 'bookmarked' ? state.bookmarks.has(t.id) : v === 'known' ? state.known.has(t.id) : !state.known.has(t.id))).length;
    $('saved-filters').innerHTML = [
      chip('saved', 'all', 'All cards', null, f.saved === 'all'),
      chip('saved', 'bookmarked', 'Bookmarked', savedCount('bookmarked'), f.saved === 'bookmarked'),
      chip('saved', 'known', 'Marked as known', savedCount('known'), f.saved === 'known'),
      chip('saved', 'unknown', 'Still to learn', savedCount('unknown'), f.saved === 'unknown'),
    ].join('');

    const letters = ['all'].concat('ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split(''));
    if (state.terms.some((t) => firstLetter(t) === '#')) letters.push('#');
    $('az-filters').innerHTML = letters.map((l) => {
      const active = f.letter === l;
      const none = l !== 'all' && !letterCounts[l] && !active;
      const text = l === 'all' ? 'All' : l === '#' ? '#<span class="lx-sr"> (terms that start with a number)</span>' : l;
      return `<button type="button" aria-pressed="${active ? 'true' : 'false'}" data-filter-type="letter" data-filter-value="${l}"${none ? ' disabled' : ''}>${text}</button>`;
    }).join('');

    const on = filtersActive();
    $('filters-on').textContent = on ? `${on} on` : '';
    $('filters-reset').hidden = !(on || f.query);
  }

  function resetFilters() {
    state.filter = { category: 'all', course: 'all', provenance: 'all', letter: 'all', saved: 'all', query: '' };
    const input = $('search-input');
    input.value = '';
    $('search-clear').classList.remove('visible');
    refresh();
  }

  // ─── Cards ──────────────────────────────────────────────────────────────
  // Every field from the dictionary is escaped, so none of it is trusted markup.
  function frontHtml(t) {
    const field = t.seedCategory ? `<span class="fc-field"> · ${escapeHtml(t.seedCategory)}</span>` : '';
    const acr = t.acronym ? `<span class="fc-acr">${escapeHtml(t.acronym)}</span>` : '';
    return `
          <button class="fc-flip" type="button" data-flip aria-expanded="false" aria-controls="fcb-${escapeHtml(t.id)}">
            <span class="fc-cat">${escapeHtml(catName(t))}${field}</span>
            <span class="fc-term">${escapeHtml(t.term)}</span>
            ${acr}
            <span class="fc-prov">${provenanceTags(t)}</span>
            <span class="fc-hint">${ICON.turn}<span>Turn over for the definition</span></span>
          </button>`;
  }
  function bookmarkBtn(t) {
    const on = state.bookmarks.has(t.id);
    return `<button class="fc-bm" type="button" data-bookmark-id="${escapeHtml(t.id)}" aria-pressed="${on ? 'true' : 'false'}" aria-label="Bookmark ${escapeHtml(t.term)}">${ICON.bm}</button>`;
  }

  function termCard(t) {
    const id = escapeHtml(t.id);
    return `
      <article class="fc ${catClass(t)}" data-card-id="${id}">
        <div class="fc-inner">
          <div class="fc-face fc-front">${frontHtml(t)}
            ${bookmarkBtn(t)}
          </div>
          <div class="fc-face fc-back" id="fcb-${id}" inert>
            <p class="fc-back-term">${escapeHtml(t.term)}</p>
            <p class="fc-def">${escapeHtml(t.definition || '')}</p>
            <div class="fc-back-actions">
              <button class="btn btn-primary" type="button" data-open-id="${id}">Full entry</button>
              <button class="btn" type="button" data-flip-back>Turn back</button>
            </div>
          </div>
        </div>
      </article>`;
  }

  // Everything the dictionary holds about a term, as sections. Used on the
  // back of the study card and on the term page.
  function entryBody(t, opts) {
    const o = opts || {};
    const out = [];
    out.push(`<div class="lx-entry-meta"><span class="lx-pill lx-pill--cat">${escapeHtml(catName(t))}</span>${
      t.seedCategory ? `<span class="lx-pill">${escapeHtml(t.seedCategory)}</span>` : ''}${
      (t.courses || []).map((c) => `<span class="lx-pill">${escapeHtml(courseName(c))}</span>`).join('')}</div>`);
    out.push(`<div class="lx-sec"><h3>Definition</h3><p>${escapeHtml(t.definition || '')}</p></div>`);
    if (t.example) out.push(`<div class="lx-sec"><h3>Example</h3><div class="example">${escapeHtml(t.example)}</div></div>`);
    if (t.formula) {
      out.push(`<div class="lx-sec"><h3>Formula</h3><div class="formula-box" tabindex="0" role="group" aria-label="Formula">${
        escapeHtml(t.formula.expression || t.formula.formula || '')}</div><p>${
        escapeHtml(t.formula.explanation || t.formula.description || '')}</p></div>`);
    }
    if (t.caseStudy) out.push(`<div class="lx-sec"><h3>Case study</h3><div class="case-study-box">${caseHtml(t.caseStudy)}</div></div>`);
    const related = t.related || [];
    if (related.length) {
      out.push(`<div class="lx-sec"><h3>Related terms</h3><div class="related-list">${
        related.map((rel) => relatedHtml(rel, o.links)).join('')}</div></div>`);
    }
    const hasSources = Boolean(t.sources && t.sources.length);
    out.push(`<div class="lx-sec"><h3>Sources</h3><div class="sources-list${hasSources ? '' : ' sources-empty'}">${sourcesHtml(t)}</div></div>`);
    out.push(`<div class="lx-sec"><h3>How this entry was written</h3><ul class="provenance-list">${provenanceLines(t)}</ul></div>`);
    return out.join('');
  }
  function caseHtml(cs) {
    return `
        <h4>${escapeHtml(cs.title || '')}</h4>
        <div class="meta">${escapeHtml([cs.region, cs.year].filter(Boolean).join(' · '))}</div>
        <p>${escapeHtml(cs.summary || '')}</p>
        ${cs.keyFinding ? `<div class="key-finding"><strong>Key finding:</strong> ${escapeHtml(cs.keyFinding)}</div>` : ''}`;
  }
  function findRelated(rel) {
    const name = String(rel).toLowerCase();
    return state.terms.find((x) => String(x.term).toLowerCase() === name) || state.byId.get(slugify(rel)) || null;
  }
  // A related term that has no entry of its own is shown, and cannot be opened.
  function relatedHtml(rel, asLinks) {
    const match = findRelated(rel);
    if (!match) return `<button class="related-pill" type="button" disabled title="No entry for this term yet">${escapeHtml(rel)}</button>`;
    return asLinks
      ? `<a class="related-pill" href="/impactlex/term.html?id=${encodeURIComponent(match.id)}">${escapeHtml(rel)}</a>`
      : `<button class="related-pill" data-related-id="${escapeHtml(match.id)}" type="button">${escapeHtml(rel)}</button>`;
  }

  function setFlipped(card, flipped, moveFocus) {
    if (!card) return;
    card.classList.toggle('is-flipped', flipped);
    const front = card.querySelector('.fc-front');
    const back = card.querySelector('.fc-back');
    const btn = card.querySelector('[data-flip]');
    if (btn) btn.setAttribute('aria-expanded', flipped ? 'true' : 'false');
    if (front) front.inert = flipped;
    if (back) back.inert = !flipped;
    if (card.classList.contains('fc--study')) {
      const f = $('study-flip');
      if (f) f.textContent = flipped ? 'Turn back' : 'Turn over';
    }
    if (moveFocus) {
      const target = flipped ? card.querySelector('[data-flip-back]') : btn;
      if (target) target.focus({ preventScroll: true });
    }
  }

  // ─── Browse ─────────────────────────────────────────────────────────────
  function renderResults() {
    const terms = visibleTerms();
    const meta = $('results-meta');
    const grid = $('terms-grid');
    const empty = $('empty-state');
    const total = state.terms.length;

    if (state.mode === 'study') return renderStudy(terms);

    meta.textContent = terms.length === total
      ? `All ${total} terms`
      : `${terms.length} of ${total} terms`;

    empty.hidden = terms.length > 0;
    if (!terms.length) {
      $('empty-title').textContent = 'No terms match that search';
      $('empty-text').textContent = 'Try another word, clear the filters, or suggest the term so we can add it.';
      grid.innerHTML = '';
      $('more-wrap').hidden = true;
      return;
    }
    const slice = terms.slice(0, state.shown);
    grid.innerHTML = slice.map(termCard).join('');
    updateMore(terms.length);
  }

  function updateMore(totalVisible) {
    const left = totalVisible - Math.min(state.shown, totalVisible);
    $('more-wrap').hidden = left <= 0;
    if (left > 0) $('more-btn').textContent = `Show ${Math.min(BATCH, left)} more of ${left}`;
  }

  // Add the next batch without redrawing the cards already on the page, so a
  // turned card stays turned and the reader keeps their place.
  function showMore(fromButton) {
    const terms = visibleTerms();
    if (state.shown >= terms.length) return;
    const next = terms.slice(state.shown, state.shown + BATCH);
    state.shown += next.length;
    $('terms-grid').insertAdjacentHTML('beforeend', next.map(termCard).join(''));
    updateMore(terms.length);
    if (fromButton && next.length) {
      const first = $('terms-grid').querySelector(`[data-card-id="${CSS.escape(next[0].id)}"] [data-flip]`);
      if (first) first.focus({ preventScroll: true });
    }
  }

  function renderFeatured() {
    if (!state.terms.length) return;
    const today = new Date();
    const seed = today.getFullYear() * 1000 + (today.getMonth() + 1) * 32 + today.getDate();
    const t = state.terms[seed % state.terms.length];
    $('featured-term').textContent = t.term + (t.acronym ? ` (${t.acronym})` : '');
    $('featured-def').textContent = t.definition;
    $('featured').hidden = false;
    $('featured').setAttribute('data-open-id', t.id);
  }

  // ─── Study ──────────────────────────────────────────────────────────────
  function shuffled(list) {
    const a = list.slice();
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }

  // Rebuild the deck from the filtered set, keeping the current card in view
  // where it is still in the deck.
  function buildDeck(terms, reshuffle) {
    const s = state.study;
    const currentId = s.order[s.index];
    let ids = terms.filter((t) => !(s.hideKnown && state.known.has(t.id))).map((t) => t.id);
    if (s.shuffle) {
      const keep = !reshuffle && s.order.length ? s.order.filter((id) => ids.includes(id)) : [];
      const rest = ids.filter((id) => !keep.includes(id));
      ids = keep.length ? keep.concat(shuffled(rest)) : shuffled(ids);
      // A fresh shuffle starts from the card already on screen.
      if (reshuffle && ids.includes(currentId)) ids = [currentId].concat(ids.filter((id) => id !== currentId));
    }
    s.order = ids;
    const at = ids.indexOf(currentId);
    s.index = at >= 0 ? at : Math.min(s.index, Math.max(0, ids.length - 1));
  }

  function renderStudy(terms, opts) {
    const o = opts || {};
    const s = state.study;
    const list = terms || visibleTerms();
    buildDeck(list, o.reshuffle);

    const total = state.terms.length;
    $('results-meta').textContent = list.length === total
      ? `Studying all ${total} terms`
      : `Studying ${list.length} of ${total} terms`;

    const knownHere = list.filter((t) => state.known.has(t.id)).length;
    $('study-known').textContent = `${knownHere} of ${list.length} marked as known`;
    $('study-shuffle').setAttribute('aria-pressed', s.shuffle ? 'true' : 'false');
    $('study-hide-known').setAttribute('aria-pressed', s.hideKnown ? 'true' : 'false');
    $('study-reset').hidden = state.known.size === 0;

    const empty = $('empty-state');
    const has = s.order.length > 0;
    empty.hidden = has;
    $('study-card').hidden = !has;
    $('study-nav').hidden = !has;
    $('study-bar').hidden = !has;
    if (!has) {
      $('study-count').textContent = 'No cards in this deck';
      if (list.length) {
        $('empty-title').textContent = 'You know every card in this set';
        $('empty-text').textContent = 'Turn off "Hide cards I know" to see them again, or change the filters to study another set.';
      } else {
        $('empty-title').textContent = 'No terms match that search';
        $('empty-text').textContent = 'Try another word, clear the filters, or suggest the term so we can add it.';
      }
      $('study-card').innerHTML = '';
      return;
    }
    drawStudyCard(o.focus);
  }

  function drawStudyCard(focus) {
    const s = state.study;
    const t = state.byId.get(s.order[s.index]);
    if (!t) return;
    const id = escapeHtml(t.id);
    const known = state.known.has(t.id);
    $('study-card').innerHTML = `
      <article class="fc fc--study ${catClass(t)}${known ? ' is-known' : ''}" data-card-id="${id}">
        <div class="fc-inner">
          <div class="fc-face fc-front">${frontHtml(t)}
            ${bookmarkBtn(t)}
          </div>
          <div class="fc-face fc-back" id="fcb-${id}" inert>
            <div class="st-back-head">
              <h2>${escapeHtml(t.term)}${t.acronym ? ` <span class="fc-acr">${escapeHtml(t.acronym)}</span>` : ''}</h2>
              <button class="btn btn-sm" type="button" data-flip-back>Turn back</button>
            </div>
            <span class="lx-tag lx-tag--ok st-known-mark">You marked this as known</span>
            ${entryBody(t)}
          </div>
        </div>
      </article>`;
    $('study-count').textContent = `Card ${s.index + 1} of ${s.order.length}`;
    const bar = $('study-bar');
    bar.setAttribute('aria-valuemax', String(s.order.length));
    bar.setAttribute('aria-valuenow', String(s.index + 1));
    bar.setAttribute('aria-valuetext', `Card ${s.index + 1} of ${s.order.length}`);
    bar.firstElementChild.style.width = `${((s.index + 1) / s.order.length) * 100}%`;
    $('study-prev').disabled = s.order.length < 2;
    $('study-next').disabled = s.order.length < 2;
    $('study-flip').textContent = 'Turn over';
    const mark = $('study-mark');
    mark.setAttribute('aria-pressed', known ? 'true' : 'false');
    mark.textContent = known ? 'Marked as known' : 'Mark as known';
    if (focus) {
      const btn = $('study-card').querySelector('[data-flip]');
      if (btn) btn.focus({ preventScroll: true });
    }
  }

  function studyStep(delta) {
    const s = state.study;
    if (s.order.length < 2) return;
    s.index = (s.index + delta + s.order.length) % s.order.length;
    drawStudyCard(false);
  }
  function studyFlip(moveFocus) {
    const card = $('study-card').querySelector('.fc');
    if (card) setFlipped(card, !card.classList.contains('is-flipped'), moveFocus);
  }
  function toggleKnown() {
    const s = state.study;
    const id = s.order[s.index];
    if (!id) return;
    if (state.known.has(id)) state.known.delete(id); else state.known.add(id);
    writeStore('impactlex:known', [...state.known]);
    if (window.gtag) window.gtag('event', 'mark_known', { term_id: id, action: state.known.has(id) ? 'add' : 'remove' });
    renderFilters();
    if (s.hideKnown || state.filter.saved !== 'all') {
      // The card may have just left the deck: stay at the same position, which
      // now holds the next card.
      const at = s.index;
      s.order = [];
      s.index = at;
      renderStudy();
    } else {
      renderStudy();
    }
  }

  function setMode(mode, opts) {
    state.mode = mode === 'study' ? 'study' : 'browse';
    $('mode-browse').setAttribute('aria-pressed', state.mode === 'browse' ? 'true' : 'false');
    $('mode-study').setAttribute('aria-pressed', state.mode === 'study' ? 'true' : 'false');
    $('browse-view').hidden = state.mode !== 'browse';
    $('study-view').hidden = state.mode !== 'study';
    document.body.classList.toggle('lx-mode-study', state.mode === 'study');
    if (state.mode === 'browse') state.shown = BATCH;
    renderResults();
    if (!(opts && opts.quiet)) syncUrl();
    if (window.gtag && !(opts && opts.quiet)) window.gtag('event', 'impactlex_mode', { mode: state.mode });
  }

  // Search or a filter changed: redraw from the top of the set.
  function refresh() {
    state.shown = BATCH;
    renderFilters();
    renderResults();
    syncUrl();
  }

  // ─── Address ────────────────────────────────────────────────────────────
  const URL_KEYS = { category: 'category', course: 'course', provenance: 'prov', letter: 'letter', saved: 'show' };
  function syncUrl() {
    const p = new URLSearchParams();
    if (state.mode === 'study') p.set('mode', 'study');
    if (state.filter.query) p.set('q', state.filter.query);
    Object.keys(URL_KEYS).forEach((k) => { if (state.filter[k] !== 'all') p.set(URL_KEYS[k], state.filter[k]); });
    if (state.openTermId) p.set('term', state.openTermId);
    const qs = p.toString();
    try { history.replaceState({}, '', window.location.pathname + (qs ? `?${qs}` : '')); } catch (e) { /* file: or sandboxed */ }
  }
  function readUrl() {
    const p = new URLSearchParams(window.location.search);
    const f = state.filter;
    const q = p.get('q');
    if (q) { f.query = q; $('search-input').value = q; $('search-clear').classList.add('visible'); }
    const cat = p.get('category');
    if (cat && state.terms.some((t) => t.category === cat)) f.category = cat;
    const course = p.get('course');
    if (course) {
      // Course lexicon pages link here with their own slug, in any letter case.
      const hit = state.terms.find((t) => (t.courses || []).some((c) => c.toLowerCase() === course.toLowerCase()));
      if (hit) f.course = hit.courses.find((c) => c.toLowerCase() === course.toLowerCase());
    }
    const prov = p.get('prov');
    if (prov && PROVENANCE_FILTERS[prov]) f.provenance = prov;
    const letter = (p.get('letter') || '').toUpperCase();
    if (/^[A-Z#]$/.test(letter)) f.letter = letter;
    const show = p.get('show');
    if (['bookmarked', 'known', 'unknown'].includes(show)) f.saved = show;
    if (p.get('mode') === 'study' || window.location.hash === '#study') state.mode = 'study';
    return p.get('term');
  }

  // ─── Full entry dialog ──────────────────────────────────────────────────
  function showDialog(dlg) {
    if (dlg.open) return;
    if (typeof dlg.showModal === 'function') dlg.showModal(); else dlg.setAttribute('open', '');
    document.body.style.overflow = 'hidden';
  }
  function hideDialog(dlg) {
    if (!dlg.open) return;
    if (typeof dlg.close === 'function') dlg.close(); else dlg.removeAttribute('open');
  }

  function openTerm(id) {
    const t = state.byId.get(id);
    if (!t) return;
    const dlg = $('term-modal');
    if (!dlg.open) state.lastFocus = document.activeElement;
    dlg.className = `lx-dialog ${catClass(t)}`;
    dlg.style.setProperty('--fc-edge', `var(--lx-edge-${CAT_ONE[t.category] ? t.category : 'concept'})`);
    dlg.style.setProperty('--fc-ink', `var(--lx-ink-${CAT_ONE[t.category] ? t.category : 'concept'})`);
    $('modal-title').textContent = t.term;
    $('modal-acronym').textContent = t.acronym || '';
    $('modal-meta').innerHTML = `
      <span class="lx-pill lx-pill--cat">${escapeHtml(catName(t))}</span>
      ${t.seedCategory ? `<span class="lx-pill">${escapeHtml(t.seedCategory)}</span>` : ''}
      ${(t.courses || []).map((c) => `<span class="lx-pill">${escapeHtml(courseName(c))}</span>`).join('')}
    `;
    $('modal-definition').textContent = t.definition || '';
    const exSec = $('modal-example-section');
    if (t.example) { $('modal-example').textContent = t.example; exSec.hidden = false; } else { exSec.hidden = true; }

    const fSec = $('modal-formula-section');
    if (t.formula) {
      $('modal-formula-expr').textContent = t.formula.expression || t.formula.formula || '';
      $('modal-formula-exp').textContent = t.formula.explanation || t.formula.description || '';
      fSec.hidden = false;
    } else fSec.hidden = true;

    const cSec = $('modal-case-section');
    if (t.caseStudy) {
      $('modal-case').innerHTML = caseHtml(t.caseStudy);
      cSec.hidden = false;
    } else cSec.hidden = true;

    const rSec = $('modal-related-section');
    const related = t.related || [];
    if (related.length) {
      $('modal-related').innerHTML = related.map((rel) => relatedHtml(rel, false)).join('');
      rSec.hidden = false;
    } else rSec.hidden = true;

    /* Never hidden. A term with no source used to render exactly like a term
       whose sources happened not to apply, because the section was dropped. */
    const hasSources = Boolean(t.sources && t.sources.length);
    if (hasSources) {
      $('modal-sources').innerHTML = sourcesHtml(t);
    } else {
      $('modal-sources').textContent = 'No source recorded for this entry.';
    }
    $('modal-sources').classList.toggle('sources-empty', !hasSources);
    $('modal-sources-section').hidden = false;

    $('modal-provenance').innerHTML = provenanceLines(t);

    const bm = $('modal-bookmark');
    const on = state.bookmarks.has(t.id);
    bm.setAttribute('aria-pressed', on ? 'true' : 'false');
    bm.querySelector('span').textContent = on ? 'Bookmarked' : 'Bookmark';
    bm.dataset.termId = t.id;

    state.openTermId = t.id;
    showDialog(dlg);
    dlg.scrollTop = 0;
    $('modal-title').focus({ preventScroll: true });
    syncUrl();
    if (window.gtag) window.gtag('event', 'view_term', { term_id: t.id });
  }

  function onDialogClosed(dlg) {
    if (!document.querySelector('dialog[open]')) document.body.style.overflow = '';
    if (dlg.id === 'term-modal') {
      state.openTermId = null;
      syncUrl();
    }
    const back = state.lastFocus;
    if (back && document.contains(back) && !document.querySelector('dialog[open]')) {
      state.lastFocus = null;
      try { back.focus({ preventScroll: true }); } catch (e) { /* gone */ }
    }
  }

  function closeModal() {
    hideDialog($('term-modal'));
    hideDialog($('submit-modal'));
  }

  function openSubmit(prefill) {
    const termDlg = $('term-modal');
    const from = termDlg.open ? state.lastFocus : document.activeElement;
    hideDialog(termDlg);
    state.lastFocus = from;
    if (prefill) {
      $('submit-term').value = prefill.term;
      $('submit-category').value = prefill.category;
      $('submit-definition').value = prefill.definition || '';
      $('submit-example').value = prefill.example || '';
    }
    showDialog($('submit-modal'));
    $('submit-term').focus();
  }

  // ─── Bookmarks ──────────────────────────────────────────────────────────
  function toggleBookmark(id) {
    if (state.bookmarks.has(id)) state.bookmarks.delete(id);
    else state.bookmarks.add(id);
    const on = state.bookmarks.has(id);
    writeStore('impactlex:bookmarks', [...state.bookmarks]);
    // Update card buttons and the dialog button without a full redraw.
    document.querySelectorAll(`[data-bookmark-id="${CSS.escape(String(id))}"]`).forEach((el) => el.setAttribute('aria-pressed', on ? 'true' : 'false'));
    const modalBm = $('modal-bookmark');
    if (modalBm.dataset.termId === id) {
      modalBm.setAttribute('aria-pressed', on ? 'true' : 'false');
      modalBm.querySelector('span').textContent = on ? 'Bookmarked' : 'Bookmark';
    }
    renderFilters();
    if (window.gtag) window.gtag('event', 'bookmark_term', { term_id: id, action: on ? 'add' : 'remove' });
  }

  // ─── Submission ─────────────────────────────────────────────────────────
  /* A suggestion is kept in localStorage first, then sent to Supabase. The
     table accepts inserts from anyone and only an admin can read them, so a
     failed send leaves the entry queued and the next visit tries again. */
  const QUEUE_KEY = 'impactlex:contributions-queue';
  const readQueue = () => { const q = readStore(QUEUE_KEY, []); return Array.isArray(q) ? q : []; };
  const writeQueue = (q) => writeStore(QUEUE_KEY, q);

  async function sendContribution(entry) {
    if (!CONFIG.supabaseUrl || !CONFIG.supabaseAnonKey) return false;
    const row = {
      term: entry.term,
      category: entry.category || null,
      definition: entry.definition || null,
      example: entry.example || null,
      email: entry.email || null,
    };
    try {
      const res = await fetch(`${CONFIG.supabaseUrl}/rest/v1/impactlex_contributions`, {
        method: 'POST',
        headers: {
          apikey: CONFIG.supabaseAnonKey,
          Authorization: `Bearer ${CONFIG.supabaseAnonKey}`,
          'Content-Type': 'application/json',
          Prefer: 'return=minimal',
        },
        body: JSON.stringify(row),
      });
      return res.ok;
    } catch (err) {
      return false;
    }
  }

  async function flushQueue() {
    const left = [];
    for (const entry of readQueue()) {
      if (!(await sendContribution(entry))) left.push(entry);
    }
    writeQueue(left);
    return left.length === 0;
  }

  async function submitContribution(payload) {
    const entry = {
      id: `c-${Date.now()}-${Math.random().toString(36).slice(2, 8)}`,
      ...payload,
      status: 'pending',
      createdAt: new Date().toISOString(),
    };
    writeQueue([...readQueue(), entry]);
    const sent = await flushQueue();
    return { ok: true, queued: !sent };
  }

  // ─── Utilities ──────────────────────────────────────────────────────────
  function slugify(s) {
    return String(s).toLowerCase()
      .replace(/\([^)]*\)/g, '')
      .replace(/[^a-z0-9\s-]/g, '')
      .trim().replace(/\s+/g, '-').replace(/-+/g, '-');
  }
  function escapeHtml(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }
  let statusTimer;
  function showStatus(text, kind) {
    const b = $('status-banner');
    if (!b) return;
    b.hidden = false;
    b.className = 'lx-status' + (kind ? ' ' + kind : '');
    $('status-text').textContent = text;
    clearTimeout(statusTimer);
    if (!kind) statusTimer = setTimeout(() => { b.hidden = true; }, 6000);
  }
  const typingIn = (el) => el && (/^(INPUT|TEXTAREA|SELECT)$/.test(el.tagName) || el.isContentEditable);

  // ─── Event wiring ───────────────────────────────────────────────────────
  function wire() {
    $('modal-close').addEventListener('click', closeModal);
    $('submit-close').addEventListener('click', closeModal);
    $('submit-cancel').addEventListener('click', closeModal);
    document.querySelectorAll('dialog.lx-dialog').forEach((dlg) => {
      // A click on the backdrop lands on the dialog element itself.
      dlg.addEventListener('click', (e) => { if (e.target === dlg) hideDialog(dlg); });
      dlg.addEventListener('close', () => onDialogClosed(dlg));
    });

    // Search
    const searchInput = $('search-input');
    const searchClear = $('search-clear');
    let searchTimer;
    searchInput.addEventListener('input', (e) => {
      const v = e.target.value;
      searchClear.classList.toggle('visible', v.length > 0);
      clearTimeout(searchTimer);
      searchTimer = setTimeout(() => {
        state.filter.query = v.trim();
        refresh();
        if (window.gtag && v.length >= 3) window.gtag('event', 'search', { search_term: v });
      }, 120);
    });
    searchClear.addEventListener('click', () => {
      searchInput.value = '';
      state.filter.query = '';
      searchClear.classList.remove('visible');
      refresh();
      searchInput.focus();
    });

    $('mode-browse').addEventListener('click', () => setMode('browse'));
    $('mode-study').addEventListener('click', () => setMode('study'));
    $('filters-reset').addEventListener('click', resetFilters);
    $('empty-reset').addEventListener('click', () => {
      if (state.mode === 'study') state.study.hideKnown = false;
      resetFilters();
    });
    $('more-btn').addEventListener('click', () => showMore(true));
    if ('IntersectionObserver' in window) {
      // Draw the next batch as the reader nears the end of the grid. The
      // button stays for keyboards and for browsers without the observer.
      new IntersectionObserver((entries) => {
        if (state.mode === 'browse' && entries.some((en) => en.isIntersecting)) showMore(false);
      }, { rootMargin: '600px 0px' }).observe($('more-sentinel'));
    }

    // Study controls
    $('study-prev').addEventListener('click', () => studyStep(-1));
    $('study-next').addEventListener('click', () => studyStep(1));
    $('study-flip').addEventListener('click', () => studyFlip(false));
    $('study-mark').addEventListener('click', toggleKnown);
    $('study-shuffle').addEventListener('click', () => {
      state.study.shuffle = !state.study.shuffle;
      renderStudy(null, { reshuffle: true });
    });
    $('study-hide-known').addEventListener('click', () => {
      state.study.hideKnown = !state.study.hideKnown;
      renderStudy();
    });
    $('study-reset').addEventListener('click', () => {
      state.known.clear();
      writeStore('impactlex:known', []);
      renderFilters();
      renderStudy();
    });

    // Cards, chips and related terms (event delegation)
    document.addEventListener('click', (e) => {
      const chipEl = e.target.closest('[data-filter-type]');
      if (chipEl) {
        const type = chipEl.dataset.filterType;
        const value = chipEl.dataset.filterValue;
        // A second press on the chosen letter clears it.
        state.filter[type] = (type === 'letter' && state.filter.letter === value) ? 'all' : value;
        refresh();
        const again = document.querySelector(`[data-filter-type="${type}"][data-filter-value="${CSS.escape(state.filter[type])}"]`);
        if (again) again.focus({ preventScroll: true });
        return;
      }
      if (e.target.closest('[data-suggest]')) { openSubmit(null); return; }
      const bm = e.target.closest('[data-bookmark-id]');
      if (bm) { toggleBookmark(bm.dataset.bookmarkId); return; }
      const open = e.target.closest('[data-open-id]');
      if (open) { openTerm(open.dataset.openId); return; }
      const rel = e.target.closest('[data-related-id]');
      if (rel) { openTerm(rel.dataset.relatedId); return; }
      const flip = e.target.closest('[data-flip]');
      if (flip) { setFlipped(flip.closest('.fc'), true, true); return; }
      const flipBack = e.target.closest('[data-flip-back]');
      if (flipBack) { setFlipped(flipBack.closest('.fc'), false, true); return; }
      // A click on the back of a small card, outside its buttons, turns it back.
      const back = e.target.closest('.fc-back');
      if (back && !e.target.closest('a, button, .formula-box') && !back.closest('.fc--study')
          && !String(window.getSelection && window.getSelection()).trim()) {
        setFlipped(back.closest('.fc'), false, false);
      }
    });

    // Keys for the study deck. They stay out of the way of typing, of open
    // dialogs and of the browser's own shortcuts.
    document.addEventListener('keydown', (e) => {
      if (state.mode !== 'study' || e.altKey || e.ctrlKey || e.metaKey) return;
      if (document.querySelector('dialog[open]') || typingIn(e.target)) return;
      if (e.target.closest && e.target.closest('.im-sc')) return;
      if (e.key === 'ArrowRight') { e.preventDefault(); studyStep(1); }
      else if (e.key === 'ArrowLeft') { e.preventDefault(); studyStep(-1); }
      else if (e.key === 'k' || e.key === 'K') { toggleKnown(); }
      else if ((e.key === ' ' || e.key === 'Enter') && !e.target.closest('a, button, summary, [tabindex]')) {
        e.preventDefault();
        studyFlip(false);
      }
    });

    // Full-entry actions
    $('modal-bookmark').addEventListener('click', (e) => {
      const id = e.currentTarget.dataset.termId;
      if (id) toggleBookmark(id);
    });
    $('modal-share').addEventListener('click', async (e) => {
      const id = $('modal-bookmark').dataset.termId;
      const url = `${window.location.origin}/impactlex/?term=${encodeURIComponent(id)}`;
      const span = e.currentTarget.querySelector('span');
      try {
        await navigator.clipboard.writeText(url);
        span.textContent = 'Link copied';
      } catch (err) {
        span.textContent = 'Could not copy';
      }
      setTimeout(() => { span.textContent = 'Copy link'; }, 1800);
    });
    $('modal-suggest-edit').addEventListener('click', () => {
      const t = state.byId.get($('modal-bookmark').dataset.termId);
      if (t) openSubmit(t);
    });

    $('submit-form').addEventListener('submit', async (e) => {
      e.preventDefault();
      const payload = {
        term: $('submit-term').value.trim(),
        category: $('submit-category').value,
        definition: $('submit-definition').value.trim(),
        example: $('submit-example').value.trim(),
        email: $('submit-email').value.trim(),
      };
      const result = await submitContribution(payload);
      if (result.ok) {
        const msg = result.queued
          ? 'Thank you. Your suggestion is saved on this device and will be sent the next time you open the dictionary with a connection.'
          : 'Thank you. Your suggestion is in the moderation queue.';
        showStatus(msg, '');
        closeModal();
        e.target.reset();
        if (window.gtag) window.gtag('event', 'submit_contribution', { queued: result.queued });
      }
    });
  }

  // ─── Term page ──────────────────────────────────────────────────────────
  async function initTermPage() {
    const params = new URLSearchParams(window.location.search);
    const slug = params.get('id') || params.get('term') || window.location.hash.slice(1);
    try {
      await loadSnapshot();
    } catch (err) {
      $('loading').hidden = true;
      $('term-content').remove();
      $('not-found').hidden = false;
      return;
    }
    const t = state.byId.get(slug);
    $('loading').hidden = true;
    // The page carries two headings in its markup and keeps one.
    if (!t) { $('term-content').remove(); $('not-found').hidden = false; return; }
    $('not-found').remove();

    document.title = `${t.term} | ImpactLex | ImpactMojo`;
    const desc = document.querySelector('meta[name="description"]');
    if (desc) desc.setAttribute('content', String(t.definition || '').slice(0, 155));

    $('breadcrumb-term').textContent = t.term;
    $('term-title').textContent = t.term;
    if (t.acronym) {
      $('term-acronym').textContent = t.acronym;
      $('term-acronym').hidden = false;
    }
    $('term-card').className = `lx-termcard ${catClass(t)}`;
    $('term-body').innerHTML = entryBody(t, { links: true });
    $('term-open').href = `/impactlex/?term=${encodeURIComponent(t.id)}`;
    $('term-content').hidden = false;
    if (window.gtag) window.gtag('event', 'view_term', { term_id: t.id });
  }

  // ─── Init ───────────────────────────────────────────────────────────────
  async function init() {
    if (PAGE === 'term') return initTermPage();
    wire();
    try {
      await loadSnapshot();
    } catch (err) {
      showStatus(`Could not load the dictionary: ${err.message}`, 'offline');
      return;
    }
    updateStats();
    const termId = readUrl();
    if (filtersActive()) $('filters').open = true;
    renderFilters();
    renderFeatured();
    setMode(state.mode, { quiet: true });
    if (termId) openTerm(termId);
    flushQueue(); // send any suggestion saved while offline
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
