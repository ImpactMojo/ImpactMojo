-- ============================================================
-- Cohort-based learning & Notification system
-- Date: 2026-03-20
--
-- Issue #144: Cohort-based learning with scheduled deadlines
-- Issue #145: Email notifications and streak reminders
-- ============================================================

-- ============================================================
-- 1. COHORTS TABLE
-- Scheduled training cohorts with start/end dates
-- ============================================================
CREATE TABLE IF NOT EXISTS public.cohorts (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    org_id UUID REFERENCES public.organizations(id) ON DELETE CASCADE NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    package_id TEXT, -- mel-officer, program-manager, field-staff, governance, custom
    course_ids TEXT[] DEFAULT '{}',
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    status TEXT DEFAULT 'upcoming', -- upcoming, active, completed, archived
    created_by UUID REFERENCES public.profiles(id),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE public.cohorts ENABLE ROW LEVEL SECURITY;

-- ============================================================
-- 2. COHORT MEMBERS TABLE
-- Links users to cohorts with progress tracking
-- ============================================================
CREATE TABLE IF NOT EXISTS public.cohort_members (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    cohort_id UUID REFERENCES public.cohorts(id) ON DELETE CASCADE NOT NULL,
    user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE NOT NULL,
    status TEXT DEFAULT 'enrolled', -- enrolled, in_progress, completed, dropped
    progress_percentage INTEGER DEFAULT 0,
    enrolled_at TIMESTAMPTZ DEFAULT NOW(),
    completed_at TIMESTAMPTZ,
    UNIQUE(cohort_id, user_id)
);

ALTER TABLE public.cohort_members ENABLE ROW LEVEL SECURITY;

-- ============================================================
-- 3. COHORT DISCUSSIONS TABLE
-- Discussion threads within cohorts
-- ============================================================
CREATE TABLE IF NOT EXISTS public.cohort_discussions (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    cohort_id UUID REFERENCES public.cohorts(id) ON DELETE CASCADE NOT NULL,
    user_id UUID REFERENCES public.profiles(id) ON DELETE SET NULL,
    parent_id UUID REFERENCES public.cohort_discussions(id) ON DELETE CASCADE,
    content TEXT NOT NULL,
    is_pinned BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE public.cohort_discussions ENABLE ROW LEVEL SECURITY;

-- ============================================================
-- 4. NOTIFICATIONS TABLE
-- In-app and email notification log
-- ============================================================
CREATE TABLE IF NOT EXISTS public.notifications (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE NOT NULL,
    type TEXT NOT NULL, -- course_update, streak_reminder, cohort_deadline, cohort_discussion, assignment, certificate, welcome
    title TEXT NOT NULL,
    body TEXT,
    link TEXT, -- relative URL to navigate to
    is_read BOOLEAN DEFAULT FALSE,
    email_sent BOOLEAN DEFAULT FALSE,
    email_sent_at TIMESTAMPTZ,
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE public.notifications ENABLE ROW LEVEL SECURITY;

-- ============================================================
-- 5. NOTIFICATION PREFERENCES TABLE
-- User opt-in/out per notification type
-- ============================================================
CREATE TABLE IF NOT EXISTS public.notification_preferences (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE NOT NULL UNIQUE,
    email_course_updates BOOLEAN DEFAULT TRUE,
    email_streak_reminders BOOLEAN DEFAULT TRUE,
    email_cohort_deadlines BOOLEAN DEFAULT TRUE,
    email_cohort_discussions BOOLEAN DEFAULT FALSE,
    email_assignments BOOLEAN DEFAULT TRUE,
    email_certificates BOOLEAN DEFAULT TRUE,
    email_digest_frequency TEXT DEFAULT 'weekly', -- daily, weekly, never
    in_app_enabled BOOLEAN DEFAULT TRUE,
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE public.notification_preferences ENABLE ROW LEVEL SECURITY;

-- ============================================================
-- RLS POLICIES — Cohorts
-- ============================================================

-- Org admins can manage cohorts
CREATE POLICY "Org admins can manage cohorts" ON public.cohorts
    FOR ALL USING (
        EXISTS (SELECT 1 FROM public.organizations WHERE id = org_id AND admin_id = auth.uid())
    );

-- Cohort members can view their cohorts
CREATE POLICY "Cohort members can view cohorts" ON public.cohorts
    FOR SELECT USING (
        EXISTS (SELECT 1 FROM public.cohort_members WHERE cohort_id = id AND user_id = auth.uid())
    );

-- Org admins can manage cohort members
CREATE POLICY "Org admins can manage cohort members" ON public.cohort_members
    FOR ALL USING (
        EXISTS (
            SELECT 1 FROM public.cohorts c
            JOIN public.organizations o ON o.id = c.org_id
            WHERE c.id = cohort_id AND o.admin_id = auth.uid()
        )
    );

-- Users can view own cohort membership
CREATE POLICY "Users can view own cohort membership" ON public.cohort_members
    FOR SELECT USING (auth.uid() = user_id);

-- Users can update own cohort membership (progress)
CREATE POLICY "Users can update own cohort progress" ON public.cohort_members
    FOR UPDATE USING (auth.uid() = user_id)
    WITH CHECK (auth.uid() = user_id);

-- ============================================================
-- RLS POLICIES — Cohort Discussions
-- ============================================================

-- Cohort members can view discussions in their cohorts
CREATE POLICY "Cohort members can view discussions" ON public.cohort_discussions
    FOR SELECT USING (
        EXISTS (SELECT 1 FROM public.cohort_members WHERE cohort_id = cohort_discussions.cohort_id AND user_id = auth.uid())
        OR EXISTS (
            SELECT 1 FROM public.cohorts c
            JOIN public.organizations o ON o.id = c.org_id
            WHERE c.id = cohort_id AND o.admin_id = auth.uid()
        )
    );

-- Cohort members can post discussions
CREATE POLICY "Cohort members can post discussions" ON public.cohort_discussions
    FOR INSERT WITH CHECK (
        auth.uid() = user_id AND
        EXISTS (SELECT 1 FROM public.cohort_members WHERE cohort_id = cohort_discussions.cohort_id AND user_id = auth.uid())
    );

-- Users can update own discussion posts
CREATE POLICY "Users can update own discussions" ON public.cohort_discussions
    FOR UPDATE USING (auth.uid() = user_id);

-- Users can delete own discussion posts
CREATE POLICY "Users can delete own discussions" ON public.cohort_discussions
    FOR DELETE USING (auth.uid() = user_id);

-- ============================================================
-- RLS POLICIES — Notifications
-- ============================================================

-- Users can view own notifications
CREATE POLICY "Users can view own notifications" ON public.notifications
    FOR SELECT USING (auth.uid() = user_id);

-- Users can update own notifications (mark as read)
CREATE POLICY "Users can update own notifications" ON public.notifications
    FOR UPDATE USING (auth.uid() = user_id);

-- Service role inserts notifications (no user INSERT policy needed)

-- ============================================================
-- RLS POLICIES — Notification Preferences
-- ============================================================

CREATE POLICY "Users can manage own notification prefs" ON public.notification_preferences
    FOR ALL USING (auth.uid() = user_id);

-- ============================================================
-- INDEXES
-- ============================================================

CREATE INDEX IF NOT EXISTS idx_cohorts_org_id ON public.cohorts(org_id);
CREATE INDEX IF NOT EXISTS idx_cohorts_status ON public.cohorts(status);
CREATE INDEX IF NOT EXISTS idx_cohort_members_cohort_id ON public.cohort_members(cohort_id);
CREATE INDEX IF NOT EXISTS idx_cohort_members_user_id ON public.cohort_members(user_id);
CREATE INDEX IF NOT EXISTS idx_cohort_discussions_cohort_id ON public.cohort_discussions(cohort_id);
CREATE INDEX IF NOT EXISTS idx_notifications_user_id ON public.notifications(user_id);
CREATE INDEX IF NOT EXISTS idx_notifications_user_unread ON public.notifications(user_id, is_read) WHERE is_read = FALSE;
CREATE INDEX IF NOT EXISTS idx_notifications_created_at ON public.notifications(created_at);
CREATE INDEX IF NOT EXISTS idx_notification_prefs_user_id ON public.notification_preferences(user_id);

-- ============================================================
-- TRIGGERS
-- ============================================================

-- Auto-update cohort status based on dates
CREATE OR REPLACE FUNCTION public.update_cohort_status()
RETURNS TRIGGER AS $$
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
$$ LANGUAGE plpgsql;

CREATE TRIGGER cohort_status_update
    BEFORE INSERT OR UPDATE OF start_date, end_date ON public.cohorts
    FOR EACH ROW EXECUTE FUNCTION public.update_cohort_status();

-- Auto-create notification preferences on profile creation
CREATE OR REPLACE FUNCTION public.create_notification_prefs()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO public.notification_preferences (user_id)
    VALUES (NEW.id)
    ON CONFLICT (user_id) DO NOTHING;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER create_notif_prefs_on_profile
    AFTER INSERT ON public.profiles
    FOR EACH ROW EXECUTE FUNCTION public.create_notification_prefs();

-- ============================================================
-- NOTIFICATION HELPER: Insert notification for a user
-- Callable from Edge Functions via service role
-- ============================================================
CREATE OR REPLACE FUNCTION public.notify_user(
    p_user_id UUID,
    p_type TEXT,
    p_title TEXT,
    p_body TEXT DEFAULT NULL,
    p_link TEXT DEFAULT NULL,
    p_metadata JSONB DEFAULT '{}'
)
RETURNS UUID AS $$
DECLARE
    notif_id UUID;
BEGIN
    INSERT INTO public.notifications (user_id, type, title, body, link, metadata)
    VALUES (p_user_id, p_type, p_title, p_body, p_link, p_metadata)
    RETURNING id INTO notif_id;
    RETURN notif_id;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;
