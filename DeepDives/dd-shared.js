// ImpactMojo Deep Dives — shared scripts (sprite injection + theme toggle)
(function () {
    // Sargam icon sprite — injected at top of body so all <use href="#si_*"> resolve.
    var sprite = '<svg xmlns="http://www.w3.org/2000/svg" style="display:none" aria-hidden="true">' +
        '<symbol id="si_Activity" viewBox="0 0 24 24" fill="none"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M1 12h4l4 9 7-18 3 9h4"/></symbol>' +
        '<symbol id="si_Album" viewBox="0 0 24 24" fill="none"><path stroke="currentColor" stroke-linejoin="round" stroke-miterlimit="10" stroke-width="1.5" d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10Z"/><path stroke="currentColor" stroke-linejoin="round" stroke-miterlimit="10" stroke-width="1.5" d="M12 16a4 4 0 1 0 0-8 4 4 0 0 0 0 8Z"/><path stroke="currentColor" stroke-linejoin="round" stroke-miterlimit="10" stroke-width="1.5" d="M12 13a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"/></symbol>' +
        '<symbol id="si_Arrow_right" viewBox="0 0 24 24" fill="none"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" stroke-width="1.5" d="m14 16 4-4m0 0-4-4m4 4H6"/></symbol>' +
        '<symbol id="si_Article" viewBox="0 0 24 24" fill="none"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" stroke-width="1.5" d="M8 12h8m-8 3h4M8 9h8M4.4 4h15.2A2.4 2.4 0 0 1 22 6.4v11.2a2.4 2.4 0 0 1-2.4 2.4H4.4A2.4 2.4 0 0 1 2 17.6V6.4A2.4 2.4 0 0 1 4.4 4"/></symbol>' +
        '<symbol id="si_Book" viewBox="0 0 24 24" fill="none"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" stroke-width="1.5" d="M12 7.333C12 5.5 10.5 4 8.667 4H2v12h6.708C12 16 12 19.334 12 19.334m0-12C12 5.5 13.5 4 15.333 4H22v12h-6.667C12 16 12 19.334 12 19.334m0-12v12m1.875 1.124A2.58 2.58 0 0 1 16.167 19H21m-10.875 1.458A2.54 2.54 0 0 0 7.833 19H3"/></symbol>' +
        '<symbol id="si_Crosshair_detailed" viewBox="0 0 24 24" fill="none"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" stroke-width="1.5" d="M2 12h4m12 0h4M12 22v-4m0-12V2m8 10a8 8 0 1 1-16 0 8 8 0 0 1 16 0m-5 0a3 3 0 1 1-6 0 3 3 0 0 1 6 0"/></symbol>' +
        '<symbol id="si_Database" viewBox="0 0 24 24" fill="none"><ellipse cx="12" cy="5" rx="9" ry="3" stroke="currentColor" stroke-width="1.5" fill="none"/><path d="M21 5v14c0 1.657-4.03 3-9 3s-9-1.343-9-3V5" stroke="currentColor" stroke-width="1.5" fill="none"/><path d="M21 12c0 1.657-4.03 3-9 3s-9-1.343-9-3" stroke="currentColor" stroke-width="1.5" fill="none"/></symbol>' +
        '<symbol id="si_Direction_alt" viewBox="0 0 24 24" fill="none"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" stroke-width="1.5" d="m3 3 18 7.92-7.987 2.093L10.92 21z"/></symbol>' +
        '<symbol id="si_Flare" viewBox="0 0 24 24" fill="none"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" stroke-width="1.5" d="M7 12H1m22 0h-6m-5 5v6m3.536-7.464 1.414 1.414m-9.9-9.9 1.414 1.414m7.072 0L16.95 7.05m-9.9 9.9 1.414-1.414M12 1v6m2 5a2 2 0 1 1-4 0 2 2 0 0 1 4 0"/></symbol>' +
        '<symbol id="si_Globe_detailed" viewBox="0 0 24 24" fill="none"><path stroke="currentColor" stroke-linejoin="round" stroke-miterlimit="10" stroke-width="1.5" d="M22 12c0 5.523-4.477 10-10 10m10-10c0-5.523-4.477-10-10-10m10 10H2m10 10C6.477 22 2 17.523 2 12m10 10 .66-.31c2.1-2.71 3.34-6.14 3.34-9.78s-1.22-7-3.27-9.69L12 2m0 20-.73-.31A15.94 15.94 0 0 1 8 12c0-3.64 1.24-7.07 3.34-9.78L12 2M2 12C2 6.477 6.477 2 12 2m7.14 17c-1.82-1.85-4.34-3-7.14-3s-5.33 1.15-7.14 3M19.14 5C17.33 6.85 14.8 8 12 8S6.68 6.85 4.86 5"/></symbol>' +
        '<symbol id="si_Heart" viewBox="0 0 24 24" fill="none"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M16.696 3C14.652 3 12.887 4.197 12 5.943 11.113 4.197 9.348 3 7.304 3 4.374 3 2 5.457 2 8.481s1.817 5.796 4.165 8.073S12 21 12 21s3.374-2.133 5.835-4.446C20.46 14.088 22 11.514 22 8.481S19.626 3 16.696 3"/></symbol>' +
        '<symbol id="si_Help" viewBox="0 0 24 24" fill="none"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" stroke-width="1.5" d="M11.83 14v-.621a2.33 2.33 0 0 1 1.164-2.02c1.126-.66 1.514-2.057.854-3.183s-2.057-1.514-3.183-.854C9.965 7.75 9.5 8.487 9.5 9.341M12 17h-.008M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12s4.477 10 10 10 10-4.477 10-10"/></symbol>' +
        '<symbol id="si_Info" viewBox="0 0 24 24" fill="none"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" stroke-width="1.5" d="M12 8h.008M12 16v-5m10 1c0 5.523-4.477 10-10 10S2 17.523 2 12 6.477 2 12 2s10 4.477 10 10"/></symbol>' +
        '<symbol id="si_Library_books" viewBox="0 0 24 24" fill="none"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" stroke-width="1.5" d="M10 11h8m-8 3h4m-4-6h8m2 14H8.4C5.42 22 3 19.58 3 16.6V5m5.4-2h11.2A2.4 2.4 0 0 1 22 5.4v11.2a2.4 2.4 0 0 1-2.4 2.4H8.4A2.4 2.4 0 0 1 6 16.6V5.4A2.4 2.4 0 0 1 8.4 3"/></symbol>' +
        '<symbol id="si_Lightning" viewBox="0 0 24 24" fill="none"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" stroke-width="1.5" d="m12.667 10.5 1.25-7.5L6 13h5l-1.25 7.5 7.917-10z"/></symbol>' +
        '<symbol id="si_Lock" viewBox="0 0 24 24" fill="none"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" stroke-width="1.5" d="M8 10V7c0-2.21 1.79-4 4-4s4 1.79 4 4v3m-4 5a1 1 0 1 0 0-2 1 1 0 0 0 0 2m0 0v3m-5.4-8h10.8c.88 0 1.6.72 1.6 1.6v7c0 1.32-1.08 2.4-2.4 2.4H7.4C6.08 21 5 19.92 5 18.6v-7c0-.88.72-1.6 1.6-1.6"/></symbol>' +
        '<symbol id="si_Mail" viewBox="0 0 24 24" fill="none"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="m5 7.06 6.87 5.89c.07.06.19.06.26 0L19 7.06M3.2 4h17.6c.66 0 1.2.54 1.2 1.2v12.4c0 1.32-1.08 2.4-2.4 2.4H4.4C3.08 20 2 18.92 2 17.6V5.2C2 4.54 2.54 4 3.2 4"/></symbol>' +
        '</svg>';

    function inject() {
        if (document.getElementById('dd-sargam-sprite')) return;
        var wrap = document.createElement('div');
        wrap.id = 'dd-sargam-sprite';
        wrap.innerHTML = sprite;
        document.body.insertBefore(wrap, document.body.firstChild);
    }
    if (document.body) inject();
    else document.addEventListener('DOMContentLoaded', inject);

    // 3-mode theme toggle (system / light / dark)
    function applyTheme(t) {
        if (t === 'system') {
            var d = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
            document.documentElement.classList.toggle('dark', d);
        } else {
            document.documentElement.classList.toggle('dark', t === 'dark');
        }
    }
    function updateButtons(pref) {
        document.querySelectorAll('.im-theme-btn').forEach(function (btn) {
            btn.classList.toggle('active', btn.getAttribute('data-imtheme') === pref);
        });
    }
    var saved = localStorage.getItem('im-theme') || 'system';
    applyTheme(saved);
    function bindToggle() {
        updateButtons(saved);
        document.querySelectorAll('.im-theme-btn').forEach(function (btn) {
            btn.addEventListener('click', function () {
                var t = this.getAttribute('data-imtheme');
                localStorage.setItem('im-theme', t);
                applyTheme(t);
                updateButtons(t);
            });
        });
    }
    if (document.body) bindToggle();
    else document.addEventListener('DOMContentLoaded', bindToggle);
})();
