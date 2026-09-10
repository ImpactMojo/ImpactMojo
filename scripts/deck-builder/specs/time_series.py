# -*- coding: utf-8 -*-
"""
Time Series Analysis 101 — ImpactMojo 101 Series (native deck spec)
Trend, seasonality, stationarity, ARIMA, exponential smoothing, forecast evaluation, ARDL and
cointegration, VAR and Granger causality, volatility and breaks, interrupted time series for
programme evaluation, and Indian macro and administrative data. For applied researchers in
South Asia working in R, Python, Stata, gretl or EViews.
Build: python3 scripts/deck-builder/build.py time_series
"""

DECK = {
    "slug": "time-series",
    "title": "Time Series Analysis 101",
    "description": ("Time Series Analysis 101 — a free foundational course for applied researchers "
                    "in South Asia. Decomposition, stationarity and unit-root tests, ARIMA, "
                    "exponential smoothing, honest forecast evaluation, spurious regression, ARDL "
                    "bounds testing, cointegration and error correction, VAR and Granger causality, "
                    "GARCH and structural breaks, interrupted time series for programme evaluation, "
                    "and where to find Indian data. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Time Series<br>Analysis 101",
         "sub": "Trend, Seasonality, Stationarity, ARIMA, Cointegration, VAR and Interrupted "
                "Time Series &mdash; for Applied Work with Indian Data",
         "tags": ["Econometrics", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "Why Time Series Is Different"},
             {"name": "Components and Decomposition"},
             {"name": "Stationarity and Unit Roots"},
             {"name": "ARIMA Modelling"},
             {"name": "Exponential Smoothing and Forecasting"},
             {"name": "Evaluating Forecasts"},
             {"name": "Regression with Time Series"},
             {"name": "VAR and Granger Causality"},
             {"name": "Volatility, Breaks and Seasonality"},
             {"name": "Time Series for Programme Evaluation"},
             {"name": "Indian Data, Software and Practice"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "Why Time Series Is Different"},

        {"type": "content", "label": "Definition", "title": "A time series is one unit observed many times, in order",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "term", "word": "Time series",
                        "def": "A sequence of observations on one variable (or several) taken at "
                        "regular intervals: monthly inflation, quarterly GDP, daily rainfall, "
                        "weekly clinic attendance. The order carries information, and each "
                        "observation is usually related to the ones before it."},
                       {"t": "body", "html": "Cross-sectional methods assume observations are "
                        "independent draws from a population. A time series violates that "
                        "assumption by construction: this month's CPI is last month's plus a "
                        "change, and the change itself is related to earlier changes. Every "
                        "method in this course exists because ordinary regression, applied to "
                        "such data, gives standard errors that are wrong and relationships "
                        "that are not there."}],
              "right": [{"t": "bullets", "color": "cyan", "items": [
                  "<strong>Autocorrelation</strong>: observations near each other in time are similar. Effective sample size is smaller than n.",
                  "<strong>Trend</strong>: the mean moves. Two trending series are correlated whether or not they are related.",
                  "<strong>Seasonality</strong>: a pattern that repeats within the year. Kharif harvests, festival spending, monsoon disease.",
                  "<strong>Non-stationarity</strong>: the distribution changes over time, so the past may not describe the future.",
                  "<strong>One realisation</strong>: there is one history of Indian inflation. Inference comes from assumptions about its structure, not from replication."]},
                        {"t": "hbox", "color": "amber", "html": "The question this course keeps "
                         "returning to: is the pattern you see a relationship, or two things "
                         "moving through time together?"}]},
         ]},

        {"type": "content", "label": "Where It Appears", "title": "Time series in development work",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Setting", "Series", "Frequency", "Typical question"],
              "rows": [
                  ["Macro policy", "GDP, CPI, repo rate, exchange rate, fiscal deficit", "Quarterly, monthly, daily", "Does monetary tightening reduce inflation, and after how long?"],
                  ["Agriculture", "Rainfall, area sown, yields, mandi prices", "Daily, seasonal, weekly", "How do prices respond to a weak monsoon?"],
                  ["Health", "Clinic attendance, disease counts, immunisation coverage, HMIS indicators", "Weekly, monthly", "Did the programme change the trend after it started?"],
                  ["Labour", "PLFS quarterly unemployment, MGNREGA person-days, CMIE employment", "Quarterly, monthly", "Is the recovery structural or seasonal?"],
                  ["Programme monitoring", "Enrolment, disbursements, complaints, stock-outs", "Monthly", "Is this month unusual, or within the normal range?"],
                  ["Environment", "AQI, river flows, temperature", "Hourly, daily", "Trend after removing seasonality and weather"],
                  ["Finance and microfinance", "Repayment rates, portfolio at risk, prices", "Daily, monthly", "Volatility, early warning"]]},
             {"t": "body", "cls": "sm", "html": "Most monitoring dashboards in the sector plot a "
              "series and draw a line through it. The methods here are what you need to say "
              "whether the line means anything: whether a dip is a seasonal dip, whether a "
              "trend is a trend, and whether a change after a programme started is the "
              "programme."},
         ]},

        {"type": "content", "label": "Notation", "title": "Notation and vocabulary used throughout",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Symbol or term", "Meaning"],
                        "rows": [
                            ["<em>y<sub>t</sub></em>", "The value at time <em>t</em>; <em>t</em> = 1, ..., <em>T</em>"],
                            ["<em>y<sub>t&minus;1</sub></em>, lag", "The value one period earlier; <em>L y<sub>t</sub></em> = <em>y<sub>t&minus;1</sub></em>"],
                            ["&Delta;<em>y<sub>t</sub></em>", "First difference, <em>y<sub>t</sub></em> &minus; <em>y<sub>t&minus;1</sub></em>"],
                            ["&Delta;<sub>12</sub><em>y<sub>t</sub></em>", "Seasonal difference, <em>y<sub>t</sub></em> &minus; <em>y<sub>t&minus;12</sub></em> for monthly data"],
                            ["&epsilon;<sub>t</sub>, white noise", "Errors with mean zero, constant variance, no autocorrelation"],
                            ["&rho;<sub>k</sub>", "Autocorrelation at lag <em>k</em>: the correlation of <em>y<sub>t</sub></em> with <em>y<sub>t&minus;k</sub></em>"],
                            ["<em>h</em>", "Forecast horizon, periods ahead"],
                            ["I(0), I(1)", "Stationary; stationary after one difference (integrated of order 1)"]]}],
              "right": [{"t": "table",
                         "head": ["Term", "Meaning"],
                         "rows": [
                             ["Frequency", "Observations per year: 4, 12, 52, 365"],
                             ["Trend", "Long-run movement in the level"],
                             ["Seasonal", "Pattern repeating at fixed frequency"],
                             ["Cycle", "Rises and falls of no fixed length (business cycles)"],
                             ["Stationary", "Mean, variance and autocovariances do not depend on <em>t</em>"],
                             ["Random walk", "<em>y<sub>t</sub></em> = <em>y<sub>t&minus;1</sub></em> + &epsilon;<sub>t</sub>; the simplest non-stationary series"],
                             ["Persistence", "How long a shock's effect lasts"],
                             ["In-sample, out-of-sample", "Data used to fit; data held back to test"]]},
                        {"t": "hbox", "color": "cyan", "html": "Logs are natural logs, and "
                         "&Delta; log <em>y</em> is approximately the growth rate. Most "
                         "macro series enter in logs."}]},
         ]},

        {"type": "content", "label": "Look First", "title": "Plot it before you model it",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Every time-series analysis begins with a line "
                        "plot of the series against time, and most of the mistakes in "
                        "published applied work could have been avoided by looking at it. "
                        "The plot shows the trend, the seasonality, the outliers, the breaks, "
                        "the changes in variance and the missing stretches. It also shows "
                        "whether the series is one thing or two things spliced (a base-year "
                        "revision, a definition change) that no test will diagnose."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Plot the level and the first difference (or the growth rate). Trend shows in the first; variance changes and outliers in the second.",
                           "Plot in logs if the series grows and its fluctuations grow with it. If the log plot is a straight line, the growth rate is constant.",
                           "Plot the seasonal sub-series (all Januaries, all Februaries) or a seasonal plot with one line per year.",
                           "Plot the autocorrelation function. It says how much memory the series has before any model is fitted."]}],
              "right": [{"t": "panel", "color": "amber", "title": "What the plot tells you about the method", "html":
                         "A series that wanders with no fixed mean needs differencing or "
                         "cointegration methods, not regression in levels. A series with "
                         "obvious annual peaks needs seasonal treatment before anything else. "
                         "A series whose swings grow over time needs logs, or a variance "
                         "model. A series with a jump in 2016 or 2020 needs a break "
                         "handled, and every test run across the break without one is "
                         "wrong. The plot decides the section of this course you need."},
                        {"t": "hbox", "color": "green", "html": "India's CPI base changed to "
                         "2012 = 100 in 2015; GDP moved to the 2011-12 base the same year. "
                         "A series that spans a base change without splicing shows a jump "
                         "that is an artefact."}]},
         ]},

        {"type": "content", "label": "Autocorrelation", "title": "The autocorrelation function: the series' memory",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Series", "ACF pattern", "Reads as"],
                        "rows": [
                            ["White noise", "All lags near zero", "No memory; nothing to model"],
                            ["Stationary AR(1), &phi; = 0.7", "Decays geometrically: 0.7, 0.49, 0.34, ...", "Shocks fade over a few periods"],
                            ["Random walk", "Near 1 at every lag, declining very slowly", "Shocks never fade; non-stationary"],
                            ["Trending series", "Very slow decay", "Trend dominates; difference or detrend first"],
                            ["Monthly seasonal", "Spikes at lags 12, 24, 36", "Seasonality present"],
                            ["MA(1)", "One spike at lag 1, then zero", "One-period memory in the shocks"]]},
                       {"t": "body", "cls": "sm", "html": "The sample ACF, &rho;&#770;<sub>k</sub>, "
                        "for k = 1 to about T/4, with bands at &plusmn;1.96/&radic;T. A bar "
                        "outside the band is significant at 5% on its own; with 40 bars, two "
                        "will be by chance."}],
              "right": [{"t": "panel", "color": "cyan", "title": "The partial autocorrelation", "html":
                         "The PACF at lag <em>k</em> is the correlation between <em>y<sub>t</sub></em> "
                         "and <em>y<sub>t&minus;k</sub></em> after removing the effect of lags 1 to "
                         "<em>k</em> &minus; 1. An AR(<em>p</em>) process has a PACF that cuts off "
                         "after lag <em>p</em>; an MA(<em>q</em>) process has an ACF that cuts "
                         "off after lag <em>q</em>. The pair is the traditional way to pick "
                         "ARIMA orders, and section 04 uses it."},
                        {"t": "hbox", "color": "amber", "html": "The Ljung-Box test (Ljung and "
                         "Box, <em>Biometrika</em> 1978, 65:297) tests whether the first "
                         "<em>m</em> autocorrelations are jointly zero. It is the standard "
                         "check on model residuals: if they fail it, the model has missed "
                         "structure."}]},
         ]},

        {"type": "content", "label": "Effective Sample", "title": "Why 120 monthly observations are not 120 observations",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "With autocorrelation &rho; at lag 1, the "
                        "variance of a sample mean is inflated by roughly (1 + &rho;) / "
                        "(1 &minus; &rho;). At &rho; = 0.8 that factor is 9: ten years of "
                        "monthly data carry about as much information about the mean as 13 "
                        "independent observations. Standard errors computed as if the "
                        "observations were independent are too small by a factor of three, "
                        "and t-statistics too large by the same."},
                       {"t": "stats", "cols": 3, "cards": [
                           {"num": "&rho; = 0.5", "label": "variance factor 3; effective n is a third", "color": "cyan", "source": "(1 + &rho;) / (1 &minus; &rho;)"},
                           {"num": "&rho; = 0.8", "label": "factor 9; 120 months act like 13", "color": "amber", "source": "Same formula"},
                           {"num": "&rho; = 0.95", "label": "factor 39; 120 months act like 3", "color": "red", "source": "Same formula"}]}],
              "right": [{"t": "bullets", "color": "cyan", "items": [
                  "The same inflation applies to every regression coefficient estimated on autocorrelated data with autocorrelated errors.",
                  "Fixes, in order of preference: model the dynamics (lags of y and x) so the errors are white; use HAC (Newey-West) standard errors as a second best; never ignore it.",
                  "The Durbin-Watson statistic tests first-order autocorrelation in residuals; Breusch-Godfrey tests higher orders and allows lagged dependent variables.",
                  "A coefficient with a t-statistic of 12 on 60 quarterly observations of two trending series is the ordinary result of doing it wrong."]},
                        {"t": "hbox", "color": "amber", "html": "Persistence is why a monthly "
                         "programme series of three years is a small sample, and why "
                         "'significant' is cheap in time series and 'robust' is not."}]},
         ]},

        {"type": "content", "label": "This Course", "title": "How the course is arranged, and what it assumes",
         "blocks": [
             {"t": "flow", "steps": [
                 "DESCRIBE: components, decomposition, autocorrelation (02)",
                 "TEST: stationarity, unit roots, differencing (03)",
                 "MODEL ONE SERIES: ARIMA, exponential smoothing, forecasting and its evaluation (04&ndash;06)",
                 "RELATE SERIES: regression, ARDL, cointegration, VAR (07&ndash;08)",
                 "COMPLICATIONS: volatility, breaks, seasonality (09)",
                 "EVALUATE PROGRAMMES: interrupted time series, synthetic control (10)",
                 "PRACTICE: Indian data, software, pitfalls (11)"]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Assumed: the regression material in Econometrics "
                        "101 and the descriptive statistics in Data Analysis 101. Each method "
                        "is presented with what it assumes, what it produces, how to read the "
                        "output, and the mistake most often made with it in South Asian "
                        "applied journals. Worked numbers are illustrative unless a source "
                        "is named."}],
              "right": [{"t": "hbox", "color": "amber", "html": "The free text that pairs with "
                        "this course is Hyndman and Athanasopoulos, <em>Forecasting: Principles "
                        "and Practice</em> (3rd ed., OTexts, 2021), online at otexts.com/fpp3. "
                        "For the econometric half, Enders, <em>Applied Econometric Time "
                        "Series</em> (4th ed., Wiley, 2014)."}]},
         ]},

        # ===================== SECTION 02: COMPONENTS AND DECOMPOSITION =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "Components and Decomposition"},

        {"type": "content", "label": "Components", "title": "Trend, seasonal, cycle, remainder",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A series is thought of as the sum (or the "
                        "product) of a trend-cycle <em>T<sub>t</sub></em>, a seasonal component "
                        "<em>S<sub>t</sub></em> and a remainder <em>R<sub>t</sub></em>. The "
                        "additive form, <em>y<sub>t</sub></em> = <em>T<sub>t</sub></em> + "
                        "<em>S<sub>t</sub></em> + <em>R<sub>t</sub></em>, suits a series whose "
                        "seasonal swings are roughly constant in size. The multiplicative "
                        "form, <em>y<sub>t</sub></em> = <em>T<sub>t</sub></em> &times; "
                        "<em>S<sub>t</sub></em> &times; <em>R<sub>t</sub></em>, suits one whose "
                        "swings grow with the level, and taking logs turns it into the "
                        "additive form."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Trend-cycle: the smooth movement; trend and cycle are separated only in some methods.",
                           "Seasonal: the same shape each year, by construction summing to zero (additive) or averaging one (multiplicative) over a year.",
                           "Remainder: what is left. If it has structure, the decomposition missed something."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Seasonality in South Asia", "html":
                         "Agricultural output follows kharif and rabi; food prices fall at "
                         "harvest and rise before it; rural wages and MGNREGA demand peak in "
                         "the lean season; hospital admissions rise with the monsoon "
                         "(diarrhoea, dengue) and winter (respiratory); consumption spikes at "
                         "Diwali, Eid, Pongal and Durga Puja, whose dates move relative to the "
                         "Gregorian month. A seasonal model that assumes the same calendar "
                         "month every year will mis-time the festivals; some series need a "
                         "moving-holiday adjustment."},
                        {"t": "hbox", "color": "cyan", "html": "Before comparing any two months, "
                         "ask whether the difference is the season. Year-on-year comparisons "
                         "sidestep the problem and lose a year of data doing it."}]},
         ]},

        {"type": "content", "label": "Classical", "title": "Classical decomposition: the moving average and the seasonal index",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Step", "What is computed", "Monthly example (illustrative)"],
                        "rows": [
                            ["1. Trend-cycle", "A centred 12-month moving average (2&times;12-MA)", "Smooths the year out; loses six months at each end"],
                            ["2. Detrend", "<em>y<sub>t</sub></em> &minus; <em>T<sub>t</sub></em> (or divide, multiplicative)", "What remains is seasonal plus noise"],
                            ["3. Seasonal index", "Average the detrended values for each month across years; centre so they sum to zero", "January &minus;4.2, ..., October +6.8, ..."],
                            ["4. Remainder", "<em>y<sub>t</sub></em> &minus; <em>T<sub>t</sub></em> &minus; <em>S<sub>t</sub></em>", "Should look like noise"],
                            ["5. Seasonally adjusted", "<em>y<sub>t</sub></em> &minus; <em>S<sub>t</sub></em>", "The series with the calendar removed"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "Simple, transparent, and still what "
                        "many spreadsheets do. Its faults: the seasonal pattern is forced to "
                        "be identical every year, the moving average cannot reach the ends of "
                        "the series, and one outlier in a March distorts every March's index. "
                        "Use it to understand what decomposition does; use STL or X-13 to "
                        "publish."},
                        {"t": "hbox", "color": "amber", "html": "'Seasonally adjusted' figures "
                         "are model outputs and get revised as the model sees more data. "
                         "Cite the series, the method and the vintage."}]},
         ]},

        {"type": "content", "label": "STL and X-13", "title": "STL and X-13ARIMA-SEATS: the methods statistical offices use",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "STL", "html":
                         "Seasonal and Trend decomposition using Loess (Cleveland and "
                         "colleagues, <em>Journal of Official Statistics</em> 1990, 6:3). "
                         "Fits the trend and the seasonal by locally weighted regression, "
                         "lets the seasonal pattern change slowly over time, is robust to "
                         "outliers if asked, handles any frequency, and reaches the ends of "
                         "the series. Two tuning choices: the seasonal window (how fast the "
                         "pattern may change) and the trend window (how smooth). In R, "
                         "<em>stl()</em> or <em>feasts::STL</em>; in Python, "
                         "<em>statsmodels.tsa.seasonal.STL</em>."},
                        {"t": "panel", "color": "amber", "title": "X-13ARIMA-SEATS", "html":
                         "The US Census Bureau's program, used by statistical offices "
                         "including for India's seasonally adjusted IIP and by the RBI. "
                         "Fits a seasonal ARIMA model to extend the series at both ends, then "
                         "applies moving-average filters (X-11) or a model-based "
                         "decomposition (SEATS), with built-in handling of trading days, "
                         "moving holidays and outliers. Free; R's <em>seasonal</em> package "
                         "wraps it. The standard when the adjusted series will be published."}],
              "right": [{"t": "body", "html": "For research use, STL is enough and easier to "
                        "explain. For a series that will be compared with an official "
                        "seasonally adjusted one, use X-13 with the same options, or the "
                        "difference between yours and theirs will be the method, not the "
                        "data."},
                        {"t": "bullets", "color": "cyan", "sm": True, "items": [
                            "Check the remainder: its ACF should be flat and its variance roughly constant.",
                            "Plot the seasonal component over time. If it drifts, say so; the drift is often the finding.",
                            "Do not seasonally adjust a series and then fit a seasonal model to it. One or the other."]},
                        {"t": "hbox", "color": "green", "html": "MoSPI publishes IIP and GDP "
                         "without seasonal adjustment; the RBI publishes adjusted versions "
                         "of some series. Know which you are using."}]},
         ]},

        {"type": "content", "label": "Trends", "title": "Deterministic and stochastic trends: the distinction everything depends on",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Deterministic trend", "html":
                         "<em>y<sub>t</sub></em> = &alpha; + &beta;<em>t</em> + &epsilon;<sub>t</sub>. "
                         "The series fluctuates around a line. A shock pushes it away and it "
                         "returns. Detrend by regressing on <em>t</em> and keeping the "
                         "residuals; the series is 'trend-stationary'."},
                        {"t": "panel", "color": "amber", "title": "Stochastic trend", "html":
                         "<em>y<sub>t</sub></em> = &delta; + <em>y<sub>t&minus;1</sub></em> + &epsilon;<sub>t</sub>, "
                         "a random walk with drift. The series wanders; a shock shifts its "
                         "path permanently and it never returns. Difference it: &Delta;<em>y<sub>t</sub></em> "
                         "= &delta; + &epsilon;<sub>t</sub> is stationary. The series is "
                         "'difference-stationary' or I(1)."}],
              "right": [{"t": "body", "html": "The two look alike in a plot of fifty years and "
                        "call for opposite treatments. Detrending a random walk leaves a "
                        "non-stationary residual and spurious cycles; differencing a "
                        "trend-stationary series introduces an MA error and throws away "
                        "information. Nelson and Plosser (<em>Journal of Monetary "
                        "Economics</em> 1982, 10:139) tested fourteen US macro series and "
                        "could not reject a unit root in thirteen, which is why the unit-root "
                        "test (section 03) sits before every model in this course."},
                        {"t": "hbox", "color": "red", "html": "The practical consequence: "
                         "regressing one random walk on another, unrelated, produces a "
                         "'significant' coefficient most of the time. Section 07 shows the "
                         "numbers."}]},
         ]},

        {"type": "content", "label": "Transformations", "title": "Logs, differences, growth rates and indices",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Transformation", "Formula", "Use when", "Watch for"],
              "rows": [
                  ["Log", "log <em>y<sub>t</sub></em>", "Growth is proportional; variance rises with level", "Zeros and negatives; log(1 + y) changes the meaning"],
                  ["First difference", "<em>y<sub>t</sub></em> &minus; <em>y<sub>t&minus;1</sub></em>", "Removing a stochastic trend", "Over-differencing a stationary series adds an MA(1) with a unit root"],
                  ["Log difference", "&Delta; log <em>y<sub>t</sub></em> &asymp; growth rate", "Growth rates for macro series", "The approximation is poor above about 20% growth"],
                  ["Seasonal difference", "<em>y<sub>t</sub></em> &minus; <em>y<sub>t&minus;s</sub></em>", "Removing stable seasonality; year-on-year change", "Loses a year; does not remove trend on its own"],
                  ["Box-Cox", "(<em>y</em><sup>&lambda;</sup> &minus; 1)/&lambda;", "Stabilising variance when log is too strong or weak", "&lambda; is estimated; report it"],
                  ["Index, base 100", "100 &times; <em>y<sub>t</sub></em> / <em>y<sub>base</sub></em>", "Comparing series with different units", "The base year choice changes every visual impression"],
                  ["Per capita, real", "Divide by population, deflate by a price index", "Almost always for macro series", "Which deflator: CPI, WPI, GDP deflator? Say which"],
                  ["Moving average", "Mean of the last <em>k</em> values", "Smoothing for display", "Lags turning points by <em>k</em>/2; never model the smoothed series"]]},
             {"t": "body", "cls": "sm", "html": "Report every transformation and apply it before "
              "any test. A unit-root test on nominal rupee GDP and one on log real per capita "
              "GDP are testing different things, and only the second is usually what the "
              "question needs."},
         ]},

        {"type": "content", "label": "Missing and Irregular", "title": "Missing values, irregular spacing and revisions",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Time-series methods assume regular spacing and "
                        "no gaps, and administrative data provide neither. A monthly HMIS "
                        "series has districts that reported late, months with zero because the "
                        "form was not filed, and a reporting-system change in 2018. Weekly "
                        "mandi prices have no trades some weeks. The choices made here decide "
                        "everything after, and they should be listed in the methods."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "A zero that means 'not reported' is missing, not zero. Check the reporting completeness field, and treat it as missing.",
                           "Short gaps: linear or seasonal interpolation, or a state-space model that handles missing values natively (Kalman filter; <em>imputeTS</em> in R).",
                           "Long gaps: do not interpolate across them. Model the segments, or shorten the sample.",
                           "Irregular spacing: aggregate to a regular frequency, and say what was lost."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Revisions and vintages", "html":
                         "GDP, IIP and CPI are revised, sometimes for years. The series "
                         "available today is not the series a decision-maker saw at the "
                         "time. For a forecasting study, use the vintage that existed at "
                         "each forecast origin (a real-time dataset); for a structural "
                         "study, the latest. India's quarterly GDP has been revised by more "
                         "than a percentage point at several points; state which release "
                         "you used and when it was downloaded."},
                        {"t": "hbox", "color": "green", "html": "Keep the raw download, dated, "
                         "unchanged. Every cleaning step is in code, so a reviewer can see "
                         "what a gap became."}]},
         ]},

        {"type": "content", "label": "Decomposition Example", "title": "A worked decomposition: monthly clinic attendance",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Month (year 3)", "Observed", "Trend-cycle", "Seasonal", "Remainder", "Adjusted"],
                        "rows": [
                            ["Jan", "1,240", "1,310", "&minus;62", "&minus;8", "1,302"],
                            ["Apr", "1,190", "1,325", "&minus;140", "+5", "1,330"],
                            ["Jul", "1,510", "1,340", "+155", "+15", "1,355"],
                            ["Aug", "1,585", "1,348", "+210", "+27", "1,375"],
                            ["Oct", "1,320", "1,360", "&minus;30", "&minus;10", "1,350"],
                            ["Dec", "1,290", "1,372", "&minus;75", "&minus;7", "1,365"]]},
                       {"t": "body", "cls": "sm", "html": "Illustrative, additive. The "
                        "seasonal component peaks in the monsoon months and troughs in April; "
                        "the trend rises about 60 visits a year; the remainder is small and "
                        "patternless. The adjusted column is what a manager should compare "
                        "month to month."}],
              "right": [{"t": "panel", "color": "cyan", "title": "Reading it", "html":
                         "August's 1,585 looks like a surge; adjusted, it is 1,375, about "
                         "20 above trend, ordinary. April's 1,190 looks like a collapse; "
                         "adjusted, it is on trend. A programme that started in May and "
                         "claimed the July&ndash;August rise as its effect would be claiming "
                         "the monsoon. The comparison that answers the programme question "
                         "is section 10's."},
                        {"t": "hbox", "color": "amber", "html": "Three years of monthly data "
                         "give three observations of each month's seasonal effect. The "
                         "seasonal indices are therefore uncertain, and STL's smoothing "
                         "across months helps."}]},
         ]},

        # ===================== SECTION 03: STATIONARITY AND UNIT ROOTS =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "Stationarity and Unit Roots"},

        {"type": "content", "label": "Stationarity", "title": "What stationarity means and why every method wants it",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "term", "word": "Weak (covariance) stationarity",
                        "def": "The mean and variance are constant over time and the covariance "
                        "between <em>y<sub>t</sub></em> and <em>y<sub>t&minus;k</sub></em> depends "
                        "only on the lag <em>k</em>, not on <em>t</em>. The series may be "
                        "autocorrelated; it must not drift, trend or change its variability."},
                       {"t": "body", "html": "Stationarity is what makes one history usable: "
                        "if the process generating the series is the same throughout, the "
                        "past describes the future and averages over time estimate the "
                        "process's parameters. Without it, a sample mean is the mean of "
                        "nothing in particular, regression t-statistics have non-standard "
                        "distributions, and forecasts inherit whichever part of the past "
                        "the model happened to see."}],
              "right": [{"t": "bullets", "color": "cyan", "items": [
                  "Stationary: an AR(1) with |&phi;| &lt; 1; white noise; the growth rate of most macro series; the interest-rate spread.",
                  "Not stationary: a random walk; a series with a trend; a series whose variance grows; a series with a break in its mean.",
                  "Trend-stationary: stationary around a deterministic trend (rare in practice).",
                  "I(1): stationary after one difference (most macro levels). I(2): needs two (some price levels, rarely).",
                  "Cointegrated: a set of I(1) series with a stationary combination (section 07)."]},
                        {"t": "hbox", "color": "amber", "html": "'The series was found to be "
                         "stationary at first difference' is the sentence in every South "
                         "Asian applied paper. What follows it decides whether the paper is "
                         "right."}]},
         ]},

        {"type": "content", "label": "The Random Walk", "title": "The random walk, and why it fools the eye",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "<em>y<sub>t</sub></em> = <em>y<sub>t&minus;1</sub></em> "
                        "+ &epsilon;<sub>t</sub>. Each period adds a fresh shock and nothing is "
                        "forgotten, so <em>y<sub>t</sub></em> is the sum of every shock since "
                        "the start: its variance is <em>t</em>&sigma;&sup2; and grows without "
                        "bound. Plotted, a random walk shows long swings that look like trends "
                        "and cycles, and no two simulated random walks look alike. Every one "
                        "of those 'trends' is noise accumulated."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "The best forecast of a random walk is its last value, at every horizon. Elaborate models of exchange rates rarely beat it (Meese and Rogoff, <em>Journal of International Economics</em> 1983, 14:3).",
                           "With drift, <em>y<sub>t</sub></em> = &delta; + <em>y<sub>t&minus;1</sub></em> + &epsilon;<sub>t</sub>: a trend plus wandering. Most nominal macro levels look like this.",
                           "The ACF of a random walk decays very slowly from near one. That pattern, in a sample ACF, is the first warning."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Simulate it once", "html":
                         "Generate 200 draws of white noise, take the cumulative sum, plot. "
                         "Repeat five times. The five plots will show 'trends' up and down, "
                         "'cycles' of varying length, apparent 'breaks', and no two alike. "
                         "Then regress one on another and read the t-statistic. Ten minutes "
                         "in R or Python (<em>cumsum(rnorm(200))</em>) teaches more about "
                         "non-stationarity than any test."},
                        {"t": "hbox", "color": "green", "html": "Everything in section 07 "
                         "about spurious regression follows from this slide."}]},
         ]},

        {"type": "content", "label": "The ADF Test", "title": "The augmented Dickey-Fuller test: the regression and the null",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "The test regression", "html":
                         "&Delta;<em>y<sub>t</sub></em> = &alpha; + &beta;<em>t</em> + &gamma;<em>y<sub>t&minus;1</sub></em> "
                         "+ &Sigma;<sub>i=1..p</sub> &delta;<sub>i</sub> &Delta;<em>y<sub>t&minus;i</sub></em> + &epsilon;<sub>t</sub><br><br>"
                         "<strong>H<sub>0</sub></strong>: &gamma; = 0 (unit root; the series is I(1)).<br>"
                         "<strong>H<sub>1</sub></strong>: &gamma; &lt; 0 (stationary, or trend-stationary if &beta; is included).<br><br>"
                         "The statistic is the t-ratio on &gamma;, but under H<sub>0</sub> it "
                         "does not follow the t distribution. Dickey and Fuller (<em>JASA</em> "
                         "1979, 74:427) tabulated its distribution; MacKinnon's response "
                         "surfaces give the critical values software reports. The lagged "
                         "differences (the 'augmentation') soak up serial correlation so "
                         "&epsilon;<sub>t</sub> is white noise."},
                        {"t": "body", "cls": "sm", "html": "The null is non-stationarity. "
                         "Failing to reject means 'we could not show it is stationary', not "
                         "'it is a random walk'. The test has low power against near-unit "
                         "roots (&phi; = 0.95) in samples of the size applied work has."}],
              "right": [{"t": "bullets", "color": "amber", "items": [
                  "<strong>Deterministic terms</strong>: none, constant, or constant and trend. Choose by looking at the plot: a series that trends needs the trend term under the alternative. Critical values differ across the three cases.",
                  "<strong>Lag length</strong> <em>p</em>: by AIC or BIC over a range, or Ng-Perron's modified criteria; too few lags leaves autocorrelation and biases the test, too many loses power. Report the choice.",
                  "<strong>Report</strong>: the statistic, the critical value at 5%, the deterministic terms, the lags, the sample. 'ADF = &minus;1.84, not rejected' with nothing else is uninterpretable.",
                  "<strong>Then</strong> test the first difference. If the level is not rejected and the difference is, the series is I(1)."]},
                        {"t": "hbox", "color": "red", "html": "A common error: including a trend "
                         "term for a series that does not trend, which throws away power; or "
                         "omitting it for one that does, which biases toward non-rejection."}]},
         ]},

        {"type": "content", "label": "Other Tests", "title": "KPSS, Phillips-Perron, and using them together",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Test", "Null hypothesis", "How it differs from ADF", "Use it for"],
              "rows": [
                  ["ADF (Dickey-Fuller 1979; Said-Dickey 1984)", "Unit root", "Parametric augmentation with lagged differences", "The default; always report"],
                  ["Phillips-Perron (<em>Biometrika</em> 1988, 75:335)", "Unit root", "Non-parametric correction for serial correlation and heteroskedasticity", "A check on ADF; behaves badly with large negative MA components"],
                  ["KPSS (Kwiatkowski et al., <em>J Econometrics</em> 1992, 54:159)", "<strong>Stationarity</strong>", "The null is reversed; rejection means non-stationary", "Confirmatory: ADF not rejected + KPSS rejected is strong evidence of I(1)"],
                  ["DF-GLS (Elliott, Rothenberg, Stock, <em>Econometrica</em> 1996, 64:813)", "Unit root", "GLS-detrends first; more power near the null", "Small samples; near-unit-root alternatives"],
                  ["Ng-Perron (2001)", "Unit root", "Modified statistics and lag selection; good size and power", "When results are borderline"],
                  ["Zivot-Andrews (<em>JBES</em> 1992, 10:251)", "Unit root, with no break", "Allows one endogenous break under the alternative", "Series with a visible break (2016, 2020); see section 09"],
                  ["HEGY (1990)", "Seasonal unit roots", "Tests at seasonal frequencies", "Monthly and quarterly data with strong seasonality"]]},
             {"t": "body", "cls": "sm", "html": "The confirmatory pair is ADF and KPSS. If ADF "
              "does not reject a unit root and KPSS rejects stationarity, the series is I(1) "
              "and both tests agree. If both reject, or neither does, the data are not "
              "informative enough and the paper should say so rather than pick the "
              "convenient result. Papers that run six tests and report the one that suited "
              "the model are common and are read as such."},
         ]},

        {"type": "content", "label": "Worked ADF", "title": "A worked unit-root test: log real GDP, quarterly",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Series", "Terms", "Lags (AIC)", "ADF statistic", "5% critical value", "KPSS", "Conclusion"],
                        "rows": [
                            ["log GDP (level)", "Constant, trend", "3", "&minus;2.11", "&minus;3.45", "0.19* (crit 0.146)", "Unit root not rejected; stationarity rejected: I(1)"],
                            ["&Delta; log GDP", "Constant", "2", "&minus;5.87", "&minus;2.89", "0.09 (crit 0.463)", "Unit root rejected; stationarity not rejected: I(0)"],
                            ["log CPI (level)", "Constant, trend", "4", "&minus;1.62", "&minus;3.45", "0.24*", "I(1), possibly I(2): test the second difference"],
                            ["&Delta; log CPI (inflation)", "Constant", "3", "&minus;3.41", "&minus;2.89", "0.31", "Rejected at 5%, borderline; note the 2020 break"]]},
                       {"t": "body", "cls": "sm", "html": "Illustrative statistics with "
                        "realistic magnitudes; critical values are MacKinnon's for about 100 "
                        "observations. The KPSS critical values differ between the trend case "
                        "(0.146) and the constant case (0.463)."}],
              "right": [{"t": "panel", "color": "cyan", "title": "What the table settles", "html":
                         "GDP and CPI enter any regression in growth rates or in an error-"
                         "correction form, never in log levels by OLS. Inflation is stationary "
                         "enough to model directly, with a dummy or a break test for 2020. "
                         "The lag choices and the deterministic terms are in the table "
                         "because a reader who disagrees with them can see what changes."},
                        {"t": "hbox", "color": "amber", "html": "Two decimal places and the "
                         "critical value beside every statistic. A star alone hides the "
                         "margin."}]},
         ]},

        {"type": "content", "label": "Power and Breaks", "title": "Why unit-root tests fail: power, breaks and the near-unit root",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "With sixty quarterly observations, the ADF test "
                        "has perhaps a one-in-three chance of rejecting a unit root when the "
                        "true autoregressive coefficient is 0.9. A stationary but persistent "
                        "series will therefore be labelled I(1) most of the time, and the "
                        "label decides the model. The test also assumes no break: Perron "
                        "(<em>Econometrica</em> 1989, 57:1361) showed that a stationary series "
                        "with one shift in its mean or trend is nearly always classified as a "
                        "unit root by ADF."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Longer span beats higher frequency: forty years of annual data have more power than ten years of monthly.",
                           "Use DF-GLS or Ng-Perron when the sample is short and the result matters.",
                           "If the plot shows a break, use a break-allowing test (section 09) or split the sample, and say so.",
                           "Treat the classification as a working assumption, and check that the substantive result survives the other classification."]}],
              "right": [{"t": "panel", "color": "amber", "title": "The economist's escape", "html":
                         "The ARDL bounds test (section 07) was designed for exactly this "
                         "uncertainty: it allows the regressors to be I(0), I(1) or a mix, "
                         "and asks about the long-run relationship without first settling "
                         "each series' order. That is why it dominates applied work in "
                         "South Asian journals. It still requires that nothing is I(2), so "
                         "the unit-root tests are run anyway, on the differences."},
                        {"t": "hbox", "color": "green", "html": "The honest sentence: 'Tests "
                         "cannot distinguish a unit root from a root of 0.95 in this sample; "
                         "we proceed under I(1) and show in Appendix B that the conclusions "
                         "hold under trend-stationarity.'"}]},
         ]},

        {"type": "content", "label": "Differencing", "title": "How many differences, and the cost of too many",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Difference until the tests say the series is "
                        "stationary and no further. One difference removes a stochastic trend; "
                        "a seasonal difference removes stable seasonality; a second ordinary "
                        "difference is needed only when the growth rate itself wanders, which "
                        "is unusual outside high-inflation episodes. Each difference costs "
                        "observations and, if unnecessary, introduces a non-invertible "
                        "moving-average term that ARIMA estimation handles badly."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Diagnostics for over-differencing: the lag-1 autocorrelation of the differenced series near &minus;0.5; the variance of the series rising after differencing rather than falling.",
                           "Order of operations: transform (logs), then seasonal difference if needed, then ordinary difference, then test.",
                           "A series that needs two differences in a model is often a series with a break in a model without one."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Differencing versus modelling the level", "html":
                         "Differencing throws away the long-run information in the levels. "
                         "For a forecasting model of one series, that is a price worth "
                         "paying. For a question about the long-run relationship between "
                         "two series (does money growth drive inflation in the long run?), "
                         "differencing removes exactly what the question is about, and the "
                         "answer is cointegration and error correction, which keep the "
                         "levels and the differences both. Section 07."},
                        {"t": "hbox", "color": "green", "html": "The <em>ndiffs()</em> and "
                         "<em>nsdiffs()</em> functions in R's <em>forecast</em> package "
                         "apply these tests automatically. Read what they chose and why "
                         "before accepting it."}]},
         ]},

        {"type": "content", "label": "Panels", "title": "Panel unit roots: many short series instead of one long one",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Twenty years of annual data for one state cannot "
                        "settle whether a series has a unit root. Twenty years for 28 states "
                        "can, if the states' series share the property. Panel unit-root tests "
                        "pool the information: Levin, Lin and Chu (<em>Journal of Econometrics</em> "
                        "2002, 108:1) assume a common autoregressive coefficient; Im, Pesaran "
                        "and Shin (2003, 115:53) average individual ADF statistics and allow "
                        "each state its own; Fisher-type tests combine the individual "
                        "p-values."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "The null is that all series have a unit root; the alternative differs by test (all stationary, or some), and the difference matters for what a rejection means.",
                           "Cross-sectional dependence, which Indian states have in abundance through common national shocks, biases the first-generation tests toward rejection. Pesaran's CIPS test (2007) allows it.",
                           "Panel cointegration follows the same logic: Pedroni, Kao, and Westerlund's tests, then the pooled mean group ARDL for the long-run coefficients."]}],
              "right": [{"t": "panel", "color": "amber", "title": "What pooling assumes", "html":
                         "That the question is about the states in general, and that a "
                         "common answer means something. A panel test that rejects a unit "
                         "root for state per capita income is not a finding about Bihar; it "
                         "is a finding that not every state's income is a random walk. For "
                         "a question about one state, the panel adds nothing and the short "
                         "series stays short."},
                        {"t": "hbox", "color": "green", "html": "Test for cross-sectional "
                         "dependence first (Pesaran's CD test). If it is there, and it will "
                         "be, use the second-generation tests and say so."}]},
         ]},

        {"type": "content", "label": "Reporting", "title": "Reporting unit-root results so a reader can check them",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "One table, all series, level and first difference, for every test used.",
                  "Columns: deterministic terms, lag length and how chosen, statistic, 5% (and 1%) critical value or p-value, conclusion.",
                  "The sample period and any adjustments (logs, seasonal adjustment, splicing) in the note.",
                  "Where tests disagree, say so in the text and say what you did.",
                  "Where a break is visible, the break-allowing test alongside the standard one."]}],
              "right": [{"t": "panel", "color": "amber", "title": "What not to write", "html":
                         "'All variables were found to be stationary at first difference and "
                         "hence the Johansen cointegration test was applied.' Three claims in "
                         "one sentence, none of them shown: which tests, at what lag, with "
                         "what terms, with what margin, and why Johansen rather than ARDL. "
                         "Referees at good journals now reject on this sentence alone, and "
                         "they are right to, because the sentence is where a wrong "
                         "classification becomes a wrong model."},
                        {"t": "hbox", "color": "green", "html": "The unit-root table is an "
                         "appendix table in a good paper and the whole methods section in a "
                         "weak one."}]},
         ]},

        # ===================== SECTION 04: ARIMA MODELLING =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "ARIMA Modelling"},

        {"type": "content", "label": "AR, MA, ARMA", "title": "Autoregressive and moving-average processes",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "AR(p)", "html":
                         "<em>y<sub>t</sub></em> = <em>c</em> + &phi;<sub>1</sub><em>y<sub>t&minus;1</sub></em> + ... + "
                         "&phi;<sub>p</sub><em>y<sub>t&minus;p</sub></em> + &epsilon;<sub>t</sub>. Today "
                         "depends on its own past. Stationary if the roots of the "
                         "characteristic polynomial lie outside the unit circle; for AR(1), "
                         "|&phi;<sub>1</sub>| &lt; 1. A shock decays geometrically."},
                        {"t": "panel", "color": "amber", "title": "MA(q)", "html":
                         "<em>y<sub>t</sub></em> = &mu; + &epsilon;<sub>t</sub> + &theta;<sub>1</sub>&epsilon;<sub>t&minus;1</sub> "
                         "+ ... + &theta;<sub>q</sub>&epsilon;<sub>t&minus;q</sub>. Today depends on "
                         "recent shocks. Always stationary; a shock lasts exactly <em>q</em> "
                         "periods. Invertible (expressible as an infinite AR) if the roots "
                         "condition holds, which estimation requires."},
                        {"t": "panel", "color": "green", "title": "ARMA(p, q)", "html":
                         "Both together. Parsimonious: an ARMA(1,1) can mimic a long AR. Box "
                         "and Jenkins (1970) built the identify-estimate-check cycle around "
                         "it."}],
              "right": [{"t": "body", "html": "The point of the family is that a stationary "
                        "series' autocorrelation structure, however complicated, can usually "
                        "be reproduced with a few parameters, and a model that reproduces "
                        "the autocorrelation forecasts well. Nothing in the model is about "
                        "economics; it is a description of the series' memory."},
                        {"t": "table",
                         "head": ["Process", "ACF", "PACF"],
                         "rows": [
                             ["AR(p)", "Decays (geometric or damped sine)", "Cuts off after lag <em>p</em>"],
                             ["MA(q)", "Cuts off after lag <em>q</em>", "Decays"],
                             ["ARMA(p, q)", "Decays after lag <em>q</em>", "Decays after lag <em>p</em>"]]},
                        {"t": "hbox", "color": "cyan", "html": "Wold's theorem: any stationary "
                         "series can be written as an MA(&infin;). ARMA is the practical "
                         "approximation."}]},
         ]},

        {"type": "content", "label": "ARIMA", "title": "ARIMA(p, d, q): differencing brought inside the model",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "An ARIMA(<em>p</em>, <em>d</em>, <em>q</em>) model "
                        "is an ARMA(<em>p</em>, <em>q</em>) fitted to the <em>d</em>-th "
                        "difference of the series. ARIMA(0,1,0) is the random walk; "
                        "ARIMA(0,1,1) is simple exponential smoothing; ARIMA(1,1,0) is a "
                        "series whose growth rate is AR(1). The <em>d</em> comes from section "
                        "03, <em>p</em> and <em>q</em> from the ACF and PACF of the "
                        "differenced series or from an information criterion, and the "
                        "forecasts are integrated back to levels."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Include a constant when <em>d</em> = 0 (it is the mean) or when <em>d</em> = 1 and the series drifts (it is the drift). Software defaults differ; check.",
                           "Keep <em>p</em> + <em>q</em> small. An ARIMA(5,1,5) on 80 observations fits the noise.",
                           "Estimate by maximum likelihood; conditional sum of squares is an older approximation that some packages still default to."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Seasonal ARIMA", "html":
                         "ARIMA(<em>p</em>,<em>d</em>,<em>q</em>)(<em>P</em>,<em>D</em>,<em>Q</em>)<sub>s</sub> "
                         "adds seasonal AR, differencing and MA terms at lag <em>s</em> "
                         "(12 for monthly, 4 for quarterly). The 'airline model', "
                         "ARIMA(0,1,1)(0,1,1)<sub>12</sub>, fits a remarkable share of "
                         "monthly economic series and is the sensible first candidate. "
                         "Seasonal differencing (<em>D</em> = 1) is usually enough; "
                         "<em>D</em> = 2 is almost never right."},
                        {"t": "hbox", "color": "green", "html": "Write the model out in full "
                         "in the paper, with the estimated coefficients and their standard "
                         "errors. 'An ARIMA model was fitted' is not a method."}]},
         ]},

        {"type": "content", "label": "Box-Jenkins", "title": "The Box-Jenkins cycle: identify, estimate, check, forecast",
         "blocks": [
             {"t": "flow", "steps": [
                 "TRANSFORM: logs if variance grows; note the seasonality",
                 "DIFFERENCE: d and D from the tests and the ACF",
                 "IDENTIFY: p, q, P, Q from the ACF/PACF of the differenced series, or an information-criterion search",
                 "ESTIMATE: maximum likelihood; check the coefficients are significant and the roots are inside bounds",
                 "CHECK: residual ACF flat; Ljung-Box not rejected; residuals roughly normal; no outliers left",
                 "FORECAST: with intervals; compare with a benchmark (section 06)"]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The cycle is iterative: a failed check sends you "
                        "back to identification. Two candidate models that both pass the "
                        "checks are compared on AIC or BIC (lower is better; BIC penalises "
                        "parameters more) and, where forecasting is the aim, on out-of-sample "
                        "accuracy. Report the models that were tried, not only the winner."}],
              "right": [{"t": "hbox", "color": "amber", "html": "Information criteria compare "
                        "models with the same <em>d</em> and <em>D</em> on the same sample. "
                        "An AIC from a model of levels and one from a model of differences "
                        "are not comparable, because the likelihoods are of different "
                        "series."}]},
         ]},

        {"type": "content", "label": "Worked ARIMA", "title": "A worked identification: monthly inflation",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Candidate", "Parameters", "Log-likelihood", "AIC", "BIC", "Ljung-Box (24 lags) p", "Verdict"],
                        "rows": [
                            ["ARIMA(1,0,0)", "&phi;<sub>1</sub> = 0.62 (0.07)", "&minus;188.4", "382.8", "391.1", "0.003", "Residuals autocorrelated; seasonality missed"],
                            ["ARIMA(1,0,0)(1,0,0)<sub>12</sub>", "&phi;<sub>1</sub> = 0.58 (0.07); &Phi;<sub>1</sub> = 0.31 (0.09)", "&minus;176.1", "360.2", "371.2", "0.21", "Passes; best BIC"],
                            ["ARIMA(2,0,1)(1,0,0)<sub>12</sub>", "Four parameters; &theta;<sub>1</sub> insignificant", "&minus;175.4", "362.8", "379.4", "0.24", "No better; drop"],
                            ["ARIMA(0,1,1)(0,1,1)<sub>12</sub>", "Airline model on the level of the index", "n/a: different d", "n/a", "n/a", "0.18", "A model of the price index, not of inflation; compare on forecasts only"]]},
                       {"t": "body", "cls": "sm", "html": "Illustrative, for 132 months of "
                        "year-on-year CPI inflation, which the section 03 tests classed as "
                        "I(0). Standard errors in parentheses. The seasonal AR term is what "
                        "the residual check demanded; the extra ARMA terms bought nothing."}],
              "right": [{"t": "panel", "color": "cyan", "title": "Reading the coefficients", "html":
                         "&phi;<sub>1</sub> = 0.58: about 58% of last month's deviation from "
                         "mean inflation carries into this month; a shock has a half-life of "
                         "about 1.3 months (log 0.5 / log 0.58). &Phi;<sub>1</sub> = 0.31: "
                         "this month resembles the same month last year, which is the "
                         "seasonal food-price pattern. The mean of the series, 5.1%, is the "
                         "level forecasts revert to."},
                        {"t": "hbox", "color": "amber", "html": "The half-life is the number "
                         "a policymaker understands. Report it beside the coefficient."}]},
         ]},

        {"type": "content", "label": "Diagnostics", "title": "Residual checks: what a good model leaves behind",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Check", "How", "Pass looks like", "Fail means"],
              "rows": [
                  ["Residual autocorrelation", "ACF of residuals; Ljung-Box at 10&ndash;24 lags", "All bars inside the band; p &gt; 0.05", "Structure missed: add AR/MA or seasonal terms"],
                  ["Residual mean", "t-test that the mean is zero", "Near zero", "Constant or drift mis-specified"],
                  ["Constant variance", "Plot residuals over time; ARCH-LM test", "No fanning; ARCH not rejected", "Variance changes: logs, or a GARCH model (section 09)"],
                  ["Normality", "Histogram, QQ plot, Jarque-Bera", "Roughly normal", "Prediction intervals wrong; outliers present; consider bootstrapped intervals"],
                  ["Outliers", "Standardised residuals beyond &plusmn;3", "None, or explained (demonetisation, lockdown)", "Add an intervention dummy; do not delete the observation"],
                  ["Parameter stability", "Recursive estimates; CUSUM", "Stable", "A break; split the sample or model it"],
                  ["Roots", "Inverse AR and MA roots inside the unit circle, not near it", "Well inside", "Near-cancelling roots (p and q both too high) or non-invertibility"]]},
             {"t": "body", "cls": "sm", "html": "A model that passes every check is not "
              "thereby the right model; it is a model the data do not contradict. Two such "
              "models often exist. The forecast comparison in section 06 is what "
              "separates them."},
         ]},

        {"type": "content", "label": "Automatic Selection", "title": "auto.arima and its cousins: use them, and check them",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Hyndman and Khandakar's algorithm (<em>Journal "
                        "of Statistical Software</em> 2008, 27(3)), in R's <em>forecast</em> "
                        "and <em>fable</em> packages and Python's <em>pmdarima</em>, chooses "
                        "<em>d</em> and <em>D</em> by unit-root tests and then searches over "
                        "<em>p</em>, <em>q</em>, <em>P</em>, <em>Q</em> by AICc with a "
                        "stepwise procedure. It is fast, reproducible, and usually lands near "
                        "what a careful analyst would choose. It is also a starting point, "
                        "not a verdict."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Read what it chose and why. The unit-root decision is the one to check by hand.",
                           "Run the residual checks on its model as on any other.",
                           "Compare with the simplest reasonable model (seasonal naive; the airline model). If the automatic choice does not beat them out of sample, use the simple one.",
                           "Set <em>stepwise = FALSE</em> for a full search when the series matters; it takes longer and occasionally finds a better model."]}],
              "right": [{"t": "panel", "color": "amber", "title": "In Stata, EViews and gretl", "html":
                         "Stata's <em>arima</em> command estimates a specified model; there is "
                         "no built-in search, and analysts loop over orders and compare "
                         "<em>estat ic</em>. EViews has an automatic ARIMA forecasting "
                         "procedure in recent versions. gretl, free and menu-driven, "
                         "estimates ARIMA with exact ML and shows the roots and the "
                         "correlogram in one window, which makes it the best free "
                         "teaching tool for this section."},
                        {"t": "hbox", "color": "green", "html": "Whatever picked the model, "
                         "the paper reports the model, the alternatives, the criteria and "
                         "the checks. The software is a footnote."}]},
         ]},

        {"type": "content", "label": "Intervention", "title": "Intervention dummies and outliers: demonetisation, lockdown, a policy change",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A known event that hits a series is modelled, "
                        "not deleted. A <strong>pulse</strong> dummy (1 in one period) "
                        "captures a one-off; a <strong>step</strong> dummy (1 from a date "
                        "onward) captures a permanent shift; a step passed through the "
                        "model's dynamics captures a shift that arrives gradually. India's "
                        "series carry several: November 2016 (demonetisation), July 2017 "
                        "(GST), April 2020 (lockdown), and base-year revisions that need "
                        "splicing rather than dummies."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "The dummy's coefficient is the estimated size of the event's effect, with a standard error; report it.",
                           "Without the dummy, the event inflates the residual variance and widens every forecast interval, and it may push the unit-root tests toward non-rejection.",
                           "A model with a 2020 dummy is a model that says 2020 was unlike other years. That is usually right, and it means the model has learned nothing about pandemics."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Automatic outlier detection", "html":
                         "X-13 and the <em>tsoutliers</em> R package find additive outliers, "
                         "level shifts and temporary changes by search. Useful for a long "
                         "series with events you do not know about; dangerous when it "
                         "finds a level shift where the analyst would have found a trend "
                         "change. Every detected outlier should be matched to something "
                         "that happened; one that cannot be is a warning about the data."},
                        {"t": "hbox", "color": "red", "html": "Deleting the observation and "
                         "interpolating is falsification if it is not disclosed, and it is "
                         "wrong even when disclosed: the event happened."}]},
         ]},

        {"type": "content", "label": "ARIMA Forecasts", "title": "Forecasting from ARIMA: point forecasts and intervals",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The one-step forecast substitutes the last "
                        "observed values and the last residuals into the model; the two-step "
                        "forecast substitutes the one-step forecast, and so on. For a "
                        "stationary ARMA the forecasts converge to the mean and the interval "
                        "widens to the unconditional variance; for an I(1) model the forecasts "
                        "follow the drift and the interval widens without limit, at a rate "
                        "proportional to &radic;<em>h</em>."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Report the point forecast with 80% and 95% intervals, on a plot with the history. A point forecast alone is a guess dressed up.",
                           "Intervals assume normal, homoskedastic, uncorrelated residuals and a correctly specified model. They are too narrow in practice; simulation or bootstrap intervals help.",
                           "Forecasts of a logged series are back-transformed; the median forecast is exp(forecast), and the mean needs a bias correction of half the variance.",
                           "Forecasts beyond about two seasonal cycles from an ARIMA are the mean plus the trend, whatever the model says."]}],
              "right": [{"t": "panel", "color": "amber", "title": "What the interval says", "html":
                         "An 80% interval for inflation twelve months out of 3.2% to 7.4% "
                         "is the honest statement of what the model knows. Users who want "
                         "'the number' are asking for the midpoint and will hold you to it; "
                         "give them the interval in the same sentence. The RBI's fan charts "
                         "in the Monetary Policy Report are the model for the presentation."},
                        {"t": "hbox", "color": "green", "html": "Every forecast in this course "
                         "is judged in section 06 against a benchmark it must beat. An ARIMA "
                         "that does not beat the seasonal naive forecast should not be "
                         "published as a forecasting model."}]},
         ]},

        # ===================== SECTION 05: EXPONENTIAL SMOOTHING AND FORECASTING =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Exponential Smoothing and Forecasting"},

        {"type": "content", "label": "Benchmarks", "title": "The four benchmarks every forecast must beat",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Method", "Forecast", "Right for"],
                        "rows": [
                            ["Mean", "The historical average", "Stationary, no trend, no season"],
                            ["Naive", "The last value", "Random walks; most financial series"],
                            ["Seasonal naive", "The value from the same season last year", "Strongly seasonal series with little trend"],
                            ["Drift", "The last value plus the average historical change", "Trending series"]]},
                       {"t": "body", "cls": "sm", "html": "Each costs nothing to compute and "
                        "each is hard to beat on the right kind of series. The M-competitions "
                        "(Makridakis and Hibon, <em>International Journal of Forecasting</em> "
                        "2000, 16:451; M4, Makridakis and colleagues, 2020, 36:54) found "
                        "repeatedly that simple methods forecast about as well as complex "
                        "ones and that combinations of methods beat most single methods."}],
              "right": [{"t": "panel", "color": "cyan", "title": "The rule", "html":
                         "A forecasting model earns its place by beating the appropriate "
                         "benchmark out of sample by a margin large enough to matter, on "
                         "the horizon that matters. A monthly disease model that beats "
                         "seasonal naive by 3% on one-month-ahead RMSE and loses to it at "
                         "six months is a model for one horizon. A paper that presents a "
                         "model with no benchmark comparison has not shown it forecasts."},
                        {"t": "hbox", "color": "amber", "html": "'Our model achieved a MAPE "
                         "of 4.2%' means nothing without the benchmark's MAPE beside it."}]},
         ]},

        {"type": "content", "label": "Simple Smoothing", "title": "Simple exponential smoothing: a weighted average that forgets",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The forecast is a weighted average of past "
                        "observations with weights that decline geometrically: "
                        "<em>&#375;<sub>t+1</sub></em> = &alpha;<em>y<sub>t</sub></em> + "
                        "(1 &minus; &alpha;)<em>&#375;<sub>t</sub></em>, with 0 &lt; &alpha; &lt; 1. "
                        "A large &alpha; trusts the latest observation; a small one averages "
                        "over a long memory. &alpha; is estimated by minimising the one-step "
                        "squared errors. The forecast is flat: the same number at every "
                        "horizon."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Equivalent to ARIMA(0,1,1); the two families overlap heavily.",
                           "Right for a series with no trend and no seasonality that drifts slowly: a stable programme's monthly caseload.",
                           "An &alpha; near 1 means the series is nearly a random walk and the naive forecast would do as well."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Holt's linear trend and the damped trend", "html":
                         "Holt's method adds a second smoothing equation for the slope, so "
                         "the forecast is a line. Gardner and McKenzie's damped trend "
                         "(1985) multiplies the slope by &phi;<sup>h</sup> so the line flattens "
                         "with the horizon, which is what long-run growth usually does; it "
                         "was one of the best single methods in the M3 competition. Use "
                         "damped unless there is a reason to believe the trend continues "
                         "unchecked."},
                        {"t": "hbox", "color": "green", "html": "Three parameters (&alpha;, "
                         "&beta;, &phi;), a level and a slope. Everything is interpretable and "
                         "a spreadsheet can do it."}]},
         ]},

        {"type": "content", "label": "Holt-Winters", "title": "Holt-Winters: level, trend and season together",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Component", "Additive", "Multiplicative"],
                        "rows": [
                            ["Level", "&ell;<sub>t</sub> = &alpha;(<em>y<sub>t</sub></em> &minus; <em>s<sub>t&minus;m</sub></em>) + (1 &minus; &alpha;)(&ell;<sub>t&minus;1</sub> + <em>b<sub>t&minus;1</sub></em>)", "&ell;<sub>t</sub> = &alpha;(<em>y<sub>t</sub></em> / <em>s<sub>t&minus;m</sub></em>) + (1 &minus; &alpha;)(&ell;<sub>t&minus;1</sub> + <em>b<sub>t&minus;1</sub></em>)"],
                            ["Trend", "<em>b<sub>t</sub></em> = &beta;(&ell;<sub>t</sub> &minus; &ell;<sub>t&minus;1</sub>) + (1 &minus; &beta;)<em>b<sub>t&minus;1</sub></em>", "Same"],
                            ["Season", "<em>s<sub>t</sub></em> = &gamma;(<em>y<sub>t</sub></em> &minus; &ell;<sub>t&minus;1</sub> &minus; <em>b<sub>t&minus;1</sub></em>) + (1 &minus; &gamma;)<em>s<sub>t&minus;m</sub></em>", "<em>s<sub>t</sub></em> = &gamma;(<em>y<sub>t</sub></em> / (&ell;<sub>t&minus;1</sub> + <em>b<sub>t&minus;1</sub></em>)) + (1 &minus; &gamma;)<em>s<sub>t&minus;m</sub></em>"],
                            ["Forecast", "&ell;<sub>t</sub> + <em>h b<sub>t</sub></em> + <em>s<sub>t+h&minus;m</sub></em>", "(&ell;<sub>t</sub> + <em>h b<sub>t</sub></em>) <em>s<sub>t+h&minus;m</sub></em>"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "Three smoothing parameters, a level, "
                        "a slope and <em>m</em> seasonal indices, updated each period. "
                        "Additive when the seasonal swing is constant in size; multiplicative "
                        "when it scales with the level, which is the common case for counts "
                        "and sales. With a damped trend it is the workhorse for monthly "
                        "operational forecasting: clinic loads, stock requirements, "
                        "collections."},
                        {"t": "hbox", "color": "cyan", "html": "Needs at least two full "
                         "seasons to initialise, and three or four to estimate the seasonal "
                         "indices with any confidence."}]},
         ]},

        {"type": "content", "label": "ETS", "title": "The ETS framework: smoothing as a statistical model",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Hyndman, Koehler, Ord and Snyder (<em>Forecasting "
                        "with Exponential Smoothing</em>, Springer, 2008) showed that every "
                        "smoothing method is the forecast function of a state-space model "
                        "with Error, Trend and Seasonal components, each Additive, "
                        "Multiplicative, Damped or None. ETS(A,N,N) is simple smoothing; "
                        "ETS(A,Ad,M) is damped Holt-Winters with multiplicative seasonality. "
                        "The state-space form gives likelihoods, so models are chosen by "
                        "AICc and forecast intervals come from the model rather than from "
                        "ad hoc formulas."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "In R: <em>ets()</em> in <em>forecast</em>, <em>ETS()</em> in <em>fable</em>; both select automatically by AICc.",
                           "Thirty models in the family; automatic selection is reliable, and the residual checks apply as for ARIMA.",
                           "ETS and ARIMA overlap but are not nested. Fit both, compare out of sample, or combine them."]}],
              "right": [{"t": "panel", "color": "amber", "title": "When to prefer which", "html":
                         "ETS handles multiplicative seasonality natively and is usually "
                         "better on short, seasonal, operational series. ARIMA handles "
                         "autocorrelation structures ETS cannot express, admits regressors "
                         "cleanly (section 07), and links to the econometric tradition. "
                         "For a monthly operational series with three to eight years of "
                         "history, fit both and average; for a macro series entering a "
                         "structural question, ARIMA with regressors."},
                        {"t": "hbox", "color": "green", "html": "The M4 competition's best "
                         "entries were combinations of ETS, ARIMA and theta, with a "
                         "little machine learning on top. Simple average of two good models "
                         "beats either."}]},
         ]},

        {"type": "content", "label": "Regressors", "title": "Adding regressors: dynamic regression and regARIMA",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A forecast of clinic attendance can use "
                        "rainfall; a forecast of mandi prices can use the sown area. A "
                        "regression with ARIMA errors, <em>y<sub>t</sub></em> = &beta;<em>x<sub>t</sub></em> "
                        "+ &eta;<sub>t</sub> with &eta;<sub>t</sub> following an ARIMA process, "
                        "keeps the regressor's effect and lets the error carry the series' "
                        "memory. OLS with the same regressor and autocorrelated errors gives "
                        "the right &beta; and the wrong standard error; the ARIMA errors fix "
                        "both."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "To forecast <em>y</em> you need forecasts of <em>x</em>, or a lagged <em>x</em> that is already known. A regressor you must also forecast adds its own uncertainty to the interval.",
                           "Deterministic regressors (dummies for holidays, a trend, Fourier terms for long seasonal periods) are always known ahead and are the common case.",
                           "Both <em>y</em> and <em>x</em> should be stationary, or both differenced, or the model becomes section 07's problem."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Fourier terms and long seasons", "html":
                         "Daily data with a yearly cycle (365 periods) cannot be handled by "
                         "seasonal ARIMA. Fourier terms, a few sine and cosine pairs at the "
                         "yearly frequency, as regressors with ARIMA errors, capture the "
                         "annual shape with three to six parameters; weekly seasonality "
                         "is then handled by the ARIMA part or by day-of-week dummies. "
                         "This is the standard treatment for daily AQI, hospital admissions "
                         "and electricity demand."},
                        {"t": "hbox", "color": "green", "html": "In R, <em>auto.arima(y, "
                         "xreg = ...)</em>; in Python, <em>SARIMAX(y, exog = ...)</em>; in "
                         "Stata, <em>arima y x, ar(1)</em>."}]},
         ]},

        {"type": "content", "label": "Hierarchies", "title": "Forecasting many series: hierarchies and reconciliation",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A state programme forecasts caseload for 700 "
                        "blocks, 38 districts and the state. Forecasting each level separately "
                        "produces forecasts that do not add up, and the district forecast "
                        "made from district data ignores what the blocks know. Reconciliation "
                        "methods (bottom-up, top-down, and the optimal 'MinT' combination of "
                        "Wickramasuriya, Athanasopoulos and Hyndman, <em>JASA</em> 2019, "
                        "114:804) produce forecasts at every level that are coherent and, "
                        "usually, more accurate than any single level's."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Bottom-up: forecast the blocks, sum. Noisy at the bottom, but no aggregation bias.",
                           "Top-down: forecast the state, share out by historical proportions. Smooth, and blind to local change.",
                           "MinT: forecast every level, then adjust all of them together using the errors' covariance. Implemented in R's <em>fable</em> (<em>reconcile()</em>)."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Batch forecasting in practice", "html":
                         "Seven hundred series cannot be hand-modelled. Automatic ETS or "
                         "ARIMA per series, a benchmark per series, out-of-sample accuracy "
                         "per series, and a report that names the series where the model "
                         "lost to the benchmark. Those are the districts where something is "
                         "changing, and finding them is more valuable than the forecasts."},
                        {"t": "hbox", "color": "green", "html": "A dashboard that flags the "
                         "blocks whose last three months fell outside their own forecast "
                         "interval is the practical output of everything in sections 04 "
                         "and 05."}]},
         ]},

        {"type": "content", "label": "Judgement", "title": "Judgemental adjustment and combining forecasts",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The statistical forecast does not know that a "
                        "new district hospital opens in March or that the state has announced "
                        "a scheme. The manager does. The evidence on adjusting model forecasts "
                        "by judgement (Fildes and colleagues, <em>International Journal of "
                        "Forecasting</em> 2009, 25:3, on 60,000 adjustments in four firms) is "
                        "that large adjustments made for a stated reason improve accuracy, "
                        "small adjustments made from habit worsen it, and optimistic "
                        "adjustments are the worst."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Record every adjustment with its reason and its size. Review them against outcomes twice a year.",
                           "Adjust for information the model cannot have; never for a feeling that the model is 'too low'.",
                           "Structure the judgement: what will change, from when, by how much, with what confidence."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Combination", "html":
                         "Averaging the forecasts of two or three reasonable models reduces "
                         "error more reliably than choosing among them, because their "
                         "errors are imperfectly correlated. Equal weights are hard to "
                         "beat; estimated weights overfit. Bates and Granger showed it in "
                         "1969 and every competition since has confirmed it. A combination "
                         "of ETS, ARIMA and the seasonal naive is the default production "
                         "forecast for a monthly operational series."},
                        {"t": "hbox", "color": "green", "html": "The forecast is a process, not "
                         "a number: model, benchmark, adjustment log, and a monthly review "
                         "of last month's error."}]},
         ]},

        # ===================== SECTION 06: EVALUATING FORECASTS =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Evaluating Forecasts"},

        {"type": "content", "label": "Out of Sample", "title": "In-sample fit is not forecast accuracy",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A model with enough parameters fits any "
                        "history. R&sup2;, in-sample RMSE and 'the fitted line tracks the "
                        "data closely' say nothing about the next twelve months, and models "
                        "chosen on in-sample fit are systematically overfitted. Accuracy is "
                        "measured on observations the model did not see: hold back the last "
                        "portion of the series, fit on the rest, forecast the holdout, compare."},
                       {"t": "flow", "steps": [
                           "SPLIT: training set to time T&minus;H, test set of the last H periods",
                           "FIT on training; FORECAST H ahead",
                           "SCORE against the test set, by horizon",
                           "REPEAT for the benchmark, the same way",
                           "ROLL: move the origin forward and repeat, so the score is an average over many origins"]}],
              "right": [{"t": "panel", "color": "amber", "title": "Rolling-origin evaluation", "html":
                         "One holdout of twelve months is one draw. Rolling the forecast "
                         "origin forward month by month (time-series cross-validation) gives "
                         "dozens of one-step, two-step, ... twelve-step errors and a reliable "
                         "accuracy profile by horizon. Implemented as <em>tsCV()</em> in R's "
                         "<em>forecast</em> and by <em>stretch_tsibble()</em> in <em>fable</em>. "
                         "It is the standard, and a paper reporting a single holdout should "
                         "say why."},
                        {"t": "hbox", "color": "red", "html": "Random k-fold cross-validation, "
                         "which shuffles observations, is wrong for time series: it lets the "
                         "model see the future. The folds must respect time."}]},
         ]},

        {"type": "content", "label": "Measures", "title": "Accuracy measures: what each rewards and where each breaks",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Measure", "Formula (errors <em>e<sub>t</sub></em> = <em>y<sub>t</sub></em> &minus; <em>&#375;<sub>t</sub></em>)", "Scale", "Breaks when"],
              "rows": [
                  ["MAE", "mean |<em>e<sub>t</sub></em>|", "Units of the series", "Comparing series in different units"],
                  ["RMSE", "&radic;(mean <em>e<sub>t</sub></em>&sup2;)", "Units; penalises large errors", "A few outliers dominate"],
                  ["MAPE", "mean |<em>e<sub>t</sub></em> / <em>y<sub>t</sub></em>| &times; 100", "Percent", "<em>y<sub>t</sub></em> near zero (infinite); asymmetric: over-forecasts penalised less"],
                  ["sMAPE", "mean 2|<em>e<sub>t</sub></em>| / (|<em>y<sub>t</sub></em>| + |<em>&#375;<sub>t</sub></em>|)", "Percent", "Still unstable near zero; used in M3/M4"],
                  ["MASE (Hyndman and Koehler, <em>IJF</em> 2006, 22:679)", "MAE / MAE of the in-sample seasonal naive", "Scale-free; 1 = as good as naive", "Rarely; the recommended default"],
                  ["Interval coverage", "Share of test observations inside the 80% or 95% interval", "Should match the nominal level", "Intervals are too narrow, which they usually are"],
                  ["Pinball / CRPS", "Scores for quantile and distributional forecasts", "Proper scoring rules", "Needs a full predictive distribution"]]},
             {"t": "body", "cls": "sm", "html": "Report MASE and RMSE by horizon, with the "
              "benchmark's values, and the interval coverage. MAPE alone is the commonest "
              "choice in applied papers and the worst: it cannot be computed for a series "
              "with zeros, it rewards under-forecasting, and 'MAPE 4.2%' cannot be compared "
              "across series or against anything."},
         ]},

        {"type": "content", "label": "Comparing Models", "title": "Is the difference real? Diebold-Mariano and its use",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Model A has RMSE 4.1 and model B 4.4 on 36 "
                        "out-of-sample months. Whether that difference is more than noise is "
                        "a testable question: Diebold and Mariano (<em>Journal of Business "
                        "&amp; Economic Statistics</em> 1995, 13:253) test whether the mean "
                        "of the loss differential, <em>d<sub>t</sub></em> = "
                        "<em>e</em><sub>A,t</sub>&sup2; &minus; <em>e</em><sub>B,t</sub>&sup2;, is "
                        "zero, with a standard error that allows the differentials to be "
                        "autocorrelated (as multi-step errors are)."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "In R: <em>dm.test()</em>; in Python: <em>statsmodels</em> has no built-in, but the test is six lines.",
                           "Use the Harvey-Leybourne-Newbold small-sample correction for fewer than about 50 forecasts.",
                           "Compare against the benchmark first, then between candidates. Report the p-value and the loss used.",
                           "A model that is not significantly better than seasonal naive after 36 months is not shown to be better, whatever the RMSE says."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Forecast encompassing", "html":
                         "A different question: does model A's forecast contain all the "
                         "information in model B's? Regress the outcome on both forecasts; "
                         "if B's coefficient is zero, A encompasses B and combination adds "
                         "nothing. If both coefficients matter, combine. This is the "
                         "principled version of 'average them', and it explains why "
                         "averages usually win: models rarely encompass each other."},
                        {"t": "hbox", "color": "green", "html": "Thirty-six evaluation points "
                         "is a small sample for these tests. Say so, and do not report "
                         "three decimal places on the p-value."}]},
         ]},

        {"type": "content", "label": "Worked Evaluation", "title": "A worked evaluation: four models, three horizons",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Model", "MASE h=1", "MASE h=3", "MASE h=12", "80% coverage", "DM vs seasonal naive (h=1)"],
                        "rows": [
                            ["Seasonal naive (benchmark)", "1.00", "1.00", "1.00", "n/a", "&mdash;"],
                            ["ETS(A,Ad,M)", "0.71", "0.78", "0.92", "74%", "p = 0.01"],
                            ["ARIMA(1,0,0)(1,0,0)<sub>12</sub>", "0.74", "0.80", "0.97", "71%", "p = 0.02"],
                            ["ARIMA with rainfall regressor", "0.66", "0.75", "0.95*", "76%", "p &lt; 0.01"],
                            ["Average of ETS and ARIMA", "0.68", "0.74", "0.90", "79%", "p &lt; 0.01"]]},
                       {"t": "body", "cls": "sm", "html": "Illustrative, 48 rolling origins on "
                        "monthly clinic attendance. *Twelve-month-ahead forecasts of rainfall "
                        "were used for the regressor model; its long-horizon advantage "
                        "disappears because rainfall is not forecastable at that range."}],
              "right": [{"t": "panel", "color": "cyan", "title": "What to conclude", "html":
                         "Every model beats the benchmark at short horizons by 25&ndash;35% "
                         "and by almost nothing at twelve months, where seasonality is all "
                         "anyone knows. Coverage below 80% says every model's intervals are "
                         "too narrow; widen them or bootstrap. The combination is the "
                         "production choice: best at three and twelve months, best "
                         "coverage, and no worse than the best single model at one. The "
                         "rainfall model is worth using for one to three months ahead, "
                         "when rainfall is known."},
                        {"t": "hbox", "color": "amber", "html": "This table is the results "
                         "section of a forecasting paper. Everything else is method."}]},
         ]},

        {"type": "content", "label": "Interval Honesty", "title": "Prediction intervals are almost always too narrow",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Model-based intervals account for the error "
                        "term's variance and nothing else. They ignore parameter uncertainty, "
                        "model uncertainty, breaks, and the fact that the future contains "
                        "events the past did not. Empirically, 95% intervals from ARIMA and "
                        "ETS models cover about 80&ndash;90% of outcomes, and macro forecasters' "
                        "intervals have historically done worse. A calibrated interval is one "
                        "whose coverage on the evaluation set matches its label."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Check coverage in the rolling evaluation and report it beside the point accuracy.",
                           "Widen by simulation: bootstrap the residuals, or simulate future paths with parameter draws.",
                           "Conformal methods (calibrate the interval width on held-out errors) give correct coverage by construction and are easy to implement.",
                           "Present fan charts: the 50%, 80% and 95% bands together, so the reader sees the shape of the uncertainty."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Why it matters in the sector", "html":
                         "A stock-out forecast with an interval that is too narrow leads "
                         "to too little buffer stock; a budget forecast with one leads to a "
                         "supplementary demand. The cost of an interval error is asymmetric "
                         "and the decision should use the quantile that matches the "
                         "asymmetry (the 90th percentile of demand, say), not the mean. "
                         "That requires an interval that is right."},
                        {"t": "hbox", "color": "green", "html": "A forecast that says '1,350 "
                         "visits, 80% interval 1,180 to 1,540, based on 48 months, "
                         "coverage checked at 79%' is a forecast a manager can use."}]},
         ]},

        {"type": "content", "label": "Forecasting Pitfalls", "title": "Forecasting pitfalls seen in applied papers",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Pitfall", "What it looks like", "Fix"],
              "rows": [
                  ["No benchmark", "'The ARIMA model achieved MAPE 3.8%'", "Seasonal naive in every table"],
                  ["In-sample accuracy", "R&sup2; = 0.98 reported as forecast performance", "Rolling out-of-sample evaluation"],
                  ["One holdout", "The last 12 months, once", "Rolling origins, accuracy by horizon"],
                  ["MAPE on counts with zeros", "Infinite or absurd values silently dropped", "MASE, RMSE"],
                  ["Test set used for selection", "Best of 30 models on the holdout, reported as the forecast", "Select on a validation set, report on a separate test set, or use rolling evaluation"],
                  ["Forecasting a regressor you do not have", "Next year's rainfall as a known input", "Lagged or forecastable regressors only; report the cost"],
                  ["Long horizons from short samples", "Ten-year forecasts from eight years of data", "Do not; or present as scenarios, not forecasts"],
                  ["Machine learning without a reason", "An LSTM on 96 monthly observations, beaten by ETS", "Fit the simple models first; ML earns its place on long, high-frequency, many-series problems"],
                  ["Point forecasts only", "A single line into the future", "Intervals, with coverage checked"]]},
             {"t": "body", "cls": "sm", "html": "Every row is common in journals that "
              "publish South Asian forecasting work, and every row is a reason a "
              "methods-literate referee rejects. The fixes are all in this section and "
              "none is expensive."},
         ]},

        # ===================== SECTION 07: REGRESSION WITH TIME SERIES =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Regression with Time Series"},

        {"type": "content", "label": "Spurious Regression", "title": "Spurious regression: two random walks and a t-statistic of 8",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Granger and Newbold (<em>Journal of "
                        "Econometrics</em> 1974, 2:111) generated pairs of independent random "
                        "walks and regressed one on the other. With fifty observations, the "
                        "t-statistic on the slope exceeded the 5% critical value in about "
                        "three-quarters of the pairs. R&sup2; was often above 0.5. Nothing was "
                        "related to anything. Phillips (<em>Journal of Econometrics</em> 1986, "
                        "33:311) proved why: with I(1) variables the t-statistic does not "
                        "converge; it grows with the sample, so more data make the problem "
                        "worse."},
                       {"t": "stats", "cols": 3, "cards": [
                           {"num": "~75%", "label": "of regressions between independent random walks 'significant' at 5%, n = 50", "color": "red", "source": "Granger and Newbold 1974"},
                           {"num": "~0.3", "label": "typical Durbin-Watson: the warning sign", "color": "amber", "source": "Same experiment"},
                           {"num": "R&sup2; &gt; DW", "label": "Granger and Newbold's rule of thumb for suspecting a spurious regression", "color": "cyan", "source": "Same paper"}]}],
              "right": [{"t": "bullets", "color": "cyan", "items": [
                  "Symptoms: a high R&sup2; between trending series, a very low Durbin-Watson, coefficients that change wildly when the sample is shifted.",
                  "Yule showed the same thing in 1926 with Church of England marriages and the mortality rate, correlated at 0.95.",
                  "Detrending does not fix it when the trends are stochastic. Differencing does, at the cost of the long run. Cointegration keeps both, if it holds.",
                  "Test the orders of integration first (section 03), always, before any regression in levels."]},
                        {"t": "hbox", "color": "red", "html": "A large share of published "
                         "regressions of one Indian macro series on another in levels, with "
                         "no cointegration test, are this experiment run once."}]},
         ]},

        {"type": "content", "label": "Cointegration", "title": "Cointegration: when levels do carry a relationship",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "term", "word": "Cointegration",
                        "def": "Two or more I(1) series are cointegrated if some linear "
                        "combination of them is I(0). They wander individually but not apart: "
                        "an equilibrium relationship ties them, and deviations from it are "
                        "temporary. Engle and Granger, <em>Econometrica</em> 1987, 55:251."},
                       {"t": "body", "html": "Consumption and income; the prices of the same "
                        "commodity in two markets; short and long interest rates; money and "
                        "nominal GDP, perhaps. Each pair drifts together because something "
                        "(a budget constraint, arbitrage, a policy rule) pulls them back when "
                        "they separate. The combination that is stationary is the long-run "
                        "relationship, and its coefficient is what a levels regression is "
                        "trying to estimate."}],
              "right": [{"t": "bullets", "color": "cyan", "items": [
                  "If <em>y</em> and <em>x</em> are cointegrated, OLS of <em>y</em> on <em>x</em> in levels is consistent (super-consistent, in fact), but its t-statistics are still not standard.",
                  "If they are not, the levels regression is spurious and only differences or a model of each series alone is valid.",
                  "Cointegration implies an error-correction representation and is implied by one (the Granger representation theorem). That is the model to estimate.",
                  "A cointegrating relationship is a statistical property. Whether it is 'equilibrium' in an economic sense is an argument, not a test result."]},
                        {"t": "hbox", "color": "amber", "html": "Wholesale onion prices in "
                         "Lasalgaon and Delhi: each I(1), the spread I(0). That is "
                         "cointegration, and the ECM says how fast a gap closes."}]},
         ]},

        {"type": "content", "label": "Engle-Granger", "title": "The Engle-Granger two-step and the error-correction model",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "flow", "steps": [
                  "STEP 1: regress y on x in levels by OLS; save the residuals u",
                  "TEST: ADF on u, using Engle-Granger critical values (more negative than standard ADF, because u was estimated)",
                  "IF REJECTED: cointegrated; the OLS slope is the long-run coefficient",
                  "STEP 2: regress &Delta;y on &Delta;x, lags of both, and u lagged once; the coefficient on u is the speed of adjustment"]},
                       {"t": "panel", "color": "cyan", "title": "The ECM", "html":
                         "&Delta;<em>y<sub>t</sub></em> = <em>c</em> + &alpha;(<em>y<sub>t&minus;1</sub></em> &minus; &beta;<em>x<sub>t&minus;1</sub></em>) "
                         "+ &Sigma; &gamma;<sub>i</sub>&Delta;<em>y<sub>t&minus;i</sub></em> + &Sigma; &delta;<sub>j</sub>&Delta;<em>x<sub>t&minus;j</sub></em> + &epsilon;<sub>t</sub><br><br>"
                         "&beta; is the long-run relationship; &alpha; (negative, between "
                         "&minus;1 and 0) is the share of last period's gap closed this "
                         "period; the &delta;s are short-run effects. &alpha; = &minus;0.25 "
                         "means a quarter of any disequilibrium is corrected each period, "
                         "a half-life of about 2.4 periods."}],
              "right": [{"t": "bullets", "color": "amber", "items": [
                  "Simple and transparent, and fine for two variables with one obvious dependent variable.",
                  "Its weaknesses: the step-1 regression's small-sample bias, the arbitrary choice of which variable is on the left, and no way to handle more than one cointegrating relationship among three or more variables.",
                  "Dynamic OLS (Stock and Watson 1993) adds leads and lags of &Delta;<em>x</em> to step 1 and gives valid standard errors for &beta;.",
                  "Report the step-1 residual test with its own critical values; a standard ADF table over-rejects."]},
                        {"t": "hbox", "color": "green", "html": "The ECM is the equation a "
                         "policy reader can use: a long-run pass-through and a speed. Both "
                         "numbers belong in the abstract."}]},
         ]},

        {"type": "content", "label": "Johansen", "title": "The Johansen procedure: several series, several relationships",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "For <em>k</em> I(1) variables there may be up to "
                        "<em>k</em> &minus; 1 cointegrating relationships. Johansen "
                        "(<em>Journal of Economic Dynamics and Control</em> 1988, 12:231; "
                        "<em>Econometrica</em> 1991, 59:1551) estimates all of them at once "
                        "in a vector error-correction model (VECM) by maximum likelihood, "
                        "and tests how many there are with the <strong>trace</strong> and "
                        "<strong>maximum-eigenvalue</strong> statistics, each compared "
                        "against critical values that depend on the deterministic terms "
                        "assumed."},
                       {"t": "table",
                        "head": ["H<sub>0</sub>: rank", "Trace statistic", "5% critical value", "Conclusion"],
                        "rows": [
                            ["r = 0", "42.7", "29.8", "Reject: at least one relationship"],
                            ["r &le; 1", "11.2", "15.5", "Not rejected: exactly one"],
                            ["r &le; 2", "2.9", "3.8", "&mdash;"]]},
                       {"t": "body", "cls": "sm", "html": "Illustrative, three variables. Read "
                        "down until the first non-rejection; the rank is one."}],
              "right": [{"t": "bullets", "color": "cyan", "items": [
                  "Lag length of the underlying VAR, chosen by information criteria, changes the result. Report the choice and the sensitivity.",
                  "The deterministic specification (Johansen's cases 1 to 5: no constant; restricted constant; unrestricted constant; restricted trend; unrestricted trend) changes the critical values and often the rank. Choose by the plot and by economics, and say which.",
                  "The cointegrating vector is identified only up to normalisation with r = 1, and needs restrictions to be interpretable with r &gt; 1.",
                  "Small samples over-reject; Reinsel-Ahn or Bartlett corrections help; sixty quarterly observations with four variables and four lags is stretching it."]},
                        {"t": "hbox", "color": "amber", "html": "In R: <em>urca::ca.jo</em>; "
                         "Stata: <em>vecrank</em> then <em>vec</em>; gretl and EViews: menu "
                         "items. All show the same tables; the judgement is the same."}]},
         ]},

        {"type": "content", "label": "ARDL Bounds", "title": "The ARDL bounds test: the workhorse of South Asian applied work",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Pesaran, Shin and Smith (<em>Journal of Applied "
                        "Econometrics</em> 2001, 16:289) proposed testing for a long-run "
                        "relationship in a single equation, an autoregressive distributed "
                        "lag model, without first classifying each regressor as I(0) or I(1). "
                        "The conditional ECM is estimated and an F-test of the joint "
                        "significance of the lagged levels is compared against two bounds: "
                        "the lower assumes all regressors I(0), the upper all I(1)."},
                       {"t": "panel", "color": "cyan", "title": "The equation", "html":
                         "&Delta;<em>y<sub>t</sub></em> = <em>c</em> + &theta;<sub>0</sub><em>y<sub>t&minus;1</sub></em> + &theta;<sub>1</sub><em>x<sub>t&minus;1</sub></em> "
                         "+ &Sigma; &gamma;<sub>i</sub>&Delta;<em>y<sub>t&minus;i</sub></em> + &Sigma; &delta;<sub>j</sub>&Delta;<em>x<sub>t&minus;j</sub></em> + &epsilon;<sub>t</sub><br><br>"
                         "H<sub>0</sub>: &theta;<sub>0</sub> = &theta;<sub>1</sub> = 0 (no long-run "
                         "relationship). F above the upper bound: cointegration. Below the "
                         "lower bound: none. Between: inconclusive, and the orders of "
                         "integration must be settled after all."}],
              "right": [{"t": "bullets", "color": "amber", "items": [
                  "Requirements that are routinely violated: no variable may be I(2); there must be one long-run relationship and <em>y</em> must be the variable it explains; the errors must be serially uncorrelated, which the lag choice must deliver.",
                  "Lags by AIC or SIC over a grid, up to a maximum set by frequency and sample; report the chosen ARDL(<em>p</em>, <em>q</em>) orders.",
                  "Small-sample critical values (Narayan, <em>Applied Economics</em> 2005, 37:1979) for fewer than about 80 observations; Pesaran's are asymptotic.",
                  "Then report the long-run coefficients (&minus;&theta;<sub>1</sub>/&theta;<sub>0</sub>) with standard errors, the ECM term (which should be negative, significant and larger than &minus;1), and the diagnostics: serial correlation, functional form, normality, heteroskedasticity, CUSUM."]},
                        {"t": "hbox", "color": "green", "html": "The method is sound. The "
                         "abuse is running it on annual series of 30 observations with five "
                         "regressors, which no bounds table was made for."}]},
         ]},

        {"type": "content", "label": "Worked ARDL", "title": "A worked ARDL: money growth and inflation",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Item", "Result", "Reads as"],
                        "rows": [
                            ["Orders of integration", "Inflation I(0) borderline; money growth I(0); output gap I(0); exchange-rate change I(0)", "All I(0) or I(1), none I(2); ARDL admissible"],
                            ["Selected model", "ARDL(2, 1, 1, 0) by AIC, max 4 lags, quarterly, n = 96", "Two lags of inflation, one each of money and output, none of the exchange rate"],
                            ["Bounds F", "6.31; I(0) bound 3.23, I(1) bound 4.35 at 5% (k = 3)", "Above the upper bound: long-run relationship"],
                            ["Long-run coefficients", "Money growth 0.48 (0.14); output gap 0.22 (0.10); exchange-rate change 0.09 (0.05)", "A percentage point of money growth raises inflation by about half a point in the long run"],
                            ["ECM term", "&minus;0.31 (0.07)", "31% of a disequilibrium closes each quarter; half-life about 1.9 quarters"],
                            ["Diagnostics", "Breusch-Godfrey p = 0.41; RESET p = 0.28; ARCH p = 0.19; CUSUM within bounds", "No evidence of misspecification"],
                            ["Break check", "Dummy for 2020Q2 significant; results unchanged without 2020", "Reported in the appendix"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "Illustrative numbers with realistic "
                        "magnitudes. Every row is a decision a reader can dispute, which is "
                        "why every row is reported. A paper that gave the long-run "
                        "coefficients and nothing else would be unreviewable."},
                        {"t": "hbox", "color": "cyan", "html": "The half-life from the ECM "
                         "term, log 0.5 / log(1 + &alpha;), is the sentence for the policy "
                         "reader: 'about half of a monetary shock's long-run effect on "
                         "inflation arrives within two quarters.'"}]},
         ]},

        {"type": "content", "label": "Choosing a Method", "title": "Engle-Granger, Johansen or ARDL: which, and when",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Situation", "Method", "Why"],
              "rows": [
                  ["Two variables, both I(1), one clearly dependent", "Engle-Granger, or ARDL", "Simple; ARDL adds valid inference on the long-run coefficient"],
                  ["Mixed I(0) and I(1) regressors, one dependent variable, small sample", "ARDL bounds", "Built for this; single equation; small-sample critical values exist"],
                  ["Three or more I(1) variables, possibly several relationships, no obvious dependent variable", "Johansen VECM", "Estimates all relationships jointly and tests their number"],
                  ["Regressors may be endogenous; feedback both ways", "Johansen VECM or a VAR", "Single-equation methods assume weak exogeneity"],
                  ["Any variable I(2)", "None of the above", "Difference the I(2) variable to I(1) first, or rethink the variables (a price level and its inflation rate cannot both be in the system)"],
                  ["A structural break in the relationship", "Gregory-Hansen (1996) test; or split the sample", "Standard tests lose power under a break"],
                  ["Panel of countries or states", "Pedroni or Westerlund panel cointegration; panel ARDL (PMG)", "Cross-section adds power; cross-sectional dependence must be handled"]]},
             {"t": "body", "cls": "sm", "html": "Running all three and reporting the one that "
              "found cointegration is not robustness. Choose by the situation, state the "
              "reasons, and show the others in an appendix if a referee will ask."},
         ]},

        {"type": "content", "label": "Dynamic Regression", "title": "Distributed lags and the difference between short and long run",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Most effects in time series arrive over several "
                        "periods. A finite distributed lag, <em>y<sub>t</sub></em> = "
                        "&Sigma;<sub>j=0..q</sub> &beta;<sub>j</sub><em>x<sub>t&minus;j</sub></em> + &epsilon;<sub>t</sub>, "
                        "gives the effect at each lag; the sum &Sigma;&beta;<sub>j</sub> is the "
                        "long-run multiplier. Adding lags of <em>y</em> (an ARDL) lets the "
                        "effect decay geometrically with few parameters: in "
                        "<em>y<sub>t</sub></em> = &phi;<em>y<sub>t&minus;1</sub></em> + &beta;<em>x<sub>t</sub></em> + &epsilon;<sub>t</sub>, "
                        "the impact effect is &beta; and the long-run effect is "
                        "&beta;/(1 &minus; &phi;)."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Report both the impact and the long-run effect, with standard errors for each (the delta method for the ratio).",
                           "The lag structure is a finding: a monsoon shock that reaches food inflation with a two-month lag and fades over six is a statement about markets.",
                           "Choose lag length by information criteria and residual autocorrelation, not by which lags are significant."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Stationarity still applies", "html":
                         "All of this assumes stationary variables, or a cointegrated system "
                         "in error-correction form. A distributed lag of one I(1) series on "
                         "another, without the ECM structure, is the spurious regression "
                         "with extra lags. The lag terms make the residuals look better "
                         "and the problem is unchanged."},
                        {"t": "hbox", "color": "green", "html": "The ARDL in ECM form is "
                         "exactly this model rewritten so that the long-run coefficient "
                         "and the adjustment speed appear as parameters. Sections 07's "
                         "methods are one model in several notations."}]},
         ]},

        {"type": "content", "label": "HAC Errors", "title": "When you cannot model the dynamics: Newey-West standard errors",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Sometimes the question is a single coefficient "
                        "in a regression of stationary variables and the dynamics are a "
                        "nuisance. Heteroskedasticity-and-autocorrelation-consistent (HAC) "
                        "standard errors (Newey and West, <em>Econometrica</em> 1987, 55:703) "
                        "leave the OLS coefficients alone and correct their standard errors "
                        "for serial correlation up to a chosen lag. The coefficients are "
                        "unbiased if the model is right; only the inference was wrong."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "The bandwidth (number of lags) matters and the automatic rules (Newey-West 1994; Andrews 1991) are a starting point. Report it.",
                           "HAC errors do not fix a spurious regression, an omitted lagged dependent variable, or a wrong functional form. They fix standard errors.",
                           "Modelling the dynamics (lags of <em>y</em> and <em>x</em>) is better when the dynamics are of interest, and often when they are not: a well-specified dynamic model has white-noise errors and needs no correction.",
                           "In Stata, <em>newey</em>; R, <em>sandwich::NeweyWest</em>; Python, <em>cov_type='HAC'</em>."]}],
              "right": [{"t": "panel", "color": "amber", "title": "A common abuse", "html":
                         "A regression of a trending outcome on a trending policy variable "
                         "in levels, with Newey-West errors and a note that 'standard errors "
                         "are robust to autocorrelation'. The errors are not the problem; "
                         "the coefficient is meaningless. Robust standard errors on a "
                         "spurious regression are precise nonsense."},
                        {"t": "hbox", "color": "green", "html": "Order of business: integration "
                         "orders, then the model form, then the standard errors."}]},
         ]},

        {"type": "content", "label": "Causality Words", "title": "What a time-series regression can and cannot say about causes",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A cointegrating relationship between money "
                        "growth and inflation is a statement that they move together in the "
                        "long run. It does not say which moves which, whether a third thing "
                        "moves both, or what would happen if the central bank changed money "
                        "growth on purpose. Those are causal questions, and a time-series "
                        "regression answers them only under assumptions that must be argued: "
                        "that <em>x</em> is not itself responding to <em>y</em>, that no "
                        "omitted series drives both, that the relationship would survive the "
                        "intervention (the Lucas critique)."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "'Is associated with in the long run' and 'adjusts toward' are what the ECM licenses.",
                           "'Causes' needs exogeneity, argued from institutions or timing, or an identification strategy (section 08's structural VAR, section 10's designs).",
                           "'Granger causes' means 'helps predict' and nothing more; the next section says why."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Weak, strong and super exogeneity", "html":
                         "Engle, Hendry and Richard (1983) drew the distinctions. Weak "
                         "exogeneity: <em>x</em> can be treated as given for estimating the "
                         "parameters of interest. Strong: plus <em>y</em> does not Granger-"
                         "cause <em>x</em>, so forecasting conditional on <em>x</em> is valid. "
                         "Super: plus the relationship is invariant to interventions in "
                         "<em>x</em>, so policy analysis is valid. Each is a stronger claim "
                         "and the ECM assumes the first, tests the second, and cannot deliver "
                         "the third."},
                        {"t": "hbox", "color": "green", "html": "Write the causal sentence you "
                         "want in the abstract, then list the assumptions it needs. If you "
                         "cannot defend them, weaken the verb."}]},
         ]},

        {"type": "content", "label": "Reporting Regression", "title": "Reporting a time-series regression: the table a referee expects",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Element", "Content"],
              "rows": [
                  ["Sample and frequency", "1996Q2 to 2024Q4, quarterly, n = 115; source and vintage of each series; transformations"],
                  ["Integration orders", "The unit-root table (section 03), in the appendix, referred to"],
                  ["Model form", "The equation written out; lag orders and how chosen; deterministic terms; dummies with dates"],
                  ["Cointegration evidence", "The bounds F or the trace statistics with critical values; or the statement that all variables are I(0) and none is needed"],
                  ["Coefficients", "Long-run and short-run, with standard errors; the ECM term; the half-life"],
                  ["Diagnostics", "Serial correlation (Breusch-Godfrey), heteroskedasticity, ARCH, normality, RESET, CUSUM and CUSUMSQ: statistics and p-values"],
                  ["Stability", "Recursive coefficients or a sub-sample estimate; break tests where the plot suggested one"],
                  ["Robustness", "Alternative lag lengths, deterministic cases, sample periods; the result's sensitivity in one sentence each"],
                  ["Interpretation", "Magnitudes in units a reader can use; the causal verb scaled to the exogeneity assumed"]]},
             {"t": "body", "cls": "sm", "html": "The table is long because the method has many "
              "decisions and each one can change the answer. A paper that reports the "
              "coefficients and 'the model passes all diagnostic tests' has reported the "
              "answer without the working."},
         ]},

        # ===================== SECTION 08: VAR AND GRANGER CAUSALITY =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "VAR and Granger Causality"},

        {"type": "content", "label": "The VAR", "title": "Vector autoregression: every variable on every variable's past",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Sims (<em>Econometrica</em> 1980, 48:1) proposed "
                        "treating a small set of macro variables symmetrically: each is "
                        "regressed on <em>p</em> lags of itself and of all the others. No "
                        "variable is assumed exogenous; the data decide the dynamics. A VAR "
                        "with <em>k</em> variables and <em>p</em> lags has <em>k</em>&sup2;<em>p</em> "
                        "slope coefficients, which is why VARs are small: three or four "
                        "variables, two to four lags, and a sample long enough to estimate "
                        "forty coefficients."},
                       {"t": "panel", "color": "cyan", "title": "A two-variable VAR(1)", "html":
                         "<em>y<sub>t</sub></em> = <em>c</em><sub>1</sub> + <em>a</em><sub>11</sub><em>y<sub>t&minus;1</sub></em> + <em>a</em><sub>12</sub><em>x<sub>t&minus;1</sub></em> + <em>e</em><sub>1t</sub><br>"
                         "<em>x<sub>t</sub></em> = <em>c</em><sub>2</sub> + <em>a</em><sub>21</sub><em>y<sub>t&minus;1</sub></em> + <em>a</em><sub>22</sub><em>x<sub>t&minus;1</sub></em> + <em>e</em><sub>2t</sub><br><br>"
                         "Estimated equation by equation by OLS. The errors <em>e</em><sub>1</sub> "
                         "and <em>e</em><sub>2</sub> are contemporaneously correlated, and that "
                         "correlation is where identification lives."}],
              "right": [{"t": "bullets", "color": "amber", "items": [
                  "Variables should be stationary (differences, growth rates, gaps), or the system should be a VECM if cointegrated. A VAR in I(1) levels is consistent but its tests are non-standard (Sims, Stock and Watson, <em>Econometrica</em> 1990, 58:113); Toda-Yamamoto's fix is on the next slide.",
                  "Lag length by AIC, HQ or SC, then check that residuals are white; SC chooses fewer lags and is usually right in small samples.",
                  "Stability: all eigenvalues of the companion matrix inside the unit circle. Software reports them; check.",
                  "Uses: forecasting (often good), Granger causality, impulse responses, variance decompositions. Each needs different assumptions."]},
                        {"t": "hbox", "color": "green", "html": "A VAR is a description of "
                         "the joint dynamics. Everything causal about it comes from what is "
                         "added afterwards."}]},
         ]},

        {"type": "content", "label": "Granger Causality", "title": "Granger causality: prediction, not causation",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "term", "word": "Granger causality",
                        "def": "<em>x</em> Granger-causes <em>y</em> if past values of <em>x</em> "
                        "help predict <em>y</em> beyond what past values of <em>y</em> already "
                        "do. Tested by a Wald or F test that the coefficients on lagged "
                        "<em>x</em> in the <em>y</em> equation are jointly zero. Granger, "
                        "<em>Econometrica</em> 1969, 37:424."},
                       {"t": "body", "html": "The name has caused fifty years of confusion. "
                        "Granger causality is incremental predictive content, and it fails as "
                        "causation in every direction: a variable that anticipates another "
                        "(the weather forecast Granger-causes the rain), two effects of a "
                        "common cause, a variable omitted from the system, and a policy "
                        "variable set in response to forecasts of the outcome (which will "
                        "appear to be Granger-caused by it)."}],
              "right": [{"t": "bullets", "color": "cyan", "items": [
                  "Report it as 'helps forecast' or 'temporally precedes'. Never as 'causes' in the abstract.",
                  "The result depends on lag length, on which other variables are in the system, and on stationarity. Report the sensitivity.",
                  "With I(1) variables, Toda and Yamamoto (<em>Journal of Econometrics</em> 1995, 66:225): estimate the VAR in levels with <em>p</em> + <em>d<sub>max</sub></em> lags and test only the first <em>p</em>. Valid whatever the integration and cointegration properties.",
                  "Bidirectional 'causality' between two macro aggregates is the usual finding and is usually uninformative."]},
                        {"t": "hbox", "color": "red", "html": "Papers whose entire contribution "
                         "is a Granger-causality table between GDP and one other series are "
                         "the most-published and least-cited genre in South Asian "
                         "economics. Do not add to it."}]},
         ]},

        {"type": "content", "label": "Impulse Responses", "title": "Impulse responses: what a shock does over time",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "An impulse response function traces the effect "
                        "of a one-time shock to one variable on itself and on the others, "
                        "period by period, holding other shocks at zero. It is the VAR's "
                        "answer to 'what happens to inflation after a policy-rate shock, and "
                        "when?' The difficulty is that the estimated errors are correlated "
                        "across equations, so a 'shock to the policy rate' has to be "
                        "separated from the part of the rate's error that is just the "
                        "economy's own noise arriving in the same quarter."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Cholesky (recursive) identification: order the variables so that each responds contemporaneously only to those before it. The ordering is an assumption and the results change with it; report the ordering and try the alternatives.",
                           "Structural VARs impose economic restrictions (short-run zeros, long-run neutrality, sign restrictions) instead; each is an argument.",
                           "Confidence bands by bootstrap; the bands are wide and should be shown.",
                           "Horizon: the responses fade in a stationary VAR; show 12 to 24 periods and stop where the bands cover zero."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Reading an IRF plot", "html":
                         "A one-standard-deviation policy-rate shock (say 25 basis points) "
                         "raises the rate on impact, output growth falls from the second "
                         "quarter, troughs around the fourth, and returns to baseline by "
                         "the eighth; inflation falls with a longer lag and the band covers "
                         "zero for the first three quarters. That is the standard shape of "
                         "monetary transmission, and the RBI's own working papers find "
                         "peak effects at three to four quarters. Illustrative; the exact "
                         "numbers are the paper's finding."},
                        {"t": "hbox", "color": "green", "html": "The IRF is the result. "
                         "Granger tables and coefficient tables are intermediate outputs and "
                         "belong in the appendix."}]},
         ]},

        {"type": "content", "label": "Variance Decomposition", "title": "Forecast error variance decomposition, and local projections",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "FEVD", "html":
                         "At each horizon, the share of the forecast error variance of each "
                         "variable attributable to each shock. 'At eight quarters, 30% of "
                         "the variance of inflation is due to exchange-rate shocks, 15% to "
                         "policy-rate shocks, the rest to its own.' Same identification "
                         "assumptions as the IRF, same sensitivity to ordering, and a "
                         "useful summary of which shocks matter for which variables."},
                        {"t": "panel", "color": "amber", "title": "Local projections", "html":
                         "Jord&agrave; (<em>American Economic Review</em> 2005, 95:161): "
                         "instead of iterating a VAR forward, regress <em>y<sub>t+h</sub></em> "
                         "directly on the shock at <em>t</em> and controls, one regression per "
                         "horizon. The coefficient at each <em>h</em> is the impulse response. "
                         "Robust to VAR misspecification, easy to add nonlinearities and "
                         "state dependence, and now the default in much applied macro. "
                         "Standard errors need HAC correction because the errors overlap."}],
              "right": [{"t": "body", "html": "Both tools answer the same question as the IRF "
                        "with different trade-offs. Local projections are simpler to "
                        "explain, more flexible and noisier at long horizons; VAR IRFs are "
                        "smoother and more dependent on the model being right. A careful "
                        "paper shows both agree on the shape."},
                        {"t": "bullets", "color": "cyan", "sm": True, "items": [
                            "Identification does not go away with local projections: the shock still has to be argued exogenous, from a VAR ordering, a narrative series, or an external instrument.",
                            "In R: <em>vars</em> for VAR/IRF/FEVD, <em>lpirfs</em> for local projections; Stata: <em>var</em>, <em>irf</em>, and <em>lpirf</em> in Stata 17+."]},
                        {"t": "hbox", "color": "green", "html": "Plot the local-projection "
                         "and VAR responses on the same axes. Where they differ is where "
                         "the VAR's lag structure is doing work."}]},
         ]},

        {"type": "content", "label": "Worked VAR", "title": "A worked three-variable VAR: growth, inflation, policy rate",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Step", "Choice", "Result"],
                        "rows": [
                            ["Variables", "GDP growth (y/y), CPI inflation (y/y), repo rate; quarterly 2001Q2&ndash;2024Q4", "All I(0) by ADF and KPSS (rate borderline); VAR in levels of these"],
                            ["Lags", "AIC 4, HQ 2, SC 2", "VAR(2); residuals pass Ljung-Box at 12 lags"],
                            ["Stability", "Largest eigenvalue modulus 0.91", "Stable"],
                            ["Granger tests", "Rate &rarr; inflation p = 0.03; inflation &rarr; rate p &lt; 0.01; growth &rarr; rate p = 0.04; rate &rarr; growth p = 0.09", "The policy rate responds to both and helps predict inflation"],
                            ["Identification", "Cholesky, ordered growth, inflation, rate", "Rate responds to growth and inflation within the quarter; they respond to the rate with a lag"],
                            ["IRF: rate shock &rarr; inflation", "Peak &minus;0.35 points at 5 quarters; band excludes zero from quarters 3 to 8", "Transmission with a lag of about a year"],
                            ["FEVD at 8 quarters", "Inflation: own 68%, growth 12%, rate 20%", "Policy shocks explain a fifth of inflation variance"],
                            ["Robustness", "Reverse ordering of growth and inflation; 3 lags; sample from 2016 (inflation targeting)", "Shape unchanged; peak effect larger post-2016"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "Illustrative throughout. The rows "
                        "are the decisions; a reader who would have ordered the variables "
                        "differently can see what that changes. The finding is the IRF "
                        "shape and the timing, and the robustness row is what makes it a "
                        "finding rather than an artefact of the ordering."},
                        {"t": "hbox", "color": "amber", "html": "The post-2016 sample has "
                         "under 40 quarters. A VAR(2) with three variables uses 21 "
                         "coefficients on it. Say so."}]},
         ]},

        {"type": "content", "label": "VECM", "title": "The VECM: a VAR for cointegrated variables",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "When the variables are I(1) and cointegrated, "
                        "the VAR in differences is misspecified (it omits the error-correction "
                        "terms) and the VAR in levels wastes the long-run restrictions. The "
                        "VECM has both: each variable's change depends on lagged changes of "
                        "all variables and on the lagged cointegrating residual(s), with a "
                        "speed-of-adjustment coefficient per equation. The Johansen procedure "
                        "(section 07) estimates it; the IRFs and decompositions follow as for "
                        "a VAR, with permanent effects of some shocks allowed."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "The adjustment coefficients tell you which variable does the adjusting. If only the exchange rate adjusts toward the money-price relationship, prices are weakly exogenous and a single-equation model of the exchange rate was enough.",
                           "Test restrictions on the cointegrating vector (does the long-run coefficient on money equal one?) with likelihood-ratio tests; they are cheap and informative.",
                           "IRFs from a VECM do not die out for the common trends; that is the point."]}],
              "right": [{"t": "panel", "color": "amber", "title": "When to stay with a VAR in differences", "html":
                         "When the variables are I(1) and not cointegrated, or when the "
                         "sample is too short to estimate the long-run relationship with "
                         "any confidence, or when the question is short-run dynamics only. "
                         "Report the cointegration test that justified the choice, either "
                         "way."},
                        {"t": "hbox", "color": "green", "html": "In Stata: <em>vec</em>; R: "
                         "<em>urca::cajorls</em> then <em>vec2var</em> for IRFs; gretl and "
                         "EViews: the VECM menu after the Johansen test."}]},
         ]},

        {"type": "content", "label": "VAR Pitfalls", "title": "VAR pitfalls and what to do about each",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Pitfall", "Consequence", "Fix"],
              "rows": [
                  ["Too many variables or lags for the sample", "Overfitted, unstable, meaningless IRFs", "Three or four variables; SC lags; Bayesian VAR shrinkage if more are needed"],
                  ["Mixed integration orders without a VECM", "Non-standard inference; spurious dynamics", "Test; VECM or Toda-Yamamoto"],
                  ["Cholesky ordering unreported or unmotivated", "Results not reproducible; identification hidden", "State the ordering and the reasoning; show alternatives"],
                  ["Granger causality as the finding", "Prediction reported as causation", "IRFs with bands; causal language scaled to identification"],
                  ["IRFs without confidence bands", "Precision overstated", "Bootstrap bands; report where they cover zero"],
                  ["Breaks ignored (2016, 2020)", "Parameters are averages over regimes", "Sub-samples; dummies; time-varying-parameter VAR if the sample allows"],
                  ["Seasonally unadjusted monthly data", "Seasonal dynamics dominate the lags", "Adjust, or use seasonal dummies and enough lags"],
                  ["Overlapping horizons in local projections", "Standard errors too small", "HAC standard errors with bandwidth at least <em>h</em>"]]},
             {"t": "body", "cls": "sm", "html": "The VAR is the easiest model in this course to "
              "estimate and the easiest to over-interpret. Its output is dynamics; its "
              "causal content is exactly what the identification assumptions put in."},
         ]},

        # ===================== SECTION 09: VOLATILITY, BREAKS AND SEASONALITY =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Volatility, Breaks and Seasonality"},

        {"type": "content", "label": "ARCH and GARCH", "title": "Volatility clustering: modelling a variance that moves",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Financial returns, exchange-rate changes and "
                        "some commodity prices have a mean that is nearly unpredictable and a "
                        "variance that is not: large changes follow large changes, calm "
                        "follows calm. Engle's ARCH (<em>Econometrica</em> 1982, 50:987) let "
                        "the conditional variance depend on recent squared errors; "
                        "Bollerslev's GARCH (<em>Journal of Econometrics</em> 1986, 31:307) "
                        "added its own lag, so that GARCH(1,1), "
                        "&sigma;&sup2;<sub>t</sub> = &omega; + &alpha;&epsilon;&sup2;<sub>t&minus;1</sub> + &beta;&sigma;&sup2;<sub>t&minus;1</sub>, "
                        "describes most such series with three parameters."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "&alpha; + &beta; is the persistence of volatility; values near 1 (0.95 is typical for daily returns) mean shocks to variance fade slowly.",
                           "Test for ARCH effects first (Engle's LM test on squared residuals of the mean model). No ARCH, no GARCH.",
                           "The mean equation (an ARMA, or a constant) and the variance equation are estimated jointly by maximum likelihood, usually with Student-t errors because returns have fat tails."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Variants, and when they earn their place", "html":
                         "EGARCH (Nelson 1991) and GJR-GARCH (Glosten, Jagannathan and "
                         "Runkle, <em>Journal of Finance</em> 1993, 48:1779) let negative "
                         "shocks raise volatility more than positive ones, which equity "
                         "returns show and exchange rates mostly do not. GARCH-in-mean puts "
                         "the variance into the mean equation as a risk premium. "
                         "Multivariate GARCH models co-movement of volatilities and needs "
                         "long samples. Each variant is one more parameter to defend."},
                        {"t": "hbox", "color": "green", "html": "Outside finance: the "
                         "volatility of food inflation, of rainfall, of remittance flows. "
                         "A GARCH model of onion price changes is a model of when the "
                         "market is dangerous."}]},
         ]},

        {"type": "content", "label": "Worked GARCH", "title": "A worked GARCH(1,1): daily rupee-dollar returns",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Parameter", "Estimate", "SE", "Reads as"],
                        "rows": [
                            ["Mean equation: constant", "0.006%", "0.004", "No predictable daily drift"],
                            ["&omega;", "0.0012", "0.0004", "Long-run variance floor"],
                            ["&alpha; (ARCH)", "0.08", "0.02", "Yesterday's surprise raises today's variance"],
                            ["&beta; (GARCH)", "0.90", "0.02", "Yesterday's variance carries forward"],
                            ["&alpha; + &beta;", "0.98", "", "Highly persistent; half-life of a volatility shock about 34 days"],
                            ["Student-t degrees of freedom", "5.4", "0.7", "Fat tails; normal errors would understate extremes"],
                            ["ARCH-LM on standardised residuals", "p = 0.62", "", "No remaining ARCH"],
                            ["Unconditional daily SD", "0.35%", "", "&radic;(&omega;/(1 &minus; &alpha; &minus; &beta;))"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "Illustrative, 2,500 daily "
                        "observations. The output that matters is the conditional variance "
                        "series plotted over time: the spikes at the 2013 taper episode, "
                        "March 2020 and any other event are the model's identification of "
                        "stress periods, and the half-life says how long each took to "
                        "subside."},
                        {"t": "hbox", "color": "amber", "html": "GARCH forecasts the variance, "
                         "not the direction. A paper that reports a GARCH model and then "
                         "predicts the exchange rate has confused the two equations."}]},
         ]},

        {"type": "content", "label": "Structural Breaks", "title": "Structural breaks: known dates and unknown dates",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Test", "Break date", "What it tests", "Notes"],
              "rows": [
                  ["Chow (<em>Econometrica</em> 1960, 28:591)", "Known", "Coefficients equal before and after a date", "F-test; the date must come from outside the data (a policy, a definition change)"],
                  ["Quandt-Andrews (Andrews, <em>Econometrica</em> 1993, 61:821)", "Unknown, single", "Supremum of Chow statistics over all candidate dates in the middle 70%", "Non-standard critical values; software has them"],
                  ["Bai-Perron (<em>Econometrica</em> 1998, 66:47; <em>J Applied Econometrics</em> 2003, 18:1)", "Unknown, multiple", "Number and dates of breaks by sequential or global search", "The standard; needs a minimum segment length; R <em>strucchange</em>, Stata <em>estat sbknown/sbsingle</em>, EViews built-in"],
                  ["CUSUM, CUSUMSQ (Brown, Durbin and Evans 1975)", "Unknown", "Instability of coefficients (CUSUM) or variance (CUSUMSQ) from recursive residuals", "Graphical; low power; good for a first look"],
                  ["Zivot-Andrews; Perron", "Unknown, one, under a unit-root null", "Unit root allowing one break in level and/or trend", "Section 03: a stationary series with a break looks I(1) to ADF"],
                  ["Gregory-Hansen (1996)", "Unknown, one", "Cointegration allowing a regime shift", "When the long-run relationship may have changed (1991, 2016)"],
                  ["Markov switching (Hamilton, <em>Econometrica</em> 1989, 57:357)", "Recurring, probabilistic", "The series switches between regimes with estimated probabilities", "For recessions, high and low volatility; needs long samples"]]},
             {"t": "body", "cls": "sm", "html": "India's series have candidate dates every "
              "analyst knows: 1991 (liberalisation), 2008&ndash;09, November 2016, July 2017, "
              "2016 (inflation targeting), April 2020. A model estimated across them without "
              "a test is assuming they did not matter. The test either supports that or it "
              "does not, and either way the paper should say."},
         ]},

        {"type": "content", "label": "Handling Breaks", "title": "Once a break is found: dummies, splits and what each costs",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "<strong>Intercept dummy</strong>: the level shifts, the dynamics do not. One parameter; keeps the whole sample.",
                  "<strong>Interaction dummies</strong>: the slopes change too. Several parameters; still one sample.",
                  "<strong>Split the sample</strong>: separate models before and after. Honest when everything changed; expensive when the post-break sample is short.",
                  "<strong>Rolling or recursive estimation</strong>: show how the coefficients evolve. A figure, not a test, and often the most persuasive evidence.",
                  "<strong>Time-varying parameters</strong>: state-space models that let coefficients drift. Powerful, and demanding of data and explanation."]}],
              "right": [{"t": "panel", "color": "amber", "title": "The 2020 problem", "html":
                         "Every monthly Indian series has an April&ndash;June 2020 that is "
                         "unlike anything before or since. Left in, it dominates the "
                         "variance, breaks the seasonal estimates and can flip unit-root "
                         "tests. Dummied out, the model has learned nothing about "
                         "pandemics and says so. Excluded, the series has a hole. There is "
                         "no right answer; there is a stated one. Most careful work uses "
                         "pulse dummies for the lockdown months and reports results with "
                         "and without 2020."},
                        {"t": "hbox", "color": "green", "html": "A break found by search "
                         "should match an event. A break at March 2015 in a CPI series is "
                         "the base-year revision, and the fix is splicing, not a dummy."}]},
         ]},

        {"type": "content", "label": "Seasonal Modelling", "title": "Seasonality in models: dummies, seasonal ARIMA, Fourier, holidays",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Approach", "How", "Suits", "Limits"],
                        "rows": [
                            ["Seasonal dummies", "<em>s</em> &minus; 1 indicator variables in a regression", "Stable, deterministic seasonality; short series", "Cannot change over time; many parameters at high frequency"],
                            ["Seasonal differencing", "&Delta;<sub>s</sub><em>y</em>", "Seasonal unit roots (HEGY); slowly changing seasonality", "Loses a year; over-differences deterministic seasonality"],
                            ["Seasonal ARIMA", "AR/MA terms at lag <em>s</em>", "Monthly and quarterly data", "Not for <em>s</em> above about 24"],
                            ["Fourier terms", "<em>K</em> sine-cosine pairs", "Daily and weekly data; long or multiple seasons", "Fixed shape; choose <em>K</em> by AICc"],
                            ["STL then model the remainder", "Decompose, model the adjusted series", "Complex, evolving seasonality", "Two-step; intervals understate uncertainty"],
                            ["ETS with seasonal component", "State-space seasonal states", "Operational forecasting", "One seasonal period only (TBATS handles more)"],
                            ["Holiday regressors", "Dummies or ramps for moving festivals", "Retail, transport, health series around Diwali, Eid, Onam", "Dates must be computed per year (X-13's <em>genhol</em>)"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "The choice depends on whether the "
                        "seasonal pattern is fixed or drifting, how many periods it has, and "
                        "whether the goal is a forecast or a coefficient on something else. "
                        "For a regression of monthly outcome on monthly policy, seasonal "
                        "dummies in both equations are usually enough and the reader can "
                        "see them."},
                        {"t": "hbox", "color": "amber", "html": "Lunar-calendar festivals move "
                         "by about eleven days a year against the Gregorian calendar. A "
                         "monthly dummy for 'October' captures Diwali in some years and "
                         "misses it in others. Build the holiday regressor from the actual "
                         "dates."}]},
         ]},

        {"type": "content", "label": "Nonlinearity", "title": "Threshold and regime models: when the dynamics depend on the state",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A linear model says a shock has the same effect "
                        "in a boom and a slump, a rate rise the same effect at 4% inflation "
                        "and at 9%. Threshold autoregressions (Tong) switch coefficients when "
                        "an observed variable crosses a threshold; smooth-transition models "
                        "let the switch be gradual; Markov-switching models (Hamilton 1989) "
                        "let an unobserved state govern the regime, with the state's "
                        "probability estimated each period. All need longer samples than "
                        "linear models and all are harder to explain."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Test for nonlinearity before fitting it: the linearity tests of Ter&auml;svirta, or simply compare out-of-sample forecasts.",
                           "A threshold at a policy-relevant level (inflation above the target band) is interpretable; one estimated at 6.37% with no story is a fit.",
                           "Markov-switching output is a probability-of-regime plot; the dating of Indian growth regimes is a legitimate use."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Asymmetry in local projections", "html":
                         "A simpler route to state dependence: estimate local projections "
                         "separately for periods when a state variable (the output gap, "
                         "the credit-to-GDP ratio) is above and below its median, or "
                         "interact the shock with a smooth transition function. Auerbach "
                         "and Gorodnichenko's fiscal-multiplier work (2012) made this the "
                         "standard approach, and it needs no new estimator."},
                        {"t": "hbox", "color": "green", "html": "Nonlinearity is a finding "
                         "only if the linear model fails in a way the nonlinear one fixes, "
                         "out of sample. Report both."}]},
         ]},

        {"type": "content", "label": "High Frequency", "title": "Daily and intraday data: the problems scale up",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Daily AQI, hourly electricity load, tick-level "
                        "prices. Everything in the course applies and three things get "
                        "harder. Seasonality is multiple: hour of day, day of week, annual. "
                        "Missing values and irregular timestamps are the norm. And the "
                        "sample is enormous, so everything is 'significant' and the "
                        "question becomes size, not existence."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Aggregate to the frequency the question needs. A policy that works over months does not need hourly data.",
                           "Multiple seasonalities: Fourier terms for each period, TBATS, or Prophet-style models with explicit components. Seasonal ARIMA cannot do it.",
                           "Calendar effects: trading days, holidays, leap years, the number of Sundays in a month. X-13 and the <em>seasonal</em> package handle these for monthly data.",
                           "Realised volatility from intraday returns is a better volatility measure than a GARCH on daily returns when the tick data exist."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Daily AQI in an Indian city", "html":
                         "Annual seasonality (winter peak), weekly (weekend dip), a trend "
                         "that the question is about, weather covariates that must be "
                         "controlled (wind speed, humidity, temperature), missing days when "
                         "the monitor failed, and a change in the monitor network in 2018. "
                         "A regression on time alone finds a 'trend' that is the network "
                         "change; a model with Fourier terms, weather, monitor dummies and "
                         "ARIMA errors finds the trend that is left, which is smaller and "
                         "real."},
                        {"t": "hbox", "color": "green", "html": "JanVayu's air-quality work "
                         "in this family of sites is the applied version of this slide."}]},
         ]},

        {"type": "content", "label": "State Space", "title": "State-space models and the Kalman filter: the general framework",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Almost every model in this course is a special "
                        "case of a state-space model: an unobserved state (level, slope, "
                        "seasonal, regime) evolves by a transition equation, and the "
                        "observation is the state plus noise. The Kalman filter computes the "
                        "likelihood and the best estimate of the state at each date; the "
                        "smoother revises those estimates using the whole sample. ETS, ARIMA, "
                        "time-varying-parameter regressions and unobserved-components trend "
                        "models all fit here."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Handles missing observations natively: the filter skips the update and the uncertainty grows.",
                           "Handles mixed frequencies: monthly indicators to nowcast quarterly GDP, which is how the RBI and many central banks do it.",
                           "Gives the trend and cycle as estimated states with uncertainty, which is what 'potential output' and 'the output gap' are.",
                           "In R: <em>KFAS</em>, <em>dlm</em>, <em>bsts</em>; Python: <em>statsmodels.tsa.statespace</em>; Stata: <em>sspace</em>, <em>ucm</em>."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Why it matters for section 10", "html":
                         "The Bayesian structural time-series approach to programme "
                         "evaluation (CausalImpact) is a state-space model of the outcome "
                         "before the intervention, projected forward as the counterfactual. "
                         "Understanding the framework is what makes its assumptions "
                         "visible: the counterfactual is the pre-period model continuing, "
                         "and it is only as good as that model."},
                        {"t": "hbox", "color": "green", "html": "You do not need to write a "
                         "Kalman filter. You need to know that the software fitting your "
                         "ETS or your unobserved-components trend is running one, and what "
                         "it assumes."}]},
         ]},

        # ===================== SECTION 10: TIME SERIES FOR PROGRAMME EVALUATION =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Time Series for Programme Evaluation"},

        {"type": "content", "label": "The Design", "title": "Interrupted time series: the strongest design when there is no control group",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A programme starts at a known date; an outcome "
                        "is measured repeatedly before and after. The interrupted time series "
                        "(ITS) design asks whether the level or the trend of the series "
                        "changed at that date, against the counterfactual that the "
                        "pre-intervention trend would have continued. Bernal, Cummins and "
                        "Gasparrini (<em>International Journal of Epidemiology</em> 2017, "
                        "46:348) give the tutorial that applied health and policy work now "
                        "follows; Wagner and colleagues (2002) gave the segmented-regression "
                        "form."},
                       {"t": "panel", "color": "cyan", "title": "Segmented regression", "html":
                         "<em>y<sub>t</sub></em> = &beta;<sub>0</sub> + &beta;<sub>1</sub><em>t</em> + &beta;<sub>2</sub><em>D<sub>t</sub></em> + &beta;<sub>3</sub>(<em>t</em> &minus; <em>t</em><sub>0</sub>)<em>D<sub>t</sub></em> + seasonal terms + &epsilon;<sub>t</sub><br><br>"
                         "<em>D<sub>t</sub></em> = 1 from the intervention date <em>t</em><sub>0</sub>. "
                         "&beta;<sub>1</sub> is the pre-trend; &beta;<sub>2</sub> the immediate "
                         "level change; &beta;<sub>3</sub> the change in slope. The effect at "
                         "any later date is &beta;<sub>2</sub> + &beta;<sub>3</sub>(<em>t</em> &minus; <em>t</em><sub>0</sub>)."}],
              "right": [{"t": "bullets", "color": "amber", "items": [
                  "Specify the impact model before looking: level change, slope change, both, delayed, temporary. The choice is a hypothesis, not a fit.",
                  "Enough points: Penfold and Zhang (<em>Academic Pediatrics</em> 2013, 13:S38) suggest at least eight before and eight after as a floor; power depends on variance and autocorrelation more than on the count.",
                  "Autocorrelated errors are the rule: model them (ARIMA errors, Prais-Winsten) or use Newey-West; a naive OLS overstates precision badly.",
                  "Seasonality must be in the model, or a programme that starts in May 'reduces' diarrhoea by October."]},
                        {"t": "hbox", "color": "green", "html": "The design's assumption, in one "
                         "sentence: nothing else that affects the outcome changed at the "
                         "same time. Write that sentence and then test it."}]},
         ]},

        {"type": "content", "label": "Worked ITS", "title": "A worked ITS: institutional deliveries after a transport scheme",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Term", "Estimate", "95% CI", "Reads as"],
                        "rows": [
                            ["Pre-intervention level (&beta;<sub>0</sub>)", "58.2%", "56.1 to 60.3", "Institutional delivery share at the start"],
                            ["Pre-trend (&beta;<sub>1</sub>)", "+0.21 points/month", "0.14 to 0.28", "Rising before the scheme: about 2.5 points a year"],
                            ["Level change (&beta;<sub>2</sub>)", "+4.8 points", "2.1 to 7.5", "An immediate jump at launch"],
                            ["Slope change (&beta;<sub>3</sub>)", "+0.09 points/month", "&minus;0.02 to 0.20", "Trend possibly steeper; not distinguishable from zero"],
                            ["Effect at 12 months", "+5.9 points", "2.4 to 9.4", "Against the counterfactual of the pre-trend continuing"],
                            ["Effect at 24 months", "+7.0 points", "1.8 to 12.2", "Widening interval: the counterfactual is extrapolated further"],
                            ["Seasonal terms", "Fourier, 2 pairs", "", "Monsoon dip captured"],
                            ["Error model", "AR(1), &phi; = 0.43", "", "Chosen by residual ACF; OLS CIs were 35% narrower"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "Illustrative, 36 months before and "
                        "30 after. The reading: a real and immediate level effect of about "
                        "five points; no clear acceleration beyond the pre-existing trend; "
                        "the two-year effect is mostly the initial jump carried forward. The "
                        "result is stated against a counterfactual that is a straight-line "
                        "extrapolation, and the limitations section says so."},
                        {"t": "hbox", "color": "amber", "html": "Plot it. The pre-period fit, "
                         "the counterfactual dashed line, the post-period fit, and the "
                         "data. Every ITS paper's Figure 1, and the referee's first stop."}]},
         ]},

        {"type": "content", "label": "Threats", "title": "What can go wrong with an ITS, and the checks",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Threat", "What it looks like", "Check or fix"],
              "rows": [
                  ["Co-intervention", "Another programme, a price change or an election at the same time", "Document the timeline; use a control series (next slide); test for the effect on an outcome the programme should not touch"],
                  ["Anticipation", "The series moves before the official date", "Plot; test with the date shifted earlier; treat the announcement as the start"],
                  ["Changed measurement", "The reporting system, definition or denominator changed at the intervention", "Read the metadata; a level change with no plausible mechanism is usually this"],
                  ["Wrong impact model", "A temporary effect modelled as permanent, or the reverse", "Pre-specify; show the alternatives in the appendix"],
                  ["Pre-trend misspecified", "A curved pre-trend fitted as a line, so the counterfactual is wrong", "Longer pre-period; a quadratic or a local trend; sensitivity to the pre-period length"],
                  ["Autocorrelation ignored", "Confidence intervals too narrow", "ARIMA errors, Prais-Winsten or Newey-West; report the residual ACF"],
                  ["Too few points", "Six months before, six after", "Say the design is descriptive; do not report a p-value as if it settled anything"],
                  ["Regression to the mean", "Programme launched because the series was at its worst", "Longer pre-period; a control series; state the selection"]]},
             {"t": "body", "cls": "sm", "html": "The last is the one that catches programmes "
              "evaluated after a crisis. A malnutrition scheme launched at the peak of a "
              "bad year will show improvement whatever it does, because bad years end."},
         ]},

        {"type": "content", "label": "Controls", "title": "Controlled ITS: adding a comparison series",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The single-series ITS cannot separate the "
                        "programme from anything else that changed at the same time. A "
                        "comparison series that was exposed to everything except the "
                        "programme (a neighbouring district, an outcome the programme should "
                        "not affect, the same outcome in an unexposed group) turns the "
                        "design into a difference-in-differences in time-series form: the "
                        "effect is the change in the treated series' level and slope minus "
                        "the change in the control's. Lopez Bernal, Cummins and Gasparrini "
                        "(<em>International Journal of Epidemiology</em> 2018, 47:2082) set "
                        "out the options."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Location control: another area. Assumes common shocks; check that pre-trends match.",
                           "Outcome control: a series in the same place the programme should not move. Assumes the co-intervention would have moved it too.",
                           "Both, where available. Disagreement between them is informative.",
                           "Model: pool the series with an indicator for treated, interactions with the segmented-regression terms; cluster or model the errors within series."]}],
              "right": [{"t": "panel", "color": "amber", "title": "The assumption, again", "html":
                         "The control series must have followed the same path as the treated "
                         "one in the absence of the programme. That is testable in the "
                         "pre-period (parallel trends) and unverifiable after. A control "
                         "district chosen because it looks similar today may have been "
                         "chosen on the outcome; state how it was chosen, before the data "
                         "were seen if possible."},
                        {"t": "hbox", "color": "green", "html": "With many districts and a "
                         "staggered rollout, the design becomes a panel event study, and "
                         "Impact Evaluation 101 covers the estimators that handle it."}]},
         ]},

        {"type": "content", "label": "Synthetic Control", "title": "Synthetic control: building the counterfactual from donors",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "One state adopts a policy; thirty do not. No "
                        "single control state matches the treated one, but a weighted "
                        "average of several might: weights chosen so the combination "
                        "reproduces the treated state's pre-period outcome path and "
                        "covariates. The post-period gap between the treated series and its "
                        "synthetic twin is the estimated effect. Abadie, Diamond and "
                        "Hainmueller (<em>JASA</em> 2010, 105:493) introduced it with "
                        "California's tobacco law; Abadie (<em>Journal of Economic "
                        "Literature</em> 2021, 59:391) reviews a decade of use and misuse."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Weights are non-negative and sum to one, so the synthetic unit stays inside the range of the donors: no extrapolation.",
                           "Inference by permutation: apply the method to every donor as if it were treated, and see where the real gap sits in the distribution of placebo gaps.",
                           "Report the weights, the pre-period fit (RMSPE), and the placebo plot. A poor pre-period fit means no credible counterfactual."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Where it fits Indian work", "html":
                         "State-level policies with annual or quarterly outcomes and a long "
                         "pre-period: a state's prohibition, a labour-law amendment, a "
                         "free-electricity scheme. Donor pool of the other states, excluding "
                         "those with similar policies. Needs perhaps ten or more pre-periods "
                         "and a treated unit that is not an outlier among donors; Bihar's "
                         "outcomes often cannot be synthesised from the other states, and "
                         "the method says so through the fit."},
                        {"t": "hbox", "color": "green", "html": "R: <em>Synth</em>, "
                         "<em>tidysynth</em>; Stata: <em>synth</em>, <em>synth_runner</em>; "
                         "Python: <em>pysyncon</em>. The augmented and penalised variants "
                         "handle imperfect fit."}]},
         ]},

        {"type": "content", "label": "Bayesian Structural", "title": "CausalImpact: the forecasting counterfactual",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Brodersen and colleagues (<em>Annals of Applied "
                        "Statistics</em> 2015, 9:247) fit a Bayesian structural time-series "
                        "model to the outcome in the pre-period, using control series as "
                        "regressors, then forecast it through the post-period as the "
                        "counterfactual. The effect is observed minus forecast, with a "
                        "credible interval that widens with the horizon. It is an ITS whose "
                        "counterfactual is a state-space forecast rather than a straight "
                        "line, and a synthetic control whose weights are regression "
                        "coefficients rather than constrained to a simplex."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Suits high-frequency series with several controls: daily web or transaction data, weekly disease counts with neighbouring districts as controls.",
                           "The controls must not be affected by the intervention; that is the identifying assumption, and it is the same one as everywhere in this section.",
                           "Run it on a pre-period placebo date. If it finds an 'effect' there, the model is finding noise."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Choosing among the three", "html":
                         "One treated series, no controls: segmented-regression ITS. One "
                         "treated unit, many potential control units, few time points: "
                         "synthetic control. One treated series, several control series, "
                         "many time points: CausalImpact or a controlled ITS. Many treated "
                         "units, staggered: a panel event study. In every case the plot of "
                         "treated versus counterfactual is the result and the placebo "
                         "checks are the credibility."},
                        {"t": "hbox", "color": "green", "html": "R: <em>CausalImpact</em>; "
                         "Python: <em>tfcausalimpact</em>. Both need the pre-period to be "
                         "long enough for the state-space model to learn the seasonality."}]},
         ]},

        {"type": "content", "label": "Reporting ITS", "title": "Reporting an evaluation built on time series",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Element", "Content"],
              "rows": [
                  ["Design", "ITS, controlled ITS, synthetic control or BSTS; why this one; the intervention date and how it was set"],
                  ["Data", "Series, frequency, source, period, number of points before and after, missing values and how handled, any measurement changes"],
                  ["Impact model", "Level, slope, both, lagged, temporary; pre-specified and stated"],
                  ["Model", "The segmented-regression equation; seasonal terms; error structure and how chosen; or the donor pool, weights and pre-period fit"],
                  ["Figure 1", "Data, pre-period fit, counterfactual, post-period fit, with intervals; or treated versus synthetic with the gap"],
                  ["Effects", "Level and slope changes with CIs; effects at stated horizons; placebo results"],
                  ["Threats", "Co-interventions considered and how excluded; anticipation; measurement; regression to the mean"],
                  ["Sensitivity", "Pre-period length; error model; impact model; control choice; excluding 2020"],
                  ["Language", "'Associated with a change of X at the intervention date, relative to the pre-trend', with the causal verb earned by the controls and checks"]]},
             {"t": "body", "cls": "sm", "html": "The design is only as strong as its "
              "counterfactual, and the counterfactual is an assumption the reader must be "
              "able to see. Every row above is there so they can."},
         ]},

        # ===================== SECTION 11: INDIAN DATA, SOFTWARE AND PRACTICE =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Indian Data, Software and Practice"},

        {"type": "content", "label": "Macro Data", "title": "Where Indian macroeconomic time series live",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Source", "Series", "Frequency and span", "Notes"],
              "rows": [
                  ["RBI DBIE (Database on Indian Economy)", "Money, credit, interest rates, exchange rates, external sector, some prices and output", "Daily to annual; decades", "The single best portal; bulk download; document the extraction date"],
                  ["MoSPI (NSO)", "CPI (base 2012 = 100), IIP (2011&ndash;12), quarterly GDP and GVA (2011&ndash;12), PLFS quarterly bulletins", "Monthly, quarterly; CPI from 2011, quarterly GDP from 1996&ndash;97", "Base changes need splicing; GDP revisions are large"],
                  ["Office of the Economic Adviser, DPIIT", "WPI (base 2011&ndash;12) and components", "Monthly; long series with base links", "The producer-price side of inflation"],
                  ["Labour Bureau", "CPI-IW (base 2016), CPI-AL/RL", "Monthly; long", "Used for wage indexation and rural real wages"],
                  ["Ministry of Finance, PIB, GSTN", "GST collections, fiscal data, monthly economic report", "Monthly since July 2017", "GST is a short series with a strong seasonal and a COVID break"],
                  ["IMD; IITM", "Rainfall by subdivision; the homogeneous all-India series from 1871", "Daily, monthly; 150 years", "The longest Indian series; the monsoon is a regressor in half of applied macro"],
                  ["CMIE (Economic Outlook, CPHS)", "High-frequency employment, sentiment, company data", "Monthly, weekly; paid", "Coverage and weighting debates; cite the vintage"],
                  ["IMF IFS; World Bank WDI; FRED", "Cross-country comparables; some Indian series mirrored", "Monthly (IFS), annual (WDI)", "Definitions may differ from the domestic source; say which you used"]]},
             {"t": "body", "cls": "sm", "html": "For Bangladesh, Pakistan, Nepal and Sri Lanka "
              "the central bank (Bangladesh Bank, State Bank of Pakistan, Nepal Rastra Bank, "
              "Central Bank of Sri Lanka) and the statistics bureau are the equivalents, "
              "with shorter and more revised series."},
         ]},

        {"type": "content", "label": "Administrative Data", "title": "Programme and administrative series: the sector's own time series",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Source", "Series", "Frequency", "Traps"],
              "rows": [
                  ["HMIS (Health Management Information System)", "Facility-reported health service indicators by district", "Monthly since 2008", "Reporting completeness varies by month and district; denominators are projections; a zero is often a non-report"],
                  ["MGNREGA MIS", "Person-days, households, wages, works by block", "Monthly, daily updates", "Strong lean-season seasonality; data revised as muster rolls are entered; state-level differences in reporting lag"],
                  ["Agmarknet", "Mandi arrivals and prices by commodity and market", "Daily", "Missing days with no trade; variety and grade changes; outliers from entry error"],
                  ["UDISE+; school MIS", "Enrolment, teachers, infrastructure", "Annual", "Not a time series in the sense here; annual with definitional changes"],
                  ["NFHS, NSS, PLFS", "Survey rounds", "Every few years; PLFS quarterly for urban", "Rounds are comparable only with care; not for ARIMA"],
                  ["CPCB; state pollution boards", "AQI and pollutant concentrations by monitor", "Hourly, daily", "Monitor network changes; missing hours; calibration"],
                  ["Programme MIS (your own)", "Beneficiaries, disbursements, complaints, stock", "Monthly", "Everything above, plus the definition changed when the software did"]]},
             {"t": "body", "cls": "sm", "html": "Administrative series are where the methods "
              "in section 10 earn their keep, and where the cleaning decisions in section 02 "
              "matter most. Keep the reporting-completeness series alongside the outcome "
              "series and plot both; a change in one explains many changes in the other."},
         ]},

        {"type": "content", "label": "Software", "title": "Software: what each does, and what it costs",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Tool", "Cost", "Time-series strengths", "Gaps"],
              "rows": [
                  ["R: <em>forecast</em>, <em>fable</em>/<em>tsibble</em>/<em>feasts</em>, <em>urca</em>, <em>vars</em>, <em>ARDL</em>, <em>strucchange</em>, <em>rugarch</em>, <em>CausalImpact</em>, <em>Synth</em>", "Free", "Everything in this course, with the reference implementations for forecasting and the best documentation (fpp3)", "Several packages to learn; Johansen output is less friendly than Stata's"],
                  ["Python: <em>statsmodels</em> (ARIMA, SARIMAX, VAR, VECM, ARDL, unit-root tests, state space), <em>pmdarima</em>, <em>arch</em>, <em>ruptures</em>", "Free", "Full coverage; integrates with data pipelines and machine learning", "Fewer diagnostics printed by default; more code per result"],
                  ["Stata: <em>tsset</em>, <em>arima</em>, <em>dfuller</em>/<em>pperron</em>, <em>vecrank</em>/<em>vec</em>, <em>var</em>/<em>irf</em>, <em>ardl</em> (Kripfganz and Schneider), <em>itsa</em> (Linden), <em>synth</em>, <em>newey</em>", "Licence", "Clean output; the econometric tradition; ARDL and ITS commands are excellent", "No automatic ARIMA or ETS; forecasting is weaker than R"],
                  ["EViews", "Licence", "Menu-driven ARDL with bounds test, Johansen, Bai-Perron, X-13, GARCH; the tool most South Asian econometrics courses teach", "Cost; scripting is awkward; reproducibility depends on saving workfiles and programs"],
                  ["gretl", "Free, open source", "Menu-driven like EViews: unit-root tests, Johansen, VAR, ARDL via scripts, GARCH, X-13 interface, good graphs", "Smaller community; fewer new methods"],
                  ["Excel / Google Sheets", "Free or licensed", "Plotting, moving averages, classical decomposition, simple smoothing", "No unit-root tests, no ARIMA worth using, no reproducibility; fine for a first look"]]},
             {"t": "body", "cls": "sm", "html": "For a learner: gretl to see every method with "
              "menus, then R with fpp3 for forecasting and <em>urca</em>/<em>vars</em> for the "
              "econometrics. For a Stata department: Stata plus R for forecasting. EViews "
              "is a fine tool whose cost is the only argument against it, and everything "
              "it does, gretl does free."},
         ]},

        {"type": "content", "label": "Workflow", "title": "A reproducible time-series workflow",
         "blocks": [
             {"t": "flow", "steps": [
                 "DOWNLOAD raw data with a script; save with the date and source URL",
                 "CLEAN in code: splice bases, handle missing, transform; log every decision",
                 "PLOT: levels, differences, ACF, seasonal plots; save the figures",
                 "TEST: integration orders, breaks, seasonality; one table",
                 "MODEL: the candidates, the diagnostics, the chosen model",
                 "EVALUATE: rolling out-of-sample against benchmarks, or placebos for evaluation designs",
                 "REPORT: tables from code, figures from code, the script in the replication package"]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Time-series results are unusually sensitive to "
                        "small decisions (lag length, deterministic terms, the sample start, "
                        "a dummy), and the only defence is that every decision is in a script "
                        "a reader can change. Quarto or R Markdown, with the data download "
                        "at the top and the tables generated at the bottom, is the form that "
                        "makes this automatic."}],
              "right": [{"t": "hbox", "color": "amber", "html": "Data vintage is a decision "
                        "too. 'GDP series downloaded from MoSPI on 12 March 2026, base "
                        "2011&ndash;12, second revised estimates for 2023&ndash;24' is the "
                        "sentence that lets a reader in 2028 know why their numbers "
                        "differ."}]},
         ]},

        {"type": "content", "label": "Worked Study", "title": "A worked study outline: does MGNREGA demand respond to rainfall shocks?",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Step", "Decision", "Section"],
                        "rows": [
                            ["Question", "Does a rainfall deficit in the monsoon raise MGNREGA person-days in the following lean season, by how much, and how fast?", "01"],
                            ["Data", "Monthly person-days by state (MIS, 2012&ndash;2025); IMD subdivision rainfall; state population; a 2020 dummy", "02, 11"],
                            ["Transform", "Log person-days per 1,000 rural population; rainfall as percentage deviation from the long-period average; seasonal plots show a June&ndash;July trough and a March&ndash;May peak", "02"],
                            ["Integration", "Log person-days: I(0) around seasonal means with a break in 2020 by ADF, KPSS and Zivot-Andrews; rainfall deviation I(0)", "03, 09"],
                            ["Model", "Dynamic regression with seasonal dummies, distributed lags of rainfall deviation (0 to 9 months), AR errors, state fixed effects; a panel ARDL as a check", "07"],
                            ["Finding (illustrative)", "A 20% monsoon deficit raises person-days by 11% at a 4&ndash;6 month lag, fading by month 9; larger in states with lower irrigation cover", "07, 09"],
                            ["Evaluation design", "For the 2016 wage revision: controlled ITS with states that revised later as controls", "10"],
                            ["Robustness", "Drop 2020; alternative lag lengths; Newey-West vs AR errors; district-level replication for two states", "06, 07"],
                            ["Report", "Unit-root table in the appendix; IRF-style plot of the rainfall lag coefficients with bands; the ITS figure; replication package on a repository", "11"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "Numbers are illustrative; the "
                        "structure is the point. Each step names the section of this course "
                        "that governs it, and the paper's methods section is this table "
                        "written out."},
                        {"t": "hbox", "color": "amber", "html": "The lag structure is the "
                         "policy result: if demand peaks five months after a failed monsoon, "
                         "that is when the funds must be in the states' accounts."}]},
         ]},

        {"type": "content", "label": "Pitfalls", "title": "The dozen errors that get time-series papers rejected",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Error", "Section", "Fix in one line"],
              "rows": [
                  ["Regression in levels of I(1) series with no cointegration test", "07", "Test; ECM or differences"],
                  ["Unit-root tests with unreported terms, lags and margins", "03", "One full table"],
                  ["Six unit-root tests, the convenient one reported", "03", "ADF and KPSS, both, always"],
                  ["ARDL on 30 annual observations with five regressors", "07", "Fewer regressors, or admit the design cannot answer"],
                  ["Granger causality as the contribution", "08", "IRFs, and a question"],
                  ["Cholesky ordering unreported", "08", "State it; try alternatives"],
                  ["Forecast accuracy with no benchmark, in-sample", "05, 06", "Seasonal naive, rolling origin, MASE"],
                  ["MAPE on a series with zeros", "06", "MASE or RMSE"],
                  ["Seasonality ignored in a monthly model", "02, 09", "Dummies, seasonal ARIMA or STL"],
                  ["2016, 2020 and base-year changes left untreated", "09", "Dummies, splicing, sub-samples; report both"],
                  ["ITS with six points each side and a p-value", "10", "Descriptive claim only; more data"],
                  ["'Causes' from a model that shows co-movement", "07, 08, 10", "Scale the verb to the identification"]]},
             {"t": "body", "cls": "sm", "html": "Every one of these appears in most issues of "
              "the journals that publish South Asian applied time-series work. Avoiding them "
              "is the difference between those journals and the ones on the reading list."},
         ]},

        {"type": "content", "label": "Checklist", "title": "Before you submit: the time-series checklist",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Data and description", "Done"],
                        "rows": [
                            ["Every series plotted in levels and differences, with the figures kept", ""],
                            ["Source, vintage, base year, transformations and sample stated", ""],
                            ["Missing values and reporting gaps identified and handled in code", ""],
                            ["Seasonality examined and treated", ""],
                            ["Known breaks (2016, 2017, 2020, base changes) tested and handled", ""],
                            ["Integration orders tested with two tests, reported in one table", ""]]}],
              "right": [{"t": "table",
                         "head": ["Modelling and reporting", "Done"],
                         "rows": [
                             ["Model form justified by the tests and the question, not by the software default", ""],
                             ["Lag lengths and deterministic terms chosen by stated criteria and reported", ""],
                             ["Residual diagnostics passed and reported with statistics", ""],
                             ["Forecasts evaluated out of sample against benchmarks, by horizon, with coverage", ""],
                             ["Identification assumptions (ordering, exogeneity, counterfactual) stated in words", ""],
                             ["Sensitivity to the main choices shown", ""],
                             ["Causal verbs scaled to what the design supports", ""],
                             ["Script and data (or download code) in a replication package", ""]]},
                        {"t": "hbox", "color": "cyan", "html": "Fourteen lines. The unit-root "
                         "table and the benchmark comparison are the two most often "
                         "missing."}]},
         ]},

        {"type": "content", "label": "Reading List", "title": "Where to go next",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Resource", "What it covers", "Notes"],
              "rows": [
                  ["Hyndman and Athanasopoulos, <em>Forecasting: Principles and Practice</em> (3rd ed., OTexts, 2021)", "Sections 02, 04, 05, 06 with R code for everything", "Free online at otexts.com/fpp3; the first thing to read"],
                  ["Enders, <em>Applied Econometric Time Series</em> (4th ed., Wiley, 2014)", "Unit roots, cointegration, VAR, GARCH, breaks; the applied econometrics half", "The standard graduate applied text"],
                  ["Stock and Watson, <em>Introduction to Econometrics</em> (4th ed., Pearson, 2019), the time-series chapters", "Dynamic regression, forecasting, cointegration, at an accessible level", "Where most economists first meet the material"],
                  ["Kilian and L&uuml;tkepohl, <em>Structural Vector Autoregressive Analysis</em> (Cambridge University Press, 2017)", "Everything about VARs and identification", "For section 08 in depth"],
                  ["Hamilton, <em>Time Series Analysis</em> (Princeton University Press, 1994)", "The theory, complete", "Reference, not a first read"],
                  ["Shumway and Stoffer, <em>Time Series Analysis and Its Applications</em> (4th ed., Springer, 2017)", "Statistical treatment with R, including state space", "Free PDF from the authors"],
                  ["Bernal, Cummins and Gasparrini, <em>Int J Epidemiol</em> 2017, 46:348; Lopez Bernal et al. 2018, 47:2082", "Interrupted time series, with and without controls", "The two papers to cite and follow"],
                  ["Abadie, <em>J Econ Lit</em> 2021, 59:391", "Synthetic control: method, practice, pitfalls", "Read before using the method"],
                  ["Pesaran, Shin and Smith, <em>J Applied Econometrics</em> 2001, 16:289; Kripfganz and Schneider's <em>ardl</em> documentation", "The bounds test and its correct use", "Read the original, not the summaries"],
                  ["ImpactMojo: Econometrics 101, Impact Evaluation 101, Data Analysis 101", "The regression and evaluation foundations this course assumes", "impactmojo.in/101-courses/"]]},
         ]},

        {"type": "content", "label": "Summary", "title": "What to remember",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "Plot first. The plot decides the method and shows what no test will.",
                  "Autocorrelation shrinks your sample; persistence makes 'significant' cheap.",
                  "Test the order of integration, with two tests, and report the table. Everything after depends on it.",
                  "Two trending series correlate whether or not they are related. Cointegration is the exception, and it is tested, not assumed.",
                  "Forecasts are judged out of sample, by horizon, against a benchmark, with interval coverage checked."]}],
              "right": [{"t": "bullets", "color": "green", "items": [
                  "The ECM gives a long-run relationship and a speed of adjustment; those two numbers are the finding.",
                  "A VAR describes dynamics; its causal content is the identification you added. Granger causality is prediction.",
                  "Breaks, seasonality and 2020 are modelled, not ignored and not deleted.",
                  "An ITS is a counterfactual drawn from the pre-period; the controls and placebos are what make it credible.",
                  "Every decision in a script; every table from code; the vintage of every series stated."]},
                        {"t": "hbox", "color": "amber", "html": "The question this course "
                         "began with, asked of every result: a relationship, or two things "
                         "moving through time together?"}]},
         ]},

        # ===================== S100 END =====================
        {"type": "end",
         "eyebrow": "Time Series Analysis 101 &middot; Complete",
         "headline": "Now go find out<br>whether the trend is real.",
         "byline": "Order carries information, and it carries traps. Test the order of "
                   "integration, model the seasonality, beat the benchmark, and say what the "
                   "counterfactual is. Explore the rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
