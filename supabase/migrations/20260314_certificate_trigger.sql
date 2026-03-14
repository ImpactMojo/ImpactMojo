-- =====================================================
-- Certificate Auto-Issuance Trigger
-- Fires when user_progress.progress_percentage reaches 100
-- Inserts a certificate record directly (no Edge Function call needed)
-- =====================================================

-- Certificate-eligible courses
CREATE OR REPLACE FUNCTION public.auto_issue_certificate()
RETURNS TRIGGER AS $$
DECLARE
  v_course_name TEXT;
  v_cert_number TEXT;
  v_existing_id UUID;
  v_hex TEXT;
BEGIN
  -- Only fire when progress reaches 100%
  IF NEW.progress_percentage < 100 THEN
    RETURN NEW;
  END IF;

  -- Only fire if this is a real change (not already 100)
  IF OLD IS NOT NULL AND OLD.progress_percentage >= 100 THEN
    RETURN NEW;
  END IF;

  -- Map course_id to course name
  v_course_name := CASE NEW.course_id
    WHEN 'mel' THEN 'Monitoring, Evaluation & Learning'
    WHEN 'dataviz' THEN 'Data Visualization for Impact'
    WHEN 'devai' THEN 'AI for Development'
    WHEN 'devecon' THEN 'Development Economics'
    WHEN 'gandhi' THEN 'Gandhi & Contemporary Development'
    WHEN 'law' THEN 'Law & Development'
    WHEN 'media' THEN 'Media, Communication & Development'
    WHEN 'SEL' THEN 'Social & Emotional Learning'
    WHEN 'poa' THEN 'Philosophy of Action'
    ELSE NULL
  END;

  -- Skip if not a recognized course
  IF v_course_name IS NULL THEN
    RETURN NEW;
  END IF;

  -- Check if certificate already exists (idempotent)
  SELECT id INTO v_existing_id
  FROM public.certificates
  WHERE user_id = NEW.user_id AND course_id = NEW.course_id;

  IF v_existing_id IS NOT NULL THEN
    RETURN NEW;
  END IF;

  -- Generate certificate number: IM-DEVECON-2026-A3F7B2
  v_hex := UPPER(SUBSTRING(MD5(uuid_generate_v4()::TEXT || NOW()::TEXT) FROM 1 FOR 6));
  v_cert_number := 'IM-' || UPPER(LEFT(NEW.course_id, 8)) || '-' || EXTRACT(YEAR FROM NOW())::TEXT || '-' || v_hex;

  -- Insert certificate
  INSERT INTO public.certificates (
    user_id,
    course_id,
    course_name,
    certificate_number,
    verification_url
  ) VALUES (
    NEW.user_id,
    NEW.course_id,
    v_course_name,
    v_cert_number,
    'https://www.impactmojo.in/verify-certificate.html?cert=' || v_cert_number
  );

  -- Update completed_at on user_progress
  NEW.completed_at := NOW();

  -- Append to profiles.certificates_earned
  UPDATE public.profiles
  SET certificates_earned = COALESCE(certificates_earned, '{}') || ARRAY[v_cert_number],
      courses_completed = COALESCE(courses_completed, '{}') || ARRAY[NEW.course_id]
  WHERE id = NEW.user_id
    AND NOT (COALESCE(courses_completed, '{}') @> ARRAY[NEW.course_id]);

  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Create the trigger
DROP TRIGGER IF EXISTS on_course_completed ON public.user_progress;
CREATE TRIGGER on_course_completed
  BEFORE INSERT OR UPDATE ON public.user_progress
  FOR EACH ROW
  WHEN (NEW.progress_percentage >= 100)
  EXECUTE FUNCTION public.auto_issue_certificate();

-- Allow public certificate verification (anon users can look up certificates)
CREATE POLICY "Public can verify certificates" ON public.certificates
  FOR SELECT USING (true);

-- Allow public profile name lookup for certificate display
CREATE POLICY "Public can view profile names for verification" ON public.profiles
  FOR SELECT USING (true);
