-- =====================================================
-- Course Content Table — Dynamic Content Delivery
-- Moves static HTML course content into Supabase so
-- forks cannot redistribute course material.
-- =====================================================

-- 1. Main course_content table
CREATE TABLE IF NOT EXISTS public.course_content (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    course_id TEXT NOT NULL,              -- e.g. 'gandhi', 'devai', 'mel'
    module_number INTEGER NOT NULL,        -- 1-based module number
    module_title TEXT NOT NULL,
    module_intro TEXT,                     -- short intro paragraph
    content_html TEXT NOT NULL,            -- full module HTML (cards, tables, quotes, etc.)
    quiz_html TEXT,                        -- quiz section HTML (separate for progress tracking)
    is_preview BOOLEAN DEFAULT FALSE,      -- TRUE = visible without auth (module 1 of each course)
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(course_id, module_number)
);

-- 2. Index for fast lookups
CREATE INDEX idx_course_content_course ON public.course_content(course_id);
CREATE INDEX idx_course_content_lookup ON public.course_content(course_id, module_number);

-- 3. RLS: content is read-only via service role or edge function
ALTER TABLE public.course_content ENABLE ROW LEVEL SECURITY;

-- No direct read policy for anon — content is served ONLY through the edge function
-- Service role (used by edge function) bypasses RLS automatically

-- 4. Admin-only write policy (for seeding/updates via dashboard)
CREATE POLICY "Service role can manage course_content"
    ON public.course_content
    FOR ALL
    USING (auth.role() = 'service_role')
    WITH CHECK (auth.role() = 'service_role');

-- 5. Updated_at trigger
CREATE OR REPLACE FUNCTION update_course_content_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER course_content_updated
    BEFORE UPDATE ON public.course_content
    FOR EACH ROW
    EXECUTE FUNCTION update_course_content_timestamp();
