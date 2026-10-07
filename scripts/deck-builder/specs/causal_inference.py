# -*- coding: utf-8 -*-
"""
Causal Inference 101 | ImpactMojo 101 Series (native deck spec)
The logic of causal claims for development practitioners in South Asia: potential
outcomes, selection bias, causal diagrams, randomisation, natural experiments,
difference-in-differences, regression discontinuity, instrumental variables,
matching, synthetic control, external validity, and reading a causal claim.
Build: python3 scripts/deck-builder/build.py causal_inference

Every study cited here was opened (Crossref, OpenAlex, PubMed, RePEc, NBER or the
publisher) before it was written down. Teaching numbers that are not from a
study are labelled Illustrative on the slide.
"""


_DAG_N = [0]


def dag(nodes, edges, w=520, h=200, note=None):
    """Small causal diagram as inline SVG. nodes: {key: (label, x, y, colour)};
    edges: [(from, to, colour, dashed)]. Text uses currentColor so it follows the theme."""
    _DAG_N[0] += 1
    mid = f"ci_arr{_DAG_N[0]}"
    parts = ['<div style="display:flex;justify-content:center;padding:4px 0">',
             f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
             f'style="width:100%;max-width:{w + 40}px;height:auto" role="img" '
             f'aria-label="Causal diagram: {note or "nodes joined by arrows"}">',
             f'<defs><marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
             'markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" '
             'fill="#64748B"/></marker></defs>']
    for a, b, col, dashed in edges:
        x1, y1 = nodes[a][1], nodes[a][2]
        x2, y2 = nodes[b][1], nodes[b][2]
        dx, dy = x2 - x1, y2 - y1
        d = (dx * dx + dy * dy) ** 0.5 or 1
        sx, sy = x1 + dx / d * 46, y1 + dy / d * 22
        ex, ey = x2 - dx / d * 50, y2 - dy / d * 24
        dash = ' stroke-dasharray="5,4"' if dashed else ''
        parts.append(f'<line x1="{sx:.0f}" y1="{sy:.0f}" x2="{ex:.0f}" y2="{ey:.0f}" '
                     f'stroke="{col}" stroke-width="2.4"{dash} marker-end="url(#{mid})"/>')
    for key, (label, x, y, col) in nodes.items():
        parts.append(f'<rect x="{x - 58}" y="{y - 20}" width="116" height="40" rx="8" '
                     f'fill="{col}" fill-opacity="0.14" stroke="{col}" stroke-width="2"/>')
        parts.append(f'<text x="{x}" y="{y + 5}" text-anchor="middle" font-size="13" '
                     f'font-weight="700" fill="currentColor">{label}</text>')
    parts.append('</svg></div>')
    return {"t": "raw", "html": "".join(parts)}


C, G, A, I, R = "#0EA5E9", "#10B981", "#F59E0B", "#6366F1", "#EF4444"

DECK = {
    "slug": "causal-inference",
    "title": "Causal Inference 101",
    "description": ("Causal Inference 101: a free foundational course for development practitioners "
                    "in South Asia on the logic of causal claims. Potential outcomes and the "
                    "counterfactual, selection bias, causal diagrams, randomisation, natural "
                    "experiments, difference-in-differences, regression discontinuity, instrumental "
                    "variables, matching, synthetic control, external validity, and how to read a "
                    "causal claim in a policy report. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Causal<br>Inference<br>101",
         "sub": "What would have happened otherwise: the logic of causal claims for development "
                "practitioners, from the counterfactual to randomisation, difference-in-differences, "
                "regression discontinuity and instrumental variables",
         "tags": ["Evaluation Methods", "South Asia Focus", "100 Slides", "Free Forever"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What we cover",
         "items": [
             {"name": "Why causal questions are hard"},
             {"name": "Potential outcomes and the counterfactual"},
             {"name": "Selection bias and confounding"},
             {"name": "Causal diagrams"},
             {"name": "Randomisation"},
             {"name": "Natural experiments and difference-in-differences"},
             {"name": "Regression discontinuity"},
             {"name": "Instrumental variables"},
             {"name": "Matching and synthetic control"},
             {"name": "External validity and heterogeneity"},
             {"name": "Reading a causal claim in practice"},
             {"name": "Summary and next steps"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "Why causal questions are hard"},

        {"type": "content", "label": "Three Kinds of Question", "title": "Describe, predict, or explain what a change would do",
         "compact": True,
         "blocks": [
             {"t": "body", "html": "Most questions a programme team asks fall into one of three kinds, and "
              "each needs a different kind of evidence. A <strong>descriptive</strong> question asks what "
              "is the case. A <strong>predictive</strong> question asks what we expect to observe next. A "
              "<strong>causal</strong> question asks what would change if we, or someone, did something "
              "differently. Only the third tells a ministry whether to spend money, and it is the hardest "
              "of the three, because the answer compares the world we see with a world we never see."},
             {"t": "table",
              "head": ["Kind", "Example question", "What answers it"],
              "rows": [
                  ["Descriptive", "What share of births in Bihar happen in a health facility?", "A good sample survey such as NFHS, with weights"],
                  ["Predictive", "Which blocks are likely to report the most malnourished children next year?", "A model that fits past data well; it need not explain anything"],
                  ["Causal", "Did a cash incentive to mothers raise facility births, and by how much?", "A comparison that stands in for the births that would have happened without the incentive"],
                  ["Causal, at scale", "Would the same incentive work if every state ran it through its own health department?", "Causal evidence plus an argument about context and implementation"]]},
             {"t": "hbox", "color": "cyan", "html": "This course is about the third and fourth rows. The "
              "first two are covered in Data Literacy 101 and Survey Design 101."},
         ]},

        {"type": "content", "label": "Association", "title": "Two things that move together may have no effect on each other",
         "blocks": [
             {"t": "body", "html": "An association is a pattern in data: where one thing is higher, another "
              "tends to be higher or lower too. A causal effect is a claim about what happens to one thing when "
              "another is changed. The two separate whenever something else drives both, or when the arrow "
              "runs the other way. Development data are full of both situations because programmes are placed "
              "on purpose and people choose whether to join them."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "amber", "title": "A common cause (Illustrative)", "html":
                        "Villages with a bank branch have higher household incomes. A planner concludes that "
                        "branches raise incomes. Banks, though, open branches where incomes, roads and "
                        "markets already exist. The same prosperity that attracted the branch would show up "
                        "in incomes even if the branch had never opened."}],
              "right": [{"t": "panel", "color": "red", "title": "Reverse causation (Illustrative)", "html":
                         "Districts that spend more on tuberculosis treatment report more tuberculosis cases. "
                         "Spending does not cause the disease. High caseloads draw the budget, and better "
                         "funded programmes also find and notify more cases, so the reported numbers rise "
                         "with the spending that was meant to bring them down."}]},
         ]},

        {"type": "content", "label": "Why It Matters", "title": "A wrong causal answer costs money and lives",
         "blocks": [
             {"t": "body", "html": "Governments in South Asia run some of the largest social programmes in "
              "the world, and each one is a bet about cause and effect. A school feeding scheme assumes "
              "meals raise attendance and learning. A conditional cash transfer for institutional delivery "
              "assumes the cash moves births into facilities and that facility births save newborns. If the "
              "first link holds and the second does not, the scheme spends its budget and the mortality it "
              "was built to reduce stays where it was."},
             {"t": "term", "word": "Causal effect",
              "def": "The difference between the outcome a unit (a person, a household, a village) has "
              "with a treatment and the outcome the same unit would have had, at the same time, without "
              "it. Everything in this course is a way of estimating that difference when half of it can "
              "never be observed."},
             {"t": "hbox", "color": "amber", "html": "Causal evidence will not tell you what to value. It "
              "tells you what a decision is likely to do, which is the part that can be checked."},
         ]},

        {"type": "content", "label": "The Credibility Revolution", "title": "Two Nobel prizes for getting the comparison right",
         "blocks": [
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "2019", "label": "Abhijit Banerjee, Esther Duflo and Michael Kremer, \"for their experimental approach to alleviating global poverty\"", "color": "cyan",
                  "source": "Nobel Prize in Economic Sciences 2019, nobelprize.org"},
                 {"num": "2021", "label": "Joshua Angrist and Guido Imbens, \"for their methodological contributions to the analysis of causal relationships\" (shared with David Card)", "color": "green",
                  "source": "Nobel Prize in Economic Sciences 2021, nobelprize.org press release"}]},
             {"t": "body", "html": "Both prizes rewarded the same shift. From the 1980s, economists stopped "
              "trusting a regression because it had many control variables and started asking where the "
              "variation in the treatment came from. Was it a lottery, a rule, a border, a date? If the "
              "answer was \"people chose it\", the estimate inherited every reason they chose. Much of the "
              "experimental work honoured in 2019 was run in India, including the remedial education "
              "trials in Mumbai and Vadodara described in Section 5. Card's half of the 2021 prize was for "
              "empirical contributions to labour economics; his minimum wage study with Alan Krueger "
              "appears in Section 6."},
         ]},

        {"type": "content", "label": "Ways to Go Wrong", "title": "Four routes from a real pattern to a false conclusion",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "amber", "items": [
                  "<strong>Selection.</strong> The people who take up a programme differ from those who do not, in ways that also shape the outcome. Self-help group members were often already more connected.",
                  "<strong>Confounding.</strong> A third factor drives both treatment and outcome. Land ownership raises both access to credit and farm income.",
                  "<strong>Reverse causation.</strong> The outcome drives the treatment. Sick children are taken to clinics, so clinic visits correlate with illness.",
                  "<strong>Chance and choice of analysis.</strong> With enough outcomes and subgroups, something will look significant. Reporting only that result manufactures an effect."]}],
              "right": [{"t": "flow", "steps": [
                  "PATTERN: participants do better",
                  "QUESTION: better than whom?",
                  "CHECK: why did they participate?",
                  "DESIGN: find variation they did not choose",
                  "CLAIM: effect, with its assumptions stated"]}]},
             {"t": "hbox", "color": "cyan", "html": "Each design later in this course is a defence "
              "against one or more of these four. Knowing which defence a study used tells you which "
              "failure to look for."},
         ]},

        {"type": "content", "label": "A Running Example", "title": "One cash transfer, two published answers",
         "blocks": [
             {"t": "body", "html": "India launched the <strong>Janani Suraksha Yojana</strong> (JSY) in 2005, "
              "paying women who give birth in a health facility (Lim et al., The Lancet 2010). Two careful "
              "studies of the same scheme reached different conclusions on the outcome that mattered most."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Lim and colleagues, The Lancet, 2010", "html":
                        "District Level Household Surveys of 2002&ndash;04 and 2007&ndash;09, analysed by "
                        "matching, a with-versus-without comparison and difference-in-differences. JSY raised "
                        "antenatal care and facility births. In the matching analysis, JSY payment was "
                        "associated with 3.7 fewer perinatal deaths per 1,000 pregnancies and 2.3 fewer "
                        "neonatal deaths per 1,000 live births."}],
              "right": [{"t": "panel", "color": "amber", "title": "Powell-Jackson, Mazumdar and Mills, J. Health Economics, 2015", "html":
                         "Difference-in-differences exploiting variation in how intensively districts "
                         "implemented JSY. Cash incentives were associated with more use of maternity "
                         "services, but there was no strong evidence of a reduction in neonatal or early "
                         "neonatal mortality. They also found more pregnancies and a shift away from private "
                         "providers."}]},
             {"t": "hbox", "color": "amber", "html": "We return to this pair in Section 9. By then you will be "
              "able to say why the two designs could disagree and which assumptions each one needs."},
         ]},

        {"type": "content", "label": "Scope", "title": "What this course covers, and where to go for the rest",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Covered here", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "The counterfactual and the vocabulary of treatment effects",
                      "Selection bias, confounders, mediators and colliders, with diagrams",
                      "Why randomisation works and what still goes wrong in trials",
                      "Difference-in-differences, regression discontinuity, instrumental variables, matching and synthetic control, each with an Indian or South Asian study",
                      "External validity, heterogeneity and scale",
                      "A checklist for reading any causal claim"]}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Covered elsewhere", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Running regressions and reading output: Econometrics 101",
                      "Designing and commissioning an evaluation end to end: Impact Evaluation 101",
                      "Sample size and power calculations: Impact Evaluation 101",
                      "Questionnaires and survey sampling: Survey Design 101",
                      "Pooling many studies: Systematic Reviews 101",
                      "Formal estimation in code: the flagship Causal Inference course"]}]}]},
             {"t": "body", "cls": "sm", "html": "No mathematics beyond averages and subtraction is needed. Where a "
              "formula appears it is written out in words beside it."},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "Potential outcomes and the counterfactual"},

        {"type": "content", "label": "The Core Idea", "title": "Every unit has two possible outcomes, and we see one",
         "blocks": [
             {"t": "term", "word": "Potential outcomes",
              "def": "For each unit there is an outcome if treated, written Y(1), and an outcome if "
              "untreated, written Y(0). The causal effect for that unit is Y(1) minus Y(0). Both exist "
              "in principle before treatment is assigned; assignment decides which one we get to observe."},
             {"t": "body", "html": "Donald Rubin set out this framework for observational and randomised "
              "studies in the <em>Journal of Educational Psychology</em> in 1974 (vol. 66, no. 5, pp. "
              "688&ndash;701), and it is often called the Rubin causal model. Its value is that it forces "
              "a precise statement. \"The scholarship improved girls' schooling\" becomes \"for these girls, "
              "years of schooling with the scholarship minus years of schooling without it, at the same "
              "time and place, is positive on average\". Once the claim is written that way, the missing "
              "half is obvious: no girl was both given and denied the scholarship."},
             {"t": "hbox", "color": "cyan", "html": "Every method in this course is a way of filling in the "
              "missing potential outcome with something defensible."},
         ]},

        {"type": "content", "label": "The Fundamental Problem", "title": "You cannot observe the same person treated and untreated",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "body", "html": "Paul Holland named this the <strong>fundamental problem of "
                        "causal inference</strong> in \"Statistics and Causal Inference\", <em>Journal of the "
                        "American Statistical Association</em>, 1986 (vol. 81, no. 396, pp. 945&ndash;960). It is "
                        "a problem of missing data, and no amount of extra data of the same kind solves it. "
                        "Surveying a million households that joined a programme still tells you nothing about "
                        "what those households would have done had they not joined."},
                       {"t": "body", "html": "The way out is to give up on individual effects and estimate "
                        "<strong>averages</strong>. If we can find a group whose average untreated outcome "
                        "equals what the treated group's average untreated outcome would have been, the "
                        "difference in averages is an average causal effect. The rest of the course is about "
                        "finding that group."}],
              "right": [{"t": "panel", "color": "indigo", "title": "The two ways to fill the gap", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "<strong>Different units, same time.</strong> Compare treated households with untreated ones that would have fared the same.",
                      "<strong>Same units, different time.</strong> Compare households with their own past, assuming nothing else changed.",
                      "Most real designs combine the two, and each brings its own assumption."]}]}]},
         ]},

        {"type": "content", "label": "A Worked Table", "title": "Five women, ten outcomes, five observed",
         "compact": True,
         "blocks": [
             {"t": "body", "html": "Illustrative (hypothetical figures). Monthly earnings in rupees for five women offered a tailoring "
              "course. In real data only the shaded column for each woman exists."},
             {"t": "table",
              "head": ["Woman", "Took course?", "Y(1): earnings if trained", "Y(0): earnings if not", "Individual effect", "What we observe"],
              "rows": [
                  ["Asha", "Yes", "&#8377;6,000", "&#8377;5,000", "+&#8377;1,000", "&#8377;6,000"],
                  ["Bina", "Yes", "&#8377;7,000", "&#8377;6,500", "+&#8377;500", "&#8377;7,000"],
                  ["Chandni", "Yes", "&#8377;5,500", "&#8377;4,000", "+&#8377;1,500", "&#8377;5,500"],
                  ["Devi", "No", "&#8377;3,500", "&#8377;2,500", "+&#8377;1,000", "&#8377;2,500"],
                  ["Esha", "No", "&#8377;3,000", "&#8377;2,000", "+&#8377;1,000", "&#8377;2,000"]]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "cls": "sm", "html": "True average effect for the three who trained: "
                        "&#8377;1,000. True average for all five: &#8377;1,000."}],
              "right": [{"t": "body", "cls": "sm", "html": "Naive comparison of observed means: &#8377;6,167 minus "
                         "&#8377;2,250 = &#8377;3,917. Nearly four times too large, because the women who "
                         "chose the course already earned more."}]},
         ]},

        {"type": "content", "label": "Which Average?", "title": "ATE, ATT and LATE answer different policy questions",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Estimand", "Plain meaning", "Policy question it answers"],
              "rows": [
                  ["ATE: average treatment effect", "Average of Y(1) minus Y(0) over everyone in the population", "What if we gave it to everybody?"],
                  ["ATT: average effect on the treated", "Average effect among those who actually received it", "Was it worth it for the people who got it?"],
                  ["ATU: average effect on the untreated", "Average effect among those who did not receive it", "What would expansion to the rest achieve?"],
                  ["ITT: intention to treat", "Effect of being offered or assigned, whether or not the unit took it up", "What does announcing the programme achieve, given real take-up?"],
                  ["LATE: local average treatment effect", "Average effect among units whose take-up was changed by the offer or instrument", "What does it do for people who respond to the nudge?"]]},
             {"t": "body", "html": "These are equal only when effects are the same for everyone, which they "
              "rarely are. A microcredit programme can have a large ATT among existing entrepreneurs who "
              "borrowed and a small ATE across all households, most of whom never wanted a loan. A report that "
              "says \"the effect\" without saying which one has left out the most useful sentence."},
         ]},

        {"type": "content", "label": "Choosing a Comparison", "title": "The comparison group is the counterfactual",
         "blocks": [
             {"t": "body", "html": "Every causal estimate is a comparison, and the comparison group is the "
              "study's guess at the missing potential outcome. Asking \"compared with whom?\" is the single "
              "most useful question a reader can put to a claim, because the answer tells you what had to be "
              "true for the number to be right."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "amber", "title": "Weak comparisons", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Participants against eligible people who declined",
                      "Programme districts against districts the state chose to leave out",
                      "The same village before and after, in a year with a better monsoon",
                      "Beneficiaries against the state average"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "Stronger comparisons", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Applicants who lost a lottery for places",
                      "Districts just below and above an eligibility score",
                      "Late-phase districts, before their phase began, tracked alongside early ones",
                      "Villages randomly assigned to wait a year"]}]}]},
             {"t": "hbox", "color": "cyan", "html": "The stronger comparisons share one property: something "
              "other than the units' own choices or the implementer's judgement decided who was treated."},
         ]},

        {"type": "content", "label": "Before and After", "title": "Before-after comparisons credit the programme with everything else",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "body", "html": "A before-after comparison uses each unit's own past as its "
                        "counterfactual. It assumes the outcome would have stayed exactly where it was. In a "
                        "fast-changing economy that assumption fails almost by default: wages, prices, "
                        "rainfall, roads, phones and other schemes all move between the two survey rounds."},
                       {"t": "body", "html": "Illustrative (hypothetical figures): a district reports that average yields rose 18% in "
                        "the two years after a soil health card drive. If the second year had a normal monsoon "
                        "after a drought, much of the rise would have happened anyway. The before-after number "
                        "measures the card drive plus the rain plus every other change, and cannot tell them "
                        "apart."}],
              "right": [{"t": "panel", "color": "red", "title": "When before-after is all you have", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Plot several years of the outcome before the programme, if they exist",
                      "Look at the same outcome in places without the programme over the same years",
                      "Name the other changes in the period and say which way each would push",
                      "Report the result as a change over time; call it an effect only with a comparison group"]}]}]},
         ]},

        {"type": "content", "label": "SUTVA", "title": "No spillovers and one version of treatment",
         "blocks": [
             {"t": "term", "word": "Stable unit treatment value assumption (SUTVA)",
              "def": "Two conditions behind every simple estimate. First, one unit's outcome does not depend "
              "on whether other units were treated (no interference). Second, the treatment is the same "
              "thing for everyone who receives it (no hidden versions)."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "amber", "title": "Interference in practice", "html":
                        "Deworming one child lowers infection risk for classmates. A public works programme "
                        "that hires many labourers can raise wages for workers who never joined it, which "
                        "Imbert and Papp (2015) found for India's employment guarantee. If untreated units "
                        "are affected, comparing them with treated units misstates the total effect."}],
              "right": [{"t": "panel", "color": "indigo", "title": "Hidden versions in practice", "html":
                         "\"Received the training\" can mean a three-day course run well in one block and a "
                         "half-day session run badly in another. Averaging the two produces an effect for a "
                         "treatment that nobody received. Record what was delivered, where, and how much."}]},
             {"t": "hbox", "color": "cyan", "html": "Randomising whole villages or schools, with everyone "
              "inside a unit in the same arm, is a common way to contain spillovers inside the unit."},
         ]},

        {"type": "content", "label": "The Selection Equation", "title": "A naive difference equals the effect plus selection bias",
         "blocks": [
             {"t": "hbox", "color": "indigo", "html": "<strong>Observed difference in means</strong> = "
              "<strong>ATT</strong> + <strong>selection bias</strong>, where selection bias = average Y(0) of "
              "the treated minus average Y(0) of the untreated."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Read the equation in words. The gap we see between participants "
                        "and non-participants has two parts. One is what the programme did for participants. "
                        "The other is how different the two groups would have been with no programme at all. "
                        "In the tailoring table, the observed gap was &#8377;3,917, the effect on the trained "
                        "was &#8377;1,000, and the remaining &#8377;2,917 was selection bias: the trained women "
                        "would have earned &#8377;5,167 on average without the course, against &#8377;2,250 for "
                        "the others."}],
              "right": [{"t": "body", "html": "This identity, set out in Angrist and Pischke's <em>Mostly "
                         "Harmless Econometrics</em> (Princeton University Press, 2009), explains the whole "
                         "course in one line. Randomisation makes the second term zero in expectation. "
                         "Difference-in-differences removes the part of it that is fixed over time. "
                         "Regression discontinuity makes it small near a cutoff. Matching removes the part "
                         "explained by what you measured. Each method attacks the same term."}]},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "Selection bias and confounding"},

        {"type": "content", "label": "Self-Selection", "title": "Who joins a programme is never an accident",
         "blocks": [
             {"t": "body", "html": "Participation is a decision, made by people with reasons, and the reasons "
              "usually relate to the outcome. Farmers who adopt a new seed tend to have irrigation, credit and "
              "information. Parents who enrol a child in an after-school class tend to care a great deal about "
              "schooling. Women who join a self-help group in its first year tend to be the ones with time, "
              "a network and some savings."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "amber", "title": "Positive selection", "html":
                        "The better-off or more motivated join, so participants would have done well anyway. "
                        "The naive estimate is too large. Most voluntary training, credit and technology "
                        "programmes are at risk of this."}],
              "right": [{"t": "panel", "color": "indigo", "title": "Negative selection", "html":
                         "The worse-off are targeted or join out of need, so participants would have done "
                         "worse anyway. The naive estimate is too small and can even flip sign. Nutrition "
                         "rehabilitation centres admit the most malnourished children, so their graduates can "
                         "look worse than children who never needed the centre."}]},
             {"t": "hbox", "color": "cyan", "html": "Targeting is a form of selection. A well-targeted "
              "programme is, for the evaluator, a programme whose beneficiaries differ systematically from "
              "everyone else."},
         ]},

        {"type": "content", "label": "A Bangladesh Case", "title": "Microcredit in Bangladesh: the estimate that did not survive reanalysis",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Pitt and Khandker, JPE 1998", "html":
                        "Studied participation in Grameen Bank and two other group-based credit programmes, "
                        "using a quasi-experimental survey design to correct for unobserved individual and "
                        "village-level differences. Reported that household "
                        "consumption rose 18 taka for every 100 taka borrowed by women, against 11 taka for "
                        "men. Roodman and Morduch later called it the most influential study of microcredit "
                        "impacts. (<em>Journal of Political Economy</em> 106(5): 958&ndash;996.)"}],
              "right": [{"t": "panel", "color": "amber", "title": "Roodman and Morduch, J. Development Studies 2014", "html":
                         "Replicated and reanalysed the same data. The poverty results disappeared after "
                         "dropping outliers or using a less fragile estimator, and assumptions the original "
                         "analysis relied on, such as normally distributed errors, were contradicted by the "
                         "data. Their conclusion: questions about impact cannot be answered in these data. "
                         "Pitt published a reply in the same issue. (50(4): 583&ndash;604.)"}]},
             {"t": "body", "html": "The lesson concerns selection, and it applies well beyond microcredit. When "
              "participation is chosen, the estimate rests on modelling assumptions, and those assumptions "
              "can be tested and can fail. A randomised trial of group lending in "
              "Hyderabad (Banerjee et al., AEJ: Applied 2015) found higher business investment but no "
              "significant rise in consumption, health or education."},
         ]},

        {"type": "content", "label": "Confounders", "title": "A confounder causes both the treatment and the outcome",
         "blocks": [
             {"t": "term", "word": "Confounder",
              "def": "A variable that affects whether a unit is treated and also affects the outcome through "
              "another path. Leaving it out mixes its effect into the estimated effect of the treatment."},
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "body", "html": "Illustrative. A study finds that children in households with a "
                        "toilet are taller for their age. Household wealth raises the chance of having a "
                        "toilet and, separately, buys better food and health care. Mother's schooling does "
                        "both too. Caste and village location shape all of these at once. Each is a confounder "
                        "of the toilet-height relationship. Some, like wealth, can be measured roughly. Others, "
                        "such as a family's attention to hygiene, are hard to measure at all."},
                       {"t": "body", "html": "Adjusting for measured confounders helps. It cannot remove "
                        "confounding by things that were never recorded, and a long list of controls in a "
                        "table gives no information about what is missing from it."}],
              "right": [dag({"W": ("Wealth", 130, 40, A), "T": ("Toilet", 60, 160, C), "Y": ("Child height", 230, 160, G)},
                            [("W", "T", A, False), ("W", "Y", A, False), ("T", "Y", C, True)],
                            w=300, h=200, note="wealth affects toilet and child height; toilet to height is the effect in question")]},
         ]},

        {"type": "content", "label": "Omitted Variables", "title": "The direction of bias can be reasoned out in advance",
         "compact": True,
         "blocks": [
             {"t": "body", "html": "When a confounder is left out of a comparison or regression, the estimate is "
              "biased by an amount that depends on two signs: how the confounder relates to the treatment, "
              "and how it relates to the outcome. You can usually reason about both before seeing any results, "
              "which tells you whether a reported effect is more likely too big or too small."},
             {"t": "table",
              "head": ["Confounder linked to treatment", "Confounder linked to outcome", "Bias in naive estimate", "Example (Illustrative)"],
              "rows": [
                  ["Positively", "Positively", "Upward, effect overstated", "Motivated farmers adopt drip irrigation and also manage crops better"],
                  ["Positively", "Negatively", "Downward, effect understated", "Sicker patients are more likely to get the new drug and more likely to die"],
                  ["Negatively", "Positively", "Downward, effect understated", "Richer households are less likely to use a ration shop and have better nutrition"],
                  ["Negatively", "Negatively", "Upward, effect overstated", "Remote villages get fewer schools and also have lower learning for other reasons"]]},
             {"t": "hbox", "color": "cyan", "html": "Use this when reading a report: if every plausible "
              "omitted factor pushes the estimate up, a modest reported effect may be close to zero."},
         ]},

        {"type": "content", "label": "Reverse Causation", "title": "Sometimes the outcome is choosing the treatment",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Reverse causation means the arrow points from the outcome to "
                        "the treatment. It is common wherever programmes respond to need, which in public "
                        "policy is most of the time. Drought relief goes to districts with poor harvests. "
                        "Police are posted where crime is high. Remedial teachers are sent to the weakest "
                        "classes. In each case a simple correlation between the programme and the outcome "
                        "has the wrong sign: relief is associated with low yields, police with crime."},
                       {"t": "body", "html": "Timing helps but is not decisive. Measuring the treatment before "
                        "the outcome rules out the outcome causing the treatment directly, yet a third factor "
                        "can still drive both, and anticipation can make the outcome move first."}],
              "right": [{"t": "panel", "color": "indigo", "title": "Simultaneity", "html":
                         "In markets, quantity and price are set together, so regressing one on the other "
                         "recovers neither supply nor demand. The same holds for women's earnings and "
                         "household bargaining power, or for school quality and enrolment. When two things "
                         "cause each other, only variation that shifts one of them from outside, such as a "
                         "rule or an instrument, separates the two directions. Section 8 returns to this."}]},
         ]},

        {"type": "content", "label": "Data Problems", "title": "Attrition and measurement can create bias after assignment",
         "blocks": [
             {"t": "body", "html": "Even a well-chosen comparison can be spoiled by what happens to the data "
              "afterwards. The two most common problems in South Asian field studies are people who cannot be "
              "found at follow-up and outcomes that are measured differently in the two groups."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "amber", "title": "Differential attrition", "html":
                        "If successful migrants leave the village and cannot be traced, and the programme "
                        "encouraged migration, the treated group loses its most successful members. The "
                        "follow-up compares stayers with everyone. Report attrition by arm, test whether "
                        "leavers differ, and use bounds (for example Lee bounds) when they do."}],
              "right": [{"t": "panel", "color": "red", "title": "Measurement that differs by group", "html":
                         "Participants in a hygiene programme learn which answers are expected and report more "
                         "handwashing. Enumerators who know which villages were treated probe differently. Use "
                         "outcomes that are hard to game (test scores, administrative records, observed "
                         "behaviour), and keep enumerators blind to treatment status where possible."}]},
             {"t": "hbox", "color": "cyan", "html": "Attrition and measurement bias apply to randomised "
              "trials as much as to observational studies. Random assignment protects only the moment of "
              "assignment."},
         ]},

        {"type": "content", "label": "Controls Are Limited", "title": "LaLonde's test: adding controls did not recover the experimental answer",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "body", "html": "Robert LaLonde took a United States job training programme that had "
                        "been run as a randomised experiment, so the true effect was known. He then threw away "
                        "the experimental control group and asked what the standard non-experimental methods "
                        "of the day would have estimated, using comparison groups drawn from national surveys "
                        "and the usual econometric adjustments."},
                       {"t": "body", "html": "Many of the methods failed to reproduce the experimental result, "
                        "and they disagreed with each other. Specifications that looked reasonable gave answers "
                        "far from the truth. (\"Evaluating the Econometric Evaluations of Training Programs with "
                        "Experimental Data\", <em>American Economic Review</em> 76(4), 1986, pp. 604&ndash;620.)"},
                       {"t": "body", "cls": "sm", "html": "Dehejia and Wahba (<em>JASA</em> 1999) reanalysed the "
                        "same data with propensity score matching. Smith and Todd (<em>Journal of Econometrics</em> "
                        "125, 2005) found matching estimates on these data highly sensitive to the variables in "
                        "the score and the sample used, and concluded that matching is a useful tool with no "
                        "general claim to solve the evaluation problem. Section 9 picks this up."}],
              "right": [{"t": "darkcard", "label": "Why it matters", "title": "A benchmark nobody usually has",
                         "body": "In most evaluations there is no experiment to check against, so a wrong "
                         "non-experimental estimate looks exactly as credible as a right one. LaLonde's "
                         "study is valuable because it measured how wrong the usual tools could be."}]},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Causal diagrams"},

        {"type": "content", "label": "What a DAG Is", "title": "Draw your assumptions before you estimate anything",
         "blocks": [
             {"t": "term", "word": "Directed acyclic graph (DAG)",
              "def": "A diagram of variables (boxes) joined by arrows, where an arrow from A to B means A is "
              "assumed to cause B, and no chain of arrows leads back to where it started. Missing arrows are "
              "assumptions too: they say one variable does not directly affect another."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Causal diagrams were developed by Judea Pearl and others in "
                        "computer science and epidemiology. Economists came to them later, but they are now "
                        "standard teaching because they turn a vague worry (\"there might be confounding\") "
                        "into a precise question: which variables must be held fixed, and which must be left "
                        "alone, to isolate one arrow."}],
              "right": [{"t": "body", "html": "A DAG does not estimate anything. It tells you what your "
                         "assumptions imply about what to control for. Hern&aacute;n and Robins's free book "
                         "<em>Causal Inference: What If</em> (miguelhernan.org/whatifbook) teaches the method "
                         "with health examples, and the free web tool DAGitty (dagitty.net) lets you draw a "
                         "diagram and lists the adjustment sets it implies."}]},
             {"t": "hbox", "color": "cyan", "html": "Drawing a diagram with a programme team takes an hour and "
              "surfaces disagreements about how the programme works that would otherwise appear only after "
              "the data are in."},
         ]},

        {"type": "content", "label": "Three Building Blocks", "title": "Forks, chains and colliders",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Shape", "Arrows", "Name of middle variable", "Adjust for it?"],
                        "rows": [
                            ["Fork", "T &larr; Z &rarr; Y", "Confounder", "Yes: it opens a non-causal path"],
                            ["Chain", "T &rarr; M &rarr; Y", "Mediator", "No, if you want the total effect of T"],
                            ["Collider", "T &rarr; K &larr; Y", "Collider", "No: adjusting opens a false path"]]},
                       {"t": "body", "cls": "sm", "html": "Every larger diagram is made of these three shapes. "
                        "A path between treatment and outcome carries association unless it is blocked. A fork "
                        "or chain is blocked by adjusting for its middle variable. A collider is blocked as long "
                        "as you leave it, and its consequences, alone. Adjusting for a collider unblocks it."}],
              "right": [dag({"T": ("Treatment", 70, 160, C), "Z": ("Confounder", 70, 40, A),
                             "Y": ("Outcome", 250, 160, G), "K": ("Collider", 250, 40, R)},
                            [("Z", "T", A, False), ("Z", "Y", A, False), ("T", "Y", C, False),
                             ("T", "K", R, True), ("Y", "K", R, True)],
                            w=320, h=200, note="confounder points into treatment and outcome; both point into a collider")]},
             {"t": "hbox", "color": "amber", "html": "The common habit of controlling for every available "
              "variable is safe only for forks. For chains and colliders it introduces bias."},
         ]},

        {"type": "content", "label": "Mediators", "title": "Controlling for a mediator removes part of the effect",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "body", "html": "Illustrative. A cash transfer to mothers is meant to improve "
                        "child height. Most of the effect is expected to work through more spending on food. "
                        "An analyst regresses height on the transfer and, to be careful, adds household food "
                        "expenditure as a control. The transfer's coefficient falls close to zero and the report "
                        "concludes the transfer had no effect on height."},
                       {"t": "body", "html": "The conclusion is wrong. Holding food spending fixed asks what "
                        "the transfer did for children whose food spending did not change, which removes the "
                        "main channel by design. The coefficient is now an estimate of the effect through every "
                        "other route, and even that is biased if anything unmeasured affects both food spending "
                        "and height."},
                       {"t": "body", "cls": "sm", "html": "Rule: variables measured after treatment that could have "
                        "been changed by it are not controls. Decompose mechanisms with methods built for "
                        "mediation, and treat the results as weaker than the total effect."}],
              "right": [dag({"T": ("Transfer", 70, 40, C), "M": ("Food spend", 170, 120, I), "Y": ("Height", 270, 40, G)},
                            [("T", "M", C, False), ("M", "Y", I, False), ("T", "Y", C, True)],
                            w=340, h=170, note="transfer works through food spending to height")]},
         ]},

        {"type": "content", "label": "Colliders", "title": "The birth weight paradox: selecting on a collider",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Among United States infants born in 1991, babies of mothers who "
                        "smoked had higher risks of both low birth weight and infant death. But <em>among "
                        "low birth weight babies</em>, those born to smokers had lower mortality (relative rate "
                        "0.79). For years this was read as a puzzle, even as a sign smoking protected small "
                        "babies."},
                       {"t": "body", "html": "Hern&aacute;ndez-D&iacute;az, Schisterman and Hern&aacute;n showed "
                        "with causal diagrams that the pattern appears with no protective effect at all. Low "
                        "birth weight is caused by smoking and also by other things, such as birth defects, "
                        "that raise mortality. Among small babies, those whose smallness is not explained by "
                        "smoking are more likely to be small for a deadlier reason. (<em>American Journal of "
                        "Epidemiology</em> 164(11), 2006, pp. 1115&ndash;1120.)"}],
              "right": [dag({"S": ("Smoking", 70, 40, C), "D": ("Defects", 270, 40, R),
                             "L": ("Low weight", 170, 110, A), "Y": ("Death", 170, 180, G)},
                            [("S", "L", C, False), ("D", "L", R, False), ("D", "Y", R, False),
                             ("L", "Y", A, False)],
                            w=340, h=210, note="smoking and birth defects both cause low birth weight; defects also cause death"),
                        {"t": "hbox", "color": "amber", "html": "Restricting a sample to one level of a "
                         "collider is the same as adjusting for it."}]},
         ]},

        {"type": "content", "label": "Colliders in Development Data", "title": "Samples selected on an outcome invite collider bias",
         "blocks": [
             {"t": "body", "html": "Collider bias often arrives through who is in the dataset, with no "
              "control variable involved. Any sample defined by something the treatment and the outcome both "
              "affect is conditioned on a collider."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "amber", "items": [
                  "<strong>Surviving firms.</strong> Studying only enterprises still operating two years after a loan programme. Loans and good management both keep a firm alive, so among survivors borrowers may look less well managed.",
                  "<strong>Admitted students.</strong> Among students admitted to a selective college, entrance score and family income can look negatively related even if they are unrelated in the population.",
                  "<strong>Facility records.</strong> Studying only women who reached a hospital. Distance and complications both shape who arrives."]}],
              "right": [{"t": "panel", "color": "indigo", "title": "What to do", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Draw how units got into the data, as an arrow in the diagram",
                      "Prefer population samples (NFHS, PLFS, a census frame) to programme or facility records when the question allows",
                      "Where only a selected sample exists, say so and reason about the direction of bias",
                      "Do not add a control just because it is available"]}]}]},
         ]},

        {"type": "content", "label": "The Backdoor Rule", "title": "Block every backdoor path, open no new ones",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A <strong>backdoor path</strong> is any path from the treatment "
                        "to the outcome that begins with an arrow pointing <em>into</em> the treatment. Such "
                        "paths carry association that is not the treatment's effect. Pearl's backdoor criterion "
                        "says a set of variables is enough to adjust for if it blocks every backdoor path and "
                        "contains no variable caused by the treatment."},
                       {"t": "body", "html": "In plain terms: control for common causes, leave alone anything "
                        "the treatment might have changed, and do not condition on colliders. If an unmeasured "
                        "variable sits on a backdoor path and nothing else blocks it, no regression with "
                        "observed controls identifies the effect, and you need a design from Sections 5 to 8."}],
              "right": [{"t": "flow", "steps": [
                  "LIST: every variable that could affect treatment or outcome",
                  "DRAW: arrows the team believes exist, with reasons",
                  "TRACE: all paths from treatment to outcome",
                  "MARK: backdoor paths and colliders",
                  "CHOOSE: a measured set that blocks the backdoors",
                  "ADMIT: paths no measured set can block"]}]},
         ]},

        {"type": "content", "label": "A Real Scheme", "title": "Drawing the diagram for Bihar's bicycles for girls",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "body", "html": "Bihar's Cycle programme gave girls who continued to secondary "
                        "school a bicycle (Muralidharan and Prakash 2017). Draw the question \"did the scheme raise girls' "
                        "secondary enrolment?\" before choosing a method."},
                       {"t": "bullets", "sm": True, "items": [
                           "<strong>Treatment:</strong> being in a cohort of girls eligible for the bicycle.",
                           "<strong>Outcome:</strong> age-appropriate enrolment in secondary school.",
                           "<strong>Common causes over time:</strong> rising incomes, new roads, more secondary schools, other state schemes, all of which raised enrolment for boys too.",
                           "<strong>Common causes across places:</strong> Bihar differs from neighbouring states in many ways that also shape schooling.",
                           "<strong>Mediator:</strong> distance to school becoming manageable. Do not control for it."]}],
              "right": [{"t": "panel", "color": "green", "title": "What the diagram points to", "html":
                         "Neither a before-after comparison (confounded by time) nor a Bihar-versus-other-states "
                         "comparison (confounded by place) works alone. Comparing girls with boys, before and "
                         "after, in Bihar and in a neighbouring state, blocks both sets of backdoor paths. That "
                         "is the triple difference Muralidharan and Prakash used, covered in Section 6."}]},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Randomisation"},

        {"type": "content", "label": "Why It Works", "title": "A lottery makes the two groups alike in expectation",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "When assignment is decided by a lottery, nothing about a unit can "
                        "influence whether it is treated. Motivation, wealth, caste, distance, the officer's "
                        "preferences: none of them can predict the coin. So the treatment and control groups "
                        "have the same expected values of every characteristic, measured or not, and the "
                        "selection bias term from Section 2 is zero in expectation."},
                       {"t": "body", "html": "\"In expectation\" matters. In any one draw the groups differ by "
                        "chance, and with few units they can differ a lot. That chance difference is what the "
                        "standard error measures, and it shrinks as the number of randomised units grows."}],
              "right": [{"t": "panel", "color": "green", "title": "What randomisation buys", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Balance on unmeasured characteristics, which no other design can promise",
                      "A simple estimator: the difference in mean outcomes",
                      "Transparent inference: the uncertainty comes from a known random process",
                      "Credibility with sceptical audiences, including finance ministries"]}]},
                       {"t": "hbox", "color": "amber", "html": "It does not buy external validity, freedom "
                        "from attrition, or a correct theory of why the programme worked."}]},
         ]},

        {"type": "content", "label": "Balance", "title": "Checking that randomisation did its job",
         "compact": True,
         "blocks": [
             {"t": "body", "html": "Illustrative baseline balance table from a school-level trial with 120 schools "
              "randomised to a remedial reading programme. A balance table reports baseline means by arm and "
              "the difference. It tests the implementation of the lottery; it does not test whether the design "
              "is valid, which randomisation already guarantees."},
             {"t": "table",
              "head": ["Baseline characteristic", "Treatment (60 schools)", "Control (60 schools)", "Difference", "p-value"],
              "rows": [
                  ["Grade 3 reading score (standardised)", "0.02", "&minus;0.01", "0.03", "0.71"],
                  ["Pupils enrolled per school", "142", "138", "4", "0.64"],
                  ["Share of pupils from SC or ST households", "0.31", "0.34", "&minus;0.03", "0.42"],
                  ["Teacher attendance on unannounced visit", "0.78", "0.76", "0.02", "0.58"],
                  ["Distance to block headquarters (km)", "14.1", "12.9", "1.2", "0.33"]]},
             {"t": "body", "cls": "sm", "html": "With many characteristics, about one in twenty will differ at the 5% "
              "level by chance. Decide in advance which baseline variables you will control for, and stratify "
              "the lottery on the most important ones (for example block, or baseline score) so the arms are "
              "balanced on them by construction."},
         ]},

        {"type": "content", "label": "Units of Randomisation", "title": "Individuals, schools, villages or districts",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Unit randomised", "When it fits", "Cost to the study"],
              "rows": [
                  ["Individual", "Treatment delivered person by person with little spillover: a scholarship, an SMS reminder", "Cheapest in sample size; spillovers inside households or villages contaminate the control"],
                  ["Household", "Transfers, asset grants, counselling", "Effects on neighbours still possible"],
                  ["School or clinic", "Anything a whole institution delivers: a teaching method, staffing", "Outcomes within a school are correlated, so more pupils add less information"],
                  ["Village or ward", "Infrastructure, community mobilisation, local markets", "Need many villages; tens are rarely enough"],
                  ["Block, district or subdistrict", "Administrative reforms rolled out by government", "Few units, so power is low unless the effect is large"]]},
             {"t": "body", "html": "Randomise at the level where the treatment is delivered and where "
              "spillovers stop. The cost is <strong>clustering</strong>: pupils in the same school share a "
              "teacher, so 40 pupils from one school carry much less information than 40 pupils from 40 "
              "schools. Standard errors must be clustered at the level of randomisation, and the power "
              "calculation must use the number of clusters. Impact Evaluation 101 works through the arithmetic."},
         ]},

        {"type": "content", "label": "Indian Evidence", "title": "Balsakhis and computers in Vadodara and Mumbai",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "0.28 SD", "label": "rise in average test scores in schools with the remedial balsakhi programme", "color": "cyan",
                  "source": "Banerjee, Cole, Duflo &amp; Linden, QJE 2007"},
                 {"num": "0.47 SD", "label": "rise in maths scores from computer-assisted learning", "color": "green",
                  "source": "Banerjee, Cole, Duflo &amp; Linden, QJE 2007"},
                 {"num": "~0.10 SD", "label": "what remained one year after the programmes ended", "color": "amber",
                  "source": "Banerjee, Cole, Duflo &amp; Linden, QJE 2007"}]},
             {"t": "body", "html": "The balsakhi programme hired young women from the community to teach "
              "children who were falling behind in basic literacy and numeracy. Schools were randomly assigned. "
              "Most of the gain came from children at the bottom of the distribution, the group the programme "
              "targeted. (\"Remedying Education: Evidence from Two Randomized Experiments in India\", "
              "<em>Quarterly Journal of Economics</em> 122(3): 1235&ndash;1264.)"},
             {"t": "hbox", "color": "cyan", "html": "Two lessons beyond the headline. A cheap input, a "
              "community teacher with little training, produced effects comparable to costlier ones. And gains "
              "faded once the programme stopped, which is a finding about persistence that only a follow-up "
              "could reveal."},
         ]},

        {"type": "content", "label": "Trials at Scale", "title": "Randomising inside government in Andhra Pradesh",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Teacher performance pay", "html":
                        "Muralidharan and Sundararaman randomised a teacher performance pay programme "
                        "across a representative sample of government rural primary schools in Andhra Pradesh. "
                        "After two years, pupils in incentive schools scored 0.27 standard deviations higher "
                        "in maths and 0.17 in language than pupils in control schools, with no evidence of "
                        "adverse consequences. (<em>Journal of Political Economy</em> 119(1), 2011, pp. "
                        "39&ndash;77.)"}],
              "right": [{"t": "panel", "color": "green", "title": "Biometric Smartcards", "html":
                         "Muralidharan, Niehaus and Sukhtankar evaluated biometrically authenticated payments "
                         "for the employment guarantee and social pensions by randomising the rollout over 157 "
                         "subdistricts covering 19 million people. Payments became faster, more predictable and "
                         "less corrupt without reducing access. (<em>American Economic Review</em> 106(10), "
                         "2016, pp. 2895&ndash;2929.)"}]},
             {"t": "body", "html": "The Smartcards study shows a practical route to randomisation inside a "
              "government programme: the state could not roll out everywhere at once, so the order of rollout "
              "was randomised. Units waiting their turn served as the control. A phased rollout that has to "
              "happen anyway is often the cheapest and most ethical trial available."},
         ]},

        {"type": "content", "label": "Lotteries and Encouragement", "title": "When you cannot assign the treatment, assign the offer",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "indigo", "title": "Mindspark lottery, urban India", "html":
                        "Muralidharan, Singh and Ganimian studied a personalised, technology-aided after-school "
                        "programme for middle-school pupils. Free places were allocated by lottery. Lottery "
                        "winners scored 0.37 SD higher in maths and 0.23 SD higher in Hindi after 4.5 months. "
                        "Gains were similar in absolute terms for all pupils, and much larger relative to "
                        "their starting point for weaker ones. (<em>AER</em> 109(4), 2019, pp. "
                        "1426&ndash;1460.)"}],
              "right": [{"t": "panel", "color": "amber", "title": "Migration incentive, Bangladesh", "html":
                         "Bryan, Chowdhury and Mobarak randomly offered households in rural Bangladesh an "
                         "incentive of US$8.50 to temporarily out-migrate during the pre-harvest lean season. The offer induced 22% of households to send a seasonal migrant, raised "
                         "consumption at home, and treated households were 8&ndash;10 percentage points more "
                         "likely to migrate again 1 and 3 years later. (<em>Econometrica</em> 82(5), 2014, pp. "
                         "1671&ndash;1748.)"}]},
             {"t": "hbox", "color": "cyan", "html": "Both designs randomise an <strong>offer</strong>. The "
              "comparison of winners with losers is the intention-to-treat effect. Section 8 shows how to turn "
              "it into the effect of actually attending or migrating."},
         ]},

        {"type": "content", "label": "Effect Sizes", "title": "What South Asian trials found, on one scale",
         "blocks": [
             {"t": "chart", "canvas": "ci_effects", "type": "bar",
              "title": "Effects on test scores in standard deviations, randomised studies",
              "source": "Banerjee et al., QJE 2007; Muralidharan &amp; Sundararaman, JPE 2011; Muralidharan, Singh &amp; Ganimian, AER 2019; Andrabi, Das &amp; Khwaja, AER 2017",
              "data": {"labels": ["Balsakhi remedial (India)", "Computer-assisted maths (India)",
                                  "Performance pay, maths (India)", "Performance pay, language (India)",
                                  "Mindspark, maths (India)", "Mindspark, Hindi (India)",
                                  "School report cards (Pakistan)"],
                       "datasets": [{"label": "Effect (SD)", "data": [0.28, 0.47, 0.27, 0.17, 0.37, 0.23, 0.11],
                                     "backgroundColor": ["#0EA5E9", "#0EA5E9", "#10B981", "#10B981",
                                                         "#6366F1", "#6366F1", "#F59E0B"]}]},
              "options": {"__js__": "{ indexAxis:'y', plugins:{ legend:{ display:false } }, scales:{ x:{ beginAtZero:true, title:{ display:true, text:'Standard deviations' } } } }"}},
             {"t": "body", "cls": "sm", "html": "The studies differ in duration (4.5 months to two years), "
              "grade and test, so the bars are not a league table. Andrabi, Das and Khwaja randomised report "
              "cards across half of the sample villages in Pakistan; scores rose 0.11 SD, private school fees fell 17% and "
              "primary enrolment rose 4.5%."},
         ]},

        {"type": "content", "label": "Threats Inside a Trial", "title": "Randomisation protects assignment, nothing after it",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Threat", "What happens", "Defence"],
              "rows": [
                  ["Non-compliance", "Some assigned units refuse; some control units find the treatment elsewhere", "Report intention to treat; estimate effect on compliers by IV (Section 8)"],
                  ["Attrition", "Units lost at follow-up differ by arm", "Track hard; report rates by arm; bound the estimate"],
                  ["Spillovers", "Control units are affected by treated neighbours", "Randomise larger clusters; measure spillovers with buffer or partial-treatment designs"],
                  ["Hawthorne and John Henry effects", "Treated units change because they are observed; controls compete", "Measure outcomes unobtrusively; give controls a placebo contact"],
                  ["Specification searching", "Many outcomes and subgroups tested, the significant ones reported", "Pre-register; write a pre-analysis plan; adjust for multiple outcomes"],
                  ["Implementation failure", "The treatment was not delivered as designed", "Monitor delivery; report what was actually delivered"]]},
             {"t": "hbox", "color": "amber", "html": "Banerjee, Duflo, Glennerster and Kinnan's Hyderabad "
              "microfinance trial (<em>AEJ: Applied</em> 7(1), 2015) shows one such issue plainly: the lender "
              "entered 52 randomly chosen neighbourhoods, but take-up of microcredit rose only 8.4 percentage "
              "points, and two years later the control areas had also gained access to microcredit."},
         ]},

        {"type": "content", "label": "Ethics and Registration", "title": "Running a fair trial in South Asia, as of October 2026",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "When a lottery is fair", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Demand exceeds supply, so someone must be left out anyway",
                      "There is real uncertainty about whether the programme helps (equipoise)",
                      "The rollout is phased, so the control group is treated later",
                      "No one is denied an entitlement they hold in law",
                      "Participants give informed consent, and an ethics committee has approved the protocol"]}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Registration and data", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Register social science trials before baseline on the American Economic Association's RCT Registry; register clinical and health trials in India on the Clinical Trials Registry of India (CTRI)",
                      "Write a pre-analysis plan naming primary outcomes and the main specification",
                      "Personal data of participants in India falls under the Digital Personal Data Protection Act 2023 and the DPDP Rules 2025, whose duties apply from 13 May 2027. From that date section 17(2)(b) exempts processing for research and statistical purposes that meets its conditions, including that no decision specific to the person is taken. Plan studies running past that date to comply"]}]}]},
             {"t": "body", "cls": "sm", "html": "Research Ethics 101 and Data Protection &amp; the DPDP Act 101 cover "
              "consent, ethics review and data handling in detail."},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Natural experiments and difference-in-differences"},

        {"type": "content", "label": "Natural Experiments", "title": "When a rule, a lottery or history does the randomising",
         "blocks": [
             {"t": "term", "word": "Natural experiment",
              "def": "A situation in which treatment was assigned by something outside the units' control, "
              "and plausibly unrelated to their outcomes, without the researcher designing it: a "
              "constitutional rotation, an eligibility cutoff, a phased rollout, a border, a date of birth."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Reserved seats for women pradhans", "html":
                        "In West Bengal in 1998, one third of village council pradhan posts were randomly selected "
                        "to be reserved for women. Chattopadhyay and Duflo used this randomised policy, with "
                        "data on 265 village councils in West Bengal and Rajasthan. In West "
                        "Bengal, women leaders invested more in water, fuel and roads, the goods rural women "
                        "had asked for, and men more in education. (<em>Econometrica</em> 72(5), 2004; NBER "
                        "Working Paper 8615.)"}],
              "right": [{"t": "panel", "color": "amber", "title": "What makes it credible", "html":
                         "Reservation was assigned at random, unrelated to a village's needs or politics, so reserved and unreserved councils were comparable. The "
                         "researcher's task shifts from building a comparison to documenting that the rule "
                         "really was followed and could not be manipulated. Always ask who could have "
                         "influenced the \"natural\" assignment."}]},
         ]},

        {"type": "content", "label": "The DiD Logic", "title": "Difference-in-differences in a two-by-two table",
         "compact": True,
         "blocks": [
             {"t": "body", "html": "Illustrative case (hypothetical figures). A state starts a free school bus in District A in 2024. District B "
              "gets nothing. Girls' attendance rates in both districts, before and after:"},
             {"t": "table",
              "head": ["", "2023 (before)", "2025 (after)", "Change"],
              "rows": [
                  ["District A (bus)", "71%", "82%", "+11 points"],
                  ["District B (no bus)", "64%", "70%", "+6 points"],
                  ["Difference A minus B", "7 points", "12 points", "<strong>+5 points</strong>"]]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The first difference (after minus before, within A) removes "
                        "everything fixed about District A. The second (A's change minus B's change) removes "
                        "everything that changed over time for both districts, such as a statewide fee waiver. "
                        "The +5 points is the estimate."}],
              "right": [{"t": "body", "html": "Neither single comparison would do. Before-after in A says +11, "
                         "crediting the bus with the statewide trend. After-only, A against B, says +12, "
                         "crediting the bus with A's head start. The DiD keeps only the part of A's change "
                         "that B did not share."}]},
         ]},

        {"type": "content", "label": "Parallel Trends", "title": "The one assumption: the same trend without the programme",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "chart", "canvas": "ci_parallel", "type": "line",
                        "title": "Girls' attendance (%), Illustrative",
                        "source": "Illustrative; dashed line is the assumed counterfactual for District A",
                        "data": {"labels": ["2020", "2021", "2022", "2023", "2024", "2025"],
                                 "datasets": [
                                     {"label": "District A (bus from 2024)", "data": [65, 67, 69, 71, 77, 82],
                                      "borderColor": "#0EA5E9", "backgroundColor": "#0EA5E9", "tension": 0.2},
                                     {"label": "District B", "data": [58, 60, 62, 64, 67, 70],
                                      "borderColor": "#F59E0B", "backgroundColor": "#F59E0B", "tension": 0.2},
                                     {"label": "A without bus (assumed)", "data": [None, None, None, 71, 74, 77],
                                      "borderColor": "#64748B", "borderDash": [6, 4], "pointRadius": 0, "tension": 0.2}]},
                        "options": {"__js__": "{ plugins:{ legend:{ position:'bottom' } }, scales:{ y:{ min:50, max:90 } } }"}}],
              "right": [{"t": "body", "html": "DiD assumes that, without the programme, the treated group's "
                         "outcome would have moved in parallel with the comparison group's. The levels can "
                         "differ; the trends must match. The assumption is about a counterfactual, so it can "
                         "never be proved."},
                        {"t": "body", "html": "What can be checked is whether the trends were parallel "
                         "<em>before</em> treatment. Several pre-programme years moving together make the "
                         "assumption more believable. Diverging pre-trends are a warning that the groups were "
                         "already on different paths."},
                        {"t": "hbox", "color": "amber", "html": "Parallel pre-trends are supporting evidence and fall short of proof. "
                         "A shock that hits only the treated area at the same time as the programme still "
                         "breaks the design."}]},
         ]},

        {"type": "content", "label": "Canonical Studies", "title": "Two natural experiments every evaluator should know",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Minimum wages, New Jersey, 1992", "html":
                        "On 1 April 1992 New Jersey raised its minimum wage from $4.25 to $5.05 an hour. Card "
                        "and Krueger surveyed 410 fast-food restaurants in New Jersey and eastern Pennsylvania, "
                        "where the minimum wage did not change, before and after. Comparing employment growth "
                        "across the border, they found no indication that the rise reduced employment. "
                        "(<em>American Economic Review</em> 84(4), 1994.) The debate it started ran for years "
                        "and sharpened how DiD studies are checked."}],
              "right": [{"t": "panel", "color": "indigo", "title": "School construction, Indonesia, 1973&ndash;78", "html":
                         "Global canon from Indonesia. Duflo combined differences across regions in the number "
                         "of INPRES schools built with differences across birth cohorts in exposure. Each school "
                         "built per 1,000 children raised education by 0.12 to 0.19 years and wages by 1.5% to "
                         "2.7%, implying returns to schooling of 6.8% to 10.6%. (<em>American Economic Review</em> "
                         "91(4), 2001, pp. 795&ndash;813.)"}]},
             {"t": "hbox", "color": "cyan", "html": "Both use the same logic: compare the change for those "
              "exposed with the change for those not exposed. The INPRES study shows how age cohorts can serve "
              "as the \"before\" and \"after\"."},
         ]},

        {"type": "content", "label": "An Indian DiD", "title": "The employment guarantee's phased rollout as a natural experiment",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "body", "html": "The National Rural Employment Guarantee Scheme came into force in "
                        "February 2006 in the first 200 districts, reached a further set of districts in April "
                        "2007, and covered all remaining districts from 1 April 2008 (Zimmermann, IZA Discussion "
                        "Paper 6858, 2012; Ministry of Rural Development). The phases were set by a "
                        "backwardness ranking, so early districts were poorer."},
                       {"t": "body", "html": "Imbert and Papp compared trends in districts that got the programme "
                        "earlier with those that got it later. Public works hiring crowded out private work and "
                        "raised private sector wages, and they calculate that the wage gains for poor households "
                        "were large relative to the gains of participants alone. (<em>AEJ: Applied Economics</em> "
                        "7(2), 2015, pp. 233&ndash;263.)"}],
              "right": [{"t": "panel", "color": "amber", "title": "As of October 2026", "html":
                         "The Mahatma Gandhi National Rural Employment Guarantee Act 2005 was repealed from 1 July "
                         "2026 and replaced by the Viksit Bharat G RAM G Act 2025, with a guarantee of 125 days. "
                         "Studies of the earlier scheme describe that scheme. Any before-after comparison spanning "
                         "July 2026 will mix the new law's effect with everything else that changed that year, "
                         "which is exactly the problem a comparison group is needed to solve."}]},
         ]},

        {"type": "content", "label": "Triple Differences", "title": "Bihar's bicycles: boys and Jharkhand as two comparison groups",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "+32%", "label": "girls' age-appropriate enrolment in secondary school, cohorts exposed to the Cycle programme", "color": "green",
                  "source": "Muralidharan &amp; Prakash, AEJ: Applied 2017"},
                 {"num": "&minus;40%", "label": "reduction in the corresponding gender gap", "color": "cyan",
                  "source": "Muralidharan &amp; Prakash, AEJ: Applied 2017"},
                 {"num": "+18%", "label": "girls appearing for the secondary school certificate exam", "color": "indigo",
                  "source": "Muralidharan &amp; Prakash, AEJ: Applied 2017"}]},
             {"t": "body", "html": "A simple DiD comparing Bihar girls before and after would credit the "
              "scheme with everything that raised enrolment in Bihar at the time. Comparing Bihar girls with "
              "Bihar boys removes Bihar-wide changes, but boys and girls might have been on different trends "
              "anyway. So the authors also used the neighbouring state of Jharkhand, carved out of Bihar on "
              "15 November 2000, and computed the girl-boy gap's change in Bihar minus its change in "
              "Jharkhand. (\"Cycling to School\", <em>AEJ: Applied Economics</em> 9(3), 2017, pp. "
              "321&ndash;350.)"},
             {"t": "hbox", "color": "cyan", "html": "The increases took place mostly in villages farther from "
              "a secondary school, the pattern you would expect if the bicycle worked by cutting the time and "
              "safety cost of getting there. A mechanism that fits the effect's shape makes the claim more believable."},
         ]},

        {"type": "content", "label": "Staggered Adoption", "title": "When units start at different times, the usual regression can mislead",
         "compact": True,
         "blocks": [
             {"t": "body", "html": "Many Indian programmes roll out district by district over years. The usual "
              "estimator, a regression with unit and time fixed effects (two-way fixed effects), was long "
              "assumed to give a sensible average. Work published from 2020 onward showed that, when effects "
              "differ across groups or grow over time, it can compare newly treated units against units "
              "treated earlier, giving some comparisons negative weight."},
             {"t": "table",
              "head": ["Paper", "Main point", "Where"],
              "rows": [
                  ["Goodman-Bacon (2021)", "The two-way fixed effects estimate is a weighted average of all two-by-two DiDs, including early-versus-late comparisons", "<em>Journal of Econometrics</em> 225(2): 254&ndash;277"],
                  ["de Chaisemartin &amp; D'Haultf&oelig;uille (2020)", "Weights can be negative; the coefficient can be negative while every group's effect is positive", "<em>American Economic Review</em> 110(9): 2964&ndash;2996"],
                  ["Callaway &amp; Sant'Anna (2021)", "Estimate effects for each adoption cohort and period, then aggregate as you choose", "<em>Journal of Econometrics</em> 225(2): 200&ndash;230"],
                  ["Sun &amp; Abraham (2021)", "Event-study leads and lags are contaminated in the same way; an interaction-weighted fix", "<em>Journal of Econometrics</em> 225(2): 175&ndash;199"]]},
             {"t": "hbox", "color": "amber", "html": "When reading a staggered-rollout study published before "
              "about 2021, ask whether its results hold with one of these estimators. Many authors have since "
              "re-run their own work this way."},
         ]},

        {"type": "content", "label": "Checking a DiD", "title": "Event studies, placebos and the questions to ask",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Event study", "html":
                        "Estimate the treated-minus-comparison gap for each year before and after the start. "
                        "Before the start the estimates should be close to zero with no trend. After, they show "
                        "how the effect builds or fades. A plot of these coefficients is the single most "
                        "informative figure in a DiD paper; read it before the main table."},
                       {"t": "panel", "color": "green", "title": "Placebo tests", "html":
                         "Pretend the programme started two years earlier and re-estimate: the effect should be "
                         "zero. Or use an outcome the programme cannot plausibly affect. A non-zero placebo means "
                         "something other than the programme differs between the groups."}],
              "right": [{"t": "bullets", "color": "amber", "items": [
                  "Who chose which units were treated first, and on what basis?",
                  "Were there several years of data before treatment, and do they move together?",
                  "Did anything else start in the treated units at the same time: a new collector, another scheme, a road?",
                  "Did people move into or out of treated areas because of the programme?",
                  "If rollout was staggered, was one of the newer staggered-timing estimators used?",
                  "Are standard errors clustered at the level treatment was assigned (state, district)?"]}]},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Regression discontinuity"},

        {"type": "content", "label": "The Idea", "title": "A cutoff rule creates a local experiment",
         "blocks": [
             {"t": "term", "word": "Regression discontinuity (RD)",
              "def": "A design for programmes that assign treatment by a rule based on a score (the running "
              "variable) and a cutoff. Units just above and just below the cutoff are nearly identical, so a "
              "jump in outcomes exactly at the cutoff estimates the effect of treatment for units near it."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Indian administration is full of cutoffs: population thresholds "
                        "for roads and schools, marks for admission and scholarships, land size for subsidies, "
                        "backwardness scores for district programmes, income for ration cards, and vote shares "
                        "that decide who wins a seat. Each is a potential RD."}],
              "right": [{"t": "body", "html": "The logic: a village of 990 people and one of 1,010 differ in "
                         "nothing that matters except which side of a 1,000 rule they fall on. If outcomes jump "
                         "at 1,000 and nowhere else, the rule's treatment is the obvious explanation. RD is often "
                         "called the most credible design short of a lottery."}]},
             {"t": "hbox", "color": "amber", "html": "The price is that the estimate applies to units near "
              "the cutoff. The effect on a village of 300 people may be quite different."},
         ]},

        {"type": "content", "label": "Sharp and Fuzzy", "title": "When the rule is followed exactly, and when it is not",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["", "Sharp RD", "Fuzzy RD"],
              "rows": [
                  ["Rule", "Everyone above the cutoff is treated; no one below is", "Crossing the cutoff raises the chance of treatment but not from 0 to 1"],
                  ["Example (Illustrative)", "A scholarship paid automatically to every student scoring 80% or more", "A road programme that prioritises villages above a population size, though some below get roads and some above do not"],
                  ["Estimate", "Jump in outcome at the cutoff", "Jump in outcome divided by jump in treatment probability"],
                  ["Who it describes", "Units at the cutoff", "Units at the cutoff whose treatment was changed by the rule (compliers)"],
                  ["Close cousin", "A simple comparison of means near the line", "Instrumental variables, with the cutoff as instrument"]]},
             {"t": "body", "html": "Most government rules are fuzzy, because officers use discretion, records "
              "are wrong, and programmes are expanded over time. A fuzzy RD is still credible, but it needs the "
              "jump in take-up at the cutoff to be large, and the estimate is a ratio of two jumps, so it is "
              "noisier than a sharp one."},
         ]},

        {"type": "content", "label": "Indian RD", "title": "Rural roads and population thresholds: PMGSY",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "body", "html": "The Pradhan Mantri Gram Sadak Yojana (PMGSY) is India's national "
                        "rural road programme. Its rules prioritised villages by population, with eligibility "
                        "thresholds at 500 and 1,000 people. Asher and Novosad used those thresholds in a "
                        "fuzzy regression discontinuity design, combined with household and firm census "
                        "microdata."},
                       {"t": "body", "html": "Four years after a road was built, the main effect was to move "
                        "workers out of agriculture. There were no major changes in agricultural outcomes, "
                        "income or assets, and employment in village firms expanded only slightly. "
                        "(\"Rural Roads and Local Economic Development\", <em>American Economic Review</em> "
                        "110(3), 2020, pp. 797&ndash;823.)"}],
              "right": [{"t": "panel", "color": "indigo", "title": "Why the design convinces", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "The programme is large: the paper puts India's national rural road construction programme at $40 billion",
                      "The rule was set by the programme, so a village's own choices did not decide its priority",
                      "Road probability jumps at the threshold, which gives a usable first stage",
                      "The finding is a null for income and assets, which a reader can weigh against the claims made for roads"]}]}]},
         ]},

        {"type": "content", "label": "A District-Level RD", "title": "The employment guarantee's backwardness ranking",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Districts entered the employment guarantee in phases based on a "
                        "Planning Commission index of backwardness built from data of the early to mid-1990s. "
                        "Districts were ranked within each state, and the poorest received the programme first. Laura "
                        "Zimmermann used the rank cutoff between phases as a regression discontinuity. Rank data "
                        "were available for 447 of 618 districts."},
                       {"t": "body", "html": "She found that private sector wages rose substantially for women "
                        "but not for men, concentrated in the main agricultural season, with little evidence of "
                        "lower private employment. (IZA Discussion Paper 6858, 2012.)"}],
              "right": [{"t": "panel", "color": "green", "title": "Two designs, one scheme", "html":
                         "Imbert and Papp's DiD and Zimmermann's RD study the same programme with different "
                         "assumptions. DiD needs early and late districts to have been on parallel trends; RD "
                         "needs districts on either side of the rank cutoff to be comparable and the ranking not "
                         "to have been manipulated. Both find that the programme raised private wages. When "
                         "designs with different weaknesses agree, the finding is stronger than either alone."},
                        {"t": "body", "cls": "sm", "html": "Zimmermann argues manipulation was unlikely because the "
                         "index used data predating the scheme."}]},
         ]},

        {"type": "content", "label": "Seeing the Jump", "title": "What an RD plot shows",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "chart", "canvas": "ci_rd", "type": "scatter",
                        "title": "Share of workers outside agriculture by village population, Illustrative",
                        "source": "Illustrative binned means; not data from any study",
                        "data": {"datasets": [
                            {"label": "Below threshold (no road priority)", "backgroundColor": "#F59E0B",
                             "data": [{"x": 800, "y": 30}, {"x": 840, "y": 31}, {"x": 880, "y": 30.5},
                                      {"x": 920, "y": 31.5}, {"x": 960, "y": 32}, {"x": 990, "y": 32.2}]},
                            {"label": "Above threshold (road priority)", "backgroundColor": "#0EA5E9",
                             "data": [{"x": 1010, "y": 36.5}, {"x": 1040, "y": 36.8}, {"x": 1080, "y": 37.5},
                                      {"x": 1120, "y": 38}, {"x": 1160, "y": 38.2}, {"x": 1200, "y": 39}]}]},
                        "options": {"__js__": "{ plugins:{ legend:{ position:'bottom' } }, scales:{ x:{ title:{ display:true, text:'Village population (threshold 1,000)' } }, y:{ min:25, max:45, title:{ display:true, text:'% non-farm' } } } }"}}],
              "right": [{"t": "body", "html": "A good RD paper shows outcomes averaged in bins of the running "
                         "variable, with separate fitted lines on each side. The effect is the vertical gap "
                         "where the lines meet the cutoff."},
                        {"t": "bullets", "sm": True, "items": [
                            "The jump should be visible to the eye in the plot as well as in the regression table",
                            "Baseline characteristics plotted the same way should show no jump",
                            "Results should hold for narrower and wider bandwidths",
                            "Placebo cutoffs (say at 900 or 1,100) should show nothing"]}]},
         ]},

        {"type": "content", "label": "Threats to RD", "title": "Sorting at the cutoff and the choice of bandwidth",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Manipulation of the running variable", "html":
                        "If people can push their score across the line, units just above differ from those "
                        "just below in whatever made them able to push. Examiners may round marks of 39 up to "
                        "the pass mark of 40; households may under-report income to qualify for a card. The "
                        "sign is bunching: too many units just above the cutoff. McCrary's density test checks "
                        "for it (<em>Journal of Econometrics</em> 142(2), 2008, pp. 698&ndash;714)."}],
              "right": [{"t": "panel", "color": "amber", "title": "Bandwidth and functional form", "html":
                         "A narrow window around the cutoff keeps the comparison clean but leaves few units; a "
                         "wide one adds units that are less alike. High-order polynomials fitted across the "
                         "whole range can create spurious jumps. Current practice uses local linear regression "
                         "with a data-driven bandwidth and bias-corrected confidence intervals (Calonico, "
                         "Cattaneo and Titiunik, <em>Econometrica</em> 82(6), 2014), available as free "
                         "software for R and Stata."}]},
             {"t": "hbox", "color": "cyan", "html": "Also check whether other programmes use the same cutoff. "
              "If a population of 1,000 also triggered a school or a health sub-centre, the jump measures all "
              "of them together."},
         ]},

        {"type": "content", "label": "Close Elections", "title": "Who wins a narrow race is close to a coin toss",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "body", "html": "Elections give a running variable: the winning margin. Among "
                        "constituencies decided by a fraction of a percentage point, which candidate won is "
                        "close to random. Comparing places where a type of candidate barely won with places "
                        "where that type barely lost estimates the effect of having that type of "
                        "representative."},
                       {"t": "body", "html": "Asher and Novosad used close elections in India "
                        "to ask whether being represented by a member of the ruling party affects local "
                        "economic activity. Favouritism led to higher private sector employment, higher share "
                        "prices of firms and more output measured by night lights, and they present evidence "
                        "that politicians work mainly through control over how regulation is implemented. "
                        "(<em>AEJ: Applied Economics</em> 9(1), 2017, pp. 229&ndash;273.)"}],
              "right": [{"t": "darkcard", "label": "Practitioner use", "title": "A design you can borrow",
                         "body": "Close-election RD needs only results by constituency, which the Election "
                         "Commission of India publishes, and an outcome measured for the same constituencies, "
                         "such as night lights, firm counts or programme spending. Check that close races are "
                         "not won disproportionately by incumbents or the ruling party, which would break the "
                         "coin-toss logic."}]},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Instrumental variables"},

        {"type": "content", "label": "The Idea", "title": "An instrument moves the treatment and touches nothing else",
         "compact": True,
         "blocks": [
             {"t": "body", "html": "When people choose whether to be treated, find something that shifts the "
              "choice for reasons unrelated to the outcome. That something is an <strong>instrument</strong>. "
              "The variation in treatment it causes is as good as random, and the effect of the treatment can be "
              "estimated from that variation alone. A lottery for an offer is the cleanest instrument there is."},
             {"t": "table",
              "head": ["Condition", "In plain words", "Can you test it?"],
              "rows": [
                  ["Relevance", "The instrument changes the treatment, substantially", "Yes: look at the first stage and its F-statistic"],
                  ["Independence", "The instrument is as good as randomly assigned, unrelated to anything else that affects the outcome", "Partly: check balance on observed characteristics"],
                  ["Exclusion restriction", "The instrument affects the outcome only through the treatment, by no other route", "No: it must be argued from knowledge of the setting"],
                  ["Monotonicity", "The instrument pushes everyone the same way (no one is less likely to take the treatment because of it)", "Rarely; argued from the setting"]]},
             {"t": "hbox", "color": "amber", "html": "Most failed instrumental variables studies fail on the "
              "exclusion restriction, which is the one condition data cannot check."},
         ]},

        {"type": "content", "label": "The Exclusion Restriction", "title": "State it in one sentence, then try to break it",
         "blocks": [
             {"t": "hbox", "color": "indigo", "html": "<strong>The exclusion restriction:</strong> the instrument "
              "has no effect on the outcome except through its effect on the treatment."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Write the sentence out for the study in front of you, replacing "
                        "the words. \"Winning the Mindspark lottery affects test scores only by changing whether "
                        "the child attends Mindspark.\" Then list every other way the instrument could reach the "
                        "outcome. Could winners' parents have changed tuition or effort because they won? If so, "
                        "the restriction fails and the estimate absorbs that route too."},
                       {"t": "body", "html": "Lotteries usually pass, because the only thing that differs "
                        "between winners and losers is the offer. Instruments taken from geography, weather or "
                        "history usually face many rival routes."}],
              "right": [{"t": "panel", "color": "red", "title": "Rainfall: a cautionary instrument", "html":
                         "Illustrative. An analyst uses district rainfall as an instrument for household income "
                         "to estimate the effect of income on children's schooling. Rainfall does change "
                         "income. It also changes disease, the demand for child labour on farms, migration and "
                         "whether roads to school are passable. Each is a route from rainfall to schooling that "
                         "bypasses income, so the exclusion restriction fails. A variable that affects many "
                         "things is a poor instrument for any one of them."}]},
         ]},

        {"type": "content", "label": "Indian IV", "title": "Dams in India: river gradient as an instrument",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "body", "html": "Large dams are not built at random. They go where the state "
                        "expects benefits, where politics favours them, and where land can be acquired. Comparing "
                        "districts with and without dams mixes these factors with the dams' effects."},
                       {"t": "body", "html": "Duflo and Pande used the fact that river gradient affects how "
                        "suitable a district is for a dam. Gradient therefore predicts where dams were built. The "
                        "exclusion restriction is that, once the authors' other controls are included, gradient "
                        "affects agricultural output and poverty only through dams."},
                       {"t": "body", "html": "Results: downstream districts gained agricultural production and "
                        "lower vulnerability to rainfall shocks; the district where the dam stood saw no "
                        "significant production gain, more volatility, and higher rural poverty. (\"Dams\", "
                        "<em>Quarterly Journal of Economics</em> 122(2), 2007, pp. 601&ndash;646.)"}],
              "right": [{"t": "panel", "color": "amber", "title": "Try to break it", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Does gradient affect farming directly, through soil or drainage?",
                      "Does it affect road building or settlement patterns?",
                      "Read the paper's own tests of these routes, and ask what else slope could change in your setting"]}]}]},
         ]},

        {"type": "content", "label": "LATE and Compliers", "title": "An instrument estimates the effect for those it moves",
         "compact": True,
         "blocks": [
             {"t": "body", "html": "Imbens and Angrist (<em>Econometrica</em> 62(2), 1994) and Angrist, Imbens and "
              "Rubin (<em>JASA</em> 91(434), 1996) showed what an IV estimate means when effects differ across "
              "people. It is the average effect for <strong>compliers</strong>: units whose treatment was changed "
              "by the instrument. This is the local average treatment effect, or LATE."},
             {"t": "table",
              "head": ["Type", "If offered", "If not offered", "In a lottery for tuition places (Illustrative)"],
              "rows": [
                  ["Always-takers", "Treated", "Treated", "Would have paid for similar classes anyway"],
                  ["Never-takers", "Untreated", "Untreated", "Would not attend even if free"],
                  ["Compliers", "Treated", "Untreated", "Attend only when the place is free; the LATE is their effect"],
                  ["Defiers", "Untreated", "Treated", "Assumed not to exist (monotonicity)"]]},
             {"t": "hbox", "color": "cyan", "html": "LATE is a real effect for a real group, but a policy "
              "that reaches different people, such as making attendance compulsory, may have a different "
              "average effect."},
         ]},

        {"type": "content", "label": "The Wald Estimator", "title": "From the effect of the offer to the effect of attending",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "hbox", "color": "indigo", "html": "<strong>LATE</strong> = effect of the "
                        "instrument on the outcome &divide; effect of the instrument on the treatment"},
                       {"t": "body", "html": "Illustrative arithmetic. A lottery offers free remedial classes. "
                        "Winners' scores are 0.12 SD higher than losers' (the intention-to-treat effect). 60% of "
                        "winners attend and 0% of losers do, so the offer raised attendance by 0.6. The effect "
                        "of attending, for compliers, is 0.12 &divide; 0.6 = 0.20 SD."},
                       {"t": "body", "cls": "sm", "html": "The division assumes the offer helped only by causing "
                        "attendance (exclusion) and that winners who did not attend gained nothing."}],
              "right": [{"t": "panel", "color": "green", "title": "In the Mindspark study", "html":
                         "Muralidharan, Singh and Ganimian report the lottery effect (0.37 SD in maths and 0.23 "
                         "SD in Hindi over 4.5 months) and use the lottery as an instrument for days attended. "
                         "Their IV estimates imply that attending for 90 days would raise maths and Hindi scores "
                         "by 0.6 SD and 0.39 SD. The lottery effect answers \"what does offering a place do?\"; "
                         "the IV estimate answers \"what does using the programme do?\" (AER 2019)."},
                        {"t": "hbox", "color": "amber", "html": "Policy reports often quote the larger IV "
                         "number. If take-up in a scaled programme is low, the offer effect is the relevant one."}]},
         ]},

        {"type": "content", "label": "Weak Instruments", "title": "A weak first stage magnifies every small violation",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The IV estimate divides by the first stage. If the instrument "
                        "moves the treatment only a little, a small direct effect of the instrument on the "
                        "outcome (a slight exclusion failure) is divided by a small number and becomes a large "
                        "bias. Weak instruments also make conventional confidence intervals far too narrow."},
                       {"t": "body", "html": "For decades practitioners pre-tested with a rule of thumb of a "
                        "first-stage F-statistic above 10, drawn from Staiger and Stock (<em>Econometrica</em> "
                        "65(3), 1997) and Stock and Yogo (2005). Lee, McCrary, "
                        "Moreira and Porter showed that conventional t-tests can be badly distorted even then. "
                        "Across 61 <em>American Economic Review</em> papers, for a quarter of specifications "
                        "the corrected standard errors were at least 49% larger than the usual ones at the 5% "
                        "level. (<em>AER</em> 112(10), 2022, pp. 3260&ndash;3290.)"}],
              "right": [{"t": "panel", "color": "amber", "title": "What to look for", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "The first-stage estimate and its F-statistic reported prominently",
                      "The reduced form (instrument on outcome), which needs no exclusion argument to interpret as the effect of the instrument",
                      "Confidence intervals that stay valid with weak instruments, such as Anderson-Rubin or the tF adjustment",
                      "An IV estimate many times larger than the simple comparison, which often signals a weak or invalid instrument"]}]}]},
         ]},

        {"type": "content", "label": "Reading an IV Study", "title": "Five questions for any instrumental variables claim",
         "blocks": [
             {"t": "flow", "steps": [
                 "NAME: what is the instrument, and why does it move the treatment?",
                 "FIRST STAGE: how strongly, and is the F-statistic reported?",
                 "EXCLUSION: every other route from instrument to outcome, ruled out how?",
                 "COMPLIERS: who did the instrument move, and do they resemble the policy's target group?",
                 "COMPARE: how does the IV estimate relate to the simple and the reduced-form estimates?"]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Instruments that usually convince", "html":
                        "Randomised offers or encouragements; lotteries for places; fuzzy cutoff rules; "
                        "random assignment of cases to judges or officers with different tendencies."}],
              "right": [{"t": "panel", "color": "red", "title": "Instruments that need hard scrutiny", "html":
                         "Rainfall, distance, historical events, lagged values of the treatment, and averages "
                         "of other people's choices in the same village. Each can reach the outcome by many "
                         "routes."}]},
             {"t": "body", "cls": "sm", "html": "If the report cannot state its exclusion restriction in one sentence "
              "that a programme officer could check against what they know of the place, treat the estimate as "
              "a correlation."},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Matching and synthetic control"},

        {"type": "content", "label": "Matching", "title": "Compare each participant with a non-participant who looked the same",
         "blocks": [
             {"t": "term", "word": "Selection on observables (conditional independence)",
              "def": "The assumption that, among units with the same values of the measured characteristics, "
              "treatment is as good as random. Matching, regression adjustment and weighting all rest on it."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Matching pairs each treated unit with one or more untreated units "
                        "that had the same or similar baseline characteristics: age, caste category, landholding, "
                        "education, village. The effect is the average outcome difference within matched pairs. "
                        "It makes the comparison transparent: you can see exactly who stands in for whom, and "
                        "check whether the matched groups are alike."}],
              "right": [{"t": "body", "html": "Its weakness is the assumption. Matching removes differences in "
                         "what you measured. It does nothing about motivation, information, social networks or "
                         "an officer's judgement, if those drove participation and are missing from the data. A "
                         "matched comparison that looks perfectly balanced on every column can still be "
                         "confounded by something that has no column."}]},
             {"t": "hbox", "color": "amber", "html": "Matching is the right tool when you know how selection "
              "happened and measured it, for example when officers applied a written eligibility checklist "
              "whose items are all in the data."},
         ]},

        {"type": "content", "label": "Propensity Scores", "title": "Reducing many characteristics to one probability",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "With many characteristics, exact matches are impossible. Rosenbaum "
                        "and Rubin showed that matching on the <strong>propensity score</strong>, the probability "
                        "of treatment given the observed characteristics, balances those characteristics as "
                        "well as matching on all of them would. (\"The central role of the propensity score in "
                        "observational studies for causal effects\", <em>Biometrika</em> 70(1), 1983, pp. "
                        "41&ndash;55.)"},
                       {"t": "body", "html": "The score is a convenience for balancing what you measured. It "
                        "adds no protection against what you did not measure, and a well-fitting model of "
                        "participation says nothing about whether the assumption holds."}],
              "right": [{"t": "flow", "steps": [
                  "MODEL: participation as a function of pre-treatment characteristics",
                  "SCORE: each unit's predicted probability of participating",
                  "TRIM: drop units with no counterpart (no common support)",
                  "MATCH or WEIGHT: pair or reweight units with similar scores",
                  "CHECK: balance on each characteristic after matching",
                  "ESTIMATE: outcome difference, with sensitivity analysis"]}]},
         ]},

        {"type": "content", "label": "Common Support", "title": "Matching only works where both groups exist",
         "compact": True,
         "blocks": [
             {"t": "body", "html": "If almost every landless Dalit household in a block joined a programme and "
              "almost no landed household did, there is nobody to match the participants with. Estimates for "
              "regions of the data with no overlap are extrapolations from a model, whatever the software "
              "reports. Good practice is to show the distributions of the score in both groups and say how "
              "many units were dropped."},
             {"t": "table",
              "head": ["Diagnostic", "What good looks like", "What it reveals if poor"],
              "rows": [
                  ["Overlap of propensity scores", "Both groups spread across the same range", "The comparison rests on a few untreated units or on extrapolation"],
                  ["Standardised differences after matching", "Below about 0.1 for each characteristic", "Matching did not balance what it was meant to"],
                  ["Number of units discarded", "Reported, with who they were", "The estimate describes a subgroup the reader did not expect"],
                  ["Sensitivity analysis", "How strong an unobserved confounder would have to be to erase the effect", "Fragile results that a modest omitted factor would overturn"]]},
             {"t": "hbox", "color": "cyan", "html": "Report the effect for the population that was actually "
              "matched, and say who that is."},
         ]},

        {"type": "content", "label": "Strengthening Matching", "title": "Combine matching with differencing, then test sensitivity",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Matching plus difference-in-differences", "html":
                        "If baseline and follow-up data exist, match on pre-programme characteristics and "
                        "then compare <em>changes</em> in outcomes. Differencing removes unmeasured "
                        "differences that are fixed over time, such as a household's location or a "
                        "village's history, which matching alone leaves in place. On the LaLonde data, Smith "
                        "and Todd (<em>Journal of Econometrics</em> 2005) found the difference-in-differences "
                        "matching estimator performed best among those they studied, because it removed "
                        "time-invariant sources of bias such as geographic mismatch between participants and "
                        "non-participants."}],
              "right": [{"t": "panel", "color": "indigo", "title": "Sensitivity analysis", "html":
                         "Ask how strong an unmeasured confounder would have to be to change the conclusion. "
                         "Cinelli and Hazlett (<em>Journal of the Royal Statistical Society Series B</em> "
                         "82(1), 2020) give measures that can be computed from standard regression output, "
                         "including the minimum strength of association hidden confounding would need, with "
                         "both treatment and outcome, to overturn the result. Compare that strength with the "
                         "strongest confounder you did measure, such as landholding or education."}]},
             {"t": "hbox", "color": "amber", "html": "A matching study that reports neither a pre-programme "
              "comparison nor a sensitivity analysis is asking the reader to accept its main assumption on "
              "trust."},
             {"t": "body", "cls": "sm", "html": "Lim and colleagues' JSY evaluation used three approaches "
              "(matching, with-versus-without and difference-in-differences) for the same reason: agreement "
              "across methods with different weaknesses is more informative than any one estimate."},
         ]},

        {"type": "content", "label": "The JSY Pair Revisited", "title": "Why matching and DiD could disagree about newborn deaths",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["", "Lim et al., <em>Lancet</em> 2010", "Powell-Jackson et al., <em>J. Health Econ.</em> 2015"],
              "rows": [
                  ["Variation used", "Individual women: who did and did not receive JSY payment", "Districts: differences in how intensively JSY was implemented"],
                  ["Main design", "Matching of women who received JSY payment to similar women who did not; also with-versus-without and DiD", "Difference-in-differences on how intensively districts implemented JSY"],
                  ["Comparison", "Similar women in the same period who did not receive payment", "Districts with lower implementation, before and after"],
                  ["Assumption that must hold", "Receiving payment is as good as random among women with the same observed characteristics", "High- and low-implementation districts would have had parallel trends"],
                  ["Use of maternity care", "Antenatal care and facility births increased", "Uptake of maternity services increased"],
                  ["Neonatal mortality", "Reduction of 2.3 per 1,000 live births (matching)", "No strong evidence of a reduction"]]},
             {"t": "body", "cls": "sm", "html": "Women who received JSY payment had to give birth in a facility, and "
              "women who reach a facility may differ in health and access in ways surveys do not record. That "
              "is the opening for selection in the matching estimate. The DiD avoids individual selection but "
              "relies on district trends. Both papers are careful; the disagreement is a lesson in how "
              "assumptions shape answers."},
         ]},

        {"type": "content", "label": "Synthetic Control", "title": "Building a comparison unit from a weighted mix of others",
         "blocks": [
             {"t": "term", "word": "Synthetic control",
              "def": "For a single treated unit (a state, a country), a weighted average of untreated units "
              "chosen so that it tracks the treated unit's outcome closely in the years before treatment. "
              "Its path after treatment stands in for the treated unit's counterfactual."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "The Basque Country", "html":
                        "Abadie and Gardeazabal built a synthetic Basque Country from other Spanish regions. "
                        "After terrorism began in the late 1960s, per capita GDP declined about 10 percentage "
                        "points relative to the synthetic control. (<em>American Economic Review</em> 93(1), "
                        "2003, pp. 113&ndash;132.)"}],
              "right": [{"t": "panel", "color": "green", "title": "California's tobacco programme", "html":
                         "Abadie, Diamond and Hainmueller formalised the method and applied it to California's "
                         "tobacco control programme, comparing California with a weighted mix of other US "
                         "states. (<em>Journal of the American Statistical Association</em> 105(490), 2010, pp. "
                         "493&ndash;505.)"}]},
             {"t": "body", "cls": "sm", "html": "Synthetic control suits the policy changes Indian states make one at "
              "a time, such as a state-specific prohibition, a new welfare scheme, or a change in land law, "
              "where there is one treated state and many possible comparisons."},
         ]},

        {"type": "content", "label": "Synthetic Control in Practice", "title": "Choosing donors and testing with placebos",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Illustrative case (hypothetical figures). Suppose one state introduces a monthly cash transfer to "
                        "women in 2024 and an analyst wants its effect on female labour force participation, "
                        "measured each year in the Periodic Labour Force Survey. The donor pool is the other "
                        "states. The method picks weights (say 40% one neighbouring state, 35% another, 25% a "
                        "third) so the weighted average matches the treated state's participation rate for "
                        "every pre-2024 year."},
                       {"t": "body", "html": "If the fit before 2024 is close, the gap after 2024 is the "
                        "estimate. If the fit is poor, no estimate should be reported."}],
              "right": [{"t": "panel", "color": "amber", "title": "How inference works", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Re-run the method pretending each donor state was the treated one (in-space placebos)",
                      "If the real state's post-treatment gap is unusually large compared with the placebo gaps, the effect is unlikely to be chance",
                      "Re-run with a fake treatment year (in-time placebo)",
                      "Drop donors that had their own similar reform: they are not untreated",
                      "Check whether results change when any one donor is dropped"]}]}]},
             {"t": "hbox", "color": "cyan", "html": "With one treated unit, there is no standard error in "
              "the usual sense. Placebo distributions are the evidence."},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "External validity and heterogeneity"},

        {"type": "content", "label": "Two Kinds of Validity", "title": "Right for this sample, and right for the next place",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "term", "word": "Internal validity",
                        "def": "Whether the study's estimate is a correct causal effect for the units and "
                        "period it studied. Sections 2 to 9 are about this."}],
              "right": [{"t": "term", "word": "External validity",
                         "def": "Whether the effect would be similar for other people, places, times, "
                         "implementers or scales. It is a separate question and needs separate evidence."}]},
             {"t": "body", "html": "A perfectly run trial in 120 schools in one district of Uttar Pradesh tells "
              "you what the programme did there, delivered by that organisation, in those years. Whether it "
              "would do the same in Tamil Nadu, delivered by the state education department to 30,000 schools, "
              "depends on whether the things that made it work are present there too. Those things include the "
              "children's starting level, teachers' incentives, the quality of supervision, and what the "
              "control group was getting instead."},
             {"t": "hbox", "color": "amber", "html": "A common error is to treat a well-identified effect as a "
              "constant of nature. It is a measurement of one programme in one context."},
         ]},

        {"type": "content", "label": "How Much Do Results Generalise?", "title": "Effects vary more than most reports admit",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "body", "html": "Eva Vivalt assembled a large dataset of impact evaluation results "
                        "across development interventions and asked how much effect sizes for the same type of "
                        "programme vary from study to study. She found a large amount of heterogeneity. Effect "
                        "sizes varied systematically with study characteristics, and "
                        "<strong>government-implemented programmes had smaller effects than those implemented by "
                        "academics or non-governmental organisations</strong>, even controlling for sample size. "
                        "Taking study characteristics into account reduced the unexplained variation "
                        "appreciably."},
                       {"t": "body", "cls": "sm", "html": "\"How Much Can We Generalize From Impact Evaluations?\", "
                        "<em>Journal of the European Economic Association</em> 18(6), 2020, pp. 3045&ndash;3089."}],
              "right": [{"t": "darkcard", "label": "For practitioners", "title": "Expect less at scale",
                         "body": "When a ministry plans to adopt a programme tested by an NGO, the honest planning "
                         "assumption is a smaller effect than the trial reported, and the budget case should "
                         "survive that. Ask for the evidence from government-run versions before assuming the "
                         "trial number."}]},
         ]},

        {"type": "content", "label": "Implementer Matters", "title": "Same contract, different employer, different result",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "indigo", "title": "Contract teachers in Kenya", "html":
                        "Bold, Kimenyi, Mwabu, Ng'ang'a and Sandefur embedded a randomised trial in a nationwide "
                        "reform of teacher hiring in Kenyan government primary schools. New teachers on a "
                        "fixed-term contract offered by an international NGO significantly raised test scores. "
                        "Teachers on identical contracts offered by the Kenyan government produced zero impact. "
                        "Bureaucratic and political opposition to the reform led to delays and a different "
                        "interpretation of the same contract terms. (<em>Journal of Public Economics</em> 168, "
                        "2018, pp. 1&ndash;20.)"}],
              "right": [{"t": "body", "html": "This is a global example, but its lesson applies directly in "
                         "South Asia, where many tested programmes are run by NGOs and scaled by state "
                         "governments. The study held the treatment fixed on paper and changed only who "
                         "delivered it. The effect vanished."},
                        {"t": "bullets", "sm": True, "items": [
                            "Record who implemented a tested programme, and how",
                            "Ask whether the implementer at scale has the same incentives and capacity",
                            "Treat \"the programme\" as including its delivery system"]}]},
         ]},

        {"type": "content", "label": "From Proof of Concept to Policy", "title": "Teaching at the Right Level: iterating towards scale in India",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "body", "html": "Pratham's Teaching at the Right Level reorganises instruction "
                        "around children's actual learning levels in place of the prescribed syllabus. It had "
                        "worked well when Pratham ran it. Banerjee, Banerji, Berry, Duflo, Kannan, Mukerji, "
                        "Shotland and Walton describe what happened when it was moved into government schools."},
                       {"t": "body", "html": "Some designs evaluated by randomised trials produced no impact "
                        "within the regular school system. Those failures shaped later versions, and two models "
                        "were eventually developed that raised children's learning levels in government schools "
                        "at scale. (\"From Proof of Concept to Scalable Policies: Challenges and Solutions, with "
                        "an Application\", <em>Journal of Economic Perspectives</em> 31(4), 2017, pp. "
                        "73&ndash;102.)"}],
              "right": [{"t": "panel", "color": "green", "title": "What scaled was a process", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Test the idea where it can work (proof of concept)",
                      "Test it inside the system that will run it",
                      "Expect failures and learn why they happened",
                      "Re-design and test again",
                      "Report the null results along with the successes"]}]}]},
         ]},

        {"type": "content", "label": "Replication Across Countries", "title": "The graduation approach in Bangladesh and six other countries",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "21,000+", "label": "households in 1,309 villages in BRAC's Bangladesh trial, surveyed four times over seven years", "color": "cyan",
                  "source": "Bandiera et al., QJE 2017"},
                 {"num": "6", "label": "countries in the multi-site trial: Ethiopia, Ghana, Honduras, India, Pakistan, Peru", "color": "green",
                  "source": "Banerjee et al., Science 2015"},
                 {"num": "10,495", "label": "households across the six country sites", "color": "indigo",
                  "source": "Banerjee et al., Science 2015"}]},
             {"t": "body", "html": "BRAC's programme for the ultra-poor gives the poorest women livestock assets "
              "and training. In Bangladesh it let poor women move from seasonal casual wage labour into "
              "livestock rearing, raising their labour supply and earnings and leading to asset accumulation "
              "and poverty reduction (\"Labor Markets and Poverty in Village Economies\", <em>QJE</em> 132(2), "
              "2017, pp. 811&ndash;870). A six-country trial of the same multi-part approach, including sites in "
              "India and Pakistan, found lasting progress for the very poor (<em>Science</em> 348(6236), 2015)."},
             {"t": "hbox", "color": "cyan", "html": "Running the same design in several countries, with "
              "common outcome measures, is the most direct evidence on external validity there is."},
         ]},

        {"type": "content", "label": "Heterogeneity", "title": "The average can hide who gains and who does not",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Study", "Average finding", "What the split revealed"],
              "rows": [
                  ["Cash and capital grants to microenterprises, Sri Lanka (de Mel, McKenzie &amp; Woodruff, <em>QJE</em> 2008)", "High average returns to capital, above market interest rates", "Returns varied with ability and household wealth; no positive return in enterprises owned by women"],
                  ["Mindspark, urban India (Muralidharan, Singh &amp; Ganimian, <em>AER</em> 2019)", "0.37 SD in maths", "Similar absolute gains for all pupils; much larger relative gains for academically weaker pupils"],
                  ["Report cards, Pakistan (Andrabi, Das &amp; Khwaja, <em>AER</em> 2017)", "Scores up 0.11 SD, fees down 17%", "Effects differed by schools' initial scores, consistent with better information"],
                  ["Balsakhi, Vadodara and Mumbai (Banerjee et al., <em>QJE</em> 2007)", "0.28 SD", "Most of the gain among children at the bottom of the distribution"]]},
             {"t": "body", "cls": "sm", "html": "Subgroup results are useful and fragile. Credible ones were named in a "
              "pre-analysis plan, have a mechanism behind them, and are reported with all the other subgroups "
              "tested. A single significant subgroup out of twenty, found after the fact, is most likely chance."},
         ]},

        {"type": "content", "label": "Scale and Equilibrium", "title": "Effects can change when everyone gets the programme",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "amber", "title": "Prices and wages move", "html":
                        "A small trial changes nothing in the wider economy. A national programme can. Imbert "
                        "and Papp found that India's employment guarantee raised private sector wages, so "
                        "non-participants who hired labour paid more and labourers who never joined earned more. "
                        "A trial comparing participants with non-participants in the same labour market would "
                        "miss both effects."}],
              "right": [{"t": "panel", "color": "indigo", "title": "Displacement and competition", "html":
                         "If a skills programme helps its trainees win jobs that other workers would otherwise "
                         "have filled, the trainees gain and the total number of jobs may not change. If one "
                         "lender enters a market, others may follow; within two years the Hyderabad microfinance "
                         "trial's control areas had access to microcredit too. The partial effect measured in a trial and the "
                         "total effect of a national policy can differ in size and even in sign."}]},
             {"t": "hbox", "color": "cyan", "html": "Designs that randomise at the level of whole markets, or "
              "vary the share of people treated across villages, are the way to measure these effects. "
              "Smartcards (157 subdistricts) and the BRAC trial (1,309 villages) were built at that scale."},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Reading a causal claim in practice"},

        {"type": "content", "label": "Checklist", "title": "Ten questions to put to any causal claim",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["#", "Question", "A good answer looks like"],
              "rows": [
                  ["1", "What exactly is the claimed effect, on what outcome, of what treatment?", "A number with units, a time period and a defined treatment"],
                  ["2", "Compared with whom?", "A named comparison group and the reason it is credible"],
                  ["3", "Who decided who was treated, and how?", "A lottery, a rule or a rollout schedule nobody could game"],
                  ["4", "What is the key assumption, in one sentence?", "Parallel trends, no sorting at the cutoff, an exclusion restriction, stated plainly"],
                  ["5", "What evidence supports that assumption?", "Pre-trends, balance tables, density tests, placebo results"],
                  ["6", "Which effect: offer or receipt, average or for compliers?", "ITT, ATT or LATE named"],
                  ["7", "Were outcomes and analysis fixed in advance?", "A registration and pre-analysis plan"],
                  ["8", "How many were lost, and from which group?", "Attrition by arm, with bounds if it differs"],
                  ["9", "Who ran it, where, and when?", "Implementer, setting and dates"],
                  ["10", "Do other studies with different designs agree?", "Citations to replications or a systematic review"]]},
         ]},

        {"type": "content", "label": "Decision Table", "title": "Which design fits the situation you are in",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Your situation", "Design to consider", "Assumption you will have to defend"],
              "rows": [
                  ["Programme not yet started; more demand than places", "Randomised lottery or randomised phase-in", "Little beyond good implementation and low attrition"],
                  ["Eligibility decided by a score with a cutoff", "Regression discontinuity", "No manipulation of the score; nothing else changes at the cutoff"],
                  ["Rolled out to some areas first, with data before and after", "Difference-in-differences (with a staggered-timing estimator if rollout was staggered)", "Parallel trends between early and late areas"],
                  ["Offer is random but take-up is voluntary", "Intention to treat, then IV for the effect of take-up", "Exclusion: the offer matters only through take-up"],
                  ["One state or district treated, many untreated, long pre-period", "Synthetic control", "A close pre-treatment fit and no shocks unique to the treated unit"],
                  ["Selection decided by a known, recorded checklist", "Matching or weighting on that checklist", "No unrecorded reasons for participation"],
                  ["None of the above, only participants' data", "Describe outcomes; do not claim an effect", "None, because no effect is claimed"]]},
             {"t": "hbox", "color": "cyan", "html": "The best time to choose a design is before the programme "
              "starts, when a lottery or a phase-in can still be built into the rollout."},
         ]},

        {"type": "content", "label": "Worked Example, Part 1", "title": "A state scholarship for girls: choosing the design",
         "blocks": [
             {"t": "body", "html": "Illustrative case (hypothetical figures). A state launches a scholarship of &#8377;10,000 a year for girls "
              "from households below an income limit who pass Class 10 and enrol in Class 11. It begins in 12 "
              "districts in 2025 and is to cover all 38 districts by 2027. The finance department asks: does it "
              "raise girls' Class 11 enrolment, and is it worth extending?"},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Designs to reject", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Recipients against non-recipients: recipients chose to enrol, which is the outcome itself",
                      "Statewide enrolment before and after: other changes in 2025&ndash;26 are mixed in",
                      "Pilot districts against the rest, after only: pilot districts were picked for a reason"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "Designs to propose", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Randomise the order in which the remaining 26 districts join in 2026 and 2027, and run DiD with an estimator built for staggered timing",
                      "Use the income limit as an RD cutoff, if incomes were certified before the scheme was announced",
                      "Use boys in the same districts as an additional comparison (triple difference)"]}]}]},
             {"t": "body", "cls": "sm", "html": "Ask early: who certifies income, and could families or officers "
              "adjust it once the scheme was known? If yes, the RD option is weak."},
         ]},

        {"type": "content", "label": "Worked Example, Part 2", "title": "Reading the numbers that come back",
         "compact": True,
         "blocks": [
             {"t": "body", "html": "Illustrative results after the 2026 phase (hypothetical figures). Girls' Class 11 enrolment as a share "
              "of girls who passed Class 10:"},
             {"t": "table",
              "head": ["", "2024 (before)", "2026 (after)", "Change"],
              "rows": [
                  ["Districts randomly assigned to join in 2026", "58%", "67%", "+9 points"],
                  ["Districts randomly assigned to join in 2027", "57%", "61%", "+4 points"],
                  ["Difference-in-differences", "", "", "<strong>+5 points</strong>"],
                  ["Same comparison for boys", "62% &rarr; 66%", "61% &rarr; 65%", "0 points"]]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "cls": "sm", "html": "Reading: the scholarship raised girls' enrolment by "
                        "about 5 points, an intention-to-treat effect for all girls who passed Class 10 in "
                        "those districts. Boys show no difference, which supports the comparison. Report the "
                        "confidence interval, clustered by district; with 26 districts it will be wide."}],
              "right": [{"t": "body", "cls": "sm", "html": "For the finance department: divide the total cost by "
                         "the number of additional enrolments implied (5 points times eligible girls). Dividing by all "
                         "scholarship recipients would count girls who would have enrolled anyway. Cost "
                         "Effectiveness 101 explains the calculation."}]},
         ]},

        {"type": "content", "label": "The Language of Reports", "title": "Words that make a claim causal, and what they require",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "amber", "title": "Causal verbs", "html":
                        "\"Led to\", \"resulted in\", \"increased\", \"reduced\", \"improved\", \"because of\", "
                        "\"impact\", \"effect of\", \"attributable to\", \"thanks to the programme\". Each claims "
                        "a counterfactual. A report that uses them about a participant survey with no comparison "
                        "group is making a causal claim without causal evidence."}],
              "right": [{"t": "panel", "color": "green", "title": "Descriptive verbs", "html":
                         "\"Was associated with\", \"participants reported\", \"rose over the period\", \"was "
                         "higher among\", \"coincided with\". These are honest descriptions of patterns. They "
                         "become misleading when the executive summary turns them back into causal verbs, which "
                         "happens often between the results chapter and the press release."}]},
             {"t": "bullets", "color": "cyan", "items": [
                 "Check whether the summary's verbs match the design described in the methods section",
                 "Look for the comparison group in the methods; if it is absent, read every causal verb as \"was associated with\"",
                 "Watch for percentages of participants who \"benefited\": a share of satisfied users is not an effect size"]},
         ]},

        {"type": "content", "label": "Policy Changes, 2025&ndash;26", "title": "Recent Indian reforms that will tempt before-after claims",
         "compact": True,
         "blocks": [
             {"t": "body", "html": "Several large legal changes took effect close together. Any outcome measured "
              "across these dates will move for many reasons at once, so a simple before-after comparison "
              "attributed to one of them should be read with care. Facts as of October 2026."},
             {"t": "table",
              "head": ["Change", "Date in force", "Why it complicates causal claims"],
              "rows": [
                  ["Four Labour Codes (Wages; Industrial Relations; Social Security; Occupational Safety, Health and Working Conditions)", "21 November 2025", "Definitions of wages, workers and establishments change, so administrative series may break"],
                  ["Income-tax Act 2025 replaces the Income-tax Act 1961", "1 April 2026", "Tax data before and after follow different statutory definitions"],
                  ["Viksit Bharat G RAM G Act 2025 replaces MGNREGA 2005 (125 days)", "1 July 2026", "Rural employment and wage outcomes change for reasons beyond any one programme"],
                  ["Digital Personal Data Protection Act 2023, with the DPDP Rules 2025", "Board from 13 November 2025; duties and the s17(2)(b) exemption from 13 May 2027", "Changes what data evaluators can collect and how; research exemption under s17(2)(b) on conditions"],
                  ["Census of India, reference date 1 March 2027, including caste enumeration", "Upcoming", "New baseline counts for sampling frames and running variables in future designs"]]},
         ]},

        {"type": "content", "label": "Commissioning", "title": "What to ask for when you commission an evaluation",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "green", "items": [
                  "<strong>Before the programme starts.</strong> Involve evaluators while rollout can still be randomised or phased. Afterwards, the options shrink to the weaker designs.",
                  "<strong>A written identification strategy.</strong> One page saying what the comparison is and which assumption it needs.",
                  "<strong>A pre-analysis plan.</strong> Primary outcomes, main specification and subgroups named in advance, and registered.",
                  "<strong>Power.</strong> A calculation showing the study can detect an effect large enough to matter for the budget decision."]}],
              "right": [{"t": "bullets", "color": "indigo", "items": [
                  "<strong>Implementation data.</strong> Records of what was delivered, to whom, when.",
                  "<strong>Costs.</strong> Collected alongside outcomes, so cost-effectiveness can be computed.",
                  "<strong>Publication of results whatever they show.</strong> A null result is information the next state needs.",
                  "<strong>Data and code.</strong> Shared in a form another team can re-run, within the limits of the DPDP Act and consent."]}]},
             {"t": "hbox", "color": "amber", "html": "Commissioners shape the evidence as much as researchers "
              "do. A contract that asks only for a final report at the end of the programme almost guarantees "
              "a before-after study of participants."},
         ]},

        # ===================== SECTION 12 =====================
        {"type": "divider", "num": "12", "label": "Section Twelve",
         "title": "Summary and next steps"},

        {"type": "content", "label": "Summary", "title": "What to remember",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "A causal effect compares the outcome with a treatment against the outcome the same units would have had without it. Half of that comparison is always missing.",
                  "A naive comparison equals the effect plus selection bias. Every design is a way of making the second term zero or small.",
                  "Draw a diagram first. Adjust for confounders; leave mediators and colliders alone.",
                  "Randomisation balances everything in expectation. It does not prevent attrition, spillovers or poor implementation.",
                  "DiD needs parallel trends; check pre-trends, and use modern estimators for staggered rollouts."]}],
              "right": [{"t": "bullets", "color": "green", "items": [
                  "RD compares units just either side of a cutoff; check for sorting and report the plot.",
                  "IV needs an exclusion restriction you can state in one sentence, and gives the effect for compliers.",
                  "Matching handles only what was measured; synthetic control needs a close pre-treatment fit.",
                  "Effects vary with implementer, context and scale. Government delivery often yields less than an NGO trial.",
                  "Match a report's verbs to its design before repeating its claims."]}]},
             {"t": "hbox", "color": "amber", "html": "The question that does most of the work, in every "
              "section: compared with whom, and why were they not treated?"},
         ]},

        {"type": "content", "label": "Glossary", "title": "Terms used in this course",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Term", "Meaning"],
              "rows": [
                  ["Counterfactual", "The outcome that would have occurred without the treatment, for the same units at the same time"],
                  ["Selection bias", "The difference between groups that would exist even with no treatment"],
                  ["Confounder / mediator / collider", "A common cause / a step on the causal path / a common effect"],
                  ["ITT / ATT / ATE / LATE", "Effect of the offer / on the treated / on everyone / on compliers"],
                  ["Parallel trends", "DiD assumption that treated and comparison groups would have moved together"],
                  ["Running variable", "The score that decides treatment in an RD design"],
                  ["Exclusion restriction", "IV assumption that the instrument affects the outcome only through the treatment"],
                  ["Common support", "The range where treated and untreated units with similar characteristics both exist"],
                  ["Donor pool", "Untreated units from which a synthetic control is built"],
                  ["External validity", "Whether an effect holds in other places, times, implementers or scales"],
                  ["Pre-analysis plan", "A document fixing outcomes and analysis before data are seen"]]},
         ]},

        {"type": "content", "label": "Reading List", "title": "Books and guides for going further",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Resource", "Why read it", "Access"],
              "rows": [
                  ["Angrist and Pischke, <em>Mostly Harmless Econometrics</em> (Princeton University Press, 2009)", "The economist's toolkit for randomisation, regression, IV, DiD and RD", "Book"],
                  ["Cunningham, <em>Causal Inference: The Mixtape</em> (Yale University Press, 2021)", "Readable, with code in R and Stata, including the newer DiD estimators", "Free online at mixtape.scunning.com"],
                  ["Huntington-Klein, <em>The Effect: An Introduction to Research Design and Causality</em> (2021)", "Built around causal diagrams; good for non-economists", "Free online at theeffectbook.net"],
                  ["Hern&aacute;n and Robins, <em>Causal Inference: What If</em>", "Potential outcomes and diagrams from epidemiology", "Free at miguelhernan.org/whatifbook"],
                  ["Gertler, Martinez, Premand, Rawlings and Vermeersch, <em>Impact Evaluation in Practice</em>, 2nd edition (World Bank)", "Practical guide for programme managers, with design chapters", "Free from the World Bank Open Knowledge Repository"],
                  ["DAGitty", "Draw a diagram and get the adjustment sets", "Free at dagitty.net"]]},
             {"t": "body", "cls": "sm", "html": "For South Asian studies, the papers cited on each slide are the best "
              "starting points. Many have free working paper versions through NBER, J-PAL or the authors' sites."},
         ]},

        {"type": "content", "label": "Where Next", "title": "Continue with related courses",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Go deeper on causal methods", "html":
                        "The flagship <a href=\"/courses/causal/\">Causal Inference course</a> is the next step: "
                        "it takes the designs in this deck into estimation, with worked exercises and a lexicon. "
                        "<br><br><a href=\"/101-courses/impact-eval.html\">Impact Evaluation 101</a> covers the "
                        "full evaluation cycle, including power and sample size. "
                        "<a href=\"/101-courses/econometrics-101.html\">Econometrics 101</a> covers the regression "
                        "tools these designs run on. <a href=\"/101-courses/multivariate-basics.html\">Multivariate "
                        "Analysis 101</a> covers working with many variables at once."}],
              "right": [{"t": "panel", "color": "green", "title": "Related skills", "html":
                         "<a href=\"/101-courses/survey-design.html\">Survey Design 101</a> for collecting the "
                         "outcomes. <a href=\"/101-courses/systematic-reviews.html\">Systematic Reviews &amp; Evidence "
                         "Synthesis 101</a> for combining many causal studies. "
                         "<a href=\"/101-courses/cost-effectiveness.html\">Cost Effectiveness 101</a> for turning an "
                         "effect into a funding decision. <a href=\"/101-courses/toc-workbench.html\">Theory of "
                         "Change 101</a> for the causal story a programme assumes. "
                         "<a href=\"/101-courses/research-ethics.html\">Research Ethics 101</a> and "
                         "<a href=\"/101-courses/data-protection-dpdp.html\">Data Protection &amp; the DPDP Act "
                         "101</a> for running studies responsibly."}]},
             {"t": "hbox", "color": "amber", "html": "Suggested order: this deck, then Impact Evaluation 101, "
              "then Econometrics 101, then the flagship course."},
         ]},

        # ===================== S100 END =====================
        {"type": "end",
         "eyebrow": "Causal Inference 101 &middot; Complete",
         "headline": "Compared with whom?<br>Ask it every time.",
         "byline": "Every causal claim rests on a comparison and an assumption. Name both, check what can be "
                   "checked, and say plainly what cannot. Explore the rest of the ImpactMojo 101 Series, free "
                   "forever.",
         "ctas": [
             {"label": "Causal Inference Course", "href": "https://www.impactmojo.in/courses/causal/"},
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}


def _wrap_panel_html(blocks):
    """.col-panel is a flex column, so loose inline markup (<em>, <strong>) in a panel's
    html would become separate flex items on their own lines. Wrap it in one div."""
    for b in blocks:
        if b.get("t") == "panel" and "html" in b and not b["html"].startswith("<div>"):
            b["html"] = "<div>" + b["html"] + "</div>"
        for key in ("left", "right", "blocks"):
            if isinstance(b.get(key), list):
                _wrap_panel_html(b[key])


for _s in DECK["slides"]:
    _wrap_panel_html(_s.get("blocks", []))
