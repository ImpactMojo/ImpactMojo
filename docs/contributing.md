# Contributing to ImpactMojo

Thank you for your interest in contributing! Whether you're fixing a broken link, translating content, or building a new tool, every contribution matters.

## Ways to Contribute

| Area | Examples | Difficulty |
|------|----------|------------|
| **Content** | Improve courses, add case studies, fix errors | Easy |
| **Translations** | Hindi, Tamil, Bengali, Telugu, Marathi | Easy–Medium |
| **Accessibility** | WCAG compliance, screen reader, keyboard nav | Medium |
| **Bug fixes** | Broken links, layout issues, JS errors | Easy–Medium |
| **Design** | UI/UX improvements, mobile experience | Medium |
| **Tools & Labs** | Build or improve interactive learning tools | Hard |
| **Games** | New economics simulations | Medium–Hard |

## Getting Started

```bash
# 1. Fork and clone
git clone https://github.com/<your-username>/ImpactMojo.git
cd ImpactMojo

# 2. Start local server
python -m http.server 8000
# or: npx http-server

# 3. Create a branch
git checkout -b feature/your-feature-name

# 4. Make changes, test locally

# 5. Commit and push
git commit -m "Add: descriptive summary"
git push origin feature/your-feature-name

# 6. Open a Pull Request on GitHub
```

## Commit Message Style

| Prefix | Use for |
|--------|---------|
| `Add:` | New feature, course, or tool |
| `Fix:` | Bug fix or broken link |
| `Update:` | Improvement to existing content or code |
| `Translate:` | Translation work |
| `Docs:` | Documentation changes |

## Code Style

This is a vanilla HTML/CSS/JS project. No build step.

- Semantic HTML where possible
- `const`/`let` over `var`
- Readable code over clever code
- No external JS frameworks
- CSS in `<style>` blocks or external files

## Pull Request Guidelines

- Keep PRs focused — one feature or fix per PR
- Test on desktop and mobile
- Include screenshots for visual changes
- Note if changes affect premium features

## Reporting Issues

Use [GitHub Issues](https://github.com/Varnasr/ImpactMojo/issues) with the appropriate template:
- **Bug Report** — broken links, layout issues, JS errors
- **Feature Request** — new ideas and improvements
- **Content Issue** — errors or outdated information

## Community Channels

- [WhatsApp PLC](https://chat.whatsapp.com/EsBjbKaQfupG1HbtajTjHM) — Peer discussions
- [Discord](https://discord.gg/M3ZCmUe7ab) — Tech tinkering
- [Telegram](https://t.me/impactmojo) — Free resources
- [GitHub Discussions](https://github.com/Varnasr/ImpactMojo/discussions) — Ideas & Q&A
