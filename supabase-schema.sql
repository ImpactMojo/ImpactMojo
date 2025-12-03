-- =====================================================
-- ImpactMojo Supabase Database Schema
-- Run this in your Supabase SQL Editor
-- Go to: SQL Editor (left sidebar) → New Query → Paste this → Run
-- =====================================================

-- Enable UUID extension (usually already enabled)
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- =====================================================
-- 1. USER PROFILES TABLE
-- Stores additional user information beyond auth
-- =====================================================
CREATE TABLE IF NOT EXISTS public.profiles (
    id UUID REFERENCES auth.users(id) ON DELETE CASCADE PRIMARY KEY,
    email TEXT,
    full_name TEXT,
    display_name TEXT,
    avatar_url TEXT,
    organization TEXT,
    role TEXT DEFAULT 'learner', -- learner, practitioner, professional, organization_admin
    subscription_tier TEXT DEFAULT 'explorer', -- explorer (free), practitioner, professional, organization
    subscription_status TEXT DEFAULT 'active', -- active, cancelled, expired, trial
    subscription_start DATE,
    subscription_end DATE,
    razorpay_customer_id TEXT,
    razorpay_subscription_id TEXT,
    phone TEXT,
    country TEXT DEFAULT 'India',
    city TEXT,
    linkedin_url TEXT,
    bio TEXT,
    interests TEXT[], -- Array of interest areas
    courses_completed TEXT[], -- Array of completed course IDs
    certificates_earned TEXT[], -- Array of certificate IDs
    total_learning_hours DECIMAL DEFAULT 0,
    streak_days INTEGER DEFAULT 0,
    last_active_at TIMESTAMPTZ,
    referral_code TEXT UNIQUE,
    referred_by UUID REFERENCES public.profiles(id),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- =====================================================
-- 2. USER PROGRESS TABLE
-- Tracks learning progress across courses
-- =====================================================
CREATE TABLE IF NOT EXISTS public.user_progress (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE,
    course_id TEXT NOT NULL,
    course_name TEXT,
    progress_percentage INTEGER DEFAULT 0,
    started_at TIMESTAMPTZ DEFAULT NOW(),
    completed_at TIMESTAMPTZ,
    last_accessed_at TIMESTAMPTZ DEFAULT NOW(),
    time_spent_minutes INTEGER DEFAULT 0,
    current_section TEXT,
    notes TEXT,
    UNIQUE(user_id, course_id)
);

-- =====================================================
-- 3. USER BOOKMARKS TABLE
-- Stores user bookmarks from the site
-- =====================================================
CREATE TABLE IF NOT EXISTS public.bookmarks (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE,
    item_type TEXT NOT NULL, -- course, deck, tool, blog, resource
    item_id TEXT NOT NULL,
    item_title TEXT,
    item_url TEXT,
    notes TEXT,
    tags TEXT[],
    created_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(user_id, item_type, item_id)
);

-- =====================================================
-- 4. USER NOTES TABLE
-- Personal notes system
-- =====================================================
CREATE TABLE IF NOT EXISTS public.user_notes (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE,
    title TEXT,
    content TEXT,
    related_course TEXT,
    related_url TEXT,
    tags TEXT[],
    is_pinned BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- =====================================================
-- 5. CERTIFICATES TABLE
-- Issued certificates for completed courses
-- =====================================================
CREATE TABLE IF NOT EXISTS public.certificates (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE,
    course_id TEXT NOT NULL,
    course_name TEXT NOT NULL,
    certificate_number TEXT UNIQUE NOT NULL,
    issued_at TIMESTAMPTZ DEFAULT NOW(),
    verification_url TEXT,
    pdf_url TEXT,
    UNIQUE(user_id, course_id)
);

-- =====================================================
-- 6. PAYMENT HISTORY TABLE
-- Tracks all payments
-- =====================================================
CREATE TABLE IF NOT EXISTS public.payments (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE,
    razorpay_payment_id TEXT,
    razorpay_order_id TEXT,
    razorpay_signature TEXT,
    amount DECIMAL NOT NULL,
    currency TEXT DEFAULT 'INR',
    status TEXT DEFAULT 'pending', -- pending, completed, failed, refunded
    payment_method TEXT, -- upi, card, netbanking, wallet
    description TEXT,
    subscription_tier TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- =====================================================
-- 7. COACHING BOOKINGS TABLE
-- For coaching session bookings
-- =====================================================
CREATE TABLE IF NOT EXISTS public.coaching_bookings (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE,
    coach_type TEXT NOT NULL, -- career, research, workshop
    session_date DATE,
    session_time TIME,
    duration_minutes INTEGER DEFAULT 60,
    status TEXT DEFAULT 'pending', -- pending, confirmed, completed, cancelled
    notes TEXT,
    payment_id UUID REFERENCES public.payments(id),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- =====================================================
-- ROW LEVEL SECURITY (RLS) POLICIES
-- Ensures users can only access their own data
-- =====================================================

-- Enable RLS on all tables
ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.user_progress ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.bookmarks ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.user_notes ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.certificates ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.payments ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.coaching_bookings ENABLE ROW LEVEL SECURITY;

-- Profiles: Users can view and update their own profile
CREATE POLICY "Users can view own profile" ON public.profiles
    FOR SELECT USING (auth.uid() = id);

CREATE POLICY "Users can update own profile" ON public.profiles
    FOR UPDATE USING (auth.uid() = id);

CREATE POLICY "Users can insert own profile" ON public.profiles
    FOR INSERT WITH CHECK (auth.uid() = id);

-- User Progress: Users can manage their own progress
CREATE POLICY "Users can manage own progress" ON public.user_progress
    FOR ALL USING (auth.uid() = user_id);

-- Bookmarks: Users can manage their own bookmarks
CREATE POLICY "Users can manage own bookmarks" ON public.bookmarks
    FOR ALL USING (auth.uid() = user_id);

-- User Notes: Users can manage their own notes
CREATE POLICY "Users can manage own notes" ON public.user_notes
    FOR ALL USING (auth.uid() = user_id);

-- Certificates: Users can view their own certificates
CREATE POLICY "Users can view own certificates" ON public.certificates
    FOR SELECT USING (auth.uid() = user_id);

-- Payments: Users can view their own payments
CREATE POLICY "Users can view own payments" ON public.payments
    FOR SELECT USING (auth.uid() = user_id);

-- Coaching Bookings: Users can manage their own bookings
CREATE POLICY "Users can manage own bookings" ON public.coaching_bookings
    FOR ALL USING (auth.uid() = user_id);

-- =====================================================
-- FUNCTIONS AND TRIGGERS
-- =====================================================

-- Function to automatically create profile on signup
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
    );
    RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Trigger to create profile on new user signup
DROP TRIGGER IF EXISTS on_auth_user_created ON auth.users;
CREATE TRIGGER on_auth_user_created
    AFTER INSERT ON auth.users
    FOR EACH ROW EXECUTE FUNCTION public.handle_new_user();

-- Function to update updated_at timestamp
CREATE OR REPLACE FUNCTION public.update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for updated_at
CREATE TRIGGER profiles_updated_at
    BEFORE UPDATE ON public.profiles
    FOR EACH ROW EXECUTE FUNCTION public.update_updated_at();

CREATE TRIGGER user_notes_updated_at
    BEFORE UPDATE ON public.user_notes
    FOR EACH ROW EXECUTE FUNCTION public.update_updated_at();

-- =====================================================
-- INDEXES FOR PERFORMANCE
-- =====================================================
CREATE INDEX IF NOT EXISTS idx_profiles_email ON public.profiles(email);
CREATE INDEX IF NOT EXISTS idx_profiles_subscription_tier ON public.profiles(subscription_tier);
CREATE INDEX IF NOT EXISTS idx_user_progress_user_id ON public.user_progress(user_id);
CREATE INDEX IF NOT EXISTS idx_bookmarks_user_id ON public.bookmarks(user_id);
CREATE INDEX IF NOT EXISTS idx_certificates_user_id ON public.certificates(user_id);
CREATE INDEX IF NOT EXISTS idx_payments_user_id ON public.payments(user_id);

-- =====================================================
-- SUCCESS MESSAGE
-- =====================================================
-- If you see this without errors, your database is ready!
-- Next: Set up authentication in your Supabase dashboard
