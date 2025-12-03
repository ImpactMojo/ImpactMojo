/**
 * ImpactMojo Section Router
 * Version 1.1.0 - December 3, 2025
 * 
 * Enables clean URLs like /courses, /labs, /about that work with Netlify
 * Maps URLs to sections (scroll), modals (open), or feature panels (speed dial)
 * 
 * FIXED in v1.1.0:
 * - Added polling to wait for IMX object to be ready
 * - Better handling of feature URLs (/bookmarks, /notes, etc.)
 * - External page redirects handled by _redirects file
 */

(function() {
    'use strict';

    // Route configuration
    // type: 'section' = scroll to element, 'modal' = open modal, 'function' = call function
    const routeConfig = {
        // Direct sections (scroll to these)
        '/': { type: 'section', target: 'home' },
        '/home': { type: 'section', target: 'home' },
        '/tracks': { type: 'section', target: 'tracks' },
        '/roadmap': { type: 'section', target: 'roadmap' },
        '/testimonials': { type: 'section', target: 'wall-of-love' },
        '/wall-of-love': { type: 'section', target: 'wall-of-love' },
        '/reviews': { type: 'section', target: 'wall-of-love' },
        '/whats-new': { type: 'section', target: 'whats-new' },
        '/new': { type: 'section', target: 'whats-new' },
        '/support': { type: 'section', target: 'support-us' },
        '/support-us': { type: 'section', target: 'support-us' },
        '/donate': { type: 'section', target: 'support-us' },
        '/about': { type: 'section', target: 'about' },
        '/contact': { type: 'section', target: 'contact' },
        
        // Modal routes (open these modals)
        '/courses': { type: 'modal', target: 'coursesModal' },
        '/labs': { type: 'modal', target: 'labsModal' },
        '/games': { type: 'modal', target: 'gamesModal' },
        '/premium': { type: 'modal', target: 'premiumModal' },
        '/coaching': { type: 'modal', target: 'coachingModal' },
        '/tools': { type: 'modal', target: 'labsModal' }, // Alias
        
        // Speed dial / feature routes (call functions)
        '/bookmarks': { type: 'function', target: 'openBookmarks' },
        '/notes': { type: 'function', target: 'openNotes' },
        '/compare': { type: 'function', target: 'openCompare' },
        '/reading-list': { type: 'function', target: 'openReadingList' },
        '/analytics': { type: 'function', target: 'openAnalytics' },
        '/streak': { type: 'function', target: 'openStreak' },
        '/pomodoro': { type: 'function', target: 'openPomodoro' }
        
        // Note: /impactlex, /dictionary, /community are handled by _redirects (301)
    };

    // Get current path without trailing slash
    function getCurrentPath() {
        let path = window.location.pathname;
        // Remove trailing slash except for root
        if (path !== '/' && path.endsWith('/')) {
            path = path.slice(0, -1);
        }
        // Handle /index.html as root
        if (path === '/index.html') {
            path = '/';
        }
        return path.toLowerCase();
    }

    // Scroll to a section smoothly with header offset
    function scrollToSection(sectionId) {
        const section = document.getElementById(sectionId);
        if (section) {
            // Small delay to ensure page is loaded
            setTimeout(() => {
                const headerOffset = 100;
                const elementPosition = section.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
                
                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
                
                // Update URL hash without triggering scroll
                if (sectionId !== 'home') {
                    history.replaceState(null, '', '#' + sectionId);
                }
            }, 150);
            return true;
        }
        return false;
    }

    // Open a modal
    function openModalByName(modalId) {
        // Check if openModal function exists (from main site)
        if (typeof window.openModal === 'function') {
            window.openModal(modalId);
            return true;
        }
        // Fallback: try to show modal directly
        const modal = document.getElementById(modalId);
        if (modal) {
            modal.style.display = 'flex';
            document.body.style.overflow = 'hidden';
            return true;
        }
        return false;
    }

    // Wait for IMX object to be available, then execute callback
    function waitForIMX(callback, maxAttempts = 50) {
        let attempts = 0;
        
        function check() {
            attempts++;
            
            // Check if IMX and required methods exist
            if (typeof window.IMX !== 'undefined' && 
                typeof window.IMX.SpeedDial !== 'undefined') {
                console.log('Router: IMX ready after ' + attempts + ' attempts');
                callback();
                return;
            }
            
            if (attempts < maxAttempts) {
                setTimeout(check, 100); // Check every 100ms
            } else {
                console.warn('Router: IMX not available after ' + maxAttempts + ' attempts');
            }
        }
        
        check();
    }

    // Handle feature functions (speed dial items)
    function handleFeatureFunction(funcName) {
        waitForIMX(() => {
            switch(funcName) {
                case 'openBookmarks':
                    // Open speed dial, then click bookmarks tab
                    IMX.SpeedDial.open();
                    setTimeout(() => {
                        // Try multiple selectors
                        const bookmarksBtn = document.querySelector('.imx-sd-bookmarks') || 
                                            document.querySelector('[data-panel="bookmarks"]');
                        if (bookmarksBtn) {
                            bookmarksBtn.click();
                        } else if (typeof IMX.openBookmarksModal === 'function') {
                            IMX.openBookmarksModal();
                        }
                    }, 300);
                    break;
                    
                case 'openNotes':
                    IMX.SpeedDial.open();
                    setTimeout(() => {
                        const notesBtn = document.querySelector('.imx-sd-notes') ||
                                        document.querySelector('[data-panel="notes"]');
                        if (notesBtn) {
                            notesBtn.click();
                        } else if (typeof IMX.openNotesModal === 'function') {
                            IMX.openNotesModal();
                        }
                    }, 300);
                    break;
                    
                case 'openCompare':
                    if (typeof IMX.openCompareModal === 'function') {
                        IMX.openCompareModal();
                    } else {
                        IMX.SpeedDial.open();
                        setTimeout(() => {
                            const compareBtn = document.querySelector('.imx-sd-compare');
                            if (compareBtn) compareBtn.click();
                        }, 300);
                    }
                    break;
                    
                case 'openReadingList':
                    if (typeof IMX.openReadingListsModal === 'function') {
                        IMX.openReadingListsModal();
                    } else {
                        IMX.SpeedDial.open();
                        setTimeout(() => {
                            const readingBtn = document.querySelector('.imx-sd-reading');
                            if (readingBtn) readingBtn.click();
                        }, 300);
                    }
                    break;
                    
                case 'openAnalytics':
                    if (typeof IMX.openAnalyticsModal === 'function') {
                        IMX.openAnalyticsModal();
                    } else {
                        IMX.SpeedDial.open();
                        setTimeout(() => {
                            const analyticsBtn = document.querySelector('.imx-sd-analytics');
                            if (analyticsBtn) analyticsBtn.click();
                        }, 300);
                    }
                    break;
                    
                case 'openStreak':
                    if (typeof IMX.openStreakModal === 'function') {
                        IMX.openStreakModal();
                    } else {
                        IMX.SpeedDial.open();
                        setTimeout(() => {
                            const streakBtn = document.querySelector('.imx-sd-streak');
                            if (streakBtn) streakBtn.click();
                        }, 300);
                    }
                    break;
                    
                case 'openPomodoro':
                    if (typeof IMX.Pomodoro !== 'undefined' && typeof IMX.Pomodoro.openModal === 'function') {
                        IMX.Pomodoro.openModal();
                    } else {
                        IMX.SpeedDial.open();
                        setTimeout(() => {
                            const pomodoroBtn = document.querySelector('.imx-sd-pomodoro') ||
                                               document.getElementById('imxPomodoroFab');
                            if (pomodoroBtn) pomodoroBtn.click();
                        }, 300);
                    }
                    break;
                    
                default:
                    console.log('Router: Unknown function:', funcName);
            }
        });
    }

    // Main route handler
    function handleRoute() {
        const path = getCurrentPath();
        const route = routeConfig[path];

        console.log('Router: Handling path:', path);

        if (!route) {
            // No matching route, check for hash fragment
            if (window.location.hash) {
                const hashTarget = window.location.hash.substring(1);
                scrollToSection(hashTarget);
            }
            return;
        }

        console.log('Router: Route found:', route);

        switch(route.type) {
            case 'section':
                scrollToSection(route.target);
                break;
            case 'modal':
                // Wait for DOM and openModal to be available
                setTimeout(() => {
                    openModalByName(route.target);
                }, 300);
                break;
            case 'function':
                // handleFeatureFunction has its own waiting logic
                handleFeatureFunction(route.target);
                break;
        }
    }

    // Convert internal links to clean URLs
    function updateInternalLinks() {
        // Find all anchor links
        document.querySelectorAll('a[href^="#"]').forEach(link => {
            const hash = link.getAttribute('href').substring(1);
            
            // Find matching route for this hash
            for (const [path, config] of Object.entries(routeConfig)) {
                if (config.target === hash && path !== '/') {
                    // Add click handler to use clean URL
                    link.addEventListener('click', (e) => {
                        e.preventDefault();
                        history.pushState(null, '', path);
                        handleRoute();
                    });
                    break;
                }
            }
        });
    }

    // Handle browser back/forward
    function handlePopState() {
        window.addEventListener('popstate', () => {
            handleRoute();
        });
    }

    // Initialize router
    function init() {
        console.log('ImpactMojo Router v1.1.0 initializing...');
        
        // Handle initial route
        handleRoute();
        
        // Set up link handling
        updateInternalLinks();
        
        // Handle browser navigation
        handlePopState();
        
        console.log('ImpactMojo Router initialized');
    }

    // Run when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    // Expose router API globally
    window.ImpactMojoRouter = {
        scrollToSection: scrollToSection,
        openModal: openModalByName,
        handleRoute: handleRoute,
        routes: routeConfig,
        version: '1.1.0'
    };

})();
