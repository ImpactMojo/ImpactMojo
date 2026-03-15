-- Challenge Submissions: stores user submissions to Live Case Challenges
CREATE TABLE IF NOT EXISTS public.challenge_submissions (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    challenge_id TEXT NOT NULL,
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE NOT NULL,
    submission_text TEXT NOT NULL,
    submission_status TEXT DEFAULT 'pending',
    submitted_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(challenge_id, user_id)
);

ALTER TABLE public.challenge_submissions ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can view own submissions" ON public.challenge_submissions
    FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Users can insert own submissions" ON public.challenge_submissions
    FOR INSERT WITH CHECK (auth.uid() = user_id);
CREATE POLICY "Users can update own submissions" ON public.challenge_submissions
    FOR UPDATE USING (auth.uid() = user_id);

CREATE INDEX IF NOT EXISTS idx_challenge_submissions_user_id ON public.challenge_submissions(user_id);
CREATE INDEX IF NOT EXISTS idx_challenge_submissions_challenge_id ON public.challenge_submissions(challenge_id);

-- Challenge Requests: custom challenge requests from Team Plan organisations
CREATE TABLE IF NOT EXISTS public.challenge_requests (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    org_id UUID REFERENCES public.organizations(id) ON DELETE CASCADE NOT NULL,
    requested_by UUID REFERENCES auth.users(id) ON DELETE SET NULL,
    topic TEXT NOT NULL,
    track TEXT NOT NULL,
    description TEXT NOT NULL,
    participants INTEGER,
    difficulty TEXT DEFAULT 'intermediate',
    status TEXT DEFAULT 'pending',
    admin_notes TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE public.challenge_requests ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Org members can view their org requests" ON public.challenge_requests
    FOR SELECT USING (
        org_id IN (SELECT org_id FROM public.organization_members WHERE user_id = auth.uid())
    );
CREATE POLICY "Org members can insert requests" ON public.challenge_requests
    FOR INSERT WITH CHECK (
        org_id IN (SELECT org_id FROM public.organization_members WHERE user_id = auth.uid())
    );

CREATE INDEX IF NOT EXISTS idx_challenge_requests_org_id ON public.challenge_requests(org_id);
