---
name: grok-ai
description: Grok (xAI) API operations — generate content, reason over data, and use AI features via $GROK_API_KEY. Use when the user asks to call Grok, use xAI capabilities, or needs an alternative LLM provider.
---

# Grok AI Skill

Use the Grok API via `$GROK_API_KEY` for AI content generation. Grok uses an OpenAI-compatible API format.

## Authentication

```
Authorization: Bearer $GROK_API_KEY
```

Base URL: `https://api.x.ai/v1`

## Available Models

- `grok-3` — Latest, most capable
- `grok-3-mini` — Fast, lightweight
- `grok-2` — Previous generation

## Capabilities

### Chat Completion
```bash
curl -s -X POST "https://api.x.ai/v1/chat/completions" \
  -H "Authorization: Bearer $GROK_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "grok-3",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Your prompt here"}
    ]
  }'
```

### With Temperature/Max Tokens
```bash
curl -s -X POST "https://api.x.ai/v1/chat/completions" \
  -H "Authorization: Bearer $GROK_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "grok-3",
    "messages": [{"role": "user", "content": "Your prompt"}],
    "temperature": 0.7,
    "max_tokens": 4096
  }'
```

### List Models
```bash
curl -s "https://api.x.ai/v1/models" \
  -H "Authorization: Bearer $GROK_API_KEY"
```

## ImpactMojo Use Cases
- Alternative LLM for content generation and review
- Cross-validate AI-generated course content against multiple providers
- Generate quiz questions and assessment items
- Summarize research papers for DevDiscourses

## Best Practices
- Use `grok-3-mini` for speed, `grok-3` for quality
- API follows OpenAI chat completions format — same structure as DeepSeek
- Handle rate limits with exponential backoff
- Never commit `$GROK_API_KEY` to the repository
