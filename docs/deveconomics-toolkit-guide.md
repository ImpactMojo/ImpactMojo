# DevEconomics Toolkit Guide

## What Is the DevEconomics Toolkit?

The DevEconomics Toolkit is a collection of **11 interactive web applications** for development economics and evaluation methods. Each app lets you adjust parameters, see results in real time, and build intuition for methods that are usually taught with equations and textbooks.

You don't need to install anything. Each app runs in your web browser.

**Access:** Professional tier (₹999/month) — [Open DevEconomics Toolkit](https://impactmojo-devecon-toolkit.netlify.app/)

---

## What Are "Shiny Apps"? (A Quick Explanation)

The DevEconomics Toolkit is built using **R Shiny** — a technology that turns statistical code into interactive web applications. Here's what that means in plain language:

- **R** is a programming language widely used by economists and researchers for data analysis
- **Shiny** is a framework that lets developers turn R code into a web page with buttons, sliders, and charts that anyone can use — no coding required
- **You don't need to know R or any programming** to use these apps. They present you with inputs (sliders, dropdown menus, text fields) and show you outputs (charts, tables, calculations) in your browser

Think of it like a calculator, but instead of simple arithmetic, each app calculates something specific to development economics — sample sizes for an RCT, inequality measures, poverty indices, or the results of different evaluation designs.

---

## The 11 Apps

### Evaluation Design Tools

#### 1. RCT Power Calculator
**What it does:** Calculates the **sample size** you need for a randomised controlled trial to detect a given effect size.

**Why this matters:** Under-powered studies waste resources and produce unreliable results. Over-powered studies are unnecessarily expensive. This calculator helps you find the right sample size.

**How to use it:** Enter your expected effect size, significance level, desired statistical power, and cluster size (if applicable). The app shows you the minimum sample size and a power curve.

**Who it's for:** Anyone designing an RCT or quasi-experiment — evaluation specialists, researchers, and programme managers writing proposals.

#### 2. DiD Simulator (Difference-in-Differences)
**What it does:** Visualises how the **difference-in-differences** method works — the most common way to estimate programme impact when random assignment isn't possible.

**Why this matters:** DiD is conceptually simple but easy to misapply. The simulator lets you see how the method isolates the treatment effect by comparing changes over time between treatment and control groups.

**How to use it:** Set the baseline and endline values for treatment and control groups. The app shows the parallel trends, the counterfactual, and the estimated treatment effect.

**Who it's for:** Anyone learning or teaching evaluation methods.

#### 3. RDD Explorer (Regression Discontinuity Design)
**What it does:** Demonstrates how **regression discontinuity** works — exploiting a cutoff (like a poverty threshold or exam score) to estimate causal effects.

**Why this matters:** RDD is one of the strongest quasi-experimental designs, but it requires understanding of bandwidths, running variables, and the visual logic of the method. This app makes it interactive.

**How to use it:** Adjust the cutoff point, bandwidth, and data parameters. See how the estimated effect changes.

#### 4. Synthetic Control Visualiser
**What it does:** Shows how the **synthetic control method** constructs a counterfactual by combining data from untreated units to create a comparison for a single treated unit.

**Why this matters:** When you're evaluating a policy that affected a single state or district (e.g., a new health policy in Tamil Nadu), you can't run an RCT. Synthetic control creates a weighted comparison from other states.

### Inequality & Poverty Tools

#### 5. Gini & Lorenz Curve Tool
**What it does:** Calculates the **Gini coefficient** (the most common measure of inequality) and draws the **Lorenz curve** — the visual representation of how income or wealth is distributed in a population.

**Why this matters:** Inequality is central to development work. This tool lets you input data (or use built-in country datasets) and instantly see how equal or unequal a distribution is.

**How to use it:** Enter income data or choose a preset country dataset. The app draws the Lorenz curve and calculates the Gini coefficient. Adjust values to see how changes affect inequality.

#### 6. MPI Explorer (Multidimensional Poverty Index)
**What it does:** Lets you explore the **Multidimensional Poverty Index** — which measures poverty not just by income but across health, education, and living standards.

**Why this matters:** Income-only poverty measures miss important dimensions. The MPI captures whether households have access to schooling, nutrition, clean water, sanitation, electricity, and adequate housing.

**How to use it:** Explore MPI data by country or region. Adjust weights on different dimensions to see how the poverty picture changes.

#### 7. Poverty Line Analysis
**What it does:** Analyses **poverty headcounts** (what percentage of the population is poor) and **poverty gaps** (how far below the poverty line poor households fall) at different poverty line thresholds.

**Why this matters:** The choice of poverty line dramatically affects who counts as poor. This tool shows how sensitive poverty statistics are to where you draw the line.

### Planning & Framework Tools

#### 8. Theory of Change Visualiser
**What it does:** Builds and visualises a **Theory of Change** diagram — mapping the causal chain from activities to outputs to outcomes to impact.

**How to use it:** Enter your programme's activities, outputs, outcomes, and impact. The app generates a visual diagram showing the causal logic.

#### 9. Cost-Benefit Analysis Tool
**What it does:** Helps you structure and calculate a **cost-benefit analysis** — comparing the total costs of a programme against its total benefits, discounted to present value.

**How to use it:** Enter cost items and benefit estimates, set a discount rate and time horizon, and the app calculates net present value, benefit-cost ratio, and internal rate of return.

#### 10. LogFrame Builder
**What it does:** Constructs a **logical framework** (logframe) — the standard planning tool used by most donors and development agencies.

**How to use it:** Enter your programme's goal, purpose, outputs, and activities. The app structures them into a logframe matrix with indicators, means of verification, and assumptions.

#### 11. WDI Dashboard (World Development Indicators)
**What it does:** Lets you explore the **World Bank's World Development Indicators** — the most comprehensive collection of development data covering 200+ countries.

**How to use it:** Select countries and indicators. The app generates time-series charts, cross-country comparisons, and downloadable data tables.

---

## How Educators Can Use the Toolkit

### For Teaching Evaluation Methods
Use the DiD Simulator, RDD Explorer, and RCT Power Calculator in class. Project the app on screen, adjust parameters together, and have students predict what will happen before you show the result.

### For Workshop Exercises
During an evaluation workshop, have participants use the RCT Power Calculator with their own programme parameters. They leave with an actual sample size calculation, not just theoretical understanding.

### For Economics Courses
The Gini tool, MPI Explorer, and Poverty Line Analysis are ideal for development economics courses. Students can interact with real concepts instead of only reading about them.

### For Proposal Writing
When teams are writing evaluation designs for proposals, the toolkit apps help them make realistic sample size calculations and choose appropriate methods.

---

## Tips

- **You don't need any programming knowledge.** Every app has a point-and-click interface. If you can use a web form, you can use these tools.
- **Use real programme numbers.** The tools are most valuable when you input your actual programme parameters — your expected effect sizes, your budget constraints, your target population.
- **Combine with courses.** The Development Economics flagship course teaches the theory behind these tools. Use the course for concepts and the toolkit for practice.
- **Apps load in your browser.** They may take a few seconds to initialise the first time, since they're running statistical computations in the background. This is normal.
- **Internet required.** Unlike some ImpactMojo content, the Shiny apps need an active internet connection to run.
