/**
 * ImpactMojo Authentication System
 * Powered by Supabase
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
// AUTH STATE MANAGEMENT
// =====================================================
const ImpactMojoAuth = {
    user: null,
    profile: null,
    isInitialized: false,

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
            }

            // Listen for auth changes
            supabase.auth.onAuthStateChange(async (event, session) => {
                console.log('Auth state changed:', event);
                
                if (event === 'SIGNED_IN' && session?.user) {
                    this.user = session.user;
                    await this.fetchProfile();
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

// Export for use in other scripts
window.ImpactMojoAuth = ImpactMojoAuth;
window.supabase = supabase;
