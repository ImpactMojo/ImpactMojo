---
name: sarvam-ai
description: Sarvam AI API operations — transcription, translation, and text-to-speech for South Asian languages via $SARVAM_API_KEY. Use when the user asks about VaniScribe, transcription, South Asian language processing, or Sarvam AI features.
---

# Sarvam AI Skill

Use the Sarvam AI API via `$SARVAM_API_KEY` for South Asian language processing — transcription (Saaras), translation (Mayura), and text-to-speech (Bulbul).

## Authentication

```
api-subscription-key: $SARVAM_API_KEY
```

Base URL: `https://api.sarvam.ai`

## Available Models

- **Saaras** — Speech-to-text (ASR) for 10+ South Asian languages
- **Mayura** — Translation across Indian languages
- **Bulbul** — Text-to-speech in Indian languages

## Capabilities

### Speech-to-Text (Transcription)
```bash
curl -s -X POST "https://api.sarvam.ai/speech-to-text-translate" \
  -H "api-subscription-key: $SARVAM_API_KEY" \
  -F "file=@audio.wav" \
  -F "model=saaras:v2" \
  -F "language_code=hi-IN"
```

Supported languages: `hi-IN`, `bn-IN`, `ta-IN`, `te-IN`, `mr-IN`, `gu-IN`, `kn-IN`, `ml-IN`, `pa-IN`, `od-IN`, `en-IN`

### Translation
```bash
curl -s -X POST "https://api.sarvam.ai/translate" \
  -H "api-subscription-key: $SARVAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input": "Text to translate",
    "source_language_code": "en-IN",
    "target_language_code": "hi-IN",
    "model": "mayura:v1"
  }'
```

### Text-to-Speech
```bash
curl -s -X POST "https://api.sarvam.ai/text-to-speech" \
  -H "api-subscription-key: $SARVAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "inputs": ["Text to speak"],
    "target_language_code": "hi-IN",
    "model": "bulbul:v1"
  }' --output speech.wav
```

## ImpactMojo Use Cases
- **VaniScribe**: Transcribe field interviews, FGDs, and KIIs in South Asian languages
- **Course translation**: Translate course content into 6 supported languages
- **Audio content**: Generate audio versions of handouts and course summaries
- **Speaker diarization**: Identify speakers in multi-participant recordings

## Integration with VaniScribe

VaniScribe (premium tool at `101.impactmojo.in/vaniscribe`) uses Sarvam's Saaras v3 for:
- Field interview transcription in 10+ languages
- Speaker diarization and auto-timestamping
- Export to structured formats for qualitative analysis

## Best Practices
- Use `saaras:v2` for transcription, `mayura:v1` for translation
- Audio files should be WAV or MP3, under 25MB
- Specify the correct `language_code` for best accuracy
- Handle rate limits with exponential backoff
- Never commit `$SARVAM_API_KEY` to the repository
