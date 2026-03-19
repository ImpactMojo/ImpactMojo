/**
 * ImpactMojo Premium Resource Launcher
 * Version: 1.1.0
 *
 * Client-side helper that requests a short-lived JWT from the
 * Supabase Edge Function and opens the gated resource in a new tab.
 *
 * Usage:
 *   <button onclick="ImpactMojoResource.launch('vaniscribe')">Open VaniScribe</button>
 *
 * Depends on: js/config.js, js/auth.js (provides `supabaseClient` and `ImpactMojoAuth`)
 */

(function () {
  'use strict';

  // ── Map resource IDs to their REAL deployment URLs ─────────────────
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

  // Resolve the Edge Function URL at call time (not parse time)
  // so config.js and auth.js are guaranteed to have loaded first.
  function getEdgeFnUrl() {
    var base = (window.ImpactMojoConfig && window.ImpactMojoConfig.SUPABASE_URL)
            || (typeof SUPABASE_URL !== 'undefined' && SUPABASE_URL)
            || 'https://ddyszmfffyedolkcugld.supabase.co';
    return base + '/functions/v1/mint-resource-token';
  }

  // Navigate a tab to a URL, with window.open fallback
  function navigateTab(tab, url) {
    if (tab && !tab.closed) {
      tab.location.href = url;
    } else {
      window.open(url, '_blank');
    }
  }

  /**
   * Launch a premium resource.
   * @param {string} resourceId  — one of the keys in RESOURCE_URLS
   */
  async function launch(resourceId) {
    // 1. Resolve the resource URL first
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

    // 3. Check supabaseClient is available
    if (typeof supabaseClient === 'undefined') {
      console.error('supabaseClient not available');
      window.open(baseUrl, '_blank');
      return;
    }

    // Open a blank tab immediately (must happen synchronously from the
    // click event or browsers will block the popup)
    var newTab = window.open('about:blank', '_blank');

    try {
      // 4. Get the user's current access token — try getSession first,
      //    fall back to refreshSession if stale
      var accessToken = null;

      var sessionResult = await supabaseClient.auth.getSession();
      if (sessionResult.data && sessionResult.data.session) {
        accessToken = sessionResult.data.session.access_token;
      }

      if (!accessToken) {
        // Session cache empty — try refreshing
        var refreshResult = await supabaseClient.auth.refreshSession();
        if (refreshResult.data && refreshResult.data.session) {
          accessToken = refreshResult.data.session.access_token;
        }
      }

      if (!accessToken) {
        // Auth is truly gone — open resource directly as fallback
        console.warn('No valid session, opening resource directly');
        navigateTab(newTab, baseUrl);
        return;
      }

      // 5. Call the Edge Function to mint a resource token
      var edgeFnUrl = getEdgeFnUrl();
      var res = await fetch(edgeFnUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + accessToken,
        },
        body: JSON.stringify({ resource: resourceId }),
      });

      // If 401, the token may be stale — refresh and retry once
      if (res.status === 401) {
        var retry = await supabaseClient.auth.refreshSession();
        if (retry.data && retry.data.session) {
          accessToken = retry.data.session.access_token;
          res = await fetch(edgeFnUrl, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': 'Bearer ' + accessToken,
            },
            body: JSON.stringify({ resource: resourceId }),
          });
        }
      }

      // 403 = tier too low or inactive subscription
      if (res.status === 403) {
        var forbiddenBody = await res.json().catch(function () { return {}; });
        if (forbiddenBody.code === 'TIER' || forbiddenBody.code === 'INACTIVE') {
          if (newTab && !newTab.closed) newTab.close();
          window.location.href = '/premium';
          return;
        }
      }

      if (!res.ok) {
        var errBody = await res.json().catch(function () { return {}; });
        console.error('Token mint failed:', res.status, errBody);
        // Fallback: open the resource directly
        navigateTab(newTab, baseUrl);
        return;
      }

      var data = await res.json();

      // 6. Navigate the pre-opened tab to the resource with the token
      navigateTab(newTab, baseUrl + '?token=' + encodeURIComponent(data.token));
    } catch (err) {
      console.error('Resource launch error:', err);
      // Fallback: open directly on any error
      navigateTab(newTab, baseUrl);
    }
  }

  // ── Public API ────────────────────────────────────────────────────
  window.ImpactMojoResource = {
    launch: launch,
    RESOURCE_URLS: RESOURCE_URLS,
    version: '1.1.0',
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
