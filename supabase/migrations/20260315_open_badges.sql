-- =====================================================
-- Open Badges 3.0 — extend certificates table with
-- badge metadata for W3C Verifiable Credentials
-- =====================================================

-- Add badge metadata columns to certificates
ALTER TABLE public.certificates
  ADD COLUMN IF NOT EXISTS badge_class_id TEXT,
  ADD COLUMN IF NOT EXISTS badge_name TEXT,
  ADD COLUMN IF NOT EXISTS badge_description TEXT,
  ADD COLUMN IF NOT EXISTS competencies TEXT[],
  ADD COLUMN IF NOT EXISTS track TEXT,
  ADD COLUMN IF NOT EXISTS credential_json JSONB,
  ADD COLUMN IF NOT EXISTS badge_svg_url TEXT,
  ADD COLUMN IF NOT EXISTS linkedin_shared_at TIMESTAMPTZ;

-- Index for track-level queries (e.g. "show all badges in MEL track")
CREATE INDEX IF NOT EXISTS idx_certificates_track
  ON public.certificates(track);

-- Index for badge class lookups
CREATE INDEX IF NOT EXISTS idx_certificates_badge_class
  ON public.certificates(badge_class_id);

-- =====================================================
-- Badge share tracking
-- Records when users share badges to external platforms
-- =====================================================
CREATE TABLE IF NOT EXISTS public.badge_shares (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE,
  certificate_id UUID REFERENCES public.certificates(id) ON DELETE CASCADE,
  platform TEXT NOT NULL,  -- 'linkedin', 'twitter', 'email', 'embed'
  shared_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_badge_shares_user
  ON public.badge_shares(user_id);

-- RLS policies
ALTER TABLE public.badge_shares ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can view own badge shares"
  ON public.badge_shares FOR SELECT
  USING (auth.uid() = user_id);

CREATE POLICY "Users can insert own badge shares"
  ON public.badge_shares FOR INSERT
  WITH CHECK (auth.uid() = user_id);

-- =====================================================
-- Update certificate trigger to include badge metadata
-- =====================================================
CREATE OR REPLACE FUNCTION public.auto_issue_certificate_with_badge()
RETURNS trigger AS $$
DECLARE
  cert_num TEXT;
  badge_class TEXT;
  badge_nm TEXT;
  badge_desc TEXT;
  badge_track TEXT;
  badge_comps TEXT[];
  verify_url TEXT;
BEGIN
  -- Only fire when progress hits 100% for the first time
  IF NEW.progress_percentage >= 100 AND
     (OLD IS NULL OR OLD.progress_percentage < 100) THEN

    -- Check if certificate already exists
    IF EXISTS (
      SELECT 1 FROM public.certificates
      WHERE user_id = NEW.user_id AND course_id = NEW.course_id
    ) THEN
      RETURN NEW;
    END IF;

    -- Generate certificate number
    cert_num := 'IM-' || UPPER(LEFT(NEW.course_id, 8)) || '-' ||
                EXTRACT(YEAR FROM NOW())::TEXT || '-' ||
                UPPER(SUBSTR(MD5(NEW.user_id::TEXT || NEW.course_id || NOW()::TEXT), 1, 6));

    verify_url := 'https://www.impactmojo.in/verify-certificate.html?cert=' || cert_num;

    -- Map course to badge metadata
    SELECT bc.name, bc.description, bc.track, bc.competencies
    INTO badge_nm, badge_desc, badge_track, badge_comps
    FROM (VALUES
      ('mel',     'MEL Practitioner',                'Demonstrated mastery of MEL frameworks.', 'Monitoring, Evaluation & Learning', ARRAY['MEL Frameworks','Theory of Change','Qualitative Methods','Research Ethics']),
      ('dataviz', 'Data Visualization Specialist',   'Proficient in visual encoding and dashboards.', 'Data & Technology', ARRAY['Visual Encoding','Chart Selection','Dashboard Design','Data Storytelling']),
      ('devai',   'AI for Impact Practitioner',      'Skilled in ML/NLP for development M&E.', 'Data & Technology', ARRAY['Machine Learning','NLP for Development','Algorithmic Bias','AI Ethics']),
      ('devecon', 'Development Economics Analyst',   'Understanding of development economics.', 'Policy & Economics', ARRAY['Development Economics','Poverty Analysis','Impact Evaluation','Cost-Effectiveness']),
      ('gandhi',  'Gandhian Thought Scholar',        'Engagement with Gandhi''s political philosophy.', 'Philosophy, Law & Governance', ARRAY['Political Philosophy','Nonviolent Praxis','Ethical Leadership','Social Movements']),
      ('law',     'Law & Development Practitioner',  'Proficient in legal frameworks for development.', 'Philosophy, Law & Governance', ARRAY['Constitutional Law','Rights-Based Approach','Legal Frameworks','Justice Systems']),
      ('media',   'Dev Communication Specialist',    'Skilled in BCC and media for development.', 'Health, Communication & Wellbeing', ARRAY['BCC Strategy','Storytelling','Media for Development','Campaign Design']),
      ('SEL',     'SEL Facilitator',                 'Certified in SEL facilitation.', 'Health, Communication & Wellbeing', ARRAY['Social-Emotional Learning','Facilitation','Wellbeing Frameworks','Group Dynamics']),
      ('poa',     'Politics of Aspiration Analyst',  'Understanding of political economy.', 'Policy & Economics', ARRAY['Political Economy','Aspiration Theory','Development Politics','Policy Analysis'])
    ) AS bc(course_id, name, description, track, competencies)
    WHERE bc.course_id = NEW.course_id;

    badge_class := NEW.course_id;

    -- Insert certificate with badge metadata
    INSERT INTO public.certificates (
      user_id, course_id, course_name, certificate_number,
      verification_url, badge_class_id, badge_name,
      badge_description, competencies, track
    ) VALUES (
      NEW.user_id, NEW.course_id, NEW.course_name, cert_num,
      verify_url, badge_class, badge_nm,
      badge_desc, badge_comps, badge_track
    );

    -- Update profile arrays
    UPDATE public.profiles SET
      certificates_earned = array_append(
        COALESCE(certificates_earned, ARRAY[]::TEXT[]), cert_num
      ),
      courses_completed = array_append(
        COALESCE(courses_completed, ARRAY[]::TEXT[]), NEW.course_id
      )
    WHERE id = NEW.user_id;
  END IF;

  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Replace existing trigger with badge-aware version
DROP TRIGGER IF EXISTS on_course_completed ON public.user_progress;
CREATE TRIGGER on_course_completed
  BEFORE INSERT OR UPDATE ON public.user_progress
  FOR EACH ROW
  EXECUTE FUNCTION public.auto_issue_certificate_with_badge();
