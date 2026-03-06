# Security Policy

## Supported Versions

ImpactMojo is a static website deployed on Netlify. The `main` branch always reflects the live production site.

| Version | Supported |
|---------|-----------|
| `main` branch (current) | Yes |
| Older commits | No |

## Reporting a Vulnerability

If you discover a security vulnerability, please report it responsibly:

1. **Do not** open a public GitHub issue
2. **Email** security concerns to **hello@impactmojo.in** with the subject line "Security: [brief description]"
3. Include steps to reproduce, impact assessment, and any suggested fixes

We will acknowledge your report within 48 hours and aim to resolve critical issues within 7 days.

## Scope

Security concerns relevant to this project include:

- XSS vulnerabilities in client-side JavaScript
- Authentication or authorization bypasses (Supabase integration)
- Exposure of API keys or secrets
- Open redirect vulnerabilities
- Issues with the JWT token-gating system

## Out of Scope

- Denial of service attacks
- Social engineering
- Issues in third-party services (Supabase, Netlify, Formspree) — report these to the respective providers
