/**
 * ImpactMojo Client-Side Token Gate
 * Version: 1.0.0
 *
 * Drop-in script for GitHub Pages (or any static host) that verifies
 * the ?token= JWT before allowing page content to render.
 *
 * HOW IT WORKS:
 *   1. Page loads with all content hidden (CSS: body { visibility: hidden })
 *   2. This script reads ?token= from the URL
 *   3. Verifies the HS256 signature using Web Crypto API
 *   4. Checks exp and resource claims
 *   5. If valid → reveals content and strips token from URL bar
 *   6. If invalid → redirects to the ImpactMojo premium page
 *
 * SECURITY NOTE:
 *   The HMAC secret is embedded in client-side JS. This is NOT secure
 *   against a determined attacker who reads the page source. It IS
 *   sufficient to block casual URL sharing (the token expires in 5 min
 *   and is tied to a specific resource).
 *
 * SETUP — add to your GitHub Pages <head>:
 *
 *   <style>body{visibility:hidden}</style>
 *   <script>window.__RESOURCE_ID='devdata-practice';</script>
 *   <script src="https://www.impactmojo.in/js/token-gate.js"></script>
 *
 *   Then set the secret below (or override via window.__TOKEN_SECRET).
 */

(function () {
  'use strict';

  // ── Configuration ─────────────────────────────────────────────────
  // The resource ID this page represents (set via window.__RESOURCE_ID)
  var RESOURCE_ID = window.__RESOURCE_ID || '';

  // HMAC-SHA256 secret — MUST match RESOURCE_TOKEN_SECRET in Supabase.
  // Override per-site via window.__TOKEN_SECRET if needed.
  var SECRET = window.__TOKEN_SECRET || '';

  // Where to send users on failure
  var PREMIUM_URL = 'https://www.impactmojo.in/premium';
  var LOGIN_URL = 'https://www.impactmojo.in/login.html';

  // Session storage key for caching validation
  var CACHE_KEY = 'im_gate_' + RESOURCE_ID;

  // ── Helpers ───────────────────────────────────────────────────────

  function base64UrlDecode(str) {
    str = str.replace(/-/g, '+').replace(/_/g, '/');
    var pad = str.length % 4;
    if (pad) str += '===='.slice(pad);
    return atob(str);
  }

  function base64UrlToUint8(str) {
    var raw = base64UrlDecode(str);
    var arr = new Uint8Array(raw.length);
    for (var i = 0; i < raw.length; i++) arr[i] = raw.charCodeAt(i);
    return arr;
  }

  function reveal() {
    document.body.style.visibility = 'visible';
  }

  function deny() {
    window.location.replace(PREMIUM_URL);
  }

  // ── JWT verification via Web Crypto ───────────────────────────────

  async function verifyToken(token) {
    var parts = token.split('.');
    if (parts.length !== 3) return null;

    var header = parts[0];
    var payload = parts[1];
    var signature = base64UrlToUint8(parts[2]);

    // Import the secret as an HMAC key
    var enc = new TextEncoder();
    var key = await crypto.subtle.importKey(
      'raw',
      enc.encode(SECRET),
      { name: 'HMAC', hash: 'SHA-256' },
      false,
      ['verify']
    );

    // Verify signature over "header.payload"
    var data = enc.encode(header + '.' + payload);
    var valid = await crypto.subtle.verify('HMAC', key, signature, data);
    if (!valid) return null;

    // Decode and return the payload
    try {
      return JSON.parse(base64UrlDecode(payload));
    } catch (_) {
      return null;
    }
  }

  // ── Main gate logic ───────────────────────────────────────────────

  async function gate() {
    // If no secret or resource ID configured, let the page through
    // (misconfigured — better to show content than break the site)
    if (!SECRET || !RESOURCE_ID) {
      reveal();
      return;
    }

    // Check for cached valid session (avoids re-verifying on SPA nav)
    var cached = sessionStorage.getItem(CACHE_KEY);
    if (cached) {
      var cachedExp = parseInt(cached, 10);
      if (cachedExp > Math.floor(Date.now() / 1000)) {
        reveal();
        return;
      }
      sessionStorage.removeItem(CACHE_KEY);
    }

    // Read ?token= from URL
    var params = new URLSearchParams(window.location.search);
    var token = params.get('token');

    if (!token) {
      deny();
      return;
    }

    // Verify the JWT
    var claims = await verifyToken(token);

    if (!claims) {
      deny();
      return;
    }

    // Check expiry
    var now = Math.floor(Date.now() / 1000);
    if (!claims.exp || claims.exp < now) {
      deny();
      return;
    }

    // Check resource claim matches this site
    if (claims.resource !== RESOURCE_ID) {
      deny();
      return;
    }

    // Valid! Cache until expiry and reveal content
    sessionStorage.setItem(CACHE_KEY, String(claims.exp));

    // Strip the token from the URL bar (cosmetic + prevents accidental sharing)
    params.delete('token');
    var cleanUrl = window.location.pathname;
    var remaining = params.toString();
    if (remaining) cleanUrl += '?' + remaining;
    cleanUrl += window.location.hash;
    window.history.replaceState(null, '', cleanUrl);

    reveal();
  }

  // Run immediately
  gate().catch(function () {
    // On any unexpected error, deny access
    deny();
  });
})();
