-- ============================================================
-- Add taranga.sriraman@gmail.com as organization-tier user
-- Date: 2026-03-26
--
-- Grants organization (highest) subscription tier without
-- admin role. User was created via Auth Admin API.
-- ============================================================

UPDATE public.profiles
SET
    subscription_tier   = 'organization',
    subscription_status = 'active',
    role                = 'learner',
    updated_at          = NOW()
WHERE email = 'taranga.sriraman@gmail.com';
