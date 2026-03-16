/**
 * ImpactMojo Premium Content Gating Module
 * Version: 1.0.0
 * Date: December 3, 2025
 * 
 * Gates content behind subscription tiers with visual indicators,
 * click interception, and upgrade prompts.
 * 
 * Tiers (in hierarchy order):
 * - explorer (free)
 * - practitioner (₹399/month)
 * - professional (₹999/month)
 * - organization (₹1,499/user/month)
 * 
 * Usage:
 * Add data-required-tier="tierName" to any element to gate it
 * Example: <div class="card" data-required-tier="practitioner">...</div>
 */

(function() {
    'use strict';

    // =========================================================================
    // CONFIGURATION
    // =========================================================================

    const CONFIG = {
        // Tier hierarchy (index = access level)
        TIERS: ['explorer', 'practitioner', 'professional', 'organization'],
        
        // Tier display names
        TIER_NAMES: {
            'explorer': 'Explorer',
            'practitioner': 'Practitioner',
            'professional': 'Professional',
            'organization': 'Organization'
        },
        
        // Tier prices (INR)
        TIER_PRICES: {
            'explorer': 'Free',
            'practitioner': '₹399/month',
            'professional': '₹999/month',
            'organization': '₹1,499/user/month'
        },
        
        // Tier colors
        TIER_COLORS: {
            'explorer': { bg: 'rgba(100, 116, 139, 0.15)', text: '#94A3B8', accent: '#64748B' },
            'practitioner': { bg: 'rgba(14, 165, 233, 0.15)', text: '#0EA5E9', accent: '#0284C7' },
            'professional': { bg: 'rgba(99, 102, 241, 0.15)', text: '#6366F1', accent: '#4F46E5' },
            'organization': { bg: 'rgba(245, 158, 11, 0.15)', text: '#F59E0B', accent: '#D97706' }
        },
        
        // Tier icons (SVG paths)
        TIER_ICONS: {
            'explorer': '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/>',
            'practitioner': '<path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>',
            'professional': '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
            'organization': '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>'
        },
        
        // Tier features for comparison
        TIER_FEATURES: {
            'explorer': [
                'All foundational courses',
                'Progress tracking',
                'Basic labs access',
                'Personal notes & bookmarks',
                'Course comparison tool'
            ],
            'practitioner': [
                'Everything in Explorer',
                'Advanced courses & deep dives',
                'Sample size calculator',
                'TOC Workbench Pro',
                'Completion certificates',
                'Discord & Telegram community'
            ],
            'professional': [
                'Everything in Practitioner',
                'Priority coaching access',
                'Power analysis tools',
                'Downloadable templates',
                'Monthly expert webinars',
                'Early access to new content'
            ],
            'organization': [
                'Everything in Professional',
                'Team dashboard & progress analytics',
                'Bulk user management',
                'Custom learning paths',
                'Dedicated account manager',
                'Branded certificates & invoice billing'
            ]
        },
        
        // Selectors for content that can be gated
        GATED_SELECTORS: [
            '.card[data-required-tier]',
            '.modal-item[data-required-tier]',
            '.lab-card[data-required-tier]',
            '.game-card[data-required-tier]',
            '.tool-card[data-required-tier]',
            '.course-card[data-required-tier]',
            '.premium-card[data-required-tier]',
            '[data-required-tier]'
        ],
        
        // Storage key for dismissed upgrade prompts
        STORAGE_KEY: 'impactmojo_premium_dismissed',
        
        // Beta mode - all premium content free
        BETA_MODE: false,
        
        // Debug mode
        DEBUG: false
    };

    // =========================================================================
    // PREMIUM MODULE
    // =========================================================================

    const Premium = {
        
        // Current user's tier (default to explorer)
        currentTier: 'explorer',
        
        // Is user authenticated
        isAuthenticated: false,
        
        // Upgrade modal element reference
        upgradeModal: null,
        
        // =====================================================================
        // INITIALIZATION
        // =====================================================================
        
        /**
         * Initialize the premium gating system
         */
        init() {
            if (CONFIG.DEBUG) console.log('[Premium] Initializing...');
            
            // Wait for auth to be ready
            this.waitForAuth(() => {
                this.loadUserTier();
                this.injectStyles();
                this.createUpgradeModal();
                this.applyGating();
                this.setupEventListeners();

                // Verify tier server-side after initial render (catches client tampering)
                this.verifyTierServerSide();

                // Re-verify every 5 minutes to catch DevTools manipulation
                setInterval(() => this.verifyTierServerSide(), 5 * 60 * 1000);

                if (CONFIG.DEBUG) console.log('[Premium] Initialized. User tier:', this.currentTier);
            });
        },
        
        /**
         * Wait for ImpactMojoAuth to be available
         */
        waitForAuth(callback, maxAttempts = 50) {
            let attempts = 0;

            const check = () => {
                attempts++;

                // Wait until ImpactMojoAuth exists AND isAuthReady is true
                // (profile is loaded at that point so we get the correct tier)
                if (typeof window.ImpactMojoAuth !== 'undefined' && window.ImpactMojoAuth.isAuthReady) {
                    callback();
                    return;
                }

                // If ImpactMojoAuth exists but not ready yet, use its promise
                if (typeof window.ImpactMojoAuth !== 'undefined' && typeof window.ImpactMojoAuth.waitForAuthReady === 'function' && attempts >= 5) {
                    window.ImpactMojoAuth.waitForAuthReady().then(callback);
                    return;
                }

                if (attempts < maxAttempts) {
                    setTimeout(check, 100);
                } else {
                    // Auth not available, proceed with defaults
                    if (CONFIG.DEBUG) console.log('[Premium] Auth not available, using defaults');
                    callback();
                }
            };

            check();
        },
        
        /**
         * Load user's subscription tier from auth
         */
        loadUserTier() {
            if (typeof window.ImpactMojoAuth !== 'undefined' && window.ImpactMojoAuth.user) {
                this.isAuthenticated = true;
                this.currentTier = window.ImpactMojoAuth.profile?.subscription_tier || 'explorer';
                
                // Tier is determined by subscription_tier field alone
            } else {
                this.isAuthenticated = false;
                this.currentTier = 'explorer';
            }
            
            // Add tier class to body for CSS targeting
            document.body.classList.remove('tier-explorer', 'tier-practitioner', 'tier-professional', 'tier-organization');
            document.body.classList.add('tier-' + this.currentTier);
            
            // Dispatch event for other modules
            window.dispatchEvent(new CustomEvent('premiumTierLoaded', { 
                detail: { tier: this.currentTier, authenticated: this.isAuthenticated }
            }));
        },
        
        // =====================================================================
        // TIER ACCESS CHECKING
        // =====================================================================
        
        /**
         * Get tier level (index in hierarchy)
         */
        getTierLevel(tier) {
            const index = CONFIG.TIERS.indexOf(tier);
            return index === -1 ? 0 : index;
        },
        
        /**
         * Check if user has access to required tier
         */
        hasAccess(requiredTier) {
            // Beta mode - all content free
            if (CONFIG.BETA_MODE) return true;
            
            const userLevel = this.getTierLevel(this.currentTier);
            const requiredLevel = this.getTierLevel(requiredTier);
            
            return userLevel >= requiredLevel;
        },
        
        /**
         * Check if user is premium (any paid tier)
         */
        isPremium() {
            return CONFIG.TIERS.indexOf(this.currentTier) > 0;
        },
        
        /**
         * Get display name for tier
         */
        getTierName(tier) {
            return CONFIG.TIER_NAMES[tier] || tier;
        },
        
        /**
         * Get tier price
         */
        getTierPrice(tier) {
            return CONFIG.TIER_PRICES[tier] || '';
        },
        
        /**
         * Get tier color
         */
        getTierColor(tier) {
            return CONFIG.TIER_COLORS[tier] || CONFIG.TIER_COLORS['explorer'];
        },
        
        // =====================================================================
        // CONTENT GATING
        // =====================================================================
        
        /**
         * Apply gating to all marked content
         */
        applyGating() {
            const gatedElements = document.querySelectorAll(CONFIG.GATED_SELECTORS.join(','));
            
            gatedElements.forEach(element => {
                const requiredTier = element.dataset.requiredTier;
                if (!requiredTier) return;
                
                const hasAccess = this.hasAccess(requiredTier);
                
                if (hasAccess) {
                    this.unlockContent(element);
                } else {
                    this.lockContent(element, requiredTier);
                }
            });
            
            if (CONFIG.DEBUG) console.log('[Premium] Applied gating to', gatedElements.length, 'elements');
        },
        
        /**
         * Lock content element
         */
        lockContent(element, requiredTier) {
            // Skip if already locked
            if (element.classList.contains('premium-locked')) return;
            
            element.classList.add('premium-locked');
            element.dataset.lockedTier = requiredTier;
            
            // Add tier badge
            this.addTierBadge(element, requiredTier);
            
            // Add lock overlay
            this.addLockOverlay(element, requiredTier);
            
            // Intercept clicks
            element.addEventListener('click', this.handleLockedClick.bind(this), true);
            
            // Disable links inside
            const links = element.querySelectorAll('a[href]');
            links.forEach(link => {
                link.dataset.originalHref = link.href;
                link.removeAttribute('href');
                link.style.cursor = 'pointer';
            });
        },
        
        /**
         * Unlock content element
         */
        unlockContent(element) {
            element.classList.remove('premium-locked');
            element.classList.add('premium-unlocked');
            delete element.dataset.lockedTier;
            
            // Remove lock overlay
            const overlay = element.querySelector('.premium-lock-overlay');
            if (overlay) overlay.remove();
            
            // Remove click interceptor
            element.removeEventListener('click', this.handleLockedClick.bind(this), true);
            
            // Restore links
            const links = element.querySelectorAll('a[data-original-href]');
            links.forEach(link => {
                link.href = link.dataset.originalHref;
                delete link.dataset.originalHref;
                link.style.cursor = '';
            });
            
            // Keep tier badge but mark as unlocked
            const badge = element.querySelector('.premium-tier-badge');
            if (badge) {
                badge.classList.add('unlocked');
            }
        },
        
        /**
         * Add tier badge to element
         */
        addTierBadge(element, tier) {
            // Skip if badge already exists
            if (element.querySelector('.premium-tier-badge')) return;
            
            const colors = this.getTierColor(tier);
            const tierName = this.getTierName(tier);
            
            const badge = document.createElement('div');
            badge.className = 'premium-tier-badge';
            badge.dataset.tier = tier;
            badge.innerHTML = `
                <svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2">
                    ${CONFIG.TIER_ICONS[tier]}
                </svg>
                <span>${tierName}</span>
            `;
            badge.style.cssText = `
                background: ${colors.bg};
                color: ${colors.text};
                border: 1px solid ${colors.text}33;
            `;
            
            // Position badge
            element.style.position = 'relative';
            element.appendChild(badge);
        },
        
        /**
         * Add lock overlay to element
         */
        addLockOverlay(element, requiredTier) {
            // Skip if overlay already exists
            if (element.querySelector('.premium-lock-overlay')) return;
            
            const tierName = this.getTierName(requiredTier);
            const tierPrice = this.getTierPrice(requiredTier);
            
            const overlay = document.createElement('div');
            overlay.className = 'premium-lock-overlay';
            overlay.innerHTML = `
                <div class="premium-lock-content">
                    <svg class="premium-lock-icon" viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/>
                        <path d="M7 11V7a5 5 0 0 1 10 0v4"/>
                    </svg>
                    <div class="premium-lock-text">
                        <strong>${tierName}</strong> required
                    </div>
                    <button class="premium-unlock-btn" data-tier="${requiredTier}">
                        Unlock ${tierPrice !== 'Free' ? 'from ' + tierPrice : ''}
                    </button>
                </div>
            `;
            
            element.appendChild(overlay);
        },
        
        /**
         * Handle click on locked content
         */
        handleLockedClick(event) {
            const element = event.currentTarget;
            const requiredTier = element.dataset.lockedTier;
            
            if (!requiredTier) return;
            
            event.preventDefault();
            event.stopPropagation();
            
            // Show upgrade modal
            this.showUpgradeModal(requiredTier);
        },
        
        // =====================================================================
        // UPGRADE MODAL
        // =====================================================================
        
        /**
         * Create the upgrade modal element
         */
        createUpgradeModal() {
            // Remove existing modal if present
            const existing = document.getElementById('premiumUpgradeModal');
            if (existing) existing.remove();
            
            const modal = document.createElement('div');
            modal.id = 'premiumUpgradeModal';
            modal.className = 'premium-upgrade-modal';
            modal.innerHTML = `
                <div class="premium-upgrade-backdrop"></div>
                <div class="premium-upgrade-content">
                    <button class="premium-upgrade-close" aria-label="Close">
                        <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2">
                            <line x1="18" y1="6" x2="6" y2="18"/>
                            <line x1="6" y1="6" x2="18" y2="18"/>
                        </svg>
                    </button>
                    
                    <div class="premium-upgrade-header">
                        <div class="premium-upgrade-icon">
                            <svg viewBox="0 0 24 24" width="48" height="48" fill="none" stroke="currentColor" stroke-width="1.5">
                                <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/>
                                <path d="M7 11V7a5 5 0 0 1 10 0v4"/>
                            </svg>
                        </div>
                        <h2 class="premium-upgrade-title">Unlock Premium Content</h2>
                        <p class="premium-upgrade-subtitle">Upgrade to access advanced tools, courses, and exclusive features</p>
                    </div>
                    
                    <div class="premium-upgrade-body">
                        <div class="premium-upgrade-required">
                            <span class="required-label">Required tier:</span>
                            <span class="required-tier"></span>
                        </div>
                        
                        <div class="premium-upgrade-current">
                            <span class="current-label">Your current tier:</span>
                            <span class="current-tier"></span>
                        </div>
                        
                        <div class="premium-upgrade-features">
                            <h3>What you'll unlock:</h3>
                            <ul class="feature-list"></ul>
                        </div>
                        
                        <div class="premium-upgrade-beta-notice" style="display: none;">
                            <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                            </svg>
                            <span><strong>Beta Bonus:</strong> All premium content is currently FREE during our beta phase!</span>
                        </div>
                    </div>
                    
                    <div class="premium-upgrade-footer">
                        <a href="premium.html" class="premium-upgrade-btn primary">
                            <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2">
                                <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
                            </svg>
                            View Plans & Pricing
                        </a>
                        <button class="premium-upgrade-btn secondary close-btn">Maybe Later</button>
                    </div>
                </div>
            `;
            
            document.body.appendChild(modal);
            this.upgradeModal = modal;
            
            // Bind close events
            modal.querySelector('.premium-upgrade-close').addEventListener('click', () => this.hideUpgradeModal());
            modal.querySelector('.premium-upgrade-backdrop').addEventListener('click', () => this.hideUpgradeModal());
            modal.querySelector('.close-btn').addEventListener('click', () => this.hideUpgradeModal());
            
            // ESC key to close
            document.addEventListener('keydown', (e) => {
                if (e.key === 'Escape' && modal.classList.contains('visible')) {
                    this.hideUpgradeModal();
                }
            });
        },
        
        /**
         * Show upgrade modal for a specific tier
         */
        showUpgradeModal(requiredTier) {
            if (!this.upgradeModal) return;
            
            const modal = this.upgradeModal;
            const requiredTierName = this.getTierName(requiredTier);
            const requiredTierPrice = this.getTierPrice(requiredTier);
            const requiredColors = this.getTierColor(requiredTier);
            
            const currentTierName = this.getTierName(this.currentTier);
            const currentColors = this.getTierColor(this.currentTier);
            
            // Update required tier display
            const requiredEl = modal.querySelector('.required-tier');
            requiredEl.innerHTML = `
                <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2">
                    ${CONFIG.TIER_ICONS[requiredTier]}
                </svg>
                ${requiredTierName}
                <span class="tier-price">${requiredTierPrice}</span>
            `;
            requiredEl.style.cssText = `background: ${requiredColors.bg}; color: ${requiredColors.text}; border-color: ${requiredColors.text}33;`;
            
            // Update current tier display
            const currentEl = modal.querySelector('.current-tier');
            currentEl.innerHTML = `
                <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2">
                    ${CONFIG.TIER_ICONS[this.currentTier]}
                </svg>
                ${currentTierName}
            `;
            currentEl.style.cssText = `background: ${currentColors.bg}; color: ${currentColors.text}; border-color: ${currentColors.text}33;`;
            
            // Update features list
            const featureList = modal.querySelector('.feature-list');
            const features = CONFIG.TIER_FEATURES[requiredTier] || [];
            featureList.innerHTML = features.map(feature => `
                <li>
                    <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2">
                        <polyline points="20 6 9 17 4 12"/>
                    </svg>
                    ${feature}
                </li>
            `).join('');
            
            // Show/hide beta notice
            const betaNotice = modal.querySelector('.premium-upgrade-beta-notice');
            betaNotice.style.display = CONFIG.BETA_MODE ? 'flex' : 'none';
            
            // Update CTA button
            const ctaBtn = modal.querySelector('.premium-upgrade-btn.primary');
            if (CONFIG.BETA_MODE) {
                ctaBtn.innerHTML = `
                    <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                    </svg>
                    Access Free During Beta
                `;
            }
            
            // Show modal
            modal.classList.add('visible');
            document.body.style.overflow = 'hidden';
            
            // Track analytics
            this.trackUpgradePrompt(requiredTier);
        },
        
        /**
         * Hide upgrade modal
         */
        hideUpgradeModal() {
            if (!this.upgradeModal) return;
            
            this.upgradeModal.classList.remove('visible');
            document.body.style.overflow = '';
        },
        
        // =====================================================================
        // UTILITY METHODS
        // =====================================================================
        
        /**
         * Gate a specific element programmatically
         */
        gateElement(element, requiredTier) {
            if (!element || !requiredTier) return;
            
            element.dataset.requiredTier = requiredTier;
            
            if (this.hasAccess(requiredTier)) {
                this.unlockContent(element);
            } else {
                this.lockContent(element, requiredTier);
            }
        },
        
        /**
         * Ungate a specific element
         */
        ungateElement(element) {
            if (!element) return;
            
            delete element.dataset.requiredTier;
            this.unlockContent(element);
            
            // Remove badge
            const badge = element.querySelector('.premium-tier-badge');
            if (badge) badge.remove();
        },
        
        /**
         * Verify tier server-side to prevent client-side tampering.
         * Re-fetches the profile from Supabase and re-applies gating
         * if the tier doesn't match what was cached locally.
         */
        async verifyTierServerSide() {
            if (!this.isAuthenticated) return;
            try {
                var cfg = window.ImpactMojoConfig || {};
                if (!cfg.SUPABASE_URL || !cfg.SUPABASE_ANON_KEY) return;
                if (!window.supabaseClient) return;

                var session = (await window.supabaseClient.auth.getSession()).data.session;
                if (!session) return;

                var res = await window.supabaseClient
                    .from('profiles')
                    .select('subscription_tier, subscription_status')
                    .eq('id', session.user.id)
                    .single();

                if (res.error || !res.data) return;

                var serverTier = res.data.subscription_tier || 'explorer';
                var serverStatus = res.data.subscription_status;

                // Only force explorer if subscription is explicitly cancelled/expired.
                // null/undefined status means the field was never set — trust the tier.
                if (serverStatus && serverStatus !== 'active' && serverStatus !== 'trialing') {
                    serverTier = 'explorer';
                }

                if (serverTier !== this.currentTier) {
                    if (CONFIG.DEBUG) console.log('[Premium] Tier mismatch — server:', serverTier, 'client:', this.currentTier);
                    this.currentTier = serverTier;
                    this.applyGating();
                }
            } catch (_) { /* silent — gating stays as-is */ }
        },

        /**
         * Refresh gating (call after tier change or page update)
         */
        refresh() {
            this.loadUserTier();
            this.applyGating();
        },
        
        /**
         * Track upgrade prompt analytics
         */
        trackUpgradePrompt(requiredTier) {
            // Dispatch event for analytics
            window.dispatchEvent(new CustomEvent('premiumUpgradePrompt', {
                detail: {
                    requiredTier: requiredTier,
                    currentTier: this.currentTier,
                    timestamp: Date.now()
                }
            }));
            
            // Track in localStorage for analytics
            try {
                const key = 'impactmojo_upgrade_prompts';
                const prompts = JSON.parse(localStorage.getItem(key) || '[]');
                prompts.push({
                    required: requiredTier,
                    current: this.currentTier,
                    time: Date.now()
                });
                // Keep last 50 prompts
                if (prompts.length > 50) prompts.shift();
                localStorage.setItem(key, JSON.stringify(prompts));
            } catch (e) {
                // Ignore storage errors
            }
        },
        
        // =====================================================================
        // EVENT LISTENERS
        // =====================================================================
        
        /**
         * Setup event listeners
         */
        setupEventListeners() {
            // Listen for auth state changes
            window.addEventListener('authStateChanged', () => {
                this.refresh();
            });
            
            // Listen for subscription updates
            window.addEventListener('subscriptionUpdated', () => {
                this.refresh();
            });
            
            // Listen for unlock button clicks
            document.addEventListener('click', (e) => {
                const unlockBtn = e.target.closest('.premium-unlock-btn');
                if (unlockBtn) {
                    e.preventDefault();
                    e.stopPropagation();
                    const tier = unlockBtn.dataset.tier;
                    this.showUpgradeModal(tier);
                }
            });
            
            // Observe DOM for dynamically added content
            this.setupMutationObserver();
        },
        
        /**
         * Setup mutation observer for dynamic content
         */
        setupMutationObserver() {
            const observer = new MutationObserver((mutations) => {
                let shouldRefresh = false;
                
                mutations.forEach((mutation) => {
                    if (mutation.type === 'childList') {
                        mutation.addedNodes.forEach((node) => {
                            if (node.nodeType === Node.ELEMENT_NODE) {
                                if (node.dataset?.requiredTier || node.querySelector('[data-required-tier]')) {
                                    shouldRefresh = true;
                                }
                            }
                        });
                    }
                });
                
                if (shouldRefresh) {
                    this.applyGating();
                }
            });
            
            observer.observe(document.body, {
                childList: true,
                subtree: true
            });
        },
        
        // =====================================================================
        // STYLES INJECTION
        // =====================================================================
        
        /**
         * Inject CSS styles for premium gating
         */
        injectStyles() {
            // Check if styles already injected
            if (document.getElementById('premium-gating-styles')) return;
            
            const styles = document.createElement('style');
            styles.id = 'premium-gating-styles';
            styles.textContent = `
                /* ========================================
                   Premium Content Gating Styles
                   ======================================== */
                
                /* Tier Badge */
                .premium-tier-badge {
                    position: absolute;
                    top: 0.5rem;
                    right: 0.5rem;
                    display: inline-flex;
                    align-items: center;
                    gap: 0.25rem;
                    padding: 0.25rem 0.5rem;
                    border-radius: 9999px;
                    font-size: 0.7rem;
                    font-weight: 600;
                    text-transform: uppercase;
                    letter-spacing: 0.025em;
                    z-index: 10;
                    pointer-events: none;
                    transition: all 0.2s ease;
                }
                
                .premium-tier-badge svg {
                    flex-shrink: 0;
                }
                
                .premium-tier-badge.unlocked {
                    opacity: 0.7;
                }
                
                /* Lock Overlay */
                .premium-lock-overlay {
                    position: absolute;
                    inset: 0;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    background: linear-gradient(
                        135deg,
                        rgba(15, 23, 42, 0.85) 0%,
                        rgba(30, 41, 59, 0.9) 100%
                    );
                    backdrop-filter: blur(4px);
                    -webkit-backdrop-filter: blur(4px);
                    border-radius: inherit;
                    z-index: 20;
                    opacity: 0;
                    visibility: hidden;
                    transition: all 0.3s ease;
                }
                
                .premium-locked .premium-lock-overlay {
                    opacity: 1;
                    visibility: visible;
                }
                
                .premium-lock-content {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    text-align: center;
                    padding: 1rem;
                    color: white;
                }
                
                .premium-lock-icon {
                    margin-bottom: 0.75rem;
                    opacity: 0.9;
                }
                
                .premium-lock-text {
                    font-size: 0.875rem;
                    margin-bottom: 0.75rem;
                    color: rgba(255, 255, 255, 0.9);
                }
                
                .premium-lock-text strong {
                    color: #60A5FA;
                }
                
                .premium-unlock-btn {
                    display: inline-flex;
                    align-items: center;
                    gap: 0.5rem;
                    padding: 0.5rem 1rem;
                    background: linear-gradient(135deg, #3B82F6 0%, #6366F1 100%);
                    color: white;
                    font-size: 0.8rem;
                    font-weight: 600;
                    border: none;
                    border-radius: 0.5rem;
                    cursor: pointer;
                    transition: all 0.2s ease;
                }
                
                .premium-unlock-btn:hover {
                    transform: translateY(-2px);
                    box-shadow: 0 4px 12px rgba(99, 102, 241, 0.4);
                }
                
                /* Locked Card Styling */
                .premium-locked {
                    position: relative;
                    cursor: pointer;
                }
                
                .premium-locked::after {
                    content: '';
                    position: absolute;
                    inset: 0;
                    border: 2px dashed rgba(148, 163, 184, 0.3);
                    border-radius: inherit;
                    pointer-events: none;
                    z-index: 5;
                }
                
                /* Unlocked styling */
                .premium-unlocked .premium-tier-badge {
                    background: rgba(34, 197, 94, 0.15) !important;
                    color: #22C55E !important;
                    border-color: rgba(34, 197, 94, 0.3) !important;
                }
                
                /* ========================================
                   Upgrade Modal Styles
                   ======================================== */
                
                .premium-upgrade-modal {
                    position: fixed;
                    inset: 0;
                    z-index: 10000;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    padding: 1rem;
                    opacity: 0;
                    visibility: hidden;
                    transition: all 0.3s ease;
                }
                
                .premium-upgrade-modal.visible {
                    opacity: 1;
                    visibility: visible;
                }
                
                .premium-upgrade-backdrop {
                    position: absolute;
                    inset: 0;
                    background: rgba(15, 23, 42, 0.8);
                    backdrop-filter: blur(8px);
                    -webkit-backdrop-filter: blur(8px);
                }
                
                .premium-upgrade-content {
                    position: relative;
                    width: 100%;
                    max-width: 480px;
                    max-height: 90vh;
                    overflow-y: auto;
                    background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
                    border: 1px solid rgba(148, 163, 184, 0.1);
                    border-radius: 1rem;
                    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
                    transform: scale(0.95) translateY(20px);
                    transition: transform 0.3s ease;
                }
                
                .premium-upgrade-modal.visible .premium-upgrade-content {
                    transform: scale(1) translateY(0);
                }
                
                .premium-upgrade-close {
                    position: absolute;
                    top: 1rem;
                    right: 1rem;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    width: 2.5rem;
                    height: 2.5rem;
                    background: rgba(148, 163, 184, 0.1);
                    border: none;
                    border-radius: 50%;
                    color: #94A3B8;
                    cursor: pointer;
                    transition: all 0.2s ease;
                    z-index: 10;
                }
                
                .premium-upgrade-close:hover {
                    background: rgba(148, 163, 184, 0.2);
                    color: white;
                }
                
                .premium-upgrade-header {
                    padding: 2rem 2rem 1.5rem;
                    text-align: center;
                    border-bottom: 1px solid rgba(148, 163, 184, 0.1);
                }
                
                .premium-upgrade-icon {
                    display: inline-flex;
                    align-items: center;
                    justify-content: center;
                    width: 80px;
                    height: 80px;
                    margin-bottom: 1rem;
                    background: linear-gradient(135deg, rgba(99, 102, 241, 0.2) 0%, rgba(14, 165, 233, 0.2) 100%);
                    border-radius: 50%;
                    color: #6366F1;
                }
                
                .premium-upgrade-title {
                    margin: 0 0 0.5rem;
                    font-size: 1.5rem;
                    font-weight: 700;
                    color: white;
                }
                
                .premium-upgrade-subtitle {
                    margin: 0;
                    font-size: 0.95rem;
                    color: #94A3B8;
                }
                
                .premium-upgrade-body {
                    padding: 1.5rem 2rem;
                }
                
                .premium-upgrade-required,
                .premium-upgrade-current {
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    margin-bottom: 0.75rem;
                    padding: 0.75rem 1rem;
                    background: rgba(148, 163, 184, 0.05);
                    border-radius: 0.5rem;
                }
                
                .required-label,
                .current-label {
                    font-size: 0.875rem;
                    color: #94A3B8;
                }
                
                .required-tier,
                .current-tier {
                    display: inline-flex;
                    align-items: center;
                    gap: 0.375rem;
                    padding: 0.375rem 0.75rem;
                    border-radius: 9999px;
                    font-size: 0.8rem;
                    font-weight: 600;
                    border: 1px solid;
                }
                
                .required-tier .tier-price {
                    margin-left: 0.25rem;
                    opacity: 0.7;
                    font-weight: 400;
                }
                
                .premium-upgrade-features {
                    margin-top: 1.5rem;
                }
                
                .premium-upgrade-features h3 {
                    margin: 0 0 1rem;
                    font-size: 0.95rem;
                    font-weight: 600;
                    color: white;
                }
                
                .feature-list {
                    list-style: none;
                    padding: 0;
                    margin: 0;
                }
                
                .feature-list li {
                    display: flex;
                    align-items: flex-start;
                    gap: 0.75rem;
                    padding: 0.5rem 0;
                    font-size: 0.9rem;
                    color: #CBD5E1;
                }
                
                .feature-list li svg {
                    flex-shrink: 0;
                    margin-top: 2px;
                    color: #22C55E;
                }
                
                .premium-upgrade-beta-notice {
                    display: flex;
                    align-items: center;
                    gap: 0.75rem;
                    margin-top: 1.5rem;
                    padding: 1rem;
                    background: linear-gradient(135deg, rgba(34, 197, 94, 0.1) 0%, rgba(16, 185, 129, 0.1) 100%);
                    border: 1px solid rgba(34, 197, 94, 0.2);
                    border-radius: 0.5rem;
                    font-size: 0.875rem;
                    color: #86EFAC;
                }
                
                .premium-upgrade-beta-notice svg {
                    flex-shrink: 0;
                    color: #22C55E;
                }
                
                .premium-upgrade-footer {
                    display: flex;
                    flex-direction: column;
                    gap: 0.75rem;
                    padding: 1.5rem 2rem;
                    border-top: 1px solid rgba(148, 163, 184, 0.1);
                }
                
                .premium-upgrade-btn {
                    display: inline-flex;
                    align-items: center;
                    justify-content: center;
                    gap: 0.5rem;
                    padding: 0.875rem 1.5rem;
                    font-size: 0.95rem;
                    font-weight: 600;
                    text-decoration: none;
                    border: none;
                    border-radius: 0.5rem;
                    cursor: pointer;
                    transition: all 0.2s ease;
                }
                
                .premium-upgrade-btn.primary {
                    background: linear-gradient(135deg, #3B82F6 0%, #6366F1 100%);
                    color: white;
                }
                
                .premium-upgrade-btn.primary:hover {
                    transform: translateY(-2px);
                    box-shadow: 0 4px 12px rgba(99, 102, 241, 0.4);
                }
                
                .premium-upgrade-btn.secondary {
                    background: rgba(148, 163, 184, 0.1);
                    color: #94A3B8;
                }
                
                .premium-upgrade-btn.secondary:hover {
                    background: rgba(148, 163, 184, 0.2);
                    color: #CBD5E1;
                }
                
                /* ========================================
                   Mobile Responsive
                   ======================================== */
                
                @media (max-width: 640px) {
                    .premium-tier-badge {
                        font-size: 0.6rem;
                        padding: 0.2rem 0.4rem;
                    }
                    
                    .premium-lock-content {
                        padding: 0.75rem;
                    }
                    
                    .premium-lock-icon {
                        width: 24px;
                        height: 24px;
                    }
                    
                    .premium-lock-text {
                        font-size: 0.75rem;
                    }
                    
                    .premium-unlock-btn {
                        font-size: 0.7rem;
                        padding: 0.4rem 0.75rem;
                    }
                    
                    .premium-upgrade-content {
                        max-width: 100%;
                        margin: 0.5rem;
                        border-radius: 0.75rem;
                    }
                    
                    .premium-upgrade-header,
                    .premium-upgrade-body,
                    .premium-upgrade-footer {
                        padding-left: 1.25rem;
                        padding-right: 1.25rem;
                    }
                    
                    .premium-upgrade-icon {
                        width: 60px;
                        height: 60px;
                    }
                    
                    .premium-upgrade-icon svg {
                        width: 36px;
                        height: 36px;
                    }
                    
                    .premium-upgrade-title {
                        font-size: 1.25rem;
                    }
                }
                
                /* ========================================
                   Dark Mode Adjustments (already dark)
                   ======================================== */
                
                /* Ensure visibility on light mode pages if any */
                @media (prefers-color-scheme: light) {
                    .premium-lock-overlay {
                        background: linear-gradient(
                            135deg,
                            rgba(30, 41, 59, 0.9) 0%,
                            rgba(15, 23, 42, 0.95) 100%
                        );
                    }
                }
            `;
            
            document.head.appendChild(styles);
        }
    };

    // =========================================================================
    // PUBLIC API
    // =========================================================================

    // Expose to window
    window.IMXPremium = Premium;
    
    // Also add to IMX namespace if available
    if (typeof window.IMX !== 'undefined') {
        window.IMX.Premium = Premium;
    } else {
        // Wait for IMX to be available
        const waitForIMX = () => {
            if (typeof window.IMX !== 'undefined') {
                window.IMX.Premium = Premium;
            } else {
                setTimeout(waitForIMX, 100);
            }
        };
        waitForIMX();
    }

    // =========================================================================
    // AUTO-INITIALIZATION
    // =========================================================================

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => Premium.init());
    } else {
        Premium.init();
    }

})();
