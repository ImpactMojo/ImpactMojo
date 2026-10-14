/* ImpactMojo: load Google Analytics only after the reader has accepted it.
   Pages queue their gtag() calls inline, with consent defaulting to denied.
   Until this file finds a "granted" choice, gtag.js (about 180 KB) is not
   downloaded at all, so a reader who has not chosen, or has declined, pays
   nothing for it. The Accept button in js/site-chrome.js calls
   window.imLoadGA() so analytics starts on the page where the reader accepts. */
(function () {
  var ID = 'G-JRCMEB9TBW', loaded = false;
  function granted() {
    try {
      var v = localStorage.getItem('im-analytics-consent');
      if (v) return v === 'granted';
      return localStorage.getItem('cookieConsent') === 'true';
    } catch (e) { return false; }
  }
  window.imLoadGA = function () {
    if (loaded) return;
    loaded = true;
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + ID;
    document.head.appendChild(s);
  };
  if (granted()) window.imLoadGA();
})();
