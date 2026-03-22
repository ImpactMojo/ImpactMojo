---
name: deepseek-ai
description: DeepSeek API operations — generate content, reason over code and data via $DEEPSEEK_API_KEY. Use when the user asks to call DeepSeek, needs code generation, or wants an alternative LLM provider.
---

# DeepSeek AI Skill

Use the DeepSeek API via `$DEEPSEEK_API_KEY` for AI content and code generation. DeepSeek uses an OpenAI-compatible API format.

## Authentication

```
Authorization: Bearer $DEEPSEEK_API_KEY
```

Base URL: `https://api.deepseek.com/v1`

## Available Models

- `deepseek-chat` — General-purpose chat (DeepSeek-V3)
- `deepseek-reasoner` — Chain-of-thought reasoning (DeepSeek-R1)

## Capabilities

### Chat Completion
```bash
curl -s -X POST "https://api.deepseek.com/v1/chat/completions" \
  -H "Authorization: Bearer $DEEPSEEK_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-chat",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Your prompt here"}
    ]
  }'
```

### Reasoning (Chain-of-Thought)
```bash
curl -s -X POST "https://api.deepseek.com/v1/chat/completions" \
  -H "Authorization: Bearer $DEEPSEEK_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-reasoner",
    "messages": [{"role": "user", "content": "Solve this step by step: ..."}]
  }'
```

### With JSON Output
```bash
curl -s -X POST "https://api.deepseek.com/v1/chat/completions" \
  -H "Authorization: Bearer $DEEPSEEK_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "Return JSON: ..."}],
    "response_format": {"type": "json_object"}
  }'
```

## ImpactMojo Use Cases
- Code generation for game and lab HTML/JS
- Reasoning tasks for evaluation framework design
- Cross-validate content against multiple LLM providers
- Generate structured JSON for data files (search-index, catalog)

## Best Practices
- Use `deepseek-chat` for general tasks, `deepseek-reasoner` for complex reasoning
- API follows OpenAI chat completions format — same structure as Grok
- DeepSeek-R1 returns reasoning in `reasoning_content` field
- Handle rate limits with exponential backoff
- Never commit `$DEEPSEEK_API_KEY` to the repository
