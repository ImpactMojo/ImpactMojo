# Glossary

A plain-language guide to technical terms you might encounter while using ImpactMojo or working with digital tools in development. Each definition is written for smart, experienced professionals who happen not to work in technology.

---

## A

### Accessibility (a11y)

The practice of designing websites, documents, and tools so they can be used by everyone — including people with visual impairments, hearing loss, motor disabilities, or cognitive differences. The abbreviation "a11y" is shorthand: the "a," then 11 letters, then "y."

**Why it matters for your work:** If you're creating training materials, reports, or digital content, accessibility ensures that nobody on your team or in your community is excluded. It also tends to make content better for *everyone* — clearer structure, better contrast, more readable text. ImpactMojo is built with accessibility in mind, following the WCAG guidelines (see below).

---

### API (Application Programming Interface)

A structured way for one piece of software to request information from another. When you visit a website, your browser is essentially using the site's API to fetch content. But the term usually refers to *data APIs* — services that let you request specific data (say, "India's infant mortality rate from 2015 to 2023") and get back exactly that, in a format a computer can work with.

**Why it matters for your work:** If you regularly need data from organizations like the World Bank, WHO, or the Indian Census, APIs let you pull exactly what you need without manually navigating websites and downloading files. Many APIs are free and have simple web-based interfaces — you don't need to write code to use them, though code makes them more powerful. The ImpactMojo [Dataverse](dataverse-guide.md) identifies which resources offer APIs.

---

## C

### CC BY-NC-ND 4.0

A Creative Commons license — specifically, **Attribution-NonCommercial-NoDerivatives 4.0 International**. This is the license that covers ImpactMojo's educational content (courses, handouts, games, labs).

Here's what each part means:

- **BY** — You must give credit to ImpactMojo when you share the content
- **NC (NonCommercial)** — You cannot sell the content or use it for commercial purposes
- **ND (NoDerivatives)** — You cannot modify the content and distribute the modified version

**What you *can* do:** Share handouts with your team, use courses in your training sessions, link to content from your website, print materials for workshops — all free, as long as you credit ImpactMojo and don't charge for it or alter it.

**What you *can't* do:** Sell printed copies, rebrand content as your own, or create modified versions for distribution.

**Why it matters for your work:** This license keeps ImpactMojo content free and consistent while still letting you use it widely in your programmes and teaching.

---

### CDN (Content Delivery Network)

A network of servers spread across many locations around the world. When you visit a website that uses a CDN, the content is served from whichever server is geographically closest to you, rather than from one central location that might be far away.

**Why it matters for your work:** This is why ImpactMojo pages load reasonably fast even on slower connections in rural areas of South Asia. Instead of every request traveling to a server in another country, the CDN delivers content from a nearby location. You don't need to do anything to benefit from this — it works automatically.

---

### CSV (Comma-Separated Values)

A simple file format for tabular data — like a spreadsheet, but stored as plain text. Each row is a line, and each column is separated by a comma. A CSV file can be opened in Excel, Google Sheets, or any data tool.

**Why it matters for your work:** CSV is the most universal format for sharing data. If someone sends you a dataset, there's a good chance it's a CSV. If you need to move data between systems (say, from a survey tool to a statistical programme), CSV is usually the common language they both speak. Most resources in the ImpactMojo Dataverse offer data in CSV format.

---

## E

### Edge Function

A small piece of code that runs on a server located geographically close to the person making a request, rather than on a central server that might be thousands of kilometres away. "Edge" refers to the edge of the network — the point closest to the user.

**Why it matters for your work:** ImpactMojo uses edge functions for certain features (like login and certificate generation) so they respond quickly regardless of where you are. If you're in Patna or Chittagong, the function runs on a nearby server rather than waiting for a round trip to a distant data centre. You won't see this happening — things just feel faster.

---

## G

### Git / GitHub

**Git** is a version control system — software that tracks every change made to a set of files over time. Think of it like "Track Changes" in Microsoft Word, but for entire projects with hundreds of files. Every change is recorded: who made it, when, and what exactly was altered. You can go back to any previous version at any time.

**GitHub** is a website where people store and share projects managed with Git. It's where ImpactMojo's code lives, and it's where contributors can suggest changes or report issues.

**Why it matters for your work:** If you want to contribute to ImpactMojo (translations, content, code), you'll interact with GitHub. Even if you don't contribute, understanding that ImpactMojo is on GitHub means you can see exactly how the platform is built — it's all public.

---

## H

### HTML / CSS / JavaScript

The three core technologies that make up every web page you visit:

- **HTML** (HyperText Markup Language) — The structure and content. It defines what's on the page: headings, paragraphs, images, links.
- **CSS** (Cascading Style Sheets) — The appearance. It defines how things look: colours, fonts, spacing, layouts.
- **JavaScript** — The behaviour. It makes pages interactive: quizzes that check your answers, charts that update, menus that open and close.

**Why it matters for your work:** ImpactMojo is built with these three technologies and nothing else on the frontend — no complex frameworks or build tools. This means it loads fast, works on any device, and can be served offline. If you ever want to understand how a feature works, viewing the page source will show you readable HTML, CSS, and JavaScript.

---

### HTTPS / SSH

Two protocols (methods) for secure communication over the internet:

- **HTTPS** (HyperText Transfer Protocol Secure) — The secure version of HTTP, the protocol your browser uses to load web pages. When you see the padlock icon in your browser's address bar, you're using HTTPS. It means the data traveling between your device and the website is encrypted — no one in between can read it.
- **SSH** (Secure Shell) — A protocol for securely connecting to and managing remote computers. Developers use it to access servers and push code to GitHub.

**Why it matters for your work:** ImpactMojo uses HTTPS for all connections, which means your login credentials, progress data, and personal information are encrypted in transit. This is especially important on public Wi-Fi networks in cafes, airports, or shared office spaces.

---

## J

### JWT (JSON Web Token)

A compact, secure token (a small piece of encoded data) that a website sends to your browser after you log in. Each time you navigate to a new page or request data, your browser sends this token back to prove that you're the person who logged in — without needing to send your password again.

**Think of it this way:** When you check into a hotel, you get a room key card. You don't show your ID every time you go to your room — you just tap the card. A JWT works the same way for websites.

**Why it matters for your work:** When you create an ImpactMojo account and log in, a JWT is what keeps you logged in as you move between pages. It's also what ensures that your progress, bookmarks, and certificates belong to *you* and not someone else. The token expires after a set period, so even if someone intercepted it, it wouldn't work for long.

---

## M

### MCP Server (Model Context Protocol)

A standardized way to connect AI assistants (like Claude) to external data sources and services. An MCP Server acts as a bridge: the AI assistant sends a request through the MCP connection, and the server retrieves real, current data from the connected source.

**Think of it this way:** Imagine your research assistant has a library card to a specific database. They can look up information for you without you needing to visit the library yourself. An MCP Server is that library card — it gives an AI assistant authorized access to a specific data source.

**Why it matters for your work:** As AI tools become more common in development research, MCP Servers let you access reliable, official data through natural conversation. Instead of navigating a complex government data portal, you can ask your AI assistant a question and get actual data back. The ImpactMojo [Dataverse](dataverse-guide.md) lists MCP Servers available for development data.

---

## N

### Netlify

A web hosting platform — the service that serves ImpactMojo's website to your browser. When you visit impactmojo.in, Netlify is the infrastructure that delivers the pages.

**Think of it this way:** If ImpactMojo is a library, Netlify is the building the library is housed in. It handles the physical delivery of pages, keeps the site available around the clock, and manages things like HTTPS security and fast loading through its CDN.

**Why it matters for your work:** You'll almost never need to think about Netlify directly. But if you notice the site is loading fast, staying available, and working well on mobile — that's partly Netlify's infrastructure at work. Contributors to ImpactMojo also benefit because Netlify makes deployment straightforward: changes to the code are automatically reflected on the live site.

---

## O

### Open Badges

A W3C (World Wide Web Consortium) standard for **verifiable digital certificates and credentials**. An Open Badge is a digital image that contains embedded metadata — who earned it, who issued it, what criteria were met, and when. This metadata can be independently verified by anyone.

**Think of it this way:** A paper certificate can be photocopied or fabricated. An Open Badge is like a certificate with a built-in verification system — anyone can click on it and confirm that it's genuine.

**Why it matters for your work:** When you complete an ImpactMojo course and earn a certificate, it's issued as an Open Badge. You can share it on LinkedIn, include it in a CV, or show it to your organization — and anyone who clicks on it can verify that you actually completed the course. This is especially useful for professional development reporting and HR records.

---

### Open Source

Software whose source code (the underlying instructions that make it work) is publicly available for anyone to read, study, and learn from. Open-source projects usually also allow anyone to suggest improvements, report bugs, and contribute.

**Why it matters for your work:** ImpactMojo's code is open source (available on GitHub under the MIT license). This means: you can see exactly how the platform works; you can verify there's nothing hidden or problematic; the community can contribute improvements; and other organizations can learn from the approach. The *educational content* has a different license (CC BY-NC-ND 4.0), but the *code* is fully open.

---

## P

### PWA (Progressive Web App)

A website that can behave like an app installed on your phone or computer. A PWA can work offline, send notifications, load quickly on slow connections, and be added to your home screen — all without being downloaded from an app store.

**Why it matters for your work:** ImpactMojo is built as a PWA. This means you can use it in areas with unreliable internet: content you've previously loaded is cached (saved locally) and available offline. You can also add ImpactMojo to your phone's home screen for quick access, just like a regular app — but without taking up much storage space or requiring updates from the app store.

---

## R

### Responsive Design

A web design approach where pages automatically adjust their layout based on the screen size of the device viewing them. The same page looks different (but equally usable) on a phone, a tablet, and a desktop monitor.

**Why it matters for your work:** Many development practitioners access ImpactMojo on mobile phones — sometimes the phone is their primary device, sometimes they're in the field and it's what they have. Responsive design means every course, handout, lab, and game works on whatever device you're using. You don't need a laptop to learn or facilitate.

---

## S

### Skill (Claude AI Context)

In the context of AI assistants like Claude, a **Skill** is a pre-built command that performs a specific, structured task. You invoke a skill by typing a command (like "/analyze-program"), and the AI runs through a defined sequence of steps — asking questions, retrieving data, structuring an analysis.

**Think of it this way:** A skill is like a recipe. Instead of starting from scratch every time you want to evaluate a programme or review literature, you invoke a skill that guides you through the process step by step.

**Why it matters for your work:** ImpactMojo is developing custom Skills for development research tasks — programme evaluation, evidence review, indicator analysis, and more. These are designed to make AI tools practical and accessible for practitioners who don't have a background in prompt engineering. The [Dataverse](dataverse-guide.md) lists available skills.

---

### South Asian Context

A deliberate design choice in ImpactMojo to use examples, case studies, data, and scenarios drawn from **India, Bangladesh, Nepal, Sri Lanka**, and the broader South Asian region.

**Why it matters for your work:** Most online learning platforms for development use examples from East Africa, Latin America, or the Global North. These are valuable, but they don't always resonate with practitioners working in South Asian settings — where governance structures, social dynamics, data systems, and programme modalities have their own characteristics. ImpactMojo's content is built for people who work in this region and need materials that reflect the realities they encounter daily. When a course discusses a vaccination programme, it references India's Universal Immunization Programme, not a generic hypothetical.

---

### Supabase

An open-source platform that provides database, authentication (login), and storage services for web applications. It's the backend infrastructure that stores and manages ImpactMojo's user data.

**Think of it this way:** If the ImpactMojo website is the building you walk into, Supabase is the filing system behind the counter — it stores your account information, remembers which courses you've completed, holds your bookmarks, and manages your certificates.

**Why it matters for your work:** You'll never interact with Supabase directly. But when you create an account, log in, track your course progress, or earn a certificate — Supabase is what makes that work. It's also open source, which means there's no proprietary lock-in: your data could be moved to another system if needed.

---

## W

### WCAG (Web Content Accessibility Guidelines)

A set of international standards, developed by the World Wide Web Consortium (W3C), that define how to make web content accessible to people with disabilities. WCAG covers things like colour contrast (so text is readable for people with low vision), keyboard navigation (so people who can't use a mouse can still navigate), and alternative text for images (so screen readers can describe images to blind users).

**Why it matters for your work:** ImpactMojo follows WCAG guidelines to ensure that its courses, handouts, and tools are usable by everyone. If you're creating your own digital materials — websites, PDFs, presentations — WCAG is the standard to aim for. It's organized into three levels: A (minimum), AA (recommended), and AAA (ideal). Most organizations target AA.
