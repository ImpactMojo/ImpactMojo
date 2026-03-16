/**
 * ImpactMojo Auth Gate
 * Version: 1.0.0
 * Date: March 16, 2026
 *
 * Shared auth-gated page logic for pages that require login.
 * Replaces the duplicated DOMContentLoaded → waitForAuthReady → redirect
 * pattern in account.html, org-dashboard.html, etc.
 *
 * USAGE — just add a data attribute to your page's body or wrapper:
 *
 *   AuthGate.protect({
 *       loadingEl:    document.getElementById('loadingOverlay'),
 *       redirectUrl:  'login.html',           // where to send unauthenticated users
 *       requiredTier: null,                   // or 'practitioner', 'organization', etc.
 *       timeoutMs:    10000,                  // safety timeout (default 10s)
 *       onReady:      function(user, profile) { ... }   // called when auth passes
 *   });
 *
 * PREREQUISITES:
 *   <script src="js/config.js"></script>
 *   <script src="js/auth.js"></script>
 *   <script src="js/auth-gate.js"></script>
 */

(function () {
  'use strict';

  var AuthGate = {

    _protected: false,

    /**
     * Protect a page behind authentication.
     * Call once from DOMContentLoaded or inline script.
     *
     * @param {Object} opts
     * @param {HTMLElement}  opts.loadingEl    - overlay to hide when ready
     * @param {string}       opts.redirectUrl  - redirect target for unauthenticated users (default: 'login.html')
     * @param {string|null}  opts.requiredTier - tier required to access the page (null = any logged-in user)
     * @param {number}       opts.timeoutMs    - safety timeout before fallback checks (default: 10000)
     * @param {Function}     opts.onReady      - callback(user, profile) when auth passes
     * @param {Function}     opts.onDenied     - optional callback when auth fails but you don't want a redirect
     */
    protect: async function (opts) {
      if (this._protected) return;
      this._protected = true;

      var loadingEl   = opts.loadingEl || null;
      var redirectUrl = opts.redirectUrl || 'login.html';
      var requiredTier = opts.requiredTier || null;
      var timeoutMs   = opts.timeoutMs || 10000;
      var onReady     = opts.onReady || function () {};
      var onDenied    = opts.onDenied || null;
      var pageReady   = false;

      // Helper: hide loading and run callback
      function succeed(user, profile) {
        if (pageReady) return;
        pageReady = true;
        if (loadingEl) loadingEl.style.display = 'none';
        onReady(user, profile);
      }

      // Helper: redirect or call onDenied
      function deny() {
        if (pageReady) return;
        pageReady = true;
        if (loadingEl) loadingEl.style.display = 'none';
        if (onDenied) {
          onDenied();
        } else {
          window.location.href = redirectUrl;
        }
      }

      // Helper: check user + tier and call succeed/deny
      function checkAndProceed(user, profile) {
        if (!user) {
          deny();
          return;
        }
        if (requiredTier) {
          var tierHierarchy = ['explorer', 'practitioner', 'professional', 'organization'];
          var userTier = (profile && profile.subscription_tier) || 'explorer';
          if (tierHierarchy.indexOf(userTier) < tierHierarchy.indexOf(requiredTier)) {
            deny();
            return;
          }
        }
        succeed(user, profile);
      }

      // ------- Safety timeout -------
      // If auth never resolves, check Supabase directly before giving up
      var safetyTimer = setTimeout(async function () {
        if (pageReady) return;
        try {
          var session = await ImpactMojoAuth.getSession();
          if (session && session.user) {
            ImpactMojoAuth.user = session.user;
            try { await ImpactMojoAuth.fetchProfile(); } catch (_) {}
            checkAndProceed(ImpactMojoAuth.user, ImpactMojoAuth.profile);
            ImpactMojoAuth.updateUI();
            return;
          }
        } catch (_) { /* proceed with deny */ }
        deny();
      }, timeoutMs);

      // ------- Listen for auth state changes -------
      // If the auth event fires while we're waiting, handle it immediately
      function onAuthChanged(e) {
        if (pageReady) return;
        if (!ImpactMojoAuth.isAuthReady) return;
        if (e.detail && e.detail.isLoggedIn) {
          clearTimeout(safetyTimer);
          checkAndProceed(ImpactMojoAuth.user, ImpactMojoAuth.profile);
        }
        // Do NOT redirect on logout events here — the main flow handles it
      }
      window.addEventListener('authStateChanged', onAuthChanged);

      // ------- Main flow -------
      try {
        await ImpactMojoAuth.init();
        await ImpactMojoAuth.waitForAuthReady();
      } catch (e) {
        console.error('[AuthGate] Auth ready wait failed:', e);
      }

      if (pageReady) return; // authStateChanged already handled it
      clearTimeout(safetyTimer);

      if (ImpactMojoAuth.isLoggedIn()) {
        checkAndProceed(ImpactMojoAuth.user, ImpactMojoAuth.profile);
      } else {
        // Fallback: double-check with Supabase directly
        // Catches transient SIGNED_OUT during token refresh
        try {
          var fallbackSession = await ImpactMojoAuth.getSession();
          if (fallbackSession && fallbackSession.user) {
            ImpactMojoAuth.user = fallbackSession.user;
            try { await ImpactMojoAuth.fetchProfile(); } catch (_) {}
            checkAndProceed(ImpactMojoAuth.user, ImpactMojoAuth.profile);
            ImpactMojoAuth.updateUI();
            return;
          }
        } catch (_) { /* proceed with deny */ }
        deny();
      }
    }
  };

  window.AuthGate = AuthGate;
})();
