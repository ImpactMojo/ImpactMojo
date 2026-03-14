/**
 * ImpactMojo Translation Widget
 * Uses Google Translate (free, no API key) with custom UI
 * Supports: English, Hindi, Tamil, Bengali, Marathi
 *
 * Replaces the previous Sarvam.ai integration.
 * The Google Translate widget is loaded invisibly and controlled
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
            '/* Hide Google Translate widget elements */',
            '.goog-te-banner-frame, .skiptranslate, #google_translate_element { display: none !important; }',
            'body { top: 0 !important; }',
            '/* Fix Google Translate font overrides */',
            '.goog-text-highlight { background: none !important; box-shadow: none !important; }',
            '@media (max-width: 768px) { .imx-lang-label { display: none; } .imx-lang-btn { padding: 0.4rem; } .imx-lang-dropdown { right: -1rem; } }'
        ].join('\n');
        document.head.appendChild(css);
    }

    // ===== GOOGLE TRANSLATE ENGINE =====

    function loadGoogleTranslate() {
        // Create hidden container for Google Translate widget
        var gtDiv = document.createElement('div');
        gtDiv.id = 'google_translate_element';
        gtDiv.style.display = 'none';
        document.body.appendChild(gtDiv);

        // Define the callback Google Translate expects
        window.googleTranslateElementInit = function() {
            new google.translate.TranslateElement({
                pageLanguage: 'en',
                includedLanguages: 'en,hi,ta,bn,mr',
                autoDisplay: false
            }, 'google_translate_element');

            // If user had a language selected, apply it after widget loads
            if (currentLang !== 'en') {
                setTimeout(function() { triggerGoogleTranslate(LANGUAGES[currentLang].gtCode); }, 1000);
            }
        };

        // Load Google Translate script
        var script = document.createElement('script');
        script.src = 'https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
        script.async = true;
        document.body.appendChild(script);
    }

    function triggerGoogleTranslate(langCode) {
        // Google Translate uses a cookie to track language selection
        // Set the cookie and reload the translate frame
        var gtCombo = document.querySelector('.goog-te-combo');
        if (gtCombo) {
            gtCombo.value = langCode;
            gtCombo.dispatchEvent(new Event('change'));
            return;
        }

        // Fallback: set the cookie directly
        document.cookie = 'googtrans=/en/' + langCode + '; path=/; domain=' + window.location.hostname;
        document.cookie = 'googtrans=/en/' + langCode + '; path=/';

        // Retry after a delay (widget may still be loading)
        setTimeout(function() {
            var combo = document.querySelector('.goog-te-combo');
            if (combo) {
                combo.value = langCode;
                combo.dispatchEvent(new Event('change'));
            }
        }, 500);
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

        if (langKey === 'en') {
            // Restore to English
            triggerGoogleTranslate('en');
            // Also clear the cookie
            document.cookie = 'googtrans=; path=/; expires=Thu, 01 Jan 1970 00:00:00 UTC';
            document.cookie = 'googtrans=; path=/; domain=' + window.location.hostname + '; expires=Thu, 01 Jan 1970 00:00:00 UTC';
        } else {
            triggerGoogleTranslate(LANGUAGES[langKey].gtCode);
        }
    }

    // ===== INIT =====
    function init() {
        injectStyles();

        // Insert language selector into the nav
        var selector = createSelector();
        var navButtons = document.querySelector('.nav-buttons');
        if (navButtons) {
            navButtons.insertBefore(selector, navButtons.firstChild);
        } else {
            // Fallback: insert into nav-container before mobile menu button
            var navContainer = document.querySelector('.nav-container');
            var hamburger = document.querySelector('.mobile-menu-toggle');
            if (navContainer && hamburger) {
                navContainer.insertBefore(selector, hamburger);
            } else if (navContainer) {
                navContainer.appendChild(selector);
            }
        }

        // Load Google Translate
        loadGoogleTranslate();
    }

    if (document.readyState === 'complete' || document.readyState === 'interactive') {
        setTimeout(init, 0);
    } else {
        document.addEventListener('DOMContentLoaded', init);
    }
})();
