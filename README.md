# ImpactMojo

[![Netlify Status](https://api.netlify.com/api/v1/badges/impactmojo/deploy-status)](https://www.impactmojo.in)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Free Development Education for Social Impact**

ImpactMojo is a free learning platform providing rigorous, practical educational content on MEAL, Theory of Change, research methods, gender studies, and development economics for NGOs, impact practitioners, and students across South Asia.

🌐 **Live:** [impactmojo.in](https://www.impactmojo.in)

---

## About

ImpactMojo addresses a critical gap in development education. Development work in India and South Asia often lacks standardized, evidence-based knowledge foundations—resulting in interventions that lack rigor and measurable impact.

We provide accessible, high-quality educational materials grounded in South Asian context, designed for educators, practitioners, researchers, students, and policymakers.

### What We Offer

| Category | Description |
|----------|-------------|
| **Courses** | Comprehensive learning tracks on MEAL, Theory of Change, Research Methods, Gender Studies, and more |
| **Labs** | Interactive tools like the Theory of Change Workbench, Sample Size Calculator, and Data Analysis Sandbox |
| **Games** | Gamified learning experiences for development concepts |
| **ImpactLex** | Development sector terminology dictionary with 23+ terms, formulas, and case studies |
| **Coaching** | Premium 1-on-1 guidance for development professionals |
| **Community** | WhatsApp PLC, Discord, and Telegram for peer learning & resources |

---

## Features

### Learning Platform
- 📚 **10+ Courses** — MEAL 101, Theory of Change, Research Methods, Gender Studies, Development Economics, Climate Change, Public Health, and more
- 🔬 **Interactive Labs** — Hands-on tools for practical application
- 🎮 **Learning Games** — Gamified concept reinforcement
- 📖 **ImpactLex Dictionary** — PWA-enabled terminology reference

### User Features
- 🔖 **Bookmarks** — Save courses and content for later
- 📝 **Personal Notes** — Take notes while learning with streak tracking
- 📊 **Progress Tracking** — Monitor your learning journey
- 📚 **Reading Lists** — Curated resource collections
- ⚖️ **Course Comparison** — Compare courses side-by-side

### Account System
- 🔐 **Secure Authentication** — Powered by Supabase
- 👤 **User Profiles** — Track progress and preferences
- ⭐ **Tiered Access** — Explorer (free), Practitioner, Professional, Organization tiers
- 🌐 **Community Access** — WhatsApp PLC, Discord, and Telegram

### Technical
- 📱 **Mobile-Optimized** — Dedicated mobile experience
- 🌍 **Multilingual** — Content in English, Hindi, Tamil, Bengali, Telugu, Marathi
- ⚡ **Fast & Lightweight** — Static site with no heavy dependencies
- 🔗 **Clean URLs** — SEO-friendly routing (`/courses`, `/labs`, `/about`)
- ♿ **Accessible** — Built with accessibility standards (UserWay integration)

---

## Quick Start

### View Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Varnasr/ImpactMojo.git
   cd ImpactMojo
   ```

2. **Start a local server:**
   ```bash
   # Using Python 3
   python -m http.server 8000
   
   # Using Node.js
   npx http-server
   ```

3. **Open in browser:**
   ```
   http://localhost:8000
   ```

> **Note:** A local server is required for authentication and routing features to work properly.

---

## Project Structure

```
ImpactMojo/
├── index.html              # Main site (desktop)
├── mobile.html             # Mobile-optimized version
├── _redirects              # Netlify clean URL routing
├── manifest.json           # PWA manifest
│
├── js/
│   ├── auth.js             # Supabase authentication
│   └── router.js           # Clean URL section router
│
├── login.html              # User login
├── signup.html             # User registration
├── account.html            # User dashboard
├── forgot-password.html    # Password recovery
├── premium.html            # Premium features & registration
│
├── blog.html               # Learning Loops blog
├── community/
│   └── index.html          # Community landing page
├── impactlex/
│   └── index.html          # ImpactLex dictionary (PWA)
│
├── assets/
│   ├── images/             # Logos, icons, illustrations
│   └── fonts/              # Custom fonts
│
├── LICENSE                 # CC-BY-4.0 license
├── CONTRIBUTING.md         # Contribution guidelines
├── CODE_OF_CONDUCT.md      # Community code of conduct
├── SECURITY.md             # Security policy
└── README.md
```

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| **HTML/CSS/JS** | Core frontend (no frameworks) |
| **Supabase** | Authentication & database |
| **Netlify** | Hosting & deployment |
| **Google Analytics** | Usage analytics |
| **Formspree** | Contact form handling |
| **UserWay** | Accessibility widget |
| **Google Fonts** | Inter & Poppins typography |

---

## Deployment

### Automatic Deployment (Netlify)

This project deploys automatically via Netlify. Any push to `main` triggers a new deployment.

**Netlify Configuration:**
- Build command: None (static site)
- Publish directory: `.` (root)
- `_redirects` file handles clean URL routing

### Deploy Your Own Fork

1. **Fork this repository** on GitHub
2. **Connect to Netlify:**
   - Go to [netlify.com](https://www.netlify.com)
   - Click "Add new site" → "Import an existing project"
   - Select your forked repository
   - Deploy
3. **Configure Supabase** (for authentication):
   - Create a Supabase project
   - Update credentials in `js/auth.js`
   - Set up `profiles` table in Supabase

---

## Environment & Configuration

### Supabase Setup

The authentication system requires a Supabase project with:

1. **Authentication** enabled (Email, Google OAuth, Magic Links)
2. **Profiles table** with schema:
   ```sql
   create table profiles (
     id uuid references auth.users primary key,
     full_name text,
     display_name text,
     organization text,
     city text,
     country text,
     linkedin_url text,
     bio text,
     avatar_url text,
     subscription_tier text default 'explorer',
     subscription_status text default 'active',
     courses_completed text[],
     total_learning_hours integer default 0,
     streak_days integer default 0,
     created_at timestamp with time zone default now(),
     updated_at timestamp with time zone default now()
   );
   ```

### Clean URL Routing

The `_redirects` file enables clean URLs:
- `/courses` → Opens Courses modal
- `/labs` → Opens Labs modal  
- `/about` → Scrolls to About section
- `/testimonials` → Scrolls to Wall of Love

The `router.js` script handles client-side navigation after Netlify serves `index.html`.

---

## Content & Courses

### Available Courses

| Course | Description |
|--------|-------------|
| **MEAL 101** | Monitoring, Evaluation, Accountability & Learning fundamentals |
| **Theory of Change** | Building effective theories of change and logic models |
| **Research Methods** | Qualitative and quantitative research design |
| **Gender Studies 101** | Feminist theory, intersectionality, and South Asian context |
| **Development Economics 101** | Growth, inequality, institutions, and policy |
| **Climate Change 101** | IPCC basics, vulnerability, adaptation, and climate justice |
| **Public Health 101** | Health systems, epidemiology, and health equity |
| **Data Feminism 101** | Challenging dominant data narratives |
| **Social Safety Nets 101** | India's welfare architecture (PDS, NREGA, Aadhaar) |
| **Decent Work 101** | Labor rights, informality, and fair livelihoods |

### Multilingual Support

Content is available in:
- 🇬🇧 English
- 🇮🇳 Hindi (हिंदी)
- 🇮🇳 Tamil (தமிழ்)
- 🇮🇳 Bengali (বাংলা)
- 🇮🇳 Telugu (తెలుగు)
- 🇮🇳 Marathi (मराठी)

---

## Contributing

We welcome contributions! Whether improving content, fixing bugs, enhancing accessibility, or adding translations. See **[CONTRIBUTING.md](CONTRIBUTING.md)** for full guidelines.

**Quick ideas:** Content improvements, South Asian case studies, translations (Hindi, Tamil, Bengali, Telugu, Marathi), accessibility fixes, UI/UX enhancements, bug reports, new tools & labs.

---

## Browser Support

| Browser | Support |
|---------|---------|
| Chrome/Chromium | ✅ Latest |
| Firefox | ✅ Latest |
| Safari | ✅ Latest |
| Edge | ✅ Latest |
| Mobile Safari (iOS) | ✅ Latest |
| Chrome Mobile | ✅ Latest |

---

## Support & Contact

- 🐛 **Report bugs:** [GitHub Issues](https://github.com/Varnasr/ImpactMojo/issues)
- 💡 **Feature requests:** [GitHub Issues](https://github.com/Varnasr/ImpactMojo/issues)
- 📧 **General inquiries:** hello@impactmojo.in
- 📧 **Registration:** register@impactmojo.in
- 💬 **WhatsApp PLC:** [Professional Learning Community](https://chat.whatsapp.com/EsBjbKaQfupG1HbtajTjHM) — Peer discussions & fieldwork support
- 💬 **Discord:** [Join Server](https://discord.gg/M3ZCmUe7ab) — Tech tinkering, data tools, MPC servers & code
- 💬 **Telegram:** [Follow Channel](https://t.me/impactmojo) — Free toolkits, datasets, templates & reading lists

### Support the Platform

ImpactMojo operates on a "pay what you think is fair" model.

**UPI:** `impactmojo@ibl`

---

## License

This project is released under the **Creative Commons Attribution 4.0 International (CC-BY-4.0)** license.

Educational content is available for educational and non-commercial use. Educators are encouraged to adapt materials with appropriate attribution.

---

## Citation

If you use ImpactMojo materials in research, teaching, or practice:

```
Raman, V. S. (2025). ImpactMojo: Free Development Education for Social Impact. 
Retrieved from https://www.impactmojo.in
```

---

## Acknowledgments

**Founded by Dr. Varna Sri Raman**, a development economist with two decades of experience in development practice, research, and education across South Asia.

**Sponsored by** PinPoint Ventures

**Key Contributors:**
- Vandana Soni — Social Media & Marketing
- Vignesh — Technical Support

The platform is shaped by contributions from educators, practitioners, designers, and the broader development community.

---

**Version:** 8.0.0
**Last Updated:** March 2026
**License:** CC-BY-4.0  
**Hosting:** Netlify
