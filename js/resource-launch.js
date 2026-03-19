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
    'rq-builder':         'https://researchquestions.netlify.app/',
    // Professional tier
    'code-convert-pro':   'https://stats-assist.netlify.app/',
    'qual-insights':      'https://qual-lab.netlify.app/',
    'vaniscribe':         'https://vaniscribe.netlify.app/',
    'devdata-practice':   'https://impactmojo-devdata-pro.netlify.app/',
    'viz-cookbook':        'https://impactmojo-devdata-pro.netlify.app/charts.html',
    'devecon-toolkit':    'https://impactmojo-devecon-toolkit.netlify.app/',
    // Workshop Pro templates
    'toc-workshop-pro':   'https://impactmojo-workshop-pro.netlify.app/toc-pro.html',
    'logframe-pro':       'https://impactmojo-workshop-pro.netlify.app/logframe-pro.html',
    'chart-selector-pro': 'https://impactmojo-workshop-pro.netlify.app/chart-selector-pro.html',
    'stakeholder-pro':    'https://impactmojo-workshop-pro.netlify.app/stakeholder-pro.html',
    'empathy-pro':        'https://impactmojo-workshop-pro.netlify.app/empathy-pro.html',
    'policy-canvas-pro':  'https://impactmojo-workshop-pro.netlify.app/policy-canvas-pro.html',
    'ai-canvas-pro':      'https://impactmojo-workshop-pro.netlify.app/ai-canvas-pro.html',
    // Field Notes Pro
    'field-notes-pro':    'https://impactmojo-field-notes-pro.netlify.app/',
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

    // Open a blank tab immediately (must happen synchronously from the
    // click event or browsers will block the popup)
    var newTab = window.open('about:blank', '_blank');

    try {
      // 3. Get the user's current access token
      let { data: { session } } = await supabaseClient.auth.getSession();
      if (!session?.access_token) {
        if (newTab) newTab.close();
        window.location.href = '/login.html';
        return;
      }

      // Helper: call the Edge Function with a given token
      async function mintToken(accessToken) {
        return fetch(EDGE_FN_URL, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Authorization: 'Bearer ' + accessToken,
          },
          body: JSON.stringify({ resource: resourceId }),
        });
      }

      // 4. Call the Edge Function to mint a resource token
      let res = await mintToken(session.access_token);

      // If 401, the session may be stale — refresh and retry once
      if (res.status === 401) {
        const { data: refreshed } = await supabaseClient.auth.refreshSession();
        if (refreshed?.session?.access_token) {
          res = await mintToken(refreshed.session.access_token);
        }
      }

      if (res.status === 403) {
        const body = await res.json();
        if (body.code === 'TIER' || body.code === 'INACTIVE') {
          if (newTab) newTab.close();
          window.location.href = '/premium.html';
          return;
        }
      }

      if (!res.ok) {
        const body = await res.json().catch(() => ({}));
        console.error('Token mint failed:', res.status, body);
        // Fallback: open the resource directly without a token
        if (newTab) {
          newTab.location.href = baseUrl;
        } else {
          window.open(baseUrl, '_blank');
        }
        return;
      }

      const { token } = await res.json();

      // 5. Navigate the pre-opened tab to the resource with the token
      if (newTab) {
        newTab.location.href = baseUrl + '?token=' + encodeURIComponent(token);
      } else {
        window.open(baseUrl + '?token=' + encodeURIComponent(token), '_blank');
      }
    } catch (err) {
      console.error('Resource launch error:', err);
      // Fallback: open directly on any error
      if (newTab) {
        newTab.location.href = baseUrl;
      } else {
        window.open(baseUrl, '_blank');
      }
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
