/**
 * ImpactMojo Product Tours (Intro.js)
 * Provides guided walkthroughs for first-time visitors on major pages.
 * Tours start from a "Take a tour" button; completion is remembered in localStorage.
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

  /**
   * Open the parent dropdown for a step's element so Intro.js can see it.
   * Returns true if a dropdown was opened, false otherwise.
   */
  function ensureDropdownVisible(selector) {
    if (!selector) return false;
    var el = document.querySelector(selector);
    if (!el) return false;

    // If the element is inside a .dropdown-menu, force-open the parent .has-dropdown
    var dropdownMenu = el.closest('.dropdown-menu');
    if (dropdownMenu) {
      var parentLi = dropdownMenu.closest('li.has-dropdown');
      if (parentLi) {
        // `.open` is the nav's own reveal class (releases max-height and the
        // specials-grouped grid layout); `.tour-dropdown-open` adds the tour
        // z-index overrides on top so the menu sits above the Intro.js overlay.
        parentLi.classList.add('tour-dropdown-open', 'open');
        return true;
      }
    }
    return false;
  }

  /** Close all tour-opened dropdowns */
  function closeAllTourDropdowns() {
    document.querySelectorAll('.tour-dropdown-open').forEach(function (el) {
      el.classList.remove('tour-dropdown-open', 'open');
    });
  }

  function startTour(page, steps) {
    if (typeof introJs === 'undefined') return;

    // Add tour-active class for CSS hooks
    document.body.classList.add('introjs-active-tour');

    var filtered = steps.filter(function (s) {
      if (!s.element) return true;
      // Temporarily open dropdown so the check sees the element as a reader would
      ensureDropdownVisible(s.element);
      var el = document.querySelector(s.element);
      // `whenVisible` steps must be rendered, not merely present (#1066).
      //
      // Intro.js highlights a box, so a step whose element is display:none
      // points at nothing. That is how to choose between two copies of one
      // control at different breakpoints: the search button exists twice, and
      // existence alone cannot say which one the reader can see.
      //
      // Deliberately opt-in rather than applied to every step. Measured on the
      // homepage at 390px, a blanket visibility rule drops seven of ten steps,
      // because the desktop nav items and the theme selector are display:none
      // on a phone and live in the hamburger menu instead. Those steps do
      // currently anchor to nothing on mobile, which is worth fixing, but it
      // changes what a phone visitor is shown and is not this fix's to decide.
      var ok = !!el;
      if (ok && s.whenVisible) {
        ok = el.offsetWidth > 0 || el.offsetHeight > 0 || el.getClientRects().length > 0;
      }
      closeAllTourDropdowns();
      return ok;
    });

    if (filtered.length < 2) {
      document.body.classList.remove('introjs-active-tour');
      return;
    }

    var tour = introJs.tour();
    tour.setOptions({
      steps: filtered,
      showProgress: true,
      showBullets: false,
      exitOnOverlayClick: true,
      disableInteraction: false,
      scrollToElement: true,
      scrollPadding: 80,
      nextLabel: 'Next →',
      prevLabel: '← Back',
      doneLabel: 'Done ✓',
      skipLabel: '×',
      tooltipClass: 'impactmojo-tour',
      highlightClass: 'impactmojo-highlight'
    });

    // Before each step: open the dropdown if needed
    tour.onbeforechange(function (targetEl) {
      closeAllTourDropdowns();
      if (targetEl) {
        var dropdownMenu = targetEl.closest('.dropdown-menu');
        if (dropdownMenu) {
          var parentLi = dropdownMenu.closest('li.has-dropdown');
          if (parentLi) {
            parentLi.classList.add('tour-dropdown-open', 'open');
          }
        }
      }
    });

    function cleanup() {
      markTourSeen(page);
      closeAllTourDropdowns();
      document.body.classList.remove('introjs-active-tour');
    }

    tour.oncomplete(cleanup);
    tour.onexit(cleanup);

    tour.start();
  }

  // ── Page-specific tour definitions ────────────────────────────────

  // NOTE: content counts below are scanned by scripts/check-counts.py —
  // keep the "<number> <type>" phrasing when editing.
  var TOURS = {
    index: [
      { intro: '<strong>Welcome to ImpactMojo</strong><br>Development know-how for South Asia: 22 flagship and 84 foundational courses, 135 games and 35 Free Studio tools, built by practitioners and free to use. Here is a quick look round.' },
      { element: '.im-sc-nav', whenVisible: true, intro: '<strong>Menu</strong><br>Five groups: Learn, Tools, Data, Read and Membership. Learn holds the 22 flagship courses, the 84 shorter courses of the 101 Series and Code School.' },
      { element: '.im-sc-menu', whenVisible: true, intro: '<strong>Menu</strong><br>Every part of the site, grouped as Learn, Tools, Data and Read. A small dot marks what changed recently.' },
      { element: '.im-sc-search', whenVisible: true, intro: '<strong>Search everything</strong><br>Search every course, studio, game and companion, and the answers to common questions. On a computer, Ctrl+K opens it from any page.' },
      { element: '.im-sc-lang', whenVisible: true, intro: '<strong>Language</strong><br>Read any page in Hindi, Tamil, Bengali, Marathi or Telugu.' },
      { element: '#quiz', intro: '<strong>Not sure where to start?</strong><br>Six quick questions give you a personal starting path, and the homepage remembers it.' },
      { element: '#routes', intro: '<strong>Three ways in</strong><br>Learn a method, find a tool, or look up the data. Everything here is free; Membership adds exports and Pro tools.' }
    ]
    // Tours run on the homepage only. Do not add per-page tours here.
  };

  // ── Detect current page and auto-start tour ───────────────────────

  function detectPage() {
    var path = window.location.pathname.replace(/\.html$/, '').replace(/^\//, '') || 'index';
    if (path === '' || path === 'home') path = 'index';
    return path;
  }

  // Tours start only when a reader asks for one, from a "Take a tour" button.
  // They used to open by themselves on a first visit, over the very page the
  // reader had come to read.
  function init() {}

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
