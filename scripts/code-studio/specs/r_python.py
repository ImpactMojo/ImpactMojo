# -*- coding: utf-8 -*-
"""R & Python for Development: moved from 101-courses/r-python-dev.html into Code Studio, text unchanged."""

PAGE = {'slug': 'r-python',
 'order': 1,
 'kind': 'runnable',
 'title': 'R & Python for Development',
 'h1': 'R &amp; Python for Development',
 'lede': 'Learn to code from absolute zero, with real R and Python running live in your browser. No '
         'installation, works on a modest laptop.',
 'description': 'Learn R and Python from absolute zero for development-sector data work in South Asia: run '
                'real code live in your browser, no installation. Read data, wrangle, summarise, visualise '
                'and estimate a regression.',
 'card': 'Both languages side by side, from your first line of code to a regression on a household survey.',
 'datasets': ['survey'],
 'engine_note': '<strong>How the live code works.</strong> The first time you run R or Python, your browser '
                'downloads the language engine once (R about 7&nbsp;MB, Python about 10&nbsp;MB; later '
                'modules fetch a package or two more). Give the first click 10 to 30 seconds; after that it '
                'is quick. A small illustrative household survey is loaded for you as <code '
                'class="inline">survey.csv</code> (and as <code class="inline">SURVEY_CSV</code>).',
 'modules': [{'tab': 'First code',
              'title': 'Your first line of code',
              'blocks': [{'t': 'html',
                          'html': '<p>Two languages run most development-sector data work: '
                                  '<strong>R</strong> (loved by statisticians and evaluators) and '
                                  "<strong>Python</strong> (loved by data scientists). You don't have to "
                                  'choose: this course teaches <strong>both, side by side</strong>. Click '
                                  '<strong>Run</strong>, then switch the tab from R to Python and Run '
                                  'again.</p>'},
                         {'t': 'dual', 'r': 'print("Hello from R")', 'py': 'print("Hello from Python")'},
                         {'t': 'html',
                          'html': '<h3>A first calculation</h3>\n'
                                  "        <p>Store five people's ages and compute the "
                                  '<strong>average</strong>. In R a list of numbers is <code '
                                  'class="inline">c(...)</code> and the mean is <code '
                                  'class="inline">mean(...)</code>; in Python it\'s a list <code '
                                  'class="inline">[...]</code> and <code class="inline">sum(...) / '
                                  'len(...)</code>.</p>'},
                         {'t': 'dual',
                          'r': 'ages <- c(19, 22, 25, 31, 45)\nmean(ages)',
                          'py': 'ages = [19, 22, 25, 31, 45]\nsum(ages) / len(ages)'},
                         {'t': 'html',
                          'html': '<div class="info-box"><strong>That\'s 80% of analysis:</strong> data goes '
                                  'into a variable, a function does something to it, you read the '
                                  'result.</div>'}]},
             {'tab': 'Data in/out',
              'title': 'Data in, data out',
              'blocks': [{'t': 'html',
                          'html': '<p>Real analysis starts with a <strong>dataset</strong>: rows (people, '
                                  "households) and columns (variables). We've loaded a small illustrative "
                                  'household-survey sample into <code class="inline">SURVEY_CSV</code> for '
                                  'you. <span class="illustrative-tag">Illustrative data</span></p>\n'
                                  '        <p>Read it into a <strong>data frame</strong>: a spreadsheet-like '
                                  'table. In R, <code class="inline">read.csv(text = SURVEY_CSV)</code>; in '
                                  'Python, <code class="inline">pandas</code>. Then peek at the first rows '
                                  'and the shape.</p>'},
                         {'t': 'dual',
                          'r': 'df <- read.csv(text = SURVEY_CSV)\n'
                               'head(df)\n'
                               'cat("rows:", nrow(df), " cols:", ncol(df), "\\n")',
                          'py': 'import pandas as pd, io\n'
                                'df = pd.read_csv(io.StringIO(SURVEY_CSV))\n'
                                'print(df.head())\n'
                                'print("rows:", df.shape[0], " cols:", df.shape[1])',
                          'pypkgs': 'pandas'},
                         {'t': 'html',
                          'html': '<h3>Look at one column</h3>\n'
                                  '        <p>Columns are accessed by name: <code '
                                  'class="inline">df$pc_exp</code> in R, <code '
                                  'class="inline">df["pc_exp"]</code> in Python. Let\'s summarise monthly '
                                  'per-capita expenditure.</p>'},
                         {'t': 'dual',
                          'r': 'df <- read.csv(text = SURVEY_CSV)\nsummary(df$pc_exp)',
                          'py': 'import pandas as pd, io\n'
                                'df = pd.read_csv(io.StringIO(SURVEY_CSV))\n'
                                'print(df["pc_exp"].describe())',
                          'pypkgs': 'pandas'},
                         {'t': 'html',
                          'html': '<div class="info-box">In the field you\'ll read NFHS, ASER, PLFS or your '
                                  'own survey the same way: from a <code class="inline">.csv</code> file '
                                  'with <code class="inline">read.csv("mydata.csv")</code> or <code '
                                  'class="inline">pd.read_csv("mydata.csv")</code>.</div>'}]},
             {'tab': 'Wrangling',
              'title': 'Wrangling: filter and select',
              'blocks': [{'t': 'html',
                          'html': '<p>Most data work is <strong>reshaping</strong>: keep some rows, keep '
                                  'some columns. Say we want only <strong>rural</strong> households. In R '
                                  '(base) we index with a condition; in Python we use <code '
                                  'class="inline">pandas</code>.</p>'},
                         {'t': 'dual',
                          'r': 'df <- read.csv(text = SURVEY_CSV)\n'
                               'rural <- df[df$area == "Rural", ]\n'
                               'rural[, c("district", "gender", "caste", "pc_exp")]',
                          'py': 'import pandas as pd, io\n'
                                'df = pd.read_csv(io.StringIO(SURVEY_CSV))\n'
                                'rural = df[df["area"] == "Rural"]\n'
                                'print(rural[["district","gender","caste","pc_exp"]])',
                          'pypkgs': 'pandas'},
                         {'t': 'html',
                          'html': '<h3>Add a new column</h3>\n'
                                  '        <p>Flag "low expenditure" households (below ₹1,500/month). Assign '
                                  'a new column and count how many.</p>'},
                         {'t': 'dual',
                          'r': 'df <- read.csv(text = SURVEY_CSV)\n'
                               'df$low_exp <- df$pc_exp < 1500\n'
                               'table(df$low_exp)',
                          'py': 'import pandas as pd, io\n'
                                'df = pd.read_csv(io.StringIO(SURVEY_CSV))\n'
                                'df["low_exp"] = df["pc_exp"] < 1500\n'
                                'print(df["low_exp"].value_counts())',
                          'pypkgs': 'pandas'},
                         {'t': 'html',
                          'html': '<div class="info-box">Once you\'re comfortable, R\'s '
                                  '<strong>tidyverse</strong> (<code class="inline">dplyr</code>) and '
                                  "Python's <strong>pandas</strong> chaining make this even cleaner: <code "
                                  'class="inline">df |&gt; filter(area=="Rural")</code> / <code '
                                  'class="inline">df.query(\'area=="Rural"\')</code>. Same idea, nicer '
                                  'grammar. (Our <a href="/premium-tools/code-converter-pro.html" '
                                  'style="color:var(--accent-color)">Code Convert Pro</a> tool translates '
                                  'between them.)</div>'}]},
             {'tab': 'Summaries',
              'title': 'Summaries &amp; disaggregation',
              'blocks': [{'t': 'html',
                          'html': '<p>An average hides as much as it reveals. The real story is in the '
                                  '<strong>disaggregation</strong>: the same number split by gender, caste, '
                                  'or geography. (This is exactly the lens of the <a '
                                  'href="/Labs/data-feminism-lab.html" '
                                  'style="color:var(--accent-color)">Data Feminism Studio</a>.)</p>\n'
                                  '        <p>Mean expenditure by <strong>gender</strong>, then by '
                                  '<strong>gender × caste</strong>:</p>'},
                         {'t': 'dual',
                          'r': 'df <- read.csv(text = SURVEY_CSV)\n'
                               'aggregate(pc_exp ~ gender, df, mean)\n'
                               'aggregate(pc_exp ~ gender + caste, df, mean)',
                          'py': 'import pandas as pd, io\n'
                                'df = pd.read_csv(io.StringIO(SURVEY_CSV))\n'
                                'print(df.groupby("gender")["pc_exp"].mean())\n'
                                'print(df.groupby(["gender","caste"])["pc_exp"].mean())',
                          'pypkgs': 'pandas'},
                         {'t': 'html',
                          'html': '<div class="info-box warning"><strong>Read the gaps.</strong> A single '
                                  '"average expenditure" number would erase the gap between, say, '
                                  'General-caste and SC/ST households, and between men and women within each '
                                  'group. Disaggregation is where inequality becomes visible.</div>'}]},
             {'tab': 'Visualise',
              'title': 'Your first chart',
              'blocks': [{'t': 'html',
                          'html': "<p>A picture makes a gap obvious. We'll draw a <strong>bar chart</strong> "
                                  'of mean expenditure by caste. In Python we use <code '
                                  'class="inline">matplotlib</code> and call <code '
                                  'class="inline">show()</code> (a helper we\'ve provided) to display it; in '
                                  'R we use base <code class="inline">barplot()</code>.</p>\n'
                                  '        <div class="info-box">First run of this module downloads the '
                                  'plotting library (a few MB more). The chart appears below the '
                                  'code.</div>'},
                         {'t': 'dual',
                          'r': 'df <- read.csv(text = SURVEY_CSV)\n'
                               'm <- aggregate(pc_exp ~ caste, df, mean)\n'
                               'barplot(m$pc_exp, names.arg = m$caste,\n'
                               '        col = "#0EA5E9", main = "Mean expenditure by caste",\n'
                               '        ylab = "Rupees / month")',
                          'py': 'import pandas as pd, io\n'
                                'import matplotlib\n'
                                'matplotlib.use("AGG")\n'
                                'import matplotlib.pyplot as plt\n'
                                'df = pd.read_csv(io.StringIO(SURVEY_CSV))\n'
                                'm = df.groupby("caste")["pc_exp"].mean()\n'
                                'fig, ax = plt.subplots(figsize=(6,3.5))\n'
                                'ax.bar(m.index, m.values, color="#0EA5E9")\n'
                                'ax.set_title("Mean expenditure by caste")\n'
                                'ax.set_ylabel("Rupees / month")\n'
                                'show(fig)',
                          'pypkgs': 'pandas,matplotlib'},
                         {'t': 'html',
                          'html': '<div class="info-box">The production-grade tools are R\'s '
                                  "<strong>ggplot2</strong> and Python's "
                                  '<strong>matplotlib/seaborn</strong>. For design principles, see the <a '
                                  'href="/101-courses/data-viz.html" style="color:var(--accent-color)">Data '
                                  'Visualization 101</a>.</div>'}]},
             {'tab': 'Regression',
              'title': 'Regression &amp; the idea of impact',
              'blocks': [{'t': 'html',
                          'html': '<p>A <strong>regression</strong> asks: as one thing changes, how does '
                                  'another move? Here: does an extra year of education go with higher '
                                  'expenditure? In R, <code class="inline">lm(y ~ x)</code>; in Python, '
                                  '<code class="inline">numpy.polyfit</code> for the same slope.</p>'},
                         {'t': 'dual',
                          'r': 'df <- read.csv(text = SURVEY_CSV)\n'
                               'model <- lm(pc_exp ~ years_edu, data = df)\n'
                               'summary(model)$coefficients',
                          'py': 'import pandas as pd, io, numpy as np\n'
                                'df = pd.read_csv(io.StringIO(SURVEY_CSV))\n'
                                'slope, intercept = np.polyfit(df["years_edu"], df["pc_exp"], 1)\n'
                                'print("slope (Rs per extra year):", round(slope, 1))\n'
                                'print("intercept:", round(intercept, 1))',
                          'pypkgs': 'pandas,numpy'},
                         {'t': 'html',
                          'html': '<h3>From correlation to impact</h3>\n'
                                  '        <p>That slope is a <em>correlation</em>, not proof that education '
                                  '<em>causes</em> higher spending. Impact evaluation isolates cause: e.g. '
                                  '<strong>difference-in-differences</strong> compares the change in a '
                                  'treated group to the change in a comparison group. A tiny illustration: '
                                  '<span class="illustrative-tag">Illustrative</span></p>'},
                         {'t': 'dual',
                          'r': '# before/after means for treated (T) and comparison (C) groups\n'
                               'T_before <- 1000; T_after <- 1600\n'
                               'C_before <- 1000; C_after <- 1200\n'
                               'did <- (T_after - T_before) - (C_after - C_before)\n'
                               'cat("Difference-in-differences estimate:", did, "\\n")',
                          'py': 'T_before, T_after = 1000, 1600\n'
                                'C_before, C_after = 1000, 1200\n'
                                'did = (T_after - T_before) - (C_after - C_before)\n'
                                'print("Difference-in-differences estimate:", did)'},
                         {'t': 'html',
                          'html': '<div class="info-box">Go deeper in the <a href="/courses/causal/" '
                                  'style="color:var(--accent-color)">Causal Inference for Development</a> '
                                  'course and <a href="/101-courses/impact-eval.html" '
                                  'style="color:var(--accent-color)">Impact Evaluation 101</a>. A great open '
                                  'text with R/Python/Stata code: Martin Huber, <em>Causal Analysis</em> '
                                  '(MIT Press).</div>'}]},
             {'tab': 'Reproduce',
              'title': 'Reproducibility &amp; sharing',
              'blocks': [{'t': 'html',
                          'html': "<p>Analysis you can't re-run is analysis nobody can trust. The habit: put "
                                  'your steps in a <strong>script</strong>, <strong>comment</strong> it, and '
                                  "share the script + data so anyone can reproduce your numbers. Here's the "
                                  'whole pipeline from this course in one runnable cell.</p>'},
                         {'t': 'dual',
                          'r': '# --- A tiny reproducible analysis ---\n'
                               'df <- read.csv(text = SURVEY_CSV)   # 1. read data\n'
                               'df$low_exp <- df$pc_exp < 1500       # 2. derive a variable\n'
                               'by_grp <- aggregate(pc_exp ~ gender + caste, df, mean)  # 3. summarise\n'
                               'print(by_grp)\n'
                               'cat("Share low-expenditure:", round(mean(df$low_exp), 2), "\\n")  # 4. '
                               'headline',
                          'py': '# --- A tiny reproducible analysis ---\n'
                                'import pandas as pd, io\n'
                                'df = pd.read_csv(io.StringIO(SURVEY_CSV))     # 1. read data\n'
                                'df["low_exp"] = df["pc_exp"] < 1500           # 2. derive a variable\n'
                                'by_grp = df.groupby(["gender","caste"])["pc_exp"].mean()  # 3. summarise\n'
                                'print(by_grp)\n'
                                'print("Share low-expenditure:", round(df["low_exp"].mean(), 2))  # 4. '
                                'headline',
                          'pypkgs': 'pandas'},
                         {'t': 'html',
                          'html': '<ul>\n'
                                  '            <li><strong>Comment</strong> every step (the <code '
                                  'class="inline">#</code> lines) so future-you understands it.</li>\n'
                                  '            <li><strong>Never edit data by hand</strong>: every change '
                                  'should be a line of code you can re-run.</li>\n'
                                  '            <li><strong>Share</strong> the script and data (a folder, a '
                                  'GitHub repo, an <code class="inline">.Rproj</code> / notebook). '
                                  'Reproducibility is the difference between a claim and evidence.</li>\n'
                                  '        </ul>'}]},
             {'tab': 'Done',
              'title': 'You can now code with data',
              'blocks': [{'t': 'html',
                          'html': '<div class="completion-badge">\n'
                                  '            <div class="tick"><svg viewBox="0 0 24 24" fill="none" '
                                  'stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline '
                                  'points="20 6 9 17 4 12"/></svg></div>\n'
                                  '            <p>From "hello" to reading a survey, wrangling it, '
                                  'disaggregating, charting, and running a regression: in both R and Python, '
                                  'entirely in your browser.</p>\n'
                                  '        </div>\n'
                                  '        <div style="text-align:center;">\n'
                                  '            <span class="tag">R</span><span '
                                  'class="tag">Python</span><span class="tag">tidyverse / pandas</span><span '
                                  'class="tag">WebR + Pyodide</span><span class="tag">No install</span>\n'
                                  '        </div>\n'
                                  '        <h3 style="text-align:center;margin-top:1.5rem;">Where to go '
                                  'next</h3>\n'
                                  '        <div class="roadmap">\n'
                                  '            <div class="road-item"><div '
                                  'class="road-num">→</div><div><h4><a '
                                  'href="/101-courses/econometrics-101.html" '
                                  'style="color:var(--text-primary)">Econometrics 101</a></h4><p>Put the '
                                  'regression to work on real questions.</p></div></div>\n'
                                  '            <div class="road-item"><div '
                                  'class="road-num">→</div><div><h4><a href="/Labs/data-feminism-lab.html" '
                                  'style="color:var(--text-primary)">Data Feminism Studio</a></h4><p>The '
                                  'ethics and power of disaggregation.</p></div></div>\n'
                                  '            <div class="road-item"><div '
                                  'class="road-num">→</div><div><h4><a '
                                  'href="/premium-tools/code-converter-pro.html" '
                                  'style="color:var(--text-primary)">Code Convert Pro</a></h4><p>Translate '
                                  'your code between R, Python, Stata and SPSS.</p></div></div>\n'
                                  '            <div class="road-item"><div '
                                  'class="road-num">→</div><div><h4><a href="/Labs/sampling-toolkit.html" '
                                  'style="color:var(--text-primary)">Sampling Toolkit</a></h4><p>Design the '
                                  'survey your code will analyse.</p></div></div>\n'
                                  '        </div>'}]}]}
