# PolicyDhara Guide

## What Is PolicyDhara?

PolicyDhara is a **curated collection of Indian public policy documents, government schemes, and legislative frameworks**, built for development practitioners and researchers. It gathers the source material of Indian policy (the schemes, laws, and frameworks that shape development work) into one browsable, **open-access** place.

PolicyDhara is **free and browser-based**. It opens directly on the page at [https://policydhara.impactmojo.in/](https://policydhara.impactmojo.in/): no login, no download.

---

## What's in the Collection

PolicyDhara is organised around the documents practitioners actually reach for:

- **Policy documents**: the frameworks and official texts that set the direction of Indian public policy.
- **Government schemes**: the programmes through which policy is delivered on the ground.
- **Legislative frameworks**: the laws and statutory instruments that underpin it all.

Browse the collection at [https://policydhara.impactmojo.in/](https://policydhara.impactmojo.in/).

---

## How it works

PolicyDhara is a standalone **Astro application**, built and published separately on GitHub Pages at its own address, [policydhara.impactmojo.in](https://policydhara.impactmojo.in/).

Until October 2026 ImpactMojo showed it inside the main site at `impactmojo.in/policydhara`, through a Netlify Edge Function. It now has its own subdomain, as the Climate TRACE and SDG dashboards do, and the old address redirects there, so existing links and bookmarks still work.

---

## Why it has its own address

A page served on www.impactmojo.in runs alongside members' sign-in sessions. Giving PolicyDhara its own subdomain keeps its code apart from those sessions, with no proxy in between to maintain. It also loads straight from its host, so a new PolicyDhara deploy is visible as soon as GitHub Pages publishes it.

---

## Who It's For

PolicyDhara is aimed at **development practitioners and researchers** who need to ground their work in primary policy sources: anyone building a course, writing a brief, designing a programme, or checking what a scheme or framework actually says. It complements ImpactMojo's other reference tools by covering the Indian public-policy landscape specifically.

---

## Related

- [BCT Repository Guide](bct-repository-guide.md): behaviour-change technique reference for practitioners.
- [Reading Companions Guide](book-summaries-guide.md): interactive companions to key development texts.
- [Deep Dives Guide](deep-dives-guide.md): long-form research explainers.
