# -*- coding: utf-8 -*-
"""
Structural Equation Modelling 101 — ImpactMojo 101 Series (native deck spec)
Latent variables, confirmatory factor analysis, reliability and validity, identification,
estimation, model fit, mediation and moderation, measurement invariance across languages,
PLS-SEM, causal interpretation, and reporting. For applied social researchers in South Asia
working in R (lavaan), Stata, AMOS, SmartPLS or JASP.
Build: python3 scripts/deck-builder/build.py sem
"""

DECK = {
    "slug": "sem",
    "title": "Structural Equation Modelling 101",
    "description": ("Structural Equation Modelling 101 — a free foundational course for applied "
                    "social researchers in South Asia. Latent variables and confirmatory factor "
                    "analysis, reliability and validity, model identification, estimation with "
                    "ordinal and missing data, fit indices read with judgement, mediation and "
                    "moderation with bootstrapped effects, measurement invariance across Hindi, "
                    "Bangla and Tamil versions of a scale, PLS-SEM and when to use it, what SEM "
                    "can and cannot say about causes, and how to report it. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Structural<br>Equation<br>Modelling 101",
         "sub": "Latent Variables, Confirmatory Factor Analysis, Mediation, Measurement "
                "Invariance and PLS-SEM &mdash; Measured, Fitted and Reported Honestly",
         "tags": ["Research Methods", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "What SEM Is, and Is Not"},
             {"name": "Latent Variables and CFA"},
             {"name": "Reliability and Validity"},
             {"name": "Specification and Identification"},
             {"name": "Estimation, Data and Sample Size"},
             {"name": "Model Fit and Modification"},
             {"name": "Structural Models: Mediation and Moderation"},
             {"name": "Measurement Invariance"},
             {"name": "PLS-SEM"},
             {"name": "Causality and Common Method Bias"},
             {"name": "Software, Reporting and Practice"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What SEM Is, and Is Not"},

        {"type": "content", "label": "Definition", "title": "SEM is a family of models for variables you cannot observe directly",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "term", "word": "Structural equation modelling",
                        "def": "A framework that combines a measurement model (how observed "
                        "indicators relate to unobserved latent variables) with a structural "
                        "model (how the latent variables relate to each other), estimated "
                        "together so that measurement error is separated from the "
                        "relationships of interest."},
                       {"t": "body", "html": "Women's empowerment, trust in institutions, "
                        "food insecurity, job satisfaction, service quality: none is a column "
                        "in a dataset. Each is inferred from several imperfect questions. "
                        "Ordinary regression on a summed score treats the sum as the thing "
                        "and its error as zero, which attenuates every coefficient and hides "
                        "how well the questions measured anything. SEM makes the measurement "
                        "explicit and testable."}],
              "right": [{"t": "bullets", "color": "cyan", "items": [
                  "Path analysis (Wright, 1921) is SEM with observed variables only.",
                  "Confirmatory factor analysis (J&ouml;reskog, 1969) is SEM with a measurement model only.",
                  "The full model (LISREL, 1970s) puts them together: latent variables measured by indicators, related by regressions.",
                  "Growth curve models, multilevel SEM, latent class models and PLS-SEM are extensions or cousins; sections 07 to 09 touch them.",
                  "Bollen's <em>Structural Equations with Latent Variables</em> (Wiley, 1989) and Kline's <em>Principles and Practice</em> (5th ed., Guilford, 2023) are the two texts this course leans on."]},
                        {"t": "hbox", "color": "amber", "html": "SEM is a way of estimating a "
                         "theory you already have. It is not a way of finding one in the "
                         "data."}]},
         ]},

        {"type": "content", "label": "Diagram", "title": "The path diagram: reading the picture",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Symbol", "Meaning"],
                        "rows": [
                            ["Rectangle", "Observed (manifest) variable: a survey item, a measured quantity"],
                            ["Oval", "Latent variable (factor, construct): unobserved, inferred from indicators"],
                            ["Single-headed arrow", "A directed effect: regression coefficient (structural) or factor loading (measurement)"],
                            ["Double-headed arrow", "A covariance or correlation, with no direction claimed"],
                            ["Small arrow into a variable, or a circle", "Error or disturbance: the part not explained by the model"],
                            ["Triangle (rare)", "The constant, when means and intercepts are modelled"]]}],
              "right": [{"t": "body", "html": "A diagram is a set of equations. Every arrow is "
                        "a parameter to estimate, every missing arrow is a restriction (a "
                        "coefficient fixed at zero), and it is the missing arrows that make "
                        "the model testable. A model with an arrow between every pair of "
                        "variables fits any data perfectly and says nothing. The discipline "
                        "of SEM is deciding which arrows to leave out, before seeing the "
                        "data, for reasons you can state."},
                        {"t": "panel", "color": "cyan", "title": "An example, in words", "html":
                         "Membership of a self-help group (observed) affects savings "
                         "behaviour (latent, three items) which affects women's decision-"
                         "making (latent, five items). Membership may also affect "
                         "decision-making directly. Two latent variables, eight items, "
                         "three structural paths, and a mediation hypothesis. Section 07 "
                         "estimates it."},
                        {"t": "hbox", "color": "amber", "html": "Draw the diagram before "
                         "collecting data. It tells you how many items each construct needs "
                         "and which questions the survey must contain."}]},
         ]},

        {"type": "content", "label": "Why Bother", "title": "What SEM buys, and what it costs",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "What it buys", "html":
                         "Coefficients corrected for measurement error, so a true effect is "
                         "not attenuated by noisy questions. A test of whether the questions "
                         "measure what you say (the measurement model). Several equations "
                         "estimated at once, so mediation and indirect effects come with "
                         "standard errors. A test of the whole theory against the data, not "
                         "one coefficient at a time. Comparison of the same model across "
                         "groups, languages or waves, with a test of whether the measurement "
                         "held."},
                        {"t": "panel", "color": "red", "title": "What it costs", "html":
                         "Sample sizes in the hundreds. Assumptions about distributions, "
                         "linearity and the correctness of the model's omissions. A large "
                         "set of decisions (indicators, estimator, fit thresholds, "
                         "modifications) each of which can be made to flatter the model. "
                         "And a literature in South Asian business and social-science "
                         "journals where every model fits, every hypothesis is supported, "
                         "and the reader learns nothing, because the decisions were made to "
                         "produce that."}],
              "right": [{"t": "body", "html": "The method is sound and much of its use is "
                        "not. This course is organised around the decisions, in the order "
                        "they arise, with the defensible choice at each and the common "
                        "abuse beside it. A reader who follows it will produce a model that "
                        "can fail, which is the only kind worth reporting."},
                        {"t": "hbox", "color": "amber", "html": "If a summed scale and OLS "
                         "would answer the question, use them. SEM earns its place when "
                         "measurement is in doubt, when mediation is the question, or when "
                         "groups must be compared on a latent construct."}]},
         ]},

        {"type": "content", "label": "Two Traditions", "title": "Covariance-based SEM and PLS-SEM: two methods with one name",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["", "Covariance-based SEM (CB-SEM)", "Partial least squares SEM (PLS-SEM)"],
              "rows": [
                  ["What it fits", "The full covariance matrix of the indicators, by maximum likelihood or a robust variant", "A sequence of regressions on weighted composites of the indicators"],
                  ["Latent variables", "Common factors: the shared variance of the indicators, error separated", "Composites: weighted sums of the indicators, error included"],
                  ["Goal", "Test a theory: does the implied covariance matrix match the observed one?", "Predict and explain: maximise explained variance of the endogenous composites"],
                  ["Global fit test", "Yes: chi-square and the fit indices", "No exact test; SRMR and prediction-based assessment"],
                  ["Sample size", "Larger; hundreds", "Smaller samples tolerated, with caveats"],
                  ["Software", "lavaan (R), Mplus, AMOS, Stata sem, JASP, semopy (Python)", "SmartPLS, SEMinR (R), ADANCO, cSEM (R)"],
                  ["Where common", "Psychology, sociology, public health, education", "Marketing, information systems, management; South Asian business schools"],
                  ["Sections", "02 to 08, 10, 11", "09"]]},
             {"t": "body", "cls": "sm", "html": "They are different estimators of different "
              "things, and the choice between them is a choice about the question, not "
              "about which software the department owns. Section 09 gives the case for "
              "each; Hair and colleagues' 'silver bullet' paper (<em>Journal of Marketing "
              "Theory and Practice</em> 2011, 19:139) and R&ouml;nkk&ouml; and Evermann's "
              "reply (<em>Organizational Research Methods</em> 2013, 16:425) are the two "
              "sides."},
         ]},

        {"type": "content", "label": "Where It Appears", "title": "SEM in development and social research",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Field", "Typical constructs", "Typical model"],
              "rows": [
                  ["Women's empowerment", "Decision-making, mobility, control over assets, attitudes to violence", "CFA of a multidimensional scale; invariance across states or languages; effects of a programme on each dimension"],
                  ["Health behaviour", "Knowledge, attitudes, perceived risk, self-efficacy, intention", "Theory of planned behaviour as a mediation chain; intention mediating knowledge to practice"],
                  ["Education", "Teacher motivation, school climate, student engagement, achievement", "Multilevel SEM: students within schools; growth models across grades"],
                  ["Service delivery and governance", "Trust in institutions, perceived corruption, satisfaction, willingness to pay", "Structural model of trust to compliance; invariance across districts"],
                  ["Livelihoods and finance", "Financial literacy, risk attitude, social capital, savings behaviour", "Mediation of programme exposure through social capital"],
                  ["Management and marketing (business schools)", "Technology acceptance, service quality, job satisfaction, intention to adopt", "PLS-SEM of UTAUT or SERVQUAL-type models on convenience samples"],
                  ["Psychology and psychometrics", "Well-being, depression, resilience scales", "CFA and bifactor models; validation of translated instruments"]]},
             {"t": "body", "cls": "sm", "html": "The unifying feature is a construct that a "
              "single question cannot capture and that the argument needs to treat as one "
              "thing. In development work the commonest use, and the most valuable, is "
              "validating a translated scale before an evaluation relies on it."},
         ]},

        {"type": "content", "label": "Vocabulary", "title": "Vocabulary and notation used throughout",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Term", "Meaning"],
                        "rows": [
                            ["Indicator, item, manifest variable", "An observed variable that measures a construct"],
                            ["Latent variable, factor, construct", "The unobserved variable the indicators measure"],
                            ["Loading (&lambda;)", "The regression of an indicator on its factor; standardised, its correlation with the factor"],
                            ["Exogenous", "A variable with no arrows pointing into it"],
                            ["Endogenous", "A variable with at least one arrow into it"],
                            ["Disturbance (&zeta;), error (&epsilon;, &delta;)", "Unexplained variance in an endogenous latent or an indicator"],
                            ["Reflective measurement", "The construct causes the indicators (arrows from oval to rectangles)"],
                            ["Formative measurement", "The indicators define the construct (arrows from rectangles to oval)"]]}],
              "right": [{"t": "table",
                         "head": ["Term", "Meaning"],
                         "rows": [
                             ["Free parameter", "Estimated from the data"],
                             ["Fixed parameter", "Set by the analyst (usually 0 or 1)"],
                             ["Degrees of freedom", "Known covariances minus free parameters"],
                             ["Identified", "Every parameter has a unique solution"],
                             ["&chi;&sup2; (chi-square)", "The test of exact fit: implied versus observed covariances"],
                             ["Direct, indirect, total effect", "A path; a product of paths through a mediator; their sum"],
                             ["Invariance", "The same measurement model holds across groups"],
                             ["Modification index", "The expected drop in &chi;&sup2; from freeing one fixed parameter"]]},
                        {"t": "hbox", "color": "cyan", "html": "Greek letters follow the "
                         "LISREL convention where they appear; the words are what matter."}]},
         ]},

        {"type": "content", "label": "This Course", "title": "How the course is arranged, and what it assumes",
         "blocks": [
             {"t": "flow", "steps": [
                 "MEASURE: latent variables, CFA, reliability, validity (02&ndash;03)",
                 "SPECIFY: the model, its identification, its data and estimator (04&ndash;05)",
                 "FIT: judge and, carefully, modify (06)",
                 "RELATE: structural paths, mediation, moderation (07)",
                 "COMPARE: invariance across groups and languages (08)",
                 "ALTERNATIVE: PLS-SEM, and when it is the right tool (09)",
                 "INTERPRET AND REPORT: causality, method bias, software, the write-up (10&ndash;11)"]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Assumed: regression at the level of "
                        "Econometrics 101, and the survey and scale material in Survey Design "
                        "101. Worked numbers are illustrative unless a source is named, with "
                        "magnitudes chosen to be realistic so the reader learns to read the "
                        "output. Code is given in lavaan syntax because it is free, readable "
                        "and the reference implementation; every other package has an "
                        "equivalent."}],
              "right": [{"t": "hbox", "color": "amber", "html": "The free companion is "
                        "Rosseel's lavaan tutorial at lavaan.ugent.be. For the theory, "
                        "Kline (2023). For PLS-SEM, Hair and colleagues, <em>A Primer on "
                        "PLS-SEM</em> (3rd ed., Sage, 2022), read alongside its critics."}]},
         ]},

        # ===================== SECTION 02: LATENT VARIABLES AND CFA =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "Latent Variables and CFA"},

        {"type": "content", "label": "The Common Factor", "title": "The common factor model: what a latent variable is, mathematically",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "The measurement equation", "html":
                         "<em>x<sub>i</sub></em> = &tau;<sub>i</sub> + &lambda;<sub>i</sub>&eta; + &epsilon;<sub>i</sub><br><br>"
                         "Each indicator <em>x<sub>i</sub></em> is an intercept, plus a loading "
                         "times the factor &eta;, plus an error unique to that indicator. The "
                         "factor is what the indicators share; the errors are what they do "
                         "not. Under the model, the covariance between two indicators is "
                         "&lambda;<sub>i</sub>&lambda;<sub>j</sub> Var(&eta;), and that is what "
                         "CFA tests: does the observed covariance matrix look like one "
                         "generated by a few factors?"},
                        {"t": "body", "cls": "sm", "html": "Standardised, &lambda;&sup2; is the "
                         "share of the indicator's variance explained by the factor; 1 &minus; "
                         "&lambda;&sup2; is error. A loading of 0.7 means about half the item "
                         "is signal."}],
              "right": [{"t": "bullets", "color": "amber", "items": [
                  "The factor has no natural scale. It is given one by fixing one loading to 1 (the marker indicator) or fixing the factor variance to 1. The choice changes the unstandardised numbers and nothing else.",
                  "Errors are assumed uncorrelated with the factor and, by default, with each other. A correlated error between two items says they share something beyond the factor (identical wording, adjacency in the questionnaire) and must be argued for.",
                  "Exploratory factor analysis lets every item load on every factor and asks how many factors there are. CFA fixes most loadings to zero in advance and asks whether the specified structure holds. Use EFA on a new scale in a development sample; CFA to confirm it on a fresh one."]},
                        {"t": "hbox", "color": "green", "html": "'Latent' does not mean 'real'. "
                         "A factor is a statistical summary of shared variance; whether it "
                         "corresponds to empowerment is a validity argument, section 03."}]},
         ]},

        {"type": "content", "label": "Reflective vs Formative", "title": "Reflective or formative: which way do the arrows point?",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Reflective", "html":
                         "The construct causes the indicators. Depression causes low mood, "
                         "poor sleep and loss of appetite; the items are interchangeable "
                         "symptoms, they should correlate, dropping one changes little, and "
                         "reliability makes sense. Most attitude and psychological scales. "
                         "The common factor model applies."},
                        {"t": "panel", "color": "amber", "title": "Formative", "html":
                         "The indicators define the construct. Socioeconomic status is "
                         "income, education and occupation; they need not correlate, "
                         "dropping one changes the meaning, and 'reliability' is the wrong "
                         "question. A composite, not a factor. Estimated as a weighted sum, "
                         "with weights from the outcomes it predicts (MIMIC models) or fixed "
                         "by the analyst (an index)."}],
              "right": [{"t": "body", "html": "Getting this wrong is the commonest "
                        "specification error in applied SEM and it is invisible in the fit "
                        "statistics. A formative construct forced into a reflective model "
                        "shows low loadings and poor 'reliability' that are not defects of "
                        "measurement but of the model. Jarvis, MacKenzie and Podsakoff "
                        "(<em>Journal of Consumer Research</em> 2003, 30:199) give the "
                        "decision rules; Bollen and Lennox (1991) the theory."},
                        {"t": "bullets", "color": "cyan", "sm": True, "items": [
                            "Ask: if the construct rose, would every indicator rise? (Reflective.) If one indicator rose, would the construct rise? (Formative.)",
                            "A wealth index from asset ownership is formative. A scale of attitudes toward girls' education is reflective. Household food insecurity (HFIAS) is argued both ways and usually treated as reflective.",
                            "CB-SEM handles formative constructs awkwardly and needs identification tricks; PLS-SEM handles them natively, which is one legitimate reason to use it."]}]},
         ]},

        {"type": "content", "label": "Specifying a CFA", "title": "Specifying a CFA: constructs, items, and the syntax",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "lavaan syntax", "html":
                         "<code>model &lt;- '<br>"
                         "&nbsp;&nbsp;decide =~ d1 + d2 + d3 + d4 + d5<br>"
                         "&nbsp;&nbsp;mobility =~ m1 + m2 + m3<br>"
                         "&nbsp;&nbsp;assets =~ a1 + a2 + a3 + a4<br>"
                         "'<br>"
                         "fit &lt;- cfa(model, data = df, estimator = \"MLR\")<br>"
                         "summary(fit, fit.measures = TRUE, standardized = TRUE)</code>"},
                        {"t": "body", "cls": "sm", "html": "<code>=~</code> reads 'is measured "
                         "by'. Three factors, twelve items, the factors correlated by default "
                         "(a double-headed arrow among the ovals), the first loading of each "
                         "factor fixed to 1 by default, errors uncorrelated. Twelve lines of "
                         "output later you have loadings, factor covariances, error variances "
                         "and fit."}],
              "right": [{"t": "bullets", "color": "amber", "items": [
                  "Three indicators per factor is the practical minimum; four or more gives the factor its own degrees of freedom and lets a bad item be dropped.",
                  "Each item loads on one factor (simple structure) unless there is a reason. Cross-loadings are argued, not discovered.",
                  "Items should be on comparable scales; a 5-point item and a 0&ndash;100 item on one factor produce loadings that are hard to read. Standardised output helps.",
                  "Name the factors by what the items ask, not by what you hope they measure. 'decide' for five items about who decides is honest; 'empowerment' for the same five is a claim."]},
                        {"t": "hbox", "color": "green", "html": "Equivalents: Stata "
                         "<code>sem (Decide -> d1 d2 d3 d4 d5) ...</code>; AMOS by drawing; "
                         "JASP by dragging items into factors; Python <code>semopy</code> "
                         "uses lavaan's syntax."}]},
         ]},

        {"type": "content", "label": "Reading Output", "title": "Reading CFA output: a worked example",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Factor and item", "Unstd. &lambda;", "SE", "Std. &lambda;", "R&sup2;", "Comment"],
                        "rows": [
                            ["decide =~ d1 (who decides on food purchases)", "1.000", "&mdash;", "0.71", "0.50", "Marker; fixed"],
                            ["decide =~ d2 (large purchases)", "1.18", "0.09", "0.79", "0.62", ""],
                            ["decide =~ d3 (visiting family)", "1.05", "0.09", "0.74", "0.55", ""],
                            ["decide =~ d4 (own health care)", "0.97", "0.10", "0.68", "0.46", ""],
                            ["decide =~ d5 (children's schooling)", "0.62", "0.11", "0.41", "0.17", "Weak; shares little with the others"],
                            ["mobility =~ m1", "1.000", "&mdash;", "0.82", "0.67", ""],
                            ["mobility =~ m2", "0.94", "0.07", "0.77", "0.59", ""],
                            ["mobility =~ m3", "0.88", "0.08", "0.70", "0.49", ""],
                            ["decide ~~ mobility (correlation)", "", "", "0.46", "", "Related, distinct"]]},
                       {"t": "body", "cls": "sm", "html": "Illustrative; n = 640 women. "
                        "Standardised loadings above about 0.5 (R&sup2; above 0.25) are the "
                        "conventional floor; d5 fails it. The factor correlation of 0.46 says "
                        "decision-making and mobility are not the same thing, which matters "
                        "for section 03's discriminant validity."}],
              "right": [{"t": "panel", "color": "cyan", "title": "What to do about d5", "html":
                         "Not delete it on sight. Ask why: children's schooling decisions "
                         "may be made jointly in most households, so the item does not "
                         "discriminate; or the question was badly translated; or it belongs "
                         "to a different construct. Check the item's distribution and the "
                         "cognitive-interview notes. Drop it only with a reason you can "
                         "write, and re-run the model on a fresh sample if the scale will "
                         "be used again."},
                        {"t": "hbox", "color": "amber", "html": "The standard errors are as "
                         "important as the loadings. A loading of 0.62 with SE 0.11 is not "
                         "different from 0.85 at conventional levels."}]},
         ]},

        {"type": "content", "label": "Higher Order", "title": "Higher-order and bifactor models: when constructs have structure",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Empowerment measured as decision-making, "
                        "mobility and control over assets raises the question whether there "
                        "is one empowerment or three. A <strong>second-order model</strong> "
                        "puts a general factor above the three, which then load on it; it "
                        "is identified with three or more first-order factors and says the "
                        "three are manifestations of one thing. A <strong>bifactor "
                        "model</strong> lets every item load on a general factor and on its "
                        "specific factor at once, and asks how much of the variance is "
                        "general."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Compare the second-order model against the correlated-factors model: it is nested and can only fit worse; if it fits nearly as well, the general factor is supported.",
                           "Bifactor models fit almost anything and are over-used; Reise's omega-hierarchical and the explained common variance (ECV) say whether the general factor is worth having.",
                           "A general factor that explains 40% of the common variance and specific factors that explain little means 'empowerment' is one thing here; the reverse means it is three, and the programme's effects should be reported on each."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Why it matters for evaluation", "html":
                         "A programme that raises mobility and not decision-making shows a "
                         "small effect on a single empowerment score and a large one on one "
                         "dimension. Kabeer's own definition (1999) treats resources, agency "
                         "and achievements as related and distinct, which is a "
                         "correlated-factors model rather than a second-order one. The "
                         "measurement model is a theory of the construct, and it should be "
                         "chosen to match the theory the evaluation is testing."},
                        {"t": "hbox", "color": "green", "html": "Report the correlated-factors "
                         "model first. Add the higher-order structure only if the argument "
                         "needs one score."}]},
         ]},

        {"type": "content", "label": "Ordinal Items", "title": "Likert items are ordinal, and the model should know",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A five-point agreement item is not a continuous "
                        "measurement. Treating it as one with maximum likelihood works "
                        "tolerably with five or more categories and roughly symmetric "
                        "distributions, and fails with skewed items or four or fewer "
                        "categories: loadings are attenuated and fit is distorted. The "
                        "ordinal treatment assumes a continuous latent response behind each "
                        "item, estimates thresholds and polychoric correlations, and fits the "
                        "model to those by diagonally weighted least squares (WLSMV in Mplus "
                        "and lavaan)."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Flora and Curran (<em>Psychological Methods</em> 2004, 9:466) show WLSMV recovers loadings well down to two categories; ML does not below five.",
                           "In lavaan: <code>ordered = c(\"d1\", ..., \"d5\")</code> and the estimator switches automatically.",
                           "Binary items (yes/no decision questions, the common form in DHS-style modules) require the ordinal treatment; ML on binary items is wrong.",
                           "Fit indices under WLSMV are on a different footing from ML; compare within an estimator, not across."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Practical consequences", "html":
                         "Most empowerment, attitude and knowledge items in South Asian "
                         "surveys are binary or three-category. That means WLSMV, "
                         "polychoric correlations, thresholds in the output, and a sample "
                         "large enough for the weight matrix to be stable (several hundred). "
                         "It also means the familiar Cronbach's alpha, computed on the raw "
                         "items, understates reliability; the ordinal alpha or omega from "
                         "the polychoric matrix is the right one."},
                        {"t": "hbox", "color": "green", "html": "Plot the item distributions "
                         "before choosing an estimator. An item with 92% 'yes' carries "
                         "little information whatever the estimator."}]},
         ]},

        {"type": "content", "label": "EFA First", "title": "Exploratory factor analysis: the step before CFA on a new scale",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Decision", "Recommended", "Avoid"],
                        "rows": [
                            ["Extraction", "Principal axis factoring or ML factor analysis", "Principal components analysis (it is not factor analysis; it models total variance)"],
                            ["Number of factors", "Parallel analysis (Horn 1965); scree with judgement; theory", "The eigenvalue-greater-than-1 rule alone (over-extracts)"],
                            ["Rotation", "Oblique (oblimin, promax): factors are allowed to correlate", "Varimax by default (forces independence the constructs rarely have)"],
                            ["Item retention", "Loading above 0.4 on one factor, cross-loadings below 0.3, with content review", "Deleting items purely on statistics"],
                            ["Sample", "A development sample, then CFA on a separate sample", "EFA and CFA on the same respondents"],
                            ["Correlation matrix", "Polychoric for ordinal items", "Pearson on binary items"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "EFA on a new or translated scale "
                        "shows how the items actually cluster before you tell the CFA how "
                        "they should. Split the sample at random, explore on one half, "
                        "confirm on the other; or explore on the pilot and confirm on the "
                        "main survey. Running CFA on the sample the EFA was tuned to is "
                        "confirming what you just fitted."},
                        {"t": "hbox", "color": "amber", "html": "Parallel analysis is in R's "
                         "<em>psych</em> package (<code>fa.parallel</code>) and in JASP and "
                         "jamovi. It compares eigenvalues against those from random data of "
                         "the same size and is the one factor-count rule that survives "
                         "scrutiny."}]},
         ]},

        {"type": "content", "label": "Item Design", "title": "Items that make CFA work: what to fix at the questionnaire stage",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "Four to six items per construct, so that dropping one still leaves a testable factor.",
                  "Items that vary: an item everyone agrees with has no variance to share. Pilot for ceiling and floor effects.",
                  "One idea per item. 'I can decide about my own health care and my children's' is two items.",
                  "Consistent response scales within a construct, and reverse-worded items used sparingly: they often form their own method factor, especially in translation.",
                  "Translation with back-translation and cognitive interviewing in each language, and the same item order in every version.",
                  "Record which respondents answered which language version; section 08 needs it."]}],
              "right": [{"t": "panel", "color": "amber", "title": "The reverse-item factor", "html":
                         "Scales with half the items reversed ('I am satisfied' / 'I am "
                         "not satisfied') routinely show a two-factor CFA solution that is "
                         "wording, not content. In Hindi and Bangla, negatively worded "
                         "items are more often misread, and the artefact is larger. Either "
                         "avoid reversal or model a method factor for the reversed items "
                         "and report it. Never present the wording factor as a substantive "
                         "finding."},
                        {"t": "hbox", "color": "green", "html": "Survey Design 101 covers the "
                         "questionnaire; this slide is the part of it that decides whether "
                         "the CFA can succeed. The measurement model is written in the "
                         "questionnaire, not in the software."}]},
         ]},

        # ===================== SECTION 03: RELIABILITY AND VALIDITY =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "Reliability and Validity"},

        {"type": "content", "label": "Reliability", "title": "Reliability: alpha, omega and what each assumes",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Coefficient", "Assumes", "Computed from", "Use"],
                        "rows": [
                            ["Cronbach's &alpha; (1951)", "Equal loadings (tau-equivalence), uncorrelated errors", "Item covariances", "Familiar; understates reliability when loadings differ; overstates it with many items or correlated errors"],
                            ["McDonald's &omega; (composite reliability)", "The CFA model holds", "Loadings and error variances", "The default for a scale with a fitted CFA; report it instead of or beside &alpha;"],
                            ["Ordinal &alpha; / &omega;", "As above, on the polychoric matrix", "Polychoric correlations, thresholds", "For Likert and binary items"],
                            ["&omega;<sub>h</sub> (hierarchical)", "Bifactor model", "General-factor loadings", "How much of the total score is the general factor"],
                            ["Test-retest", "Stability of the construct", "Two administrations", "For traits, not states; rarely feasible in field surveys"],
                            ["Inter-rater", "Multiple observers", "Agreement statistics (&kappa;, ICC)", "Observational measures, enumerator-rated items"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "Reliability is the share of "
                        "observed-score variance that is true-score variance: how repeatable "
                        "the measurement is, not whether it measures the right thing. Values "
                        "above 0.7 are conventional for research use and above 0.8 or 0.9 "
                        "for individual decisions; the thresholds are conventions, not "
                        "findings. Composite reliability = (&Sigma;&lambda;)&sup2; / "
                        "[(&Sigma;&lambda;)&sup2; + &Sigma;&theta;] from the standardised "
                        "CFA."},
                        {"t": "hbox", "color": "amber", "html": "An &alpha; of 0.95 on a "
                         "twelve-item scale is often a sign of redundancy (six items asked "
                         "twice), not of excellence. Report &omega; and the number of "
                         "items."}]},
         ]},

        {"type": "content", "label": "Convergent Validity", "title": "Convergent validity: do the items agree about something?",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Convergent validity in the CFA sense is that "
                        "the items of a construct share enough variance to be measuring one "
                        "thing. The evidence is the loadings (all substantial, all "
                        "significant) and the average variance extracted, AVE = mean of the "
                        "squared standardised loadings, the share of item variance the factor "
                        "explains on average. Fornell and Larcker (<em>Journal of Marketing "
                        "Research</em> 1981, 18:39) proposed 0.5 as the floor: the factor "
                        "explains more of its items than error does."},
                       {"t": "stats", "cols": 3, "cards": [
                           {"num": "&ge; 0.5", "label": "AVE floor (Fornell and Larcker 1981)", "color": "cyan", "source": "Convention"},
                           {"num": "&ge; 0.7", "label": "composite reliability floor", "color": "green", "source": "Convention"},
                           {"num": "&ge; 0.5", "label": "standardised loading floor, with 0.7 preferred", "color": "amber", "source": "Hair et al.; Kline"}]}],
              "right": [{"t": "bullets", "color": "amber", "items": [
                  "In the worked CFA, 'decide' has AVE = (0.50 + 0.62 + 0.55 + 0.46 + 0.17) / 5 = 0.46 with d5, and 0.53 without it. The threshold is crossed by dropping one item, which is exactly the kind of decision that should be stated and justified.",
                  "AVE below 0.5 with composite reliability above 0.6 is sometimes accepted (Fornell and Larcker's own note); say so if you rely on it.",
                  "The thresholds are conventions from marketing research in 1981. They are useful defaults and poor gods; a scale that fails them by a little and has strong theory and invariance evidence is better than one that clears them by item deletion.",
                  "Convergent validity in the broader sense (the scale correlates with other measures of the same thing) is a separate and stronger test, when another measure exists."]}]},
         ]},

        {"type": "content", "label": "Discriminant Validity", "title": "Discriminant validity: are the constructs different from each other?",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Criterion", "Rule", "Notes"],
                        "rows": [
                            ["Fornell-Larcker", "&radic;AVE of each construct exceeds its correlation with every other construct", "Traditional; weak at detecting problems when loadings vary (Henseler et al. 2015)"],
                            ["HTMT (heterotrait-monotrait ratio)", "Ratio of between-construct to within-construct item correlations below 0.85 (strict) or 0.90 (lenient); bootstrap CI excludes 1", "Henseler, Ringle and Sarstedt, <em>J Acad Marketing Sci</em> 2015, 43:115; now the default in PLS-SEM and increasingly in CB-SEM"],
                            ["Factor correlation CI", "The 95% CI of the correlation between two factors excludes 1", "Direct and simple; report the correlation and CI"],
                            ["Chi-square difference", "A model with the two factors merged fits significantly worse", "A nested-model test; sensitive to sample size"],
                            ["Cross-loadings", "Each item loads more on its own construct than on others", "Weak; mainly a PLS-SEM habit"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "Two factors correlated at 0.92 are "
                        "one factor with two names, and any 'effect' of one on the other is "
                        "an effect of a thing on itself. Discriminant validity is the check "
                        "that the constructs in a structural model are distinct enough for "
                        "the paths between them to mean anything. It is where over-fitted "
                        "models most often fail, and where the failure is most often hidden "
                        "by reporting only the Fornell-Larcker table."},
                        {"t": "hbox", "color": "amber", "html": "In the worked example, "
                         "decide and mobility correlate at 0.46 with &radic;AVE of 0.73 and "
                         "0.77. Distinct by every criterion."}]},
         ]},

        {"type": "content", "label": "Beyond the CFA", "title": "Validity is an argument, and the CFA is one piece of it",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A scale can have clean loadings, high omega and "
                        "perfect discriminant validity and still not measure what it claims. "
                        "Messick (1995) and the <em>Standards for Educational and "
                        "Psychological Testing</em> (2014) frame validity as the evidence "
                        "supporting a specific interpretation of scores for a specific use. "
                        "The CFA is internal-structure evidence. The other kinds come from "
                        "outside the model."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "<strong>Content</strong>: do the items cover the construct as defined, judged by experts and by the people being measured? Cognitive interviews in the field are content evidence.",
                           "<strong>Response process</strong>: do respondents understand the items as intended? Think-aloud pilots.",
                           "<strong>Relations to other variables</strong>: does the score correlate with what it should (known-groups: members versus non-members) and not with what it should not (social desirability)?",
                           "<strong>Consequences</strong>: what happens when the score is used, and to whom?"]}],
              "right": [{"t": "panel", "color": "amber", "title": "The development-sector case", "html":
                         "A decision-making scale validated in Bangladesh in 2005 is "
                         "administered in Odisha in 2025 in Odia. The CFA fitting well says "
                         "the Odia items cohere. It does not say they mean what the Bangla "
                         "ones meant, that 'deciding' has the same content in a different "
                         "household structure, or that a higher score is empowerment "
                         "rather than a change in who is asked. Section 08's invariance "
                         "tests address the first; the others need fieldwork, and a "
                         "paragraph in the paper."},
                        {"t": "hbox", "color": "green", "html": "Write the validity argument "
                         "as a paragraph with the CFA as one sentence of it. A table of "
                         "AVEs is not a validity argument."}]},
         ]},

        {"type": "content", "label": "Worked Validity", "title": "A worked validity table for a three-construct scale",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Construct", "Items", "&omega;", "AVE", "&radic;AVE", "r with decide", "r with mobility", "HTMT (max)"],
                        "rows": [
                            ["decide", "4 (d5 dropped)", "0.81", "0.53", "0.73", "&mdash;", "", "0.52"],
                            ["mobility", "3", "0.81", "0.59", "0.77", "0.46", "&mdash;", "0.52"],
                            ["assets", "4", "0.78", "0.48", "0.69", "0.38", "0.31", "0.44"]]},
                       {"t": "body", "cls": "sm", "html": "Illustrative. 'assets' has AVE just "
                        "under 0.5 with acceptable reliability; the paper says so rather than "
                        "dropping a fourth item to cross the line. Every construct's "
                        "&radic;AVE exceeds its correlations, and every HTMT is below 0.85. "
                        "The note gives the estimator (WLSMV), the sample, and that d5 was "
                        "dropped for a stated reason before the structural model was fitted."}],
              "right": [{"t": "panel", "color": "cyan", "title": "What the table is for", "html":
                         "A reader can see in one glance that the three constructs are "
                         "reliable enough, coherent enough and distinct enough to carry a "
                         "structural model, and where the weak point is. That is the whole "
                         "job of the measurement section. The structural results in "
                         "section 07 are read against it: an effect of assets on "
                         "decision-making is an effect of a construct with AVE 0.48, and "
                         "the reader is entitled to weigh that."},
                        {"t": "hbox", "color": "amber", "html": "Report this table for every "
                         "SEM paper, before any path coefficient. Referees at good journals "
                         "look for it first."}]},
         ]},

        {"type": "content", "label": "Known Groups", "title": "Known-groups and criterion validity: does the score behave as it should?",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The cheapest external validity check is to ask "
                        "whether the latent score differs between groups that theory says it "
                        "must. A decision-making scale should score higher among women with "
                        "their own income than without, higher among household heads than "
                        "daughters-in-law, and should not differ by enumerator. Each is a "
                        "latent mean comparison (section 04) or a regression of the factor "
                        "on the grouping variable, and each either supports the "
                        "interpretation or raises a question the CFA could not."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Choose the groups before the analysis, from the construct's theory. Post hoc 'known groups' are noise.",
                           "A difference in the wrong direction is a finding about the scale or the setting, not a nuisance.",
                           "Criterion validity: the score should predict an outcome measured differently (an administrative record, a partner's report, later behaviour). One such correlation is worth several fit indices."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Illustrative", "html":
                         "Latent decision-making: women with own income 0.34 SD higher "
                         "(95% CI 0.18 to 0.50); household heads 0.51 SD higher (0.29 to "
                         "0.73); no difference by enumerator (largest 0.06, CI including "
                         "0). The husband's independent report of who decides correlates "
                         "0.38 with the woman's latent score. Together with the CFA and the "
                         "reliability table, that is a validity argument; the CFA alone is "
                         "a coherence argument."},
                        {"t": "hbox", "color": "green", "html": "Plan the criterion into the "
                         "survey. A partner's report or an administrative link costs a "
                         "module and buys the strongest validity evidence available."}]},
         ]},

        {"type": "content", "label": "Scale Translation", "title": "Validating a translated scale: the sequence",
         "blocks": [
             {"t": "flow", "steps": [
                 "FORWARD translate by two independent translators; reconcile",
                 "BACK translate blind; compare with the source; resolve",
                 "EXPERT panel: content equivalence, cultural fit, reading level",
                 "COGNITIVE interviews in the field (n = 10&ndash;20 per language)",
                 "PILOT (n = 100&ndash;200 per language): item distributions, EFA",
                 "MAIN survey: CFA per language, then invariance tests across languages (section 08)"]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A South Asian evaluation often fields one "
                        "instrument in three languages. Pooling the languages in one CFA "
                        "assumes the items work the same way in each, which is exactly what "
                        "has to be shown. The sequence above is the standard (Beaton and "
                        "colleagues, <em>Spine</em> 2000, 25:3186, for health measures; "
                        "the ITC guidelines for tests), and the last step is the one most "
                        "often skipped."}],
              "right": [{"t": "hbox", "color": "amber", "html": "Budget the cognitive "
                        "interviews. They cost a fortnight and find the item that means "
                        "something different in Bangla, which no statistic will."}]},
         ]},

        # ===================== SECTION 04: SPECIFICATION AND IDENTIFICATION =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Specification and Identification"},

        {"type": "content", "label": "From Theory", "title": "Specification: the model is the theory written as arrows",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Every arrow in the structural model is a "
                        "hypothesis with a direction, and every absent arrow is the "
                        "hypothesis that two things are unrelated once the rest of the model "
                        "is accounted for. Both come from theory, prior evidence, or the "
                        "logic of the programme, and both are written down before the data "
                        "are analysed. A model whose arrows were chosen to fit is not a "
                        "test of anything; it is a description of one sample."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Start from the theory of change or the published theory (the theory of planned behaviour, Kabeer's resources-agency-achievements) and translate it construct by construct.",
                           "Decide the direction of each arrow from time order, mechanism or design. Cross-sectional data cannot decide it for you.",
                           "Decide what is exogenous. In an evaluation, programme exposure is; in a cross-sectional attitude survey, almost nothing is.",
                           "Write the list of omitted paths and why each is omitted. That list is the model's content."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Recursive and non-recursive", "html":
                         "A recursive model has no feedback loops: arrows run one way and "
                         "disturbances are uncorrelated. It is always identified given an "
                         "identified measurement model. A non-recursive model (trust "
                         "affects participation and participation affects trust) needs "
                         "instruments, one excluded exogenous variable per loop, and is "
                         "identified only if they exist. Most applied models are recursive "
                         "and should say so; a feedback loop is a claim that needs an "
                         "instrument, not an arrow."},
                        {"t": "hbox", "color": "green", "html": "Pre-register the diagram. "
                         "OSF takes a PDF of it, and a registered model is one that referees "
                         "cannot suspect of being found in the data."}]},
         ]},

        {"type": "content", "label": "Counting", "title": "Identification: can the parameters be estimated at all?",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The data supply <em>p</em>(<em>p</em> + 1)/2 "
                        "unique variances and covariances for <em>p</em> observed variables "
                        "(plus <em>p</em> means if modelled). The model asks for some number "
                        "of free parameters. If it asks for more than the data supply, it is "
                        "under-identified and no unique solution exists. If exactly as many, "
                        "just-identified: it fits perfectly and tests nothing. If fewer, "
                        "over-identified, with degrees of freedom equal to the difference, "
                        "and the fit test has something to test."},
                       {"t": "stats", "cols": 3, "cards": [
                           {"num": "78", "label": "known moments for 12 indicators: 12 &times; 13 / 2", "color": "cyan", "source": "Counting rule"},
                           {"num": "27", "label": "free parameters in a 3-factor CFA: 9 loadings, 12 error variances, 3 factor variances, 3 covariances", "color": "amber", "source": "With three markers fixed"},
                           {"num": "51", "label": "degrees of freedom: the model is over-identified and testable", "color": "green", "source": "78 &minus; 27"}]}],
              "right": [{"t": "bullets", "color": "amber", "items": [
                  "The counting rule (df &ge; 0) is necessary, not sufficient. A model can pass it and still have unidentified parts.",
                  "Each latent variable needs a scale: fix one loading to 1 or the factor variance to 1.",
                  "The three-indicator rule: a single factor with three or more indicators, uncorrelated errors, is identified. With two indicators it is identified only if the factor correlates with something else in the model. One indicator needs its error variance fixed from a known reliability.",
                  "Software warns of non-identification with messages about non-positive-definite matrices, huge standard errors or failure to converge. Take the warnings literally."]},
                        {"t": "hbox", "color": "green", "html": "Kline's chapter on "
                         "identification and Bollen's chapter 4 give the rules for every "
                         "case; the counting rule and the three-indicator rule cover most "
                         "applied models."}]},
         ]},

        {"type": "content", "label": "Single Indicators", "title": "Single indicators and observed variables in a latent model",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Programme membership, age, household size and "
                        "income are measured once and enter the model as observed variables, "
                        "with arrows from rectangles. That is correct for variables measured "
                        "without much error. For a single-item construct that is noisy (a "
                        "one-question trust measure), the model can still separate error if "
                        "the analyst fixes the error variance at (1 &minus; reliability) "
                        "&times; the observed variance, using a reliability from a prior "
                        "study."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Do not build a 'latent' variable from one item with a free error variance; it is not identified and software will either fail or fix it silently.",
                           "A latent variable measured by a single composite score (a summed scale) is a common compromise: fix the error from the scale's omega. It loses the measurement test but keeps the error correction.",
                           "Categorical exogenous variables (state, caste category) enter as dummies, as in regression."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Programme exposure as the exogenous variable", "html":
                         "In an evaluation, the structural model's first exogenous variable "
                         "is treatment, observed and binary. Its paths into the latent "
                         "outcomes are the programme effects, corrected for measurement "
                         "error in the outcomes, and its path into a mediator and the "
                         "mediator's path onward give the mechanism. Randomisation makes "
                         "the treatment arrow causal; nothing makes the mediator arrow "
                         "causal (section 10). The model is still worth fitting for the "
                         "measurement correction alone."},
                        {"t": "hbox", "color": "green", "html": "Treatment as an observed "
                         "exogenous variable is the one arrow in most SEMs that a "
                         "reviewer will accept as causal without argument."}]},
         ]},

        {"type": "content", "label": "Controls", "title": "Covariates: where they go and what they do",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A covariate that predicts an endogenous latent "
                        "variable gets an arrow into it, from an observed rectangle. Every "
                        "endogenous variable the covariate might affect gets one; leaving a "
                        "covariate out of one equation is a restriction that must be true "
                        "for the model to be right. Covariates correlate with each other and "
                        "with the exogenous latents by default (double-headed arrows), and "
                        "those correlations are estimated, not restricted."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Include the covariates the design needs (stratification variables, baseline outcome) and the confounders theory names. Not every variable in the dataset.",
                           "Each covariate costs parameters and degrees of freedom; with twelve covariates and three endogenous latents that is 36 paths. The model gets large and the fit indices harder to read.",
                           "An alternative for many covariates: residualise the indicators on the covariates first, then fit the SEM to the residuals. It is honest if stated and it keeps the model readable.",
                           "In a randomised evaluation, covariates in the treatment equation are not needed and their presence changes nothing except precision."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Clustered data", "html":
                         "Respondents in villages, students in schools. The default "
                         "standard errors assume independence and are too small. Options, "
                         "in order of ease: cluster-robust standard errors "
                         "(<code>cluster = \"village\"</code> in lavaan; <code>vce(cluster)</code> "
                         "in Stata); a multilevel SEM if the village-level construct is "
                         "itself of interest; or design-based estimation with survey weights "
                         "(<em>lavaan.survey</em>). The first is enough for most evaluation "
                         "uses and is the one referees now expect."},
                        {"t": "hbox", "color": "green", "html": "Survey weights change the "
                         "estimates; clustering changes the standard errors. Both belong "
                         "in the methods, with the level of clustering stated."}]},
         ]},

        {"type": "content", "label": "Equivalent Models", "title": "Equivalent models: the same fit, a different story",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "For almost any structural model there exist "
                        "others, with different arrows, that imply exactly the same "
                        "covariance matrix and therefore fit identically. Reverse a path "
                        "between two exogenous-free variables, replace a path with a "
                        "correlation, swap a mediator and an outcome: the &chi;&sup2; does "
                        "not move. MacCallum and colleagues (<em>Psychological Bulletin</em> "
                        "1993, 114:185) found that published models routinely had dozens of "
                        "equivalent alternatives and that authors never mentioned them."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Fit supports a model only relative to the alternatives that fit worse. It cannot choose among those that fit the same.",
                           "Stelzl's and Lee-Hershberger's replacing rules generate the equivalent models; Kline's chapter 8 walks through them.",
                           "The only things that break the equivalence are design (randomisation, time order) and theory strong enough to rule alternatives out."]}],
              "right": [{"t": "panel", "color": "amber", "title": "The applied consequence", "html":
                         "'Social capital increases savings behaviour (&beta; = 0.34, "
                         "p &lt; .001), and the model fits well' is compatible with savings "
                         "behaviour increasing social capital, and with both being driven "
                         "by an unmeasured trait, at identical fit. The path coefficient "
                         "is the same number under all three. A paper that presents one "
                         "story as established by the fit has not understood what the fit "
                         "tested."},
                        {"t": "hbox", "color": "green", "html": "State at least one equivalent "
                         "model in the discussion and say why you prefer yours. It is a "
                         "sentence, and it is the difference between a test and an "
                         "assertion."}]},
         ]},

        {"type": "content", "label": "Means", "title": "Means and intercepts: when the model needs them",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The default SEM fits covariances only; means "
                        "are ignored and every intercept is free. A mean structure adds the "
                        "item intercepts and the latent means to the model and is needed for "
                        "three purposes: comparing latent means across groups (does the "
                        "treatment group have higher empowerment, on the latent scale?), "
                        "measurement invariance beyond the metric level (section 08), and "
                        "growth models where the trajectory's intercept and slope are the "
                        "latent variables."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "With a mean structure, the marker indicator's intercept is fixed to 0 (or the latent mean to 0 in a reference group) to identify the latent mean.",
                           "<code>meanstructure = TRUE</code> in lavaan; Stata's <code>sem</code> includes means by default.",
                           "Latent mean differences are reported in the latent metric, which has no units; standardise by the reference group's latent SD to get a Cohen's d."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Why the latent mean beats the summed score", "html":
                         "A treatment effect on a summed score of five items weights each "
                         "item equally and mixes measurement error into the estimate. The "
                         "latent mean difference weights items by their loadings, "
                         "separates error, and, under scalar invariance, is a comparison on "
                         "the same scale in both groups. It is the right effect size for a "
                         "latent outcome in an evaluation, and it comes with a standard "
                         "error from the same model."},
                        {"t": "hbox", "color": "green", "html": "Report both. The summed-score "
                         "difference is what a programme officer understands; the latent "
                         "difference is what a methodologist trusts."}]},
         ]},

        {"type": "content", "label": "Specification Checklist", "title": "Before estimation: the specification checklist",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Question", "Answer written down"],
              "rows": [
                  ["What are the constructs, and is each reflective or formative?", "A definition and a direction for each, with the source"],
                  ["Which items measure which construct, and why?", "The mapping, with the questionnaire numbers"],
                  ["Which structural paths exist, and in which direction?", "The diagram, with a one-line justification per arrow"],
                  ["Which paths are deliberately absent?", "The list, because it is what makes the model testable"],
                  ["Which variables are exogenous?", "Named; treatment if randomised, otherwise argued"],
                  ["Which covariates, into which equations?", "The list and the reason"],
                  ["Is the model recursive?", "Yes, or the instruments for each loop"],
                  ["Is it identified?", "The counting rule and the indicator rule, checked"],
                  ["Is the data clustered or weighted?", "The cluster variable and the weights"],
                  ["Are the items ordinal?", "Then the estimator is WLSMV and thresholds are in the model"],
                  ["Are means needed?", "Yes for group comparison, invariance or growth"],
                  ["Registered?", "Where, when, with the diagram"]]},
             {"t": "body", "cls": "sm", "html": "Twelve questions. Answered before the "
              "software opens, they become the methods section. Answered after, they become "
              "the things a referee asks about, and the answers tend to be whatever made "
              "the model fit."},
         ]},

        # ===================== SECTION 05: ESTIMATION, DATA AND SAMPLE SIZE =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Estimation, Data and Sample Size"},

        {"type": "content", "label": "Estimators", "title": "Estimators: ML, robust ML, and WLSMV",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Estimator", "Assumes", "Use when", "Notes"],
              "rows": [
                  ["ML (maximum likelihood)", "Multivariate normality of continuous indicators; complete data or FIML", "Continuous, roughly normal items; the default in most software", "Standard errors and &chi;&sup2; wrong under non-normality, usually too small"],
                  ["MLR / MLM (robust ML)", "Continuous indicators; corrects SEs and &chi;&sup2; for non-normality (Satorra-Bentler)", "Continuous items that are skewed, which is most of them", "The safe default for continuous data; lavaan <code>estimator = \"MLR\"</code>"],
                  ["FIML", "Data missing at random (MAR); used with ML/MLR", "Any missing data on the indicators", "Uses every case; better than listwise deletion in almost every situation (Enders 2010)"],
                  ["WLSMV / DWLS", "Latent continuous response behind each ordinal item", "Likert with fewer than five categories, binary items", "Pairwise-present for missing data by default; needs several hundred cases"],
                  ["Bayesian", "Priors on parameters", "Small samples, complex models, informative prior knowledge", "Mplus and blavaan; report priors and sensitivity"],
                  ["ULS / GLS", "Weaker assumptions; less used", "Rarely", "Historical interest"],
                  ["PLS", "None on distributions; composites, not factors", "Section 09", "Not a CB-SEM estimator"]]},
             {"t": "body", "cls": "sm", "html": "The estimator follows from the data, not "
              "from the software's default. Five-point items with a skewed distribution and "
              "some missingness: WLSMV with pairwise or multiple imputation, or MLR with FIML "
              "if the categories are numerous enough. Report the estimator, the missing-data "
              "treatment and the reason for each."},
         ]},

        {"type": "content", "label": "Non-Normality", "title": "Non-normality is the norm, and what it does",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Attitude and behaviour items in field surveys "
                        "are skewed: most respondents agree, or most report never. Under "
                        "ordinary ML, skew and kurtosis inflate the &chi;&sup2; (the model is "
                        "rejected too often), deflate the standard errors (paths look more "
                        "significant than they are), and distort the fit indices in the "
                        "direction of rejection. The parameter estimates themselves are "
                        "mostly fine. The fix is a robust estimator and it costs nothing."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Check univariate skewness and kurtosis for every item; Mardia's multivariate kurtosis as a summary. Values well above 2 (skew) or 7 (kurtosis) on many items call for MLR or WLSMV.",
                           "Satorra-Bentler scaled &chi;&sup2; (1994; 2001 difference test) and the robust fit indices are what to report under MLR.",
                           "Bootstrapping the standard errors (Bollen-Stine for the &chi;&sup2;) is the alternative, and it is what mediation needs anyway (section 07).",
                           "Transforming items to reduce skew changes what they measure; do not."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Outliers and careless responses", "html":
                         "A respondent who gave the same answer to forty items, or who "
                         "finished a thirty-minute module in four, contributes a pattern no "
                         "model should fit. Screen for straight-lining, implausible speed "
                         "and multivariate outliers (Mahalanobis distance) before "
                         "estimation, decide the rule in advance, and report how many "
                         "cases were removed and why. Enumerator effects are the field "
                         "version: a CFA that fails in one enumerator's interviews and "
                         "fits in the rest is a data-quality finding."},
                        {"t": "hbox", "color": "green", "html": "Survey Design 101's "
                         "high-frequency checks are the upstream fix. A clean dataset makes "
                         "every slide in this section easier."}]},
         ]},

        {"type": "content", "label": "Missing Data", "title": "Missing data: FIML and multiple imputation, and what not to do",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Listwise deletion (drop any case with any "
                        "missing item) throws away information, biases estimates unless the "
                        "data are missing completely at random, and can halve a sample with "
                        "twenty items and 5% missingness each. Full-information maximum "
                        "likelihood uses every case's available data under the weaker "
                        "missing-at-random assumption and is the default in Mplus and one "
                        "option away in lavaan (<code>missing = \"fiml\"</code>). Enders "
                        "(<em>Applied Missing Data Analysis</em>, Guilford, 2010) is the "
                        "reference."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "FIML with MLR handles continuous items; for WLSMV, use multiple imputation (m = 20 or more) and pool with <em>semTools</em>' <code>runMI</code>, or accept pairwise-present with caution.",
                           "Auxiliary variables that predict missingness (age, enumerator, interview length) make MAR more plausible; include them via the saturated-correlates approach.",
                           "Report the missingness per item and its pattern. 'Data were complete' is rarely true in a field survey and is checked."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Not missing at random", "html":
                         "Women who refuse the decision-making module may be the ones with "
                         "least say. No estimator fixes that from the data alone. The "
                         "honest treatments are a sensitivity analysis (pattern-mixture "
                         "or selection models, or simply bounding the result under "
                         "extreme assumptions) and a sentence in the limitations that says "
                         "which direction the bias would run. 'Missing at random was "
                         "assumed' is an assumption, and a reader is owed the reasoning."},
                        {"t": "hbox", "color": "green", "html": "Mean imputation and 'replace "
                         "with the scale mean' shrink variances and inflate correlations. "
                         "Never."}]},
         ]},

        {"type": "content", "label": "Sample Size", "title": "How many respondents: the rules of thumb and the honest answer",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Rule", "Says", "Status"],
                        "rows": [
                            ["n &ge; 200", "A floor for any SEM", "A folk rule; often too few for ordinal items or many parameters, sometimes more than needed"],
                            ["n:q &ge; 10 (Jackson 2003)", "Ten cases per free parameter; 20 preferred", "A better rule; 27 parameters need 270&ndash;540"],
                            ["Five to ten per indicator", "For CFA", "Crude; ignores loadings and the number of factors"],
                            ["Power for RMSEA (MacCallum, Browne and Sugawara 1996)", "n for a given df to detect misfit", "Answers the fit question, not the parameter question"],
                            ["Monte Carlo simulation (Muth&eacute;n and Muth&eacute;n 2002)", "Simulate the planned model with expected loadings and effects; find n for adequate power and bias", "The right answer; <em>simsem</em> in R, Mplus's Monte Carlo"],
                            ["Wolf et al. 2013 (<em>Educ Psychol Meas</em> 73:913)", "Required n ranged from 30 to 460 across ordinary models", "The evidence that no single rule works"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "Sample size depends on the number "
                        "of indicators, the size of the loadings (strong loadings need fewer "
                        "cases), the number and size of structural paths, the estimator "
                        "(WLSMV wants more), missingness, and what power is wanted for which "
                        "effect. A simulation with the planned model takes an afternoon and "
                        "replaces every rule of thumb. For a field evaluation with three "
                        "latent outcomes, four items each and binary items, expect to need "
                        "500 or more, and to say why."},
                        {"t": "hbox", "color": "amber", "html": "Small samples do not make SEM "
                         "impossible; they make convergence failures, improper solutions and "
                         "wide intervals likely, and the paper must report all three rather "
                         "than the one model that ran."}]},
         ]},

        {"type": "content", "label": "Convergence", "title": "When the model will not run, or runs wrong",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Symptom", "Likely cause", "What to do"],
              "rows": [
                  ["Non-convergence after many iterations", "Under-identification; poor starting values; an empirically weak factor", "Check identification; simplify; supply starting values from a simpler model"],
                  ["Heywood case: negative error variance", "Over-fitting; a factor with two indicators; an outlier; a misspecified model", "Do not fix the variance to zero and move on; find the cause; consider dropping the two-indicator factor or merging"],
                  ["Standardised loading above 1", "As above, or a factor correlation near 1 (two factors are one)", "Discriminant validity check; merge factors"],
                  ["Correlation between factors above 1", "Two factors are one", "Merge, or the model is wrong"],
                  ["Enormous standard errors on one parameter", "Empirical under-identification", "The parameter is not estimable with these data; fix or drop it"],
                  ["Non-positive-definite covariance matrix", "Linear dependence among items; a mis-coded item; too few cases", "Check the correlation matrix; find the duplicate"],
                  ["Different results across software", "Different defaults (marker, estimator, missing data, means)", "Match the defaults; report them"]]},
             {"t": "body", "cls": "sm", "html": "Every warning is information about the model "
              "or the data. Suppressing warnings, fixing variances at zero, or trying "
              "estimators until one converges are ways of hiding it. A paper that reports "
              "an improper solution and explains it is more credible than one that reports "
              "a clean one nobody believes."},
         ]},

        {"type": "content", "label": "Worked Estimation", "title": "A worked estimation report",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Item", "Choice", "Reason"],
                        "rows": [
                            ["Sample", "n = 640 women in 32 villages; 14 cases removed for straight-lining (rule set before analysis)", "Design; pre-specified screening"],
                            ["Items", "11 items across three constructs, all binary or three-category", "Questionnaire"],
                            ["Estimator", "WLSMV on polychoric correlations, with thresholds", "Ordinal items; Flora and Curran 2004"],
                            ["Missing data", "3.1% of item responses missing, at most 6% on any item; pairwise-present under WLSMV; multiple-imputation check (m = 20) gave the same loadings to two decimals", "Reported and checked"],
                            ["Clustering", "Village-clustered standard errors", "Sampling design"],
                            ["Scaling", "First loading of each factor fixed at 1; results reported standardised", "Convention"],
                            ["Software", "R 4.4, lavaan 0.6-19, semTools 0.5-6", "Reproducibility"],
                            ["Convergence", "Normal; no improper values; all standardised loadings between 0.41 and 0.82", "Checked"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "Illustrative. This is the estimation "
                        "paragraph of the methods, as a table. Every row is a decision a "
                        "reader might have made differently and can now see. It takes ten "
                        "minutes to write and is absent from most SEM papers in the "
                        "journals this course's readers publish in."},
                        {"t": "hbox", "color": "amber", "html": "Software versions matter: "
                         "lavaan's default handling of ordinal missing data and its "
                         "robust-fit-index formulas have changed across versions."}]},
         ]},

        {"type": "content", "label": "Bootstrapping", "title": "Bootstrapping: standard errors and intervals without normality",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Resample the cases with replacement, refit "
                        "the model, record every parameter; repeat 1,000 to 5,000 times. The "
                        "spread of the estimates is a standard error that assumes nothing "
                        "about normality, and the percentiles are a confidence interval that "
                        "can be asymmetric, which matters for products of coefficients "
                        "(indirect effects) whose sampling distribution is skewed. Section 07 "
                        "relies on it."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "<code>se = \"bootstrap\", bootstrap = 5000</code> in lavaan; <code>vce(bootstrap)</code> in Stata; a checkbox in AMOS.",
                           "Bias-corrected intervals were the standard (Preacher and Hayes 2008) and can be liberal; percentile intervals are now often preferred (Hayes 2022).",
                           "Bootstrap within clusters when the data are clustered, or the intervals are too narrow.",
                           "The Bollen-Stine bootstrap gives a &chi;&sup2; p-value robust to non-normality, as an alternative to the Satorra-Bentler correction."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Cost and reporting", "html":
                         "Five thousand refits of an ordinal model with FIML can take an "
                         "hour. Run it once, at the end, on the final model, and store the "
                         "results. Report the number of resamples, the interval type, the "
                         "random seed, and the interval itself rather than a p-value: "
                         "'indirect effect 0.11, 95% percentile bootstrap CI 0.04 to 0.19, "
                         "5,000 resamples' is the sentence."},
                        {"t": "hbox", "color": "green", "html": "The bootstrap resamples the "
                         "respondents you have. It does not fix a biased sample, a wrong "
                         "model or a missing confounder."}]},
         ]},

        # ===================== SECTION 06: MODEL FIT AND MODIFICATION =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Model Fit and Modification"},

        {"type": "content", "label": "The Chi-Square", "title": "The chi-square test: the one exact test, and why nobody likes it",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The model implies a covariance matrix; the "
                        "data supply one; the &chi;&sup2; statistic, (n &minus; 1) times the "
                        "fit function, tests whether the difference is zero. A significant "
                        "&chi;&sup2; means the model does not reproduce the data exactly. "
                        "With a few hundred cases almost every model is rejected, because "
                        "no model is exactly right and the test has power to see it; with "
                        "fifty cases almost none is, because the test cannot see anything. "
                        "The test is correct and its verdict is rarely the question."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Report it always: &chi;&sup2;, df, p, and the scaling factor under MLR. Never omit it because it is significant.",
                           "&chi;&sup2;/df ratios ('below 3', 'below 5') have no theoretical basis and depend on n; retire them.",
                           "The difference between two nested models' &chi;&sup2; is a test of the restriction that separates them, and that use of the statistic is unambiguous and valuable (sections 07 and 08).",
                           "A non-significant &chi;&sup2; with n = 80 is not evidence of good fit; it is evidence of low power."]}],
              "right": [{"t": "panel", "color": "amber", "title": "What a rejected model means", "html":
                         "That something is missing or wrong: a cross-loading, a correlated "
                         "error, a path, a non-linearity, an outlying group. The residual "
                         "covariance matrix (observed minus implied, standardised) says "
                         "where. Look at it before looking at the fit indices, which "
                         "summarise the misfit into one number and lose the location. A "
                         "large residual between two items of different factors is a "
                         "finding about the questionnaire; a large residual between two "
                         "items of one factor is a finding about the factor."},
                        {"t": "hbox", "color": "green", "html": "Standardised residuals above "
                         "|2| are worth looking at; above |4| are worth explaining in the "
                         "paper."}]},
         ]},

        {"type": "content", "label": "Fit Indices", "title": "The fit indices: what each measures and the conventional cutoffs",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Index", "Measures", "Conventional threshold", "Behaviour"],
              "rows": [
                  ["RMSEA (Steiger-Lind; Browne and Cudeck 1993)", "Misfit per degree of freedom, in the population; with a 90% CI", "&le; 0.06 (Hu and Bentler 1999); &le; 0.08 acceptable; CI upper bound &lt; 0.10", "Penalises complexity; unreliable with small df; report the CI"],
                  ["CFI (Bentler 1990)", "Improvement over the null model of no correlations, 0 to 1", "&ge; 0.95; &ge; 0.90 acceptable", "Depends on how bad the null is; inflated when items barely correlate"],
                  ["TLI / NNFI", "As CFI, with a parsimony penalty; can exceed 1", "&ge; 0.95", "As CFI"],
                  ["SRMR", "Average standardised residual correlation", "&le; 0.08", "The most direct; not affected by n in the same way"],
                  ["AIC, BIC", "Likelihood with a complexity penalty", "Lower is better; no absolute meaning", "For comparing non-nested models on the same data"],
                  ["GFI, AGFI", "Historical", "Do not report", "Depend on n; superseded"]]},
             {"t": "body", "cls": "sm", "html": "Hu and Bentler (<em>Structural Equation "
              "Modeling</em> 1999, 6:1) derived their cutoffs from simulations of particular "
              "models and warned against treating them as universal; the field ignored the "
              "warning. Marsh, Hau and Wen (2004) and Kline (2023) both argue the cutoffs "
              "are too strict for some models and too lenient for others, and that the "
              "residuals matter more. Report RMSEA with its CI, CFI, TLI and SRMR, alongside "
              "the &chi;&sup2;, and interpret them together."},
         ]},

        {"type": "content", "label": "Reading Fit", "title": "Reading fit with judgement: three cases",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Case", "&chi;&sup2; (df)", "RMSEA [90% CI]", "CFI", "SRMR", "Reading"],
                        "rows": [
                            ["A. 3-factor CFA, n = 640, WLSMV", "112.4 (41), p &lt; .001", "0.052 [0.041, 0.064]", "0.96", "0.048", "Rejected by &chi;&sup2; as expected at this n; approximate fit is acceptable on every index; check residuals for the location of misfit"],
                            ["B. Same model, n = 140", "48.7 (41), p = 0.19", "0.037 [0.000, 0.078]", "0.97", "0.071", "Not rejected, but the RMSEA CI runs to 0.078 and SRMR is near its limit: the data cannot distinguish good fit from mediocre"],
                            ["C. Structural model with 6 constructs, 24 items, n = 640", "612.0 (237), p &lt; .001", "0.050 [0.045, 0.055]", "0.91", "0.062", "CFI at the lenient threshold, RMSEA good: typical of large models where CFI suffers; acceptable, with the misfit located and reported"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "Illustrative. The indices "
                        "disagree in each case, and the disagreement is information: about "
                        "sample size in B, about model size in C. A paper that reports 'all "
                        "fit indices met the recommended thresholds' has stopped where the "
                        "reading starts."},
                        {"t": "hbox", "color": "amber", "html": "Fit indices under WLSMV are "
                         "computed differently and tend to look better than under ML for "
                         "the same model. Compare within an estimator."}]},
         ]},

        {"type": "content", "label": "Modification Indices", "title": "Modification indices: the road to a model that fits and means nothing",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "For every fixed parameter, the software reports "
                        "the expected drop in &chi;&sup2; if it were freed. Free the largest, "
                        "refit, repeat, and any model will reach any fit threshold. "
                        "MacCallum, Roznowski and Necowitz (<em>Psychological Bulletin</em> "
                        "1992, 111:490) showed that such specification searches capitalise "
                        "on chance: the modifications rarely replicate in a new sample, and "
                        "the final model is a description of the sample's noise. This is the "
                        "single most common way SEM papers in applied journals are made to "
                        "'fit'."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Look at modification indices to understand misfit, not to fix it.",
                           "Free a parameter only if it has a substantive reason you would have accepted before seeing the index: two items with near-identical wording, two items adjacent in the questionnaire, a path the theory predicts but you forgot.",
                           "Report every modification, its reason, and the fit before and after. A reader must be able to see the original model.",
                           "Cross-validate: modify on one half of the sample, test on the other. If the modified model does not fit the holdout, it was noise."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Correlated errors, in particular", "html":
                         "The commonest modification is a correlated error between two "
                         "items. It says the items share something beyond their factor. "
                         "Sometimes true (a shared stem, a shared method), and then it "
                         "should have been in the model from the start. Usually it is a "
                         "sign that the factor is not what the items measure, and adding "
                         "the correlation hides that. Five correlated errors in a "
                         "twelve-item CFA is a different scale from the one specified, and "
                         "the reliability and validity numbers must be recomputed on it."},
                        {"t": "hbox", "color": "red", "html": "A model with modifications "
                         "is exploratory. Say so, and do not test hypotheses on it as if it "
                         "were the pre-specified one."}]},
         ]},

        {"type": "content", "label": "Nested Comparison", "title": "Comparing nested models: the chi-square difference test",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Two models are nested if one is the other "
                        "with some parameters fixed. The difference in their &chi;&sup2; "
                        "values, on the difference in their degrees of freedom, tests "
                        "whether the restriction holds. This is the principled way to ask "
                        "most SEM questions: is a path zero (fix it and compare)? Are two "
                        "factors one (fix their correlation to 1 and compare)? Does the "
                        "model hold across groups (section 08)? Is the second-order factor "
                        "adequate (compare with the correlated-factors model)?"},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Under MLR or WLSMV, the scaled difference test (Satorra-Bentler 2001; lavaan's <code>lavTestLRT</code>) is needed; the raw difference of scaled &chi;&sup2; values is not &chi;&sup2; distributed.",
                           "With large n the test rejects small restrictions; report the change in CFI and RMSEA alongside (&Delta;CFI &gt; 0.01 is the usual practical criterion, Cheung and Rensvold 2002).",
                           "For non-nested models (different indicators, different constructs), AIC and BIC, or out-of-sample prediction, not the difference test."]}],
              "right": [{"t": "panel", "color": "amber", "title": "The model comparison as the result", "html":
                         "A paper that fits one model and reports its indices has shown "
                         "the model is not absurd. A paper that fits the theoretical model "
                         "and two rivals (the mediation model against the direct-effects "
                         "model; the three-factor scale against a one-factor version) and "
                         "shows which the data prefer has shown something. Design the "
                         "comparison before estimation; it is what turns fit into "
                         "evidence."},
                        {"t": "hbox", "color": "green", "html": "In the worked CFA: the "
                         "one-factor model has &chi;&sup2; = 418 on 44 df against 112 on "
                         "41. The three-factor structure is supported by a difference of "
                         "306 on 3 df, whatever the absolute indices say."}]},
         ]},

        {"type": "content", "label": "Reporting Fit", "title": "Reporting fit: the sentence and the table",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "The sentence", "html":
                         "'The three-factor model fit the data acceptably: scaled "
                         "&chi;&sup2;(41) = 112.4, p &lt; .001; RMSEA = 0.052, 90% CI "
                         "[0.041, 0.064]; CFI = 0.96; TLI = 0.95; SRMR = 0.048 (WLSMV, "
                         "n = 640). The largest standardised residual (2.9) was between "
                         "items d2 and a1; no modifications were made. A one-factor "
                         "alternative fit substantially worse (&Delta;&chi;&sup2;(3) = "
                         "306, &Delta;CFI = 0.19).'"},
                        {"t": "body", "cls": "sm", "html": "Every number a reader needs, the "
                         "misfit located, the alternative rejected, the modifications "
                         "(none) stated. Four lines."}],
              "right": [{"t": "table",
                         "head": ["Model", "&chi;&sup2; (df)", "RMSEA [CI]", "CFI", "TLI", "SRMR", "&Delta;&chi;&sup2; (&Delta;df) vs M1"],
                         "rows": [
                             ["M1: three correlated factors", "112.4 (41)", "0.052 [0.041, 0.064]", "0.96", "0.95", "0.048", "&mdash;"],
                             ["M2: one factor", "418.3 (44)", "0.115 [0.105, 0.126]", "0.77", "0.71", "0.104", "306 (3), p &lt; .001"],
                             ["M3: second-order factor over the three", "115.0 (41)", "0.053 [0.042, 0.065]", "0.96", "0.95", "0.050", "2.6 (0), not nested with M1 in df; equivalent fit"],
                             ["M4: M1 with d5 dropped", "78.9 (32)", "0.048 [0.035, 0.061]", "0.97", "0.96", "0.041", "Different items; not comparable by &chi;&sup2;"]]},
                        {"t": "hbox", "color": "amber", "html": "Illustrative. The table is "
                         "where the model comparison lives; the sentence is what the "
                         "abstract carries."}]},
         ]},

        {"type": "content", "label": "Fit Pitfalls", "title": "How fit is gamed, and how a reader can tell",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Practice", "What it does", "Tell-tale sign"],
              "rows": [
                  ["Freeing correlated errors from modification indices", "Improves fit by describing noise", "Several error correlations with no substantive rationale; fit 'after modification' only"],
                  ["Deleting items until AVE and fit pass", "Changes the construct to whatever the survivors measure", "A 12-item scale reported with 6 items and no account of the other 6"],
                  ["Item parcelling (averaging items into a few composites)", "Hides item-level misfit; inflates fit", "Two or three 'indicators' per factor that are themselves averages; no item-level CFA"],
                  ["Reporting the model that converged", "Survivorship", "No mention of alternatives tried or of warnings"],
                  ["Reporting &chi;&sup2;/df instead of &chi;&sup2; and p", "Obscures rejection", "The ratio without the components"],
                  ["Choosing lenient thresholds after seeing the values", "Moves the goalposts", "Citations to whichever paper's cutoff the model clears"],
                  ["Fitting a saturated structural model", "Nothing to test", "df of the structural part is zero; fit is the CFA's fit"],
                  ["Comparing WLSMV indices against ML cutoffs", "Flatters the model", "WLSMV with CFI = 0.99 on a model that looks ordinary"]]},
             {"t": "body", "cls": "sm", "html": "None of these is fraud; each is a decision "
              "made after seeing the data and reported as if made before. The remedy is "
              "the same in every case: register the model, report the first fit and the "
              "final fit, and list what changed between them."},
         ]},

        # ===================== SECTION 07: STRUCTURAL MODELS =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Structural Models: Mediation and Moderation"},

        {"type": "content", "label": "Two Steps", "title": "Measurement first, then structure: the two-step approach",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Anderson and Gerbing (<em>Psychological "
                        "Bulletin</em> 1988, 103:411) argued for fitting the measurement model "
                        "as a CFA (all factors correlated) before imposing any structural "
                        "paths, so that misfit in the measurement is found and fixed where it "
                        "belongs and the structural model is tested against a measurement "
                        "model that is known to hold. The structural model is nested in the "
                        "CFA (it replaces free correlations with paths and zeros), so the "
                        "&chi;&sup2; difference between them is the test of the structural "
                        "restrictions alone."},
                       {"t": "flow", "steps": [
                           "CFA: all constructs, all correlated; assess and fix measurement",
                           "STRUCTURAL: replace correlations with the theorised paths",
                           "COMPARE: &Delta;&chi;&sup2; between them tests the omitted paths",
                           "INTERPRET: paths, indirect effects, R&sup2; of each endogenous construct"]}],
              "right": [{"t": "bullets", "color": "amber", "items": [
                  "If the structural model fits much worse than the CFA, the omitted paths matter; the residuals say which.",
                  "If the structural part is saturated (every construct connected to every other), it fits exactly as well as the CFA and tests nothing. Such models are common and their fit statistics are the CFA's.",
                  "Report the CFA fit and the structural fit separately, and the difference.",
                  "The one-step alternative (fit everything at once) is fine for a well-established scale, and hides measurement problems behind structural ones for a new one."]},
                        {"t": "hbox", "color": "green", "html": "R&sup2; for each endogenous "
                         "latent variable is reported alongside the paths; a significant "
                         "path into a construct with R&sup2; = 0.04 explains little."}]},
         ]},

        {"type": "content", "label": "Mediation", "title": "Mediation: direct, indirect and total effects",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "The model", "html":
                         "<em>M</em> = <em>a</em> <em>X</em> + <em>e</em><sub>M</sub><br>"
                         "<em>Y</em> = <em>c&prime;</em> <em>X</em> + <em>b</em> <em>M</em> + <em>e</em><sub>Y</sub><br><br>"
                         "Indirect effect of <em>X</em> on <em>Y</em> through <em>M</em>: "
                         "<em>ab</em>. Direct effect: <em>c&prime;</em>. Total: <em>c&prime;</em> + <em>ab</em>. "
                         "In SEM the three are estimated together, with <em>M</em> and "
                         "<em>Y</em> latent if they are measured by several items, and the "
                         "indirect effect's standard error comes from the bootstrap "
                         "(section 05)."},
                        {"t": "body", "cls": "sm", "html": "Baron and Kenny's 1986 causal-steps "
                         "procedure (test <em>c</em>, then <em>a</em>, then <em>b</em>, then see "
                         "if <em>c&prime;</em> shrinks) is superseded: it has low power, it "
                         "requires a total effect that need not exist when paths offset, and "
                         "it never tests the indirect effect itself. Test <em>ab</em> "
                         "directly with a bootstrap interval (Preacher and Hayes, "
                         "<em>Behavior Research Methods</em> 2008, 40:879; Hayes, 2022)."}],
              "right": [{"t": "bullets", "color": "amber", "items": [
                  "The Sobel test assumes <em>ab</em> is normal; it is not, so the test is conservative. Report it only alongside the bootstrap.",
                  "'Full' and 'partial' mediation are labels about whether <em>c&prime;</em> is significant, which depends on n; report the effects and their intervals and drop the labels (Zhao, Lynch and Chen, <em>Journal of Consumer Research</em> 2010, 37:197).",
                  "The proportion mediated, <em>ab</em>/(<em>c&prime;</em> + <em>ab</em>), is unstable when the total effect is small; report it with its interval or not at all.",
                  "Several mediators: specific indirect effects through each, and the contrast between them, all bootstrapped."]},
                        {"t": "hbox", "color": "red", "html": "Every mediation estimate "
                         "assumes no unmeasured confounding of the <em>M</em>&ndash;<em>Y</em> "
                         "relationship. Randomising <em>X</em> does not deliver that. Section "
                         "10."}]},
         ]},

        {"type": "content", "label": "Worked Mediation", "title": "A worked mediation: SHG membership, savings, decision-making",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Path", "Std. estimate", "SE", "95% bootstrap CI", "Reads as"],
                        "rows": [
                            ["<em>a</em>: membership &rarr; savings (latent)", "0.38", "0.05", "[0.28, 0.48]", "Members score 0.38 SD higher on the savings factor"],
                            ["<em>b</em>: savings &rarr; decide (latent)", "0.31", "0.06", "[0.19, 0.42]", "Savings behaviour predicts decision-making, membership held constant"],
                            ["<em>c&prime;</em>: membership &rarr; decide (direct)", "0.09", "0.05", "[&minus;0.01, 0.19]", "Direct effect small and imprecise"],
                            ["<em>ab</em>: indirect", "0.12", "0.03", "[0.07, 0.18]", "The indirect path is clear"],
                            ["Total (<em>c&prime;</em> + <em>ab</em>)", "0.21", "0.05", "[0.11, 0.30]", "Overall association of membership with decision-making"],
                            ["R&sup2; savings", "0.14", "", "", ""],
                            ["R&sup2; decide", "0.12", "", "", ""]]},
                       {"t": "body", "cls": "sm", "html": "Illustrative; 5,000 percentile "
                        "bootstrap resamples, village-clustered; covariates age, education, "
                        "household size into both endogenous constructs; WLSMV; structural "
                        "fit RMSEA 0.049, CFI 0.95, SRMR 0.051."}],
              "right": [{"t": "panel", "color": "cyan", "title": "What can be said", "html":
                         "Membership was assigned by lottery in this design, so <em>a</em> "
                         "and the total effect are causal. The <em>b</em> path and therefore "
                         "the indirect effect assume that nothing unmeasured drives both "
                         "savings and decision-making among members, which the design does "
                         "not guarantee: a woman whose husband has migrated may save more "
                         "and decide more, and migration is not in the model. The sentence "
                         "in the paper: 'the association is consistent with mediation "
                         "through savings; the mediator was not randomised'."},
                        {"t": "hbox", "color": "amber", "html": "Two-thirds of the total effect "
                         "runs through the savings path in this sample. That is a finding "
                         "about where to look, not a proof of mechanism."}]},
         ]},

        {"type": "content", "label": "Moderation", "title": "Moderation: when the effect depends on something else",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A moderator changes the size or sign of an "
                        "effect: membership raises decision-making more where women's "
                        "baseline mobility is low, or less in households with a resident "
                        "mother-in-law. Statistically, an interaction term. With observed "
                        "variables it is the product <em>X</em> &times; <em>W</em>, mean-centred, "
                        "as in regression. With a latent moderator or latent predictor the "
                        "product of latents is needed, and that is where SEM has to work "
                        "harder."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "<strong>Multigroup</strong>: split by the moderator (two or three groups), fit the model in each, and test whether the path differs (equality constraint, &Delta;&chi;&sup2;). Simple, and the right choice for a categorical moderator.",
                           "<strong>Product indicators</strong> (Marsh, Wen and Hau 2004): form products of the indicators of <em>X</em> and <em>W</em> as indicators of the latent interaction. Workable; sensitive to the pairing scheme.",
                           "<strong>Latent moderated structural equations</strong> (Klein and Moosbrugger, <em>Psychometrika</em> 2000, 65:457): the principled method; in Mplus (XWITH) and now in some R packages. No conventional fit indices.",
                           "<strong>Observed moderator</strong>: keep it observed and interact it with the latent predictor via the product-indicator route, or use multigroup with the moderator cut at meaningful points."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Interpreting an interaction", "html":
                         "The coefficient on the product says how much the effect of "
                         "<em>X</em> changes per unit of <em>W</em>. It is not interpretable "
                         "alone. Plot simple slopes: the effect of <em>X</em> at low, mean "
                         "and high <em>W</em> (one SD below and above), with confidence bands, "
                         "or the Johnson-Neyman region where the effect is significant. "
                         "'The interaction was significant (&beta; = 0.11)' is a sentence "
                         "no reader can use; 'membership raised decision-making by 0.3 SD "
                         "where baseline mobility was low and by 0.05 SD where it was high' "
                         "is."},
                        {"t": "hbox", "color": "green", "html": "Interactions need more "
                         "power than main effects: roughly four times the sample for the "
                         "same precision. Plan for it or do not test them."}]},
         ]},

        {"type": "content", "label": "Conditional Process", "title": "Moderated mediation: when the mechanism depends on context",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The indirect effect may itself vary with a "
                        "moderator: savings mediate membership's effect on decision-making "
                        "where a bank is far away and not where one is near. Conditional "
                        "process models (Preacher, Rucker and Hayes, <em>Multivariate "
                        "Behavioral Research</em> 2007, 42:185; Hayes 2022) estimate the "
                        "indirect effect at values of the moderator and test whether it "
                        "changes, using the index of moderated mediation (Hayes, 2015): the "
                        "slope of the indirect effect on the moderator, with a bootstrap "
                        "interval."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Specify which path is moderated (<em>a</em>, <em>b</em>, or both) from theory, before estimation. Each is a different model.",
                           "Report the conditional indirect effects at meaningful moderator values with intervals, and the index with its interval.",
                           "Hayes's PROCESS macro (SPSS, SAS, R) does this with observed variables; SEM software does it with latents and is more work. Use PROCESS when the constructs are reliable summed scores and SEM when measurement is the point.",
                           "Every assumption of mediation applies, plus the moderator's exogeneity."]}],
              "right": [{"t": "panel", "color": "amber", "title": "How much model is too much", "html":
                         "A model with two mediators, two moderators and their products, "
                         "on 300 respondents, has perhaps twenty structural parameters and "
                         "the power to detect none of the interactions it exists to test. "
                         "The result is a paper with one 'significant' conditional indirect "
                         "effect out of eight tested, reported as the finding. Pre-specify "
                         "one conditional hypothesis, power the study for it, and present "
                         "the others as exploratory."},
                        {"t": "hbox", "color": "green", "html": "The diagram for a conditional "
                         "process model should fit on one slide and be explicable in three "
                         "sentences. If not, it is several studies."}]},
         ]},

        {"type": "content", "label": "Longitudinal", "title": "Panel data: cross-lagged models and their trap",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "With the same constructs measured at two or "
                        "more waves, the cross-lagged panel model regresses each construct "
                        "at wave 2 on both constructs at wave 1, and the cross-lagged paths "
                        "(trust at 1 to participation at 2, and the reverse) are read as "
                        "evidence of direction. Hamaker, Kuiper and Grasman "
                        "(<em>Psychological Methods</em> 2015, 20:102) showed the standard "
                        "model confounds within-person change with stable between-person "
                        "differences, and can find cross-lagged 'effects' that are entirely "
                        "trait differences. The random-intercept cross-lagged panel model "
                        "separates the two and needs three or more waves."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Two waves: a cross-lagged model is possible and its causal reading is weak; report it as association over time.",
                           "Three or more waves: RI-CLPM, with the within-person cross-lagged paths as the estimates of interest.",
                           "Measurement invariance across waves (section 08) is required before any of this; a change in the construct's measurement looks like change in the construct."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Latent growth models", "html":
                         "With three or more waves of one construct, a latent growth model "
                         "treats each respondent's trajectory as an intercept and a slope, "
                         "both latent, with their means, variances and predictors. 'Did the "
                         "programme change the slope of empowerment over three years, and "
                         "for whom?' is a growth-model question. Multilevel models answer "
                         "it too; the SEM version adds latent outcomes and measurement "
                         "invariance tests, at the cost of needing balanced waves."},
                        {"t": "hbox", "color": "green", "html": "Longitudinal SEM is where "
                         "measurement invariance stops being a formality. An item whose "
                         "meaning shifts between baseline and endline manufactures a "
                         "trajectory."}]},
         ]},

        {"type": "content", "label": "Effect Sizes", "title": "Effect sizes in SEM: what to report and in what units",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Quantity", "Report", "Interpretation"],
              "rows": [
                  ["Structural path, standardised (&beta;)", "Estimate, SE, 95% CI", "SD change in the outcome per SD change in the predictor, other predictors held constant"],
                  ["Structural path, unstandardised (B)", "Estimate, SE, CI, in the marker indicator's units", "Needed when the predictor is binary (treatment): the effect in latent-outcome units"],
                  ["Treatment effect on a latent outcome", "Latent mean difference / reference-group latent SD", "A Cohen's d corrected for measurement error"],
                  ["Indirect effect", "Standardised and unstandardised, bootstrap CI", "Product of paths; its interval is the test"],
                  ["R&sup2; of each endogenous construct", "Value", "Share of the construct's variance explained; small values are common and honest"],
                  ["f&sup2; for a path", "(R&sup2;<sub>with</sub> &minus; R&sup2;<sub>without</sub>) / (1 &minus; R&sup2;<sub>with</sub>)", "Cohen's local effect size; 0.02, 0.15, 0.35 are his small, medium, large, and are too demanding for field data"],
                  ["Factor loadings", "Standardised, with SE", "Measurement quality; not effect sizes"]]},
             {"t": "body", "cls": "sm", "html": "Standardised paths are comparable within a "
              "model and not across samples with different variances. For evaluation "
              "reporting, the unstandardised treatment effect in a named unit (or the latent "
              "d) is what a programme reader needs, and it is rarely reported."},
         ]},

        {"type": "content", "label": "Structural Syntax", "title": "The structural model in lavaan, with mediation and covariates",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Syntax", "html":
                         "<code>model &lt;- '<br>"
                         "&nbsp;&nbsp;# measurement<br>"
                         "&nbsp;&nbsp;savings =~ s1 + s2 + s3<br>"
                         "&nbsp;&nbsp;decide =~ d1 + d2 + d3 + d4<br>"
                         "&nbsp;&nbsp;# structural<br>"
                         "&nbsp;&nbsp;savings ~ a*member + age + educ + hhsize<br>"
                         "&nbsp;&nbsp;decide ~ cp*member + b*savings + age + educ + hhsize<br>"
                         "&nbsp;&nbsp;# effects<br>"
                         "&nbsp;&nbsp;ab := a*b<br>"
                         "&nbsp;&nbsp;total := cp + a*b<br>"
                         "'<br>"
                         "fit &lt;- sem(model, data = df, ordered = c(\"s1\",...,\"d4\"),<br>"
                         "&nbsp;&nbsp;&nbsp;&nbsp;cluster = \"village\", se = \"bootstrap\", bootstrap = 5000)</code>"}],
              "right": [{"t": "body", "html": "Labels (<code>a*</code>, <code>b*</code>) name "
                        "parameters; <code>:=</code> defines a new quantity from them and "
                        "gives it a standard error and, with the bootstrap, an interval. "
                        "The covariates enter both endogenous equations. Note the "
                        "limitation: lavaan's bootstrap and its ordinal estimator do not "
                        "combine in every version, and clustered bootstrapping needs care; "
                        "check the current documentation and say what was done."},
                        {"t": "bullets", "color": "amber", "sm": True, "items": [
                            "Stata: <code>sem (Savings -> s1 s2 s3) (Decide -> d1 d2 d3 d4) (Savings <- member age educ hhsize) (Decide <- member Savings age educ hhsize), vce(cluster village)</code>, then <code>estat teffects</code> for indirect effects, and <code>bootstrap</code> around it.",
                            "AMOS: draw it; tick 'indirect, direct and total effects' and 'perform bootstrap'.",
                            "Mplus: MODEL INDIRECT; the most complete for latent interactions."]}]},
         ]},

        {"type": "content", "label": "Structural Pitfalls", "title": "Structural-model pitfalls",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Pitfall", "Consequence", "Fix"],
              "rows": [
                  ["Saturated structural model", "Nothing tested; fit is the CFA's", "Omit paths the theory does not need; compare with alternatives"],
                  ["Baron-Kenny steps as the mediation test", "Low power; wrong logic", "Bootstrap the indirect effect"],
                  ["'Full mediation' claimed from a non-significant direct path", "Sample-size artefact", "Report effects and intervals; drop the labels"],
                  ["Cross-sectional mediation read as process", "Maxwell and Cole (2007) show the bias can be any size and sign", "Longitudinal design, or say 'consistent with'"],
                  ["Interaction without simple slopes", "Uninterpretable", "Plot at &plusmn;1 SD; Johnson-Neyman"],
                  ["Many mediators and moderators on a small sample", "One significant result out of many; a finding by chance", "Pre-specify one; treat others as exploratory"],
                  ["Standardised effects of a binary treatment", "Meaningless SD of a dummy", "Unstandardised, or the latent d"],
                  ["Covariates in some equations and not others without reason", "Hidden restrictions", "State the rule and apply it"],
                  ["Reversed arrows fit identically", "Direction asserted, not tested", "Name the equivalent model; use design"]]},
             {"t": "body", "cls": "sm", "html": "The last row is the one that turns a "
              "competent SEM into an over-claimed one, and section 10 is about it."},
         ]},

        # ===================== SECTION 08: MEASUREMENT INVARIANCE =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Measurement Invariance"},

        {"type": "content", "label": "The Question", "title": "Are we measuring the same thing in both groups?",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Comparing women in Bihar and Tamil Nadu on a "
                        "decision-making scale, or the same women before and after a "
                        "programme, or respondents who answered in Hindi and in Bangla, "
                        "assumes that the items relate to the construct in the same way in "
                        "each group. If a Bangla item loads more weakly, or has a different "
                        "intercept (Bangla speakers answer 'yes' more often at the same "
                        "true level), the group difference in scores mixes real difference "
                        "with measurement difference and cannot be separated. Invariance "
                        "testing checks the assumption, level by level."},
                       {"t": "term", "word": "Measurement invariance",
                        "def": "The property that the measurement model (loadings, "
                        "intercepts, error variances) is the same across groups or "
                        "occasions, so that differences in latent means and relationships "
                        "reflect the construct and not the instrument. Vandenberg and Lance, "
                        "<em>Organizational Research Methods</em> 2000, 3:4."}],
              "right": [{"t": "bullets", "color": "cyan", "items": [
                  "Required before comparing latent means across groups, before pooling groups in one model, and before longitudinal models.",
                  "Almost never tested in South Asian multi-language surveys, and almost always partly violated when it is.",
                  "The test is a sequence of nested multigroup models with increasing equality constraints, compared by &Delta;&chi;&sup2; and &Delta;CFI.",
                  "Partial invariance (most items invariant, a few freed) is the usual outcome and is enough for most comparisons if handled honestly (Byrne, Shavelson and Muth&eacute;n, <em>Psychological Bulletin</em> 1989, 105:456)."]},
                        {"t": "hbox", "color": "amber", "html": "Item Response Theory 101 in "
                         "this series covers differential item functioning, which is the "
                         "same question asked item by item."}]},
         ]},

        {"type": "content", "label": "The Levels", "title": "Configural, metric, scalar, strict: the sequence",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Level", "Constrained equal across groups", "Licenses", "Typical outcome"],
              "rows": [
                  ["Configural", "Nothing; the same pattern of loadings", "The construct has the same structure", "Usually holds"],
                  ["Metric (weak)", "Loadings", "Comparing relationships (paths, correlations) across groups", "Usually holds, or nearly"],
                  ["Scalar (strong)", "Loadings and intercepts (thresholds for ordinal items)", "Comparing latent means; pooling groups", "Often fails on one or two items; partial scalar invariance is the common result"],
                  ["Strict", "Plus error variances", "Comparing observed (summed) scores", "Often fails; rarely needed, since latent comparisons do not require it"]]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "cls": "sm", "html": "Each level is nested in the one "
                        "above; the &Delta;&chi;&sup2; tests whether the added constraints "
                        "hold. Because &Delta;&chi;&sup2; rejects trivial differences at "
                        "large n, the practical criteria are &Delta;CFI &le; 0.01 (Cheung and "
                        "Rensvold, <em>Structural Equation Modeling</em> 2002, 9:233) and "
                        "&Delta;RMSEA &le; 0.015 (Chen 2007), used together."}],
              "right": [{"t": "hbox", "color": "amber", "html": "For ordinal items the "
                        "sequence differs: thresholds and loadings are tested in a "
                        "particular order (Wu and Estabrook, <em>Psychometrika</em> 2016, "
                        "81:1014); <em>semTools</em>' <code>measEq.syntax</code> writes the "
                        "models correctly."}]},
         ]},

        {"type": "content", "label": "Worked Invariance", "title": "A worked invariance test: Hindi and Bangla versions of a scale",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Model", "&chi;&sup2; (df)", "CFI", "RMSEA", "&Delta;&chi;&sup2; (&Delta;df), p", "&Delta;CFI", "Verdict"],
                        "rows": [
                            ["Configural", "96.2 (82)", "0.981", "0.033", "&mdash;", "&mdash;", "Same structure in both"],
                            ["Metric", "108.9 (90)", "0.975", "0.036", "12.7 (8), 0.12", "&minus;0.006", "Loadings equal: holds"],
                            ["Scalar", "151.3 (98)", "0.930", "0.058", "42.4 (8), &lt; .001", "&minus;0.045", "Fails"],
                            ["Partial scalar (d3 and m2 thresholds freed)", "117.6 (94)", "0.969", "0.040", "8.7 (4) vs metric, 0.07", "&minus;0.006", "Holds with two items freed"],
                            ["Latent mean difference (Bangla &minus; Hindi), under partial scalar", "", "", "", "", "", "&minus;0.18 SD, 95% CI [&minus;0.36, 0.00]"]]},
                       {"t": "body", "cls": "sm", "html": "Illustrative; n = 320 per "
                        "language; WLSMV; thresholds rather than intercepts because the "
                        "items are ordinal. Two items behave differently across languages: "
                        "d3 ('visiting your natal family') and m2 ('going to the market "
                        "alone')."}],
              "right": [{"t": "panel", "color": "cyan", "title": "What it means, and what to do", "html":
                         "The scale measures the same construct in both languages "
                         "(configural, metric), but two items are answered differently at "
                         "the same true level, plausibly because the practices they name "
                         "differ between the regions rather than because of translation. "
                         "With those two freed, the latent means can be compared, and the "
                         "Bangla group is slightly lower, imprecisely. Had the scalar "
                         "failure been ignored and summed scores compared, the difference "
                         "would have been larger and partly an artefact of d3 and m2."},
                        {"t": "hbox", "color": "amber", "html": "Go back to the cognitive "
                         "interviews for d3 and m2. The statistics found the items; the "
                         "fieldwork explains them."}]},
         ]},

        {"type": "content", "label": "Partial Invariance", "title": "Partial invariance: how much is enough, and how to find the items",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "When scalar invariance fails, the aim is to "
                        "find the few items responsible, free their intercepts or thresholds, "
                        "and check that the rest hold. Modification indices in the "
                        "constrained model point to the items; free them one at a time, "
                        "largest first, retesting after each, and stop when &Delta;CFI "
                        "against the metric model is within tolerance. Byrne, Shavelson and "
                        "Muth&eacute;n's rule is that at least two invariant items per "
                        "factor (the marker plus one) are needed for the latent mean "
                        "comparison to be identified and meaningful; more is better."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Freeing more than a third of a factor's items is not partial invariance; it is a different scale in each group.",
                           "Report which items were freed, in which direction they differ, and what the latent mean difference is with and without the freeing.",
                           "The freed items are findings about the instrument and the setting. They belong in the discussion, not a footnote.",
                           "Alternative: the alignment method (Asparouhov and Muth&eacute;n, <em>Structural Equation Modeling</em> 2014, 21:495) for many groups (all Indian states) where sequential testing is impractical."]}],
              "right": [{"t": "panel", "color": "amber", "title": "When invariance really fails", "html":
                         "Sometimes the construct is different in the two groups: 'mobility' "
                         "for a woman in a Bihar village and in a Chennai apartment may not "
                         "be one thing. Then no amount of freeing rescues the comparison, "
                         "and the honest report is that the groups cannot be compared on "
                         "this scale, with the evidence. That is a result, and a more "
                         "useful one for the next study than a forced comparison."},
                        {"t": "hbox", "color": "green", "html": "Test invariance on the "
                         "pilot data if the pilot is large enough. Finding a non-invariant "
                         "item before the main survey means it can be rewritten."}]},
         ]},

        {"type": "content", "label": "Across Time", "title": "Invariance across waves: the same scale before and after",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Longitudinal invariance is tested the same "
                        "way, with waves as 'groups' in a single model where the same "
                        "respondents appear at each wave and each item's error is allowed "
                        "to correlate with itself across waves (the same person's "
                        "idiosyncratic response to item d2 persists). Without it, a change "
                        "in the latent mean between baseline and endline could be a change "
                        "in how the items are understood, which a programme that talks to "
                        "women about decision-making might well produce."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Response shift: the programme changes the respondent's frame of reference, so the same answer means something different. Invariance testing detects it as a scalar failure at endline.",
                           "Enumerator change between waves is confounded with time; note it.",
                           "With two waves and a control group, test invariance across waves within the control group first; if it holds there, a failure in the treatment group is itself evidence of response shift."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Why it matters for evaluations", "html":
                         "An empowerment programme that raises the summed score by 0.3 SD "
                         "may have raised the construct, or taught respondents what the "
                         "questions are asking, or both. The treatment-group scalar "
                         "failure at endline is the diagnostic, and the latent mean "
                         "difference under partial invariance is the corrected estimate. "
                         "Most evaluations report neither, and their effects on "
                         "self-reported attitudes are correspondingly hard to read."},
                        {"t": "hbox", "color": "green", "html": "Behavioural items (did you "
                         "go to the market alone last week?) are less prone to response "
                         "shift than attitudinal ones. Mix them."}]},
         ]},

        {"type": "content", "label": "Multigroup SEM", "title": "Multigroup structural models: does the effect differ by group?",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Once metric invariance holds, structural paths "
                        "can be compared across groups: is the effect of savings on "
                        "decision-making the same for women with and without their own "
                        "income? Fit the structural model in both groups at once, then "
                        "constrain the path equal and test the constraint. This is "
                        "moderation by a categorical variable (section 07), done with full "
                        "measurement models and a proper test."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Constrain one path at a time and test each; an omnibus test of all paths equal is rarely the question.",
                           "Report the path in each group with its CI, and the &Delta;&chi;&sup2; for the equality constraint.",
                           "Group sizes: each group needs to be large enough for its own model; 150 per group is a practical floor for a modest model with ordinal items.",
                           "In lavaan: <code>group = \"language\", group.equal = c(\"loadings\", \"intercepts\")</code>, then equality labels on the paths."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Many groups", "html":
                         "Twenty-eight states, or thirty districts, cannot be handled by "
                         "pairwise multigroup models. Options: multilevel SEM with the "
                         "group as a random level, the alignment method for invariance, "
                         "or collapsing to a few theoretically meaningful groups (north and "
                         "south; high and low female labour force participation). The last "
                         "is usually the right one and the grouping should be stated before "
                         "the data are seen."},
                        {"t": "hbox", "color": "green", "html": "Group differences in a "
                         "structural path are among the most useful things SEM can show a "
                         "programme, because they say for whom the mechanism works."}]},
         ]},

        {"type": "content", "label": "Invariance Syntax", "title": "Invariance testing in practice: the code and the report",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "lavaan with semTools", "html":
                         "<code>library(semTools)<br>"
                         "cfg &lt;- cfa(model, df, group = \"lang\", ordered = items)<br>"
                         "met &lt;- cfa(model, df, group = \"lang\", ordered = items,<br>"
                         "&nbsp;&nbsp;&nbsp;group.equal = \"loadings\")<br>"
                         "sca &lt;- cfa(model, df, group = \"lang\", ordered = items,<br>"
                         "&nbsp;&nbsp;&nbsp;group.equal = c(\"loadings\", \"thresholds\"))<br>"
                         "compareFit(cfg, met, sca)<br>"
                         "lavTestScore(sca)&nbsp;&nbsp;# which constraints to release<br>"
                         "# or, for the correct ordinal sequence:<br>"
                         "measEq.syntax(model, df, group = \"lang\", ordered = items,<br>"
                         "&nbsp;&nbsp;&nbsp;ID.cat = \"Wu.Estabrook.2016\", group.equal = ...)</code>"}],
              "right": [{"t": "body", "html": "Stata: <code>sem ..., group(lang) ginvariant(mcoef)</code> "
                        "and <code>estat ginvariant</code>. Mplus: <code>MODEL = CONFIGURAL "
                        "METRIC SCALAR</code> in one line. AMOS: the multigroup wizard. All "
                        "produce the same table; the judgement about partial invariance is "
                        "the analyst's."},
                        {"t": "bullets", "color": "amber", "sm": True, "items": [
                            "Report the table of nested models with &chi;&sup2;, df, CFI, RMSEA, the differences and the criteria used.",
                            "Report the freed items and the reasoning.",
                            "Report the latent mean difference (or the group path difference) under the final model, with its interval.",
                            "Say which comparisons the achieved level licenses and which it does not."]}]},
         ]},

        # ===================== SECTION 09: PLS-SEM =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "PLS-SEM"},

        {"type": "content", "label": "What It Is", "title": "PLS-SEM: composites, regressions, and a different question",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Partial least squares path modelling (Wold, "
                        "1982; Lohm&ouml;ller, 1989) builds each construct as a weighted "
                        "composite of its indicators, with weights chosen iteratively to "
                        "maximise the explained variance of the endogenous composites, then "
                        "estimates the structural paths by ordinary regression among the "
                        "composites. There is no common factor, no separation of measurement "
                        "error, and no overall fit function to test. What there is: a "
                        "prediction-oriented model that runs on small samples, handles "
                        "formative constructs natively, and converges when CB-SEM will not."},
                       {"t": "term", "word": "Composite",
                        "def": "A weighted sum of indicators, treated as the construct. "
                        "Unlike a common factor, it contains the indicators' error, and its "
                        "path coefficients are attenuated accordingly unless the consistent "
                        "PLS correction (PLSc) is applied."}],
              "right": [{"t": "bullets", "color": "cyan", "items": [
                  "Standard in marketing, information systems and management; the dominant method in South Asian business-school research, usually via SmartPLS.",
                  "Hair, Hult, Ringle and Sarstedt, <em>A Primer on PLS-SEM</em> (3rd ed., Sage, 2022) is the manual; Hair and colleagues, <em>European Business Review</em> 2019, 31:2, the reporting guide.",
                  "Its critics (R&ouml;nkk&ouml; and Evermann 2013; R&ouml;nkk&ouml;, McIntosh, Antonakis and Edwards, <em>Journal of Operations Management</em> 2016, 47&ndash;48:9) argue that most of its claimed advantages do not survive simulation and that it is often used because it makes weak models look supported.",
                  "Both sides are right about something. This section says what each is right about."]},
                        {"t": "hbox", "color": "amber", "html": "The honest statement of "
                         "purpose: PLS-SEM estimates a predictive model on composites. It "
                         "is not a cheaper way to do CB-SEM."}]},
         ]},

        {"type": "content", "label": "When", "title": "When PLS-SEM is the right tool, and when it is the convenient one",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["A defensible reason", "Why"],
                        "rows": [
                            ["The constructs are formative composites (an index of adoption barriers, a service-quality composite)", "CB-SEM handles formative constructs awkwardly; PLS is built for them"],
                            ["The goal is prediction of a target construct, evaluated out of sample", "PLS maximises explained variance and PLSpredict assesses it honestly"],
                            ["The model is complex relative to the sample and CB-SEM will not converge", "PLS always converges; the estimates are still to be read with the composite caveat"],
                            ["Exploratory theory building in a new domain", "No fit test to fail; the structure can be revised and reported as exploratory"],
                            ["Secondary data with single-item and archival measures", "Composites of one item are fine; factors of one item are not"]]}],
              "right": [{"t": "table",
                         "head": ["A convenient reason", "Why it does not hold"],
                         "rows": [
                             ["'The sample is small' (n = 120)", "Goodhue, Lewis and Thompson (<em>MIS Quarterly</em> 2012, 36:981): PLS has no more power than regression at small n; it just produces numbers"],
                             ["'The data are non-normal'", "Robust ML and WLSMV handle non-normality in CB-SEM; PLS's distribution-free property is about estimation, not inference"],
                             ["'PLS does not require a fit test'", "That is a cost, not a benefit; the model is not tested against the data"],
                             ["'The 10-times rule says 100 is enough'", "The rule is discredited; use the inverse-square-root method (Kock and Hadaya, <em>Information Systems Journal</em> 2018, 28:227) or a power analysis"],
                             ["'Everyone in my field uses it'", "True, and the field's replication record is the argument against"]]},
                        {"t": "hbox", "color": "amber", "html": "Choose the method for the "
                         "question, state the reason in the methods, and cite both the "
                         "advocates and the critics. Referees at good journals are now "
                         "from both camps."}]},
         ]},

        {"type": "content", "label": "Outer Model", "title": "Assessing the measurement (outer) model in PLS-SEM",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Construct type", "Criterion", "Threshold (Hair et al. 2019, 2022)", "Notes"],
              "rows": [
                  ["Reflective", "Indicator loadings", "&ge; 0.708 (so loading&sup2;, the indicator reliability, &ge; 0.5)", "Loadings 0.4&ndash;0.7 retained only if deletion does not raise CR or AVE above threshold"],
                  ["Reflective", "Internal consistency: Cronbach's &alpha;, &rho;<sub>A</sub> (Dijkstra-Henseler), composite reliability &rho;<sub>c</sub>", "0.70&ndash;0.95; &rho;<sub>A</sub> is the recommended one", "Above 0.95 signals redundant items"],
                  ["Reflective", "Convergent validity: AVE", "&ge; 0.50", "As in CB-SEM"],
                  ["Reflective", "Discriminant validity: HTMT", "&lt; 0.85 (conceptually distinct) or 0.90; bootstrap CI excludes 1", "Fornell-Larcker and cross-loadings are no longer sufficient"],
                  ["Formative", "Convergent validity: redundancy analysis", "Correlation &ge; 0.70 with a single global item measuring the same construct", "Requires the global item to have been asked; plan it in the questionnaire"],
                  ["Formative", "Collinearity: VIF of indicators", "&lt; 3 (ideal), &lt; 5 (tolerable)", "High VIF means indicators overlap; the weights become unstable"],
                  ["Formative", "Outer weights significance and relevance", "Weight significant by bootstrap; if not, retain if loading &ge; 0.5 and theory supports", "Deleting a formative indicator changes the construct"]]},
             {"t": "body", "cls": "sm", "html": "Every row is a decision that removes or "
              "keeps an item, and the recommended practice is to report the initial and "
              "final sets with reasons. A model whose outer assessment deleted a third of "
              "the items has changed its constructs and should say so."},
         ]},

        {"type": "content", "label": "Inner Model", "title": "Assessing the structural (inner) model and predictive power",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Criterion", "Threshold or reading", "Notes"],
              "rows": [
                  ["Collinearity among predictor composites (VIF)", "&lt; 3", "Above 5 the path coefficients are unreliable"],
                  ["Path coefficients", "Sign, size, bootstrap CI (10,000 subsamples, percentile)", "The estimate and interval, not stars"],
                  ["R&sup2; of endogenous constructs", "Hair's 0.75 / 0.50 / 0.25 as substantial / moderate / weak are from marketing and far too demanding for field data; report and interpret in context", "Adjusted R&sup2; when comparing models"],
                  ["f&sup2; effect size", "0.02 / 0.15 / 0.35 (Cohen)", "The change in R&sup2; when a predictor is removed"],
                  ["Predictive relevance", "PLSpredict (Shmueli et al., <em>European Journal of Marketing</em> 2019, 53:2322): out-of-sample RMSE of the PLS model versus a linear-model benchmark on the indicators", "Replaces the older blindfolding Q&sup2;; if PLS does not beat the benchmark on most indicators, the model has no predictive power"],
                  ["Model fit (approximate)", "SRMR &lt; 0.08 (Henseler et al. 2014); d<sub>ULS</sub>, d<sub>G</sub> bootstrap tests", "Contested; report SRMR and say it is approximate"],
                  ["Mediation, moderation", "As in CB-SEM: bootstrapped indirect effects; interaction terms with simple slopes", "Two-stage approach for interactions"]]},
             {"t": "body", "cls": "sm", "html": "PLSpredict is the important addition. A "
              "PLS-SEM paper that reports R&sup2; and path significance without out-of-sample "
              "prediction has not shown what the method is for. Most do not report it."},
         ]},

        {"type": "content", "label": "Worked PLS", "title": "A worked PLS-SEM assessment: mobile-money adoption among traders",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Construct", "Type", "Items", "&rho;<sub>A</sub>", "AVE", "HTMT max", "R&sup2;", "Notes"],
                        "rows": [
                            ["Performance expectancy", "Reflective", "4", "0.86", "0.64", "0.71", "&mdash;", "All loadings &gt; 0.75"],
                            ["Effort expectancy", "Reflective", "3", "0.81", "0.61", "0.71", "&mdash;", ""],
                            ["Social influence", "Reflective", "3", "0.78", "0.58", "0.55", "&mdash;", "One loading 0.66, retained"],
                            ["Adoption barriers", "Formative", "5", "&mdash;", "&mdash;", "&mdash;", "&mdash;", "VIF &lt; 2.4; redundancy r = 0.74; two weights not significant, loadings &gt; 0.5, retained"],
                            ["Intention to adopt", "Reflective", "3", "0.89", "0.73", "0.71", "0.42", ""],
                            ["Use (self-reported transactions)", "Single item", "1", "&mdash;", "&mdash;", "&mdash;", "0.19", "PLSpredict: PLS RMSE lower than LM benchmark on the item; Q&sup2;<sub>predict</sub> = 0.11"]]},
                       {"t": "body", "cls": "sm", "html": "Illustrative; n = 310 small "
                        "traders in two districts, UTAUT-type model (Venkatesh and "
                        "colleagues, <em>MIS Quarterly</em> 2012, 36:157). Paths: performance "
                        "expectancy &rarr; intention 0.31 [0.19, 0.42]; barriers &rarr; "
                        "intention &minus;0.24 [&minus;0.35, &minus;0.13]; intention &rarr; use "
                        "0.44 [0.33, 0.54]; 10,000 bootstrap subsamples."}],
              "right": [{"t": "panel", "color": "cyan", "title": "Reading it", "html":
                         "The measurement is adequate on every criterion, the barriers "
                         "composite is validly formative, and intention explains 42% of "
                         "its own variance and predicts reported use out of sample, "
                         "modestly. That is what a PLS-SEM study can show. It cannot show "
                         "that raising performance expectancy would raise adoption, that "
                         "the constructs are distinct common factors, or that the model "
                         "fits in the CB-SEM sense; the paper should not say any of those."},
                        {"t": "hbox", "color": "amber", "html": "R&sup2; = 0.42 is 'weak' by "
                         "Hair's marketing benchmarks and respectable for a field survey. "
                         "Say which yardstick you are using."}]},
         ]},

        {"type": "content", "label": "PLSc", "title": "Consistent PLS and the composite-versus-factor question",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Ordinary PLS path coefficients between "
                        "reflective constructs are biased toward zero, because the "
                        "composites carry measurement error, and loadings are biased upward. "
                        "Consistent PLS (Dijkstra and Henseler, <em>MIS Quarterly</em> 2015, "
                        "39:297) corrects both using &rho;<sub>A</sub>, so that PLSc estimates "
                        "for a common-factor model are consistent, and for a well-specified "
                        "model come close to CB-SEM's. It is one click in SmartPLS and one "
                        "argument in SEMinR and cSEM."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "If the constructs are argued to be common factors (attitudes, traits), use PLSc or use CB-SEM.",
                           "If they are argued to be composites (indices, formed constructs), ordinary PLS is the right estimator and the 'bias' is not a bias.",
                           "Say which. The composite-factor distinction is the actual disagreement between the PLS advocates and their critics, and a paper that names its constructs' status has answered most of the objection.",
                           "Report both estimates when the choice is contested; if they differ substantially, the measurement error is large and that is worth knowing."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Sample size for PLS-SEM", "html":
                         "The '10 times the largest number of arrows into a construct' rule "
                         "has no statistical basis and Hair and colleagues (2019) now "
                         "reject it. The inverse-square-root method gives the n needed to "
                         "detect a path of a given size at 80% power: about 155 for a "
                         "standardised path of 0.2, and about 620 for 0.1 (Kock and Hadaya "
                         "2018). A power analysis for the smallest path of interest is "
                         "the honest answer, as in CB-SEM."},
                        {"t": "hbox", "color": "green", "html": "PLS on 80 respondents does "
                         "produce estimates. So does regression. Neither has the power to "
                         "learn anything from them."}]},
         ]},

        {"type": "content", "label": "Software", "title": "PLS-SEM software: SmartPLS, SEMinR, cSEM",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Tool", "Cost", "Strengths", "Limits"],
              "rows": [
                  ["SmartPLS 4 (Ringle, Wende and Becker)", "Licence; free student and time-limited trial licences", "Menu-driven, complete: PLSc, bootstrapping, PLSpredict, HTMT with CIs, mediation, moderation, multigroup, necessary condition analysis, and a CB-SEM module since version 4", "Cost; point-and-click makes the analysis hard to reproduce unless the project file is shared"],
                  ["SEMinR (R)", "Free", "Readable syntax that mirrors the PLS-SEM vocabulary; bootstrapping, PLSc, PLSpredict, plots; the Hair et al. companion package", "R"],
                  ["cSEM (R)", "Free", "Composite and factor models in one framework; tests of overall fit; the methodologically most complete", "Less friendly documentation"],
                  ["plspm (R)", "Free", "The older standard; still works", "Fewer recent methods"],
                  ["ADANCO", "Licence", "Henseler's package; strong on composite models and fit tests", "Smaller user base"],
                  ["Python: <em>semopy</em> (CB), <em>plspm</em> port", "Free", "For pipelines", "PLS coverage is thinner than R's"]]},
             {"t": "body", "cls": "sm", "html": "For a student in a South Asian business "
              "school where SmartPLS is taught: learn it, and reproduce one analysis in "
              "SEMinR so that the work can be shared as code. For anyone else: SEMinR or "
              "cSEM."},
         ]},

        {"type": "content", "label": "PLS Reporting", "title": "Reporting a PLS-SEM study: the Hair et al. 2019 checklist, condensed",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Section", "Report"],
              "rows": [
                  ["Justification", "Why PLS-SEM rather than CB-SEM, in terms of the question and the constructs' status (composite or factor)"],
                  ["Model", "The diagram; each construct's measurement type; the theory behind each path"],
                  ["Data", "Sample, sampling, n, missing data and treatment, distributional summary, power analysis or inverse-square-root n"],
                  ["Settings", "Software and version; weighting scheme (path); PLSc or not; bootstrap subsamples (10,000), interval type; PLSpredict folds and repetitions; seed"],
                  ["Outer model", "The full table from the outer-model slide, initial and final item sets, deletions with reasons"],
                  ["Inner model", "VIF; paths with bootstrap CIs; R&sup2;, f&sup2;; PLSpredict results against the LM benchmark; SRMR"],
                  ["Additional analyses", "Mediation, moderation, multigroup (with MICOM invariance test for composites), as pre-specified"],
                  ["Limitations", "Cross-sectional, self-report, composite measurement, the causal status of the paths"],
                  ["Availability", "The data and the SmartPLS project file or R script"]]},
             {"t": "body", "cls": "sm", "html": "Papers that follow this list are rare and "
              "reviewable. Papers that report loadings, AVEs, R&sup2; and starred paths "
              "are the norm and are the reason the method has the reputation it has."},
         ]},

        {"type": "content", "label": "PLS Pitfalls", "title": "PLS-SEM pitfalls, in the order they appear in the typical thesis",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Pitfall", "Fix"],
              "rows": [
                  ["Chosen because CB-SEM would not fit", "Say so, and present the CB-SEM misfit as a finding about the model"],
                  ["Reflective constructs with ordinary PLS and no PLSc", "PLSc, or argue the composite status"],
                  ["Fornell-Larcker only for discriminant validity", "HTMT with bootstrap CI"],
                  ["R&sup2; interpreted with marketing benchmarks", "Contextual interpretation; compare with the literature's values"],
                  ["No out-of-sample prediction", "PLSpredict against the LM benchmark"],
                  ["Item deletion to pass thresholds", "Report initial and final sets; do not delete formative indicators"],
                  ["5,000 bootstrap samples with bias-corrected intervals reported as p &lt; 0.001 on everything", "10,000 percentile; report intervals"],
                  ["Multigroup comparison without MICOM", "Test measurement invariance of composites first (Henseler, Ringle and Sarstedt 2016)"],
                  ["Convenience sample of 150 students generalised to 'consumers in India'", "Describe the sample as what it is"],
                  ["Causal language throughout", "Section 10: 'is associated with', 'predicts'"]]},
         ]},

        {"type": "content", "label": "Both Methods", "title": "Running both: CB-SEM and PLS-SEM on the same data as a robustness check",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "When the constructs are reflective and the "
                        "sample allows it, fitting the model both ways is cheap and "
                        "informative. If the CB-SEM fits and the PLSc paths agree with it, "
                        "the result does not depend on the estimator. If CB-SEM rejects the "
                        "model while PLS reports strong paths, the paths are estimated on a "
                        "structure the data contradict, and the PLS result is the weaker "
                        "one. Papers that do this are rare; referees notice them."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Same items, same constructs, same paths; CB-SEM with MLR or WLSMV, PLS with PLSc.",
                           "Compare the path coefficients and intervals in one table; report the CB-SEM fit.",
                           "SmartPLS 4 runs both; in R, lavaan and SEMinR share the data frame."]}],
              "right": [{"t": "hbox", "color": "amber", "html": "The disagreement between the "
                        "two camps is partly a disagreement about what a construct is. The "
                        "analyst who can say which kind theirs are, and show the result "
                        "under both estimators, has stepped out of the argument."}]},
         ]},

        # ===================== SECTION 10: CAUSALITY AND COMMON METHOD BIAS =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Causality and Common Method Bias"},

        {"type": "content", "label": "The Claim", "title": "SEM does not establish causation, and never did",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The arrows in a path diagram are causal "
                        "hypotheses. Estimating them assumes the causal structure; it does "
                        "not test it. Bollen and Pearl ('Eight myths about causality and "
                        "structural equation models', in Morgan, ed., <em>Handbook of Causal "
                        "Analysis for Social Research</em>, Springer, 2013) list the "
                        "misreadings on both sides: that SEM proves causation (it cannot), "
                        "and that SEM is merely correlational (it is a language for stating "
                        "causal assumptions and deriving what they imply). The coefficients "
                        "are causal effects if, and only if, the assumptions hold."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Every path <em>X</em> &rarr; <em>Y</em> assumes no unmeasured common cause of <em>X</em> and <em>Y</em>, no reverse effect, and no selection on the outcome.",
                           "Randomising <em>X</em> secures the assumptions for <em>X</em>'s paths and for nothing downstream of it.",
                           "Good fit is compatible with the arrows reversed (section 04) and with an omitted confounder that the model absorbs into a path.",
                           "The language follows the design: 'effect' and 'causes' for randomised paths; 'is associated with', 'predicts', 'is consistent with' for the rest."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Antonakis's list", "html":
                         "Antonakis, Bendahan, Jacquart and Lalive ('On making causal "
                         "claims', <em>Leadership Quarterly</em> 2010, 21:1086) reviewed a "
                         "field's SEM papers and found the large majority made causal "
                         "claims their designs could not support, through omitted "
                         "variables, simultaneity, measurement error in predictors treated "
                         "as observed, selection, and common-method variance. The paper "
                         "is written for management research and applies without change "
                         "to South Asian development research using the same methods."},
                        {"t": "hbox", "color": "green", "html": "Draw the DAG with the "
                         "unmeasured variables in it. If an unmeasured node points into "
                         "both ends of a path, that path is not identified by the SEM."}]},
         ]},

        {"type": "content", "label": "Mediation Assumptions", "title": "Mediation's hidden assumption, and the sensitivity analysis that exposes it",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Imai, Keele and Tingley (<em>Psychological "
                        "Methods</em> 2010, 15:309) formalised what mediation needs: "
                        "sequential ignorability, meaning that the treatment is as good as "
                        "random given covariates, and that the mediator is as good as random "
                        "given treatment and covariates. The first is delivered by "
                        "randomisation; the second is delivered by nothing, because the "
                        "mediator was not assigned. Their sensitivity analysis asks how "
                        "strong an unmeasured confounder of the mediator-outcome path "
                        "would have to be (the correlation &rho; between the two error "
                        "terms) to reduce the indirect effect to zero."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "R's <em>mediation</em> package implements it; report the &rho; at which the effect vanishes and the R&sup2; it corresponds to.",
                           "An indirect effect that disappears at &rho; = 0.1 is fragile; at 0.4 it is not easily explained away.",
                           "Bullock, Green and Ha (<em>JPSP</em> 2010, 98:550) show how badly mediation estimates behave when the mediator is confounded, and argue for designs that manipulate the mediator directly.",
                           "Cross-sectional mediation adds a second problem (Maxwell and Cole 2007): the cross-sectional estimate of a longitudinal process can have the wrong sign."]}],
              "right": [{"t": "panel", "color": "amber", "title": "What a careful paper says", "html":
                         "'Membership was randomised; its total effect on decision-making "
                         "is causal. The indirect effect through savings assumes no "
                         "unmeasured confounder of savings and decision-making among "
                         "members. A sensitivity analysis indicates the indirect effect "
                         "would be eliminated by a confounder correlating with both error "
                         "terms at &rho; = 0.28. We interpret the mediation result as "
                         "consistent with a savings mechanism and not as a test of it.'"},
                        {"t": "hbox", "color": "green", "html": "Four sentences. They "
                         "distinguish a paper that understands its method from one that "
                         "runs it."}]},
         ]},

        {"type": "content", "label": "CMB", "title": "Common method bias: when the instrument makes the correlations",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Every construct in the model measured from one "
                        "respondent, in one sitting, on the same response format, shares "
                        "variance that has nothing to do with the constructs: the "
                        "respondent's mood, acquiescence, social desirability, the desire to "
                        "be consistent, the enumerator's manner. Podsakoff, MacKenzie, Lee "
                        "and Podsakoff (<em>Journal of Applied Psychology</em> 2003, 88:879) "
                        "catalogued the sources and the remedies; their 2012 review "
                        "(<em>Annual Review of Psychology</em> 63:539) updated them. The "
                        "bias inflates correlations among self-reported constructs and "
                        "therefore every path between them."},
                       {"t": "term", "word": "Common method variance",
                        "def": "Variance attributable to the measurement method rather "
                        "than to the constructs the measures represent. It is present in "
                        "every single-source, single-occasion survey; the question is how "
                        "much."}],
              "right": [{"t": "bullets", "color": "amber", "items": [
                  "<strong>Procedural remedies</strong>, at design: different sources for predictor and outcome (the woman's report and the husband's; self-report and an administrative record); temporal separation; different response formats; behavioural rather than attitudinal outcomes; assurance of anonymity.",
                  "<strong>Statistical remedies</strong>, after: a marker variable theoretically unrelated to the constructs (Lindell and Whitney 2001; the CFA marker technique of Williams, Hartman and Cavazotte, <em>Organizational Research Methods</em> 2010, 13:477); an unmeasured latent method factor with equal loadings on every item.",
                  "<strong>Not a remedy</strong>: Harman's single-factor test (one unrotated factor explaining less than 50%). It has almost no power and detects nothing; its presence in a paper signals that the authors looked for the cheapest possible check."]},
                        {"t": "hbox", "color": "red", "html": "A programme's effect on "
                         "self-reported empowerment, measured by the programme's own "
                         "enumerators, from the participant, with the mediator on the same "
                         "page, has every source of method variance at once."}]},
         ]},

        {"type": "content", "label": "CMB in Practice", "title": "A method factor in the model: how to do it and what it shows",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Model", "&chi;&sup2; (df)", "CFI", "Method variance share", "Key path (savings &rarr; decide)", "Reading"],
                        "rows": [
                            ["Substantive CFA only", "112.4 (41)", "0.96", "&mdash;", "0.31 [0.19, 0.42]", "Baseline"],
                            ["Plus unmeasured latent method factor (equal loadings)", "104.1 (40)", "0.97", "8%", "0.27 [0.15, 0.39]", "Some method variance; path attenuated a little"],
                            ["Plus CFA marker (attitude to cricket, 3 items)", "128.6 (60)", "0.96", "5%", "0.28 [0.16, 0.40]", "Consistent with the ULMC"],
                            ["Outcome from a different source (husband's report of who decides)", "n/a", "n/a", "n/a", "0.19 [0.06, 0.32]", "The procedural check: smaller, still present"]]},
                       {"t": "body", "cls": "sm", "html": "Illustrative. The three statistical "
                        "approaches agree that method variance is present and modest and "
                        "that the path survives it. The different-source estimate is the "
                        "most convincing and the smallest, which is the usual pattern and "
                        "the reason procedural remedies beat statistical ones."}],
              "right": [{"t": "panel", "color": "cyan", "title": "Reporting", "html":
                         "State the procedural steps taken at design and the statistical "
                         "check run after, with the method variance share and the key "
                         "paths before and after. If no procedural step was possible, say "
                         "so and treat the paths among self-reported constructs as upper "
                         "bounds. A marker variable has to be planned into the "
                         "questionnaire: three items on something the constructs cannot "
                         "plausibly relate to, on the same response scale."},
                        {"t": "hbox", "color": "amber", "html": "The ULMC with equal loadings "
                         "is an approximation; with free loadings it is not identified. "
                         "Report which was used."}]},
         ]},

        {"type": "content", "label": "Endogeneity", "title": "Selection, reverse causality and instruments in SEM",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Women who join a self-help group differ from "
                        "those who do not in ways the model does not measure, and those ways "
                        "affect decision-making. Membership is endogenous, and its path in "
                        "an observational SEM is biased by whatever drives both. This is "
                        "the same problem as in any regression, and SEM offers the same "
                        "remedies: an instrument (a variable that affects membership and "
                        "affects the outcome only through it), a design (randomisation, a "
                        "discontinuity), or an honest limitation."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "An instrument enters the SEM as an exogenous variable with a path into membership and no path into the outcome; the disturbances of membership and outcome are allowed to correlate. This is 2SLS inside a latent model, and its assumptions are 2SLS's.",
                           "A weak or invalid instrument (distance to the nearest group, a common choice, affects many things) makes it worse, not better.",
                           "Impact Evaluation 101 covers the designs. SEM adds latent outcomes and mediation to them; it does not replace them."]}],
              "right": [{"t": "panel", "color": "amber", "title": "The typical South Asian SEM paper", "html":
                         "A cross-sectional survey, all constructs self-reported, a "
                         "convenience or purposive sample, a model with six constructs and "
                         "twelve paths, all significant, fit indices at threshold, and a "
                         "conclusion that construct A 'significantly impacts' construct F. "
                         "Every problem in this section is present and none is mentioned. "
                         "The same data, analysed the same way and reported with sections "
                         "10 and 11's caveats, would be a competent descriptive study. The "
                         "difference is only in what is claimed."},
                        {"t": "hbox", "color": "green", "html": "Write the limitations "
                         "paragraph before the results. It disciplines the verbs in the "
                         "results."}]},
         ]},

        {"type": "content", "label": "DAGs", "title": "Drawing the causal diagram before the path diagram",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A directed acyclic graph is a path diagram "
                        "with the unmeasured variables drawn in and no estimation implied. "
                        "Drawing one for the study, including the things you cannot "
                        "measure (household bargaining power, the husband's attitudes, the "
                        "enumerator's effect), shows which paths are identified by "
                        "adjustment, which need a design, and which are hopeless. Pearl's "
                        "back-door criterion gives the rule: a path <em>X</em> &rarr; <em>Y</em> "
                        "is identified if every back-door path from <em>X</em> to <em>Y</em> "
                        "is blocked by measured covariates."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "DAGitty (free, browser) draws the graph and lists the adjustment sets and the testable implications.",
                           "A collider (a variable caused by both <em>X</em> and <em>Y</em>) must not be conditioned on; conditioning on it creates a spurious association. Selecting the sample on the outcome, or controlling for a post-treatment variable, does this routinely.",
                           "The DAG is the pre-registration document that a path diagram alone is not."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Post-treatment bias, the common case", "html":
                         "Controlling for savings when estimating membership's total "
                         "effect on decision-making blocks the very path the programme "
                         "works through and, if savings is confounded with the outcome, "
                         "introduces bias. The mediation model does this deliberately and "
                         "reports the direct effect as one of its outputs; a 'control for "
                         "savings' in a regression does it by accident and reports the "
                         "direct effect as the total. The DAG makes the difference visible."},
                        {"t": "hbox", "color": "green", "html": "The SEM estimates what the "
                         "DAG says it can. The DAG is the argument; the SEM is the "
                         "arithmetic."}]},
         ]},

        {"type": "content", "label": "Language", "title": "Scaling the verbs to the design: a table",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Design", "Path", "Verb", "Example sentence"],
              "rows": [
                  ["Randomised <em>X</em>", "<em>X</em> &rarr; latent <em>Y</em>", "raises, reduces, has an effect of", "'Membership raises the latent decision-making score by 0.21 SD (95% CI 0.11 to 0.30).'"],
                  ["Randomised <em>X</em>, observed <em>M</em>", "<em>X</em> &rarr; <em>M</em> &rarr; <em>Y</em>", "is consistent with mediation through; the indirect association", "'The pattern is consistent with mediation through savings; the mediator was not assigned.'"],
                  ["Observational, well-controlled, DAG-justified", "<em>X</em> &rarr; <em>Y</em>", "is associated with; predicts; under the assumptions in Figure 1, the estimated effect is", "'Under the adjustment set in Figure 1, savings behaviour is associated with a 0.31 SD higher score.'"],
                  ["Observational, cross-sectional, self-report", "Any", "is associated with; correlates with", "'Performance expectancy is associated with adoption intention (&beta; = 0.31).'"],
                  ["Panel with RI-CLPM", "Cross-lagged", "precedes; within-person increases in <em>X</em> are followed by", "'Within-person increases in trust are followed by increases in participation the next year.'"],
                  ["Any", "Good fit", "the data are consistent with the model; the model was not rejected", "Never 'the model is confirmed' or 'proven'"]]},
             {"t": "body", "cls": "sm", "html": "The table is not pedantry. A ministry "
              "reading 'social influence significantly impacts adoption' will fund a "
              "social-influence campaign. The verb is the policy claim."},
         ]},

        {"type": "content", "label": "Robustness", "title": "Robustness checks that a careful SEM paper includes",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Check", "What it tests", "Report"],
              "rows": [
                  ["Alternative estimator (ML vs WLSMV; PLS vs PLSc)", "Sensitivity to distributional treatment", "Paths and fit under each"],
                  ["Equivalent model", "Whether the data can distinguish your story from a rival", "Name one, show the fit is the same, argue the choice"],
                  ["Item deletion reversed", "Whether the results depend on the items dropped", "Paths with the full item set"],
                  ["Method factor", "Common method variance", "Paths with and without"],
                  ["Mediation sensitivity", "Unmeasured mediator-outcome confounding", "&rho; at which the indirect effect vanishes"],
                  ["Cross-validation", "Modifications capitalising on chance", "Fit on the holdout half"],
                  ["Subsample stability", "Enumerator, district, language effects", "Multigroup or dummies; anything that changes the story"],
                  ["Covariate sensitivity", "Dependence on the adjustment set", "Paths with the minimal and the full set"],
                  ["Missing-data assumption", "MAR", "FIML vs multiple imputation; a pattern-mixture bound"]]},
             {"t": "body", "cls": "sm", "html": "Not every paper needs all nine; every paper "
              "needs the ones its design makes relevant, and the appendix is where they "
              "live."},
         ]},

        # ===================== SECTION 11: SOFTWARE, REPORTING AND PRACTICE =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Software, Reporting and Practice"},

        {"type": "content", "label": "Software", "title": "Software for CB-SEM: what each does and what it costs",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Tool", "Cost", "Strengths", "Limits"],
              "rows": [
                  ["lavaan (R; Rosseel, <em>J Stat Softw</em> 2012, 48(2))", "Free", "The reference implementation: CFA, SEM, multigroup, ordinal (WLSMV), FIML, MLR, bootstrap, growth, multilevel; readable syntax; <em>semTools</em> for invariance and reliability, <em>semPlot</em> for diagrams", "Latent interactions need workarounds; some ordinal-plus-missing combinations are awkward"],
                  ["Mplus (Muth&eacute;n and Muth&eacute;n)", "Licence", "The most complete: latent interactions (XWITH), mixtures, Bayesian, complex survey designs, alignment", "Cost; syntax; closed"],
                  ["Stata <code>sem</code> / <code>gsem</code>", "Licence", "Clean integration with survey data (<code>svy</code>), clustering, weights; <code>gsem</code> for ordinal and multilevel; <code>estat</code> commands for fit, invariance, effects", "No WLSMV; ordinal models via gsem are slower and lack the usual fit indices"],
                  ["IBM SPSS AMOS", "Licence (SPSS add-on)", "Drawing interface; bootstrap; the tool most Indian universities teach", "No robust ML, no ordinal estimator, no FIML with ordinal; encourages modification-index fishing"],
                  ["JASP and jamovi (SEMLj)", "Free", "lavaan with menus; good for learning and for departments without R", "Fewer options exposed"],
                  ["semopy (Python)", "Free", "lavaan-style syntax in Python; pipelines", "Younger; fewer estimators"],
                  ["OpenMx, blavaan (R)", "Free", "Flexible matrix specification; Bayesian SEM", "Specialist"]]},
             {"t": "body", "cls": "sm", "html": "For a South Asian researcher: lavaan, "
              "learned through JASP if menus help at first. AMOS's limitations (no robust "
              "or ordinal estimation) are real limitations for Likert data, and a thesis "
              "committee that requires AMOS is requiring a weaker analysis."},
         ]},

        {"type": "content", "label": "Reporting Standards", "title": "Reporting: what the standards ask for",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Element", "Content", "Source"],
              "rows": [
                  ["Theory and model", "The diagram, every hypothesised path, the omitted paths, the constructs' definitions and status", "Kline 2023, ch. 18; APA JARS-Quant SEM table (Appelbaum et al., <em>American Psychologist</em> 2018, 73:3)"],
                  ["Sample and data", "n, design, missingness, screening, distributions, clustering, weights", "Jackson, Gillaspy and Purc-Stephenson, <em>Psychological Methods</em> 2009, 14:6"],
                  ["Measurement", "Items (in an appendix, in every language), loadings with SEs, reliability (&omega;), AVE, discriminant validity, invariance where groups are compared", "Hoyle and Isherwood, <em>Archives of Scientific Psychology</em> 2013, 1:14"],
                  ["Estimation", "Estimator and why; missing-data method; software and version; identification; convergence; improper solutions", "As above"],
                  ["Fit", "&chi;&sup2; (df, p, scaling), RMSEA with CI, CFI, TLI, SRMR; residuals; nested comparisons; every modification with reason", "Section 06"],
                  ["Structural results", "Unstandardised and standardised paths with SEs and CIs; indirect effects with bootstrap CIs; R&sup2;", "Section 07"],
                  ["Causal status", "The design, the assumptions, the equivalent models, the sensitivity analyses, the verbs", "Section 10"],
                  ["Reproducibility", "Data (or synthetic data with the covariance matrix), the syntax, the correlation matrix with SDs in an appendix", "A covariance matrix and n is enough to refit any CB-SEM"]]},
             {"t": "body", "cls": "sm", "html": "The last row is the one that costs nothing "
              "and is almost never done. A correlation matrix with standard deviations "
              "and n lets any reader refit the model, and its absence is the reason most "
              "published SEMs cannot be checked."},
         ]},

        {"type": "content", "label": "The Paper", "title": "An SEM paper, section by section",
         "blocks": [
             {"t": "flow", "steps": [
                 "INTRODUCTION: the question, the constructs, the model as a figure, the hypotheses as paths",
                 "METHODS: sample, instrument and translation, measurement model, estimation, analysis plan, registration",
                 "MEASUREMENT RESULTS: CFA fit, loadings, reliability, validity, invariance",
                 "STRUCTURAL RESULTS: fit and comparison with rivals, paths, indirect effects, effect sizes",
                 "ROBUSTNESS: the checks the design made relevant",
                 "DISCUSSION: what the paths mean, in the verbs the design allows; the equivalent model; limitations with direction of bias; implications"]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Academic Writing 101 in this series covers the "
                        "prose. The SEM-specific rule is that the measurement results come "
                        "before the structural results and are read as a condition on "
                        "them: a reader who does not trust the constructs has no reason to "
                        "read the paths."}],
              "right": [{"t": "hbox", "color": "amber", "html": "Two figures: the hypothesised "
                        "model with paths labelled, and the estimated model with "
                        "standardised coefficients and their significance. Two tables: "
                        "the measurement table and the structural table. Everything else "
                        "goes to the appendix."}]},
         ]},

        {"type": "content", "label": "Pre-registration", "title": "Pre-registering an SEM: the template",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Item", "What to write"],
              "rows": [
                  ["Constructs", "Name, definition, reflective or formative, the items (numbered) that measure each"],
                  ["Model", "The diagram; the list of paths with predicted signs; the omitted paths"],
                  ["Hypotheses", "Each as a path or a comparison, with the effect size that would matter"],
                  ["Sample", "Planned n and the power analysis or simulation behind it; the sampling design"],
                  ["Estimation", "Estimator; missing-data treatment; clustering; software"],
                  ["Fit criteria", "The indices and the thresholds that will be used, chosen now"],
                  ["Modification policy", "'No post hoc modifications' or the specific class allowed (e.g. correlated errors between items with shared stems), with the rule for reporting"],
                  ["Invariance", "The groups to be compared and the level required before comparison"],
                  ["Mediation and moderation", "Which effects, which bootstrap, which sensitivity analysis"],
                  ["Exploratory", "What will be reported as exploratory if run"]]},
             {"t": "body", "cls": "sm", "html": "Registered on OSF as a PDF before the data "
              "are cleaned. It turns every decision in sections 04 to 07 from something a "
              "referee suspects into something a referee can check, and it is the single "
              "step that most separates a credible SEM from the typical one."},
         ]},

        {"type": "content", "label": "Worked Study", "title": "A worked study outline: validating and using an empowerment scale in an evaluation",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Step", "Decision", "Section"],
                        "rows": [
                            ["Question", "Does an SHG programme raise women's decision-making, and does it work through savings?", "01"],
                            ["Instrument", "12 items adapted from a published scale; translated into Hindi and Bangla with cognitive interviews; pilot EFA on n = 180 gives three factors", "02, 03"],
                            ["Design", "Village-level randomisation; baseline and endline; n = 640 women", "04, 10"],
                            ["Registration", "Diagram, hypotheses, estimator, fit criteria, invariance plan on OSF before endline", "11"],
                            ["Measurement", "CFA per wave and language; WLSMV; d5 dropped with reason; partial scalar invariance across languages (two thresholds freed) and waves (one)", "02, 05, 08"],
                            ["Structural", "Treatment &rarr; savings &rarr; decide with covariates; village-clustered; 5,000 bootstrap; CFA-then-structural comparison", "06, 07"],
                            ["Finding (illustrative)", "Latent treatment effect on decide 0.21 SD [0.11, 0.30]; indirect through savings 0.12 [0.07, 0.18]; sensitivity &rho; = 0.28", "07, 10"],
                            ["Robustness", "Summed-score effect; ML vs WLSMV; method factor; different-source outcome for a subsample; equivalent model stated", "10"],
                            ["Report", "Measurement table, invariance table, structural table, two figures, correlation matrix and syntax in the appendix", "11"]]}],
              "right": [{"t": "body", "cls": "sm", "html": "Numbers illustrative; the structure "
                        "is the point. Each row names the section that governs it, and "
                        "the whole is what a competent SEM contribution to an evaluation "
                        "looks like: the scale validated, the effect estimated on the "
                        "latent outcome, the mechanism explored with its assumptions "
                        "stated."},
                        {"t": "hbox", "color": "amber", "html": "The randomised effect is the "
                         "headline. The mediation is the second paragraph, in the "
                         "conditional mood."}]},
         ]},

        {"type": "content", "label": "Pitfalls", "title": "The dozen errors that get SEM papers rejected",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Error", "Section", "Fix in one line"],
              "rows": [
                  ["Formative construct modelled as reflective", "02", "Decide the direction from theory; PLS or MIMIC for formative"],
                  ["ML on binary or skewed Likert items", "05", "WLSMV or MLR"],
                  ["Listwise deletion", "05", "FIML or multiple imputation"],
                  ["Fit reached by modification indices", "06", "Report the original model; justify each change; cross-validate"],
                  ["&chi;&sup2;/df and GFI as fit evidence", "06", "&chi;&sup2; with df and p, RMSEA with CI, CFI, TLI, SRMR"],
                  ["Saturated structural model reported as tested", "07", "Omit theoretically absent paths; compare with rivals"],
                  ["Mediation by Baron-Kenny steps, or 'full mediation' claimed", "07", "Bootstrap the indirect effect; report intervals"],
                  ["Groups or languages compared without invariance", "08", "Configural, metric, scalar; partial if needed"],
                  ["PLS-SEM chosen for small n or non-normality", "09", "State a defensible reason or use CB-SEM"],
                  ["Causal verbs from cross-sectional self-report", "10", "Associated with; predicts"],
                  ["No common-method check in a single-source survey", "10", "Procedural remedy at design; ULMC or marker after"],
                  ["No correlation matrix, syntax or data", "11", "Appendix and repository"]]},
         ]},

        {"type": "content", "label": "Checklist", "title": "Before you submit: the SEM checklist",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Measurement", "Done"],
                        "rows": [
                            ["Each construct defined and its reflective or formative status stated", ""],
                            ["Items listed, with translations, in an appendix", ""],
                            ["CFA fit reported in full; residuals inspected", ""],
                            ["Loadings with SEs; &omega;; AVE; HTMT or equivalent", ""],
                            ["Estimator matched to the items; missing data handled and reported", ""],
                            ["Invariance tested for every group and wave comparison", ""],
                            ["Item deletions and modifications listed with reasons", ""]]}],
              "right": [{"t": "table",
                         "head": ["Structure and claims", "Done"],
                         "rows": [
                             ["Structural model compared with the CFA and with at least one rival", ""],
                             ["Paths with SEs and CIs, unstandardised and standardised", ""],
                             ["Indirect effects bootstrapped; sensitivity analysis where the mediator was not assigned", ""],
                             ["Clustering and weights handled", ""],
                             ["Common method bias addressed procedurally or statistically", ""],
                             ["An equivalent model named and argued against", ""],
                             ["Verbs scaled to the design", ""],
                             ["Correlation matrix, SDs, n and syntax available", ""]]},
                        {"t": "hbox", "color": "cyan", "html": "Fifteen lines. Invariance "
                         "and the equivalent model are the two most often missing."}]},
         ]},

        {"type": "content", "label": "Reading List", "title": "Where to go next",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Resource", "What it covers", "Notes"],
              "rows": [
                  ["Kline, <em>Principles and Practice of Structural Equation Modeling</em> (5th ed., Guilford, 2023)", "Everything in sections 01 to 08 and 10, with the arguments", "The first book to buy"],
                  ["Rosseel, lavaan tutorial (lavaan.ugent.be) and <em>J Stat Softw</em> 2012, 48(2)", "The software, with worked examples", "Free"],
                  ["Brown, <em>Confirmatory Factor Analysis for Applied Research</em> (2nd ed., Guilford, 2015)", "CFA in depth: ordinal items, invariance, higher-order models", "For sections 02, 03, 08"],
                  ["Bollen, <em>Structural Equations with Latent Variables</em> (Wiley, 1989)", "The theory", "Reference"],
                  ["Hayes, <em>Introduction to Mediation, Moderation, and Conditional Process Analysis</em> (3rd ed., Guilford, 2022)", "Section 07 with observed variables", "PROCESS"],
                  ["Enders, <em>Applied Missing Data Analysis</em> (Guilford, 2010; 2nd ed. 2022)", "Missing data", "Section 05"],
                  ["Putnick and Bornstein, <em>Developmental Review</em> 2016, 41:71", "Measurement invariance: a review and guide", "Section 08"],
                  ["Hair, Hult, Ringle and Sarstedt, <em>A Primer on PLS-SEM</em> (3rd ed., Sage, 2022); R&ouml;nkk&ouml; et al. 2016", "PLS-SEM, from both sides", "Section 09"],
                  ["Bollen and Pearl 2013; Antonakis et al. 2010; Imai, Keele and Tingley 2010", "Causality, claims, and mediation sensitivity", "Section 10"],
                  ["Podsakoff et al. 2003, 2012", "Common method bias", "Section 10"],
                  ["ImpactMojo: Survey Design 101, Item Response Theory 101, Impact Evaluation 101, Econometrics 101", "The instrument, the items, the designs, the regressions", "impactmojo.in/101-courses/"]]},
         ]},

        {"type": "content", "label": "Summary", "title": "What to remember",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "A latent variable is shared variance among items. Whether it is empowerment is a validity argument the CFA does not make.",
                  "Decide reflective or formative from theory. It changes everything downstream.",
                  "Match the estimator to the items: ordinal items, WLSMV; skewed continuous, MLR; missing data, FIML or imputation.",
                  "Report the &chi;&sup2; and the residuals; read the indices with judgement; modify only with a reason stated in advance.",
                  "Test the structural model against the CFA and against a rival. A saturated structural model tests nothing."]}],
              "right": [{"t": "bullets", "color": "green", "items": [
                  "Bootstrap the indirect effect; say what its identification assumes; run the sensitivity analysis.",
                  "No group, language or wave comparison without invariance testing, and partial invariance reported honestly.",
                  "PLS-SEM for composites and prediction, with PLSc and PLSpredict; not as an escape from fit.",
                  "Fit does not choose between equivalent models; design and theory do. Name one.",
                  "Scale the verbs to the design, address method bias, and put the correlation matrix and syntax where a reader can find them."]},
                        {"t": "hbox", "color": "amber", "html": "The method is sound. Most of "
                         "its use is not. Be in the first group."}]},
         ]},

        # ===================== S100 END =====================
        {"type": "end",
         "eyebrow": "Structural Equation Modelling 101 &middot; Complete",
         "headline": "Now go measure<br>something that can fail.",
         "byline": "A model that cannot be rejected has not been tested. Specify it first, "
                   "validate the measurement, compare it with a rival, and say what the arrows "
                   "assume. Explore the rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
