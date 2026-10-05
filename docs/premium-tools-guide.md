# Pro Studio guide

## What Pro Studio is

Pro Studio is ImpactMojo's set of 13 browser tools for research and evaluation work. Each one runs in the page: you open it, build something, and take the result away. The tools live under `/premium-tools/` (the folder keeps its old name so existing links still work) and the front door is [impactmojo.in/premium-tools](/premium-tools/).

Most of them are free to use. What costs money is narrow: exporting your work from the seven builders, copying code out of the Visualization Cookbook, copying notes out of Field Notes, running the Advisory Board on ImpactMojo's own AI models, and downloading the VaniScribe Colab notebook. Everything else, including the analysis you do on screen, is free.

Membership has four levels. Explorer is free. Practitioner is ₹399 a month or ₹3,990 a year. Professional is ₹999 a month or ₹9,990 a year, which is two months free. The Team Plan is ₹1,499 per user per month: every member gets Professional access, and the plan adds a team dashboard, branded certificates and invoice billing. Organisation accounts hold a set number of seats and an administrator, and are arranged by writing to [hello@impactmojo.in](mailto:hello@impactmojo.in). The [Membership page](/premium.html) lists what each plan includes and is the place to check current prices.

## The 13 tools

### Seven builders: free to use, export on a paid plan

You build in the page without signing in. Exporting or printing the result asks for a plan.

| Tool | What you build |
|---|---|
| [Research Question Builder](/premium-tools/rq-builder.html) | A research question framed with PICO or SPIDER |
| [ToR Builder](/premium-tools/tor-builder.html) | A structured Terms of Reference for an evaluation or study, with a costing sheet |
| [Logframe Builder](/premium-tools/logframe-pro.html) | A logical-framework matrix: indicators, means of verification, assumptions |
| [Empathy Mapping](/premium-tools/empathy-pro.html) | A map of what people say, think, do and feel before you design for them |
| [AI Strategy Canvas](/premium-tools/ai-canvas-pro.html) | A responsible-AI opportunities and risks canvas for a programme |
| [Statistical Code Converter](/premium-tools/code-converter-pro.html) | Analysis code translated between R, Python and Stata, in the browser |
| [Qualitative Insights Lab](/premium-tools/qual-insights-lab.html) | Coded and themed qualitative data, without leaving the page |

### Four reference tools: free to open

| Tool | What it is | What needs a plan |
|---|---|---|
| [Chart Selector](/premium-tools/chart-selector-pro.html) | A decision tree for choosing the right chart | Nothing |
| [DevData Practice](/premium-tools/devdata-practice.html) | 36 generators that produce more than 840,000 synthetic rows in the style of DHS, LSMS and labour force surveys, for practising analysis. None of it is real survey data | Nothing |
| [Visualization Cookbook](/premium-tools/viz-cookbook.html) | 63 chart recipes, organised by the question you are asking of your data, with Python code | Copying the code needs a Professional plan |
| [Field Notes](/premium-tools/field-notes.html) | A reader for field notes and observations from a development economist | Copying a note needs a Professional plan |

### Two AI tools: free to try with your own API key

Both tools call an AI service. They run on a key that you supply, so using them costs ImpactMojo nothing and they are free to try. The key stays in your browser and goes only to the provider you pick.

| Tool | What it does | What needs a plan |
|---|---|---|
| [Advisory Board](/premium-tools/advisory-board-pro.html) | You describe a development dilemma. A panel of five AI personas (a moderator, a development economist, a field practitioner, a behavioural scientist and an equity-minded critic) debates it for up to four rounds, and the moderator closes with a synthesis. You can steer each round and export the transcript | With your own key, nothing. On a Professional plan you can run it on ImpactMojo's hosted models instead, where the advisors run on several different models and a daily limit applies |
| [VaniScribe](/premium-tools/vaniscribe.html) | Transcribes interviews and field recordings in the browser, using your own Sarvam AI key. The language menu offers auto-detect, Hindi, Bengali, Tamil, Telugu, Kannada, Malayalam, Marathi, Gujarati, Punjabi, Odia and Indian English. Files longer than 30 seconds are split and stitched back together | The browser transcriber is free. The Colab notebook adds speaker labels, interviews up to 60 minutes and batches of up to 20 files, and needs a Professional plan |

The browser version of VaniScribe uses Sarvam's speech-to-text API, which does not label speakers. If you need to know who said what in a focus group, use the notebook.

## Which providers the Advisory Board accepts

Groq, Google Gemini, OpenAI, Anthropic and DeepSeek. Pick the provider, paste your key, and leave the model box empty to use the default shown, or type a model name your account can use. A full panel is about a dozen short calls, billed by your provider. Some providers, Groq and Google Gemini among them, have offered free usage tiers. Check their current terms before you rely on that.

With one key, all five advisors speak through the same model. That is the main difference from the hosted mode.

Your key is held in the browser tab for the session. Tick "Remember this key on this device" to keep it in this browser's local storage; clear your site data or delete the key at your provider to remove it.

## Using Pro Studio in teaching

- Use DevData Practice to give a class a dataset with a known structure, so people practise methods and not data cleaning.
- Use the Chart Selector and the Visualization Cookbook together: choose the chart for the question, then read the recipe.
- Use the Logframe Builder, the ToR Builder or the Research Question Builder as a live exercise. Participants build in the page and the facilitator reviews the result on screen.
- Use VaniScribe for the first pass on recordings in regional languages, and read the transcript against the audio before you quote it. Machine transcription of code-mixed speech makes mistakes.

## Things to know

- The tools are for learning and practice. The Advisory Board personas are AI voices that give perspectives, not professional advice.
- The free tools do not need an account. The paid features check your plan when you try to export, copy or run the hosted models.
- For grassroots organisations, write to [hello@impactmojo.in](mailto:hello@impactmojo.in) about group access.
