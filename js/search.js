/* ============================================================
   ImpactMojo site search: Ctrl+K / Cmd+K, "/" or the search button.
   Fuse.js over data/search-index.json for the results, plus two small
   separate Fuse instances: short answers from data/faq.json (shown first,
   under "Answers") and Field Radio transcripts. Opening with a string,
   ImpactMojoSearch.open('certificate'), starts with that query.
   ============================================================ */
(function () {
  'use strict';

  var FUSE_CDN = 'https://cdn.jsdelivr.net/npm/fuse.js@7.0.0/dist/fuse.min.js';
  var INDEX_URL = '/data/search-index.json';

  var fuse = null;
  var searchData = null;
  /* Set when Fuse.js or the index cannot be fetched (jsDelivr blocked, offline,
     a 404). Without it the panel kept showing its idle prompt whatever was
     typed, so a visitor could not tell a broken search from an empty one. */
  var loadFailed = false;
  var loading = false;

  /* The main index config. Exposed below as _options so the ranking can be
     replayed in node against the real index. */
  var FUSE_OPTIONS = {
    keys: [
      { name: 'title', weight: 0.45 },
      { name: 'description', weight: 0.25 },
      { name: 'tags', weight: 0.15 },
      { name: 'category', weight: 0.1 },
      { name: 'id', weight: 0.05 }
    ],
    threshold: 0.35,
    distance: 200,
    includeScore: true,
    minMatchCharLength: 2,
    limit: 20
  };

  /* Synonyms. Each rule matches the lowercased query and names a second query
     that is run alongside it. People search with the words they use at work
     ("M&E", "pricing", "login"); the index is written with the site's own
     names ("MEL", "Membership", "Log in"). Whole-query rules are anchored so
     that, for example, "cost effectiveness" is not read as a price question. */
  var SYNONYMS = [
    [/(^|\s)(m\s*&\s*e|m\s+and\s+e|monitoring\s*(and|&)?\s*evaluation)(\s|$)/, 'monitoring and evaluation'],
    [/^labs?$/, 'free studio'],
    [/^(membership\s+|subscription\s+)?(price|prices|pricing|cost|costs|fees?|plans?)$/, 'membership'],
    [/^(log\s*-?\s*in|sign\s*-?\s*in|signin)$/, 'log in'],
    [/^(sign\s*-?\s*up|register|create\s+(an\s+)?account)$/, 'create a free account'],
    [/^r$/, 'R language'],
    [/^(hindi|tamil|bengali|bangla|telugu|marathi|languages?|translations?|translate)$/, 'languages'],
    [/^(beginners?|start\s+here|basics)$/, 'start here']
  ];

  function synonymFor(query) {
    var q = query.toLowerCase().trim();
    for (var i = 0; i < SYNONYMS.length; i++) {
      if (SYNONYMS[i][0].test(q)) {
        var alt = SYNONYMS[i][1];
        return alt.toLowerCase() === q ? null : alt;
      }
    }
    return null;
  }

  /* Paid products and the Marginalia specials matched free courses and tools
     word for word, so "logframe" put a paid template beside the free builder
     and "monitoring and evaluation" led with three specials. A small penalty
     moves them below a free item of near-equal score and leaves a clearly
     better match where it was. */
  var TYPE_PENALTY = { product: 0.08, special: 0.08 };
  var SYNONYM_BONUS = 0.05;

  function rank(f, query) {
    var alt = synonymFor(query);
    var lists = alt ? [f.search(alt, { limit: 30 }), f.search(query, { limit: 30 })]
                    : [f.search(query, { limit: 30 })];
    var best = {}, order = [];
    lists.forEach(function (list, li) {
      // A synonym is a curated reading of what the person meant, so its hits
      // get a small bonus: "M&E" should reach the MEL courses ahead of pages
      // that merely contain the letters.
      var bonus = alt && li === 0 ? SYNONYM_BONUS : 0;
      list.forEach(function (r) {
        var id = r.item.id || r.item.url;
        var s = (r.score || 0) + (TYPE_PENALTY[r.item.type] || 0) - bonus;
        if (!(id in best)) { best[id] = { item: r.item, score: s }; order.push(id); }
        else if (s < best[id].score) best[id].score = s;
      });
    });
    // Array.prototype.sort is stable, so on a tie the synonym's hits (searched
    // first) stay ahead of the literal query's.
    return order.map(function (id) { return best[id]; })
      .sort(function (a, b) { return a.score - b.score; })
      .slice(0, 15);
  }

  function priceOf(item) {
    if (item.price) return item.price;
    var tags = item.tags || [];
    for (var i = 0; i < tags.length; i++) {
      if (/^₹\s?[0-9][0-9,]*$/.test(tags[i])) return tags[i];
    }
    return '';
  }
  var modal = null;
  var input = null;
  var resultsList = null;
  var countEl = null;
  var liveEl = null;
  var visible = false;
  var opener = null;      // the element that had focus when the panel opened
  var openedAt = 0;

  /* What each result is, in the reader's words. The index's own `type` values
     are internal ("lab", "book-summary", "dataverse"), and a course's category
     says whether it is a flagship or a 101 deck. */
  var TYPE_LABEL = {
    bct: 'BCT technique', dataverse: 'Dataset', game: 'Game', lab: 'Studio',
    page: 'Page', 'book-summary': 'Reading companion', blog: 'Blog post',
    'deep-dive': 'Deep dive', product: 'Product', 'practice-pack': 'Practice pack',
    tool: 'Tool', 'data-dive': 'Data note', 'data-note': 'Data note',
    timeline: 'Timeline', poster: 'Poster', reference: 'Reference',
    handout: 'Handout', challenge: 'Challenge', showcase: 'Work sample',
    special: 'Special', 'field-radio': 'Field Radio', explorer: 'Data explorer',
    'law-guide': 'Law guide', 'reading-list': 'Reading list', theory: 'Theory',
    fundamental: 'Fundamentals', 'landing-page': 'Page', dataset: 'Dataset'
  };

  function typeLabel(item) {
    if (item.type === 'course') {
      var c = String(item.category || '');
      if (/101|foundational/i.test(c) || /^\/101-courses\//.test(item.url || '')) return '101 course';
      if (/workbook/i.test(c)) return 'Practice workbook';
      return 'Course';
    }
    if (item.type === 'tool' && /code school/i.test(item.category || '')) return 'Code School';
    return TYPE_LABEL[item.type] || 'Page';
  }

  /* Suggestions shown before anything is typed and after a search that finds
     nothing. Each one returns something on the live index. */
  var SUGGESTIONS = ['theory of change', 'NFHS', 'certificate', 'sample size', 'gender', 'R and Python'];

  /* ---- Recent searches (this browser only) ---- */
  var RECENT_KEY = 'im-search-recent';
  function readRecent() {
    try {
      var v = JSON.parse(window.localStorage.getItem(RECENT_KEY) || '[]');
      return Array.isArray(v) ? v.filter(function (s) { return typeof s === 'string' && s; }).slice(0, 5) : [];
    } catch (e) { return []; }
  }
  function saveRecent(q) {
    q = String(q || '').trim();
    if (q.length < 2) return;
    var list = readRecent().filter(function (s) { return s.toLowerCase() !== q.toLowerCase(); });
    list.unshift(q);
    try { window.localStorage.setItem(RECENT_KEY, JSON.stringify(list.slice(0, 5))); } catch (e) { /* private mode */ }
  }
  function clearRecent() {
    try { window.localStorage.removeItem(RECENT_KEY); } catch (e) { /* private mode */ }
  }

  /* ---- Load Fuse.js ---- */
  function loadFuse(cb) {
    if (window.Fuse) return cb();
    var s = document.createElement('script');
    s.src = FUSE_CDN;
    s.onload = cb;
    s.onerror = function () {
      console.warn('ImpactMojo Search: Failed to load Fuse.js');
      markFailed();
    };
    document.head.appendChild(s);
  }

  /* ---- Load search index ---- */
  function loadIndex(cb) {
    if (searchData) return cb(searchData);
    var controller = window.AbortController ? new AbortController() : null;
    var timeoutId = controller ? setTimeout(function () { controller.abort(); }, 10000) : null;
    fetch(INDEX_URL, controller ? { signal: controller.signal } : {})
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(function (data) { searchData = data; cb(data); })
      .catch(function (e) { console.warn('ImpactMojo Search: Failed to load index', e); markFailed(); })
      .finally(function () { if (timeoutId) clearTimeout(timeoutId); });
  }

  function markFailed() {
    loadFailed = true;
    loading = false;
    if (visible && input) renderResults(input.value.trim());
  }

  /* ---- Initialize Fuse instance ---- */
  function initFuse() {
    loadFailed = false;
    loading = true;
    loadFuse(function () {
      loadIndex(function (data) {
        loading = false;
        fuse = new window.Fuse(data, FUSE_OPTIONS);
        if (visible && input) renderResults(input.value.trim());
      });
    });
  }

  /* ---- Answers ----
     Short answers to common questions about the platform (certificates,
     prices, languages, how to get in touch), from data/faq.json. They replace
     the answer bank of the retired Mojini chat assistant, and they are shown
     above the results because a question with a one-line answer should not
     send anyone to a page to find it.

     Like the Field Radio transcripts below, they get their own small Fuse
     instance and are fetched when someone first opens search. Adding them to
     the main index would move its ranking (.claude/rules/testing.md item 22
     measured that for transcripts), and the main options are not touched.

     An answer sits above everything else, so a wrong one costs more than a
     missing one, and plain fuzzy matching was measured to be too loose for
     that: "caste" scored 0.05 against the certificate answer, one letter
     away from "case". So the query is cut to its content words, and every
     one of them must appear in the question or the keywords of the same
     entry (Fuse extended search: 'word is an exact substring). Only words of
     seven letters or more are matched fuzzily, which keeps "certficate"
     working. The answer text itself is not searched. */
  var FAQ_URL = '/data/faq.json';
  var ANSWER_OPTIONS = {
    keys: [
      { name: 'keywords', weight: 0.6 },
      { name: 'q', weight: 0.4 }
    ],
    useExtendedSearch: true,
    threshold: 0.3,
    ignoreLocation: true,
    includeScore: true
  };
  var ANSWER_MAX_SCORE = 0.4;
  var STOPWORDS = ('a an the is are am be do does did can could how what where which who whom why when ' +
    'i im me my we our you your it its to of for in on at by with and or about any there this that ' +
    'get got have has need want please tell show find give').split(' ');
  var faqData = null, faqFuse = null, faqTried = false;

  function answerQuery(text) {
    var words = String(text).toLowerCase().replace(/[^a-z0-9\s-]/g, ' ').split(/\s+/);
    var out = [];
    words.forEach(function (w) {
      w = w.replace(/^-+|-+$/g, '');
      if (w.length < 2 || STOPWORDS.indexOf(w) !== -1) return;
      out.push(w.length >= 7 ? w : "'" + w);
    });
    return out.join(' ');
  }

  function loadAnswers() {
    if (faqTried) return;
    faqTried = true;
    fetch(FAQ_URL)
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(function (d) {
        faqData = (d && Array.isArray(d.answers) ? d.answers : []).filter(function (a) { return a && a.q && a.a; });
        if (visible && input) renderResults(input.value.trim());
      })
      .catch(function (e) { faqTried = false; console.warn('ImpactMojo Search: answers unavailable', e); });
  }

  function answerHits(query) {
    if (!faqFuse && faqData && faqData.length && window.Fuse) faqFuse = new window.Fuse(faqData, ANSWER_OPTIONS);
    if (!faqFuse || query.length < 3) return [];
    var alt = synonymFor(query);
    var best = {}, order = [];
    (alt ? [alt, query] : [query]).forEach(function (q) {
      var expr = answerQuery(q);
      if (!expr) return;
      faqFuse.search(expr).forEach(function (r) {
        if (r.score > ANSWER_MAX_SCORE) return;
        var id = r.item.id || r.item.q;
        if (!(id in best)) { best[id] = r; order.push(id); }
        else if (r.score < best[id].score) best[id] = r;
      });
    });
    return order.map(function (id) { return best[id]; })
      .sort(function (a, b) { return a.score - b.score; })
      .slice(0, 2)
      .map(function (r) { return r.item; });
  }

  /* An answer is plain text. Escape it, then make two things clickable:
     root-relative .html paths on this site and https links. Nothing else in
     the text can become markup. */
  function linkify(text) {
    var s = escapeHTML(text);
    s = s.replace(/https:\/\/[^\s<"']*[^\s<"'.,;:)]/g, function (u) {
      return '<a href="' + u + '" target="_blank" rel="noopener noreferrer">' + u + '</a>';
    });
    s = s.replace(/(^|[\s(])(\/[A-Za-z0-9_\-\/]+\.html)/g, function (m, pre, path) {
      return pre + '<a href="' + path + '">' + path + '</a>';
    });
    return s;
  }

  /* ---- Field Radio transcripts ----
     The station's clips carry ~45,000 characters of transcript. They are
     deliberately NOT in data/search-index.json: that file is fetched on every
     page load (initFuse runs on DOMContentLoaded below), so carrying them
     there would charge every visitor on every page for a search few of them
     run. They are fetched here instead, once, when search is first opened.

     Why a second Fuse instance rather than another key on the main one: the
     main index uses Fuse's default location scoring with distance 200, which
     ranks a match by how near it sits to the start of the field. That is fine
     for a title and useless for a 4,000-character transcript -- measured, a
     transcript key on the main index matched nothing that was not in the
     opening line. ignoreLocation fixes it, and setting it globally moved the
     top result on a quarter of ordinary queries. So it is set here only. */
  var trClips = null, trFuse = null, trTried = false;

  function loadTranscripts() {
    if (trTried) return;
    trTried = true;
    fetch('/data/field-radio.json')
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(function (d) {
        trClips = (d && Array.isArray(d.clips) ? d.clips : []).filter(function (c) {
          return c && c.id && c.transcript;
        });
      })
      .catch(function (e) { console.warn('ImpactMojo Search: transcripts unavailable', e); });
  }

  /* Clips whose transcript matches, as index entries, minus any already shown. */
  function transcriptHits(query, already) {
    // Built on first use, so it does not matter whether Fuse or the clips
    // arrived first.
    if (!trFuse && trClips && trClips.length && window.Fuse) {
      trFuse = new window.Fuse(trClips, {
        keys: [{ name: 'transcript' }],
        threshold: 0.3,
        ignoreLocation: true,
        minMatchCharLength: 4,
        includeScore: true,
        limit: 5
      });
    }
    if (!trFuse || !searchData || query.length < 4) return [];
    var seen = {};
    already.forEach(function (r) { seen[r.item.id] = true; });
    var out = [];
    trFuse.search(query).forEach(function (r) {
      var entry = null;
      for (var i = 0; i < searchData.length; i++) {
        if (searchData[i].id === 'FIELD-RADIO-' + r.item.id) { entry = searchData[i]; break; }
      }
      if (entry && !seen[entry.id]) { seen[entry.id] = true; out.push({ item: entry }); }
    });
    return out;
  }

  /* ---- Build the panel ---- */
  var SEARCH_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>';

  function createModal() {
    modal = document.createElement('div');
    modal.id = 'impactmojo-search-modal';
    modal.innerHTML =
      '<div class="ims-backdrop" aria-hidden="true"></div>' +
      '<div class="ims-dialog" role="dialog" aria-modal="true" aria-labelledby="ims-heading">' +
        '<h2 id="ims-heading" class="ims-sr">Search ImpactMojo</h2>' +
        '<div class="ims-input-row">' +
          '<span class="ims-search-icon">' + SEARCH_SVG + '</span>' +
          '<input id="ims-input" type="search" placeholder="Search courses, tools, data and answers" ' +
            'autocomplete="off" spellcheck="false" enterkeyhint="go" aria-label="Search ImpactMojo" aria-describedby="ims-help">' +
          '<button type="button" class="ims-close" aria-label="Close search"><span class="ims-close-key">Esc</span>' +
            '<svg class="ims-close-x" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>' +
          '</button>' +
        '</div>' +
        '<div id="ims-results" class="ims-results"></div>' +
        '<div class="ims-footer">' +
          '<span id="ims-help" class="ims-help"><kbd>&uarr;</kbd><kbd>&darr;</kbd> to move, <kbd>Enter</kbd> to open, <kbd>Esc</kbd> to close</span>' +
          '<span class="ims-count" id="ims-count"></span>' +
        '</div>' +
        '<div id="ims-live" class="ims-sr" role="status" aria-live="polite"></div>' +
      '</div>';
    document.body.appendChild(modal);

    input = document.getElementById('ims-input');
    resultsList = document.getElementById('ims-results');
    countEl = document.getElementById('ims-count');
    liveEl = document.getElementById('ims-live');

    modal.querySelector('.ims-backdrop').addEventListener('click', closeSearch);
    modal.querySelector('.ims-close').addEventListener('click', closeSearch);
    input.addEventListener('input', onInput);
    input.addEventListener('keydown', onInputKeydown);
    modal.addEventListener('keydown', onPanelKeydown);

    resultsList.addEventListener('click', function (e) {
      var chip = e.target.closest('[data-q]');
      if (chip) {
        e.preventDefault();
        input.value = chip.getAttribute('data-q');
        renderResults(input.value.trim());
        input.focus();
        return;
      }
      if (e.target.closest('.ims-clear-recent')) {
        e.preventDefault();
        clearRecent();
        renderResults('');
        input.focus();
        return;
      }
      var link = e.target.closest('a[href]');
      if (link) {
        saveRecent(input.value);
        // A link to another part of this page does not unload it, so close.
        if (link.target !== '_blank') setTimeout(closeSearch, 0);
      }
    });
  }

  /* ---- Styles ----
     The panel carries its own tokens, light and dark, so it reads the same on
     every page whatever that page's own palette declares. Ink #0F172A on
     white is 17.9:1, muted #475569 is 7.6:1, accent ink #0369A1 is 5.9:1; in
     dark, #F1F5F9, #CBD5E1 and #7DD3FC on #0F172A are 16.3:1, 12.0:1 and
     11.0:1. */
  function injectStyles() {
    var LIGHT = '--ims-bg:#FFFFFF;--ims-ink:#0F172A;--ims-muted:#475569;--ims-accent:#0369A1;--ims-border:#E2E8F0;' +
      '--ims-hover:#F1F5F9;--ims-active:#E0F2FE;--ims-chip:#F8FAFC;--ims-tag-bg:#F0F9FF;--ims-tag-ink:#075985;' +
      '--ims-answer:#F0F9FF;--ims-answer-bd:#BAE6FD;--ims-mark:#FEF3C7;--ims-backdrop:rgba(15,23,42,.45)';
    var DARK = '--ims-bg:#0F172A;--ims-ink:#F1F5F9;--ims-muted:#CBD5E1;--ims-accent:#7DD3FC;--ims-border:#334155;' +
      '--ims-hover:#1E293B;--ims-active:#0C4A6E;--ims-chip:#1E293B;--ims-tag-bg:#082F49;--ims-tag-ink:#BAE6FD;' +
      '--ims-answer:#0B2537;--ims-answer-bd:#075985;--ims-mark:#713F12;--ims-backdrop:rgba(2,6,23,.7)';
    var M = '#impactmojo-search-modal';
    var css = document.createElement('style');
    css.textContent =
      M + '{' + LIGHT + ';display:none;position:fixed;inset:0;z-index:99999;font-family:"Inter",system-ui,-apple-system,"Segoe UI",sans-serif;' +
        'color:var(--ims-ink);-webkit-font-smoothing:antialiased;line-height:1.45;text-align:left}' +
      'html[data-theme="dark"] ' + M + ',html.dark ' + M + '{' + DARK + '}' +
      '@media(prefers-color-scheme:dark){html:not([data-theme]) ' + M + '{' + DARK + '}}' +
      M + '.ims-open{display:flex;align-items:flex-start;justify-content:center;padding:min(12vh,96px) 16px 16px}' +
      M + ' *{box-sizing:border-box}' +
      '.ims-sr{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}' +
      '.ims-backdrop{position:fixed;inset:0;background:var(--ims-backdrop);backdrop-filter:blur(3px);-webkit-backdrop-filter:blur(3px)}' +
      '.ims-dialog{position:relative;width:100%;max-width:680px;max-height:min(640px,calc(100vh - 32px));max-height:min(640px,calc(100dvh - 32px));' +
        'background:var(--ims-bg);color:var(--ims-ink);border:1px solid var(--ims-border);border-radius:14px;' +
        'box-shadow:0 24px 60px rgba(15,23,42,.28);display:flex;flex-direction:column;overflow:hidden}' +
      '.ims-input-row{display:flex;align-items:center;gap:10px;padding:12px 14px 12px 18px;border-bottom:1px solid var(--ims-border)}' +
      '.ims-search-icon{display:flex;color:var(--ims-muted);flex-shrink:0}.ims-search-icon svg{width:20px;height:20px}' +
      '#ims-input{flex:1;min-width:0;border:0;outline:none;font:inherit;font-size:1.0625rem;padding:8px 0;background:transparent;color:var(--ims-ink);-webkit-appearance:none;appearance:none}' +
      '#ims-input::-webkit-search-cancel-button{-webkit-appearance:none}' +
      '#ims-input::placeholder{color:var(--ims-muted);opacity:1}' +
      '.ims-close{display:inline-flex;align-items:center;justify-content:center;min-width:44px;min-height:36px;padding:4px 8px;border:1px solid var(--ims-border);' +
        'border-radius:8px;background:var(--ims-chip);color:var(--ims-muted);font:inherit;font-size:.75rem;font-weight:600;cursor:pointer;flex-shrink:0}' +
      '.ims-close:hover{color:var(--ims-ink)}.ims-close-x{display:none;width:18px;height:18px}' +
      '.ims-results{overflow-y:auto;overscroll-behavior:contain;flex:1;padding:6px 8px 10px}' +
      '.ims-group{margin:0;padding:12px 10px 6px;font-size:.75rem;font-weight:600;letter-spacing:.04em;text-transform:uppercase;color:var(--ims-muted);display:flex;align-items:center;justify-content:space-between;gap:8px}' +
      '.ims-list{list-style:none;margin:0;padding:0}' +
      '.ims-result{display:block;padding:10px 12px;border-radius:10px;text-decoration:none;color:var(--ims-ink);outline:none;border:1px solid transparent}' +
      '.ims-result:hover{background:var(--ims-hover)}' +
      '.ims-result:focus-visible,.ims-result:focus,.ims-result.ims-active{background:var(--ims-active);border-color:var(--ims-accent)}' +
      '.ims-title{display:block;font-weight:600;font-size:.95rem;color:var(--ims-ink);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}' +
      '.ims-desc{display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;font-size:.84rem;color:var(--ims-muted);margin-top:2px}' +
      '.ims-meta{display:flex;flex-wrap:wrap;align-items:center;gap:6px 10px;margin-top:6px;font-size:.75rem;color:var(--ims-muted)}' +
      '.ims-tag{display:inline-block;padding:1px 8px;border-radius:999px;background:var(--ims-tag-bg);color:var(--ims-tag-ink);font-weight:600}' +
      '.ims-price{font-weight:600;color:var(--ims-ink)}' +
      '.ims-hl{background:var(--ims-mark);color:inherit;border-radius:2px;padding:0 1px}' +
      '.ims-answer{margin:2px 0 8px;padding:12px 14px;border:1px solid var(--ims-answer-bd);border-radius:10px;background:var(--ims-answer)}' +
      '.ims-answer + .ims-answer{margin-top:8px}' +
      '.ims-answer-q{display:flex;align-items:center;gap:8px;margin:0 0 4px;font-size:.95rem;font-weight:600;color:var(--ims-ink)}' +
      '.ims-answer-a{margin:0;font-size:.875rem;color:var(--ims-ink)}' +
      '.ims-answer-a a{color:var(--ims-accent);text-decoration:underline;text-underline-offset:2px;word-break:break-word}' +
      '.ims-answer-link{display:inline-flex;align-items:center;gap:4px;margin-top:8px;padding:4px 10px;border-radius:8px;font-size:.84rem;font-weight:600;' +
        'color:var(--ims-accent);text-decoration:none;border:1px solid var(--ims-answer-bd);outline:none}' +
      '.ims-answer-link:hover{text-decoration:underline}' +
      '.ims-answer-link:focus-visible,.ims-answer-link:focus,.ims-answer-link.ims-active{background:var(--ims-active);border-color:var(--ims-accent)}' +
      '.ims-empty{padding:14px 10px 8px;color:var(--ims-muted);font-size:.9rem}' +
      '.ims-empty strong{color:var(--ims-ink)}' +
      '.ims-empty a{color:var(--ims-accent);text-decoration:underline}' +
      '.ims-chips{display:flex;flex-wrap:wrap;gap:8px;padding:2px 10px 8px}' +
      '.ims-chip{display:inline-flex;align-items:center;gap:6px;min-height:36px;padding:6px 12px;border:1px solid var(--ims-border);border-radius:999px;background:var(--ims-chip);' +
        'color:var(--ims-ink);font:inherit;font-size:.84rem;cursor:pointer}' +
      '.ims-chip:hover{border-color:var(--ims-accent);color:var(--ims-accent)}' +
      '.ims-chip:focus-visible{outline:2px solid var(--ims-accent);outline-offset:2px}' +
      '.ims-clear-recent{border:0;background:none;padding:4px 6px;font:inherit;font-size:.75rem;font-weight:600;letter-spacing:0;text-transform:none;color:var(--ims-accent);cursor:pointer;text-decoration:underline}' +
      '.ims-footer{display:flex;align-items:center;gap:16px;padding:10px 18px;border-top:1px solid var(--ims-border);font-size:.75rem;color:var(--ims-muted)}' +
      '.ims-footer kbd{font:inherit;font-size:.7rem;padding:1px 5px;border-radius:4px;border:1px solid var(--ims-border);background:var(--ims-chip);color:var(--ims-ink);margin:0 1px}' +
      '.ims-count{margin-left:auto;white-space:nowrap}' +
      M + ' a:focus-visible,' + M + ' button:focus-visible{outline:2px solid var(--ims-accent);outline-offset:2px}' +
      '@media(max-width:600px){' +
        M + '.ims-open{padding:8px}' +
        '.ims-dialog{max-height:calc(100vh - 16px);max-height:calc(100dvh - 16px);border-radius:12px}' +
        '.ims-help{display:none}.ims-close-key{display:none}.ims-close-x{display:block}' +
        '.ims-footer{padding:8px 14px}' +
      '}' +
      '@media(prefers-reduced-motion:no-preference){.ims-result,.ims-chip{transition:background .12s,border-color .12s}}' +
      /* Navbar search button */
      '.ims-nav-btn{display:inline-flex;align-items:center;gap:6px;padding:6px 14px;border-radius:8px;border:1px solid var(--border-color,#e2e8f0);background:var(--surface-color,#f8fafc);color:var(--text-secondary,#475569);cursor:pointer;font-size:0.82rem;font-family:inherit;transition:all 0.2s;margin-left:8px}' +
      '.ims-nav-btn:hover{border-color:var(--accent-color,#6366F1);color:var(--text-primary,#1e293b);box-shadow:0 2px 8px rgba(99,102,241,0.15)}' +
      '.ims-nav-btn svg{width:15px;height:15px}' +
      '.ims-nav-btn kbd{font-size:0.65rem;padding:1px 5px;border-radius:3px;border:1px solid var(--border-color,#d1d5db);background:var(--card-bg,#fff);font-family:monospace;color:var(--text-secondary,#475569)}' +
      '@media(max-width:768px){.ims-nav-btn kbd{display:none}.ims-nav-btn{padding:6px 10px}}' +
      /* Mobile button (#1062). The desktop button lives in .nav-buttons, which
         css/imx-main.css sets to display:none !important below 768px, so on a
         phone it was in the DOM at 0x0 and there was no search entry in the
         hamburger menu either. This one sits in .nav-container, which stays
         visible, and appears only where the other one disappears. 44px square
         is the minimum comfortable tap target. */
      /* order:98 because the mobile bar sequences itself with flex order, not
         DOM order: .logo-container is 1, .nav-buttons 2, .mobile-menu-toggle
         99. A button left at the default 0 renders before the logo, which is
         where this one first landed. 98 puts it immediately left of the
         hamburger, and margin-left:auto keeps the pair together on the right. */
      '.ims-nav-btn--m{display:none;align-items:center;justify-content:center;width:44px;height:44px;padding:0;' +
        'order:98;margin:0 4px 0 auto;border-radius:10px;border:1px solid var(--border-color,#e2e8f0);' +
        'background:var(--surface-color,#f8fafc);color:var(--text-secondary,#475569);cursor:pointer;flex:0 0 auto}' +
      '.ims-nav-btn--m svg{width:20px;height:20px}' +
      '[data-theme="dark"] .ims-nav-btn--m{background:#1e293b;color:#e2e8f0;border-color:#334155}' +
      '@media(max-width:768px){.ims-nav-btn--m{display:inline-flex}}' +
      /* --text-secondary is defined in dark mode but --surface-color is not,
         so the button kept its light fallback background under light text:
         1.42:1. Pin both sides for dark rather than relying on the vars. */
      '[data-theme="dark"] .ims-nav-btn{background:#1e293b;color:#e2e8f0;border-color:#334155}';
    document.head.appendChild(css);
  }

  /* ---- Render ---- */
  function setStatus(count, live) {
    countEl.textContent = count || '';
    liveEl.textContent = live || '';
  }

  function chipsHTML(list, cls) {
    return '<div class="ims-chips">' + list.map(function (q) {
      return '<button type="button" class="ims-chip ' + (cls || '') + '" data-q="' + escapeHTML(q) + '">' + escapeHTML(q) + '</button>';
    }).join('') + '</div>';
  }

  function idleHTML() {
    var html = '';
    var recent = readRecent();
    if (recent.length) {
      html += '<h3 class="ims-group">Recent searches<button type="button" class="ims-clear-recent">Clear</button></h3>' +
        chipsHTML(recent, 'ims-chip--recent');
    }
    html += '<h3 class="ims-group">Try searching for</h3>' + chipsHTML(SUGGESTIONS) +
      '<p class="ims-empty">Search ' + (searchData ? searchData.length.toLocaleString('en-IN') + ' pages' : 'every page') +
      ' across courses, Studios, data explorers, reading companions and datasets, with short answers to common questions about ImpactMojo.</p>';
    return html;
  }

  function answerHTML(a) {
    var url = String(a.url || '');
    var ext = /^https?:/.test(url);
    return '<div class="ims-answer">' +
      '<p class="ims-answer-q"><span class="ims-tag">Answer</span>' + escapeHTML(a.q) + '</p>' +
      '<p class="ims-answer-a">' + linkify(a.a) + '</p>' +
      (url ? '<a class="ims-answer-link" data-nav href="' + escapeHTML(url) + '"' +
        (ext ? ' target="_blank" rel="noopener noreferrer"' : '') + '>' +
        escapeHTML(a.label || 'Open the page') + ' <span aria-hidden="true">&rarr;</span></a>' : '') +
      '</div>';
  }

  function resultHTML(item, query) {
    var price = item.type === 'product' ? priceOf(item) : '';
    var label = price ? 'Paid' : typeLabel(item);
    var url = String(item.url || '');
    var cat = item.category && String(item.category).toLowerCase() !== label.toLowerCase() ? item.category : '';
    return '<li><a class="ims-result" data-nav href="' + escapeHTML(url) + '"' +
      (url.indexOf('http') === 0 ? ' target="_blank" rel="noopener noreferrer"' : '') + '>' +
      '<span class="ims-title">' + highlightMatch(item.title, query) + '</span>' +
      (item.description ? '<span class="ims-desc">' + escapeHTML(item.description) + '</span>' : '') +
      '<span class="ims-meta"><span class="ims-tag">' + escapeHTML(label) + '</span>' +
        (price ? '<span class="ims-price">' + escapeHTML(price) + '</span>' : '') +
        (cat ? '<span>' + escapeHTML(cat) + '</span>' : '') +
      '</span></a></li>';
  }

  function plural(n, one, many) { return n + ' ' + (n === 1 ? one : many); }

  function renderResults(query) {
    if (!resultsList) return;
    if (!query || query.length < 2) {
      resultsList.innerHTML = idleHTML();
      setStatus('', '');
      return;
    }

    var answers = answerHits(query);
    var results = [], radio = [];
    if (fuse) {
      results = rank(fuse, query);
      // Clips whose spoken words match go in their own group after the
      // results: a phrase someone half-remembers from a voice note should find
      // it, but should not outrank a course whose title is what they asked for.
      radio = transcriptHits(query, results);
    }

    var html = '';
    if (answers.length) {
      html += '<h3 class="ims-group">Answers</h3>' + answers.map(answerHTML).join('');
    }
    if (results.length) {
      html += '<h3 class="ims-group">Results</h3><ul class="ims-list">' +
        results.map(function (r) { return resultHTML(r.item, query); }).join('') + '</ul>';
    }
    if (radio.length) {
      html += '<h3 class="ims-group">Heard in Field Radio</h3><ul class="ims-list">' +
        radio.map(function (r) { return resultHTML(r.item, query); }).join('') + '</ul>';
    }

    if (!fuse && !answers.length) {
      if (loadFailed) {
        html = '<p class="ims-empty" role="alert"><strong>Search could not load.</strong> Try the <a href="/sitemap.html">site map</a>.</p>';
      } else {
        html = '<p class="ims-empty">Search is loading.</p>';
      }
      resultsList.innerHTML = html;
      setStatus('', '');
      return;
    }

    var total = results.length + radio.length;
    if (!answers.length && !total) {
      resultsList.innerHTML =
        '<p class="ims-empty"><strong>No results for &ldquo;' + escapeHTML(query) + '&rdquo;.</strong> ' +
        'Check the spelling or try a broader word.</p>' +
        '<h3 class="ims-group">Try searching for</h3>' + chipsHTML(SUGGESTIONS) +
        '<p class="ims-empty">You can also browse the <a href="/sitemap.html">site map</a>.</p>';
      setStatus('No results', 'No results for ' + query);
      return;
    }

    resultsList.innerHTML = html;
    resultsList.scrollTop = 0;
    var parts = [];
    if (answers.length) parts.push(plural(answers.length, 'answer', 'answers'));
    if (total) parts.push(plural(total, 'result', 'results'));
    var summary = parts.join(' and ');
    setStatus(summary, summary);
  }

  function highlightMatch(text, query) {
    var safe = escapeHTML(text);
    var q = escapeHTML(query);
    var regex = new RegExp('(' + q.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi');
    return safe.replace(regex, '<mark class="ims-hl">$1</mark>');
  }

  function escapeHTML(str) {
    var map = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' };
    return String(str || '').replace(/[&<>"']/g, function (c) { return map[c]; });
  }

  /* ---- Keyboard ----
     Focus stays in the box while typing. The arrow keys move real focus onto
     the results (each one is an ordinary link), so Enter opens it the way any
     link opens, a screen reader announces it as a link, and Tab still reaches
     the links inside an answer. Typing on a result sends the key back to the
     box. */
  function navItems() {
    return resultsList ? Array.prototype.slice.call(resultsList.querySelectorAll('[data-nav]')) : [];
  }

  function onInputKeydown(e) {
    var items = navItems();
    if (e.key === 'ArrowDown') {
      if (items.length) { e.preventDefault(); items[0].focus(); }
    } else if (e.key === 'Enter') {
      if (items.length) {
        e.preventDefault();
        saveRecent(input.value);
        items[0].click();
      }
    }
  }

  function onPanelKeydown(e) {
    if (e.key === 'Escape') {
      e.preventDefault();
      closeSearch();
      return;
    }
    if (e.key === 'Tab') {
      // Keep focus inside the panel while it is open.
      var f = Array.prototype.slice.call(modal.querySelectorAll('input,button,a[href]')).filter(function (el) {
        return el.offsetWidth || el.offsetHeight || el.getClientRects().length;
      });
      if (!f.length) return;
      var first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      return;
    }
    if (e.target === input) return;
    var items = navItems();
    var i = items.indexOf(document.activeElement);
    if (i === -1) return;
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      if (i < items.length - 1) items[i + 1].focus();
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      if (i > 0) items[i - 1].focus(); else input.focus();
    } else if (e.key === 'Home' && !e.shiftKey) {
      e.preventDefault(); items[0].focus();
    } else if (e.key === 'End' && !e.shiftKey) {
      e.preventDefault(); items[items.length - 1].focus();
    } else if (e.key.length === 1 && !e.ctrlKey && !e.metaKey && !e.altKey) {
      input.focus();   // the character lands in the box
    } else if (e.key === 'Backspace') {
      input.focus();
    }
  }

  function onInput() {
    renderResults(input.value.trim());
  }

  /* ---- Open / Close ---- */
  /* open('certificate') opens with that text already searched, the cursor at
     the end: the homepage's own search box hands its text over this way. Any
     non-string argument (an event, say) is ignored. */
  function openSearch(query) {
    var q = typeof query === 'string' ? query.trim() : '';
    if (visible) {
      if (q) { input.value = q; renderResults(q); placeCursor(); }
      return;
    }
    if (!modal) createModal();
    if (!fuse && !loading) initFuse();   // also retries after a failed load
    loadAnswers();       // fetched when someone opens search, not on every page load
    loadTranscripts();
    opener = document.activeElement && document.activeElement !== document.body ? document.activeElement : null;
    visible = true;
    openedAt = Date.now();
    modal.classList.add('ims-open');
    input.value = q;
    renderResults(q);
    placeCursor();
    setTimeout(function () { if (visible && !modal.contains(document.activeElement)) placeCursor(); }, 50);
    document.body.style.overflow = 'hidden';
  }

  function placeCursor() {
    input.focus();
    try { input.setSelectionRange(input.value.length, input.value.length); } catch (e) { /* type=search in old engines */ }
  }

  function closeSearch() {
    if (!visible) return;
    visible = false;
    modal.classList.remove('ims-open');
    document.body.style.overflow = '';
    // Back to whatever opened it, so a keyboard reader keeps their place.
    if (opener && document.contains(opener) && typeof opener.focus === 'function') {
      try { opener.focus({ preventScroll: true }); } catch (err) { opener.focus(); }
    }
    opener = null;
  }

  /* ---- Global keyboard shortcut ----
     js/site-chrome.js may also answer Ctrl/Cmd+K by calling open(). When both
     listeners see the same keypress, whichever runs second must not undo the
     first, so a toggle within a moment of opening is ignored. */
  document.addEventListener('keydown', function (e) {
    if ((e.ctrlKey || e.metaKey) && !e.altKey && (e.key === 'k' || e.key === 'K')) {
      e.preventDefault();
      if (!visible) openSearch();
      else if (Date.now() - openedAt > 150) closeSearch();
      return;
    }
    if (e.key === '/' && !visible && !isInputFocused() && !e.ctrlKey && !e.metaKey && !e.altKey) {
      e.preventDefault();
      openSearch();
    }
  });

  function isInputFocused() {
    var el = document.activeElement;
    return el && (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA' || el.tagName === 'SELECT' || el.isContentEditable);
  }

  var ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">' +
             '<circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>';

  function makeButton(cls, label, inner) {
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = cls;
    btn.setAttribute('aria-label', label);
    btn.innerHTML = inner;
    btn.addEventListener('click', function (e) { e.preventDefault(); openSearch(); });
    return btn;
  }

  /* ---- Inject nav button ---- */
  function injectNavButton() {
    /* Pages that load the shared top bar already have .im-sc-search there, and
       that one keeps its icon on a narrow screen. Two search buttons in one bar
       is worse than one. */
    if (document.querySelector('.im-sc-search')) return;

    var btn = makeButton('ims-nav-btn', 'Search (Ctrl+K)', ICON + 'Search' + '<kbd>⌘K</kbd>');

    /* Place in nav-buttons area (next to theme selector / auth buttons) for prominence */
    var navButtons = document.querySelector('.nav-buttons');
    if (navButtons) {
      var themeSelector = navButtons.querySelector('.theme-selector');
      if (themeSelector) {
        themeSelector.parentNode.insertBefore(btn, themeSelector);
      } else {
        navButtons.insertBefore(btn, navButtons.firstChild);
      }
      injectMobileButton();
      return;
    }

    /* Fallback: append to nav container. This one is not inside .nav-buttons,
       so it stays visible on a phone and needs no companion. */
    var nav = document.querySelector('.nav-with-badge') || document.querySelector('.nav-container');
    if (nav) {
      nav.style.display = 'flex';
      nav.style.alignItems = 'center';
      nav.appendChild(btn);
    }
  }

  /* ---- Mobile companion (#1062) ----
     .nav-buttons is display:none below 768px, so the button above cannot be
     reached on a phone; the hamburger menu carries no search entry either, and
     Ctrl+K is not available to someone holding a phone. This puts an icon-only
     button in .nav-container, which stays laid out at every width, next to the
     hamburger. CSS shows it only below the same breakpoint, so the two are
     never both on screen. */
  function injectMobileButton() {
    var container = document.querySelector('.nav-container');
    if (!container || container.querySelector('.ims-nav-btn--m')) return;
    var btn = makeButton('ims-nav-btn ims-nav-btn--m', 'Search', ICON);
    var toggle = container.querySelector('.mobile-menu-toggle, #mobile-menu-btn');
    /* The toggle is not always a direct child of .nav-container (on updates.html it
       sits one level down), and insertBefore throws unless it is, which stopped
       this script on those pages. Insert beside it in its own parent instead. */
    if (toggle) toggle.parentNode.insertBefore(btn, toggle);
    else container.appendChild(btn);
  }

  /* ---- Init ---- */
  injectStyles();

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      injectNavButton();
      initFuse();
    });
  } else {
    injectNavButton();
    initFuse();
  }

  window.ImpactMojoSearch = {
    open: openSearch, close: closeSearch,
    _rank: rank, _options: FUSE_OPTIONS,
    _answerOptions: ANSWER_OPTIONS, _answerMax: ANSWER_MAX_SCORE, _answerQuery: answerQuery
  };
})();
