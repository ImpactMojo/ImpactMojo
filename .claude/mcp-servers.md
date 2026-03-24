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
