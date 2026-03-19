/**
 * ImpactMojo Premium Resource Launcher
 * Version: 2.0.0
 *
 * Opens premium resources directly for authenticated users.
 * No JWT minting — resource sites are access-gated at the platform level
 * (via premium.js tier checks), not at the resource site level.
 *
 * Usage:
 *   <button onclick="ImpactMojoResource.launch('vaniscribe')">Open VaniScribe</button>
 *
 * Depends on: js/auth.js (provides `ImpactMojoAuth`)
 */

(function () {
  'use strict';

  // ── Map resource IDs to their deployment URLs ─────────────────────
  var RESOURCE_URLS = {
    // Practitioner tier
    'rq-builder':         'https://researchquestions.netlify.app/',
    // Professional tier
    'vaniscribe':         'https://vaniscribe.netlify.app/',
    'devdata-practice':   'https://impactmojo-devdata-pro.netlify.app/',
    'viz-cookbook':        'https://impactmojo-devdata-pro.netlify.app/charts.html',
    'devecon-toolkit':    'https://impactmojo-devecon-toolkit.netlify.app/',
    'field-notes-pro':    'https://impactmojo-field-notes-pro.netlify.app/',
    // Workshop Pro templates
    'toc-workshop-pro':   'https://impactmojo-workshop-pro.netlify.app/toc-pro.html',
    'logframe-pro':       'https://impactmojo-workshop-pro.netlify.app/logframe-pro.html',
    'chart-selector-pro': 'https://impactmojo-workshop-pro.netlify.app/chart-selector-pro.html',
    'stakeholder-pro':    'https://impactmojo-workshop-pro.netlify.app/stakeholder-pro.html',
    'empathy-pro':        'https://impactmojo-workshop-pro.netlify.app/empathy-pro.html',
    'policy-canvas-pro':  'https://impactmojo-workshop-pro.netlify.app/policy-canvas-pro.html',
    'ai-canvas-pro':      'https://impactmojo-workshop-pro.netlify.app/ai-canvas-pro.html',
  };

  /**
   * Launch a premium resource.
   * @param {string} resourceId  — one of the keys in RESOURCE_URLS
   */
  function launch(resourceId) {
    // 1. Resolve the resource URL
    var baseUrl = RESOURCE_URLS[resourceId];
    if (!baseUrl) {
      console.error('Unknown resource:', resourceId);
      return;
    }

    // 2. Must be logged in
    if (typeof ImpactMojoAuth === 'undefined' || !ImpactMojoAuth.isLoggedIn()) {
      sessionStorage.setItem('authRedirect', window.location.href);
      window.location.href = '/login';
      return;
    }

    // 3. Open the resource directly
    window.open(baseUrl, '_blank');
  }

  // ── Public API ────────────────────────────────────────────────────
  window.ImpactMojoResource = {
    launch: launch,
    RESOURCE_URLS: RESOURCE_URLS,
    version: '2.0.0',
  };

  // ── Auto-intercept clicks on links with data-resource-id ─────────
  document.addEventListener('click', function (e) {
    var link = e.target.closest('a[data-resource-id]');
    if (!link) return;

    // If premium.js has locked the parent card, let it handle the click
    var card = link.closest('[data-locked-tier]');
    if (card) return;

    e.preventDefault();
    e.stopPropagation();
    launch(link.dataset.resourceId);
  });
})();
