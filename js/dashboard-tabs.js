/**
 * ImpactMojo Unified Dashboard Tabs
 * Version: 2.0.0
 * Date: March 16, 2026
 *
 * Renders a shared top-level tab bar across all dashboard pages:
 *   - My Dashboard    (always visible, requires login)
 *   - Org Dashboard   (visible if subscription_tier === 'organization' OR admin)
 *   - Admin Dashboard (visible if role === 'admin' — includes live analytics)
 *
 * USAGE:
 *   1. Add <div id="dashboardTabs"></div> where you want the bar
 *   2. Include this script after auth.js
 *   3. Call DashboardTabs.init('current-page-id') from your page
 *      where page-id is one of: 'account', 'organization', 'admin'
 */

(function () {
  'use strict';

  var TABS = [
    { id: 'account',      label: 'My Dashboard',     href: '/account.html',       icon: '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>', access: 'all' },
    { id: 'organization', label: 'Org Dashboard',     href: '/org-dashboard.html', icon: '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>', access: 'org' },
    { id: 'admin',        label: 'Admin Dashboard',   href: '/admin/',             icon: '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/><circle cx="12" cy="12" r="3"/></svg>', access: 'admin' }
  ];

  // CSS injected once
  var CSS = '\
.dashboard-tabs{max-width:1400px;margin:0 auto;padding:0.75rem 2rem 0;display:flex;gap:0;border-bottom:2px solid var(--border-color,#E2E8F0);}\
.dashboard-tab{display:inline-flex;align-items:center;gap:6px;padding:0.65rem 1.25rem;font-size:0.85rem;font-weight:500;color:var(--text-muted,#94A3B8);text-decoration:none;border-bottom:2px solid transparent;margin-bottom:-2px;transition:all 0.2s ease;white-space:nowrap;font-family:inherit;background:none;border-top:none;border-left:none;border-right:none;cursor:pointer;}\
.dashboard-tab:hover{color:var(--text-primary,#0F172A);}\
.dashboard-tab.active{color:var(--accent-color,#0EA5E9);border-bottom-color:var(--accent-color,#0EA5E9);font-weight:600;}\
.dashboard-tab svg{flex-shrink:0;opacity:0.7;}\
.dashboard-tab.active svg{opacity:1;}\
@media(max-width:640px){.dashboard-tabs{padding:0.5rem 1rem 0;overflow-x:auto;-webkit-overflow-scrolling:touch;}.dashboard-tab{padding:0.5rem 0.75rem;font-size:0.78rem;}}\
';

  var DashboardTabs = {
    _rendered: false,

    /**
     * Initialize the dashboard tabs.
     * @param {string} currentPage - one of 'account', 'organization', 'admin'
     * @param {Object} [profileOverride] - optional profile object to use instead of ImpactMojoAuth.profile
     */
    init: function (currentPage, profileOverride) {
      if (this._rendered) return;

      var container = document.getElementById('dashboardTabs');
      if (!container) return;

      // Inject CSS once
      if (!this._cssInjected) {
        var style = document.createElement('style');
        style.textContent = CSS;
        document.head.appendChild(style);
        this._cssInjected = true;
      }

      // Determine user's access level — prefer passed-in profile over global
      var profile = profileOverride || (typeof ImpactMojoAuth !== 'undefined' && ImpactMojoAuth.profile) || null;
      var tier = (profile && profile.subscription_tier) || 'explorer';
      var role = (profile && profile.role) || 'user';
      var isOrg = (tier === 'organization');
      var isAdmin = (role === 'admin');

      // Build tab bar
      var nav = document.createElement('nav');
      nav.className = 'dashboard-tabs';
      nav.setAttribute('aria-label', 'Dashboard navigation');

      for (var i = 0; i < TABS.length; i++) {
        var tab = TABS[i];

        // Access check
        if (tab.access === 'org' && !isOrg && !isAdmin) continue;
        if (tab.access === 'admin' && !isAdmin) continue;

        var a = document.createElement('a');
        a.className = 'dashboard-tab' + (tab.id === currentPage ? ' active' : '');
        a.href = tab.href;
        a.innerHTML = tab.icon + ' ' + tab.label;
        a.setAttribute('data-tab-id', tab.id);

        if (tab.id === currentPage) {
          a.setAttribute('aria-current', 'page');
        }

        nav.appendChild(a);
      }

      container.appendChild(nav);
      this._rendered = true;
    },

    /**
     * Re-render tabs (e.g. after profile is fetched and role/tier changes).
     * @param {string} currentPage
     * @param {Object} [profileOverride]
     */
    refresh: function (currentPage, profileOverride) {
      this._rendered = false;
      var container = document.getElementById('dashboardTabs');
      if (container) container.innerHTML = '';
      this.init(currentPage, profileOverride);
    }
  };

  window.DashboardTabs = DashboardTabs;
})();
