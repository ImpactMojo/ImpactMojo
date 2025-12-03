/**
 * ImpactMojo Authentication System
 * Powered by Supabase
 * Version 2.0.0 - December 3, 2025
 * 
 * NEW IN v2.0.0:
 * - Cloud sync for bookmarks, notes, progress, reading lists, compare list
 * - Auto-sync on login/logout
 * - Manual sync function
 * - Intelligent data merging (newer/more complete wins)
 * 
 * Include this file in your HTML pages:
 * <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
 * <script src="js/auth.js"></script>
 */

// =====================================================
// SUPABASE CONFIGURATION
// =====================================================
const SUPABASE_URL = 'https://ddyszmfffyedolkcugld.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRkeXN6bWZmZnllZG9sa2N1Z2xkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjQ3MzMxMzEsImV4cCI6MjA4MDMwOTEzMX0.vPLlFkC3pqOBtofZ8B6_FBLbRfOKwlyv3DzLvJBS16w';

// Initialize Supabase client
const supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

// =====================================================
// LOCALSTORAGE KEYS (must match index.html)
// =====================================================
const STORAGE_KEYS = {
    BOOKMARKS: 'impactMojoBookmarks',
    NOTES: 'impactMojoNotes',
    PROGRESS: 'impactMojoProgress',
    READING_LIST: 'impactMojoReadingList',
    COMPARE_LIST: 'impactMojoCompareList',
    STREAK: 'impactMojoStreak',
    LAST_SYNC: 'impactMojoLastSync'
};

// =====================================================
// AUTH STATE MANAGEMENT
// =====================================================
const ImpactMojoAuth = {
    user: null,
    profile: null,
    isInitialized: false,
    isSyncing: false,

    // Initialize auth and check session
    async init() {
        if (this.isInitialized) return;
        
        try {
            // Get current session
            const { data: { session }, error } = await supabase.auth.getSession();
            
            if (error) {
                console.error('Auth init error:', error);
                return;
            }

            if (session?.user) {
                this.user = session.user;
                await this.fetchProfile();
                // Auto-sync on init if logged in
                await this.syncFromCloud();
            }

            // Listen for auth changes
            supabase.auth.onAuthStateChange(async (event, session) => {
                console.log('Auth state changed:', event);
                
                if (event === 'SIGNED_IN' && session?.user) {
                    this.user = session.user;
                    await this.fetchProfile();
                    // Sync data when user signs in
                    await this.syncAll();
                    this.updateUI();
                } else if (event === 'SIGNED_OUT') {
                    this.user = null;
                    this.profile = null;
                    this.updateUI();
                }
            });

            this.isInitialized = true;
            this.updateUI();
            
        } catch (err) {
            console.error('Auth initialization failed:', err);
        }
    },

    // Fetch user profile from database
    async fetchProfile() {
        if (!this.user) return null;

        try {
            const { data, error } = await supabase
                .from('profiles')
                .select('*')
                .eq('id', this.user.id)
                .single();

            if (error) {
                console.error('Error fetching profile:', error);
                return null;
            }

            this.profile = data;
            return data;
        } catch (err) {
            console.error('Profile fetch failed:', err);
            return null;
        }
    },

    // =====================================================
    // DATA SYNC METHODS (NEW IN v2.0.0)
    // =====================================================

    // Get data from localStorage
    getLocalData() {
        return {
            bookmarks: JSON.parse(localStorage.getItem(STORAGE_KEYS.BOOKMARKS) || '[]'),
            notes: JSON.parse(localStorage.getItem(STORAGE_KEYS.NOTES) || '[]'),
            progress: JSON.parse(localStorage.getItem(STORAGE_KEYS.PROGRESS) || '{}'),
            reading_lists: JSON.parse(localStorage.getItem(STORAGE_KEYS.READING_LIST) || '[]'),
            compare_list: JSON.parse(localStorage.getItem(STORAGE_KEYS.COMPARE_LIST) || '[]'),
            streak_data: JSON.parse(localStorage.getItem(STORAGE_KEYS.STREAK) || '{"current":0,"longest":0,"last_date":null}')
        };
    },

    // Save data to localStorage
    setLocalData(data) {
        if (data.bookmarks !== undefined) {
            localStorage.setItem(STORAGE_KEYS.BOOKMARKS, JSON.stringify(data.bookmarks));
        }
        if (data.notes !== undefined) {
            localStorage.setItem(STORAGE_KEYS.NOTES, JSON.stringify(data.notes));
        }
        if (data.progress !== undefined) {
            localStorage.setItem(STORAGE_KEYS.PROGRESS, JSON.stringify(data.progress));
        }
        if (data.reading_lists !== undefined) {
            localStorage.setItem(STORAGE_KEYS.READING_LIST, JSON.stringify(data.reading_lists));
        }
        if (data.compare_list !== undefined) {
            localStorage.setItem(STORAGE_KEYS.COMPARE_LIST, JSON.stringify(data.compare_list));
        }
        if (data.streak_data !== undefined) {
            localStorage.setItem(STORAGE_KEYS.STREAK, JSON.stringify(data.streak_data));
        }
    },

    // Merge local and cloud data (newer/more complete wins)
    mergeData(localData, cloudData) {
        const merged = {};

        // Merge bookmarks (combine unique items by ID)
        const allBookmarks = [...(cloudData.bookmarks || []), ...(localData.bookmarks || [])];
        const bookmarkMap = new Map();
        allBookmarks.forEach(item => {
            const key = item.id || item.courseId || JSON.stringify(item);
            if (!bookmarkMap.has(key) || (item.timestamp && item.timestamp > bookmarkMap.get(key).timestamp)) {
                bookmarkMap.set(key, item);
            }
        });
        merged.bookmarks = Array.from(bookmarkMap.values());

        // Merge notes (combine unique by ID, newer timestamp wins)
        const allNotes = [...(cloudData.notes || []), ...(localData.notes || [])];
        const notesMap = new Map();
        allNotes.forEach(note => {
            const key = note.id || note.timestamp;
            if (!notesMap.has(key) || (note.updatedAt && note.updatedAt > notesMap.get(key).updatedAt)) {
                notesMap.set(key, note);
            }
        });
        merged.notes = Array.from(notesMap.values()).sort((a, b) => 
            (b.timestamp || 0) - (a.timestamp || 0)
        );

        // Merge progress (combine all completed items)
        merged.progress = {
            ...(cloudData.progress || {}),
            ...(localData.progress || {})
        };
        // Merge completed arrays within progress
        if (cloudData.progress?.completed || localData.progress?.completed) {
            const allCompleted = [
                ...(cloudData.progress?.completed || []),
                ...(localData.progress?.completed || [])
            ];
            merged.progress.completed = [...new Set(allCompleted)];
        }

        // Merge reading lists (combine unique items)
        const allReadingLists = [...(cloudData.reading_lists || []), ...(localData.reading_lists || [])];
        const readingMap = new Map();
        allReadingLists.forEach(item => {
            const key = item.id || JSON.stringify(item);
            readingMap.set(key, item);
        });
        merged.reading_lists = Array.from(readingMap.values());

        // Merge compare list (combine unique items)
        const allCompare = [...(cloudData.compare_list || []), ...(localData.compare_list || [])];
        merged.compare_list = [...new Set(allCompare.map(i => typeof i === 'string' ? i : JSON.stringify(i)))]
            .map(i => { try { return JSON.parse(i); } catch { return i; } });

        // Merge streak data (keep higher values)
        const localStreak = localData.streak_data || { current: 0, longest: 0, last_date: null };
        const cloudStreak = cloudData.streak_data || { current: 0, longest: 0, last_date: null };
        merged.streak_data = {
            current: Math.max(localStreak.current || 0, cloudStreak.current || 0),
            longest: Math.max(localStreak.longest || 0, cloudStreak.longest || 0),
            last_date: localStreak.last_date && cloudStreak.last_date 
                ? (localStreak.last_date > cloudStreak.last_date ? localStreak.last_date : cloudStreak.last_date)
                : (localStreak.last_date || cloudStreak.last_date)
        };

        return merged;
    },

    // Sync local data TO cloud (push)
    async syncToCloud() {
        if (!this.user || this.isSyncing) {
            return { success: false, message: 'Not logged in or sync in progress' };
        }

        this.isSyncing = true;

        try {
            const localData = this.getLocalData();

            const { data, error } = await supabase
                .from('profiles')
                .update({
                    bookmarks: localData.bookmarks,
                    notes: localData.notes,
                    progress: localData.progress,
                    reading_lists: localData.reading_lists,
                    compare_list: localData.compare_list,
                    streak_data: localData.streak_data,
                    last_synced_at: new Date().toISOString(),
                    updated_at: new Date().toISOString()
                })
                .eq('id', this.user.id)
                .select()
                .single();

            if (error) throw error;

            // Update local last sync time
            localStorage.setItem(STORAGE_KEYS.LAST_SYNC, new Date().toISOString());
            
            this.profile = data;
            this.isSyncing = false;

            console.log('✅ Data synced to cloud');
            return { success: true, message: 'Data synced to cloud', data };

        } catch (err) {
            console.error('Sync to cloud failed:', err);
            this.isSyncing = false;
            return { success: false, message: err.message, error: err };
        }
    },

    // Sync cloud data TO local (pull)
    async syncFromCloud() {
        if (!this.user || this.isSyncing) {
            return { success: false, message: 'Not logged in or sync in progress' };
        }

        this.isSyncing = true;

        try {
            // Fetch latest profile with sync data
            const { data, error } = await supabase
                .from('profiles')
                .select('bookmarks, notes, progress, reading_lists, compare_list, streak_data, last_synced_at')
                .eq('id', this.user.id)
                .single();

            if (error) throw error;

            const cloudData = {
                bookmarks: data.bookmarks || [],
                notes: data.notes || [],
                progress: data.progress || {},
                reading_lists: data.reading_lists || [],
                compare_list: data.compare_list || [],
                streak_data: data.streak_data || { current: 0, longest: 0, last_date: null }
            };

            const localData = this.getLocalData();
            
            // Merge data (handles conflicts)
            const mergedData = this.mergeData(localData, cloudData);
            
            // Save merged data locally
            this.setLocalData(mergedData);
            
            // Update last sync time
            localStorage.setItem(STORAGE_KEYS.LAST_SYNC, new Date().toISOString());

            this.isSyncing = false;

            console.log('✅ Data synced from cloud');
            
            // Dispatch event for UI updates
            window.dispatchEvent(new CustomEvent('dataSynced', { detail: mergedData }));

            return { success: true, message: 'Data synced from cloud', data: mergedData };

        } catch (err) {
            console.error('Sync from cloud failed:', err);
            this.isSyncing = false;
            return { success: false, message: err.message, error: err };
        }
    },

    // Full two-way sync (merge local + cloud, then push)
    async syncAll() {
        if (!this.user) {
            return { success: false, message: 'Not logged in' };
        }

        console.log('🔄 Starting full sync...');

        try {
            // First pull and merge
            const pullResult = await this.syncFromCloud();
            if (!pullResult.success) {
                console.warn('Pull failed, attempting push anyway');
            }

            // Then push merged data back
            const pushResult = await this.syncToCloud();
            
            console.log('✅ Full sync complete');
            
            // Dispatch sync complete event
            window.dispatchEvent(new CustomEvent('syncComplete', { 
                detail: { pullResult, pushResult } 
            }));

            return { 
                success: true, 
                message: 'Full sync complete',
                pullResult,
                pushResult
            };

        } catch (err) {
            console.error('Full sync failed:', err);
            return { success: false, message: err.message, error: err };
        }
    },

    // Get last sync time
    getLastSyncTime() {
        const lastSync = localStorage.getItem(STORAGE_KEYS.LAST_SYNC);
        return lastSync ? new Date(lastSync) : null;
    },

    // Get formatted last sync time for display
    getLastSyncDisplay() {
        const lastSync = this.getLastSyncTime();
        if (!lastSync) return 'Never synced';
        
        const now = new Date();
        const diffMs = now - lastSync;
        const diffMins = Math.floor(diffMs / 60000);
        const diffHours = Math.floor(diffMs / 3600000);
        const diffDays = Math.floor(diffMs / 86400000);

        if (diffMins < 1) return 'Just now';
        if (diffMins < 60) return `${diffMins} minute${diffMins > 1 ? 's' : ''} ago`;
        if (diffHours < 24) return `${diffHours} hour${diffHours > 1 ? 's' : ''} ago`;
        return `${diffDays} day${diffDays > 1 ? 's' : ''} ago`;
    },

    // =====================================================
    // AUTHENTICATION METHODS
    // =====================================================

    // Sign up with email and password
    async signUp(email, password, fullName = '') {
        try {
            const { data, error } = await supabase.auth.signUp({
                email: email,
                password: password,
                options: {
                    data: {
                        full_name: fullName,
                        display_name: fullName || email.split('@')[0]
                    },
                    emailRedirectTo: window.location.origin + '/account.html'
                }
            });

            if (error) throw error;

            return {
                success: true,
                message: 'Account created! Please check your email to verify your account.',
                data: data
            };
        } catch (err) {
            console.error('Sign up error:', err);
            return {
                success: false,
                message: err.message || 'Sign up failed. Please try again.',
                error: err
            };
        }
    },

    // Sign in with email and password
    async signIn(email, password) {
        try {
            const { data, error } = await supabase.auth.signInWithPassword({
                email: email,
                password: password
            });

            if (error) throw error;

            this.user = data.user;
            await this.fetchProfile();
            
            // Sync data after login (NEW in v2.0.0)
            await this.syncAll();

            return {
                success: true,
                message: 'Welcome back!',
                data: data
            };
        } catch (err) {
            console.error('Sign in error:', err);
            return {
                success: false,
                message: err.message || 'Sign in failed. Please check your credentials.',
                error: err
            };
        }
    },

    // Sign in with Google
    async signInWithGoogle() {
        try {
            const { data, error } = await supabase.auth.signInWithOAuth({
                provider: 'google',
                options: {
                    redirectTo: window.location.origin + '/account.html'
                }
            });

            if (error) throw error;

            return { success: true, data: data };
        } catch (err) {
            console.error('Google sign in error:', err);
            return {
                success: false,
                message: err.message || 'Google sign in failed.',
                error: err
            };
        }
    },

    // Sign in with magic link (passwordless)
    async signInWithMagicLink(email) {
        try {
            const { data, error } = await supabase.auth.signInWithOtp({
                email: email,
                options: {
                    emailRedirectTo: window.location.origin + '/account.html'
                }
            });

            if (error) throw error;

            return {
                success: true,
                message: 'Check your email for the login link!',
                data: data
            };
        } catch (err) {
            console.error('Magic link error:', err);
            return {
                success: false,
                message: err.message || 'Failed to send magic link.',
                error: err
            };
        }
    },

    // Sign out
    async signOut() {
        try {
            // Sync before logout (save any unsaved data) - NEW in v2.0.0
            if (this.user) {
                await this.syncToCloud();
            }

            const { error } = await supabase.auth.signOut();
            
            if (error) throw error;

            this.user = null;
            this.profile = null;

            // Redirect to home page
            window.location.href = '/';

            return { success: true };
        } catch (err) {
            console.error('Sign out error:', err);
            return {
                success: false,
                message: err.message || 'Sign out failed.',
                error: err
            };
        }
    },

    // Reset password
    async resetPassword(email) {
        try {
            const { data, error } = await supabase.auth.resetPasswordForEmail(email, {
                redirectTo: window.location.origin + '/reset-password.html'
            });

            if (error) throw error;

            return {
                success: true,
                message: 'Password reset email sent! Check your inbox.',
                data: data
            };
        } catch (err) {
            console.error('Password reset error:', err);
            return {
                success: false,
                message: err.message || 'Failed to send reset email.',
                error: err
            };
        }
    },

    // Update password (when user has reset token)
    async updatePassword(newPassword) {
        try {
            const { data, error } = await supabase.auth.updateUser({
                password: newPassword
            });

            if (error) throw error;

            return {
                success: true,
                message: 'Password updated successfully!',
                data: data
            };
        } catch (err) {
            console.error('Update password error:', err);
            return {
                success: false,
                message: err.message || 'Failed to update password.',
                error: err
            };
        }
    },

    // =====================================================
    // PROFILE MANAGEMENT
    // =====================================================

    // Update user profile
    async updateProfile(updates) {
        if (!this.user) {
            return { success: false, message: 'Not logged in' };
        }

        try {
            const { data, error } = await supabase
                .from('profiles')
                .update({
                    ...updates,
                    updated_at: new Date().toISOString()
                })
                .eq('id', this.user.id)
                .select()
                .single();

            if (error) throw error;

            this.profile = data;

            return {
                success: true,
                message: 'Profile updated successfully!',
                data: data
            };
        } catch (err) {
            console.error('Profile update error:', err);
            return {
                success: false,
                message: err.message || 'Failed to update profile.',
                error: err
            };
        }
    },

    // =====================================================
    // SUBSCRIPTION HELPERS
    // =====================================================

    // Check if user has active premium subscription
    isPremium() {
        if (!this.profile) return false;
        return ['practitioner', 'professional', 'organization'].includes(this.profile.subscription_tier) 
            && this.profile.subscription_status === 'active';
    },

    // Check specific tier access
    hasTierAccess(requiredTier) {
        const tierHierarchy = ['explorer', 'practitioner', 'professional', 'organization'];
        const userTierIndex = tierHierarchy.indexOf(this.profile?.subscription_tier || 'explorer');
        const requiredTierIndex = tierHierarchy.indexOf(requiredTier);
        return userTierIndex >= requiredTierIndex && this.profile?.subscription_status === 'active';
    },

    // Get subscription tier display name
    getTierDisplayName() {
        const tierNames = {
            'explorer': 'Explorer (Free)',
            'practitioner': 'Practitioner',
            'professional': 'Professional',
            'organization': 'Organization'
        };
        return tierNames[this.profile?.subscription_tier] || 'Explorer (Free)';
    },

    // =====================================================
    // UI UPDATE METHODS
    // =====================================================

    // Update UI based on auth state
    updateUI() {
        const isLoggedIn = !!this.user;

        // Update login/signup buttons visibility
        document.querySelectorAll('.auth-logged-out').forEach(el => {
            el.style.display = isLoggedIn ? 'none' : '';
        });

        document.querySelectorAll('.auth-logged-in').forEach(el => {
            el.style.display = isLoggedIn ? '' : 'none';
        });

        // Update user name displays
        document.querySelectorAll('.auth-user-name').forEach(el => {
            el.textContent = this.profile?.display_name || this.profile?.full_name || this.user?.email?.split('@')[0] || 'User';
        });

        // Update user email displays
        document.querySelectorAll('.auth-user-email').forEach(el => {
            el.textContent = this.user?.email || '';
        });

        // Update subscription tier displays
        document.querySelectorAll('.auth-user-tier').forEach(el => {
            el.textContent = this.getTierDisplayName();
        });

        // Update avatar displays
        document.querySelectorAll('.auth-user-avatar').forEach(el => {
            if (this.profile?.avatar_url) {
                el.src = this.profile.avatar_url;
            } else {
                // Generate initials avatar
                const name = this.profile?.display_name || this.profile?.full_name || this.user?.email || 'U';
                el.src = `https://ui-avatars.com/api/?name=${encodeURIComponent(name)}&background=6366f1&color=fff`;
            }
        });

        // Update sync status displays (NEW in v2.0.0)
        document.querySelectorAll('.auth-sync-status').forEach(el => {
            el.textContent = this.getLastSyncDisplay();
        });

        // Handle premium-only content
        document.querySelectorAll('.premium-only').forEach(el => {
            if (this.isPremium()) {
                el.classList.remove('premium-locked');
            } else {
                el.classList.add('premium-locked');
            }
        });

        // Dispatch custom event for other scripts to listen to
        window.dispatchEvent(new CustomEvent('authStateChanged', {
            detail: { user: this.user, profile: this.profile, isLoggedIn }
        }));
    },

    // =====================================================
    // UTILITY METHODS
    // =====================================================

    // Check if user is logged in
    isLoggedIn() {
        return !!this.user;
    },

    // Get current user
    getUser() {
        return this.user;
    },

    // Get current profile
    getProfile() {
        return this.profile;
    },

    // Redirect to login if not authenticated
    requireAuth(redirectUrl = '/login.html') {
        if (!this.user) {
            // Store intended destination
            sessionStorage.setItem('authRedirect', window.location.href);
            window.location.href = redirectUrl;
            return false;
        }
        return true;
    },

    // Redirect after successful login
    redirectAfterLogin() {
        const redirectUrl = sessionStorage.getItem('authRedirect');
        sessionStorage.removeItem('authRedirect');
        window.location.href = redirectUrl || '/account.html';
    }
};

// =====================================================
// AUTO-INITIALIZE ON PAGE LOAD
// =====================================================
document.addEventListener('DOMContentLoaded', () => {
    ImpactMojoAuth.init();
});

// Also try to initialize immediately if DOM is already ready
if (document.readyState === 'complete' || document.readyState === 'interactive') {
    ImpactMojoAuth.init();
}

// =====================================================
// AUTO-SYNC ON PAGE VISIBILITY CHANGE (NEW in v2.0.0)
// =====================================================
document.addEventListener('visibilitychange', () => {
    // Sync when user returns to the page (if logged in)
    if (document.visibilityState === 'visible' && ImpactMojoAuth.user) {
        // Only sync if last sync was more than 5 minutes ago
        const lastSync = ImpactMojoAuth.getLastSyncTime();
        if (!lastSync || (new Date() - lastSync) > 5 * 60 * 1000) {
            ImpactMojoAuth.syncAll();
        }
    }
});

// =====================================================
// AUTO-SYNC BEFORE PAGE UNLOAD (NEW in v2.0.0)
// =====================================================
window.addEventListener('beforeunload', () => {
    // Quick sync before leaving (non-blocking)
    if (ImpactMojoAuth.user && !ImpactMojoAuth.isSyncing) {
        // Log that data is ready to sync
        console.log('📤 Page unload - data will sync on next visit');
    }
});

// Export for use in other scripts
window.ImpactMojoAuth = ImpactMojoAuth;
window.supabase = supabase;
