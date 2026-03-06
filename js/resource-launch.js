/**
 * ImpactMojo Premium Resource Launcher
 * Version: 1.0.0
 *
 * Client-side helper that requests a short-lived JWT from the
 * Supabase Edge Function and opens the gated resource in a new tab.
 *
 * Usage:
 *   <button onclick="ImpactMojoResource.launch('vaniscribe')">Open VaniScribe</button>
 *
 * Depends on: js/auth.js (provides `supabaseClient` and `ImpactMojoAuth`)
 */

(function () {
  'use strict';

  // ── Map resource IDs to their REAL deployment URLs ─────────────────
  // The launcher opens these directly (bypassing short.io cloaking)
  // so the ?token= query param reaches the auth-gate / token-gate.
  const RESOURCE_URLS = {
    // Practitioner tier
    'field-notes':      'https://marginmuse.space/themarginmuse',
    'rq-builder':       'https://researchquestions.netlify.app/',
    // Professional tier
    'code-convert-pro': 'https://stats-assist.netlify.app/',
    'qual-insights':    'https://qual-lab.netlify.app/',
    'vaniscribe':       'https://vaniscribe.netlify.app/',
    'devdata-practice': 'https://varnasr.github.io/devdata-practice/',
    'viz-cookbook':      'https://varnasr.github.io/devdata-practice/charts.html',
    'devecon-toolkit':  'https://varnasr.github.io/deveconomics-toolkit/',
  };

  // Supabase Edge Function URL (auto-derived from the Supabase project URL in auth.js)
  const EDGE_FN_URL = SUPABASE_URL + '/functions/v1/mint-resource-token';

  /**
   * Launch a premium resource.
   * @param {string} resourceId  — one of the keys in RESOURCE_URLS
   */
  async function launch(resourceId) {
    // 1. Must be logged in
    if (!ImpactMojoAuth.isLoggedIn()) {
      sessionStorage.setItem('authRedirect', window.location.href);
      window.location.href = '/login.html';
      return;
    }

    // 2. Resolve the resource URL
    const baseUrl = RESOURCE_URLS[resourceId];
    if (!baseUrl) {
      console.error('Unknown resource:', resourceId);
      return;
    }

    try {
      // 3. Get the user's current access token
      const { data: { session } } = await supabaseClient.auth.getSession();
      if (!session?.access_token) {
        window.location.href = '/login.html';
        return;
      }

      // 4. Call the Edge Function to mint a resource token
      const res = await fetch(EDGE_FN_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: 'Bearer ' + session.access_token,
        },
        body: JSON.stringify({ resource: resourceId }),
      });

      if (res.status === 403) {
        const body = await res.json();
        if (body.code === 'TIER' || body.code === 'INACTIVE') {
          window.location.href = '/premium.html';
          return;
        }
      }

      if (!res.ok) {
        const body = await res.json().catch(() => ({}));
        console.error('Token mint failed:', res.status, body);
        alert('Unable to access this resource. Please try again or contact support.');
        return;
      }

      const { token } = await res.json();

      // 5. Open the resource in a new tab with the token
      window.open(baseUrl + '?token=' + encodeURIComponent(token), '_blank');
    } catch (err) {
      console.error('Resource launch error:', err);
      alert('Something went wrong. Please check your connection and try again.');
    }
  }

  // ── Public API ────────────────────────────────────────────────────
  window.ImpactMojoResource = {
    launch,
    RESOURCE_URLS,
    version: '1.0.0',
  };

  // ── Auto-intercept clicks on links with data-resource-id ─────────
  // Works with premium.js: when locked, premium.js captures the click
  // first (capture phase) and shows the upgrade modal. When unlocked,
  // this handler runs and routes through the JWT launcher.
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
