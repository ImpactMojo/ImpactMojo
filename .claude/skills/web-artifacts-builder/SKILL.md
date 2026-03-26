---
description: "Build interactive calculators, dashboards, simulators, and tools as self-contained HTML pages. Use when the user asks to create a new lab tool, BookCompanionTool, calculator, data explorer, interactive widget, or any standalone browser-based utility for ImpactMojo."
---

# Web Artifacts Builder — ImpactMojo Edition

Build self-contained interactive HTML tools that run entirely in the browser with zero dependencies.

## When to Use

- User asks for a **calculator** (sample size, budget, cost-effectiveness)
- User asks for a **simulator** (targeting, transfer size, cost-benefit)
- User asks for a **data explorer** (chart builder, dataset browser)
- User asks for a **dashboard** (progress tracker, analytics view)
- User asks for a **new lab tool** or **BookCompanionTool**
- User wants to **prototype an interactive widget**

## Output Format

Every artifact is a **single self-contained HTML file** with inline CSS and JS. No external dependencies, no build step, no npm.

```html
<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{Tool Name} — ImpactMojo</title>
    <link href="https://fonts.googleapis.com/css2?family=Amaranth:wght@400;700&family=Inter:wght@600;700&family=JetBrains+Mono&display=swap" rel="stylesheet">
    <style>
        /* ImpactMojo brand variables — see brand-guidelines skill */
        :root { ... }
        /* All styles inline */
    </style>
</head>
<body>
    <!-- Sticky top bar -->
    <!-- Main content -->
    <!-- Floating paper plane -->
    <!-- 4-section footer -->
    <script>
        // All logic inline
        // Theme toggle with localStorage
    </script>
</body>
</html>
```

## Architecture Patterns

### 1. Calculator Pattern
For tools that take inputs and produce a computed result.

```
┌─────────────────────────────────┐
│  Title + Description            │
├─────────────────────────────────┤
│  Input Panel                    │
│  ┌───────┐ ┌───────┐ ┌───────┐│
│  │ Field │ │ Field │ │ Field ││
│  └───────┘ └───────┘ └───────┘│
│  [Calculate Button]            │
├─────────────────────────────────┤
│  Results Panel                  │
│  • Primary result (large)       │
│  • Supporting metrics           │
│  • Interpretation text          │
├─────────────────────────────────┤
│  Methodology / Assumptions     │
└─────────────────────────────────┘
```

**Use for:** Sample size calculators, cost-effectiveness analysis, budget estimators, statistical power analysis.

### 2. Explorer Pattern
For tools that let users browse, filter, and visualize data.

```
┌─────────────────────────────────┐
│  Title + Description            │
├──────────┬──────────────────────┤
│ Filters  │  Data Display        │
│ □ Cat A  │  ┌─────┐ ┌─────┐   │
│ □ Cat B  │  │Card │ │Card │   │
│ □ Cat C  │  └─────┘ └─────┘   │
│ Search:  │  ┌─────┐ ┌─────┐   │
│ [______] │  │Card │ │Card │   │
│          │  └─────┘ └─────┘   │
├──────────┴──────────────────────┤
│  Detail view / chart            │
└─────────────────────────────────┘
```

**Use for:** Dataset browsers, indicator banks, case study finders, tool comparisons.

### 3. Simulator Pattern
For tools where users adjust parameters and see real-time results.

```
┌─────────────────────────────────┐
│  Title + Scenario Description   │
├─────────────────────────────────┤
│  Parameter Sliders              │
│  Budget: ──●────── ₹50,000     │
│  Coverage: ────●─── 60%         │
│  Duration: ─●────── 6 months   │
├─────────────────────────────────┤
│  Live Visualization             │
│  [Chart / Graph / Table]        │
│  Updates in real-time           │
├─────────────────────────────────┤
│  Scenario Comparison            │
│  [Save Scenario] [Compare]     │
└─────────────────────────────────┘
```

**Use for:** SP spending explorers, targeting simulators, transfer size calculators, policy impact models.

### 4. Step-by-Step Builder Pattern
For tools that guide users through a workflow to produce an output.

```
┌─────────────────────────────────┐
│  Step 1 of 5: Define Objective  │
│  ━━━━━━━━━░░░░░░░░░░░ 20%      │
├─────────────────────────────────┤
│  Instructions + Context         │
│                                 │
│  Input Fields / Choices         │
│                                 │
│  [← Back]          [Next →]    │
├─────────────────────────────────┤
│  Tips / Examples sidebar        │
└─────────────────────────────────┘
```

**Use for:** Theory of Change builder, research question builder, MEL plan builder, survey instrument designer.

## Charting (No Dependencies)

Use **Canvas API** for charts — no Chart.js, no D3. ImpactMojo uses lightweight custom canvas charts:

```javascript
function drawBarChart(canvas, data, options) {
    const ctx = canvas.getContext('2d');
    // HiDPI support
    const dpr = window.devicePixelRatio || 1;
    canvas.width = canvas.clientWidth * dpr;
    canvas.height = canvas.clientHeight * dpr;
    ctx.scale(dpr, dpr);
    // Draw with brand colors
}
```

For smooth line charts, use **Catmull-Rom splines** (see admin dashboard pattern).

## Data Handling

- **Static data**: Embed JSON directly in `<script>` tags
- **User input**: Store in `localStorage` for session persistence
- **Export**: Offer "Copy as Text" or "Download CSV" — no server needed
- **PDF export**: Use `window.print()` with `@media print` styles

## Interaction Design

- **Instant feedback**: Update results on `input` event, not just on button click
- **Sensible defaults**: Pre-fill inputs with realistic South Asian development context values
- **Units**: Use ₹ (INR) for currency, lakhs/crores for large numbers
- **Tooltips**: Explain jargon inline — assume user is a practitioner, not a data scientist
- **Mobile-first**: Inputs stack vertically on mobile, side-by-side on desktop

## File Placement

| Type | Path |
|------|------|
| BookCompanionTool | `/BookCompanionTools/{tool-name}.html` |
| Lab tool | `/Labs/{tool-name}-lab.html` |
| Standalone calculator | `/tools/{tool-name}.html` |

## Checklist

Before delivering an artifact:

- [ ] Single HTML file, no external dependencies
- [ ] ImpactMojo brand applied (fonts, colors, topbar, footer, paper plane)
- [ ] Theme toggle (System/Light/Dark) with localStorage
- [ ] Responsive — works on mobile (test at 375px width)
- [ ] Accessible — keyboard navigable, contrast ratios met
- [ ] Viewport meta tag present
- [ ] `<title>` set to `{Tool Name} — ImpactMojo`
- [ ] Sensible defaults in all inputs
- [ ] Export option available (copy/download/print)
- [ ] Reduced-motion respected for animations
