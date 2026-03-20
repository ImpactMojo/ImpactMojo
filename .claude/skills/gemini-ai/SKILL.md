---
name: gemini-ai
description: Google Gemini AI API operations — generate content, manage models, and use AI features via $GEMINI_API_KEY. Use when the user asks to call Gemini, generate AI content, or use Google AI Studio capabilities.
---

# Gemini AI Skill

Use the Google Gemini API via `$GEMINI_API_KEY` for AI content generation, embeddings, and model management.

## Authentication

API key passed as query parameter:
```
?key=$GEMINI_API_KEY
```

Base URL: `https://generativelanguage.googleapis.com/v1beta`

## Available Models

- `gemini-2.0-flash` — Fast, versatile (recommended default)
- `gemini-2.0-pro` — Highest quality reasoning
- `gemini-1.5-flash` — Lightweight, fast
- `gemini-1.5-pro` — Long context (up to 2M tokens)
- `gemini-embedding-001` — Text embeddings

## Capabilities

### Generate Content
```bash
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"parts": [{"text": "Your prompt here"}]}]
  }'
```

### Generate with System Instruction
```bash
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "system_instruction": {"parts": [{"text": "You are a helpful assistant"}]},
    "contents": [{"parts": [{"text": "User message"}]}]
  }'
```

### Streaming
```bash
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:streamGenerateContent?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"parts": [{"text": "Your prompt"}]}]
  }'
```

### Embeddings
```bash
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-001:embedContent?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "content": {"parts": [{"text": "Text to embed"}]}
  }'
```

### List Models
```bash
curl -s "https://generativelanguage.googleapis.com/v1beta/models?key=$GEMINI_API_KEY"
```

## Advanced Options

### Generation Config
```json
{
  "generationConfig": {
    "temperature": 0.7,
    "topP": 0.95,
    "topK": 40,
    "maxOutputTokens": 8192,
    "responseMimeType": "application/json"
  }
}
```

### Safety Settings
```json
{
  "safetySettings": [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_ONLY_HIGH"}
  ]
}
```

## Common Use Cases for ImpactMojo
- Generate course content summaries
- Create quiz questions from educational material
- Translate content for South Asian languages
- Generate embeddings for semantic search
- AI-powered game agent decisions (fallback provider)

## Best Practices
- Use `gemini-2.0-flash` for speed, `gemini-2.0-pro` for quality
- Set `responseMimeType: "application/json"` when you need structured output
- Handle rate limits with exponential backoff
- Never commit `$GEMINI_API_KEY` to the repository
