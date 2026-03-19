-- ============================================================
-- Populate org dashboard with initial data
-- Date: 2026-03-19
--
-- Problem: Org dashboard displayed nothing because:
--   1. No organizations existed for 2 of 3 admin accounts
--   2. Admins were not added as organization_members
--   3. No learning paths were pre-populated
--   4. challenge_requests table was missing
--
-- This migration:
--   1. Creates organizations for all admin accounts
--   2. Adds admins as members of their respective orgs
--   3. Creates default learning paths for the primary org
--   4. Creates the challenge_requests table with RLS
-- ============================================================

-- ============================================================
-- 1. Ensure all admins have organizations
-- ============================================================
INSERT INTO public.organizations (name, admin_id, billing_email)
VALUES
    ('ImpactMojo', '3749adb1-5c23-4bd1-82ab-1793946c0236', 'varna.sr@gmail.com'),
    ('Pinpoint Ventures', 'b6ca90f0-01c5-4b8a-920b-13ddb817ee7f', 'varna@pinpointventures.in'),
    ('ImpactMojo Team', 'c19810af-0ec0-485b-8010-5853756fd587', 'vsoni.1986@gmail.com')
ON CONFLICT DO NOTHING;

-- ============================================================
-- 2. Add admins as members of their respective orgs
-- ============================================================
INSERT INTO public.organization_members (org_id, user_id, role, status, joined_at)
SELECT o.id, o.admin_id, 'admin', 'active', NOW()
FROM public.organizations o
WHERE o.admin_id IN (
    '3749adb1-5c23-4bd1-82ab-1793946c0236',
    'b6ca90f0-01c5-4b8a-920b-13ddb817ee7f',
    'c19810af-0ec0-485b-8010-5853756fd587'
)
ON CONFLICT (org_id, user_id) DO NOTHING;

-- ============================================================
-- 3. Create default learning paths for the primary org
-- ============================================================
INSERT INTO public.learning_paths (org_id, title, description, course_ids, created_by)
SELECT
    o.id,
    v.title,
    v.description,
    v.course_ids,
    o.admin_id
FROM public.organizations o,
(VALUES
    ('MEL Foundations', 'Core monitoring, evaluation & learning competencies', ARRAY['mel', 'dataviz', 'devai']),
    ('Development Practitioner', 'Economics, policy and program management', ARRAY['devecon', 'poa', 'law', 'gandhi']),
    ('Communication & Impact', 'Media, data storytelling and social-emotional skills', ARRAY['media', 'sel', 'dataviz'])
) AS v(title, description, course_ids)
WHERE o.admin_id = '3749adb1-5c23-4bd1-82ab-1793946c0236'
AND NOT EXISTS (
    SELECT 1 FROM public.learning_paths lp WHERE lp.org_id = o.id
);

-- ============================================================
-- 4. Create challenge_requests table
-- ============================================================
CREATE TABLE IF NOT EXISTS public.challenge_requests (
    id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
    org_id uuid REFERENCES public.organizations(id) ON DELETE CASCADE,
    requested_by uuid REFERENCES auth.users(id),
    topic text NOT NULL,
    track text,
    description text,
    participants integer,
    difficulty text DEFAULT 'Intermediate',
    status text DEFAULT 'pending',
    created_at timestamptz DEFAULT now(),
    updated_at timestamptz DEFAULT now()
);

ALTER TABLE public.challenge_requests ENABLE ROW LEVEL SECURITY;

-- Org admins can manage challenge requests
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_policies WHERE policyname = 'challenge_req_org_admin' AND tablename = 'challenge_requests') THEN
        CREATE POLICY challenge_req_org_admin ON public.challenge_requests
            FOR ALL
            USING (EXISTS (
                SELECT 1 FROM public.organizations
                WHERE id = challenge_requests.org_id AND admin_id = auth.uid()
            ));
    END IF;
END $$;
