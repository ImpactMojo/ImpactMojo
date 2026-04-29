// ImpactMojo Deep Dives — shared theme toggle
(function() {
    function applyTheme(t) {
        if (t === 'system') {
            var d = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
            document.documentElement.classList.toggle('dark', d);
        } else {
            document.documentElement.classList.toggle('dark', t === 'dark');
        }
    }
    function updateButtons(pref) {
        document.querySelectorAll('.im-theme-btn').forEach(function(btn) {
            btn.classList.toggle('active', btn.getAttribute('data-imtheme') === pref);
        });
    }
    var saved = localStorage.getItem('im-theme') || 'system';
    applyTheme(saved);
    updateButtons(saved);
    document.querySelectorAll('.im-theme-btn').forEach(function(btn) {
        btn.addEventListener('click', function() {
            var t = this.getAttribute('data-imtheme');
            localStorage.setItem('im-theme', t);
            applyTheme(t);
            updateButtons(t);
        });
    });
})();
