/**
 * ImpactMojo Translation Widget
 * Uses Google Translate (free, no API key) with custom UI
 * Supports: English, Hindi, Tamil, Bengali, Marathi
 *
 * The Google Translate widget is loaded off-screen and controlled
 * programmatically through our own language selector UI.
 */
(function() {
    'use strict';

    var LANGUAGES = {
        en: { label: 'English', native: 'English', gtCode: 'en' },
        hi: { label: 'Hindi',   native: '\u0939\u093F\u0928\u094D\u0926\u0940', gtCode: 'hi' },
        ta: { label: 'Tamil',   native: '\u0BA4\u0BAE\u0BBF\u0BB4\u0BCD', gtCode: 'ta' },
        bn: { label: 'Bengali', native: '\u09AC\u09BE\u0982\u09B2\u09BE', gtCode: 'bn' },
        mr: { label: 'Marathi', native: '\u092E\u0930\u093E\u0920\u0940', gtCode: 'mr' }
    };

    var currentLang = localStorage.getItem('impactmojo_lang') || 'en';
    var gtReady = false;
    var pendingLang = null;

    // ===== COOKIE CLEANUP =====
    function clearGoogTransCookies() {
        document.cookie = 'googtrans=; path=/; expires=Thu, 01 Jan 1970 00:00:00 UTC';
        document.cookie = 'googtrans=; path=/; domain=' + location.hostname + '; expires=Thu, 01 Jan 1970 00:00:00 UTC';
        document.cookie = 'googtrans=; path=/; domain=.' + location.hostname + '; expires=Thu, 01 Jan 1970 00:00:00 UTC';
    }

    // ALWAYS clear googtrans cookies on every page load FIRST.
    // We will re-set them only if the user explicitly chose a non-English
    // language via our UI (stored in localStorage). This prevents Google
    // Translate from auto-translating based on stale cookies or browser
    // language detection.
    clearGoogTransCookies();

    // Prevent Chrome's built-in page translation from interfering.
    // This stops the "Translate this page?" prompt and auto-translation
    // based on browser language settings.
    if (!document.querySelector('meta[name="google"][content="notranslate"]')) {
        var noTransMeta = document.createElement('meta');
        noTransMeta.name = 'google';
        noTransMeta.content = 'notranslate';
        document.head.appendChild(noTransMeta);
    }

    // ===== UI: Language Selector =====
    function createSelector() {
        var container = document.createElement('div');
        container.className = 'imx-lang-selector';
        container.setAttribute('role', 'navigation');
        container.setAttribute('aria-label', 'Language selection');

        var btn = document.createElement('button');
        btn.className = 'imx-lang-btn';
        btn.setAttribute('aria-expanded', 'false');
        btn.setAttribute('aria-haspopup', 'true');
        btn.setAttribute('type', 'button');
        btn.innerHTML = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg> <span class="imx-lang-label">' + (LANGUAGES[currentLang] ? LANGUAGES[currentLang].native : 'English') + '</span>';

        var dropdown = document.createElement('div');
        dropdown.className = 'imx-lang-dropdown';
        dropdown.style.display = 'none';

        Object.keys(LANGUAGES).forEach(function(key) {
            var lang = LANGUAGES[key];
            var item = document.createElement('button');
            item.className = 'imx-lang-option' + (key === currentLang ? ' active' : '');
            item.setAttribute('data-lang', key);
            item.setAttribute('type', 'button');
            item.innerHTML = '<span class="imx-lang-native">' + lang.native + '</span> <span class="imx-lang-english">' + lang.label + '</span>';
            item.addEventListener('click', function(e) {
                e.stopPropagation();
                selectLanguage(key);
                dropdown.style.display = 'none';
                btn.setAttribute('aria-expanded', 'false');
            });
            dropdown.appendChild(item);
        });

        btn.addEventListener('click', function(e) {
            e.stopPropagation();
            var open = dropdown.style.display === 'none';
            dropdown.style.display = open ? 'block' : 'none';
            btn.setAttribute('aria-expanded', open ? 'true' : 'false');
        });

        document.addEventListener('click', function() {
            dropdown.style.display = 'none';
            btn.setAttribute('aria-expanded', 'false');
        });

        container.appendChild(btn);
        container.appendChild(dropdown);
        return container;
    }

    function injectStyles() {
        var css = document.createElement('style');
        css.textContent = [
            '/* Language Selector */',
            '.imx-lang-selector { position: relative; display: inline-flex; margin-left: 0.5rem; }',
            '.imx-lang-btn { display: inline-flex; align-items: center; gap: 0.4rem; padding: 0.4rem 0.75rem; border: 1px solid var(--border-color, #334155); border-radius: 8px; background: var(--card-bg, #1E293B); color: var(--text-primary, #F1F5F9); font-size: 0.8rem; font-weight: 500; cursor: pointer; transition: all 0.2s; white-space: nowrap; }',
            '.imx-lang-btn:hover { border-color: #0EA5E9; color: #0EA5E9; }',
            '.imx-lang-btn svg { flex-shrink: 0; }',
            '.imx-lang-dropdown { position: absolute; top: calc(100% + 4px); right: 0; background: var(--card-bg, #1E293B); border: 1px solid var(--border-color, #334155); border-radius: 10px; box-shadow: 0 8px 24px rgba(0,0,0,0.2); z-index: 1000; min-width: 180px; padding: 0.35rem; overflow: hidden; }',
            '.imx-lang-option { display: flex; align-items: center; gap: 0.5rem; width: 100%; padding: 0.5rem 0.75rem; border: none; background: none; color: var(--text-primary, #F1F5F9); font-size: 0.85rem; cursor: pointer; border-radius: 6px; transition: background 0.15s; text-align: left; }',
            '.imx-lang-option:hover { background: var(--hover-bg, #334155); }',
            '.imx-lang-option.active { background: rgba(14, 165, 233, 0.15); color: #0EA5E9; font-weight: 600; }',
            '.imx-lang-native { font-weight: 500; }',
            '.imx-lang-english { color: var(--text-muted, #64748B); font-size: 0.75rem; }',
            '',
            '/* Hide Google Translate UI — off-screen, NOT display:none */',
            '#google_translate_element { position: absolute; top: -9999px; left: -9999px; width: 1px; height: 1px; overflow: hidden; }',
            '.goog-te-banner-frame { display: none !important; }',
            '#goog-gt-tt, .goog-te-balloon-frame { display: none !important; }',
            '.goog-text-highlight { background: none !important; box-shadow: none !important; }',
            '',
            '/* Google Translate top bar fix */',
            'body { top: 0 !important; position: static !important; }',
            '.skiptranslate { display: none !important; height: 0 !important; overflow: hidden !important; }',
            '.skiptranslate iframe { display: none !important; }',
            '',
            '/* ============================================ */',
            '/* Indic script font adjustments               */',
            '/* Hindi, Tamil, Bengali, Marathi need smaller  */',
            '/* fonts and more line-height to avoid cutoff   */',
            '/* ============================================ */',
            '',
            '/* When translated to any Indic language */',
            '.imx-translated-indic { font-size: 0.92em; line-height: 1.8; }',
            '.imx-translated-indic h1 { font-size: 1.8rem !important; line-height: 1.4 !important; }',
            '.imx-translated-indic h2 { font-size: 1.5rem !important; line-height: 1.4 !important; }',
            '.imx-translated-indic h3 { font-size: 1.2rem !important; line-height: 1.4 !important; }',
            '.imx-translated-indic p, .imx-translated-indic li, .imx-translated-indic span, .imx-translated-indic a { line-height: 1.8 !important; }',
            '',
            '/* Card titles and descriptions */',
            '.imx-translated-indic .imx-card-title { font-size: 1.05rem !important; line-height: 1.5 !important; }',
            '.imx-translated-indic .imx-card-desc { font-size: 0.82rem !important; line-height: 1.7 !important; }',
            '.imx-translated-indic .imx-card-subtitle { font-size: 0.8rem !important; line-height: 1.5 !important; }',
            '.imx-translated-indic .imx-resource-title { font-size: 0.95rem !important; line-height: 1.5 !important; }',
            '.imx-translated-indic .imx-resource-desc { font-size: 0.8rem !important; line-height: 1.7 !important; }',
            '',
            '/* Section headings */',
            '.imx-translated-indic .section-title { font-size: 1.6rem !important; line-height: 1.4 !important; }',
            '.imx-translated-indic .section-subtitle { font-size: 0.95rem !important; line-height: 1.6 !important; }',
            '',
            '/* Hero text */',
            '.imx-translated-indic .hero-title { font-size: 2rem !important; line-height: 1.3 !important; }',
            '.imx-translated-indic .hero-subtitle { font-size: 1rem !important; line-height: 1.6 !important; }',
            '.imx-translated-indic .page-hero h1 { font-size: 1.8rem !important; line-height: 1.3 !important; }',
            '.imx-translated-indic .page-hero p { font-size: 0.95rem !important; line-height: 1.6 !important; }',
            '',
            '/* Navigation */',
            '.imx-translated-indic .nav-links a { font-size: 0.82rem !important; }',
            '.imx-translated-indic .dropdown-menu a { font-size: 0.82rem !important; }',
            '',
            '/* Buttons and tags */',
            '.imx-translated-indic .imx-tag-green, .imx-translated-indic .imx-tag-blue { font-size: 0.7rem !important; }',
            '.imx-translated-indic .imx-card-modules { font-size: 0.7rem !important; }',
            '',
            '/* Footer */',
            '.imx-translated-indic .footer-section a { font-size: 0.8rem !important; line-height: 1.7 !important; }',
            '',
            '/* Course pages */',
            '.imx-translated-indic .module-title { font-size: 1.1rem !important; line-height: 1.5 !important; }',
            '.imx-translated-indic .lesson-content p { font-size: 0.9rem !important; line-height: 1.8 !important; }',
            '',
            '/* Tamil-specific: Tamil script is wider */',
            '.imx-translated-ta h1 { font-size: 1.6rem !important; }',
            '.imx-translated-ta h2 { font-size: 1.3rem !important; }',
            '.imx-translated-ta .imx-card-title { font-size: 0.95rem !important; }',
            '',
            '@media (max-width: 768px) {',
            '  .imx-lang-label { display: none; }',
            '  .imx-lang-btn { padding: 0.4rem; }',
            '  .imx-lang-dropdown { right: -1rem; }',
            '  .imx-translated-indic h1 { font-size: 1.4rem !important; }',
            '  .imx-translated-indic h2 { font-size: 1.2rem !important; }',
            '  .imx-translated-indic h3 { font-size: 1rem !important; }',
            '}'
        ].join('\n');
        document.head.appendChild(css);
    }

    // ===== INDIC FONT CLASS MANAGEMENT =====

    function applyIndicClass(langKey) {
        var body = document.body;
        // Remove all translated classes
        body.classList.remove('imx-translated-indic', 'imx-translated-hi', 'imx-translated-ta', 'imx-translated-bn', 'imx-translated-mr');

        if (langKey && langKey !== 'en') {
            body.classList.add('imx-translated-indic');
            body.classList.add('imx-translated-' + langKey);
        }
    }

    // ===== GOOGLE TRANSLATE ENGINE =====

    function loadGoogleTranslate() {
        // Create the container Google Translate needs — positioned off-screen
        var gtDiv = document.createElement('div');
        gtDiv.id = 'google_translate_element';
        document.body.appendChild(gtDiv);

        // Define the callback Google Translate expects
        window.googleTranslateElementInit = function() {
            new google.translate.TranslateElement({
                pageLanguage: 'en',
                includedLanguages: 'hi,ta,bn,mr',
                autoDisplay: false,
                layout: google.translate.TranslateElement.InlineLayout.SIMPLE
            }, 'google_translate_element');

            // Poll for the combo box to appear (GT creates it async)
            waitForCombo(0);
        };

        // Load Google Translate script
        var script = document.createElement('script');
        script.src = 'https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
        script.async = true;
        script.onerror = function() {
            console.warn('Google Translate failed to load');
        };
        document.body.appendChild(script);
    }

    function waitForCombo(attempts) {
        var combo = document.querySelector('.goog-te-combo');
        if (combo) {
            gtReady = true;
            // If user had a non-English language saved, apply it now
            if (pendingLang) {
                doTranslate(pendingLang);
                pendingLang = null;
            } else if (currentLang !== 'en') {
                doTranslate(LANGUAGES[currentLang].gtCode);
            } else {
                // Language is English — force-revert any auto-translation
                // that Google Translate may have applied despite our cookie
                // cleanup (e.g., based on browser language detection).
                doTranslate('en');
            }
        } else if (attempts < 30) {
            // Poll up to ~9 seconds
            setTimeout(function() { waitForCombo(attempts + 1); }, 300);
        }
    }

    function doTranslate(langCode) {
        var combo = document.querySelector('.goog-te-combo');
        if (!combo) return;

        if (langCode === 'en') {
            // Revert to English
            combo.value = '';
            combo.dispatchEvent(new Event('change'));

            // Clear cookies to fully reset
            setTimeout(function() {
                document.cookie = 'googtrans=; path=/; expires=Thu, 01 Jan 1970 00:00:00 UTC';
                document.cookie = 'googtrans=; path=/; domain=' + location.hostname + '; expires=Thu, 01 Jan 1970 00:00:00 UTC';
                document.cookie = 'googtrans=; path=/; domain=.' + location.hostname + '; expires=Thu, 01 Jan 1970 00:00:00 UTC';

                // Try clicking "Show original" in banner frame
                try {
                    var frame = document.querySelector('.goog-te-banner-frame');
                    if (frame && frame.contentDocument) {
                        var btn = frame.contentDocument.querySelector('.goog-close-link');
                        if (btn) btn.click();
                    }
                } catch(e) {}
            }, 200);

            applyIndicClass('en');
        } else {
            // Set cookie first for reliability
            document.cookie = 'googtrans=/en/' + langCode + '; path=/';
            document.cookie = 'googtrans=/en/' + langCode + '; path=/; domain=' + location.hostname;

            combo.value = langCode;
            combo.dispatchEvent(new Event('change'));

            // Google Translate sometimes misses deeply nested elements
            // Re-trigger after a short delay to catch stragglers
            setTimeout(function() {
                combo.value = langCode;
                combo.dispatchEvent(new Event('change'));
            }, 1500);

            // Apply Indic font adjustments
            applyIndicClass(langCode);
        }
    }

    function selectLanguage(langKey) {
        if (langKey === currentLang) return;

        currentLang = langKey;
        localStorage.setItem('impactmojo_lang', langKey);

        // Update active state in dropdown
        document.querySelectorAll('.imx-lang-option').forEach(function(opt) {
            opt.classList.toggle('active', opt.getAttribute('data-lang') === langKey);
        });

        // Update button label
        var label = document.querySelector('.imx-lang-label');
        if (label) label.textContent = LANGUAGES[langKey].native;

        var gtLangCode = LANGUAGES[langKey].gtCode;

        if (gtReady) {
            doTranslate(gtLangCode);
        } else {
            pendingLang = gtLangCode;
            applyIndicClass(langKey);
        }
    }

    // ===== INIT =====
    function init() {
        injectStyles();

        // If returning with a non-English language, apply Indic font classes immediately
        if (currentLang !== 'en') {
            applyIndicClass(currentLang);
        }

        // Insert language selector into the nav
        var selector = createSelector();
        var navButtons = document.querySelector('.nav-buttons');
        if (navButtons) {
            navButtons.insertBefore(selector, navButtons.firstChild);
        } else {
            var navContainer = document.querySelector('.nav-container');
            var hamburger = document.querySelector('.mobile-menu-toggle');
            if (navContainer && hamburger) {
                navContainer.insertBefore(selector, hamburger);
            } else if (navContainer) {
                navContainer.appendChild(selector);
            } else {
                // Flagship course pages use .mobile-header instead of .nav-container
                var mobileHeader = document.querySelector('.mobile-header');
                if (mobileHeader) {
                    // Insert before the theme toggle (last child) in the mobile header
                    var themeToggle = mobileHeader.querySelector('#theme-toggle-mobile');
                    if (themeToggle) {
                        mobileHeader.insertBefore(selector, themeToggle);
                    } else {
                        mobileHeader.appendChild(selector);
                    }
                }
            }
        }

        // Load Google Translate engine
        loadGoogleTranslate();
    }

    if (document.readyState === 'complete' || document.readyState === 'interactive') {
        setTimeout(init, 0);
    } else {
        document.addEventListener('DOMContentLoaded', init);
    }
})();
