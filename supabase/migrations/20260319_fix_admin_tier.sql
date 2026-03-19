-- ============================================================
-- Fix admin tier for platform admins and prevent future resets
-- Date: 2026-03-19
--
-- Problem: Profiles were created with default 'explorer' tier and
-- 'learner' role. The handle_new_user() trigger always inserts
-- defaults, and there is no protection against tier downgrades.
--
-- This migration:
--   1. Sets all admin accounts to organization tier + admin role
--   2. Creates a trigger to prevent accidental tier downgrades for admins
--   3. Makes handle_new_user() safe against duplicate inserts
-- ============================================================

-- ============================================================
-- 1. Fix admin profiles
-- ============================================================
UPDATE public.profiles
SET
    subscription_tier   = 'organization',
    subscription_status = 'active',
    role                = 'admin',
    updated_at          = NOW()
WHERE email IN (
    'varna.sr@gmail.com',
    'varna@pinpointventures.in',
    'vandana@pinpointventures.in'
);

-- Also match by display name in case email differs
UPDATE public.profiles
SET
    subscription_tier   = 'organization',
    subscription_status = 'active',
    role                = 'admin',
    updated_at          = NOW()
WHERE (full_name ILIKE '%vandana soni%' OR display_name ILIKE '%vandana soni%')
  AND role != 'admin';

-- ============================================================
-- 2. Protect admin tier from accidental downgrades
--
-- This trigger prevents:
--   - Changing an admin's role away from 'admin'
--   - Downgrading an admin's subscription_tier
--   - Setting subscription_status to inactive for admins
--
-- Admins can still be modified via the Supabase dashboard
-- (service_role key bypasses RLS and triggers can be
-- temporarily disabled if needed).
-- ============================================================
CREATE OR REPLACE FUNCTION public.protect_admin_tier()
RETURNS TRIGGER AS $$
BEGIN
    -- Only protect rows where the OLD role is 'admin'
    IF OLD.role = 'admin' THEN
        -- Prevent role change away from admin
        IF NEW.role IS DISTINCT FROM 'admin' THEN
            RAISE WARNING 'Cannot change admin role via client. Use Supabase dashboard.';
            NEW.role := OLD.role;
        END IF;

        -- Prevent tier downgrade
        IF NEW.subscription_tier IS DISTINCT FROM OLD.subscription_tier THEN
            -- Allow upgrades but not downgrades
            IF NEW.subscription_tier IN ('explorer', 'practitioner') AND OLD.subscription_tier IN ('professional', 'organization') THEN
                RAISE WARNING 'Cannot downgrade admin tier via client. Use Supabase dashboard.';
                NEW.subscription_tier := OLD.subscription_tier;
            END IF;
        END IF;

        -- Prevent status deactivation
        IF NEW.subscription_status IS DISTINCT FROM OLD.subscription_status
           AND NEW.subscription_status NOT IN ('active', 'trialing') THEN
            RAISE WARNING 'Cannot deactivate admin subscription via client. Use Supabase dashboard.';
            NEW.subscription_status := OLD.subscription_status;
        END IF;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Drop the trigger if it already exists, then create
DROP TRIGGER IF EXISTS protect_admin_tier_trigger ON public.profiles;
CREATE TRIGGER protect_admin_tier_trigger
    BEFORE UPDATE ON public.profiles
    FOR EACH ROW EXECUTE FUNCTION public.protect_admin_tier();

-- ============================================================
-- 3. Make handle_new_user() idempotent (ON CONFLICT DO NOTHING)
--
-- If a profile already exists for the user ID, skip insertion.
-- This prevents the trigger from overwriting existing tier/role
-- if auth.users is somehow re-processed.
-- ============================================================
CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO public.profiles (id, email, full_name, display_name, referral_code)
    VALUES (
        NEW.id,
        NEW.email,
        COALESCE(NEW.raw_user_meta_data->>'full_name', ''),
        COALESCE(NEW.raw_user_meta_data->>'display_name', SPLIT_PART(NEW.email, '@', 1)),
        UPPER(SUBSTRING(MD5(NEW.id::TEXT) FROM 1 FOR 8))
    )
    ON CONFLICT (id) DO NOTHING;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;
