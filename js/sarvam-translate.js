/**
 * ImpactMojo Sarvam Translation Widget
 * Translates page content using Sarvam.ai Translate API
 * Supports: Hindi, Tamil, Bengali, Marathi
 *
 * NOTE: Set your Sarvam API key in the SARVAM_API_KEY variable below,
 * or ideally proxy through a serverless function to avoid exposing the key.
 */
(function() {
    'use strict';

    // ===== CONFIGURATION =====
    var SARVAM_API_KEY = ''; // Set your key here or use proxy
    var TRANSLATE_ENDPOINT = 'https://api.sarvam.ai/translate';
    var CACHE_KEY = 'impactmojo_translations';
    var CACHE_VERSION = 1;

    var LANGUAGES = {
        en: { label: 'English', code: 'en-IN', native: 'English' },
        hi: { label: 'Hindi', code: 'hi-IN', native: '\u0939\u093F\u0928\u094D\u0926\u0940' },
        ta: { label: 'Tamil', code: 'ta-IN', native: '\u0BA4\u0BAE\u0BBF\u0BB4\u0BCD' },
        bn: { label: 'Bengali', code: 'bn-IN', native: '\u09AC\u09BE\u0982\u09B2\u09BE' },
        mr: { label: 'Marathi', code: 'mr-IN', native: '\u092E\u0930\u093E\u0920\u0940' }
    };

    var currentLang = localStorage.getItem('impactmojo_lang') || 'en';
    var translationCache = {};
    var isTranslating = false;
    var originalTexts = new Map();

    // Load cache from localStorage
    try {
        var stored = JSON.parse(localStorage.getItem(CACHE_KEY) || '{}');
        if (stored.v === CACHE_VERSION) translationCache = stored.data || {};
    } catch(e) {}

    function saveCache() {
        try {
            localStorage.setItem(CACHE_KEY, JSON.stringify({ v: CACHE_VERSION, data: translationCache }));
        } catch(e) {}
    }

    // ===== UI: Language Selector =====
    function createSelector() {
        var container = document.createElement('div');
        container.className = 'sarvam-lang-selector';
        container.setAttribute('role', 'navigation');
        container.setAttribute('aria-label', 'Language selection');

        var btn = document.createElement('button');
        btn.className = 'sarvam-lang-btn';
        btn.setAttribute('aria-expanded', 'false');
        btn.setAttribute('aria-haspopup', 'true');
        btn.innerHTML = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg> <span class="sarvam-lang-label">' + (LANGUAGES[currentLang] ? LANGUAGES[currentLang].native : 'English') + '</span>';

        var dropdown = document.createElement('div');
        dropdown.className = 'sarvam-lang-dropdown';
        dropdown.style.display = 'none';

        Object.keys(LANGUAGES).forEach(function(key) {
            var lang = LANGUAGES[key];
            var item = document.createElement('button');
            item.className = 'sarvam-lang-option' + (key === currentLang ? ' active' : '');
            item.setAttribute('data-lang', key);
            item.innerHTML = '<span class="sarvam-lang-native">' + lang.native + '</span> <span class="sarvam-lang-english">' + lang.label + '</span>';
            item.addEventListener('click', function(e) {
                e.stopPropagation();
                selectLanguage(key);
                dropdown.style.display = 'none';
                btn.setAttribute('aria-expanded', 'false');
            });
            dropdown.appendChild(item);
        });

        // Powered by badge
        var badge = document.createElement('div');
        badge.className = 'sarvam-powered';
        badge.innerHTML = 'Powered by <a href="https://www.sarvam.ai" target="_blank" rel="noopener noreferrer">Sarvam AI</a>';
        dropdown.appendChild(badge);

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
            '.sarvam-lang-selector { position: relative; display: inline-flex; margin-left: 0.5rem; }',
            '.sarvam-lang-btn { display: inline-flex; align-items: center; gap: 0.4rem; padding: 0.4rem 0.75rem; border: 1px solid var(--border-color, #E2E8F0); border-radius: 8px; background: var(--card-bg, #fff); color: var(--text-primary, #0F172A); font-size: 0.8rem; font-weight: 500; cursor: pointer; transition: all 0.2s; white-space: nowrap; }',
            '.sarvam-lang-btn:hover { border-color: #0EA5E9; color: #0EA5E9; }',
            '.sarvam-lang-btn svg { flex-shrink: 0; }',
            '.sarvam-lang-dropdown { position: absolute; top: calc(100% + 4px); right: 0; background: var(--card-bg, #fff); border: 1px solid var(--border-color, #E2E8F0); border-radius: 10px; box-shadow: 0 8px 24px rgba(0,0,0,0.12); z-index: 1000; min-width: 180px; padding: 0.35rem; overflow: hidden; }',
            '.sarvam-lang-option { display: flex; align-items: center; gap: 0.5rem; width: 100%; padding: 0.5rem 0.75rem; border: none; background: none; color: var(--text-primary, #0F172A); font-size: 0.85rem; cursor: pointer; border-radius: 6px; transition: background 0.15s; text-align: left; }',
            '.sarvam-lang-option:hover { background: var(--hover-bg, #F1F5F9); }',
            '.sarvam-lang-option.active { background: rgba(14, 165, 233, 0.1); color: #0EA5E9; font-weight: 600; }',
            '.sarvam-lang-native { font-weight: 500; }',
            '.sarvam-lang-english { color: var(--text-muted, #94A3B8); font-size: 0.75rem; }',
            '.sarvam-powered { padding: 0.5rem 0.75rem; border-top: 1px solid var(--border-color, #E2E8F0); margin-top: 0.25rem; font-size: 0.65rem; color: var(--text-muted, #94A3B8); }',
            '.sarvam-powered a { color: #0EA5E9; text-decoration: none; }',
            '.sarvam-translating { opacity: 0.6; pointer-events: none; }',
            '.sarvam-lang-btn.loading .sarvam-lang-label::after { content: "..."; }',
            '@media (max-width: 768px) { .sarvam-lang-label { display: none; } .sarvam-lang-btn { padding: 0.4rem; } .sarvam-lang-dropdown { right: -1rem; } }'
        ].join('\n');
        document.head.appendChild(css);
    }

    // ===== TRANSLATION ENGINE =====

    // Get translatable text nodes from key page sections
    function getTranslatableElements() {
        var selectors = [
            '.section-title', '.section-subtitle', '.section-sub',
            '.imx-resource-title', '.imx-resource-desc', '.imx-resource-cta',
            '.card-title', '.card-desc', '.card-description',
            '.page-title h1', '.page-title p',
            'h1', 'h2', 'h3',
            '.nav-links > li > a',
            '.dropdown-menu > li > a',
            '.hero-title', '.hero-subtitle', '.hero-desc',
            '.stat-label',
            '.btn-text'
        ];
        var elements = [];
        var seen = new Set();
        selectors.forEach(function(sel) {
            document.querySelectorAll(sel).forEach(function(el) {
                if (!seen.has(el) && el.childNodes.length > 0) {
                    // Only translate elements with direct text content (skip complex nested structures)
                    var text = getDirectText(el);
                    if (text && text.length > 1 && text.length < 500) {
                        seen.add(el);
                        elements.push(el);
                    }
                }
            });
        });
        return elements;
    }

    // Get direct text content (not deeply nested children)
    function getDirectText(el) {
        var text = '';
        for (var i = 0; i < el.childNodes.length; i++) {
            if (el.childNodes[i].nodeType === 3) { // Text node
                text += el.childNodes[i].textContent;
            }
        }
        return text.trim();
    }

    function setDirectText(el, newText) {
        for (var i = 0; i < el.childNodes.length; i++) {
            if (el.childNodes[i].nodeType === 3 && el.childNodes[i].textContent.trim()) {
                el.childNodes[i].textContent = newText;
                return;
            }
        }
    }

    // Batch translate texts via Sarvam API
    async function translateBatch(texts, targetLangCode) {
        var results = [];
        // Sarvam API translates one string at a time, so batch them
        // Group into chunks to avoid overwhelming the API
        var BATCH_SIZE = 5;
        for (var i = 0; i < texts.length; i += BATCH_SIZE) {
            var chunk = texts.slice(i, i + BATCH_SIZE);
            var promises = chunk.map(function(text) {
                var cacheKey = targetLangCode + ':' + text;
                if (translationCache[cacheKey]) {
                    return Promise.resolve(translationCache[cacheKey]);
                }
                return fetch(TRANSLATE_ENDPOINT, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'api-subscription-key': SARVAM_API_KEY
                    },
                    body: JSON.stringify({
                        input: text,
                        source_language_code: 'en-IN',
                        target_language_code: targetLangCode,
                        model: 'mayura:v1',
                        mode: 'formal'
                    })
                }).then(function(r) {
                    if (!r.ok) throw new Error('Translation failed: ' + r.status);
                    return r.json();
                }).then(function(data) {
                    var translated = data.translated_text || text;
                    translationCache[targetLangCode + ':' + text] = translated;
                    return translated;
                }).catch(function() {
                    return text; // Fallback to original on error
                });
            });
            var chunkResults = await Promise.all(promises);
            results = results.concat(chunkResults);
        }
        saveCache();
        return results;
    }

    async function selectLanguage(langKey) {
        if (langKey === currentLang || isTranslating) return;
        isTranslating = true;

        var langBtn = document.querySelector('.sarvam-lang-btn');
        if (langBtn) langBtn.classList.add('loading');

        // Update active state in dropdown
        document.querySelectorAll('.sarvam-lang-option').forEach(function(opt) {
            opt.classList.toggle('active', opt.getAttribute('data-lang') === langKey);
        });

        var elements = getTranslatableElements();

        if (langKey === 'en') {
            // Restore original English text
            elements.forEach(function(el) {
                var original = originalTexts.get(el);
                if (original) setDirectText(el, original);
            });
            document.documentElement.lang = 'en';
        } else {
            // Store originals if not already stored
            elements.forEach(function(el) {
                if (!originalTexts.has(el)) {
                    originalTexts.set(el, getDirectText(el));
                }
            });

            // Collect texts to translate
            var textsToTranslate = elements.map(function(el) {
                return originalTexts.get(el) || getDirectText(el);
            });

            if (SARVAM_API_KEY) {
                var targetCode = LANGUAGES[langKey].code;
                var translated = await translateBatch(textsToTranslate, targetCode);
                elements.forEach(function(el, idx) {
                    if (translated[idx]) setDirectText(el, translated[idx]);
                });
                document.documentElement.lang = langKey;
            } else {
                console.warn('Sarvam API key not set. Add your key to js/sarvam-translate.js or set window.SARVAM_API_KEY');
            }
        }

        currentLang = langKey;
        localStorage.setItem('impactmojo_lang', langKey);

        // Update button label
        var label = document.querySelector('.sarvam-lang-label');
        if (label) label.textContent = LANGUAGES[langKey].native;

        if (langBtn) langBtn.classList.remove('loading');
        isTranslating = false;
    }

    // ===== INIT =====
    function init() {
        // Allow setting API key via window global
        if (window.SARVAM_API_KEY) SARVAM_API_KEY = window.SARVAM_API_KEY;

        injectStyles();

        // Insert language selector into the nav
        var selector = createSelector();
        var navButtons = document.querySelector('.nav-buttons');
        if (navButtons) {
            navButtons.insertBefore(selector, navButtons.firstChild);
        } else {
            // Mobile: insert before hamburger button
            var navContainer = document.querySelector('.nav-container');
            var hamburger = document.getElementById('hamburgerBtn');
            if (navContainer && hamburger) {
                navContainer.insertBefore(selector, hamburger);
            }
        }

        // If user previously selected a non-English language, translate on load
        if (currentLang !== 'en' && SARVAM_API_KEY) {
            // Delay to let page content render first
            setTimeout(function() { selectLanguage(currentLang); }, 1500);
        }
    }

    if (document.readyState === 'complete' || document.readyState === 'interactive') {
        setTimeout(init, 0);
    } else {
        document.addEventListener('DOMContentLoaded', init);
    }
})();
