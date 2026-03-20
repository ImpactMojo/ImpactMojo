---
name: gamma-ops
description: Gamma API operations — manage presentations, decks, and content generation using $GAMMA_API_KEY. Use when the user asks to create presentations, sync course content to Gamma, or manage Gamma decks.
---

# Gamma Operations Skill

Use the Gamma API via `$GAMMA_API_KEY` to create and manage AI-generated presentations and documents.

## Authentication

```
Authorization: Bearer $GAMMA_API_KEY
```

Base URL: `https://public-api.gamma.app/v1.0`

## Capabilities

### Folders
- List folders: `GET /folders`
- Create folder: `POST /folders`

### Cards (Presentations/Docs)
- List cards: `GET /cards`
- Get card: `GET /cards/{id}`
- Create card: `POST /cards/generate`
- Update card: `PATCH /cards/{id}`
- Delete card: `DELETE /cards/{id}`

## Generate a Presentation

```bash
curl -s -X POST \
  "https://public-api.gamma.app/v1.0/cards/generate" \
  -H "Authorization: Bearer $GAMMA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Presentation Title",
    "content": "Source content or outline",
    "folder_id": "optional-folder-id"
  }'
```

## ImpactMojo Use Cases
- Regenerate 101 courses as Gamma presentation decks
- Sync course content from the platform to Gamma for visual delivery
- Create training materials with Indian folk art themes
- Generate handouts and workshop materials

## Existing Integration
See `/scripts/gamma-sync.js` for the existing Gamma sync pipeline that:
- Reads course content from the platform
- Creates/updates Gamma presentations per course
- Manages folder organization
- Handles theme and art style configuration

## Best Practices
- Use folder organization to separate course categories
- Check for existing cards before creating duplicates
- Handle rate limits gracefully
- Never commit `$GAMMA_API_KEY` to the repository
