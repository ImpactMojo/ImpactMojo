# The Transparency Page — What It Is, Why It Exists, and How to Read It

ImpactMojo has a public [Transparency page](https://www.impactmojo.in/transparency.html). This guide explains why we built it, what's on it, and why we made specific decisions about what to share and what to keep private.

---

## Why We Have a Transparency Page

Most ed-tech platforms tell you how many users they have in marketing copy and expect you to take their word for it. We think that's insufficient — especially for a platform that serves development professionals who spend their careers demanding evidence and accountability from others.

The Transparency page exists because:

1. **We ask our users to be evidence-driven. We should be too.** If we teach evaluation and accountability, we should practise it ourselves. Publishing our numbers — including how we calculate them — holds us to the same standard we teach.

2. **We're bootstrapped and small.** We don't have millions of users or venture capital funding. Our numbers are modest and real. We'd rather show honest, modest numbers than hide behind vague claims like "thousands of learners worldwide."

3. **Trust requires openness.** When an NGO considers using ImpactMojo for team training, or when a funder evaluates us as a capacity-building partner, they deserve to see real data — not just a polished marketing page.

4. **We're open source.** Our code is on GitHub. Our documentation is public. The Transparency page is the public-facing complement — showing not just how the platform is built, but how it's used.

---

## What's on the Transparency Page

The page has five sections:

### 1. How We Make Money

A clear breakdown of ImpactMojo's revenue model:

- **Explorer tier (Free):** All courses, games, handouts, Dataverse, ImpactLex, BCT repository, and community access
- **Practitioner tier (Paid):** Adds interactive labs, premium tools, live case challenges, certificates, and VaniScribe
- **Organisation tier (Paid):** Adds team dashboards, member management, learning path assignments, bulk onboarding, and priority support

We also state our core commitment: free content stays free. Paid tiers fund development, servers, and new content. We don't sell user data or run advertising.

**Why this section matters:** Too many "free" platforms are actually advertising businesses or data harvesting operations. We want to be explicit about how the money works so users don't have to wonder.

### 2. Methodology & Data Sources

This is the section that makes our Transparency page different from a typical "about" page. We explain exactly how every number on the page is calculated:

**Two data sources:**
- **Legacy data:** Historical records from Google Sheets maintained since launch — form submissions, enrolment records, and manual usage logs from before our current analytics setup
- **Current analytics (GA4):** Google Analytics 4 tracking live platform usage — users, sessions, pageviews, and engagement

**How totals work:** Total = Legacy Data + Current GA4 Data. We're upfront that legacy numbers are approximate (based on Google Forms and manual tracking) and that GA4 numbers reflect the most recent data pull.

**Metric definitions:** Every metric is defined precisely:
- **Users** — Unique visitors who loaded a page at least once (GA4 `active_users` + legacy form submissions)
- **Sessions** — A period of site activity; expires after 30 minutes of inactivity (GA4 default)
- **Engagement Rate** — Percentage of sessions that lasted >10 seconds, had a conversion event, or had 2+ pageviews
- **Course/Game/Tool Engagement** — Cumulative unique users per item, combining legacy enrolment records with GA4 page-level user counts
- **Content Count** — Manual audit of HTML files in the codebase
- **Feature Adoption** — Whether a feature is live and its cumulative user count

**Why this section matters:** Numbers without methodology are just marketing. By showing how we count, we let users judge for themselves whether our metrics are meaningful. A development evaluator reading this page will recognise the same rigour they'd expect in a programme monitoring report.

### 3. Platform Numbers (KPI Cards)

Cumulative totals for key metrics — users, sessions, engagement rate, and content counts. These are aggregate numbers, not broken down by individual user or session.

### 4. Engagement Charts

Visual breakdowns of:
- **Course engagement** — which courses have the most users
- **Game engagement** — which games are most played
- **Tools & Labs engagement** — which interactive tools see the most use

These charts help us (and you) understand what content is most valuable. They also show honestly which content is underused — we don't hide the less popular items.

### 5. Feature Adoption Table

A table showing every major platform feature, whether it's live, and its cumulative user count. This is our public feature tracker — you can see what we've shipped and what's getting traction.

### 6. Legal & Compliance

A privacy notice confirming that all data on the page is aggregate — no individual user data, session recordings, personal identifiers, or PII are collected, stored, or displayed. Links to our full Privacy Policy, Terms of Service, Disclaimer, Data Protection policy, and Refund Policy.

---

## Why Google Analytics Data Is Private

You'll notice the Transparency page shows **combined cumulative totals** but does not display the GA4 sub-totals separately. Here's why:

### What we show publicly
- Combined cumulative numbers (legacy + GA4)
- Engagement charts showing relative usage across content
- Feature adoption status and user counts
- Full methodology explaining how every number is calculated

### What we keep internal
- Raw GA4 dashboards and breakdowns
- Real-time traffic data
- Geographic breakdowns of users
- Session-level data
- Referral sources and acquisition channels
- Conversion funnels

### Why the distinction?

**1. User privacy.** Even though GA4 data is anonymised, granular breakdowns (e.g., "3 users from Muzaffarpur accessed the Gender course this week") can become identifying in small populations. Development professionals in specific districts working on specific topics are a small community. Aggregate totals protect individual privacy; granular breakdowns could compromise it.

**2. Competitive sensitivity.** Detailed traffic data — which acquisition channels work, which content converts, which pages have high bounce rates — is operationally sensitive. We're a bootstrapped platform competing with well-funded alternatives. Sharing our traffic strategy publicly would be like a small business publishing its customer acquisition playbook.

**3. Data can be misinterpreted.** Raw GA4 data without context is easily misread. A page with low traffic might be low because it's new, not because it's bad. A high bounce rate on a handout page might mean users found what they needed quickly, not that the content failed. We'd rather publish curated, contextualised numbers than raw data that invites wrong conclusions.

**4. The totals are what matter.** For the purposes of transparency — "is this platform real, is it used, is it growing?" — cumulative totals with clear methodology answer the question. GA4 sub-totals add precision but not meaningful transparency.

### What if you need more detail?

If you're a funder, partner, or institution evaluating ImpactMojo and need more detailed usage data for due diligence, email [hello@impactmojo.in](mailto:hello@impactmojo.in). We're happy to share additional metrics in a private context where we can provide proper context alongside the numbers.

---

## How We Think About Transparency

Transparency isn't the same as publishing everything. It's about being honest, providing evidence for claims, and explaining your reasoning — including the reasoning behind what you choose not to share.

Our approach:

| What we do | Why |
|-----------|-----|
| **Publish cumulative metrics with methodology** | So users can verify our claims and judge our metrics |
| **Explain how we make money** | So users understand the business model and trust that free content isn't a bait-and-switch |
| **Define every metric precisely** | So numbers can't be inflated through vague definitions |
| **Keep raw GA4 data internal** | To protect user privacy, operational sensitivity, and prevent misinterpretation |
| **Offer detailed data privately on request** | So partners and funders can do proper due diligence |
| **Open-source our code** | So anyone can verify how the platform works technically |

We'd rather be a small platform with honest, verifiable numbers than a platform with impressive-sounding numbers that no one can check.

---

## Questions?

If something on the Transparency page seems unclear, inconsistent, or incomplete, tell us. Email [hello@impactmojo.in](mailto:hello@impactmojo.in) or open an issue on [GitHub](https://github.com/ImpactMojo/ImpactMojo/issues). Transparency works best when people actually scrutinise it.
