# Typography

## Font Stack

ImpactMojo uses a standardized three-font system across all 242+ pages:

| Role | Font | Weights | Fallback |
|------|------|---------|----------|
| **Headings** | Inter | 400, 500, 600, 700, 800 | sans-serif |
| **Body text** | Amaranth | 400, 700 | sans-serif |
| **Code / monospace** | JetBrains Mono | 400 | monospace |
| **Multilingual** | Noto Sans (Devanagari, Bengali, Tamil, Telugu) | 400, 700 | sans-serif |

## Google Fonts Loading

All pages load fonts via a single Google Fonts URL:

```html
<link href="https://fonts.googleapis.com/css2?family=Amaranth:wght@400;700&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono&family=Noto+Sans:wght@400;700&display=swap" rel="stylesheet">
```

## Design Tokens

### Font Families

```css
--font-heading: 'Inter', sans-serif;
--font-body: 'Amaranth', sans-serif;
--font-mono: 'JetBrains Mono', monospace;
```

### Font Sizes

| Token | Size | Usage |
|-------|------|-------|
| `--text-xs` | 0.75rem | Labels, captions |
| `--text-sm` | 0.875rem | Secondary text, metadata |
| `--text-base` | 1rem | Body text |
| `--text-lg` | 1.125rem | Lead paragraphs |
| `--text-xl` | 1.25rem | Section headings (h3) |
| `--text-2xl` | 1.5rem | Page headings (h2) |
| `--text-3xl` | 1.875rem | Hero headings (h1) |

### Font Weights

| Token | Weight | Usage |
|-------|--------|-------|
| `--font-normal` | 400 | Body text |
| `--font-medium` | 500 | Navigation, buttons |
| `--font-semibold` | 600 | Subheadings |
| `--font-bold` | 700 | Headings, emphasis |
| `--font-extrabold` | 800 | Hero text |

## Encoding

All HTML files use UTF-8 encoding:

```html
<meta charset="UTF-8">
```

This ensures correct rendering of:
- Hindi (हिन्दी), Bengali (বাংলা), Tamil (தமிழ்), Telugu (తెలుగు)
- Special characters in academic content (em-dashes, smart quotes, etc.)

## Previous Fonts (Removed in v10.0.0)

The following fonts were removed during the v10.0.0 typography standardization:

- Poppins (replaced by Inter for headings)
- Fraunces (removed)
- Merriweather (removed)
- Source Serif 4 (removed)
- Source Sans 3 (removed)
- Cormorant Garamond (removed)
- Georgia (removed from fallback chains)
