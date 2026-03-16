/**
 * ImpactMojo Product Tours (Intro.js)
 * Provides guided walkthroughs for first-time visitors on major pages.
 * Tours auto-start once per page (tracked via localStorage).
 */

(function () {
  'use strict';

  var STORAGE_PREFIX = 'impactmojo_tour_seen_';

  function hasSeenTour(page) {
    try { return localStorage.getItem(STORAGE_PREFIX + page) === '1'; }
    catch (e) { return true; }
  }

  function markTourSeen(page) {
    try { localStorage.setItem(STORAGE_PREFIX + page, '1'); }
    catch (e) { /* silent */ }
  }

  function startTour(page, steps) {
    if (typeof introJs === 'undefined') return;

    var filtered = steps.filter(function (s) {
      if (!s.element) return true;
      return document.querySelector(s.element);
    });

    if (filtered.length < 2) return;

    var tour = introJs.tour();
    tour.setOptions({
      steps: filtered,
      showProgress: true,
      showBullets: false,
      exitOnOverlayClick: true,
      disableInteraction: false,
      scrollToElement: true,
      nextLabel: 'Next →',
      prevLabel: '← Back',
      doneLabel: 'Got it!'
    });

    tour.oncomplete(function () { markTourSeen(page); });
    tour.onexit(function () { markTourSeen(page); });

    tour.start();
  }

  // ── Page-specific tour definitions ────────────────────────────────

  var TOURS = {
    index: [
      { intro: '<strong>Welcome to ImpactMojo!</strong><br>A free learning platform for MEAL, development economics, and impact research. Let us show you around.' },
      { element: '#navLinks', intro: '<strong>Navigation</strong><br>Browse Courses, Labs, Games, and Premium tools from here.' },
      { element: '#nav-courses', intro: '<strong>Courses</strong><br>39 free courses covering everything from econometrics to gender studies.' },
      { element: '#nav-labs', intro: '<strong>Labs</strong><br>Hands-on interactive tools — build a Theory of Change, design MEL frameworks, and more.' },
      { element: '#nav-games', intro: '<strong>Games</strong><br>Learn behavioral economics, game theory, and policy concepts through play.' },
      { element: '#nav-dataverse', intro: '<strong>Dataverse</strong><br>239+ curated data tools, APIs, and datasets for development research.' },
      { element: '#nav-premium', intro: '<strong>Premium</strong><br>Advanced AI-powered tools for practitioners and organizations.' },
      { element: '.theme-selector', intro: '<strong>Theme</strong><br>Switch between light, dark, and system themes.' },
      { element: '#premium', intro: '<strong>Premium Tools</strong><br>Professional-grade tools like VaniScribe AI, Code Convert Pro, and Qual Insights Lab.' }
    ],

    catalog: [
      { intro: '<strong>Course Catalog</strong><br>Browse all courses, labs, games, and premium tools in one place.' },
      { element: '#searchInput', intro: '<strong>Search</strong><br>Find courses by name, topic, or keyword.' },
      { element: '.filter-tabs', intro: '<strong>Filter by Type</strong><br>Narrow down to Flagship courses, Labs, Games, or Premium tools.' },
      { element: '.track-filters', intro: '<strong>Filter by Track</strong><br>Focus on a specific topic like MEL, Economics, or Gender Studies.' },
      { element: '#cardsGrid', intro: '<strong>Content Cards</strong><br>Click any card to open the course, lab, or game.' }
    ],

    dataverse: [
      { intro: '<strong>ImpactMojo Dataverse</strong><br>A curated collection of 239+ data tools, APIs, datasets, and MCP servers for development work.' },
      { element: '#searchInput', intro: '<strong>Search</strong><br>Search across all resources by name, description, or tag.' },
      { element: '#typeFilters', intro: '<strong>Filter by Type</strong><br>Show only APIs, datasets, tools, or MCP servers.' },
      { element: '#categoryFilters', intro: '<strong>Browse Categories</strong><br>Explore resources by domain — government data, health, climate, legal, and more.' },
      { element: '#cardGrid', intro: '<strong>Resource Cards</strong><br>Click any card for details, links, and tags.' },
      { element: '#statTotal', intro: '<strong>Stats</strong><br>See how many resources are available and what percentage are free.' }
    ],

    premium: [
      { intro: '<strong>Premium Membership</strong><br>Unlock advanced AI tools, templates, and expert support.' },
      { element: '.pricing-grid', intro: '<strong>Choose Your Tier</strong><br>Compare what each membership level includes.' },
      { element: '.pricing-card.featured', intro: '<strong>Most Popular</strong><br>The Practitioner tier unlocks RQ Builder Pro for just ₹399/month.' },
      { element: '.pricing-card.org-tier', intro: '<strong>Team Plan</strong><br>Organizations get all tools plus team management and analytics.' }
    ],

    transparency: [
      { intro: '<strong>Transparency Dashboard</strong><br>See exactly how ImpactMojo is used — all numbers, all public.' },
      { element: '.tier-grid', intro: '<strong>Revenue Model</strong><br>Our free vs paid tier structure and pricing.' },
      { element: '#kpiGrid', intro: '<strong>Platform Numbers</strong><br>Cumulative users, sessions, and engagement across the platform.' },
      { element: '#courseChart', intro: '<strong>Course Engagement</strong><br>See how each course performs over time.' },
      { element: '#platformTable', intro: '<strong>Content Library</strong><br>Full breakdown of everything on the platform.' }
    ]
  };

  // ── Detect current page and auto-start tour ───────────────────────

  function detectPage() {
    var path = window.location.pathname.replace(/\.html$/, '').replace(/^\//, '') || 'index';
    if (path === '' || path === 'home') path = 'index';
    return path;
  }

  function init() {
    var page = detectPage();
    if (!TOURS[page]) return;
    if (hasSeenTour(page)) return;

    // Delay tour start so page fully renders
    setTimeout(function () { startTour(page, TOURS[page]); }, 1500);
  }

  // Expose manual trigger for "Take a Tour" buttons
  window.ImpactMojoTour = {
    start: function (page) {
      page = page || detectPage();
      if (TOURS[page]) startTour(page, TOURS[page]);
    },
    reset: function (page) {
      page = page || detectPage();
      try { localStorage.removeItem(STORAGE_PREFIX + page); }
      catch (e) { /* silent */ }
    },
    resetAll: function () {
      Object.keys(TOURS).forEach(function (p) {
        try { localStorage.removeItem(STORAGE_PREFIX + p); }
        catch (e) { /* silent */ }
      });
    }
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
