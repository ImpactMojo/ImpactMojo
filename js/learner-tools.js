/**
 * ImpactMojo learner tools.
 *
 * Bookmarks, personal notes, reading lists, compare, learning streak,
 * learning analytics, a focus timer and study music, on the signed-in
 * learner's dashboard (account.html). They used to sit behind a floating
 * toolbox on the home page, retired in October 2026.
 *
 * Two layers:
 *
 *   IMXLearnerData   every storage read and write goes through this one
 *                    object. It reads and writes the same localStorage keys
 *                    the toolbox used, so nothing a learner saved is lost.
 *                    Syncing to the account later means changing get/set
 *                    here, and nowhere else.
 *
 *   IMXLearnerTools  the logic for each tool (no DOM), plus mount(el), which
 *                    draws the dashboard section into an element.
 *
 * Storage can be unavailable (private windows, blocked site data). Every
 * access is wrapped, and the tools still render with empty data.
 */
(function () {
  'use strict';

  // =========================================================================
  // DATA LAYER
  // =========================================================================

  // The keys the toolbox wrote. Do not rename: renaming one strands every
  // learner's saved data under the old name.
  var KEYS = Object.freeze({
    bookmarks: 'impactmojo_bookmarks',
    notes:     'impactmojo_notes',
    compare:   'impactmojo_compare',
    streak:    'impactmojo_streak',
    analytics: 'impactmojo_analytics',
    pomodoro:  'imx_pomodoro_stats',
    toolsTab:  'imx_tools_tab'
  });

  var listeners = [];

  function copy(v) {
    if (v === undefined || v === null) return v;
    try { return JSON.parse(JSON.stringify(v)); } catch (e) { return v; }
  }

  function emit(key) {
    for (var i = 0; i < listeners.length; i++) {
      try { listeners[i](key); } catch (e) { /* a broken listener must not stop the rest */ }
    }
    try { window.dispatchEvent(new CustomEvent('imx-learner-data', { detail: { key: key } })); } catch (e) {}
  }

  var IMXLearnerData = {
    KEYS: KEYS,

    get: function (key, fallback) {
      try {
        var raw = window.localStorage.getItem(key);
        if (raw === null) return copy(fallback);
        var val = JSON.parse(raw);
        return (val === null || val === undefined) ? copy(fallback) : val;
      } catch (e) {
        return copy(fallback);
      }
    },

    set: function (key, value) {
      try {
        window.localStorage.setItem(key, JSON.stringify(value));
      } catch (e) {
        return false;
      }
      emit(key);
      return true;
    },

    remove: function (key) {
      try {
        window.localStorage.removeItem(key);
      } catch (e) {
        return false;
      }
      emit(key);
      return true;
    },

    onChange: function (fn) {
      if (typeof fn === 'function') listeners.push(fn);
    }
  };

  // Another tab changed a key, or auth.js pulled data from the account.
  try {
    window.addEventListener('storage', function (e) {
      if (!e.key) { emit(null); return; }
      for (var k in KEYS) { if (KEYS[k] === e.key) { emit(e.key); return; } }
    });
    window.addEventListener('dataSynced', function () { emit(null); });
  } catch (e) {}

  function asArray(v) { return Array.isArray(v) ? v : []; }

  // =========================================================================
  // HELPERS
  // =========================================================================

  function safeUrl(u) {
    if (!u || typeof u !== 'string') return null;
    try {
      var x = new URL(u, window.location.href);
      if (x.protocol === 'http:' || x.protocol === 'https:') return x.href;
    } catch (e) {}
    return null;
  }

  function csvCell(v) {
    return '"' + String(v === undefined || v === null ? '' : v).replace(/"/g, '""') + '"';
  }

  function download(filename, text, type) {
    try {
      var blob = new Blob([text], { type: type });
      var url = URL.createObjectURL(blob);
      var a = document.createElement('a');
      a.href = url;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      setTimeout(function () { URL.revokeObjectURL(url); }, 1000);
      return true;
    } catch (e) {
      return false;
    }
  }

  function today() { return new Date().toISOString().split('T')[0]; }

  function plural(n, one, many) { return n + ' ' + (n === 1 ? one : many); }

  // =========================================================================
  // BOOKMARKS
  // Item shape (unchanged from the toolbox):
  //   { id, name, url, type, rating, learners, addedAt }
  // =========================================================================

  var bookmarks = {
    list: function () { return asArray(IMXLearnerData.get(KEYS.bookmarks, [])); },
    has: function (id) { return this.list().some(function (b) { return b && b.id === id; }); },
    add: function (item) {
      if (!item || !item.id) return false;
      var all = this.list();
      if (all.some(function (b) { return b && b.id === item.id; })) return true;
      var entry = copy(item);
      entry.addedAt = entry.addedAt || new Date().toISOString();
      all.push(entry);
      return IMXLearnerData.set(KEYS.bookmarks, all);
    },
    remove: function (id) {
      return IMXLearnerData.set(KEYS.bookmarks, this.list().filter(function (b) { return b && b.id !== id; }));
    },
    clear: function () { return IMXLearnerData.set(KEYS.bookmarks, []); },
    toCSV: function () {
      var rows = ['Name,Type,URL,Rating,Learners,Added'];
      this.list().forEach(function (b) {
        rows.push([b.name, b.type, b.url, b.rating, b.learners, b.addedAt].map(csvCell).join(','));
      });
      return rows.join('\n') + '\n';
    }
  };

  // =========================================================================
  // NOTES
  // Note shape (unchanged): { id, title, content, created, updated }
  // created and updated are millisecond timestamps.
  // =========================================================================

  var notes = {
    list: function () {
      var all = IMXLearnerData.get(KEYS.notes, []);
      // A very old format stored an object keyed by id.
      if (all && !Array.isArray(all) && typeof all === 'object') {
        all = Object.keys(all).map(function (k) { var n = all[k] || {}; n.id = n.id || k; return n; });
      }
      return asArray(all).filter(function (n) { return n && typeof n === 'object'; });
    },
    get: function (id) {
      return this.list().filter(function (n) { return n.id === id; })[0] || null;
    },
    save: function (data) {
      var title = String(data.title || '').trim();
      var content = String(data.content || '').trim();
      if (!title && !content) return null;
      var all = this.list();
      var now = Date.now();
      if (data.id) {
        for (var i = 0; i < all.length; i++) {
          if (all[i].id === data.id) {
            all[i].title = title || 'Untitled';
            all[i].content = content;
            all[i].updated = now;
            IMXLearnerData.set(KEYS.notes, all);
            return all[i];
          }
        }
      }
      var note = {
        id: 'note_' + now + '_' + Math.random().toString(36).slice(2, 11),
        title: title || 'Untitled',
        content: content,
        created: now,
        updated: now
      };
      all.unshift(note);
      IMXLearnerData.set(KEYS.notes, all);
      return note;
    },
    remove: function (id) {
      return IMXLearnerData.set(KEYS.notes, this.list().filter(function (n) { return n.id !== id; }));
    },
    clear: function () { return IMXLearnerData.set(KEYS.notes, []); },
    search: function (q) {
      q = String(q || '').toLowerCase().trim();
      var all = this.list();
      if (!q) return all;
      return all.filter(function (n) {
        return String(n.title || '').toLowerCase().indexOf(q) !== -1 ||
               String(n.content || '').toLowerCase().indexOf(q) !== -1;
      });
    },
    toText: function () {
      var out = 'ImpactMojo personal notes\nExported: ' + new Date().toLocaleString() + '\n\n';
      this.list().forEach(function (n, i) {
        out += (i + 1) + '. ' + (n.title || 'Untitled') + '\n';
        if (n.created) out += 'Created: ' + new Date(n.created).toLocaleString() + '\n';
        out += '\n' + (n.content || '') + '\n\n';
      });
      return out;
    }
  };

  // =========================================================================
  // COMPARE (up to three items, same shape as a bookmark)
  // =========================================================================

  // Descriptions for the items most often compared. Matched by path or name.
  var CATALOGUE = [
    { name: 'Gender 101', type: 'Course', url: '/courses/gender/', audience: 'Beginners to intermediate', duration: '4 to 6 hours', format: 'Self-paced online',
      description: 'Gender theory, intersectionality and their social implications in development work.',
      objectives: ['Understand foundational gender concepts', 'Analyse intersectionality in practice', 'Apply gender analysis frameworks', 'Develop gender-sensitive designs'] },
    { name: 'MEAL 101', type: 'Course', url: '/101-courses/mel-basics.html', audience: 'All levels', duration: '6 to 8 hours', format: 'Self-paced online',
      description: 'Monitoring, evaluation, accountability and learning frameworks for measuring impact.',
      objectives: ['Design sound M&E frameworks', 'Create effective indicators', 'Implement accountability mechanisms', 'Build learning loops'] },
    { name: 'Climate 101', type: 'Course', url: '/101-courses/climate-essentials.html', audience: 'Beginners to intermediate', duration: '5 to 7 hours', format: 'Self-paced online',
      description: 'Climate science, its impacts and resilience strategies for development.',
      objectives: ['Understand climate science', 'Analyse climate impacts', 'Design climate-resilient interventions', 'Integrate climate into programmes'] },
    { name: 'Theory of Change Workbench', type: 'Lab', url: '/Labs/toc-lab.html', audience: 'Intermediate to advanced', duration: '2 to 4 hours per project', format: 'Interactive web tool',
      description: 'Build and draw a theory of change.',
      objectives: ['Build a theory of change', 'Map assumptions and evidence', 'Create a TOC diagram', 'Export and share it'] },
    { name: 'LogFrame Lab', type: 'Lab', url: '/Labs/mel-plan-lab.html', audience: 'Intermediate', duration: '3 to 5 hours per project', format: 'Interactive web tool',
      description: 'Design monitoring, evaluation and learning frameworks.',
      objectives: ['Create logical frameworks', 'Define SMART indicators', 'Build results chains', 'Export the document'] },
    { name: 'Storytelling Lab', type: 'Lab', url: '/Labs/storytelling-lab.html', audience: 'All levels', duration: '2 to 3 hours', format: 'Interactive exercises',
      description: 'Write stories about social impact that hold a reader.',
      objectives: ['Structure a story', 'Use data visualisation', 'Create multimedia stories', 'Apply ethical storytelling'] },
    { name: 'The Middle Class Game', type: 'Game', url: '/Games/real-middle-india.html', audience: 'All levels', duration: '30 to 45 minutes', format: 'Interactive simulation',
      description: 'Who the middle class in India is, through the dynamics of wealth inequality.',
      objectives: ['Explore income distribution', 'Understand wealth inequality', 'Test economic assumptions', 'Apply economic thinking'] },
    { name: 'Prospect Theory Game', type: 'Game', url: '/Games/risk-reward-game.html', audience: 'Intermediate', duration: '20 to 30 minutes', format: 'Interactive simulation',
      description: 'Behavioural economics through prospect theory and cognitive biases.',
      objectives: ['Understand loss aversion', 'Recognise framing effects', 'Apply behavioural insights', 'Analyse decision-making'] },
    { name: 'Public Good Game', type: 'Game', url: '/Games/public-good-game.html', audience: 'All levels', duration: '20 to 30 minutes', format: 'Interactive simulation',
      description: 'The free-rider problem and the public goods dilemma.',
      objectives: ['Understand public goods economics', 'See free-rider dynamics at work', 'Analyse collective action', 'Explore cooperation mechanisms'] },
    { name: 'Prisoners Dilemma', type: 'Game', url: '/Games/prisoners-dilemma-game.html', audience: 'All levels', duration: '15 to 25 minutes', format: 'Interactive simulation',
      description: 'Strategic decisions where individual rationality conflicts with collective benefit.',
      objectives: ['Understand the classic dilemma', 'Explore cooperation strategies', 'Analyse repeated games', 'Apply it to coordination problems'] }
  ];

  function pathOf(u) {
    try { return new URL(u, window.location.href).pathname.toLowerCase(); } catch (e) { return ''; }
  }

  var compare = {
    MAX: 3,
    list: function () { return asArray(IMXLearnerData.get(KEYS.compare, [])); },
    has: function (id) { return this.list().some(function (i) { return i && i.id === id; }); },
    add: function (item) {
      if (!item || !item.id) return { ok: false, reason: 'invalid' };
      var all = this.list();
      if (all.some(function (i) { return i && i.id === item.id; })) return { ok: true };
      if (all.length >= this.MAX) return { ok: false, reason: 'full' };
      all.push(copy(item));
      IMXLearnerData.set(KEYS.compare, all);
      return { ok: true };
    },
    remove: function (id) {
      return IMXLearnerData.set(KEYS.compare, this.list().filter(function (i) { return i && i.id !== id; }));
    },
    clear: function () { return IMXLearnerData.set(KEYS.compare, []); },
    enrich: function (item) {
      var p = pathOf(item.url);
      var name = String(item.name || '').toLowerCase();
      for (var i = 0; i < CATALOGUE.length; i++) {
        var c = CATALOGUE[i];
        if ((p && p === c.url.toLowerCase()) || name === c.name.toLowerCase()) {
          var out = copy(c);
          for (var k in item) { if (item[k] !== undefined && item[k] !== '') out[k] = item[k]; }
          return out;
        }
      }
      return copy(item);
    },
    toCSV: function () {
      var self = this;
      var rows = ['Name,Type,Audience,Duration,Format,Description,Objectives,URL'];
      this.list().forEach(function (raw) {
        var it = self.enrich(raw);
        rows.push([it.name, it.type, it.audience, it.duration, it.format, it.description,
          (it.objectives || []).join('; '), it.url].map(csvCell).join(','));
      });
      return rows.join('\n') + '\n';
    }
  };

  // =========================================================================
  // STREAK
  // Shape written by the toolbox:
  //   { currentStreak, longestStreak, totalDays, lastVisit (YYYY-MM-DD, UTC),
  //     visitDates: [YYYY-MM-DD], celebratedMilestone }
  // A copy synced through the account may lack visitDates; that is tolerated.
  // =========================================================================

  var MILESTONES = [
    { days: 3, label: '3 days' },
    { days: 7, label: '1 week' },
    { days: 14, label: '2 weeks' },
    { days: 30, label: '1 month' },
    { days: 60, label: '2 months' },
    { days: 100, label: '100 days' }
  ];

  var streak = {
    MILESTONES: MILESTONES,
    data: function () {
      var d = IMXLearnerData.get(KEYS.streak, {}) || {};
      if (typeof d !== 'object' || Array.isArray(d)) d = {};
      d.currentStreak = d.currentStreak || d.current || 0;
      d.longestStreak = d.longestStreak || d.longest || 0;
      d.visitDates = asArray(d.visitDates);
      d.totalDays = Math.max(d.totalDays || 0, d.visitDates.length);
      d.lastVisit = d.lastVisit || null;
      return d;
    },
    recordVisit: function () {
      var d = this.data();
      var t = today();
      if (d.visitDates.indexOf(t) !== -1 && d.lastVisit === t) return d;
      if (d.visitDates.indexOf(t) === -1) d.visitDates.push(t);
      if (d.visitDates.length > 365) d.visitDates = d.visitDates.slice(-365);
      var y = new Date();
      y.setDate(y.getDate() - 1);
      var yStr = y.toISOString().split('T')[0];
      if (d.lastVisit === yStr) {
        d.currentStreak = (d.currentStreak || 0) + 1;
      } else if (d.lastVisit !== t) {
        d.currentStreak = 1;
        d.celebratedMilestone = 0;
      }
      d.lastVisit = t;
      d.totalDays = Math.max(d.totalDays || 0, d.visitDates.length);
      if (d.currentStreak > d.longestStreak) d.longestStreak = d.currentStreak;
      IMXLearnerData.set(KEYS.streak, d);
      return d;
    },
    daysThisMonth: function (d) {
      d = d || this.data();
      var now = new Date();
      var ym = now.getFullYear() + '-' + String(now.getMonth() + 1).padStart(2, '0');
      return d.visitDates.filter(function (x) { return String(x).indexOf(ym) === 0; }).length;
    }
  };

  // =========================================================================
  // LEARNING ANALYTICS
  // Shape written by the toolbox:
  //   { totalViews, totalTimeSeconds, sessions, firstVisit, lastVisit,
  //     viewsByItem: { id: { name, type, views, lastViewed } },
  //     recentItems: [{ id, name, type, time }], currentSessionStart }
  // =========================================================================

  function analyticsDefault() {
    return { totalViews: 0, totalTimeSeconds: 0, sessions: 0, firstVisit: null, lastVisit: null,
             viewsByItem: {}, recentItems: [], currentSessionStart: null };
  }

  var analytics = {
    data: function () {
      var d = IMXLearnerData.get(KEYS.analytics, null);
      if (!d || typeof d !== 'object' || Array.isArray(d)) return analyticsDefault();
      var base = analyticsDefault();
      for (var k in base) { if (d[k] === undefined || d[k] === null) d[k] = base[k]; }
      if (typeof d.viewsByItem !== 'object' || Array.isArray(d.viewsByItem)) d.viewsByItem = {};
      d.recentItems = asArray(d.recentItems);
      return d;
    },
    trackView: function (id, name, type) {
      if (!id) return;
      var d = this.data();
      var now = new Date().toISOString();
      d.totalViews = (d.totalViews || 0) + 1;
      d.lastVisit = now;
      if (!d.firstVisit) d.firstVisit = now;
      var v = d.viewsByItem[id] || { name: name, type: type, views: 0 };
      v.views = (v.views || 0) + 1;
      v.lastViewed = now;
      d.viewsByItem[id] = v;
      d.recentItems = d.recentItems.filter(function (i) { return i && i.id !== id; });
      d.recentItems.unshift({ id: id, name: name, type: type, time: now });
      d.recentItems = d.recentItems.slice(0, 10);
      IMXLearnerData.set(KEYS.analytics, d);
    },
    summary: function () {
      var d = this.data();
      var top = Object.keys(d.viewsByItem).map(function (k) {
        var v = d.viewsByItem[k] || {};
        return { id: k, name: v.name || k, type: v.type || '', views: v.views || 0 };
      }).sort(function (a, b) { return b.views - a.views; }).slice(0, 5);
      var mins = Math.floor((d.totalTimeSeconds || 0) / 60);
      var h = Math.floor(mins / 60);
      return {
        totalViews: d.totalViews || 0,
        sessions: d.sessions || 0,
        time: h > 0 ? h + 'h ' + (mins % 60) + 'm' : (mins % 60) + ' min',
        firstVisit: d.firstVisit,
        lastVisit: d.lastVisit,
        topItems: top,
        recentItems: d.recentItems.slice(0, 5)
      };
    },
    clear: function () { return IMXLearnerData.remove(KEYS.analytics); }
  };

  // =========================================================================
  // FOCUS TIMER (pomodoro)
  // Stats shape (unchanged): { sessions, totalMinutes, lastDate }
  // sessions counts today only; totalMinutes is all time.
  // =========================================================================

  var pomodoro = {
    PRESETS: [
      { minutes: 25, label: 'Focus time' },
      { minutes: 5, label: 'Short break' },
      { minutes: 15, label: 'Long break' },
      { minutes: 50, label: 'Deep focus' }
    ],
    stats: function () {
      var s = IMXLearnerData.get(KEYS.pomodoro, null);
      var d = new Date().toDateString();
      if (!s || typeof s !== 'object') return { sessions: 0, totalMinutes: 0, lastDate: d };
      return {
        sessions: s.lastDate === d ? (s.sessions || 0) : 0,
        totalMinutes: s.totalMinutes || 0,
        lastDate: s.lastDate || d
      };
    },
    addSession: function (minutes) {
      var s = this.stats();
      s.sessions += 1;
      s.totalMinutes += Math.floor(minutes);
      s.lastDate = new Date().toDateString();
      IMXLearnerData.set(KEYS.pomodoro, s);
      return s;
    }
  };

  // =========================================================================
  // STATIC CONTENT: reading lists and study music
  // =========================================================================

  var READING_LISTS = [
    { id: 'meal-essentials', name: 'MEAL essentials', description: 'Core resources for monitoring, evaluation, accountability and learning',
      items: [
        { title: 'BetterEvaluation Rainbow Framework', url: 'https://www.betterevaluation.org/frameworks-guides/rainbow-framework', type: 'Framework' },
        { title: 'USAID Evaluation Toolkit', url: 'https://www.usaid.gov/evaluation', type: 'Toolkit' },
        { title: 'World Bank Impact Evaluation Guide', url: 'https://dimewiki.worldbank.org/Impact_Evaluation', type: 'Guide' },
        { title: 'ODI Results-Based Management', url: 'https://odi.org/en/publications/results-based-management-in-development-cooperation/', type: 'Publication' },
        { title: 'ALNAP Evaluation Resources', url: 'https://www.alnap.org/help-library/evaluation', type: 'Library' }
      ] },
    { id: 'theory-of-change', name: 'Theory of change', description: 'Designing and testing a theory of change',
      items: [
        { title: 'Center for Theory of Change', url: 'https://www.theoryofchange.org/', type: 'Hub' },
        { title: 'UNDP Theory of Change Guide', url: 'https://www.undp.org/publications/undp-guidance-note-theory-change', type: 'Guide' },
        { title: 'Nesta Theory of Change', url: 'https://www.nesta.org.uk/toolkit/theory-change/', type: 'Toolkit' },
        { title: 'Comic Relief TOC Guidance', url: 'https://www.comicrelief.com/our-approach/how-we-measure-our-impact/', type: 'Guide' },
        { title: 'DIY Theory of Change Toolkit', url: 'https://diytoolkit.org/tools/theory-of-change/', type: 'Tool' }
      ] },
    { id: 'gender-development', name: 'Gender in development', description: 'Readings on gender analysis and mainstreaming',
      items: [
        { title: 'UN Women Training Centre', url: 'https://trainingcentre.unwomen.org/', type: 'Courses' },
        { title: 'BRIDGE Gender & Development', url: 'https://www.bridge.ids.ac.uk/', type: 'Research' },
        { title: 'Gender Analysis Toolkit (USAID)', url: 'https://www.usaid.gov/engendering-industries', type: 'Toolkit' },
        { title: 'CARE Gender Toolkit', url: 'https://www.care.org/our-work/womens-economic-justice/', type: 'Resources' },
        { title: 'World Bank Gender Data Portal', url: 'https://genderdata.worldbank.org/', type: 'Data' }
      ] },
    { id: 'research-methods', name: 'Research methods', description: 'Qualitative and quantitative research resources',
      items: [
        { title: 'J-PAL Research Resources', url: 'https://www.povertyactionlab.org/research-resources', type: 'Library' },
        { title: 'SAGE Research Methods', url: 'https://methods.sagepub.com/', type: 'Database' },
        { title: 'Qualitative Research Guidelines (CDC)', url: 'https://www.cdc.gov/healthyyouth/evaluation/pdf/brief19.pdf', type: 'Guide' },
        { title: 'IPA Best Practices', url: 'https://www.poverty-action.org/researchers', type: 'Resources' },
        { title: '3ie Systematic Reviews', url: 'https://www.3ieimpact.org/evidence-hub/systematic-review-repository', type: 'Repository' }
      ] },
    { id: 'behavioral-economics', name: 'Behavioural economics', description: 'Behavioural insights for development programmes',
      items: [
        { title: 'ideas42 Behavioral Design', url: 'https://www.ideas42.org/learn/', type: 'Learning' },
        { title: 'Behavioral Insights Team', url: 'https://www.bi.team/publications/', type: 'Publications' },
        { title: 'World Bank Mind, Behavior, Development', url: 'https://www.worldbank.org/en/programs/embed', type: 'Programme' },
        { title: 'Busara Center Resources', url: 'https://busaracenter.org/resources/', type: 'Resources' },
        { title: 'OECD Behavioral Insights', url: 'https://www.oecd.org/gov/regulatory-policy/behavioural-insights.htm', type: 'Policy' }
      ] }
  ];

  // Links only. Nothing is embedded: the account page's Content-Security-Policy
  // allows no Spotify or YouTube frames, and a link sends nothing to either
  // service until the learner chooses to go there.
  var PLAYLISTS = [
    { title: 'Deep focus', description: 'Instrumental beats for long study sessions.',
      spotify: 'https://open.spotify.com/playlist/37i9dQZF1DWZeKCadgRdKQ', youtube: 'https://www.youtube.com/watch?v=jfKfPfyJRdk' },
    { title: 'Chill lo-fi', description: 'Relaxed beats to keep in the background while you read.',
      spotify: 'https://open.spotify.com/playlist/0vvXsWCC9xrXsKd4FyS8kM', youtube: 'https://www.youtube.com/watch?v=5qap5aO4i9A' },
    { title: 'Ambient soundscapes', description: 'Atmospheric sound with no lyrics.',
      spotify: 'https://open.spotify.com/playlist/37i9dQZF1DX3Ogo9pFvBkY', youtube: 'https://www.youtube.com/watch?v=lTRiuFIWV54' },
    { title: 'Nature sounds', description: 'Rain, forest and ocean.',
      spotify: 'https://open.spotify.com/playlist/37i9dQZF1DX4PP3DA4J0N8', youtube: 'https://www.youtube.com/watch?v=q76bMs-NwRk' },
    { title: 'Classical focus', description: 'Classical pieces for concentration.',
      spotify: 'https://open.spotify.com/playlist/37i9dQZF1DWWEJlAGA9gs0', youtube: 'https://www.youtube.com/watch?v=mIYzp5rcTvU' }
  ];

  // =========================================================================
  // DOM HELPERS
  // =========================================================================

  function el(tag, attrs, children) {
    var n = document.createElement(tag);
    if (attrs) {
      for (var k in attrs) {
        if (!attrs.hasOwnProperty(k) || attrs[k] === null || attrs[k] === undefined || attrs[k] === false) continue;
        if (k === 'text') n.textContent = attrs[k];
        else if (k === 'className') n.className = attrs[k];
        else if (k.indexOf('on') === 0 && typeof attrs[k] === 'function') n.addEventListener(k.slice(2), attrs[k]);
        else n.setAttribute(k, attrs[k] === true ? '' : attrs[k]);
      }
    }
    (children || []).forEach(function (c) {
      if (c === null || c === undefined || c === false) return;
      n.appendChild(typeof c === 'string' ? document.createTextNode(c) : c);
    });
    return n;
  }

  function btn(label, onclick, opts) {
    opts = opts || {};
    return el('button', {
      type: 'button',
      className: 'lt-btn' + (opts.variant ? ' lt-btn-' + opts.variant : ''),
      'aria-label': opts.ariaLabel || null,
      'aria-pressed': opts.pressed === undefined ? null : String(!!opts.pressed),
      disabled: opts.disabled || null,
      onclick: onclick
    }, [label]);
  }

  function extLink(text, url, className) {
    var href = safeUrl(url);
    if (!href) return el('span', { className: 'lt-item-title', text: text });
    return el('a', { className: className || 'lt-link', href: href, target: '_blank', rel: 'noopener noreferrer' },
      [text, el('span', { className: 'lt-sr', text: ' (opens in a new tab)' })]);
  }

  function empty(text) { return el('p', { className: 'lt-empty', text: text }); }

  function fmtDate(iso) {
    if (!iso) return 'not yet';
    var d = new Date(iso);
    if (isNaN(d.getTime())) return 'not yet';
    return d.toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' });
  }

  function stat(value, label) {
    return el('div', { className: 'lt-stat' }, [
      el('div', { className: 'lt-stat-value', text: String(value) }),
      el('div', { className: 'lt-stat-label', text: label })
    ]);
  }

  // =========================================================================
  // UI
  // =========================================================================

  var TABS = [
    { id: 'bookmarks', label: 'Bookmarks' },
    { id: 'notes', label: 'Notes' },
    { id: 'reading', label: 'Reading lists' },
    { id: 'compare', label: 'Compare' },
    { id: 'streak', label: 'Streak' },
    { id: 'analytics', label: 'Learning analytics' },
    { id: 'timer', label: 'Focus timer' },
    { id: 'music', label: 'Study music' }
  ];

  function Dashboard(root) {
    this.root = root;
    this.panels = {};
    this.tabs = {};
    this.counts = {};
    this.noteQuery = '';
    this.editingNote = null;
    this.timer = { interval: null, endAt: 0, remaining: 25 * 60, total: 25 * 60, label: 'Focus time', running: false };
  }

  Dashboard.prototype.say = function (msg) {
    if (!this.status) return;
    this.status.textContent = '';
    var s = this.status;
    setTimeout(function () { s.textContent = msg; }, 30);
  };

  Dashboard.prototype.build = function () {
    var self = this;
    this.root.classList.add('lt-root');
    this.root.textContent = '';

    this.root.appendChild(el('p', { className: 'lt-intro',
      text: 'Your bookmarks, notes and study tools in one place. They are saved in this browser.' }));

    var list = el('div', { className: 'lt-tabs', role: 'tablist', 'aria-label': 'My tools' });
    TABS.forEach(function (t) {
      var count = el('span', { className: 'lt-count', 'aria-hidden': 'true' });
      var b = el('button', {
        type: 'button', role: 'tab', className: 'lt-tab', id: 'lt-tab-' + t.id,
        'aria-controls': 'lt-panel-' + t.id, 'aria-selected': 'false', tabindex: '-1',
        onclick: function () { self.select(t.id, true); }
      }, [el('span', { text: t.label }), count]);
      b.addEventListener('keydown', function (e) { self.onTabKey(e, t.id); });
      self.tabs[t.id] = b;
      self.counts[t.id] = count;
      list.appendChild(b);
    });
    this.root.appendChild(list);

    this.status = el('p', { className: 'lt-status', role: 'status', 'aria-live': 'polite' });
    this.root.appendChild(this.status);

    TABS.forEach(function (t) {
      var p = el('div', { className: 'lt-panel', role: 'tabpanel', id: 'lt-panel-' + t.id,
        'aria-labelledby': 'lt-tab-' + t.id, tabindex: '0', hidden: true });
      self.panels[t.id] = p;
      self.root.appendChild(p);
    });

    this.renderAll();

    var initial = 'bookmarks';
    var m = /^#tools-([a-z]+)$/.exec(window.location.hash || '');
    if (m && this.panels[m[1]]) initial = m[1];
    else {
      var saved = IMXLearnerData.get(KEYS.toolsTab, null);
      if (saved && this.panels[saved]) initial = saved;
    }
    this.select(initial, false);

    IMXLearnerData.onChange(function (key) {
      if (key === KEYS.toolsTab) return;
      self.renderAll();
    });
  };

  Dashboard.prototype.onTabKey = function (e, id) {
    var ids = TABS.map(function (t) { return t.id; });
    var i = ids.indexOf(id);
    var next = null;
    if (e.key === 'ArrowRight' || e.key === 'ArrowDown') next = ids[(i + 1) % ids.length];
    else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') next = ids[(i - 1 + ids.length) % ids.length];
    else if (e.key === 'Home') next = ids[0];
    else if (e.key === 'End') next = ids[ids.length - 1];
    if (next) {
      e.preventDefault();
      this.select(next, true);
      this.tabs[next].focus();
    }
  };

  Dashboard.prototype.select = function (id, remember) {
    for (var k in this.tabs) {
      var on = k === id;
      this.tabs[k].setAttribute('aria-selected', on ? 'true' : 'false');
      this.tabs[k].setAttribute('tabindex', on ? '0' : '-1');
      this.panels[k].hidden = !on;
    }
    this.current = id;
    if (remember) IMXLearnerData.set(KEYS.toolsTab, id);
  };

  Dashboard.prototype.renderAll = function () {
    var b = bookmarks.list().length, n = notes.list().length, c = compare.list().length;
    var s = streak.data().currentStreak || 0;
    this.counts.bookmarks.textContent = b ? String(b) : '';
    this.counts.notes.textContent = n ? String(n) : '';
    this.counts.compare.textContent = c ? c + '/' + compare.MAX : '';
    this.counts.streak.textContent = s ? String(s) : '';
    this.renderBookmarks();
    this.renderNotes();
    this.renderReading();
    this.renderCompare();
    this.renderStreak();
    this.renderAnalytics();
    this.renderTimer();
    this.renderMusic();
  };

  Dashboard.prototype.head = function (panel, title, actions) {
    panel.appendChild(el('div', { className: 'lt-panel-head' }, [
      el('h3', { text: title }),
      actions && actions.length ? el('div', { className: 'lt-actions' }, actions) : null
    ]));
  };

  // ---- Bookmarks ---------------------------------------------------------

  Dashboard.prototype.renderBookmarks = function () {
    var self = this, p = this.panels.bookmarks;
    p.textContent = '';
    var all = bookmarks.list();
    this.head(p, 'Bookmarks', all.length ? [
      btn('Export CSV', function () {
        download('impactmojo_bookmarks_' + today() + '.csv', bookmarks.toCSV(), 'text/csv;charset=utf-8');
        self.say('Bookmarks exported.');
      }),
      btn('Clear all', function () {
        if (window.confirm('Remove all bookmarks? This cannot be undone.')) { bookmarks.clear(); self.say('All bookmarks removed.'); }
      }, { variant: 'danger' })
    ] : null);
    if (!all.length) {
      p.appendChild(empty('Nothing saved yet. Courses, labs and games you save appear here.'));
      return;
    }
    p.appendChild(el('p', { className: 'lt-muted', text: plural(all.length, 'item', 'items') + ' saved.' }));
    var ul = el('ul', { className: 'lt-list' });
    all.forEach(function (b) {
      var name = b.name || 'Untitled';
      var inCompare = compare.has(b.id);
      var meta = [b.type || 'Item'];
      if (b.addedAt) meta.push('saved ' + fmtDate(b.addedAt));
      ul.appendChild(el('li', { className: 'lt-item' }, [
        el('div', { className: 'lt-item-main' }, [
          el('div', { className: 'lt-item-title' }, [safeUrl(b.url) ? el('a', { className: 'lt-link', href: safeUrl(b.url) }, [name]) : name]),
          el('div', { className: 'lt-item-meta', text: meta.join(' · ') })
        ]),
        el('div', { className: 'lt-actions' }, [
          btn(inCompare ? 'In compare' : 'Compare', function () {
            if (compare.has(b.id)) { compare.remove(b.id); self.say(name + ' removed from compare.'); return; }
            var r = compare.add(b);
            self.say(r.ok ? name + ' added to compare.' : 'Compare holds three items. Remove one first.');
          }, { pressed: inCompare, ariaLabel: 'Compare ' + name }),
          btn('Remove', function () { bookmarks.remove(b.id); self.say(name + ' removed from bookmarks.'); },
            { variant: 'danger', ariaLabel: 'Remove ' + name + ' from bookmarks' })
        ])
      ]));
    });
    p.appendChild(ul);
  };

  // ---- Notes -------------------------------------------------------------

  Dashboard.prototype.renderNotes = function () {
    var self = this, p = this.panels.notes;
    // Keep what is being typed if a re-render arrives mid-edit.
    // Only when the form is still in the same mode (new note, or the same
    // note being edited); switching mode loads that mode's text instead.
    var prevTitle = p.querySelector('#lt-note-title');
    var prevBody = p.querySelector('#lt-note-body');
    var sameMode = (p.getAttribute('data-editing') || '') === (this.editingNote || '');
    var draft = prevTitle && sameMode ? { title: prevTitle.value, content: prevBody.value } : null;
    p.setAttribute('data-editing', this.editingNote || '');
    var hadFocus = document.activeElement && p.contains(document.activeElement) ? document.activeElement.id : null;

    p.textContent = '';
    var all = notes.list();
    this.head(p, 'Notes', all.length ? [
      btn('Export as text', function () {
        download('impactmojo_notes_' + today() + '.txt', notes.toText(), 'text/plain;charset=utf-8');
        self.say('Notes exported.');
      }),
      btn('Delete all', function () {
        if (window.confirm('Delete all notes? This cannot be undone.')) { notes.clear(); self.editingNote = null; self.say('All notes deleted.'); }
      }, { variant: 'danger' })
    ] : null);

    var editing = this.editingNote ? notes.get(this.editingNote) : null;
    if (this.editingNote && !editing) this.editingNote = null;
    var titleIn = el('input', { className: 'lt-input', id: 'lt-note-title', type: 'text', maxlength: '200', autocomplete: 'off' });
    var bodyIn = el('textarea', { className: 'lt-textarea', id: 'lt-note-body', rows: '5' });
    if (draft) { titleIn.value = draft.title; bodyIn.value = draft.content; }
    else if (editing) { titleIn.value = editing.title || ''; bodyIn.value = editing.content || ''; }

    var form = el('form', { className: 'lt-note-form', 'aria-label': editing ? 'Edit note' : 'New note' }, [
      el('h4', { text: editing ? 'Edit note' : 'New note' }),
      el('div', { className: 'lt-field' }, [el('label', { for: 'lt-note-title', text: 'Title' }), titleIn]),
      el('div', { className: 'lt-field' }, [el('label', { for: 'lt-note-body', text: 'Note' }), bodyIn]),
      el('div', { className: 'lt-actions' }, [
        el('button', { type: 'submit', className: 'lt-btn lt-btn-primary' }, [editing ? 'Save changes' : 'Save note']),
        editing ? btn('Cancel', function () { self.editingNote = null; self.renderNotes(); }) : null
      ])
    ]);
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var data = { id: self.editingNote, title: titleIn.value, content: bodyIn.value };
      if (!data.title.trim() && !data.content.trim()) { self.say('Write a title or some text first.'); titleIn.focus(); return; }
      var wasEditing = !!self.editingNote;
      // Clear the form before saving: the save re-renders this panel, and the
      // re-render keeps whatever text is still in the form as a draft.
      self.editingNote = null;
      titleIn.value = ''; bodyIn.value = '';
      notes.save(data);
      self.renderNotes();
      self.say(wasEditing ? 'Note updated.' : 'Note saved.');
    });
    p.appendChild(form);

    if (!all.length) {
      p.appendChild(empty('No notes yet.'));
      return;
    }

    var search = el('input', { className: 'lt-input', id: 'lt-note-search', type: 'search', autocomplete: 'off' });
    search.value = this.noteQuery;
    search.addEventListener('input', function () { self.noteQuery = search.value; self.renderNoteList(listWrap); });
    p.appendChild(el('div', { className: 'lt-field' }, [el('label', { for: 'lt-note-search', text: 'Search notes' }), search]));

    var listWrap = el('div');
    p.appendChild(listWrap);
    this.renderNoteList(listWrap);

    if (hadFocus) { var f = document.getElementById(hadFocus); if (f) f.focus(); }
  };

  Dashboard.prototype.renderNoteList = function (wrap) {
    var self = this;
    wrap.textContent = '';
    var shown = notes.search(this.noteQuery);
    if (!shown.length) { wrap.appendChild(empty('No notes match that search.')); return; }
    var ul = el('ul', { className: 'lt-list' });
    shown.forEach(function (n) {
      var title = n.title || 'Untitled';
      ul.appendChild(el('li', { className: 'lt-item' }, [
        el('div', { className: 'lt-item-main' }, [
          el('div', { className: 'lt-item-title', text: title }),
          el('div', { className: 'lt-item-meta', text: 'Updated ' + fmtDate(n.updated || n.created) }),
          n.content ? el('div', { className: 'lt-note-body', text: n.content }) : null
        ]),
        el('div', { className: 'lt-actions' }, [
          btn('Edit', function () {
            self.editingNote = n.id;
            self.renderNotes();
            var t = document.getElementById('lt-note-title');
            if (t) t.focus();
          }, { ariaLabel: 'Edit note ' + title }),
          btn('Delete', function () {
            if (window.confirm('Delete this note?')) { notes.remove(n.id); self.say('Note deleted.'); }
          }, { variant: 'danger', ariaLabel: 'Delete note ' + title })
        ])
      ]));
    });
    wrap.appendChild(ul);
  };

  // ---- Reading lists -----------------------------------------------------

  Dashboard.prototype.renderReading = function () {
    var p = this.panels.reading;
    if (p.childNodes.length) return; // static; keep open/closed state
    this.head(p, 'Reading lists');
    p.appendChild(el('p', { className: 'lt-muted', text: 'Curated outside reading on five themes. Each link opens the source in a new tab.' }));
    READING_LISTS.forEach(function (l) {
      var ul = el('ul', { className: 'lt-list' });
      l.items.forEach(function (it) {
        ul.appendChild(el('li', { className: 'lt-item' }, [
          el('div', { className: 'lt-item-main' }, [extLink(it.title, it.url)]),
          el('span', { className: 'lt-item-meta', text: it.type })
        ]));
      });
      p.appendChild(el('details', { className: 'lt-details' }, [
        el('summary', null, [l.name, el('span', { className: 'lt-muted', text: l.description })]),
        ul
      ]));
    });
  };

  // ---- Compare -----------------------------------------------------------

  Dashboard.prototype.renderCompare = function () {
    var self = this, p = this.panels.compare;
    p.textContent = '';
    var all = compare.list();
    this.head(p, 'Compare', all.length ? [
      btn('Export CSV', function () {
        download('impactmojo-comparison-' + today() + '.csv', compare.toCSV(), 'text/csv;charset=utf-8');
        self.say('Comparison exported.');
      }),
      btn('Clear', function () { compare.clear(); self.say('Comparison cleared.'); }, { variant: 'danger' })
    ] : null);
    if (!all.length) {
      p.appendChild(empty('Add up to three items from your bookmarks to see them side by side.'));
      return;
    }
    var grid = el('div', { className: 'lt-compare-grid' });
    all.forEach(function (raw) {
      var it = compare.enrich(raw);
      var name = it.name || 'Untitled';
      var rows = [['Type', it.type], ['Audience', it.audience], ['Duration', it.duration], ['Format', it.format],
                  ['Rating', it.rating], ['Learners', it.learners]];
      var dl = el('dl');
      rows.forEach(function (r) {
        if (!r[1]) return;
        dl.appendChild(el('dt', { text: r[0] }));
        dl.appendChild(el('dd', { text: String(r[1]) }));
      });
      var href = safeUrl(it.url);
      grid.appendChild(el('article', { className: 'lt-compare-card', 'aria-label': name }, [
        el('h4', { text: name }),
        dl,
        it.description ? el('p', { className: 'lt-muted', text: it.description }) : null,
        it.objectives && it.objectives.length ? el('div', null, [
          el('p', { className: 'lt-muted', text: 'What you learn' }),
          el('ul', null, it.objectives.map(function (o) { return el('li', { text: o }); }))
        ]) : null,
        el('div', { className: 'lt-actions' }, [
          href ? el('a', { className: 'lt-btn lt-btn-primary', href: href }, ['Open']) : null,
          btn('Remove', function () { compare.remove(raw.id); self.say(name + ' removed from compare.'); },
            { variant: 'danger', ariaLabel: 'Remove ' + name + ' from compare' })
        ])
      ]));
    });
    p.appendChild(grid);
    if (all.length < compare.MAX) {
      p.appendChild(el('p', { className: 'lt-muted', text: 'You can add ' + plural(compare.MAX - all.length, 'more item', 'more items') + ' from Bookmarks.' }));
    }
  };

  // ---- Streak ------------------------------------------------------------

  Dashboard.prototype.renderStreak = function () {
    var p = this.panels.streak;
    p.textContent = '';
    var d = streak.data();
    this.head(p, 'Learning streak');
    p.appendChild(el('p', { className: 'lt-muted', text: 'A day counts when you open ImpactMojo while signed in on this browser.' }));
    p.appendChild(el('div', { className: 'lt-stats' }, [
      stat(d.currentStreak || 0, 'Day streak'),
      stat(d.longestStreak || 0, 'Best streak'),
      stat(d.totalDays || 0, 'Total days'),
      stat(streak.daysThisMonth(d), 'This month')
    ]));

    var now = new Date(), year = now.getFullYear(), month = now.getMonth();
    var monthName = now.toLocaleDateString('en-IN', { month: 'long', year: 'numeric' });
    var table = el('table', { className: 'lt-calendar' }, [el('caption', { text: 'Days visited in ' + monthName })]);
    var headRow = el('tr');
    [['S', 'Sunday'], ['M', 'Monday'], ['T', 'Tuesday'], ['W', 'Wednesday'], ['T', 'Thursday'], ['F', 'Friday'], ['S', 'Saturday']]
      .forEach(function (w) { headRow.appendChild(el('th', { scope: 'col', abbr: w[1], text: w[0] })); });
    table.appendChild(el('thead', null, [headRow]));
    var body = el('tbody');
    var first = new Date(year, month, 1).getDay();
    var days = new Date(year, month + 1, 0).getDate();
    var todayStr = today();
    var row = el('tr');
    for (var i = 0; i < first; i++) row.appendChild(el('td', { className: 'lt-blank' }));
    for (var dd = 1; dd <= days; dd++) {
      var ds = year + '-' + String(month + 1).padStart(2, '0') + '-' + String(dd).padStart(2, '0');
      var visited = d.visitDates.indexOf(ds) !== -1;
      var cls = [];
      if (visited) cls.push('lt-visited');
      if (ds === todayStr) cls.push('lt-today');
      row.appendChild(el('td', { className: cls.join(' ') || null }, [
        String(dd),
        visited ? el('span', { className: 'lt-sr', text: ' visited' }) : null,
        ds === todayStr ? el('span', { className: 'lt-sr', text: ' today' }) : null
      ]));
      if ((first + dd) % 7 === 0) { body.appendChild(row); row = el('tr'); }
    }
    if (row.childNodes.length) {
      while (row.childNodes.length < 7) row.appendChild(el('td', { className: 'lt-blank' }));
      body.appendChild(row);
    }
    table.appendChild(body);
    p.appendChild(table);

    var ms = el('ul', { className: 'lt-milestones' });
    MILESTONES.forEach(function (m) {
      var earned = (d.longestStreak || 0) >= m.days;
      ms.appendChild(el('li', { className: 'lt-milestone' + (earned ? ' lt-earned' : '') },
        [m.label, el('span', { className: 'lt-sr', text: earned ? ', reached' : ', not reached yet' })]));
    });
    p.appendChild(el('div', { className: 'lt-section' }, [el('h4', { text: 'Milestones' }), ms]));
  };

  // ---- Analytics ---------------------------------------------------------

  Dashboard.prototype.renderAnalytics = function () {
    var self = this, p = this.panels.analytics;
    p.textContent = '';
    var s = analytics.summary();
    this.head(p, 'Learning analytics', s.totalViews ? [
      btn('Clear analytics', function () {
        if (window.confirm('Clear your learning analytics? This cannot be undone.')) { analytics.clear(); self.say('Analytics cleared.'); }
      }, { variant: 'danger' })
    ] : null);
    if (!s.totalViews && !s.sessions) {
      p.appendChild(empty('No activity recorded on this browser yet. What you open from the course, lab and game cards shows here.'));
      return;
    }
    p.appendChild(el('div', { className: 'lt-stats' }, [
      stat(s.totalViews, 'Items opened'),
      stat(s.sessions, 'Sessions'),
      stat(s.time, 'Time learning')
    ]));
    function itemList(title, items, metaFn) {
      if (!items.length) return null;
      var ul = el('ul', { className: 'lt-list' });
      items.forEach(function (it) {
        ul.appendChild(el('li', { className: 'lt-item' }, [
          el('div', { className: 'lt-item-main' }, [el('div', { className: 'lt-item-title', text: it.name || 'Untitled' })]),
          el('span', { className: 'lt-item-meta', text: metaFn(it) })
        ]));
      });
      return el('div', { className: 'lt-section' }, [el('h4', { text: title }), ul]);
    }
    p.appendChild(itemList('Most opened', s.topItems, function (it) { return plural(it.views, 'time', 'times'); }));
    p.appendChild(itemList('Recently opened', s.recentItems, function (it) { return fmtDate(it.time); }));
    p.appendChild(el('p', { className: 'lt-muted lt-section', text: 'First visit ' + fmtDate(s.firstVisit) + '. Last visit ' + fmtDate(s.lastVisit) + '.' }));
  };

  // ---- Focus timer -------------------------------------------------------

  function mmss(sec) {
    sec = Math.max(0, Math.round(sec));
    var m = Math.floor(sec / 60), s = sec % 60;
    return (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
  }

  Dashboard.prototype.renderTimer = function () {
    var self = this, p = this.panels.timer, t = this.timer;
    if (!p.childNodes.length) {
      this.head(p, 'Focus timer');
      p.appendChild(el('p', { className: 'lt-muted', text: 'Work in short, timed blocks with a break between them. The timer keeps running while you use the other tools on this page.' }));
      this.tTime = el('div', { className: 'lt-timer-time', role: 'timer', 'aria-live': 'off' });
      this.tLabel = el('p', { className: 'lt-timer-label' });
      this.tStart = btn('Start', function () { self.timerToggle(); }, { variant: 'primary' });
      var reset = btn('Reset', function () { self.timerReset(); self.say('Timer reset.'); });
      this.tPresets = el('div', { className: 'lt-actions lt-presets', role: 'group', 'aria-label': 'Timer length' });
      pomodoro.PRESETS.forEach(function (pr) {
        var b = btn(pr.minutes + ' min', function () { self.timerPreset(pr); },
          { ariaLabel: pr.label + ', ' + pr.minutes + ' minutes', pressed: pr.minutes * 60 === t.total });
        b.setAttribute('data-min', String(pr.minutes));
        self.tPresets.appendChild(b);
      });
      p.appendChild(el('div', { className: 'lt-timer' }, [
        this.tTime, this.tLabel, el('div', { className: 'lt-actions' }, [this.tStart, reset]), this.tPresets
      ]));
      this.tStats = el('div', { className: 'lt-stats' });
      p.appendChild(this.tStats);
      p.appendChild(el('p', { className: 'lt-muted', text: 'Study music has playlists to go with it.' }));
    }
    this.tTime.textContent = mmss(t.remaining);
    this.tLabel.textContent = t.label;
    this.tStart.textContent = t.running ? 'Pause' : (t.remaining < t.total ? 'Resume' : 'Start');
    Array.prototype.forEach.call(this.tPresets.querySelectorAll('button'), function (b) {
      b.setAttribute('aria-pressed', String(Number(b.getAttribute('data-min')) * 60 === t.total));
    });
    var st = pomodoro.stats();
    var hrs = Math.floor(st.totalMinutes / 60);
    this.tStats.textContent = '';
    this.tStats.appendChild(stat(st.sessions, 'Sessions today'));
    this.tStats.appendChild(stat(hrs + 'h ' + (st.totalMinutes % 60) + 'm', 'Total focus time'));
  };

  Dashboard.prototype.timerTick = function () {
    var t = this.timer;
    t.remaining = Math.max(0, Math.round((t.endAt - Date.now()) / 1000));
    this.tTime.textContent = mmss(t.remaining);
    try { document.title = (t.running ? mmss(t.remaining) + ' · ' : '') + this.baseTitle; } catch (e) {}
    if (t.remaining <= 0) this.timerDone();
  };

  Dashboard.prototype.timerToggle = function () {
    var self = this, t = this.timer;
    if (!this.baseTitle) this.baseTitle = document.title;
    if (t.running) {
      clearInterval(t.interval);
      t.running = false;
      t.remaining = Math.max(0, Math.round((t.endAt - Date.now()) / 1000));
      document.title = this.baseTitle;
      this.say('Timer paused at ' + mmss(t.remaining) + '.');
    } else {
      if (t.remaining <= 0) t.remaining = t.total;
      t.endAt = Date.now() + t.remaining * 1000;
      t.running = true;
      t.interval = setInterval(function () { self.timerTick(); }, 500);
      this.say(t.label + ' started, ' + Math.round(t.remaining / 60) + ' minutes.');
    }
    this.renderTimer();
  };

  Dashboard.prototype.timerReset = function () {
    var t = this.timer;
    clearInterval(t.interval);
    t.running = false;
    t.remaining = t.total;
    if (this.baseTitle) document.title = this.baseTitle;
    this.renderTimer();
  };

  Dashboard.prototype.timerPreset = function (pr) {
    var t = this.timer;
    t.total = pr.minutes * 60;
    t.label = pr.label;
    this.timerReset();
    this.say(pr.label + ' set to ' + pr.minutes + ' minutes.');
  };

  Dashboard.prototype.timerDone = function () {
    var t = this.timer;
    clearInterval(t.interval);
    t.running = false;
    pomodoro.addSession(t.total / 60);
    var msg = t.label + ' finished. Time for a break.';
    try {
      if ('Notification' in window && Notification.permission === 'granted') {
        new Notification('ImpactMojo focus timer', { body: msg, icon: '/assets/images/favicon-32x32.png' });
      }
    } catch (e) {}
    try {
      var Ctx = window.AudioContext || window.webkitAudioContext;
      if (Ctx) {
        var ctx = new Ctx(), o = ctx.createOscillator(), g = ctx.createGain();
        o.frequency.value = 660; g.gain.value = 0.08;
        o.connect(g); g.connect(ctx.destination);
        o.start(); o.stop(ctx.currentTime + 0.4);
      }
    } catch (e) {}
    t.remaining = t.total;
    if (this.baseTitle) document.title = this.baseTitle;
    this.renderTimer();
    this.say(msg);
  };

  // ---- Study music -------------------------------------------------------

  Dashboard.prototype.renderMusic = function () {
    var p = this.panels.music;
    if (p.childNodes.length) return;
    this.head(p, 'Study music');
    p.appendChild(el('p', { className: 'lt-muted', text: 'Playlists to study with. Each opens on Spotify or YouTube in a new tab, so nothing plays or loads on this page.' }));
    var grid = el('div', { className: 'lt-music-grid' });
    PLAYLISTS.forEach(function (pl) {
      grid.appendChild(el('div', { className: 'lt-music-card' }, [
        el('h4', { text: pl.title }),
        el('p', { text: pl.description }),
        el('div', { className: 'lt-actions' }, [
          el('a', { className: 'lt-btn', href: pl.spotify, target: '_blank', rel: 'noopener noreferrer' },
            ['Spotify', el('span', { className: 'lt-sr', text: ': ' + pl.title + ' (opens in a new tab)' })]),
          el('a', { className: 'lt-btn', href: pl.youtube, target: '_blank', rel: 'noopener noreferrer' },
            ['YouTube', el('span', { className: 'lt-sr', text: ': ' + pl.title + ' (opens in a new tab)' })])
        ])
      ]));
    });
    p.appendChild(grid);
  };

  // =========================================================================
  // PUBLIC API
  // =========================================================================

  var IMXLearnerTools = {
    bookmarks: bookmarks,
    notes: notes,
    compare: compare,
    streak: streak,
    analytics: analytics,
    pomodoro: pomodoro,
    READING_LISTS: READING_LISTS,
    PLAYLISTS: PLAYLISTS,
    mount: function (rootEl) {
      if (!rootEl || rootEl.__ltMounted) return null;
      rootEl.__ltMounted = true;
      var d = new Dashboard(rootEl);
      d.build();
      return d;
    }
  };

  window.IMXLearnerData = IMXLearnerData;
  window.IMXLearnerTools = IMXLearnerTools;

  // Auto-mount on any element marked data-learner-tools.
  function autoMount() {
    var nodes = document.querySelectorAll('[data-learner-tools]');
    for (var i = 0; i < nodes.length; i++) {
      if (nodes[i].getAttribute('data-record-visit') === 'true') streak.recordVisit();
      IMXLearnerTools.mount(nodes[i]);
    }
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', autoMount);
  else autoMount();
})();
