# Narration prompts — The Heat Floor

Two narration tracks. **Do not call any TTS API without explicit user confirmation** — these are configs, not generations.

---

## Track A — English (ElevenLabs)

```yaml
provider: elevenlabs
voice_id: <choose: "Adam" / "Daniel" / "Charlotte" — pick one with a calm, explanatory register, NOT a hype YouTuber voice>
model: eleven_multilingual_v2
voice_settings:
  stability: 0.55          # higher than default — explanatory, not theatrical
  similarity_boost: 0.75
  style: 0.20              # low style — we are not performing
  use_speaker_boost: true
output_format: mp3_44100_192
```

**Style notes for the voice prompt block:**

> Calm, paced, explanatory. ImpactMojo voice is a senior researcher walking you through the numbers, not a podcaster trying to keep you engaged. Slow down on the three numbers (259 billion, 17 times, 16 percent / 19 percent) — let each one land for half a beat before moving on. No upspeak. No dramatic music swells. The argument is the show.

**Pacing target:** ~130 wpm. Total runtime ≈ 8:50 for the script as written.

**Pronunciation guides (give to ElevenLabs as the script's first pass):**
- "Somanathan" → so-MA-na-tan
- "Sudarshan" → su-DAR-shan
- "PLI" → pee-ell-eye (spell the letters)
- "wet-bulb" → wet-bulb (slight hyphen pause)
- "MGNREGA" → em-jee-NREG-a

---

## Track B — Hindi / Regional (Sarvam AI — preferred for South Asia)

Use the `sarvam-ai` skill. Sarvam outperforms ElevenLabs on South Asian phonetics and is project-aligned (already in our key registry).

```yaml
provider: sarvam
endpoint: https://api.sarvam.ai/text-to-speech
model: bulbul:v1
target_languages:
  - hi-IN   # Hindi
  - bn-IN   # Bengali (post-LDC Bangladesh framing)
  - ta-IN   # Tamil (the Nature paper's South India focus)
voice:
  speaker: "meera"        # warm, mid-register, professional
  pitch: 0
  pace: 1.0
  loudness: 1.0
sample_rate: 22050
enable_preprocessing: true
```

**Translation note:** the script as written is in English. For Hindi/Bengali/Tamil dubs, translate via a human reviewer — auto-translation will mangle the technical terms (wet-bulb temperature, parametric insurance, PLI). Estimated translation review time: 90 min per language.

**Numbers to keep in numerals:** 6.3%, 7%, 17×, 259 billion, 16%, 19%, 40%. Sarvam handles digit pronunciation in-language correctly, so don't spell them out.

---

## Output paths (when generated)

```
audio/
  en-elevenlabs.mp3
  hi-sarvam.mp3
  bn-sarvam.mp3
  ta-sarvam.mp3
```

## Cost guard

- ElevenLabs: ~1,150 words ≈ $0.20–$0.40 per render at standard tier
- Sarvam: ~$0.02–$0.05 per minute of audio (4 languages × ~9 min ≈ $1.50)

**Total estimated cost: under $2.50.** Still requires user confirmation before any API call.
