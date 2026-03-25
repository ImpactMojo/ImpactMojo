# Recommended MCP Servers for ImpactMojo

MCP servers extend Claude's capabilities with external tools and data access. Add these via `claude mcp add` or your Claude Code settings.

## Currently Active

These MCP servers are already connected in this workspace:

| Server | Purpose |
|--------|---------|
| **GitHub** | PRs, issues, code search, reviews |
| **Notion** | Project documentation and knowledge base |
| **Gmail** | Email drafts and search |
| **Google Calendar** | Event management and scheduling |
| **Figma** | Design-to-code workflows |
| **Canva** | Design creation and export |

## Recommended Additions

### Tavily MCP — AI-Native Search
Search engine optimized for AI agents. Returns structured results ideal for research tasks.

```bash
claude mcp add tavily -- npx -y tavily-mcp@latest
```
Requires: `TAVILY_API_KEY` (free tier: 1,000 searches/month)
- Source: https://github.com/tavily-ai/tavily-mcp
- Use case: Deep research for blog posts, course content, Threads posts

### Context7 MCP — Library Documentation
Injects current library docs into context. Eliminates hallucinated APIs.

```bash
claude mcp add context7 -- npx -y @upstash/context7-mcp@latest
```
No API key required (free).
- Source: https://github.com/upstash/context7
- Use case: When writing code that uses external libraries

### Task Master AI — Project Management
AI-powered task breakdown, dependency tracking, and project planning.

```bash
claude mcp add taskmaster -- npx -y task-master-ai@latest
```
Requires: `ANTHROPIC_API_KEY`
- Source: https://github.com/eyaltoledano/claude-task-master
- Use case: Planning complex multi-step features, sprint planning

## Setup Instructions

1. Run the `claude mcp add` command for each server
2. Set required environment variables in `.claude/.env.keys`
3. Restart Claude Code session
4. Verify with `claude mcp list`

## Notes
- MCP servers run as separate processes alongside Claude Code
- Each server adds tools that Claude can invoke during conversations
- Free tiers are sufficient for ImpactMojo's usage patterns
- See `data/dataverse.json` for the full catalog of 260+ tools and data sources

## Community Resources

Curated skills, MCP servers, and repos worth tracking (sourced from [@zodchiii's roundup](https://x.com/i/status/2034924354337714642)):

### GitHub Repos to Watch
- [anthropics/skills](https://github.com/anthropics/skills) — Official Anthropic skills repository
- [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) — Curated community skills (22k+ stars)
- [anthropics/claude-code-security-review](https://github.com/anthropics/claude-code-security-review) — Security review skill
- [199-biotechnologies/claude-deep-research-skill](https://github.com/199-biotechnologies/claude-deep-research-skill) — Deep research patterns
- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) — Prompt/output testing
- [mendableai/firecrawl](https://github.com/mendableai/firecrawl) — Web scraping for content research
- [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) — AI project management

### Notable Community Skills
- **Frontend Design** (277k+ installs) — UI generation patterns
- **Claude SEO** (12 sub-skills) — Search optimization
- **Systematic Debugging** — Structured troubleshooting
- **Context Optimization** — Better context window usage
- Browse more at [skillsmp.com](https://skillsmp.com)
