-- Cohorts, cohort members and cohort discussions.
--
-- 20260320_cohorts_and_notifications.sql defined these tables, but they were
-- never created in production, so the Training tab of the organisation
-- dashboard saved cohorts only in the admin's own browser and the daily
-- cohort-deadline reminder found nothing to send. This version differs from
-- the 2026-03-20 file in three ways:
--   * access rules that look at another table use security definer helpers,
--     because a cohorts rule that reads cohort_members and a cohort_members
--     rule that reads cohorts recurse (error 42P17);
--   * anonymous callers get nothing;
--   * a member can change only their own progress and status, not which
--     cohort the row belongs to.

CREATE TABLE IF NOT EXISTS public.cohorts (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    org_id UUID NOT NULL REFERENCES public.organizations(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    description TEXT,
    package_id TEXT,
    course_ids TEXT[] DEFAULT '{}',
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    status TEXT DEFAULT 'upcoming',
    created_by UUID REFERENCES public.profiles(id),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS public.cohort_members (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    cohort_id UUID NOT NULL REFERENCES public.cohorts(id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    status TEXT DEFAULT 'enrolled',
    progress_percentage INTEGER DEFAULT 0,
    enrolled_at TIMESTAMPTZ DEFAULT NOW(),
    completed_at TIMESTAMPTZ,
    UNIQUE (cohort_id, user_id)
);

CREATE TABLE IF NOT EXISTS public.cohort_discussions (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    cohort_id UUID NOT NULL REFERENCES public.cohorts(id) ON DELETE CASCADE,
    user_id UUID REFERENCES public.profiles(id) ON DELETE SET NULL,
    parent_id UUID REFERENCES public.cohort_discussions(id) ON DELETE CASCADE,
    content TEXT NOT NULL,
    is_pinned BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE public.cohorts ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.cohort_members ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.cohort_discussions ENABLE ROW LEVEL SECURITY;

-- Helpers. They bypass row security on purpose, so the policies below do not
-- recurse, and they answer only about the caller.
CREATE OR REPLACE FUNCTION public.is_cohort_org_admin(p_cohort_id UUID)
RETURNS BOOLEAN
LANGUAGE sql STABLE SECURITY DEFINER
SET search_path TO 'public', 'pg_temp'
AS $$
  SELECT EXISTS (
    SELECT 1 FROM public.cohorts c
    JOIN public.organizations o ON o.id = c.org_id
    WHERE c.id = p_cohort_id AND o.admin_id = (SELECT auth.uid())
  );
$$;

CREATE OR REPLACE FUNCTION public.is_cohort_member(p_cohort_id UUID)
RETURNS BOOLEAN
LANGUAGE sql STABLE SECURITY DEFINER
SET search_path TO 'public', 'pg_temp'
AS $$
  SELECT EXISTS (
    SELECT 1 FROM public.cohort_members m
    WHERE m.cohort_id = p_cohort_id AND m.user_id = (SELECT auth.uid())
  );
$$;

REVOKE ALL ON FUNCTION public.is_cohort_org_admin(UUID) FROM PUBLIC, anon;
REVOKE ALL ON FUNCTION public.is_cohort_member(UUID) FROM PUBLIC, anon;
GRANT EXECUTE ON FUNCTION public.is_cohort_org_admin(UUID) TO authenticated, service_role;
GRANT EXECUTE ON FUNCTION public.is_cohort_member(UUID) TO authenticated, service_role;

-- cohorts
CREATE POLICY cohorts_org_admin_all ON public.cohorts
    FOR ALL TO authenticated
    USING (EXISTS (SELECT 1 FROM public.organizations o
                   WHERE o.id = org_id AND o.admin_id = (SELECT auth.uid())))
    WITH CHECK (EXISTS (SELECT 1 FROM public.organizations o
                        WHERE o.id = org_id AND o.admin_id = (SELECT auth.uid())));
CREATE POLICY cohorts_member_select ON public.cohorts
    FOR SELECT TO authenticated
    USING (public.is_cohort_member(id));

-- cohort_members
CREATE POLICY cohort_members_org_admin_all ON public.cohort_members
    FOR ALL TO authenticated
    USING (public.is_cohort_org_admin(cohort_id))
    WITH CHECK (public.is_cohort_org_admin(cohort_id));
CREATE POLICY cohort_members_own_select ON public.cohort_members
    FOR SELECT TO authenticated
    USING (user_id = (SELECT auth.uid()));
CREATE POLICY cohort_members_own_update ON public.cohort_members
    FOR UPDATE TO authenticated
    USING (user_id = (SELECT auth.uid()))
    WITH CHECK (user_id = (SELECT auth.uid()));

-- cohort_discussions
CREATE POLICY cohort_discussions_select ON public.cohort_discussions
    FOR SELECT TO authenticated
    USING (public.is_cohort_member(cohort_id) OR public.is_cohort_org_admin(cohort_id));
CREATE POLICY cohort_discussions_insert ON public.cohort_discussions
    FOR INSERT TO authenticated
    WITH CHECK (user_id = (SELECT auth.uid())
                AND (public.is_cohort_member(cohort_id) OR public.is_cohort_org_admin(cohort_id)));
CREATE POLICY cohort_discussions_own_update ON public.cohort_discussions
    FOR UPDATE TO authenticated
    USING (user_id = (SELECT auth.uid()))
    WITH CHECK (user_id = (SELECT auth.uid()));
CREATE POLICY cohort_discussions_delete ON public.cohort_discussions
    FOR DELETE TO authenticated
    USING (user_id = (SELECT auth.uid()) OR public.is_cohort_org_admin(cohort_id));

-- Table privileges: nothing for anon; authenticated callers are limited by the
-- policies above. A member may update only progress and status on their row.
REVOKE ALL ON public.cohorts, public.cohort_members, public.cohort_discussions FROM PUBLIC, anon, authenticated;
GRANT ALL ON public.cohorts, public.cohort_members, public.cohort_discussions TO service_role;
GRANT SELECT, INSERT, DELETE ON public.cohorts, public.cohort_members, public.cohort_discussions TO authenticated;
GRANT UPDATE ON public.cohorts TO authenticated;
GRANT UPDATE (status, progress_percentage, completed_at) ON public.cohort_members TO authenticated;
GRANT UPDATE (content, is_pinned, updated_at) ON public.cohort_discussions TO authenticated;

CREATE INDEX IF NOT EXISTS idx_cohorts_org_id ON public.cohorts(org_id);
CREATE INDEX IF NOT EXISTS idx_cohorts_status ON public.cohorts(status);
CREATE INDEX IF NOT EXISTS idx_cohorts_created_by ON public.cohorts(created_by);
CREATE INDEX IF NOT EXISTS idx_cohort_members_cohort_id ON public.cohort_members(cohort_id);
CREATE INDEX IF NOT EXISTS idx_cohort_members_user_id ON public.cohort_members(user_id);
CREATE INDEX IF NOT EXISTS idx_cohort_discussions_cohort_id ON public.cohort_discussions(cohort_id);
CREATE INDEX IF NOT EXISTS idx_cohort_discussions_user_id ON public.cohort_discussions(user_id);
CREATE INDEX IF NOT EXISTS idx_cohort_discussions_parent_id ON public.cohort_discussions(parent_id);

CREATE OR REPLACE FUNCTION public.update_cohort_status()
RETURNS TRIGGER
LANGUAGE plpgsql
SET search_path TO 'public', 'pg_temp'
AS $$
BEGIN
    IF NEW.start_date <= CURRENT_DATE AND NEW.end_date >= CURRENT_DATE THEN
        NEW.status = 'active';
    ELSIF NEW.end_date < CURRENT_DATE THEN
        NEW.status = 'completed';
    ELSE
        NEW.status = 'upcoming';
    END IF;
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS cohort_status_update ON public.cohorts;
CREATE TRIGGER cohort_status_update
    BEFORE INSERT OR UPDATE OF start_date, end_date ON public.cohorts
    FOR EACH ROW EXECUTE FUNCTION public.update_cohort_status();
