# Visualization Cookbook Guide

## What Is the Visualization Cookbook?

The Visualization Cookbook is a **question-driven chart selection tool** with production-ready Python code. Instead of browsing chart galleries and guessing which chart type suits your data, you answer a simple question — "What story does my data tell?" — and get the right chart with working code you can copy and use immediately.

It includes **14 chart types** covering the most common data stories in development work.

**Access:** Part of DevData Practice (Professional tier) — [Open Visualization Cookbook](https://impactmojo-devdata-pro.netlify.app/charts.html)

---

## The Problem This Solves

Development professionals produce reports, proposals, and presentations full of data — but the charts are often the weakest part. Common problems:

- **Wrong chart type** — using a pie chart when a bar chart would be clearer, or a line chart when you're not showing time
- **Cluttered visuals** — too many colours, labels, or data points on one chart
- **Starting from scratch** — spending hours in Excel or trying to learn Python just to make one good chart
- **Inconsistent quality** — every team member produces charts that look different

The Visualization Cookbook solves these by asking you one question first: **What is your data trying to say?**

---

## How It Works

### Step 1: Choose Your Data Story

Every chart answers one of six types of questions:

| Data story | What you're showing | Example |
|-----------|-------------------|---------|
| **Comparison** | How things differ from each other | "Which district has the highest immunisation rate?" |
| **Distribution** | How data is spread across a range | "How are household incomes distributed in our target area?" |
| **Relationship** | How two variables relate to each other | "Is there a correlation between education spending and learning outcomes?" |
| **Composition** | What makes up a whole | "What proportion of our budget goes to each programme area?" |
| **Time series** | How something changes over time | "How has stunting prevalence changed over the last 10 years?" |
| **Spatial** | How something varies across geography | "Which states have the highest poverty rates?" |

### Step 2: Get the Right Chart

Based on your data story, the Cookbook recommends one or more chart types and shows you:
- A **sample chart** so you can see what it looks like
- **When to use it** — and when not to
- **Production-ready Python code** using matplotlib and seaborn (standard data science libraries)

### Step 3: Adapt the Code

Copy the Python code, replace the sample data with your own, and run it. The chart is publication-ready — proper labels, clean formatting, and professional styling.

---

## The 14 Chart Types

| Chart | Best for | Data story |
|-------|---------|-----------|
| Bar chart | Comparing categories | Comparison |
| Grouped bar chart | Comparing categories across groups | Comparison |
| Horizontal bar chart | Many categories with long names | Comparison |
| Line chart | Trends over time | Time series |
| Area chart | Cumulative trends over time | Time series + Composition |
| Scatter plot | Relationship between two variables | Relationship |
| Bubble chart | Three-variable relationships | Relationship |
| Histogram | Distribution of a single variable | Distribution |
| Box plot | Comparing distributions across groups | Distribution |
| Pie / donut chart | Parts of a whole (few categories) | Composition |
| Stacked bar chart | Parts of a whole across categories | Composition |
| Heatmap | Patterns in two-dimensional data | Relationship |
| Choropleth map | Geographic variation | Spatial |
| Slope chart | Change between two time points | Comparison + Time |

---

## Do I Need to Know Python?

**Not necessarily.** The Cookbook is most useful if you can run Python code (or have a colleague who can), but even without coding knowledge:

- **The chart selection guidance is valuable on its own.** Knowing which chart type to use is half the battle — you can then create it in Excel, Google Sheets, or any tool you're comfortable with.
- **The code is annotated.** Comments explain what each line does, so someone with basic Python skills can modify it.
- **ImpactMojo's Data & Technology courses teach the basics.** If you want to learn Python for data visualization, start with the Data Visualization foundational course.

---

## How Educators Can Use the Cookbook

### For Data Visualization Workshops
Walk participants through the "choose your data story" framework. Have them bring their own data and identify which story it tells before choosing a chart type.

### For Report Writing Sessions
When teams are preparing reports, use the Cookbook to ensure charts are appropriate and clear. The six data story categories help teams think about what they're trying to communicate.

### For Teaching Chart Literacy
Even if participants won't write code, the Cookbook teaches them to read charts critically. "What data story is this chart telling? Is it the right chart type for that story?"

---

## Tips

- **Start with the data story, not the chart type.** "I want to make a pie chart" is the wrong starting point. "I want to show what proportion of our budget goes to each programme" is the right one.
- **Less is more.** The best charts communicate one thing clearly. If your chart needs a paragraph of explanation, simplify it.
- **Use the Cookbook alongside the Handout on data visualization.** The handout covers principles; the Cookbook provides implementation.
- **Python code works in Google Colab.** If you don't have Python installed, paste the code into [Google Colab](https://colab.research.google.com) — it's free and runs in your browser.
