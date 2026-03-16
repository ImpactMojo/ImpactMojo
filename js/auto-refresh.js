/**
 * ImpactMojo Auto-Refresh
 * Silently reloads the page when a new version is deployed.
 * Checks /version.json every 60 seconds. If the version string
 * changes, the page reloads automatically.
 *
 * To trigger a refresh on deploy, update version.json with a new
 * timestamp or build ID (e.g. via a Netlify build command).
 */
(function () {
  'use strict';

  var CHECK_INTERVAL = 60000; // 60 seconds
  var currentVersion = null;

  function check() {
    // Only check when tab is visible — no wasted requests
    if (document.visibilityState !== 'visible') return;

    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/version.json?_=' + Date.now(), true);
    xhr.timeout = 5000;
    xhr.onload = function () {
      if (xhr.status !== 200) return;
      try {
        var data = JSON.parse(xhr.responseText);
        var v = data.v || data.version || '';
        if (!v) return;

        if (currentVersion === null) {
          // First check — just record the version
          currentVersion = v;
        } else if (v !== currentVersion) {
          // Version changed — reload silently
          console.log('[AutoRefresh] New version detected:', v);
          window.location.reload();
        }
      } catch (_) { /* ignore parse errors */ }
    };
    xhr.onerror = function () { /* ignore network errors */ };
    xhr.send();
  }

  // Start checking after page is fully loaded
  if (document.readyState === 'complete') {
    check();
  } else {
    window.addEventListener('load', check);
  }

  setInterval(check, CHECK_INTERVAL);
})();
