/**
 * ImpactMojo human check (Cloudflare Turnstile) for the sign-in forms.
 *
 * Supabase Auth refuses sign-up, password sign-in, magic links and password
 * reset without a captcha token once CAPTCHA protection is switched on in the
 * Supabase dashboard. This script draws the Turnstile check into every
 * `.im-captcha` element on the page and hands js/auth.js a fresh token for
 * each attempt.
 *
 * Off until `TURNSTILE_SITE_KEY` is set in js/config.js: with no key it loads
 * nothing and `token()` resolves to null, so auth.js sends what it always did.
 * Set the key and deploy BEFORE turning CAPTCHA on in Supabase, or every sign-in
 * form stops working until the deploy lands.
 */
(function () {
  'use strict';

  var cfg = window.ImpactMojoConfig || {};
  var KEY = cfg.TURNSTILE_SITE_KEY || '';
  var widgets = [];
  var ready = null;

  function load() {
    if (ready) return ready;
    ready = new Promise(function (resolve, reject) {
      if (window.turnstile) return resolve(window.turnstile);
      window.imTurnstileLoaded = function () { resolve(window.turnstile); };
      var s = document.createElement('script');
      s.src = 'https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit&onload=imTurnstileLoaded';
      s.async = true;
      s.onerror = function () { reject(new Error('turnstile unavailable')); };
      document.head.appendChild(s);
    });
    return ready;
  }

  function theme() {
    var t = document.documentElement.getAttribute('data-theme');
    return t === 'dark' ? 'dark' : t === 'light' ? 'light' : 'auto';
  }

  function render() {
    var slots = document.querySelectorAll('.im-captcha');
    if (!slots.length) return;
    load().then(function (ts) {
      slots.forEach(function (el) {
        if (el.getAttribute('data-rendered')) return;
        el.setAttribute('data-rendered', '1');
        var w = { el: el, id: null, token: null, waiters: [] };
        w.id = ts.render(el, {
          sitekey: KEY,
          theme: theme(),
          action: el.getAttribute('data-action') || 'auth',
          callback: function (t) { w.token = t; w.waiters.splice(0).forEach(function (f) { f(t); }); },
          'expired-callback': function () { w.token = null; },
          'error-callback': function () { w.token = null; }
        });
        widgets.push(w);
      });
    }).catch(function () {
      document.querySelectorAll('.im-captcha').forEach(function (el) {
        el.textContent = 'The human check could not load. Check your connection and reload the page.';
      });
    });
  }

  /** A fresh token, waiting up to 20 seconds for the check to finish. */
  function token() {
    if (!KEY) return Promise.resolve(null);
    // The check in the form the reader is using: login.html has two forms.
    var w = widgets.filter(function (x) { return x.el.offsetParent !== null; })[0] || widgets[0];
    if (!w) return Promise.resolve(null);
    if (w.token) {
      var t = w.token;
      w.token = null;
      // A token is good for one request; ask for the next one now.
      try { window.turnstile.reset(w.id); } catch (e) { /* ignore */ }
      return Promise.resolve(t);
    }
    return new Promise(function (resolve) {
      var done = false;
      w.waiters.push(function (t) { if (!done) { done = true; w.token = null; try { window.turnstile.reset(w.id); } catch (e) {} resolve(t); } });
      setTimeout(function () { if (!done) { done = true; resolve(null); } }, 20000);
    });
  }

  window.IMCaptcha = { enabled: !!KEY, token: token };

  if (!KEY) return;
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', render);
  else render();
})();
