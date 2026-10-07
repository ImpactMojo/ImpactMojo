# -*- coding: utf-8 -*-
"""
Social Determinants of Health 101 - ImpactMojo 101 Series (native deck spec)
Why health follows the social ladder, how the WHO frameworks describe it, what
the South Asian surveys show by wealth, caste, tribe, gender, place and
schooling, the specific determinants (water, sanitation, housing, air, heat,
food, transport, violence, work), how health is paid for, the policy
responses, how inequity is measured, and an equity lens for practitioners.
Build: python3 scripts/deck-builder/build.py social_determinants_health

Sources opened while writing (October 2026) are named on the slides
themselves. Figures marked Illustrative are teaching examples.
"""


def C(label, title, blocks, **kw):
    s = {"type": "content", "label": label, "title": title, "blocks": blocks}
    s.update(kw)
    return s


def body(html, sm=False):
    b = {"t": "body", "html": html}
    if sm:
        b["cls"] = "sm"
    return b


def hbox(html, color="cyan"):
    return {"t": "hbox", "color": color, "html": html}


def term(word, d):
    return {"t": "term", "word": word, "def": d}


def bullets(items, color=None, sm=False):
    b = {"t": "bullets", "items": items}
    if color:
        b["color"] = color
    if sm:
        b["sm"] = True
    return b


def table(head, rows):
    return {"t": "table", "head": head, "rows": rows}


def flow(steps):
    return {"t": "flow", "steps": steps}


def panel(color, title, blocks):
    return {"t": "panel", "color": color, "title": title, "blocks": blocks}


def tw(left, right, ratio="half"):
    return {"t": "twocol", "ratio": ratio, "left": left, "right": right}


def pp(color, title, html):
    """A two-column half made of one panel holding small body text."""
    return [panel(color, title, [body(html, sm=True)])]


def stats(cards, cols=None):
    return {"t": "stats", "cols": cols or len(cards), "cards": cards}


def card(num, label, color, source):
    return {"num": num, "label": label, "color": color, "source": source}


def quote(text, attr):
    return {"t": "quote", "text": text, "attr": attr}


def D(num, label, title):
    return {"type": "divider", "num": num, "label": label, "title": title}


def bar(canvas, title, source, labels, series, ymax=None, ytitle="", horizontal=False):
    colors = ["#0EA5E9", "#F59E0B", "#10B981", "#6366F1", "#EF4444"]
    ds = []
    for i, (name, vals) in enumerate(series):
        ds.append({"label": name, "data": vals, "backgroundColor": colors[i % 5],
                   "borderRadius": 4})
    scale = "x" if horizontal else "y"
    lim = (", max:%s" % ymax) if ymax else ""
    opts = ("{ %s plugins:{legend:{display:%s}}, scales:{ %s:{ beginAtZero:true%s, "
            "title:{display:true,text:'%s'} } } }"
            % ("indexAxis:'y'," if horizontal else "",
               "true" if len(series) > 1 else "false", scale, lim, ytitle))
    return {"t": "chart", "canvas": canvas, "title": title, "source": source,
            "type": "bar", "data": {"labels": labels, "datasets": ds},
            "options": {"__js__": opts}}


NFHS = "NFHS-5 (2019-21) India Report, IIPS and ICF, 2022"
NFHS6 = "NFHS-6 (2023-24): India and State/UT Fact Sheets, IIPS, May 2026 (provisional)"
NFHS_T72 = NFHS + ", Table 7.2"
NFHS_T101 = NFHS + ", Table 10.1"
DHS_API = "DHS Program STATcompiler API, accessed October 2026"
CSDH = "WHO Commission on Social Determinants of Health, Closing the gap in a generation, 2008"
SOLAR = "Solar and Irwin, A conceptual framework for action on the social determinants of health, WHO, 2010"
NHA = "National Health Accounts Estimates for India 2022-23, NHSRC/MoHFW, via PIB, 27 May 2026"
NSS75 = "NSS 75th round (2017-18), Key Indicators of Social Consumption in India: Health, MoSPI, 2019"
JMP = "WHO/UNICEF JMP, via World Bank WDI, accessed October 2026"

DECK = {
    "slug": "social-determinants-health",
    "title": "Social Determinants of Health 101",
    "description": ("Social Determinants of Health 101: a free foundational course for development "
                    "practitioners in South Asia. The WHO Commission on Social Determinants of "
                    "Health and its three recommendations; the Solar and Irwin framework of "
                    "structural and intermediary determinants; the Dahlgren and Whitehead rainbow; "
                    "the 2025 World report on social determinants of health equity; Marmot and the "
                    "social gradient; NFHS-5 and DHS gaps by wealth, caste, tribe, gender, place and "
                    "schooling; water, sanitation, housing, air, heat, food, transport, violence and "
                    "work; out-of-pocket spending, National Health Accounts and PM-JAY; Health in "
                    "All Policies and proportionate universalism; concentration index and "
                    "PROGRESS-Plus; an equity lens for programmes. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== TITLE =====================
        {"type": "title",
         "main": "Social<br>Determinants<br>of Health 101",
         "sub": "Why health follows the social ladder in South Asia, how to measure the gap, "
                "and what programmes and policies can do about it",
         "tags": ["100 Slides", "South Asia Focus", "Free Forever", "Health Equity"]},

        # ===================== TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What we cover",
         "items": [
             {"name": "What the social determinants are"},
             {"name": "Three frameworks: CSDH, Solar and Irwin, the rainbow"},
             {"name": "The social gradient"},
             {"name": "South Asia: wealth, place and schooling"},
             {"name": "Caste, tribe and gender"},
             {"name": "Living conditions: water, sanitation, housing, air"},
             {"name": "Heat, food, roads, violence and work"},
             {"name": "Paying for health"},
             {"name": "Policy approaches"},
             {"name": "Measuring inequity"},
             {"name": "Practical application: an equity lens"},
             {"name": "Bringing it together"},
         ]},

        # ===================== SECTION 01 =====================
        D("01", "Section One", "What the social determinants are"),

        C("Starting point", "Most of what makes people ill happens outside the clinic", [
            body("A child in the poorest fifth of Indian households is about three times as "
                 "likely to die before age five as a child in the richest fifth. The child's "
                 "doctor did not cause that gap, and a better doctor alone will not close it. The "
                 "gap is produced by the water the family drinks, the fuel the mother cooks with, "
                 "her years of schooling, the debt a hospital bill creates, and the caste and "
                 "place the family was born into. These are the <strong>social determinants of "
                 "health</strong>."),
            tw(pp("cyan", "The working definition",
                  "The WHO Commission on Social Determinants of Health (2008) described them as "
                  "the circumstances in which people grow, live, work and age, and the systems "
                  "put in place to deal with illness. Those circumstances are in turn shaped by "
                  "political, social and economic forces."),
               pp("green", "Why a practitioner cares",
                  "A nutrition, sanitation or livelihoods programme is a health programme whether "
                  "or not it says so. Knowing the determinants tells you where your work changes "
                  "health, and for whom.")),
            hbox("Source for the opening comparison: under-five mortality of 59.0 (lowest wealth "
                 "quintile) against 20.1 (highest) per 1,000 live births, " + NFHS_T72 + ".",
                 "indigo"),
        ], compact=True),

        C("Definitions", "Inequality and inequity are different words for a reason", [
            tw([term("Health inequality",
                     "Any measured difference in health between groups: men and women, old and "
                     "young, rich and poor. Some inequalities are biological and expected. Older "
                     "people have more heart disease than younger people, and only women die in "
                     "childbirth.")],
               [term("Health inequity",
                     "A difference that is systematic, avoidable by reasonable action, and "
                     "therefore unfair. The CSDH wrote: 'Where systematic differences in health are "
                     "judged to be avoidable by reasonable action they are, quite simply, unfair. "
                     "It is this that we label health inequity.'")]),
            body("The distinction matters in practice. A programme that reports 'inequality in "
                 "anaemia' makes a descriptive claim. A programme that reports 'inequity' makes a "
                 "normative one and commits itself to explaining why the gap is avoidable. "
                 "Margaret Whitehead's paper 'The concepts and principles of equity and health' "
                 "(<em>International Journal of Health Services</em> 22(3), 1992) set out this "
                 "framing for the WHO European Region's Health for All policy, separating "
                 "differences that are inevitable from those that are unnecessary and unfair.",
                 sm=True),
            hbox("Rule of thumb: measure inequality, argue inequity. Your data show the first; your "
                 "reasoning about causes and remedies establishes the second.", "amber"),
        ], compact=True),

        C("The Commission", "The WHO Commission on Social Determinants of Health, 2005-2008", [
            body("WHO set up the Commission in 2005 to gather the evidence on what can be done "
                 "to promote health equity. Chaired by Michael Marmot, it published its final "
                 "report, <em>Closing the gap in a generation: health equity through action on the "
                 "social determinants of health</em>, in August 2008. Its executive summary "
                 "compared life chances across countries: a child could expect to live more than "
                 "80 years in Japan or Sweden, 72 in Brazil, 63 in India and fewer than 50 in "
                 "several African countries."),
            quote("Social injustice is killing people on a grand scale.",
                  "Executive summary, " + CSDH),
            tw(pp("cyan", "What it argued",
                  "'But poor health is not confined to those worst off. In countries at all levels of "
                  "income, health and illness follow a social gradient: the lower the "
                  "socioeconomic position, the worse the health.'"),
               pp("amber", "What it blamed",
                  "The report attributed health inequity to 'a toxic combination of poor social "
                  "policies and programmes, unfair economic arrangements, and bad politics', and "
                  "called for closing the gap within a generation.")),
        ], compact=True),

        C("Three recommendations", "The Commission's three overarching recommendations", [
            table(["Recommendation", "What it asks for", "A South Asian example of the lever"],
                  [["1. Improve daily living conditions",
                    "Wellbeing of girls and women, early child development, education, living "
                    "and working conditions, social protection across the life course",
                    "Anganwadi services, school meals, maternity benefits"],
                   ["2. Tackle the inequitable distribution of power, money and resources",
                    "Gender equity, a strong and adequately financed public sector, fair "
                    "financing, accountable governance from community to global level",
                    "Tax-financed health care, reservations in local government"],
                   ["3. Measure and understand the problem and assess the impact of action",
                    "National and global health equity surveillance, equity impact assessment, "
                    "training, research on social determinants",
                    "Disaggregated NFHS and SRS tables, equity analysis of schemes"]]),
            body("The three recommendations are ordered from the conditions people live in, to the "
                 "structures that distribute those conditions, to the evidence needed to act. Most "
                 "development programmes work on the first. The second is political and is often "
                 "left to governments, though advocacy and governance programmes act on it. The "
                 "third is where monitoring and evaluation teams contribute directly.", sm=True),
            hbox("Source: executive summary, " + CSDH + ", page 2.", "indigo"),
        ], compact=True),

        C("Twenty years on", "The 2025 World report on social determinants of health equity", [
            body("On 6 May 2025 WHO launched the <em>World report on social determinants of health "
                 "equity</em>, the first such global report since the Commission. Its news release "
                 "reported that the targets for 2040 the Commission had set for reducing gaps in life "
                 "expectancy and child and maternal mortality were likely to be missed."),
            stats([card("33 years", "gap in average life expectancy between the countries with "
                        "the lowest and highest", "red", "WHO news release, 6 May 2025"),
                   card("13&times;", "higher risk of dying before age five for children born in "
                        "poorer countries", "amber", "WHO news release, 6 May 2025"),
                   card("3.8 bn", "people without adequate social protection coverage", "cyan",
                        "WHO news release, 6 May 2025")], cols=3),
            body("The report grouped its calls for action into four areas: reduce economic "
                 "inequality through social infrastructure and universal services; overcome "
                 "structural discrimination and the health effects of conflict and forced "
                 "migration; manage climate action and digital change so that they benefit "
                 "equity; and govern for equity through cross-government platforms and community "
                 "participation.", sm=True),
        ], compact=True),

        C("Beyond poverty", "The determinants act on everyone, along a slope", [
            tw(pp("cyan", "A poverty view",
                  "Health problems are concentrated among the poor, so target the poor. This is "
                  "the logic of many schemes: identify a deprived group, deliver a service to it. "
                  "It reaches people in the worst conditions and is easy to explain."),
               pp("green", "A gradient view",
                  "Health improves at every step up the social ladder, including steps far above "
                  "poverty. In NFHS-5, under-five mortality falls from 59.0 in the lowest wealth "
                  "quintile to 48.0, 39.1, 32.7 and 20.1 in the next four (" + NFHS_T72 + "). "
                  "Even the fourth quintile does worse than the top.")),
            body("Solar and Irwin's 2010 framework names three broad policy approaches: targeted "
                 "programmes for disadvantaged groups, closing the gap between worse-off and "
                 "better-off groups, and addressing the gradient across the whole population. They "
                 "write that these 'are not mutually exclusive' and can build on each other, but "
                 "that a consistent equity approach must ultimately lead to a focus on gradients.",
                 sm=True),
            hbox("Implication: targeting the bottom quintile helps the people with the worst "
                 "outcomes, but most of the excess deaths across a population sit in the middle "
                 "quintiles too.", "amber"),
        ], compact=True),

        C("Why it matters here", "South Asia carries large gaps inside and between countries", [
            table(["Country", "Under-5 mortality, 2024 (per 1,000)", "Life expectancy, 2024 (years)"],
                  [["Sri Lanka", "5.9", "77.7"], ["Maldives", "5.4", "81.3"],
                   ["Bhutan", "17.2", "73.3"], ["Nepal", "25.1", "70.6"],
                   ["India", "26.6", "72.2"], ["Bangladesh", "30.5", "74.9"],
                   ["Pakistan", "56.0", "67.8"]]),
            body("Sources: UN Inter-agency Group for Child Mortality Estimation (indicator "
                 "SH.DYN.MORT) and World Bank life expectancy series (SP.DYN.LE00.IN), via World "
                 "Bank WDI, accessed October 2026. These are modelled estimates for comparison "
                 "across countries. For India itself, use the Sample Registration System: SRS 2023 "
                 "put under-five mortality at 29, ranging from 33 in rural areas to 20 in urban "
                 "areas (MoSPI, Children in India 2025, PIB, 25 September 2025).", sm=True),
            hbox("Sri Lanka's under-five mortality is about one-tenth of Pakistan's, at a far lower "
                 "income than Europe's. Differences of this size between neighbours point to "
                 "policy and social arrangements, which is the subject of this course.", "indigo"),
        ], compact=True),

        # ===================== SECTION 02 =====================
        D("02", "Section Two", "Three frameworks: CSDH, Solar and Irwin, the rainbow"),

        C("The CSDH framework", "Solar and Irwin: structural determinants work through intermediary ones", [
            body("The framework the Commission adopted was written up by Orielle Solar and Alec "
                 "Irwin as <em>A conceptual framework for action on the social determinants of "
                 "health</em> (WHO, Social Determinants of Health Discussion Paper 2, 2010). It "
                 "separates two layers of cause, and its vocabulary is meant to give the "
                 "structural factors causal priority."),
            flow(["CONTEXT: governance, macroeconomic, social and public policy, culture and "
                  "values",
                  "POSITION: class, gender, ethnicity, education, occupation, income",
                  "INTERMEDIARY: material, psychosocial, behavioural and biological, health "
                  "system",
                  "OUTCOME: the distribution of health and wellbeing"]),
            tw(pp("cyan", "Structural determinants",
                  "Context, the structural mechanisms that sort people into positions, and the "
                  "resulting socioeconomic position together form the 'social determinants of "
                  "health inequities'. They decide who gets which conditions of daily life."),
               pp("green", "Intermediary determinants",
                  "The conditions that act more directly on the body: housing, food, work "
                  "environment, stress and social support, smoking and diet, and access to "
                  "health care. These are the 'social determinants of health' in the narrow "
                  "sense.")),
            hbox("Source: " + SOLAR + ", pages 5-6 and Figure A.", "indigo"),
        ], compact=True),

        C("Structural determinants", "Context: the six things to map before you design anything", [
            body("Solar and Irwin define context as 'all social and political mechanisms that "
                 "generate, configure and maintain social hierarchies'. Among the most powerful "
                 "contextual factors they name the welfare state and its redistributive policies, "
                 "or their absence. They suggest that mapping context should cover at least six "
                 "points:"),
            table(["Point to map", "Indian example of what to look at"],
                  [["1. Governance and its processes", "Panchayat functioning, grievance redress, "
                    "civil society space, transparency of scheme data"],
                   ["2. Macroeconomic policy", "Fiscal space for health and nutrition, labour "
                    "market structure"],
                   ["3. Social policies (labour, welfare, land, housing)", "Labour Codes in force "
                    "since 21 November 2025, food entitlements, land records"],
                   ["4. Public policy in education, medical care, water and sanitation",
                    "Jal Jeevan Mission, Swachh Bharat, state health budgets"],
                   ["5. Culture and societal values", "Caste norms, son preference, purdah"],
                   ["6. Epidemiological conditions", "TB, heat waves, a pandemic"]]),
            body("Source: " + SOLAR + ", pages 24-25. The examples in the right column are this "
                 "course's, chosen to show how the six points translate in an Indian district.",
                 sm=True),
        ], compact=True),

        C("Socioeconomic position", "Six stratifiers, and why each needs its own measure", [
            body("Solar and Irwin list the most important structural stratifiers and their proxy "
                 "indicators as income, education, occupation, social class, gender and "
                 "race/ethnicity. In South Asia the last of these is best read as caste, tribe and "
                 "religion. Each stratifier captures a different route to health."),
            table(["Stratifier", "What it captures", "Usual measure in South Asian surveys"],
                  [["Income or wealth", "Command over goods, buffer against shocks",
                    "Asset-based wealth index (NFHS, DHS); consumption (HCES)"],
                   ["Education", "Knowledge, skills, bargaining power, future earnings",
                    "Years of schooling of mother or head of household"],
                   ["Occupation", "Work hazards, security, status",
                    "Main occupation; formal or informal; PLFS categories"],
                   ["Social class", "Position in relations of production", "Rarely measured "
                    "directly; proxied by occupation and land"],
                   ["Gender", "Unequal power and resources in household and society",
                    "Sex of individual; women's decision-making modules"],
                   ["Caste, tribe, religion", "Historical exclusion and discrimination",
                    "SC, ST, OBC, other; religion of head"]]),
            hbox("These stratifiers are correlated but not interchangeable. A Dalit household in "
                 "the top wealth quintile still faces caste discrimination, which is why analysts "
                 "report several stratifiers side by side.", "amber"),
        ], compact=True),

        C("Intermediary determinants", "Four channels that carry position into the body", [
            table(["Channel", "What Solar and Irwin include", "Example from NFHS, India"],
                  [["Material circumstances", "Housing and neighbourhood quality, consumption "
                    "potential (money for food and clothing), physical work environment",
                    "41% of households did not use clean cooking fuel"],
                   ["Psychosocial circumstances", "Stressors, stressful living conditions and "
                    "relationships, social support",
                    "22.3% of ever-married women aged 18-49 had ever experienced spousal "
                    "physical or sexual violence (NFHS-6)"],
                   ["Behavioural and biological factors", "Nutrition, physical activity, tobacco "
                    "and alcohol, genetic factors",
                    "36.3% of men and 8.4% of women aged 15+ use tobacco (NFHS-6)"],
                   ["The health system", "Access, exposure and vulnerability, intersectoral action "
                    "led from health", "60.2% of households had any member covered by a health "
                    "scheme or insurance (NFHS-6)"]]),
            body("Sources: categories from " + SOLAR + ", page 6. Figures marked NFHS-6 are from "
                 "the " + NFHS6 + "; the cooking-fuel figure is from " + NFHS + ", Chapter 2 (59% "
                 "of households use clean fuel), because the NFHS-6 fact sheet does not report it. Behaviour sits here, as a channel, because who smokes and what "
                 "people eat are distributed by social position.", sm=True),
        ], compact=True),

        C("The health system", "The health system is itself a determinant, and illness feeds back", [
            tw(pp("cyan", "Health care as a determinant",
                  "Solar and Irwin write that the CSDH framework 'departs from many previous "
                  "models by conceptualizing the health system itself as a social determinant of "
                  "health'. Who reaches care, how early, and at what cost is distributed by "
                  "position. The Commission's report said 'it is vital to minimize out-of-pocket "
                  "spending on health care'."),
               pp("amber", "Illness changes position",
                  "The framework includes a feedback loop. Illness 'can feed back on a given "
                  "individual's social position, e.g. by compromising employment opportunities "
                  "and reducing income'. A farm labourer with TB loses wages; a family that sells "
                  "land to pay a hospital drops a wealth quintile.")),
            body("The second point has a measurement consequence. When we see that the poor are "
                 "sicker, part of the association may run from illness to poverty. Panel data, "
                 "or measures of position taken before illness, help separate the two directions. "
                 "Diderichsen's model, on which the CSDH framework draws, names four mechanisms: "
                 "social stratification, differential exposure, differential vulnerability, and "
                 "differential consequences of ill health.", sm=True),
            hbox("Sources: " + SOLAR + ", pages 5-6 and 23-24; executive summary, " + CSDH + ".",
                 "indigo"),
        ], compact=True),

        C("The rainbow", "Dahlgren and Whitehead, 1991: the main determinants of health", [
            body("Goran Dahlgren and Margaret Whitehead drew their model in <em>Policies and "
                 "strategies to promote social equity in health</em>, a background document to a "
                 "WHO strategy paper for Europe, published in September 1991 by the Institute for "
                 "Futures Studies, Stockholm. It shows the main influences on health as layers, "
                 "'one on top of the other'."),
            table(["Layer (inner to outer)", "Contents in the 1991 figure"],
                  [["Core", "Age, sex and constitutional factors"],
                   ["1", "Individual lifestyle factors"],
                   ["2", "Social and community networks"],
                   ["3", "Living and working conditions: agriculture and food production, "
                    "education, work environment, unemployment, water and sanitation, health "
                    "care services, housing"],
                   ["4", "General socio-economic, cultural and environmental conditions"]]),
            body("The authors call the core 'fixed factors over which we have little control'. "
                 "The model was written to suggest 'quite distinct levels of intervention for "
                 "health policy-making', layer by layer. Their 2021 reflection, 'The "
                 "Dahlgren-Whitehead model of health determinants: 30 years on and still chasing "
                 "rainbows' (<em>Public Health</em> 199: 20-24), explains how they pair it with "
                 "the Diderichsen framework to explain gradients.", sm=True),
        ], compact=True),

        C("Choosing a model", "The rainbow and the CSDH framework answer different questions", [
            table(["", "Dahlgren and Whitehead (1991)", "Solar and Irwin / CSDH (2010)"],
                  [["Main question", "What influences health?", "Why is health unequally "
                    "distributed?"],
                   ["Shape", "Nested layers around the individual", "Causal chain from context "
                    "to outcome"],
                   ["Strength", "Easy to explain to a panchayat or a ministry; maps onto "
                    "sectors", "Puts power, policy and position at the start of the chain"],
                   ["Weakness", "Says little about how layers produce gradients", "Harder to "
                    "communicate; many boxes"],
                   ["Use it for", "Stakeholder mapping, intersectoral planning",
                    "Theory of change for an equity programme, evaluation design"]]),
            tw(pp("cyan", "In a district health plan",
                  "Use the rainbow to list which departments own each layer: agriculture, "
                  "education, rural development, Jal Shakti, health, housing."),
               pp("green", "In an evaluation",
                  "Use the CSDH chain to state which intermediary determinant your intervention "
                  "changes and for which socioeconomic position, then measure both.")),
        ], compact=True),

        C("Common ground", "What all three frameworks agree on", [
            tw([panel("cyan", "Agreement", [bullets([
                    "Health care matters, and most determinants lie outside it",
                    "Position in society shapes exposure and vulnerability",
                    "Policy choices set the conditions of daily life",
                    "Inequalities can be measured and should be monitored",
                    "Action has to cross sectors"], sm=True)])],
               [panel("amber", "Points of debate", [bullets([
                    "How much weight to give politics and power",
                    "Whether to target the poor or the whole gradient",
                    "How to treat behaviour: choice or circumstance",
                    "Social capital: useful idea or depoliticising one",
                    "Which stratifier to put first in a given country"], sm=True)])]),
            body("Solar and Irwin flag the social capital debate directly: a focus on social "
                 "capital, 'depending on interpretation, risks reinforcing depoliticized "
                 "approaches' to the social determinants. A community group that pools savings "
                 "for health emergencies helps its members, and it also leaves the public "
                 "financing gap unchanged. A practitioner should know which of the two the "
                 "programme is claiming to fix.", sm=True),
            hbox("Pick one framework per project, state it in the design document, and use its "
                 "terms consistently in indicators and reports.", "indigo"),
        ], compact=True),

        # ===================== SECTION 03 =====================
        D("03", "Section Three", "The social gradient"),

        C("Whitehall I", "Whitehall: the civil servants who changed the question", [
            body("The first Whitehall study, begun in 1967, followed 17,530 civil servants working "
                 "in London. All were employed by the same organisation, in one city, on regular "
                 "salaries, so few were poor in the usual sense. Yet after seven and a half years of "
                 "follow-up, men in the lowest employment grade (messengers) had 3.6 times the "
                 "coronary heart disease mortality of men in the highest grade (administrators)."),
            stats([card("17,530", "civil servants in the first Whitehall study", "cyan",
                        "Marmot et al., J Epidemiol Community Health 32(4), 1978"),
                   card("3.6&times;", "coronary heart disease mortality, lowest grade against "
                        "highest, at 7.5 years", "red",
                        "Marmot et al., J Epidemiol Community Health 32(4), 1978"),
                   card("3&times;", "mortality from coronary disease, other causes and all "
                        "causes, lowest grade, 10 years", "amber",
                        "Marmot, Shipley and Rose, Lancet, 5 May 1984")], cols=3),
            body("Lower grades smoked more, were shorter, heavier and had higher blood pressure. "
                 "But when the authors allowed for all of these and cholesterol, 'the inverse "
                 "association between grade of employment and CHD mortality was still strong'. "
                 "Risk factors explained only part of the gap.", sm=True),
        ], compact=True),

        C("Whitehall II", "Whitehall II: the gradient did not narrow in twenty years", [
            body("Between 1985 and 1988 Michael Marmot and colleagues recruited a new cohort of "
                 "10,314 civil servants (6,900 men and 3,414 women) aged 35-55. Reporting in "
                 "<em>The Lancet</em> on 8 June 1991, they found that 'in the 20 years separating "
                 "the two studies there has been no diminution in social class difference in "
                 "morbidity'."),
            tw(pp("cyan", "What they measured",
                  "Angina, ischaemia on ECG, chronic bronchitis and self-rated health were all "
                  "worse in lower grades. So were smoking, diet and exercise, height (a marker "
                  "of early-life conditions), economic circumstances, and work characterised by "
                  "low control and low satisfaction."),
               pp("green", "Smoking by grade, men",
                  "Moving from the lowest to the highest of six grades, current smoking among "
                  "men was 33.6%, 21.9%, 18.4%, 13.0%, 10.2% and 8.3% (Whitehall II figures "
                  "quoted in " + SOLAR + ", page 38). The behaviour itself is graded.")),
            hbox("The authors concluded that more attention should be paid 'to the social "
                 "environments, job design, and the consequences of income inequality', alongside "
                 "encouraging healthy behaviour across the whole of society.", "indigo"),
        ], compact=True),

        C("Why a gradient", "Three explanations for a gradient, and what each implies", [
            table(["Explanation", "The mechanism", "What it predicts", "Policy implication"],
                  [["Material", "Money buys food, housing, safe work, care",
                    "Gaps close when incomes and services improve",
                    "Cash transfers, public services"],
                   ["Psychosocial", "Low control, insecurity and subordination cause chronic "
                    "stress", "A gradient even among the securely employed",
                    "Job design, security, voice"],
                   ["Life course", "Disadvantage in early life accumulates",
                    "Adult height and early nutrition predict adult disease",
                    "Early childhood, maternal nutrition"]]),
            body("Whitehall was useful because it reduced the material explanation without "
                 "removing it: all the men had jobs and pensions, so a gradient that persisted "
                 "pointed to control, status and early life as well. The 1984 paper noted that "
                 "'the inverse relation between height and mortality suggests that factors "
                 "operating from early life may influence adult death rates' (Marmot, Shipley "
                 "and Rose, <em>Lancet</em> 1984).", sm=True),
            hbox("In South Asia, with large material deprivation, the material explanation "
                 "carries more weight than in London. The other two still apply, and caste adds a "
                 "fourth: status assigned at birth.", "amber"),
        ], compact=True),

        C("A gradient in India", "Under-five mortality falls at every step of the wealth ladder", [
            bar("sdhU5Wealth", "Under-five mortality by household wealth quintile, India, NFHS-5 "
                "(per 1,000 live births, 5 years before the survey)", NFHS_T72,
                ["Lowest", "Second", "Middle", "Fourth", "Highest"],
                [("Under-five mortality", [59.0, 48.0, 39.1, 32.7, 20.1])], ytitle="Deaths per 1,000"),
            body("Each quintile does better than the one below it. The step from fourth to "
                 "highest (32.7 to 20.1) is as large as the step from lowest to second (59.0 to "
                 "48.0). This is the shape the Commission called a social gradient. A programme "
                 "that defines its target group as 'below the poverty line' covers part of the "
                 "first two bars and none of the rest. The NFHS-5 wealth index ranks households "
                 "by their assets and housing, so it measures relative position; it says nothing "
                 "about how far apart the quintiles are in money.", sm=True),
        ], compact=True),

        C("Marmot Review", "England's version: seven years of life, seventeen of disability-free life", [
            body("In 2008 the UK Health Secretary asked Michael Marmot, who had chaired the "
                 "Commission, to apply its findings to England. The result was <em>Fair Society, "
                 "Healthy Lives</em> (the Marmot Review, 2010)."),
            stats([card("7 years", "gap in life expectancy between the poorest and richest "
                        "neighbourhoods in England", "red", "Fair Society, Healthy Lives, 2010"),
                   card("17 years", "gap in disability-free life expectancy between the same "
                        "neighbourhoods", "amber", "Fair Society, Healthy Lives, 2010"),
                   card("6 years", "gap even after excluding the poorest and richest 5%", "cyan",
                        "Fair Society, Healthy Lives, 2010")], cols=3),
            body("The third number is the argument for a gradient: removing both extremes still "
                 "leaves a six-year gap in life expectancy between low and high income. The "
                 "review's response was proportionate universalism, which Section 9 explains. The "
                 "review also notes that people in poorer areas die sooner and spend more of their "
                 "shorter lives with a disability.", sm=True),
        ], compact=True),

        C("Reading gradients", "Four ways a gradient can mislead you", [
            tw([panel("red", "Traps", [bullets([
                    "Reverse causation: illness lowers income and wealth",
                    "Confounding: wealth tracks caste, place and schooling",
                    "Composition: quintiles differ in age, region, family size",
                    "Small groups: wide confidence intervals at the extremes"], sm=True)])],
               [panel("green", "Responses", [bullets([
                    "Use position measured before the outcome where possible",
                    "Show stratifiers jointly, for example wealth within caste",
                    "Standardise for age and region before comparing",
                    "Report intervals and unweighted counts with every rate"], sm=True)])]),
            body("NFHS-5 marks estimates based on 250-499 unweighted person-years of exposure in "
                 "parentheses (Table 7.2 note, " + NFHS +
                 "). In the urban caste rows, for example, the 'Don't know' group's under-five "
                 "mortality of 78.2 is in parentheses. A practitioner who quotes that figure "
                 "without the warning overstates what is known.", sm=True),
            hbox("A gradient is a description. Turning it into a causal claim needs the methods "
                 "in Impact Evaluation 101 and Causal Inference 101.", "indigo"),
        ], compact=True),

        # ===================== SECTION 04 =====================
        D("04", "Section Four", "South Asia: wealth, place and schooling"),

        C("The newest round", "NFHS-6 (2023-24): what the first fact sheet shows", [
            table(["India, % (NFHS-6 urban / rural / total)", "Urban", "Rural", "NFHS-6 total",
                   "NFHS-5 total"],
                  [["Children under 5 stunted", "23.9", "30.9", "29.3", "35.5"],
                   ["Households with a member covered by a health scheme or insurance", "56.4",
                    "62.0", "60.2", "41.0"],
                   ["Ever-married women 18-49 who experienced spousal violence", "17.5", "24.4",
                    "22.3", "29.2"],
                   ["Women 15+ with high blood sugar or on medication", "21.9", "16.2", "17.8",
                    "13.5"],
                   ["Women with 10 or more years of schooling", "61.5", "39.7", "46.4", "41.0"],
                   ["Women 20-24 married before age 18", "11.4", "23.3", "20.1", "23.3"]]),
            body("Source: " + NFHS6 + ". Fieldwork ran from 28 May 2023 to 31 December 2024 and "
                 "covered 679,238 households, 716,397 women and 100,977 men. IIPS describes the "
                 "fact-sheet results as provisional. As of October 2026 the full report with "
                 "breakdowns by caste, wealth quintile and schooling, and the anaemia estimates, "
                 "had not been released. This course therefore uses NFHS-6 for headline levels "
                 "and NFHS-5 (2019-21) for gaps between groups, and labels each figure with its "
                 "round.", sm=True),
            hbox("Not every gradient runs the same way. High blood sugar among women is more "
                 "common in urban (21.9%) than rural (16.2%) areas, while stunting runs the other "
                 "way. The determinants of chronic disease, such as diet and physical activity, "
                 "are distributed differently from those of undernutrition.", "amber"),
        ], compact=True),

        C("Wealth and survival", "The wealth gap in child survival in four South Asian countries", [
            bar("sdhU5Four", "Under-five mortality, poorest and richest wealth quintiles (per 1,000 "
                "live births, 10 years before each survey)", DHS_API + "; India NFHS-5 2019-21, "
                "Bangladesh DHS 2022, Nepal DHS 2022, Pakistan DHS 2017-18",
                ["India", "Bangladesh", "Nepal", "Pakistan"],
                [("Lowest quintile", [58, 54, 53, 100]), ("Highest quintile", [22, 28, 16, 56])],
                ytitle="Deaths per 1,000"),
            body("All four countries show the same direction, with different scales. Pakistan's "
                 "richest quintile has higher under-five mortality (56) than India's or Nepal's "
                 "poorest. Breakdowns by background characteristic in DHS reports use the ten "
                 "years before the survey, to have enough births in each group, so these figures "
                 "differ slightly from the five-year national rates. The Pakistan survey is the "
                 "most recent DHS available for that country in the API, fielded in 2017-18, so "
                 "compare it with care.", sm=True),
        ], compact=True),

        C("The full gradient", "Wealth quintile by quintile: the shape differs by country", [
            table(["Under-5 mortality (10 years)", "Lowest", "Second", "Middle", "Fourth", "Highest"],
                  [["India, NFHS-5 2019-21", "58", "49", "40", "32", "22"],
                   ["Bangladesh, DHS 2022", "54", "43", "38", "27", "28"],
                   ["Nepal, DHS 2022", "53", "50", "30", "28", "16"],
                   ["Pakistan, DHS 2017-18", "100", "82", "82", "58", "56"]]),
            body("Source: " + DHS_API + ", indicator CM_ECMR_C_U5M by wealth quintile. India's is "
                 "a smooth staircase. Bangladesh flattens at the top: the fourth and highest "
                 "quintiles are about the same. Nepal has a jump between the second and middle "
                 "quintiles. Pakistan has two plateaus. Each shape suggests a different policy "
                 "question.", sm=True),
            tw(pp("cyan", "A staircase (India)",
                  "Suggests a gradient across the whole population: universal services with "
                  "intensity that rises towards the bottom."),
               pp("amber", "A cliff (Nepal, Pakistan)",
                  "Suggests a threshold, for example a group cut off from facilities or roads, "
                  "where a targeted push could close much of the gap.")),
        ], compact=True),

        C("Stunting", "Stunting halves between the poorest and richest fifth", [
            bar("sdhStuntFour", "Children under five who are stunted, poorest and richest wealth "
                "quintiles (%)", DHS_API + "; NFHS-5 2019-21, BDHS 2022, NDHS 2022, PDHS 2017-18",
                ["India", "Bangladesh", "Nepal", "Pakistan"],
                [("Lowest quintile", [46.1, 34.3, 36.9, 56.5]),
                 ("Highest quintile", [22.9, 15.2, 13.1, 22.0])], ytitle="% stunted"),
            body("Stunting (height-for-age more than two standard deviations below the WHO "
                 "median) records years of poor nutrition, infection and care. In India, 46.1% of "
                 "children in the lowest quintile are stunted against 22.9% in the highest (" +
                 NFHS_T101 + "). The ratio is about 2 in India and about 2.8 in Nepal. Notice that "
                 "nearly one child in four is stunted even in India's richest fifth: the "
                 "determinants of stunting, such as sanitation in the neighbourhood and mothers' "
                 "own height and nutrition, are shared across income groups.", sm=True),
            hbox("Newer round: NFHS-6 (2023-24) puts stunting in India at 29.3%, down from 35.5% in "
                 "NFHS-5, with 23.9% in urban and 30.9% in rural areas (" + NFHS6 + "). Its "
                 "breakdown by wealth quintile had not been published as of October 2026, so the "
                 "quintile comparison above uses NFHS-5.", "green"),
        ], compact=True),

        C("Place", "Rural children face higher risk in every country", [
            table(["Under-5 mortality", "Urban", "Rural", "Source"],
                  [["India (5 years)", "31.5", "45.7", NFHS_T72],
                   ["India, 2023", "20", "33", "SRS Statistical Report 2023, via PIB, 25 Sep 2025"],
                   ["Bangladesh (10 years)", "33", "41", "BDHS 2022, " + DHS_API],
                   ["Nepal (10 years)", "31", "50", "NDHS 2022, " + DHS_API],
                   ["Pakistan (10 years)", "63", "85", "PDHS 2017-18, " + DHS_API]]),
            body("Place works through several channels at once: distance to a facility and to a "
                 "doctor who is present, quality of water and sanitation, road access in an "
                 "emergency, and the income structure of rural labour markets. The urban figure "
                 "is an average that hides slums, which Section 6 takes up. Notice also that two "
                 "Indian sources for the same idea give different levels: NFHS-5 covers the five "
                 "years to 2019-21 and SRS measures 2023. Never mix them in one comparison.",
                 sm=True),
            hbox("Rural disadvantage in Nepal (31 against 50) is wider than in Bangladesh (33 "
                 "against 41). Geography, from Himalayan districts to the Tarai, is a determinant "
                 "in its own right.", "amber"),
        ], compact=True),

        C("States", "A child's state of birth changes the odds tenfold", [
            bar("sdhStates", "Under-five mortality by selected state, NFHS-5 (per 1,000 live "
                "births, 5 years before the survey)", NFHS + ", Table 7.4",
                ["Kerala", "Goa", "Tamil Nadu", "Assam", "Jharkhand", "Madhya Pradesh",
                 "Chhattisgarh", "Bihar", "Uttar Pradesh"],
                [("Under-five mortality", [5.2, 10.6, 22.3, 39.1, 45.4, 49.2, 50.4, 56.4, 59.8])],
                ytitle="Deaths per 1,000", horizontal=True),
            body("Kerala's 5.2 against Uttar Pradesh's 59.8 is a gap of more than eleven times "
                 "inside one country, one constitution and one national health mission. Solar "
                 "and Irwin cite Kerala as a widely studied case showing the relationship between "
                 "a reduction of inequalities over 40 years and improvements in health status, "
                 "and note that these gains have rarely been traced to the state's public "
                 "policies. State differences in schooling, women's status, public services and "
                 "political history are determinants that sit above any single household.",
                 sm=True),
        ], compact=True),

        C("Urban slums", "The 2011 Census counted 6.5 crore people in slums", [
            stats([card("6,54,94,604", "people enumerated in slums", "red",
                        "Primary Census Abstract for Slum, Census 2011, ORGI, 2013"),
                   card("17.4%", "of the urban population lived in slums", "amber",
                        "Primary Census Abstract for Slum, Census 2011, ORGI"),
                   card("1.39 crore", "slum households (1,39,20,191)", "cyan",
                        "Primary Census Abstract for Slum, Census 2011, ORGI")], cols=3),
            body("The Census counted notified, recognised and identified slums. The central law, "
                 "Section 3 of the Slum Areas (Improvement and Clearance) Act, 1956, lets an area be "
                 "declared a slum where its buildings 'are in any respect unfit for human "
                 "habitation', or where dilapidation, overcrowding, faulty arrangement of streets, "
                 "lack of ventilation, light or sanitation facilities, or any combination of these, "
                 "make them 'detrimental to safety, health or morals'. The statutory test is "
                 "itself a list of social determinants.", sm=True),
            tw(pp("cyan", "What the urban average hides",
                  "A city-wide child mortality or immunisation rate mixes planned colonies "
                  "with notified, recognised and identified slums. Disaggregate by slum status "
                  "wherever the sample allows."),
               pp("amber", "Who lives there",
                  "Scheduled Castes were 20.4% of the slum population against 12.6% of the "
                  "urban population (ORGI data, in NBO, Slums in India: A Statistical "
                  "Compendium, 2015). Place and caste overlap.")),
        ], compact=True),

        C("Schooling", "A mother's schooling is one of the strongest predictors of child health", [
            table(["Mother's schooling (India, NFHS-5)", "Under-5 mortality (per 1,000)",
                   "Children stunted (%)"],
                  [["No schooling", "60.3", "46.3"], ["Less than 5 years", "48.4", "42.1"],
                   ["5-7 years", "46.0", "40.1"], ["8-9 years", "43.0", "35.6"],
                   ["10-11 years", "33.8", "31.0"], ["12 or more years", "24.9", "25.7"]]),
            body("Sources: " + NFHS_T72 + " (mortality by schooling of the mother, 5 years before "
                 "the survey) and Table 10.1 (stunting). The gradient appears in neighbours too: "
                 "stunting among children of mothers with no education against those with higher "
                 "education is 39.3% against 13.2% in Bangladesh (BDHS 2022), 36.3% against 12.0% "
                 "in Nepal (NDHS 2022) and 47.6% against 15.8% in Pakistan (PDHS 2017-18), per " +
                 DHS_API + ".", sm=True),
            hbox("Schooling works through knowledge, but also through a woman's say over money, "
                 "food and care-seeking, through her age at marriage, and through the wealth that "
                 "schooling tends to bring. Its effect is partly its own and partly a marker of "
                 "the rest. Women with 10 or more years of schooling rose from 41.0% (NFHS-5) to "
                 "46.4% (NFHS-6, 2023-24).", "indigo"),
        ], compact=True),

        C("Poverty and longevity", "An IIPS estimate: the multidimensionally poor live four years less", [
            body("J. Das and S.K. Mohanty of the International Institute for "
                 "Population Sciences, Mumbai, used NFHS-5 microdata on 636,699 households and "
                 "2,843,917 individuals to build life tables separately for people who are "
                 "multidimensionally poor and those who are not (<em>BMC Public Health</em> 24: "
                 "3546, December 2024)."),
            stats([card("26%", "estimated multidimensional poverty in India, NFHS-5", "amber",
                        "Das and Mohanty, BMC Public Health, 2024"),
                   card("65.2 vs 69.0", "life expectancy at birth, poor and non-poor (years)",
                        "red", "Das and Mohanty, BMC Public Health, 2024"),
                   card("0.33 vs 0.25", "probability of dying before age 70, poor and non-poor",
                        "cyan", "Das and Mohanty, BMC Public Health, 2024")], cols=3),
            body("The authors found the gap in life expectancy at birth was larger among urban "
                 "dwellers (4.6 years) than rural (1.8 years), and that differences were larger by "
                 "residence than by caste and religion. A measure of deprivation that combines "
                 "education, health and living standards captures several determinants at once, "
                 "which is why it predicts longevity.", sm=True),
        ], compact=True),

        # ===================== SECTION 05 =====================
        D("05", "Section Five", "Caste, tribe and gender"),

        C("Caste and survival", "Scheduled Caste and Scheduled Tribe children die younger", [
            bar("sdhU5Caste", "Under-five mortality by caste or tribe of the household head, India, "
                "NFHS-5 (per 1,000 live births, 5 years before the survey)", NFHS_T72,
                ["Scheduled Caste", "Scheduled Tribe", "Other Backward Class", "Other"],
                [("Under-five mortality", [48.9, 50.3, 40.5, 32.8])], ytitle="Deaths per 1,000"),
            body("A Scheduled Tribe child faces an under-five mortality of 50.3 per 1,000, about "
                 "one and a half times the 32.8 of a child in the 'Other' group. Scheduled Caste "
                 "children are close behind at 48.9. Caste and tribe work through several "
                 "routes: land and asset ownership shaped by history, segregated settlements with "
                 "poorer water and roads, discrimination in schools and health facilities, and, "
                 "for many Adivasi communities, distance and forest geography. Caste Studies 101 "
                 "covers the history and law.", sm=True),
        ], compact=True),

        C("Caste within place", "The caste gap survives inside rural and urban areas", [
            table(["Under-5 mortality, NFHS-5", "Urban", "Rural", "Total"],
                  [["Scheduled Caste", "39.0", "51.9", "48.9"],
                   ["Scheduled Tribe", "35.5", "52.2", "50.3"],
                   ["Other Backward Class", "29.9", "44.4", "40.5"],
                   ["Other", "26.3", "36.6", "32.8"],
                   ["Total", "31.5", "45.7", "41.9"]]),
            body("Source: " + NFHS_T72 + ". A sceptic might say caste gaps are just rural-urban "
                 "gaps, because SC and ST households are more often rural. The table answers "
                 "this partly: within urban areas, SC children face 39.0 against 26.3 for 'Other'; "
                 "within rural areas, 51.9 against 36.6. Place explains some of the caste gap and "
                 "leaves most of it standing.", sm=True),
            tw(pp("cyan", "Stratify jointly",
                  "Cross-tabulating two stratifiers is the simplest way to see whether one gap "
                  "is a disguised version of another."),
               pp("amber", "Mind the sample",
                  "Cross-tabulations thin the cells fast. In the urban table, the small "
                  "'Don't know' caste group is flagged in parentheses for that reason.")),
        ], compact=True),

        C("Nutrition by caste", "Stunting and anaemia: steep in one, shallow in the other", [
            table(["NFHS-5, India", "Children stunted (%)", "Women 15-49 with anaemia (%)"],
                  [["Scheduled Caste", "39.2", "59.2"], ["Scheduled Tribe", "40.9", "64.6"],
                   ["Other Backward Class", "34.8", "54.6"], ["Other", "30.1", "56.4"],
                   ["Lowest wealth quintile", "46.1", "63.7"],
                   ["Highest wealth quintile", "22.9", "51.0"],
                   ["Total", "35.5", "57.0"]]),
            body("Sources: " + NFHS_T101 + " and Table 10.23.1. Stunting has a clear caste and "
                 "wealth gradient. Anaemia among women is high everywhere: even in the richest "
                 "fifth, half of women are anaemic, and 'Other' caste women (56.4%) are slightly "
                 "more often anaemic than OBC women (54.6%). Scheduled Tribe women stand out at "
                 "64.6%.", sm=True),
            hbox("A shallow gradient on a high base is the case for a universal programme with "
                 "extra intensity for the worst-off groups, here ST women. A steep gradient is the "
                 "case for directing effort down the ladder.", "amber"),
        ], compact=True),

        C("Intersections", "IIPS research: who is anaemic depends on several identities at once", [
            body("B. Das (IIT Guwahati), M. Adhikary (Department of Public Health and Mortality "
                 "Studies, IIPS Mumbai) and colleagues analysed NFHS-5 with an explicitly intersectional "
                 "approach in 'Who is Anaemic in India? Intersections of class, caste, and "
                 "gender' (<em>Journal of Biosocial Science</em> 56(4): 731-753, 2024). They "
                 "argued that much research uses a 'single-axis analytical framework', treating "
                 "gender, class and caste as separate categories."),
            tw(pp("cyan", "Their finding",
                  "ST and SC women 'share a disproportionate burden of anaemia', and those who "
                  "are economically marginalised and live in rural areas with high poverty, "
                  "exclusion and poor nutritional status have a higher prevalence than other "
                  "groups."),
               pp("green", "For a programme",
                  "Report outcomes for combinations, for example rural ST women in the poorest "
                  "two quintiles, in addition to each stratifier in turn. A group can be "
                  "invisible in every single-axis table and still be the worst off.")),
            hbox("Intersectional analysis needs large samples. NFHS-5 interviewed 724,115 women, "
                 "which is what makes such cross-cuts possible (" + NFHS + ", Chapter 1).",
                 "indigo"),
        ], compact=True),

        C("Missing women", "Sen, 1990: more than 100 million women are missing", [
            body("In the <em>New York Review of Books</em> of 20 December 1990, Amartya Sen observed "
                 "that in Europe and North America 'the ratio of women to men is typically around "
                 "1.05 or 1.06, or higher'. 'In South Asia, West Asia, and China, the ratio of women to men "
                 "can be as low as 0.94, or even lower.' Comparing actual numbers with the "
                 "expected ones, he concluded that 'a great many more than 100 million women' were "
                 "missing."),
            stats([card("904", "girls born per 1,000 boys, India, 2017-19", "amber",
                        "SRS, in MoSPI Women and Men in India 2025, PIB, 29 Apr 2026"),
                   card("917", "girls born per 1,000 boys, India, 2021-23", "green",
                        "SRS, in MoSPI Women and Men in India 2025, PIB, 29 Apr 2026")], cols=2),
            body("Gender is a social determinant that acts before birth through sex selection, "
                 "and after birth through feeding, care-seeking and spending on girls and women. "
                 "The rise from 904 to 917 is welcome, and the ratio is still below what a "
                 "population without selection would show. Gender & Development 101 covers the "
                 "measures and the law in detail.", sm=True),
        ], compact=True),

        C("Violence", "Spousal violence follows wealth, schooling and caste", [
            table(["Ever-married women 18-49, NFHS-5", "Physical or sexual spousal violence (%)"],
                  [["Lowest wealth quintile", "38.4"], ["Highest wealth quintile", "16.9"],
                   ["No schooling", "38.1"], ["12 or more years of schooling", "17.7"],
                   ["Scheduled Caste", "34.7"], ["Scheduled Tribe", "31.8"],
                   ["Other Backward Class", "30.2"], ["Other", "22.6"],
                   ["All women", "29.2"]]),
            body("Source: " + NFHS + ", Table 15.11. Violence is a determinant of physical injury, "
                 "mental health, reproductive health and children's health, and it is itself "
                 "socially patterned. The NFHS-5 key findings add that one-fourth of women who "
                 "experienced spousal physical or sexual violence reported injuries, and 'only 14 "
                 "percent of women who have experienced physical or sexual violence by anyone have "
                 "sought help'. The newer NFHS-6 (2023-24) fact sheet reports 22.3% for all "
                 "ever-married women (17.5% urban, 24.4% rural), down from 29.2%; its breakdown by "
                 "caste and wealth is not yet published, so the table uses NFHS-5.", sm=True),
            hbox("The gradient does not mean violence is a problem only of poor households: one "
                 "woman in six in the richest fifth reports it. Design for universal access to "
                 "help, and for extra outreach where rates are highest.", "amber"),
        ], compact=True),

        C("Religion", "A puzzle that warns against assuming the direction of a gap", [
            table(["Under-5 mortality, India, NFHS-5", "Per 1,000 live births"],
                  [["Hindu", "42.8"], ["Muslim", "39.2"], ["Sikh", "33.5"],
                   ["Buddhist/Neo-Buddhist", "32.4"], ["Christian", "31.5"], ["Total", "41.9"]]),
            body("Source: " + NFHS_T72 + ". In NFHS-5, Hindu and Muslim households are spread almost "
                 "evenly across wealth quintiles: 20.5% of people in Hindu-headed households and "
                 "19.6% in Muslim-headed households are in the lowest quintile (Table 2.9). Yet "
                 "Muslim children's under-five mortality (39.2) is lower than Hindu children's "
                 "(42.8). The difference runs that way in rural areas (42.9 against 46.6) and "
                 "reverses slightly in urban areas (32.8 against 31.7). Contrast caste: 46.3% of "
                 "people in Scheduled Tribe households are in the lowest quintile, against 11.3% "
                 "in 'Other' households."),
            tw(pp("cyan", "The lesson for analysis",
                  "Do not predict the direction of a gap from a group's average position on "
                  "other measures. Look at the data for the outcome you care about."),
               pp("amber", "The lesson for reporting",
                  "Religion and caste data are sensitive. Report them to show where services "
                  "fall short, with care that the numbers cannot be used to stigmatise a "
                  "community.")),
        ], compact=True),

        C("Using identity data", "Collecting caste, tribe and religion responsibly", [
            tw([panel("cyan", "Why collect it", [bullets([
                    "Gaps by caste and tribe are large and persist within place and wealth",
                    "Schemes target SC and ST households explicitly (PM-JAY's D5 criterion)",
                    "Without the data, exclusion cannot be shown or fixed",
                    "The Census 2027, with reference date 1 March 2027, includes caste "
                    "enumeration"], sm=True)])],
               [panel("amber", "How to collect it", [bullets([
                    "Ask in the survey's standard categories so results compare with NFHS",
                    "Explain the purpose; allow 'prefer not to say'",
                    "Store identity variables separately from names",
                    "Report only aggregates large enough to protect individuals"], sm=True)])]),
            body("India's Digital Personal Data Protection Act, 2023 commences in stages under "
                 "G.S.R. 843(E) of 13 November 2025. Definitions and the Data Protection Board "
                 "(ss 18-26) are in force; the core duties and rights in ss 3-17, including the "
                 "s17(2)(b) exemption for research and statistical processing, apply only from 13 "
                 "May 2027. Treat those duties as the standard to prepare for now. Data "
                 "Protection & the DPDP Act 101 and Research Ethics 101 cover consent and "
                 "safeguards.", sm=True),
        ], compact=True),

        # ===================== SECTION 06 =====================
        D("06", "Section Six", "Living conditions: water, sanitation, housing, air"),

        C("Water and sanitation", "Water and sanitation across South Asia, 2024", [
            table(["2024, % of population", "At least basic drinking water",
                   "At least basic sanitation", "Safely managed sanitation", "Open defecation"],
                  [["India", "95.7", "83.4", "62.8", "6.7"],
                   ["Bangladesh", "98.8", "67.6", "37.3", "0.0"],
                   ["Nepal", "93.6", "86.0", "53.4", "0.5"],
                   ["Pakistan", "90.7", "71.9", "n/a", "8.2"],
                   ["Sri Lanka", "90.2", "95.4", "n/a", "0.0"]]),
            body("Source: " + JMP + " (indicators SH.H2O.BASW.ZS, SH.STA.BASS.ZS, SH.STA.SMSS.ZS, "
                 "SH.STA.ODFC.ZS). 'Basic' sanitation means an improved facility not shared with "
                 "other households. 'Safely managed' adds that excreta are safely disposed of in "
                 "place or treated off-site. The ladder matters: Bangladesh has almost eliminated "
                 "open defecation, yet only about a third of its people have safely managed "
                 "sanitation. A toilet that empties into an open drain still contaminates the "
                 "neighbourhood.", sm=True),
            hbox("Sanitation is a neighbourhood good. A child's risk of diarrhoea and stunting "
                 "depends on whether the neighbours' faeces are contained, which is why household "
                 "wealth alone does not protect against it.", "indigo"),
        ], compact=True),

        C("Open defecation", "India's open defecation fell from 73% to 7% of the population", [
            {"t": "chart", "canvas": "sdhOdf",
             "title": "Population practising open defecation, India, 2000-2024 (%)",
             "source": JMP + ", indicator SH.STA.ODFC.ZS",
             "type": "line",
             "data": {"labels": ["2000", "2004", "2008", "2012", "2014", "2016", "2018", "2020",
                                 "2022", "2024"],
                      "datasets": [{"label": "Open defecation (%)",
                                    "data": [73.2, 61.5, 50.1, 38.8, 33.3, 27.8, 22.4, 17.0,
                                             11.7, 6.7],
                                    "borderColor": "#0EA5E9",
                                    "backgroundColor": "rgba(14,165,233,0.10)",
                                    "fill": True, "tension": 0.2, "pointRadius": 4}]},
             "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:80, title:{display:true,text:'% of population'} } } }"}},
            body("JMP estimates are modelled from household surveys, so the series moves smoothly; it "
                 "shows a fall that began well before 2014 and continued after 2019. "
                 "In rural India the 2024 figure was still 10.7% (indicator SH.STA.ODFC.RU.ZS). The "
                 "national average hides where the remaining open defecation is concentrated: in "
                 "rural areas, and in households without space, water or money to maintain a "
                 "toilet.", sm=True),
        ], compact=True),

        C("Swachh Bharat", "Swachh Bharat Mission: what administrative data and surveys each say", [
            tw(pp("cyan", "The administrative record",
                  "Swachh Bharat Mission (Grameen) was launched on 2 October 2014 with the aim of "
                  "an open defecation free India by 2 October 2019. The Department of Drinking "
                  "Water and Sanitation reports that rural sanitation coverage rose 'from 39% in "
                  "2014 to 100% in 2019', and that more than 12 crore household latrines had been "
                  "built by 16 December 2025 (Department of Drinking Water and Sanitation, Year End Review 2025, PIB, 1 January 2026)."),
               pp("amber", "The surveys",
                  "JMP estimates 19.7% of India's population practised open defecation in 2019. "
                  "NFHS-5 (2019-21) found 19% of households had no facility and 'practice open "
                  "defecation' (" + NFHS + ", Chapter 2 key findings).")),
            body("Both can be true in their own terms. Administrative coverage counts toilets "
                 "built and villages declared. Surveys count people's actual practice, which "
                 "depends on whether the toilet works, has water, is close by, and is used by "
                 "every member. The gap between the two is a measure of use and maintenance, and "
                 "it is largest where water is scarce and housing crowded."),
            hbox("Rule for practitioners: use administrative data for inputs and outputs, and "
                 "household surveys for practice and outcomes. Never use a declaration as "
                 "evidence of behaviour.", "indigo"),
        ], compact=True),

        C("Housing", "Housing quality is a health condition and an eligibility rule", [
            body("Crowded, poorly ventilated, kutcha housing raises the risk of TB and respiratory "
                 "infection, makes heat worse, and leaves families exposed in floods. Indian "
                 "policy already recognises housing as a marker of deprivation. Under PM-JAY, the "
                 "first rural deprivation criterion from the Socio-Economic and Caste Census 2011 "
                 "is D1: 'Households having only one room with kucha walls and kucha roof' (PIB "
                 "Backgrounder, 22 September 2026)."),
            tw(pp("cyan", "Channels from housing to health",
                  "Indoor smoke where kitchens lack ventilation; damp and crowding for "
                  "respiratory infection; heat retention under tin roofs; lack of a latrine or "
                  "water connection; insecure tenure that blocks access to services in "
                  "unrecognised slums."),
               pp("green", "What a programme can measure",
                  "Rooms per person, roof and wall material, separate kitchen, cooking fuel, "
                  "water and sanitation on premises, and recognised address. NFHS household "
                  "questionnaires collect most of these.")),
            hbox("Urban housing programmes that relocate slum families far from work can raise "
                 "income loss and travel time even as they improve the dwelling. Measure the "
                 "determinants on both sides.", "amber"),
        ], compact=True),

        C("Cooking fuel", "Four in ten Indian households still cook without clean fuel", [
            stats([card("58.6%", "households using clean cooking fuel, India", "cyan",
                        NFHS + ", Table 2.6"),
                   card("89.7%", "urban households using clean fuel", "green", NFHS),
                   card("43.2%", "rural households using clean fuel", "red", NFHS)], cols=3),
            body("Burning wood, dung or crop residue indoors exposes those who cook, mostly women, "
                 "and the young children beside them to smoke. The GBD India state analysis "
                 "attributed 0.61 million deaths in 2019 to household air pollution, while "
                 "finding that the death rate from this cause fell by 64.2% between 1990 and 2019 "
                 "(India State-Level Disease Burden Initiative Air Pollution Collaborators, "
                 "<em>Lancet Planetary Health</em> 5: e25-e38, 2021).", sm=True),
            tw(pp("cyan", "A determinant within a determinant",
                  "Having an LPG connection is different from using it every day. Cost of "
                  "refills and free fuelwood shape the choice, so households stack fuels."),
               pp("amber", "Who is exposed",
                  "The rural-urban gap (43.2% against 89.7%) is a gap in women's exposure, "
                  "because women do most of the cooking.")),
        ], compact=True),

        C("Ambient air", "Air pollution: 1.67 million deaths in India in 2019", [
            stats([card("1.67 m", "deaths attributable to air pollution, India, 2019", "red",
                        "Lancet Planetary Health 5: e25-e38, 2021"),
                   card("17.8%", "of all deaths in India that year", "amber",
                        "Lancet Planetary Health 5: e25-e38, 2021"),
                   card("1.36%", "of GDP lost to premature death and illness from air "
                        "pollution", "cyan", "Lancet Planetary Health 5: e25-e38, 2021")], cols=3),
            body("The same study found that ambient particulate matter accounted for 0.98 million "
                 "of the deaths, and that the death rate from ambient particulate pollution rose "
                 "by 115.3% between 1990 and 2019, even as household air pollution deaths fell. "
                 "The economic loss as a share of state GDP was highest in 'the low per-capita GDP "
                 "states of Uttar Pradesh, Bihar, Rajasthan, Madhya Pradesh, and Chhattisgarh'. "
                 "Poorer states bear a larger relative burden.", sm=True),
            hbox("Air pollution is the clearest case of a determinant no household can buy its way "
                 "out of fully. Its exposure is shared, but vulnerability is not: outdoor workers, "
                 "people in poor housing and those without access to care bear more of the harm.",
                 "indigo"),
        ], compact=True),

        C("Exposure and vulnerability", "Diderichsen's mechanisms applied to living conditions", [
            table(["Mechanism", "Water and sanitation example", "Air pollution example"],
                  [["Differential exposure", "Low-lying slums flood with drain water",
                    "Roadside vendors and construction workers breathe more"],
                   ["Differential vulnerability", "Undernourished children get sicker from the "
                    "same infection", "Anaemic or older workers suffer more from the same dose"],
                   ["Differential consequences", "A daily-wage parent loses pay caring for a "
                    "sick child", "A family borrows to pay for a hospital stay for asthma"],
                   ["Feedback to position", "Repeated illness lowers schooling",
                    "Chronic lung disease ends a working life early"]]),
            body("The four mechanisms come from the Diderichsen model that Solar and Irwin built "
                 "into the CSDH framework (" + SOLAR + ", pages 23-24). They give a programme "
                 "four separate places to intervene. A drain cover reduces exposure. Nutrition "
                 "reduces vulnerability. Insurance and sick leave reduce consequences. Schooling "
                 "support for children who miss classes interrupts the feedback.", sm=True),
            hbox("When you write a theory of change for a health equity project, name which of "
                 "the four mechanisms each activity targets.", "amber"),
        ], compact=True),

        C("Measuring conditions", "Indicators for living conditions, and where to find them", [
            table(["Determinant", "Indicator", "Source", "Lowest geography"],
                  [["Water", "At least basic drinking water", "JMP; NFHS household module",
                    "Country (JMP); district (NFHS)"],
                   ["Sanitation", "Improved, not shared facility; open defecation", "NFHS; JMP",
                    "District (NFHS)"],
                   ["Cooking fuel", "Clean fuel for cooking", "NFHS", "District"],
                   ["Housing", "Kutcha house, rooms per person", "Census; NFHS", "Village and "
                    "ward (Census)"],
                   ["Slums", "Slum population and households", "Census 2011 slum abstract",
                    "Town"],
                   ["Air", "PM2.5 exposure; attributable deaths", "GBD; CPCB monitors",
                    "State (GBD)"]]),
            body("The lowest geography tells you whether you can use the source to target a "
                 "programme. NFHS-5 provides district-level estimates for many indicators across "
                 "707 districts, so a district team can compare itself with its state. The Census reaches villages and wards but is a decade "
                 "old until the 2027 round (reference date 1 March 2027) is published.", sm=True),
        ], compact=True),

        # ===================== SECTION 07 =====================
        D("07", "Section Seven", "Heat, food, roads, violence and work"),

        C("Heat", "Ahmedabad's heat action plan: South Asia's first, and evaluated", [
            body("After a heatwave in 2010, Ahmedabad implemented what an evaluation team called "
                 "'South Asia's first heat action plan', which issues warnings when extreme heat is "
                 "forecast and triggers a response across city agencies. J.J. Hess and "
                 "colleagues from the Indian Institute of Public Health, Gandhinagar and partner "
                 "institutions compared summer mortality in 2014-2015 with a 2007-2010 baseline "
                 "(<em>Journal of Environmental and Public Health</em>, article 7973519, 2018)."),
            stats([card("2.34", "rate ratio for daily deaths at 47&deg;C, before the plan", "red",
                        "Hess et al., J Environ Public Health, 2018"),
                   card("1.25", "rate ratio at 47&deg;C after the plan", "green",
                        "Hess et al., J Environ Public Health, 2018"),
                   card("1,190", "estimated deaths avoided per year after the plan (95% CI "
                        "162-2,218)", "cyan", "Hess et al., J Environ Public Health, 2018")],
                  cols=3),
            body("The confidence interval is wide, and a before-after comparison cannot rule out "
                 "other changes over the period, so read the 1,190 as indicative. Heat is a "
                 "social determinant because exposure and vulnerability follow position: outdoor "
                 "and construction work, tin roofs, no fan or water, and older age all raise the "
                 "risk.", sm=True),
        ], compact=True),

        C("Who is exposed to heat", "Heat risk follows work, housing and age", [
            tw([panel("red", "Higher exposure", [bullets([
                    "Outdoor workers: farm labour, construction, street vending, delivery",
                    "Households under tin or asbestos roofs in dense settlements",
                    "Workers in hot indoor workplaces: kilns, foundries, kitchens",
                    "People with no water at the worksite"], sm=True)])],
               [panel("amber", "Higher vulnerability", [bullets([
                    "Older people and infants",
                    "People with heart, kidney or respiratory disease",
                    "Pregnant women",
                    "People who cannot afford to stop work on a hot day"], sm=True)])]),
            body("The last item links heat to income security. A daily-wage worker who stops work "
                 "at noon loses pay, so a warning is useful only if the work schedule can change. "
                 "Heat plans that shift construction hours, provide water and shade at worksites "
                 "and open cooling centres act on exposure; plans that only send messages assume "
                 "the person can act on them. The 2018 evaluation reported that extreme heat and "
                 "plan warnings after implementation were associated with lower summer mortality, "
                 "'with largest declines at highest temperatures'.", sm=True),
            hbox("For a climate-and-health programme, add heat exposure at work to your baseline: "
                 "hours outdoors between noon and 4 pm, water and shade at the worksite, roof "
                 "type at home. Climate Essentials 101 covers the wider picture.", "indigo"),
        ], compact=True),

        C("Food", "Food as a legal entitlement: the National Food Security Act, 2013", [
            table(["Provision", "What it says"],
                  [["Section 3(1)", "Every person in a priority household is entitled to five "
                    "kilograms of foodgrains per person per month at subsidised prices; Antyodaya "
                    "Anna Yojana households to 35 kg per household per month"],
                   ["Section 3(2)", "Entitlements extend up to 75% of the rural population and "
                    "up to 50% of the urban population"],
                   ["Section 4", "Pregnant women and lactating mothers are entitled to a free "
                    "meal through the anganwadi and maternity benefit of not less than Rs 6,000"],
                   ["Section 13(1)", "The eldest woman aged 18 or above is head of the household "
                    "for issuing ration cards"]]),
            body("Source: National Food Security Act, 2013 (No. 20 of 2013), as printed by PRS "
                 "Legislative Research. The Act turned access to subsidised grain from a scheme "
                 "into a right, with a grievance mechanism in Section 14. Section 13 is a gender "
                 "provision: making a woman the head of household for the ration card changes "
                 "who controls the entitlement.", sm=True),
            hbox("Grain addresses calories more than diet quality. Protein, fat and "
                 "micronutrients depend on income, prices and other programmes, which is why "
                 "anaemia can stay high where grain coverage is wide.", "amber"),
        ], compact=True),

        C("Diet and anaemia", "Two-thirds of young children are anaemic, across income groups", [
            stats([card("67%", "children aged 6-59 months with anaemia", "red",
                        NFHS + ", Chapter 10 key findings"),
                   card("57.0%", "women aged 15-49 with anaemia", "amber",
                        NFHS + ", Table 10.23.1"),
                   card("21%", "children aged 6-23 months who ate iron-rich foods the day "
                        "before", "cyan", NFHS + ", Chapter 10 key findings")], cols=3),
            body("These are NFHS-5 (2019-21) figures; the NFHS-6 fact sheet released in May 2026 "
                 "does not yet include anaemia. NFHS-5 reported that anaemia among children aged "
                 "6-59 months rose from the NFHS-4 "
                 "estimate of 59% to 67%. Women's anaemia ranges only from 63.7% in the lowest "
                 "wealth quintile to 51.0% in the highest. When even the richest fifth has "
                 "anaemia in half of its women, income alone cannot explain the pattern. Diet "
                 "composition, infections, menstrual and pregnancy losses, and fortification "
                 "policy matter for everyone."),
            hbox("Nutrition 101 covers the immediate, underlying and basic causes of "
                 "undernutrition, which map closely onto intermediary and structural "
                 "determinants.", "indigo"),
        ], compact=True),

        C("Roads", "Road crashes killed 1,68,491 people in India in 2022", [
            stats([card("4,61,312", "road accidents reported, India, 2022", "amber",
                        "MoRTH, Road Accidents in India 2022, via PIB, 31 Oct 2023"),
                   card("1,68,491", "people killed", "red",
                        "MoRTH, Road Accidents in India 2022, via PIB, 31 Oct 2023"),
                   card("+9.4%", "rise in fatalities over 2021", "cyan",
                        "MoRTH, Road Accidents in India 2022, via PIB, 31 Oct 2023")], cols=3),
            body("Transport is a determinant in two ways. It shapes injury risk: pedestrians, "
                 "cyclists and two-wheeler riders, many of whom cannot afford a car, share roads "
                 "with trucks and buses. And it shapes access: the time and cost of reaching a facility "
                 "in labour, in an accident or with a sick child. The report is compiled from "
                 "police data reported by states and union territories, in formats set by "
                 "UNESCAP's Asia Pacific Road Accident Data project."),
            tw(pp("cyan", "Care after a crash",
                  "Road accident victims covered under PM-RAHAT are among the additional "
                  "beneficiary categories of AB PM-JAY (PIB Backgrounder, 22 September 2026)."),
               pp("amber", "Data limits",
                  "Police-recorded crashes undercount injuries that never reach a police "
                  "station. Use hospital and survey data alongside them.")),
        ], compact=True),

        C("Work", "Work shapes health through hazard, security and protection", [
            body("In 2025, 56.2% of Indian workers were self-employed, 20.2% were casual labourers and "
                 "only 23.6% were in regular wage or salaried jobs (PLFS Annual Report 2025, NSO, "
                 "MoSPI, press note, March 2026). For most self-employed and casual workers an "
                 "illness means lost income, so a health shock becomes an income shock. The four "
                 "Labour Codes came into force on 21 November 2025, and the Code on Social "
                 "Security, 2020 (Act 36 of 2020) includes provisions for gig and platform "
                 "workers."),
            table(["Code on Social Security, 2020", "Content"],
                  [["Section 114(1)", "The Central Government may frame and notify social security "
                    "schemes for gig workers and platform workers on life and disability cover, "
                    "accident insurance, health and maternity benefits, old age protection, "
                    "creche, and other benefits"],
                   ["Section 114(2)", "Schemes may specify the role of aggregators and the "
                    "sources of funding"],
                   ["Section 114(3)", "Schemes may be funded by the Centre, states, aggregators' "
                    "contributions, combinations including beneficiaries, CSR funds or any other "
                    "source"]]),
            body("Source: The Code on Social Security, 2020, Gazette of India, as printed by PRS "
                 "Legislative Research. Note the verb: the Government 'may' frame schemes. The "
                 "health effect depends on schemes being notified and funded. Work, Labour & "
                 "Livelihoods 101 covers the Codes in detail.", sm=True),
        ], compact=True),

        C("Occupation and targeting", "Some occupations are now eligibility categories for health cover", [
            body("PM-JAY identifies urban beneficiaries by occupation, a recognition that certain "
                 "kinds of work carry both risk and insecurity. The PIB Backgrounder of 22 "
                 "September 2026 lists 11 urban occupational categories, including ragpickers, "
                 "domestic workers, street vendors, construction workers, sanitation workers, "
                 "home-based workers, transport workers and washer-men."),
            tw(pp("cyan", "Additional categories (2026)",
                  "Building and other construction workers; transgender persons under SMILE; "
                  "children orphaned by COVID-19 under PM CARES for Children; waste pickers and "
                  "sanitation workers under the NAMASTE scheme; Particularly Vulnerable Tribal "
                  "Groups under PM-JANMAN."),
               pp("amber", "What eligibility does not do",
                  "Cover for hospital bills does not remove the hazard. Sanitation workers still "
                  "face toxic gases; construction workers still face falls and heat. Prevention "
                  "sits with employers, contractors and the labour inspectorate.")),
            hbox("Occupation is a PROGRESS stratifier (Section 10). Record it in your baseline in "
                 "categories that match the scheme you want people to reach.", "indigo"),
        ], compact=True),

        # ===================== SECTION 08 =====================
        D("08", "Section Eight", "Paying for health"),

        C("Why financing", "How care is paid for is itself a determinant", [
            body("The Commission described the health care system as 'itself a social determinant "
                 "of health, influenced by and influencing the effect of other social "
                 "determinants'. It advocated financing through general taxation or mandatory "
                 "universal insurance, noted that 'public health-care spending has been found to "
                 "be redistributive in country after country', and wrote that 'upwards of 100 "
                 "million people are pushed into poverty each year through catastrophic household "
                 "health costs' (executive summary, " + CSDH + ")."),
            flow(["ILLNESS: a family member needs care",
                  "COST: fees, medicines, tests, travel, lost wages",
                  "COPING: savings, borrowing, selling assets, skipping care",
                  "POSITION: lower wealth, less schooling, worse future health"]),
            tw(pp("cyan", "Two kinds of harm",
                  "Some families pay and are impoverished. Others cannot pay and go without care. "
                  "The second group does not appear in spending statistics at all."),
               pp("amber", "Why it is regressive",
                  "A fixed hospital bill is a larger share of a poor household's budget, and poor "
                  "households have less to sell or borrow against.")),
        ], compact=True),

        C("National Health Accounts", "India's out-of-pocket share has fallen, and is still large", [
            stats([card("64.2% &rarr; 43.4%", "out-of-pocket expenditure as a share of total health "
                        "expenditure, 2013-14 to 2022-23", "amber", NHA),
                   card("28.6% &rarr; 43.7%", "government health expenditure as a share of total "
                        "health expenditure, same period", "green", NHA),
                   card("1.15% &rarr; 1.43%", "government health expenditure as a share of GDP, "
                        "same period", "cyan", NHA)], cols=3),
            body("The NHA 2022-23, released on 27 May 2026, is the tenth set of estimates prepared "
                 "by the National Health Accounts Technical Secretariat at NHSRC using the System "
                 "of Health Accounts 2011. Per person, government health expenditure rose from "
                 "Rs 1,042 to Rs 2,786. On the new GDP series with base year 2022-23, government "
                 "health expenditure is 1.48% of GDP. The share of private health insurance in "
                 "total health expenditure rose from 3.4% to 9.2%, and of social security "
                 "expenditure (including PM-JAY and government employee schemes) from 6% to 9.9%.",
                 sm=True),
            hbox("Even after the fall, households paid about 43 rupees of every 100 spent on health "
                 "in India in 2022-23, directly at the point of care.", "indigo"),
        ], compact=True),

        C("A pandemic dip", "Read one year of financing data with care", [
            bar("sdhOope", "Out-of-pocket expenditure as % of total health expenditure, India",
                NHA, ["2013-14", "2021-22", "2022-23"],
                [("OOPE share of THE", [64.2, 39.4, 43.4])], ymax=70, ytitle="% of THE"),
            body("The press release explains the 2021-22 figure: government raised health "
                 "spending to 1.84% of GDP that year for the COVID-19 response, including "
                 "emergency response packages and mass vaccination, and 'given these additional "
                 "spending by the government as a one-time measure, OOPE as percentage of Total "
                 "Health Expenditure (THE) during this period also declined to 39.4%'. In "
                 "2022-23 the share rose back to 43.4%. The long-run trend is downward. A single "
                 "pandemic year is the wrong baseline for judging it.", sm=True),
            hbox("When a ratio falls, check both parts. The out-of-pocket share can fall because "
                 "households pay less, or because government pays more while households pay the "
                 "same.", "amber"),
        ], compact=True),

        C("The region", "Out-of-pocket spending across South Asia, 2023", [
            table(["Country", "Out-of-pocket, % of current health expenditure (2023)"],
                  [["Bangladesh", "79.3"], ["Nepal", "59.4"], ["Sri Lanka", "54.8"],
                   ["Pakistan", "52.9"], ["India", "43.9"], ["Bhutan", "25.5"],
                   ["Maldives", "18.0"]]),
            body("Source: WHO Global Health Expenditure Database (indicator SH.XPD.OOPC.CH.ZS), via "
                 "World Bank WDI, accessed October 2026. This series uses current health "
                 "expenditure as the denominator, while India's NHA headline uses total health "
                 "expenditure (which includes capital spending). The two are close for India "
                 "(43.9% and 43.4%) but are different measures. Never mix denominators in one "
                 "chart.", sm=True),
            tw(pp("cyan", "Bangladesh",
                  "Nearly four-fifths of current health spending comes from household pockets, the "
                  "highest share in the region and close to double India's."),
               pp("green", "Bhutan and Maldives",
                  "Small populations with largely public provision show that low out-of-pocket "
                  "shares are possible in the region.")),
        ], compact=True),

        C("Catastrophic spending", "How many people spend more than a tenth of their budget on health", [
            table(["Country", "Latest year", "Population spending >10% of household budget on "
                   "health (%)"],
                  [["Bangladesh", "2016", "24.4"], ["India", "2017", "17.5"],
                   ["Nepal", "2016", "10.7"], ["Sri Lanka", "2016", "5.4"],
                   ["Pakistan", "2018", "5.4"]]),
            body("Source: WHO Global Health Observatory, indicator FINPROTECTION_CATA_TOT_10_POP "
                 "(SDG 3.8.2, reported data), accessed October 2026. This is the SDG measure of "
                 "financial hardship. The latest Indian point comes from survey data for 2017, "
                 "before PM-JAY's scale-up, so it cannot tell you the scheme's effect.", sm=True),
            tw(pp("amber", "A limit of the measure",
                  "A household that cannot pay and forgoes care spends nothing and is counted as "
                  "protected. A low catastrophic-spending rate can therefore hide unmet need, which "
                  "is why the measure is never read alone."),
               pp("cyan", "What to pair it with",
                  "Report forgone care (people who were ill and did not seek treatment because "
                  "of cost) alongside spending. NSS health rounds ask about reasons for not "
                  "seeking treatment.")),
        ], compact=True),

        C("Public and private", "A private hospital stay costs about six to eight times a public one", [
            table(["Average medical expenditure per hospitalisation (Rs), 2017-18",
                   "Public, rural", "Public, urban", "Private, rural", "Private, urban"],
                  [["Medicines", "2,220", "2,100", "6,818", "7,035"],
                   ["Doctor's or surgeon's fee", "172", "197", "5,340", "6,284"],
                   ["Diagnostic tests", "800", "770", "2,802", "3,403"],
                   ["Bed charges", "118", "152", "3,377", "4,176"],
                   ["Total (all components)", "4,290", "4,837", "27,347", "38,822"]]),
            body("Source: " + NSS75 + ", Statement 3.17 (excluding childbirth). Even in a public "
                 "hospital, a rural family spent over Rs 4,000 per stay, mostly on medicines and "
                 "tests. The same survey found that 13.4% of rural and 8.5% of urban "
                 "hospitalisation cases were financed mainly by borrowing (Statement 3.13), and that "
                 "85.9% of rural and 80.9% of urban people had no health expenditure coverage "
                 "(Statement 3.14).", sm=True),
            hbox("These figures predate PM-JAY's expansion. The next NSS health round will show "
                 "how far the pattern has changed; until then, cite 2017-18 with its date.",
                 "amber"),
        ], compact=True),

        C("PM-JAY", "Ayushman Bharat PM-JAY at eight years", [
            stats([card("Rs 5 lakh", "annual cashless hospital cover per eligible family", "cyan",
                        "PIB Backgrounder, 22 Sep 2026"),
                   card("48.51 crore", "people holding Ayushman cards, about 33% of the population "
                        "(21 Sep 2026)", "green", "PIB Backgrounder, 22 Sep 2026"),
                   card("13.25 crore", "hospital admissions worth Rs 2.03 lakh crore (31 Aug "
                        "2026)", "amber", "PIB Backgrounder, 22 Sep 2026")], cols=3),
            body("PM-JAY was launched on 23 September 2018. It covers secondary and tertiary "
                 "hospital care through over 38,000 empanelled public and private hospitals, for "
                 "1,961 procedures. Rural eligibility uses SECC 2011 deprivation criteria, "
                 "including D5 (SC and ST households) and D7 (landless households relying on "
                 "manual casual labour). On 11 September 2024 the scheme was extended to all "
                 "people aged 70 and above, about 6 crore senior citizens, of whom more than 1.36 "
                 "crore held Ayushman Vay Vandana cards by 21 September 2026. West Bengal became "
                 "the 36th state or union territory to implement the scheme on 8 June 2026 (PIB).", sm=True),
            hbox("Eligibility is built from social determinants: housing, caste, household "
                 "composition, landlessness and occupation. It is a targeted scheme with "
                 "universal elements for the elderly.", "indigo"),
        ], compact=True),

        C("What insurance covers", "Hospital insurance meets one cost among many", [
            tw([panel("green", "What PM-JAY addresses", [bullets([
                    "Inpatient bills for listed procedures, cashless at the point of care",
                    "Catastrophic hospital costs for eligible families",
                    "Cover for families identified by SECC 2011 criteria and listed categories",
                    "Some of the cost difference between public and private care"], sm=True)])],
               [panel("amber", "What it leaves to other policies", [bullets([
                    "Outpatient visits, medicines and tests outside a hospital stay",
                    "Travel, food and lost wages during treatment",
                    "Families who are eligible but hold no card or do not know",
                    "Places with no empanelled hospital within reach"], sm=True)])]),
            body("At least one usual member was covered by a health insurance or financing "
                 "scheme in 29% of households in NFHS-4, 41% in NFHS-5 (2019-21) and 60.2% in "
                 "NFHS-6 (2023-24), with rural households (62.0%) ahead of urban (56.4%) (" +
                 NFHS6 + "; " + NFHS + ", Chapter 11). Coverage on paper is a start. Use of the cover depends on "
                 "awareness, documents, distance and how hospitals treat card-holders: the "
                 "determinants again. Ayushman Arogya Mandirs, the primary-care pillar of "
                 "Ayushman Bharat, provide free essential medicines and diagnostics, which reach "
                 "part of the outpatient need that hospital cover leaves out.", sm=True),
        ], compact=True),

        # ===================== SECTION 09 =====================
        D("09", "Section Nine", "Policy approaches"),

        C("Health in All Policies", "Helsinki, 2013: Health in All Policies", [
            body("The 8th Global Conference on Health Promotion met in Helsinki from 10 to 14 June "
                 "2013 and adopted the <em>Helsinki Statement on Health in All Policies</em>, "
                 "published by WHO with a framework for country action."),
            term("Health in All Policies (HiAP)",
                 "'An approach to public policies across sectors that systematically takes into "
                 "account the health implications of decisions ... and avoids "
                 "harmful health impacts in order to improve population health and health "
                 "equity. It improves accountability of policymakers for health impacts at all "
                 "levels of policy-making.' (Health in All Policies: Helsinki Statement, WHO, "
                 "2014)"),
            tw(pp("cyan", "What it asks of non-health ministries",
                  "Before a road, a housing scheme, a mining lease or an agricultural subsidy is "
                  "approved, ask what it will do to health and to health equity, and change the "
                  "design if the answer is harmful."),
               pp("amber", "What makes it hard",
                  "Health is rarely the first goal of other ministries. The Statement itself "
                  "recognises that governments have many priorities in which health and equity "
                  "do not automatically take precedence.")),
            hbox("At district level, HiAP looks like a convergence committee in which the "
                 "Collector asks every department to report on one shared health outcome, such "
                 "as stunting or anaemia.", "indigo"),
        ], compact=True),

        C("Intersectoral action", "Who owns each determinant in an Indian state", [
            table(["Determinant (rainbow layer)", "Lead department or programme",
                   "A shared indicator"],
                  [["Water and sanitation", "Jal Shakti; Swachh Bharat Mission",
                    "Households with water and an improved, unshared toilet"],
                   ["Food", "Food and civil supplies (NFSA); women and child development",
                    "Ration uptake; anaemia among women"],
                   ["Education", "School education; higher education",
                    "Girls completing secondary school"],
                   ["Work environment", "Labour (the four Codes)", "Workers with social "
                    "security cover"],
                   ["Housing", "Rural development; urban development", "Kutcha houses; "
                    "slum households served"],
                   ["Health care services", "Health and family welfare", "Out-of-pocket "
                    "spending; facility births"],
                   ["Socio-economic conditions", "Finance; planning; social justice",
                    "Gaps by caste, tribe and wealth"]]),
            body("The rainbow's middle layer becomes a list of departments. Intersectoral action "
                 "means agreeing on shared indicators, pooling some budget, and holding regular "
                 "joint reviews. Without the shared indicator, each department reports its "
                 "own outputs and nobody reports the outcome.", sm=True),
        ], compact=True),

        C("Proportionate universalism", "Universal, with intensity proportionate to disadvantage", [
            quote("To reduce the steepness of the social gradient in health, actions must be "
                  "universal, but with a scale and intensity that is proportionate to the level "
                  "of disadvantage. We call this proportionate universalism.",
                  "Fair Society, Healthy Lives (the Marmot Review), 2010"),
            body("The review adds: 'Greater intensity of action is likely to be needed for those "
                 "with greater social and economic disadvantage, but focusing solely on the most "
                 "disadvantaged will not reduce the health gradient, and will only tackle a small "
                 "part of the problem.' The phrase is sometimes inverted as 'universal "
                 "proportionalism'; the review's own term is proportionate universalism."),
            tw(pp("cyan", "What it looks like",
                  "Every child gets an anganwadi service. Districts or blocks with the worst "
                  "stunting get more workers per child, more home visits and supplementary "
                  "food. The service is the same; the dose is graded."),
               pp("green", "Why not pure targeting",
                  "Targeting by a poverty line misses the middle of the gradient, excludes "
                  "eligible people through errors, and can lose political support among those "
                  "just above the line.")),
        ], compact=True),

        C("Three designs", "Targeted, universal or proportionate: an Indian comparison", [
            table(["Design", "Indian example", "Strength", "Risk"],
                  [["Targeted", "PM-JAY rural eligibility by SECC 2011 deprivation criteria",
                    "Concentrates funds on identified deprivation", "Exclusion errors; a list "
                    "that ages"],
                   ["Broad entitlement with a ceiling", "NFSA 2013: up to 75% rural and 50% "
                    "urban population (s3(2))", "Fewer exclusion errors at the bottom",
                    "Coverage capped by fixed population shares"],
                   ["Universal by category", "PM-JAY for everyone aged 70 and above (from 11 "
                    "September 2024)", "No means test; simple to explain",
                    "Spends on those who could pay"],
                   ["Proportionate", "Extra workers or funds for high-burden blocks inside a "
                    "universal service", "Reaches the whole gradient, with more where needed",
                    "Needs good small-area data to set intensity"]]),
            body("Sources for the scheme facts: PIB Backgrounder on AB PM-JAY, 22 September 2026; "
                 "National Food Security Act, 2013, s3. The last row is a design principle rather "
                 "than a named scheme; any example you build should be tested against small-area "
                 "data such as NFHS-5 district estimates.", sm=True),
            hbox("The design choice is itself a determinant: who is counted in shapes who gets "
                 "care.", "amber"),
        ], compact=True),

        C("Rights and law", "Health in the constitutions of South Asia", [
            table(["Instrument", "Provision", "What it does"],
                  [["Constitution of India, Article 47", "Directive Principle",
                    "The State shall regard raising the level of nutrition and the standard of "
                    "living and improving public health 'as among its primary duties'"],
                   ["Constitution of India, Article 21", "Right to life (judicial reading)",
                    "Paschim Banga Khet Mazdoor Samity v. State of West Bengal (1996) 4 SCC 37: "
                    "'Article 21 imposes an obligation on the State to safeguard the right to life "
                    "of every person'; government hospitals must provide timely medical treatment"],
                   ["Constitution of Nepal, 2015, Article 35", "Fundamental right",
                    "Makes basic health services and emergency health care a right of citizens"]]),
            body("In Paschim Banga (judgment of 6 May 1996), Hakim Seikh, a member of an "
                 "organisation of agricultural labourers, was injured falling from a train and refused admission by government hospitals in "
                 "Calcutta for want of beds. The Supreme Court held that 'it is the constitutional "
                 "obligation of the State to provide adequate medical services to the people' and "
                 "that financial constraints could not excuse it. The case is about the health "
                 "system as a determinant: a poor man's access to emergency care.", sm=True),
        ], compact=True),

        C("Measuring and monitoring", "The Commission's third recommendation, in practice", [
            body("The Commission asked governments to 'set up national and global health equity "
                 "surveillance systems for routine monitoring of health inequity and the social "
                 "determinants of health' and to 'evaluate the health equity impact of policy and "
                 "action'. In South Asia, the raw material exists: NFHS and the DHS surveys "
                 "publish every indicator by wealth, schooling, residence and, in India, caste and "
                 "religion."),
            tw(pp("cyan", "What routine monitoring needs",
                  "The same stratifiers in every round; publication of gaps alongside averages; "
                  "district estimates; and a named office responsible for reporting them."),
               pp("amber", "What is changing",
                  "The Census 2027, with reference date 1 March 2027, includes caste enumeration. "
                  "That will give small-area population denominators by caste that surveys "
                  "alone cannot provide.")),
            hbox("A health equity impact assessment asks three questions of any policy: who "
                 "benefits, who bears the cost, and does the gap widen or narrow. It is the "
                 "monitoring counterpart of Health in All Policies.", "indigo"),
        ], compact=True),

        C("Politics", "Equity is a political choice as well as a technical one", [
            body("Solar and Irwin stress 'the relative inattention to issues of political context' "
                 "in much of the literature on health determinants. They note that the quality of "
                 "the social determinants 'is conditioned by approaches to public policy', and "
                 "cite research finding that the type of welfare state explained about 20% of the "
                 "differences in infant mortality among 18 wealthy countries."),
            table(["2025 World report area for action", "What it means for a South Asian programme"],
                  [["Economic inequality, social infrastructure, universal services",
                    "Support public provision and fiscal space for health, schooling, water"],
                   ["Structural discrimination, conflict and forced migration",
                    "Monitor by caste, tribe, religion and migrant status"],
                   ["Climate action and digital transformation",
                    "Heat plans; avoid digital-only access that excludes the poor"],
                   ["Governance for equity, community participation",
                    "Convergence committees; community monitoring of services"]]),
            body("Source for the four areas: WHO news release on the World report on social "
                 "determinants of health equity, 6 May 2025. Political Economy 101 and Governance "
                 "& Accountability 101 develop the political side.", sm=True),
        ], compact=True),

        # ===================== SECTION 10 =====================
        D("10", "Section Ten", "Measuring inequity"),

        C("Simple gap measures", "Start with the rate ratio and the rate difference", [
            tw([term("Rate ratio (relative gap)",
                     "Outcome in the worse-off group divided by the outcome in the better-off "
                     "group. Under-five mortality, NFHS-5: 59.0 / 20.1 = <strong>2.9</strong>. "
                     "A child in the poorest quintile is about three times as likely to die "
                     "before five.")],
               [term("Rate difference (absolute gap)",
                     "Outcome in the worse-off group minus the better-off group. 59.0 - 20.1 = "
                     "<strong>38.9</strong> deaths per 1,000 live births. That is the number of "
                     "extra deaths per 1,000 births in the poorest group.")]),
            table(["NFHS-5 comparison", "Worse-off", "Better-off", "Ratio", "Difference"],
                  [["U5MR, lowest vs highest quintile", "59.0", "20.1", "2.9", "38.9"],
                   ["U5MR, Scheduled Tribe vs Other", "50.3", "32.8", "1.5", "17.5"],
                   ["Stunting, lowest vs highest quintile (%)", "46.1", "22.9", "2.0",
                    "23.2 points"],
                   ["Stunting, Scheduled Tribe vs Other (%)", "40.9", "30.1", "1.4",
                    "10.8 points"]]),
            body("Sources: " + NFHS_T72 + " and Table 10.1; ratios and differences are this "
                 "course's arithmetic. Both measures use only the two extreme groups and ignore "
                 "everyone in between, which is their main weakness.", sm=True),
        ], compact=True),

        C("Absolute and relative", "A gap can narrow on one measure and not the other", [
            table(["Under-5 mortality (5 years)", "NFHS-4 (2015-16)", "NFHS-5 (2019-21)"],
                  [["Rural", "55.8", "45.7"], ["Urban", "34.4", "31.5"],
                   ["Absolute gap (rural minus urban)", "21.4", "14.2"],
                   ["Relative gap (rural / urban)", "1.62", "1.45"]]),
            body("Source: " + NFHS_T72 + " (NFHS-4 rows for each residence); gap calculations are "
                 "this course's. Here both measures narrowed, because rural mortality fell faster "
                 "in absolute terms. Often they disagree. If mortality falls from 40 to 20 in one "
                 "group and from 20 to 8 in another, the absolute gap narrows from 20 to 12 while "
                 "the ratio widens from 2.0 to 2.5 (Illustrative)."),
            tw(pp("cyan", "Report both",
                  "An absolute gap tells a planner how many deaths a programme could prevent. A "
                  "relative gap tells you whether the disadvantaged are catching up in "
                  "proportion."),
               pp("amber", "Say which you mean",
                  "'Inequality fell' is ambiguous. Write 'the absolute gap fell from 21.4 to 14.2 "
                  "deaths per 1,000, and the ratio from 1.62 to 1.45'.")),
        ], compact=True),

        C("Concentration curve and index", "The concentration index uses the whole distribution", [
            body("A. Wagstaff, P. Paci and E. van Doorslaer reviewed measures of "
                 "socioeconomic inequality in health and argued that only two, 'the slope index "
                 "of inequality and the concentration index', are likely to give an accurate "
                 "picture; the range and some other measures can mislead (<em>Social Science and "
                 "Medicine</em> 33(5): 545-557, 1991)."),
            term("Concentration index (C)",
                 "Rank everyone from poorest to richest. Plot the cumulative share of the health "
                 "variable against the cumulative share of the population: that is the "
                 "concentration curve. C is twice the area between the curve and the 45-degree "
                 "line of equality. A convenient formula is C = 2 cov(h, r) / &mu;, where h is "
                 "the health variable, r the fractional rank and &mu; the mean of h."),
            tw(pp("cyan", "Reading the sign",
                  "C runs from -1 to +1. Zero means no wealth-related inequality. A negative value "
                  "means the variable is concentrated among the poor: for an illness, that is "
                  "pro-rich inequality in health."),
               pp("green", "The standard reference",
                  "O'Donnell, van Doorslaer, Wagstaff and Lindelow, <em>Analyzing Health Equity "
                  "Using Household Survey Data</em> (World Bank, 2008), Chapter 8, with Stata "
                  "code.")),
        ], compact=True),

        C("A worked index", "Computing a concentration index from quintile rates", [
            table(["Quintile", "U5MR (NFHS-5)", "Population share f", "Midpoint rank R",
                   "f &times; U5MR &times; R"],
                  [["Lowest", "59.0", "0.2", "0.1", "1.18"], ["Second", "48.0", "0.2", "0.3", "2.88"],
                   ["Middle", "39.1", "0.2", "0.5", "3.91"], ["Fourth", "32.7", "0.2", "0.7", "4.58"],
                   ["Highest", "20.1", "0.2", "0.9", "3.62"],
                   ["Sum / mean", "&mu; = 39.8", "1.0", "", "16.17"]]),
            body("For grouped data, C = (2 / &mu;) &times; &Sigma; f &times; h &times; R - 1 = (2 / "
                 "39.78) &times; 16.17 - 1 = <strong>-0.19</strong>. The same steps on stunting by "
                 "quintile (46.1, 39.7, 34.4, 28.1, 22.9) give <strong>-0.14</strong>. Both are "
                 "negative: deaths and stunting are concentrated among poorer children, and the "
                 "concentration is stronger for mortality."),
            hbox("Illustrative computation. It assumes each quintile holds one-fifth of births "
                 "and children, which is only approximately true because births are not spread "
                 "evenly across quintiles. A real analysis uses the microdata with sampling weights, as in "
                 "O'Donnell et al. (2008).", "amber"),
        ], compact=True),

        C("PROGRESS-Plus", "An acronym that keeps the stratifiers in view", [
            table(["Letter", "Stratifier", "South Asian reading"],
                  [["P", "Place of residence", "Rural or urban, slum, state, district, hill or "
                    "plain"],
                   ["R", "Race, ethnicity, culture, language", "Caste and tribe; language "
                    "minorities"],
                   ["O", "Occupation", "Casual labour, sanitation work, farming, domestic work"],
                   ["G", "Gender and sex", "Women, men, transgender persons"],
                   ["R", "Religion", "As recorded in NFHS and the Census"],
                   ["E", "Education", "Years of schooling, often of the mother"],
                   ["S", "Socioeconomic status", "Wealth quintile, consumption, land"],
                   ["S", "Social capital", "Networks, membership of groups"]]),
            body("Source: O'Neill and colleagues, 'Applying an equity lens to interventions: using "
                 "PROGRESS ensures consideration of socially stratifying factors to illuminate "
                 "inequities in health', <em>Journal of Clinical Epidemiology</em> 67(1): 56-64, "
                 "2014. The Cochrane Equity Methods Group adds 'Plus': personal characteristics "
                 "associated with discrimination (for example age and disability), features of "
                 "relationships, and time-dependent relationships.", sm=True),
        ], compact=True),

        C("Data sources", "Where South Asian equity data come from", [
            table(["Source", "Stratifiers available", "Strength", "Limit"],
                  [["NFHS (India), DHS (Bangladesh, Nepal, Pakistan)", "Wealth, schooling, "
                    "residence, caste and religion (India), region", "Comparable across "
                    "countries and rounds; district estimates in India",
                    "Every 4-5 years; full tables lag the fact sheets"],
                   ["SRS (India)", "Residence, state, sex", "Annual mortality and sex ratio at "
                    "birth", "No wealth or caste breakdown"],
                   ["NSS health rounds, HCES", "Consumption quintile, residence, social group",
                    "Spending and use of care", "Infrequent; the health round cited "
                    "here is 2017-18"],
                   ["PLFS", "Sex, residence, social group, education", "Work and earnings, "
                    "annual and quarterly", "Little on health"],
                   ["Census 2027", "Caste (newly enumerated), residence, slum status",
                    "Small-area denominators", "Reference date 1 March 2027; results "
                    "later"]]),
            body("Programme data rarely carry stratifiers. Adding two or three (caste or tribe, "
                 "sex, a short asset list) to your beneficiary records lets you compare your reach "
                 "with the survey distribution of need.", sm=True),
        ], compact=True),

        C("Pitfalls", "Five measurement errors that create false equity stories", [
            table(["Error", "What goes wrong", "Remedy"],
                  [["Comparing rounds with different definitions", "Apparent change is a change "
                    "in the question", "Check indicator definitions in each round's report"],
                   ["Mixing sources", "SRS and NFHS give different levels for the same year",
                    "One source per comparison; state it"],
                   ["Ignoring sampling error", "Small groups move by chance", "Show intervals; "
                    "flag cells with few cases"],
                   ["Using means only", "Averages rise while the bottom is left behind",
                    "Report by stratifier, every time"],
                   ["Relative change only", "A falling ratio can hide a stuck absolute gap",
                    "Report both absolute and relative gaps"]]),
            body("The NFHS-6 fact sheet warns that readers 'should be cautious while interpreting "
                 "and comparing the trends as some States/UTs may have' smaller sample sizes, and "
                 "describes its results as provisional (" + NFHS6 + "). Read every first release "
                 "with the same care.", sm=True),
        ], compact=True),

        # ===================== SECTION 11 =====================
        D("11", "Section Eleven", "Practical application: an equity lens"),

        C("Checklist", "An equity lens checklist for any programme", [
            tw([panel("cyan", "Design", [bullets([
                    "Which determinant does the programme change, and for whom?",
                    "Which groups have the worst outcome now (use PROGRESS-Plus)?",
                    "Is the gradient steep, shallow, or a cliff at one group?",
                    "Who could be excluded by eligibility rules, documents or distance?",
                    "Which other departments own the determinant?"], sm=True)])],
               [panel("green", "Delivery and monitoring", [bullets([
                    "Does reach match need, group by group?",
                    "Are costs to users (travel, fees, wages lost) recorded?",
                    "Are outcomes reported by at least two stratifiers?",
                    "Are both absolute and relative gaps tracked?",
                    "Is there a feedback route for the worst-off groups?"], sm=True)])]),
            body("Ten questions are enough for a design review or a proposal annex. Answer each "
                 "with evidence: a table from NFHS-5 or NFHS-6, your own baseline, or a named "
                 "study. Where you cannot answer a question, record it as a gap to fill in the "
                 "first year. The checklist follows the CSDH chain from structural position to "
                 "intermediary determinant to outcome, and the Commission's third recommendation "
                 "to measure and assess the impact of action.", sm=True),
            hbox("A programme that cannot say who it is not reaching has not yet applied an "
                 "equity lens.", "amber"),
        ], compact=True),

        C("Choosing stratifiers", "Which stratifiers to collect, by type of programme", [
            table(["Programme type", "Essential stratifiers", "Add if feasible", "Why"],
                  [["Maternal and child health", "Caste or tribe, mother's schooling, wealth "
                    "(asset list), residence", "Birth order, mother's age", "These carry the "
                    "largest gaps in NFHS-5"],
                   ["WASH", "Residence, slum status, caste or tribe", "Disability in household",
                    "Sanitation is a neighbourhood good; settlements are segregated"],
                   ["Livelihoods and social protection", "Sex, occupation, caste or tribe",
                    "Migrant status", "Work type sets hazard and security"],
                   ["Health financing and insurance", "Wealth, residence, age (70+ eligibility)",
                    "Card holding, distance to empanelled hospital", "Eligibility rules use "
                    "these categories"],
                   ["Gender-based violence", "Wealth, schooling, caste or tribe", "Disability",
                    "Rates differ widely by these (NFHS-5 Table 15.11)"]]),
            body("Keep the categories identical to the national survey so that you can compare "
                 "your beneficiaries with the population. Collect the minimum: each extra "
                 "identity question adds respondent burden and a data protection duty.", sm=True),
        ], compact=True),

        C("Decision table", "Matching the response to the shape of the gap", [
            table(["What your baseline shows", "Likely reading", "Response"],
                  [["Steady gradient across all quintiles", "A population-wide determinant",
                    "Universal service, intensity rising towards the bottom"],
                   ["One group far behind (a cliff)", "An access barrier specific to that group",
                    "Targeted outreach, removal of the barrier, then fold into universal"],
                   ["High everywhere, shallow gradient", "A shared exposure or norm",
                    "Universal action (fortification, clean air, water), extra reach for the "
                    "worst-off"],
                   ["Reverse gradient (better-off worse)", "Diet, sedentary work, urban exposure",
                    "Universal prevention; do not assume the poor are the only target"],
                   ["Gap in use while need is similar", "Cost, distance, discrimination at the "
                    "facility", "Fix the service: fees, timing, staff conduct"]]),
            body("Each row maps to an example in this course: under-five mortality by wealth in "
                 "India (staircase), Pakistan's quintile plateaus, anaemia among women (high and "
                 "shallow), women's high blood sugar in NFHS-6 (higher in urban areas), and the "
                 "PM-JAY gap between eligibility and use.", sm=True),
        ], compact=True),

        C("Worked example 1", "Illustrative: a block-level nutrition and WASH programme", [
            body("<strong>Illustrative case (hypothetical figures).</strong> An NGO works in three blocks of a district with "
                 "a large Scheduled Tribe population. Its baseline surveys 1,200 households with "
                 "a child under five, using NFHS categories."),
            table(["Group (baseline, Illustrative)", "Children", "Stunted (%)",
                   "No toilet used by all members (%)"],
                  [["Scheduled Tribe, poorest two quintiles", "420", "48", "55"],
                   ["Scheduled Tribe, top three quintiles", "160", "36", "30"],
                   ["Scheduled Caste", "240", "41", "35"],
                   ["Other Backward Class and Other", "380", "30", "18"],
                   ["All children", "1,200", "39.3", "36.0"]]),
            body("The averages are computed from the rows (weighted by children). The ST poorest "
                 "group has 18 more percentage points of stunting than the OBC and Other group: a "
                 "relative gap of 1.6. It also has three times the share of households where not "
                 "everyone uses a toilet. Within ST households, wealth matters (48% against 36%), "
                 "so neither caste nor wealth alone describes the problem.", sm=True),
            hbox("Read the table the way Section 5 read NFHS-5: stratify jointly, and check that "
                 "each cell has enough children to support a percentage.", "indigo"),
        ], compact=True),

        C("Worked example 2", "Illustrative: allocating effort in proportion to disadvantage", [
            body("<strong>Illustrative (hypothetical figures).</strong> The NGO has 30 community workers. Option A "
                 "allocates them by number of children. Option B gives every group a base level of "
                 "home visits and adds intensity in proportion to the stunting gap."),
            table(["Group", "Share of children", "Option A workers", "Option B workers",
                   "Home visits per child per month (B)"],
                  [["ST, poorest", "35%", "10.5", "14", "2"],
                   ["ST, better-off", "13%", "4", "4", "1.5"],
                   ["Scheduled Caste", "20%", "6", "6", "1.5"],
                   ["OBC and Other", "32%", "9.5", "6", "1"]]),
            body("Option B is proportionate universalism in small: every child is visited, and "
                 "the dose rises where the gap is largest. It also changes the sanitation plan: "
                 "toilet repair and water access go first to the ST poorest hamlets, because use, "
                 "not construction, is the gap there. Write the allocation rule into the project "
                 "document so that it survives staff turnover.", sm=True),
            hbox("Check the allocation against what the group needs as well as its size. A rule "
                 "that is fair by headcount can still widen a gap.", "amber"),
        ], compact=True),

        C("Worked example 3", "Illustrative: a monitoring plan that can show equity change", [
            table(["Indicator", "Stratified by", "Gap measure", "Frequency"],
                  [["Home visits completed", "Group (four rows above)", "Ratio of visit rate to "
                    "plan", "Monthly, from programme records"],
                   ["Toilet used by all members", "Group; hamlet", "Absolute gap, ST poorest vs "
                    "OBC/Other", "Six-monthly spot survey"],
                   ["Children stunted", "Group; sex", "Absolute and relative gap", "Baseline and "
                    "endline survey"],
                   ["Out-of-pocket cost of a clinic visit", "Group", "Median by group",
                    "Annual survey"],
                   ["Complaints and feedback", "Group; sex", "Count and resolution time",
                    "Quarterly"]]),
            body("At endline, report the change in each group, the change in the absolute and "
                 "relative gaps, and the concentration index if wealth was measured. A fall in the "
                 "average with no change in the ST poorest group is a result to report openly. "
                 "To attribute change to the programme, add a comparison group as described in "
                 "Impact Evaluation 101.", sm=True),
        ], compact=True),

        C("Common mistakes", "Six mistakes in health equity work, and the fix for each", [
            table(["Mistake", "Why it happens", "Fix"],
                  [["Reporting only averages", "Donor templates ask for one number",
                    "Add a stratified table to every report"],
                   ["Treating a declaration as an outcome", "Administrative data are easy to get",
                    "Pair it with a survey of practice, as with ODF and toilet use"],
                   ["Targeting only below a poverty line", "Simple to explain and cost",
                    "Check the gradient; use proportionate intensity"],
                   ["Mixing survey rounds or sources", "Convenience", "One source per "
                    "comparison, labelled by round"],
                   ["Assuming the direction of a gap", "Expectations from other indicators",
                    "Look at the data for each outcome (religion, blood sugar)"],
                   ["Counting cover as access", "Card numbers are reported",
                    "Measure use, costs and distance among the covered"]]),
            body("Each mistake corresponds to an example in this course: the Swachh Bharat "
                 "declaration against JMP and NFHS estimates, PM-JAY cards against hospital use, "
                 "NFHS against SRS mortality, and the Hindu-Muslim and urban-rural puzzles. When a "
                 "programme review raises one of them, return to the section where it was "
                 "discussed and rerun the analysis with the fix.", sm=True),
            hbox("Equity analysis is a habit: stratify, compare, ask why, and report the gap "
                 "whichever way it moved.", "indigo"),
        ], compact=True),

        # ===================== SECTION 12 =====================
        D("12", "Section Twelve", "Bringing it together"),

        C("Summary", "Ten ideas to take away", [
            tw([panel("cyan", "Concepts", [bullets([
                    "Health is shaped where people grow, live, work and age",
                    "Inequity is a gap that is avoidable and unfair",
                    "Structural position works through intermediary conditions",
                    "Health runs along a gradient, beyond poverty",
                    "The health system and its financing are determinants too"], sm=True)])],
               [panel("green", "Evidence and practice", [bullets([
                    "Under-five mortality is 2.9 times higher in India's poorest fifth (NFHS-5)",
                    "Caste and tribe gaps survive within rural and urban areas",
                    "Households still paid 43.4% of India's health spending (NHA 2022-23)",
                    "Proportionate universalism: universal, graded by need",
                    "Measure gaps both ways and stratify jointly"], sm=True)])]),
            body("Each idea rests on a source you can open: the CSDH report, Solar and Irwin's "
                 "framework, the Whitehall papers, NFHS-5 and NFHS-6, the DHS surveys, the NSS 75th "
                 "round, the National Health Accounts and the statutes and judgment cited. Check "
                 "the latest round before you reuse any figure: NFHS-6 full tables, a new NSS "
                 "health round and the Census 2027 will all change the numbers in this course.",
                 sm=True),
            hbox("Ask of every programme: which determinant does it change, for whom, and does "
                 "the gap close?", "indigo"),
        ], compact=True),

        C("Glossary", "Terms used in this course", [
            table(["Term", "Meaning"],
                  [["Social determinants of health", "Conditions in which people grow, live, work "
                    "and age, and the forces that shape them"],
                   ["Structural determinants", "Context and socioeconomic position: the social "
                    "determinants of health inequities"],
                   ["Intermediary determinants", "Material, psychosocial, behavioural and "
                    "biological factors, and the health system"],
                   ["Social gradient", "Health improving at each step up the social ladder"],
                   ["Proportionate universalism", "Universal action with intensity proportionate "
                    "to disadvantage"],
                   ["Health in All Policies", "Taking health and equity into account in every "
                    "sector's decisions"],
                   ["Concentration index", "Twice the area between the concentration curve and "
                    "the line of equality; -1 to +1"],
                   ["Catastrophic health spending", "Health spending above a threshold share (10% "
                    "or 25%) of household budget (SDG 3.8.2)"],
                   ["PROGRESS-Plus", "A checklist of stratifiers for equity analysis"]]),
            body("Definitions follow the sources cited on earlier slides: the CSDH report (2008), "
                 "Solar and Irwin (2010), the Marmot Review (2010), the Helsinki Statement (2013), "
                 "O'Donnell et al. (2008) and the WHO Global Health Observatory.", sm=True),
        ], compact=True),

        C("Where next", "Where next: related 101 decks", [
            tw([panel("cyan", "Health and nutrition", [body(
                    "<a href=\"/101-courses/pub-health-basics.html\">Public Health 101</a> for "
                    "epidemiology and health systems. "
                    "<a href=\"/101-courses/maternal-health.html\">Maternal Health 101</a>, "
                    "<a href=\"/101-courses/nutrition.html\">Nutrition 101</a> and "
                    "<a href=\"/101-courses/mental-health.html\">Mental Health 101</a> for specific "
                    "outcomes. <a href=\"/101-courses/child-development.html\">Child Development "
                    "101</a> for the early years. "
                    "<a href=\"/101-courses/climate-essentials.html\">Climate Essentials 101</a> and "
                    "<a href=\"/101-courses/env-justice.html\">Environmental Justice 101</a> for "
                    "heat and air.", sm=True)])],
               [panel("green", "Equity, policy and methods", [body(
                    "<a href=\"/101-courses/inequality-basics.html\">Inequality Basics 101</a>, "
                    "<a href=\"/101-courses/caste-studies.html\">Caste Studies 101</a>, "
                    "<a href=\"/101-courses/gender-dev.html\">Gender &amp; Development 101</a> and "
                    "<a href=\"/101-courses/social-margins.html\">Social Margins 101</a> for the "
                    "stratifiers. <a href=\"/101-courses/public-finance-budgeting.html\">Public "
                    "Finance &amp; Budgeting 101</a> and "
                    "<a href=\"/101-courses/public-policy-101.html\">Public Policy 101</a> for "
                    "financing and policy. <a href=\"/101-courses/impact-eval.html\">Impact "
                    "Evaluation 101</a> and <a href=\"/101-courses/survey-design.html\">Survey "
                    "Design 101</a> for measurement. "
                    "<a href=\"/101-courses/data-protection-dpdp.html\">Data Protection &amp; the "
                    "DPDP Act 101</a> for handling identity data.", sm=True)])]),
            hbox("Suggested order: Public Health, then Inequality Basics, then the deck for the "
                 "stratifier or outcome closest to your programme.", "indigo"),
        ], compact=True),

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Social Determinants of Health 101",
         "headline": "Ask which determinant a programme changes, for whom, and whether the gap closes",
         "byline": "ImpactMojo 101 Series &middot; Free foundational learning for development "
                   "practitioners in South Asia",
         "ctas": [{"label": "Public Health 101", "href": "/101-courses/pub-health-basics.html"},
                  {"label": "Inequality Basics 101", "href": "/101-courses/inequality-basics.html"},
                  {"label": "All 101 courses", "href": "/101-courses/"}],
         "meta": ["100 slides", "12 sections", "CC BY-NC-ND"]},
    ],
}
