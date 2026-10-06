# -*- coding: utf-8 -*-
"""
Nutrition 101 - ImpactMojo 101 Series (native deck spec)
Malnutrition in all its forms for South Asian practitioners: definitions and
growth standards, measurement in the field, the UNICEF frameworks and the first
1,000 days, India's numbers from NFHS and CNNS, the Indian enigma debates, the
National Food Security Act 2013 and the PDS, Poshan 2.0, PM POSHAN, Anemia Mukt
Bharat and fortification, the intervention evidence, South Asian comparisons
and a practitioner toolkit.
Build: python3 scripts/deck-builder/build.py nutrition

Every figure on a slide names its source. Sources were opened in October 2026.
Figures marked Illustrative are teaching examples.
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


N5 = "NFHS-5 India Report, IIPS and ICF, 2022"
N5T = "NFHS-5 India Report, IIPS and ICF, 2022, Table 10.1"
N6 = "NFHS-6 India Fact Sheet (provisional), IIPS, May 2026"
SC = "DHS Program STATcompiler, NFHS-3, NFHS-4 and NFHS-5"
CNNS = "CNNS 2016-18 National Report, MoHFW, UNICEF and Population Council, 2019"
LANCET13 = "Black et al., Lancet, 2013"
NFSA = "National Food Security Act 2013 (No. 20 of 2013)"

SLIDES_A = [

    # ===================== TITLE =====================
    {"type": "title",
     "main": "Nutrition<br>101",
     "sub": "Malnutrition in all its forms, how South Asia measures it, why India's "
            "numbers are argued over, and what the law and the evidence say a "
            "practitioner should do",
     "tags": ["100 Slides", "South Asia Focus", "Free Forever", "Food &amp; Nutrition"]},

    # ===================== TOC =====================
    {"type": "toc", "label": "Agenda", "title": "What we cover",
     "items": [
         {"name": "Malnutrition in all its forms"},
         {"name": "Measuring malnutrition: standards, z-scores and the field"},
         {"name": "Causes: the UNICEF frameworks and the first 1,000 days"},
         {"name": "India's numbers: NFHS and CNNS"},
         {"name": "The Indian enigma debates"},
         {"name": "The right to food: NFSA 2013 and the PDS"},
         {"name": "Programmes for mothers and children"},
         {"name": "Anaemia, micronutrients and fortification"},
         {"name": "What works: the intervention evidence"},
         {"name": "South Asia compared"},
         {"name": "Practical application: a practitioner's toolkit"},
         {"name": "Bringing it together"},
     ]},

    # ===================== SECTION 01 =====================
    D("01", "Section One", "Malnutrition in all its forms"),

    C("Definitions", "Malnutrition means too little, too much or the wrong mix", [
        body("Public health uses <strong>malnutrition</strong> as an umbrella for three "
             "families of problem. Undernutrition is a body that has not received or "
             "absorbed enough energy, protein or nutrients, and it shows in a child who is "
             "short, thin or light for age. Micronutrient deficiency is a shortfall in "
             "vitamins and minerals such as iron, vitamin A, zinc, folate, iodine and "
             "vitamin B12, and it can exist in a child of normal size. Overweight, obesity "
             "and diet-related non-communicable disease sit at the other end of the scale."),
        tw(pp("red", "Undernutrition",
              "Stunting, wasting, underweight and low birthweight. Linked to child deaths, "
              "poor learning and lower adult earnings."),
           pp("amber", "Hidden hunger and excess",
              "Micronutrient deficiencies, anaemia, overweight and obesity. Linked to "
              "lower productivity, diabetes, hypertension and heart disease.")),
        hbox("UNICEF's 2020 framework calls this the <strong>triple burden</strong>: "
             "undernutrition, micronutrient deficiencies and overweight, often in the same "
             "country, district or household (UNICEF Conceptual Framework on Maternal and "
             "Child Nutrition, 2021)."),
    ], compact=True),

    C("Stunting", "Stunting: too short for age, the mark of chronic deprivation", [
        term("Stunting",
             "Height-for-age more than two standard deviations below the median of the WHO "
             "Child Growth Standards (HAZ below -2 SD). Below -3 SD is severe stunting."),
        body("Height grows slowly and, after the early years, catches up only partly, so a "
             "short child records months or years of inadequate diet, repeated infection "
             "and often a poor start in the womb. Stunting is therefore read as a summary "
             "of a child's history. The 2008 Lancet series found height-for-age at two "
             "years to be the best predictor of adult human capital among the measures "
             "studied, using five cohorts from Brazil, Guatemala, India, the Philippines "
             "and South Africa (Victora et al., Lancet, 2008)."),
        stats([card("29.3%", "children under five stunted in India, 2023-24", "red", N6),
               card("35.5%", "stunted in 2019-21, the previous round", "amber", N5T),
               card("15.1%", "severely stunted (HAZ below -3 SD), 2019-21", "amber", N5T)]),
        hbox("Stunting is a population indicator. A single short child may simply have "
             "short parents; a district where a third of children are short has a problem.",
             "indigo"),
    ], compact=True),

    C("Wasting", "Wasting: too thin for height, the mark of acute crisis", [
        term("Wasting",
             "Weight-for-height (or weight-for-length) more than two standard deviations "
             "below the WHO median (WHZ below -2 SD), or a mid-upper arm circumference "
             "under 125 mm in children aged 6-59 months, or nutritional oedema."),
        body("Weight responds within weeks to illness or hunger, so wasting tracks recent "
             "events: a diarrhoeal episode, a lean season, a failed harvest. It is the form "
             "most directly tied to death. The 2021 Lancet update reported that in "
             "low-income countries 4.7% of children are both stunted and wasted, a "
             "condition associated with a 4.8-fold increase in mortality (Victora et al., "
             "Lancet, 2021)."),
        stats([card("19.0%", "children under five wasted in India, 2023-24 (19.3% in "
                    "2019-21)", "red", N6),
               card("5.2%", "severely wasted (WHZ below -3 SD), down from 7.7% in 2019-21",
                    "amber", N6)]),
        hbox("Wasting is treated as an emergency in the individual child: severe acute "
             "malnutrition needs screening, referral and therapeutic feeding, which "
             "Section 2 and Section 7 cover.", "amber"),
    ], compact=True),

    C("Underweight", "Underweight mixes two stories into one number", [
        tw(pp("cyan", "What it measures",
              "<strong>Underweight</strong> is weight-for-age below -2 SD of the WHO "
              "median. A child can be underweight because she is short (stunted), thin "
              "(wasted) or both. It needs only a scale, which is why growth monitoring "
              "leaned on it; the 2017 Cabinet decision on the National Nutrition Mission "
              "listed introducing height measurement at Anganwadi Centres as a new feature "
              "(PIB, 1 December 2017)."),
           pp("amber", "Why practitioners are cautious",
              "Because it blends chronic and acute problems, a fall in underweight does "
              "not tell you which one improved. NFHS-6 (2023-24) puts underweight at 31.8% "
              "against 29.3% stunting and 19.0% wasting; stunting fell six points since "
              "NFHS-5 while underweight barely moved (NFHS-6 India Fact Sheet, 2026). "
              "Report the three together, and prefer height-for-age and weight-for-height "
              "when you design or evaluate.")),
        table(["Indicator", "Index", "Reads as", "Time scale"],
              [["Stunting", "Height-for-age", "Chronic undernutrition", "Months to years"],
               ["Wasting", "Weight-for-height", "Acute undernutrition", "Days to weeks"],
               ["Underweight", "Weight-for-age", "Composite of both", "Mixed"],
               ["Overweight", "Weight-for-height above +2 SD", "Excess", "Months"]]),
    ], compact=True),

    C("Hidden hunger", "Micronutrient deficiency and anaemia", [
        body("Iron, vitamin A, zinc, iodine, folate and vitamin B12 are needed in small "
             "amounts, but a shortfall affects immunity, growth, cognition and pregnancy "
             "outcomes. Because deficiency is invisible without a blood or urine test, it "
             "is called hidden hunger. Anaemia, low haemoglobin, is the most widely "
             "measured sign, but it has many causes beyond iron: infections such as "
             "malaria and hookworm, other nutrient deficiencies, chronic inflammation and "
             "inherited conditions such as thalassaemia and sickle cell disease (CNNS "
             "2016-18 National Report, 2019, Ch. 6)."),
        stats([card("67.1%", "children 6-59 months anaemic", "red", N5),
               card("57.0%", "women 15-49 anaemic", "red", N5),
               card("25.0%", "men 15-49 anaemic", "amber", N5)]),
        hbox("These are NFHS-5 (2019-21) figures. The NFHS-6 fact sheets released in May "
             "2026 carry no anaemia indicator, and as of October 2026 NFHS-6 anaemia data "
             "have not been released. The figures are also contested: Section 5 explains "
             "why capillary and venous blood give different answers.", "indigo"),
    ], compact=True),

    C("Overweight", "Overweight and diet-related disease are rising in the same places", [
        body("India's women and men now carry undernutrition and overweight side by side. "
             "NFHS-6 (2023-24) found 19.7% of women and 19.7% of men aged 15-49 with a "
             "body mass index below 18.5, while 30.7% of women and 27.3% of men were "
             "overweight or obese, up from 24.0% and 22.9% in NFHS-5 (NFHS-6 India Fact "
             "Sheet, 2026). The overweight share is now higher than the thin share for "
             "women."),
        tw(pp("amber", "Blood sugar",
              "High or very high random blood sugar (above 140 mg/dl) or taking medicine "
              "for it rose from 13.5% to 17.8% among women and from 15.6% to 20.9% among "
              "men aged 15 and over between NFHS-5 and NFHS-6 (NFHS-6 India Fact Sheet, "
              "2026). In NFHS-5, overweight among women rose from 10% in the lowest wealth "
              "quintile to 39% in the highest (NFHS-5, Ch. 10)."),
           pp("red", "Among children and adolescents",
              "The CNNS found one in ten school-age children and adolescents pre-diabetic "
              "and 5% of adolescents with hypertension (CNNS 2016-18 National Report, "
              "2019, Ch. 8). Overweight among under-fives was 1.3% in NFHS-6 against 3.4% "
              "in NFHS-5 (NFHS-6 India Fact Sheet, 2026).")),
        hbox("The Lancet's 2019-20 series on the double burden traces the rise of "
             "overweight in the poorest LMICs mainly to cheap ultra-processed food and "
             "falling physical activity (Popkin, Corvalan and Grummer-Strawn, Lancet, 2020).",
             "cyan"),
    ], compact=True),

    C("Double burden", "The double burden in one country, one district, one home", [
        term("Double burden of malnutrition",
             "The simultaneous presence of undernutrition and overweight or obesity, at the "
             "level of a population, a household or an individual over the life course "
             "(Popkin, Corvalan and Grummer-Strawn, Lancet, 2020)."),
        tw(pp("cyan", "Why it matters for programmes",
              "Programmes built only to add calories can worsen the second burden. A take "
              "home ration rich in sugar and refined flour fills an energy gap and does "
              "little for micronutrients. The Lancet 2008 cohorts also found that low "
              "birthweight followed by rapid weight gain after infancy was linked to higher "
              "glucose, blood pressure and harmful lipids in adulthood (Victora et al., "
              "Lancet, 2008)."),
           pp("green", "What double-duty design looks like",
              "Protect breastfeeding, improve diet quality as well as quantity, "
              "measure height and weight together, and track adult waist and blood "
              "pressure in the same surveys that track child stunting. The CNNS was the "
              "first Indian national survey to measure NCD biomarkers in children and "
              "adolescents (CNNS 2016-18 National Report, 2019, Ch. 8).")),
    ], compact=True),

    C("Why it matters", "The cost of malnutrition is counted in lives and in earnings", [
        stats([card("45%", "of child deaths in 2011 attributed to undernutrition in the "
                    "aggregate (3.1 million)", "red", LANCET13),
               card("165 million", "children under five stunted worldwide in 2011", "amber",
                    LANCET13),
               card("52 million", "children under five wasted worldwide in 2011", "amber",
                    LANCET13)]),
        body("The 2013 Lancet estimate counts fetal growth restriction, stunting, wasting, "
             "vitamin A and zinc deficiency and suboptimal breastfeeding together. "
             "Survivors carry the cost too: the 2008 series found undernutrition strongly "
             "associated with shorter adult height, less schooling and reduced economic "
             "productivity, and for women with lower offspring birthweight, which passes "
             "the disadvantage to the next generation (Victora et al., Lancet, 2008)."),
        hbox("These global numbers are a decade old by design: they come from the series "
             "that set the agenda. Use the latest Joint Child Malnutrition Estimates from "
             "UNICEF, WHO and the World Bank for current global counts.", "indigo"),
    ], compact=True),

    # ===================== SECTION 02 =====================
    D("02", "Section Two", "Measuring malnutrition: standards, z-scores and the field"),

    C("The yardstick", "The WHO Child Growth Standards, 2006", [
        body("WHO released new Child Growth Standards on 27 April 2006 (WHO, Child Growth "
             "Standards web page). They were built from the WHO Multicentre Growth "
             "Reference Study, which pooled about 8,500 children from six countries: "
             "Brazil, Ghana, India, Norway, Oman and the United States. The Indian site "
             "was Delhi. Children were selected for conditions that do not constrain "
             "growth: no maternal smoking, single term births, adherence to feeding "
             "recommendations including breastfeeding, and no significant illness "
             "(de Onis et al., Food and Nutrition Bulletin, 2004)."),
        tw(pp("cyan", "A standard",
              "The study was prescriptive. It describes how children <em>should</em> grow "
              "when their needs are met, with the breastfed infant as the norm, and its "
              "authors concluded the standards can be used to assess children everywhere, "
              "regardless of ethnicity, socio-economic status and type of feeding (WHO "
              "MGRS Group, Acta Paediatrica, 2006)."),
           pp("amber", "A reference",
              "A growth reference describes how a particular sample of children "
              "<em>did</em> grow, whatever their conditions. Estimates made on different "
              "yardsticks cannot be compared, so recompute any long trend on the 2006 "
              "standard before reading it. NFHS-3, 4 and 5 figures from the DHS Program "
              "are all on the 2006 standard.")),
    ], compact=True),

    C("Z-scores", "A z-score says how far a child is from the healthy median", [
        body("A z-score expresses a child's measurement as the number of standard "
             "deviations above or below the median of the reference population of the same "
             "age and sex. A girl whose height-for-age z-score is -2.5 is two and a half "
             "standard deviations shorter than the median healthy girl of her age. In a "
             "healthy population about 2.3% of children fall below -2 SD by chance, so "
             "prevalence far above that signals a population problem."),
        table(["Z-score band", "Height-for-age", "Weight-for-height"],
              [["Below -3 SD", "Severely stunted", "Severely wasted"],
               ["-3 to below -2 SD", "Moderately stunted", "Moderately wasted"],
               ["-2 to +2 SD", "Within the normal range", "Within the normal range"],
               ["Above +2 SD", "Tall (rarely a concern)", "Overweight"]]),
        hbox("The mean z-score carries more information than the prevalence below -2 SD. "
             "India's mean height-for-age z-score in NFHS-5 is -1.3, which means the whole "
             "distribution has shifted down, including children well above the cut-off "
             "(NFHS-5 India Report, 2022, Table 10.1).", "indigo"),
    ], compact=True),

    C("Cut-offs", "Why a binary cut-off loses information", [
        tw(pp("cyan", "What the line does",
              "Stunting, wasting and underweight convert a continuous measure into yes or "
              "no. That makes the numbers easy to report and to set targets for, which is "
              "why governments and the SDGs use them. A child at -1.99 SD and a child at "
              "-2.01 SD are almost identical, yet one counts and one does not."),
           pp("amber", "What researchers do",
              "Analysts usually model the z-score itself. Spears, Ghosh and Cumming showed "
              "by simulation that dichotomising height into a stunting indicator "
              "sacrifices statistical power, so an estimated effect on stunting may be a "
              "lower bound on the effect on height (PLoS One, 2013).")),
        flow(["MEASURE height, weight and exact age",
              "COMPUTE z-scores against the WHO standard",
              "CHECK for implausible values and heaping",
              "REPORT mean z-score and prevalence together"]),
        body("In a proposal or evaluation, name the indicator, the standard (WHO 2006), the "
             "age range (0-59 months or 6-59 months) and whether prevalence or mean z-score "
             "is the primary outcome. Changing any of these changes the number.", sm=True),
    ], compact=True),

    C("Anthropometry", "Measuring a child well takes training and the right kit", [
        body("Children under two are measured lying down (length) on a measuring board; "
             "older children standing (height). The WHO standards build in an average "
             "difference of 0.7 cm between length and height, so recording which position "
             "was used matters (WHO MGRS Group, Acta Paediatrica, 2006). Weight needs a "
             "calibrated scale, ideally one that can tare a mother's weight so the child "
             "can be weighed in her arms. Age needs a recorded date of birth, because a "
             "few months' error moves a height-for-age z-score substantially."),
        table(["Error source", "What goes wrong", "Field fix"],
              [["Age", "Rounded ages pile up at whole years", "Use birth certificates, MCP "
                "card, local event calendars"],
               ["Position", "Height taken for a 1-year-old", "Length under 24 months"],
               ["Equipment", "Uncalibrated or soft boards", "Rigid boards, daily calibration"],
               ["Measurer", "One person, child moving", "Two trained measurers, re-measure"],
               ["Recording", "Digits transposed", "Read back, tablet range checks"]]),
    ], compact=True),

    C("Standardisation", "Data quality is a design decision, made before fieldwork", [
        tw(pp("cyan", "Before the survey",
              "Run a standardisation exercise: each measurer measures the same children "
              "twice and is compared with an expert, for both precision (agreement with "
              "themselves) and accuracy (agreement with the expert). Retrain or replace "
              "those who fall outside agreed limits. Budget for rigid equipment and spare "
              "scales."),
           pp("green", "During and after",
              "Re-measure a random subsample. Plot z-score distributions by measurer and "
              "by day. Look for digit preference (heights ending in .0 or .5) and heaping "
              "of ages. Exclude only values flagged as biologically implausible by the WHO "
              "software, and report how many were excluded.")),
        body("Large surveys report their exclusions. The CNNS, for example, documents "
             "for each anthropometric table how many cases were excluded because a value "
             "was flagged and how many because a measurement was missing (CNNS 2016-18 "
             "National Report, 2019, Ch. 5). Ask for the same disclosure from any "
             "programme survey before trusting its prevalence figure."),
        hbox("A programme's own baseline, measured by its own staff, is the place where "
             "poor anthropometry most often creates a fake trend.", "amber"),
    ], compact=True),

    C("MUAC", "Mid-upper arm circumference: the field screening tool", [
        body("A colour-coded tape around the middle of the left upper arm takes seconds, "
             "needs no scale or calculator, and predicts mortality well. That is why "
             "community workers use it to find acutely malnourished children aged 6-59 "
             "months and refer them."),
        table(["Classification (6-59 months)", "MUAC", "Or weight-for-height", "Plus"],
              [["Severe acute malnutrition (SAM)", "Below 115 mm", "WHZ below -3 SD",
                "Or nutritional oedema"],
               ["Moderate acute malnutrition (MAM)", "115 to below 125 mm",
                "WHZ -3 to below -2 SD", "And no oedema"],
               ["Not acutely malnourished", "125 mm or more", "WHZ -2 or above", ""]]),
        body("Source: WHO and UNICEF, Implementation guidance on the management of wasting "
             "and nutritional oedema in infants and children under 5 years, 2026, "
             "following the WHO 2023 guideline. MUAC and weight-for-height identify "
             "overlapping but different children, so the guidance accepts either.", sm=True),
        hbox("In India, the CNNS found 11% of children 6-59 months acutely malnourished by "
             "MUAC-for-age below -2 SD, and 5% by absolute MUAC below 125 mm, against 17% "
             "wasted by weight-for-height (CNNS 2016-18 National Report, 2019, Ch. 5). The "
             "tool you choose changes the caseload you plan for.", "amber"),
    ], compact=True),

    C("Diets", "Measuring what children eat: the IYCF indicators", [
        body("Anthropometry shows outcomes; diet indicators show one of the immediate "
             "causes. WHO and UNICEF publish standard infant and young child feeding (IYCF) "
             "indicators; the 2021 edition lists 17 recommended indicators, seven of them "
             "new (WHO and UNICEF, Indicators for assessing infant and young child feeding "
             "practices, 12 April 2021). Three matter most for children 6-23 months: "
             "minimum dietary diversity, minimum meal frequency and their combination, the "
             "minimum acceptable diet."),
        stats([card("15.3%", "children 6-23 months with an adequate diet, 2023-24 (11.0% "
                    "in 2019-21)", "red", N6),
               card("23%", "with minimum dietary diversity, 2019-21", "amber", N5),
               card("35%", "with minimum meal frequency, 2019-21", "amber", N5)]),
        hbox("Check the definition behind any trend. The NFHS-5 India report describes "
             "minimum dietary diversity as at least four food groups in its text and as "
             "five or more food groups in the footnote to its table (NFHS-5 India Report, "
             "2022, Ch. 10). The NFHS-6 fact sheet defines its adequate diet with four or "
             "more food groups (NFHS-6 India Fact Sheet, 2026, note 11). Compare rounds "
             "only on one definition.", "indigo"),
    ], compact=True),

    C("Haemoglobin", "Measuring anaemia: one drop of blood, several decisions", [
        body("Anaemia is diagnosed from haemoglobin concentration in grams per decilitre. "
             "Every survey makes four decisions that change the answer: which blood "
             "(capillary from a finger or heel prick, or venous from a vein), which device "
             "(a portable haemoglobinometer, or a laboratory analyser), which adjustments "
             "(altitude, and smoking in adults) and which cut-off."),
        table(["Decision", "NFHS-5 (2019-21)", "CNNS (2016-18)"],
              [["Blood", "Capillary", "Venous whole blood"],
               ["Method", "Portable haemoglobinometer in the home",
                "Cyanmethaemoglobin method and automated counters in laboratories"],
               ["Adjustments", "Altitude above 1,000 m; smoking for adults",
                "Altitude above 1,000 m"],
               ["Child cut-off", "Below 11.0 g/dL, ages 6-59 months",
                "Below 11.0 g/dL ages 1-4; 11.5 ages 5-11"],
               ["Completion", "91% of eligible children tested", "51,029 samples drawn"]]),
        body("Sources: NFHS-5 India Report, 2022, Ch. 10; CNNS 2016-18 National Report, "
             "2019, Ch. 2 and 6. Anemia Mukt Bharat field testing uses digital invasive "
             "haemoglobinometers (PIB, 6 August 2024). When two surveys disagree on "
             "anaemia, compare these four decisions before comparing the numbers; Section "
             "5 shows how far apart they can land.", sm=True),
    ], compact=True),

    C("Survey design", "Surveys are weighted and clustered: analyse them that way", [
        tw(pp("cyan", "Weights",
              "DHS-type surveys such as NFHS select households with unequal probabilities, "
              "so each record carries a weight. The DHS Program's guide notes that weights "
              "are stored without the decimal point and must be divided by 1,000,000 "
              "before use, for example <code>wt = v005/1000000</code> for women and "
              "children (DHS Program, Guide to DHS Statistics, Analyzing DHS Data)."),
           pp("amber", "Clusters and strata",
              "Households are sampled in clusters within strata. Ignoring that design "
              "gives standard errors that are too small and confidence intervals that "
              "look precise when they are not. Use survey commands (Stata <code>svy</code>, "
              "R <code>survey</code>) with the cluster and strata variables.")),
        body("Two further traps. First, subgroups such as a district or a caste group are "
             "estimated on the full survey design; dropping the other records first "
             "understates the standard error. Second, district estimates rest on far "
             "smaller samples than national ones, so a three-point change in "
             "one district between rounds may be noise. Read the confidence interval "
             "before you announce a district's progress or decline."),
        hbox("Survey Design 101 and Statistics Without Code 101 cover these ideas in more "
             "depth; links are at the end of this deck.", "indigo"),
    ], compact=True),

    C("Admin data", "Administrative data: Poshan Tracker and its limits", [
        body("Mission Poshan 2.0 runs the Poshan Tracker app, launched on 1 March 2021, in "
             "which Anganwadi Workers record attendance, take home ration and hot cooked "
             "meal delivery and monthly growth measurement. As of March 2026 the system "
             "covered about 14,03,170 Anganwadi Centres and 8,95,29,425 eligible "
             "beneficiaries (PIB backgrounder, Mission Poshan 2.0, 14 April 2026)."),
        tw(pp("green", "What it adds",
              "Monthly, child-level, near real-time data at the scale of the whole "
              "Anganwadi network. It can flag a child whose weight falls, and show which "
              "centres have stopped measuring."),
           pp("red", "What to watch",
              "It covers children enrolled at Anganwadis, who differ from all children. It "
              "is measured by workers who are also judged on the results, with equipment "
              "that varies by centre. Its prevalence figures are not comparable with NFHS, "
              "which uses trained measurers and a probability sample.")),
        hbox("This deck does not quote Poshan Tracker prevalence figures. Use them to "
             "manage a programme; use NFHS or CNNS to describe the population.", "amber"),
    ], compact=True),

    C("Data law", "Collecting nutrition data under the DPDP Act", [
        body("Anthropometry, haemoglobin and diet data on identifiable children are "
             "personal data under the Digital Personal Data Protection Act 2023. The Act "
             "commences in stages under G.S.R. 843(E) of 13 November 2025. The definitions "
             "and the Data Protection Board (ss 18-26) have applied since 13 November 2025. "
             "The core duties and rights in ss 3-17, including s9 on children's data and "
             "the s17 exemptions, together with the penalties in ss 27-34, apply only from "
             "13 May 2027. The DPDP Rules 2025 (G.S.R. 846(E)) follow the same phasing."),
        tw(pp("cyan", "Prepare now (as of October 2026)",
              "Treat the May 2027 duties as the standard to design for: notice, verifiable "
              "parental consent for children's data under s9, purpose limitation, "
              "retention limits and security safeguards. Surveys that will still be "
              "running in mid-2027 need consent forms written for it today."),
           pp("amber", "The research exemption",
              "Section 17(2)(b) will exempt processing for research, archiving or "
              "statistical purposes where the data are not used to take decisions about "
              "a specific person and the processing follows prescribed standards. It is "
              "not in force until 13 May 2027, and it never replaces research ethics "
              "review, which applies independently.")),
        hbox("Data Protection &amp; the DPDP Act 101 and Research Ethics 101 cover consent "
             "and children's data in detail.", "indigo"),
    ], compact=True),

    # ===================== SECTION 03 =====================
    D("03", "Section Three", "Causes: the UNICEF frameworks and the first 1,000 days"),

    C("UNICEF 1990", "The 1990 framework: immediate, underlying and basic causes", [
        body("The conceptual framework most nutrition programmes still draw on was "
             "published by Urban Jonsson in the Food and Nutrition Bulletin in 1981 and "
             "used in the Strategy for Improved Nutrition of Children and Women in "
             "Developing Countries adopted by the UNICEF Board in May 1990 (Jonsson, "
             "World Nutrition, 2014). It arranges causes in a hierarchy."),
        flow(["IMMEDIATE: inadequate dietary intake and disease",
              "UNDERLYING: inadequate food, inadequate care, inadequate health services",
              "BASIC: historical, social, economic and cultural processes",
              "OUTCOME: child malnutrition"]),
        tw(pp("cyan", "The vicious circle",
              "Poor intake weakens immunity; infection reduces appetite and absorption and "
              "raises needs. Each worsens the other, which is why diet and disease sit "
              "together at the immediate level."),
           pp("amber", "Necessary conditions",
              "Jonsson stresses that food, health and care are each necessary and none, "
              "alone or in pairs, is sufficient. Poverty and gender inequality are two of "
              "the most common basic causes (World Nutrition, 2014).")),
    ], compact=True),

    C("UNICEF 2020", "The 2020 framework: diets, care and the enabling environment", [
        body("UNICEF's Conceptual Framework on the Determinants of Maternal and Child "
             "Nutrition, 2020, guides its Nutrition Strategy 2020-2030. It builds on the "
             "1990 work, uses a positive narrative about what produces good nutrition, and "
             "names the triple burden explicitly (UNICEF Conceptual Framework on Maternal "
             "and Child Nutrition, November 2021)."),
        table(["Level", "2020 framework", "Example in an Indian block"],
              [["Immediate", "Good diets and good care", "Child eats 5 food groups; mother "
                "feeds responsively"],
               ["Underlying", "Food, practices and services", "Affordable eggs, handwashing, "
                "a functioning Anganwadi"],
               ["Enabling", "Governance, resources and norms", "Budget released on time; "
                "norms on girls' marriage age"],
               ["Outcomes", "Survival, growth, development, learning, earnings",
                "Height, school readiness, adult wages"]]),
        hbox("The shift from 'causes' to 'determinants' matters in practice: the 2020 "
             "version asks what has to be in place, so it reads as a checklist for design "
             "as well as a diagnostic.", "green"),
    ], compact=True),

    C("Two kinds of action", "Nutrition-specific and nutrition-sensitive", [
        tw(pp("cyan", "Nutrition-specific",
              "Act on the immediate determinants: breastfeeding promotion, complementary "
              "feeding counselling, micronutrient supplements, treatment of acute "
              "malnutrition, antenatal supplements. The 2013 Lancet series modelled ten "
              "such interventions at 90% coverage (Bhutta et al., Lancet, 2013)."),
           pp("green", "Nutrition-sensitive",
              "Act on underlying and enabling determinants: social protection, "
              "agriculture and food systems, women's status, education, water and "
              "sanitation. Bhutta and colleagues argue these can greatly accelerate "
              "progress when linked to improved access to specific interventions.")),
        body("The split explains a common disappointment. Ten specific interventions at "
             "very high coverage were estimated to avert only about a fifth of the stunting "
             "burden (Bhutta et al., Lancet, 2013). The rest depends on income, sanitation, "
             "women's schooling and status, and food prices, which sit with ministries "
             "other than health and women and child development."),
        hbox("Jonsson criticised frameworks that drop the basic causes in order to avoid "
             "the politics of malnutrition (World Nutrition, 2014). A practitioner can "
             "work at one level while naming the others.", "amber"),
    ], compact=True),

    C("The window", "The first 1,000 days: conception to the second birthday", [
        body("The period from conception to a child's second birthday is when growth and "
             "brain development are fastest and when damage is hardest to reverse. "
             "POSHAN Abhiyaan was designed with special emphasis on these 1,000 days "
             "(PIB backgrounder, Mission Poshan 2.0, 14 April 2026)."),
        {"t": "chart", "canvas": "nutStuntAgeChart",
         "title": "Stunted children by age in months, India, 2019-21 (%)",
         "source": "NFHS-5 India Report, IIPS and ICF, 2022, Table 10.1",
         "type": "bar",
         "data": {"labels": ["<6", "6-8", "9-11", "12-17", "18-23", "24-35", "36-47", "48-59"],
                  "datasets": [{"label": "Stunted (%)",
                                "data": [24.4, 23.2, 26.2, 36.3, 43.4, 38.1, 39.2, 35.4],
                                "backgroundColor": ["#0EA5E9", "#0EA5E9", "#0EA5E9",
                                                    "#F59E0B", "#EF4444", "#F59E0B",
                                                    "#F59E0B", "#F59E0B"]}]},
         "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:50, title:{display:true,text:'% stunted'} } } }"}},
        body("Stunting climbs steeply from 6-8 months to 18-23 months, the age when "
             "complementary foods should begin and when exposure to infection rises. "
             "After two years it plateaus. The window for prevention is early.", sm=True),
    ], compact=True),

    C("Before birth", "Growth faltering often begins in the womb", [
        body("The 2021 Lancet review found that stunting and wasting may already be present "
             "at birth and that the incidence of both peaks in the first six months of life "
             "(Victora et al., Lancet, 2021). The 2013 series estimated that maternal "
             "undernutrition contributes to 800,000 neonatal deaths a year through "
             "small-for-gestational-age births (Bhutta et al., Lancet, 2013)."),
        stats([card("24.4%", "infants under 6 months already stunted, India", "red", N5T),
               card("44%", "of children reported very small at birth are stunted", "amber",
                    N5 + ", Ch. 10"),
               card("11.5%", "women aged 15-49 under 145 cm tall", "amber",
                    N5 + ", Ch. 10")]),
        hbox("A child programme that starts at six months starts late. Maternal "
             "nutrition before and during pregnancy, and adolescent girls' nutrition "
             "before that, are part of a child stunting strategy.", "indigo"),
    ], compact=True),

    C("Mothers", "A mother's schooling and status show up in her child's height", [
        {"t": "chart", "canvas": "nutStuntEduChart",
         "title": "Stunted children under five by background, India, 2019-21 (%)",
         "source": "NFHS-5 India Report, IIPS and ICF, 2022, Ch. 10",
         "type": "bar",
         "data": {"labels": ["Mother no schooling", "Mother 12+ years", "Lowest wealth quintile",
                             "Highest wealth quintile", "Rural", "Urban"],
                  "datasets": [{"label": "Stunted (%)",
                                "data": [46, 26, 46, 23, 37, 30],
                                "backgroundColor": ["#EF4444", "#10B981", "#EF4444",
                                                    "#10B981", "#F59E0B", "#0EA5E9"]}]},
         "options": {"__js__": "{ indexAxis:'y', plugins:{legend:{display:false}}, scales:{ x:{ min:0, max:50 } } }"}},
        body("The gradients are steep: a child whose mother has twelve or more years of "
             "schooling is about half as likely to be stunted as a child whose mother has "
             "none. Children born to thin mothers (BMI below 18.5) are also more likely to "
             "be stunted, wasted and underweight (NFHS-5, Ch. 10). These are associations, "
             "and schooling, wealth and residence overlap, so the bars cannot be added.",
             sm=True),
    ], compact=True),

    C("Infection", "Infection and the gut: why food alone is not enough", [
        tw(pp("cyan", "Environmental enteric dysfunction",
              "Children exposed to faecal contamination can develop subclinical "
              "inflammation of the gut that reduces absorption without causing obvious "
              "diarrhoea. The 2021 Lancet review names subclinical inflammation and "
              "environmental enteric dysfunction as the direction new evidence on poor "
              "growth points to (Victora et al., Lancet, 2021)."),
           pp("amber", "Implication",
              "A child who eats an adequate diet can still falter if the environment "
              "keeps her gut inflamed. This is the biological argument behind the open "
              "defecation hypothesis in Section 5 and the water, sanitation and hygiene "
              "trials in Section 9.")),
        body("Anaemia shows the same overlap. The NFHS-5 report lists malaria, hookworm "
             "and other helminths, other nutritional deficiencies, chronic infections and "
             "genetic conditions as causes besides iron, and estimates that iron deficiency "
             "is responsible for about half of anaemia globally (NFHS-5 India Report, "
             "2022, Ch. 10). Deworming reached only 30% of children 6-59 months in the six "
             "months before NFHS-5."),
    ], compact=True),
]

SLIDES_B = [

    # ===================== SECTION 04 =====================
    D("04", "Section Four", "India's numbers: NFHS and CNNS"),

    C("Headline", "India's children in NFHS-6, 2023-24", [
        body("The National Family Health Survey is India's Demographic and Health Survey, "
             "run by the International Institute for Population Sciences for the Ministry "
             "of Health and Family Welfare. NFHS-6 covered 679,238 households in every "
             "state and UT except Manipur, in two phases from 28 May 2023 to 31 December "
             "2024. The Ministry released it on 29 May 2026, and the fact sheet marks its "
             "results as provisional (NFHS-6 India Fact Sheet, 2026; PIB, 29 May 2026)."),
        stats([card("29.3%", "stunted (35.5% in 2019-21)", "red", N6),
               card("19.0%", "wasted (19.3%)", "red", N6),
               card("31.8%", "underweight (32.1%)", "amber", N6),
               card("1.3%", "overweight (3.4%)", "cyan", N6)], cols=4),
        tw(pp("cyan", "Urban and rural",
              "Stunting is 23.9% in urban and 30.9% in rural areas; underweight 25.3% and "
              "33.8% (NFHS-6 India Fact Sheet, 2026). In NFHS-5, stunting rose from 31.5% "
              "among first-born children to 48.6% at birth order six or more, and was 46% "
              "in the poorest wealth quintile against 23% in the richest (NFHS-5, Table "
              "10.1 and Ch. 10)."),
           pp("amber", "What moved and what did not",
              "Stunting fell 6.2 points and severe wasting from 7.7% to 5.2% in about four "
              "years. Wasting and underweight barely changed. The government's release "
              "describes a 17% reduction in stunting and 32% in severe wasting (PIB, 29 May "
              "2026).")),
        hbox("The fact sheet gives the main indicators only. Breakdowns by sex, birth "
             "order, wealth and age in this deck are from the NFHS-5 India Report (2022) "
             "until the NFHS-6 report is published.", "indigo"),
    ], compact=True),

    C("Trend", "Two decades of progress on stunting, and none on wasting", [
        {"t": "chart", "canvas": "nutTrendChart",
         "title": "Children under five, India, NFHS-3 (2005-06) to NFHS-6 (2023-24), %",
         "source": "DHS Program STATcompiler (NFHS-3 to NFHS-5); NFHS-6 India Fact Sheet (provisional), IIPS, May 2026",
         "type": "bar",
         "data": {"labels": ["Stunted", "Wasted", "Underweight"],
                  "datasets": [
                      {"label": "NFHS-3 (2005-06)", "data": [48.0, 19.8, 42.5],
                       "backgroundColor": "#94A3B8"},
                      {"label": "NFHS-4 (2015-16)", "data": [38.4, 21.0, 35.7],
                       "backgroundColor": "#F59E0B"},
                      {"label": "NFHS-5 (2019-21)", "data": [35.5, 19.3, 32.1],
                       "backgroundColor": "#EF4444"},
                      {"label": "NFHS-6 (2023-24)", "data": [29.3, 19.0, 31.8],
                       "backgroundColor": "#0EA5E9"}]},
         "options": {"__js__": "{ plugins:{legend:{position:'bottom'}}, scales:{ y:{ min:0, max:55, title:{display:true,text:'%'} } } }"}},
        body("Stunting fell by about a point a year between NFHS-3 and NFHS-4, under a "
             "point a year to NFHS-5, and then by 6.2 points to 29.3% in NFHS-6. Wasting "
             "has stayed near 19-21% for almost two decades, and underweight hardly moved "
             "between the last two rounds. All four rounds use the WHO standard. NFHS-6 "
             "figures are provisional fact-sheet values.",
             sm=True),
    ], compact=True),

    C("States", "State stunting, NFHS-5 and NFHS-6", [
        {"t": "chart", "canvas": "nutStateChart",
         "title": "Stunted children under five, selected states, 2019-21 and 2023-24 (%)",
         "source": "NFHS-6 India and State/UT Fact Sheets (provisional), IIPS, May 2026; NFHS-5 values from the same fact sheets",
         "type": "bar",
         "data": {"labels": ["Meghalaya", "Bihar", "Gujarat", "Jharkhand", "Uttar Pradesh",
                             "Madhya Pradesh", "Assam", "Rajasthan", "Maharashtra", "INDIA",
                             "Telangana", "Karnataka", "West Bengal", "Kerala", "Puducherry"],
                  "datasets": [
                      {"label": "NFHS-5 (2019-21)",
                       "data": [46.5, 42.9, 39.0, 39.6, 39.7, 35.7, 35.3, 31.8, 35.2, 35.5,
                                33.1, 35.4, 33.8, 23.4, 20.0],
                       "backgroundColor": "#F59E0B"},
                      {"label": "NFHS-6 (2023-24)",
                       "data": [36.8, 35.6, 35.3, 35.0, 31.5, 31.4, 30.3, 29.6, 29.5, 29.3,
                                27.0, 26.5, 22.4, 20.1, 16.6],
                       "backgroundColor": "#EF4444"}]},
         "options": {"__js__": "{ indexAxis:'y', plugins:{legend:{position:'bottom'}}, scales:{ x:{ min:0, max:50 } } }"}},
        body("In NFHS-6 the highest stunting is in Dadra and Nagar Haveli and Daman and "
             "Diu (37.1%), Meghalaya (36.8%) and Bihar (35.6%); the lowest in Puducherry "
             "(16.6%), Chandigarh (19.0%) and Goa (19.4%). Stunting fell in almost every "
             "state, but rose in Lakshadweep (32.0% to 34.1%) and the Andaman and Nicobar "
             "Islands (22.5% to 26.7%), where samples are small. Manipur was not surveyed "
             "(NFHS-6 State/UT Fact Sheets, 2026).", sm=True),
    ], compact=True),

    C("Anaemia trend", "Anaemia went up between NFHS-4 and NFHS-5", [
        stats([card("59% to 67%", "children 6-59 months", "red", N5 + ", Ch. 10"),
               card("53% to 57%", "women 15-49", "red", N5 + ", Ch. 10"),
               card("23% to 25%", "men 15-49", "amber", N5 + ", Ch. 10")]),
        tw(pp("cyan", "Who and where",
              "Child anaemia peaks at 80% among children aged 12-17 months. Among women it "
              "is 61% for breastfeeding women, 52% for pregnant women and 57% for others. "
              "Among children it ranges from Gujarat (80%) and Madhya Pradesh (73%) to "
              "Kerala (39%); Ladakh records 94% (NFHS-5, Ch. 10)."),
           pp("amber", "Severity",
              "Of children, 29% had mild, 36% moderate and 2% severe anaemia. Of women, "
              "26% mild, 29% moderate and 3% severe. Higher altitude adjustments apply "
              "above 1,000 metres, which affects Ladakh and the hill states (NFHS-5, "
              "Ch. 10).")),
        hbox("As of October 2026 these NFHS-5 figures are the latest: the NFHS-6 fact "
             "sheets of May 2026 contain no anaemia indicator. NFHS measures haemoglobin "
             "in capillary blood from a finger or heel prick; Section 5 sets out why that "
             "method and the WHO cut-offs make these numbers disputed.", "indigo"),
    ], compact=True),

    C("Feeding", "How Indian infants and young children are fed", [
        table(["Practice", "NFHS-6 (2023-24)", "NFHS-5 (2019-21)", "What it means"],
              [["Breastfed within one hour of birth (children under 3)", "50.1%", "41.8%",
                "Improving, from a low base"],
               ["Exclusively breastfed under 6 months", "55.8%", "63.7%",
                "Fell by eight points, a warning sign"],
               ["Solid or semi-solid food plus breastmilk at 6-8 months", "59.5%", "45.9%",
                "Timely start of complementary food improved"],
               ["Adequate diet, all children 6-23 months", "15.3%", "11.0%",
                "Still fewer than one in six"],
               ["Vitamin A dose in last 6 months, 9-35 months", "74.6%", "71.2%",
                "Programme coverage gap remains"],
               ["Minimum dietary diversity, 6-23 months", "not in fact sheet", "23%",
                "Most diets are cereal and milk based"]]),
        body("Sources: NFHS-6 India Fact Sheet (provisional), IIPS, May 2026, which also "
             "gives the NFHS-5 comparison values; NFHS-5 India Report, 2022, Ch. 10, for "
             "dietary diversity. Two numbers stand out. Fewer than one in six Indian "
             "children at the age when stunting accelerates receive a diet adequate in "
             "both diversity and frequency. And exclusive breastfeeding fell, which "
             "matters because wasting is highest in the first months of life. Programme "
             "teams should check the NFHS-6 state sheet for their own state before "
             "drawing a local conclusion.", sm=True),
    ], compact=True),

    C("CNNS", "The Comprehensive National Nutrition Survey, 2016-18", [
        body("The CNNS was run by the Ministry of Health and Family Welfare with UNICEF and "
             "the Population Council. It describes itself as the largest micronutrient "
             "survey ever conducted: 112,316 children and adolescents aged 0-19 were "
             "measured in 30 states, and blood, urine and stool samples were drawn from "
             "51,029 of them (CNNS 2016-18 National Report, 2019, Ch. 2)."),
        tw(pp("cyan", "What makes it different",
              "It covers school-age children (5-9) and adolescents (10-19), who NFHS does "
              "not measure as children. It used venous blood and laboratory methods for "
              "haemoglobin and measured iron, vitamin A, vitamin D, zinc, folate, vitamin "
              "B12 and iodine status directly, plus NCD biomarkers."),
           pp("amber", "Anthropometry",
              "Under-fives: 35% stunted, 17% wasted, 33% underweight. School-age "
              "children: 22% stunted and 23% thin (BMI-for-age below -2 SD). Adolescents: "
              "24% thin and 5% overweight or obese (CNNS 2016-18 National Report, 2019, "
              "Ch. 5).")),
        hbox("Use the CNNS for micronutrients and for older children; use NFHS, now in "
             "its sixth round, for trends and district estimates of under-five "
             "anthropometry.", "green"),
    ], compact=True),

    C("Micronutrients", "Hidden hunger by age group, CNNS 2016-18", [
        {"t": "chart", "canvas": "nutCnnsChart",
         "title": "Prevalence of deficiency by age group, India, 2016-18 (%)",
         "source": "CNNS 2016-18 National Report, MoHFW, UNICEF and Population Council, 2019, Ch. 7",
         "type": "bar",
         "data": {"labels": ["Vitamin A", "Vitamin D", "Zinc", "Vitamin B12", "Folate"],
                  "datasets": [
                      {"label": "Pre-school (1-4)", "data": [18, 14, 19, 14, 23],
                       "backgroundColor": "#0EA5E9"},
                      {"label": "School-age (5-9)", "data": [22, 18, 17, 17, 28],
                       "backgroundColor": "#F59E0B"},
                      {"label": "Adolescents (10-19)", "data": [16, 24, 32, 31, 37],
                       "backgroundColor": "#EF4444"}]},
         "options": {"__js__": "{ plugins:{legend:{position:'bottom'}}, scales:{ y:{ min:0, max:40, title:{display:true,text:'% deficient'} } } }"}},
        body("Adolescents carry the heaviest burden of zinc, vitamin B12 and folate "
             "deficiency. Iodine status was adequate in all three age groups, with median "
             "urinary iodine of 213, 175 and 173 micrograms per litre, the visible "
             "success of salt iodisation; Tamil Nadu sat at the lower limit of excess "
             "intake (CNNS, Ch. 7).", sm=True),
    ], compact=True),

    C("Iron", "Anaemia and iron deficiency are different things", [
        stats([card("41% / 24% / 28%", "anaemic: pre-school, school-age, adolescents",
                    "red", CNNS),
               card("32% / 17% / 22%", "iron deficient (low serum ferritin), same groups",
                    "amber", CNNS)], cols=2),
        tw(pp("cyan", "The gap between them",
              "Some anaemic children are not iron deficient and some iron-deficient "
              "children are not anaemic. Adolescent girls show the sharpest gap with boys: "
              "40% of girls against 18% of boys were anaemic, and 31% of girls against 12% "
              "of boys iron deficient (CNNS 2016-18 National Report, 2019, Ch. 6)."),
           pp("amber", "A counter-intuitive pattern",
              "Children and adolescents in urban areas had a higher prevalence of iron "
              "deficiency than rural ones (CNNS, Ch. 6). Serum ferritin rises with "
              "inflammation, which is why the CNNS-based cut-off study in Section 5 excluded "
              "children with inflammation (Sachdev et al., Lancet Global Health, 2021).")),
        hbox("Iron supplements treat iron deficiency anaemia. If a large share of anaemia "
             "has other causes, more iron alone will not close the gap. That is the policy "
             "stake in the debate in the next section.", "indigo"),
    ], compact=True),

    C("Adolescents", "Adolescents: the missing middle of nutrition policy", [
        body("Programmes for children under five and for pregnant women have deep roots; "
             "adolescents fall between them. Yet adolescence is a second growth spurt, the "
             "time when girls' iron needs rise with menstruation, and for many Indian girls "
             "the years just before a first pregnancy. A thin, anaemic, short adolescent "
             "girl is the mother whose baby is small at birth."),
        table(["Indicator, 10-19 years", "Value", "Source"],
              [["Thin (BMI-for-age below -2 SD)", "24%", "CNNS 2016-18, Ch. 5"],
               ["Overweight or obese (BMI-for-age above +1 SD)", "5%", "CNNS 2016-18, Ch. 5"],
               ["Anaemic, girls / boys", "40% / 18%", "CNNS 2016-18, Ch. 6"],
               ["Zinc deficient", "32%", "CNNS 2016-18, Ch. 7"],
               ["Pre-diabetic (with school-age children)", "about 1 in 10", "CNNS 2016-18, Ch. 8"],
               ["Thin women aged 15-19", "40%", "NFHS-5, Ch. 10"]]),
        hbox("India's Scheme for Adolescent Girls is now part of Mission Saksham Anganwadi "
             "and Poshan 2.0, and Anemia Mukt Bharat names adolescents aged 10-19 as one of "
             "its six target groups (PIB, 6 August 2024).", "green"),
    ], compact=True),

    # ===================== SECTION 05 =====================
    D("05", "Section Five", "The Indian enigma debates"),

    C("The puzzle", "Why are Indian children shorter than children in poorer countries?", [
        body("Indian children are on average shorter than children in sub-Saharan Africa, "
             "a region that is poorer on average and does worse on many other health "
             "indicators. The pattern was dubbed the 'South Asian Enigma' by Ramalingaswami "
             "and colleagues in 1996, as Rohini Pande recounts in her 2013 reply in the "
             "Economic and Political Weekly. The main explanations offered since fall into "
             "four groups."),
        table(["Explanation", "Core claim", "Main proponents"],
              [["Measurement", "The global yardstick overstates Indian stunting",
                "Panagariya, EPW, 2013; Ghosh et al., Indian Pediatrics, 2023"],
               ["Intra-household allocation", "Later-born children, especially girls, get "
                "less", "Jayachandran and Pande, AER, 2017"],
               ["Disease environment", "Open defecation and infection impair growth",
                "Spears, World Bank WP 6351, 2013"],
               ["Maternal status", "Short, thin, young mothers have small babies",
                "Lancet series 2008 and 2013; NFHS-5 gradients"]]),
        hbox("These explanations are not mutually exclusive. The useful question for a "
             "practitioner is how much each accounts for, and which a programme can "
             "change.", "indigo"),
    ], compact=True),

    C("Genes or yardstick", "The measurement argument, and the reply", [
        tw(pp("amber", "Panagariya, 2013",
              "In 'Does India Really Suffer from Worse Child Malnutrition Than Sub-Saharan "
              "Africa?' (EPW, 2013) Arvind Panagariya argued that applying one global "
              "height and weight standard ignores genetic, environmental, cultural and "
              "geographic differences, and called for a better methodology "
              "(as reported by Counterview, October 2013)."),
           pp("cyan", "The reply",
              "Rohini Pande's 'Choice Not Genes' (2013) argued the India-Africa gap "
              "is better explained by household choices. The WHO standards themselves "
              "include a Delhi sample and were built on the premise that well-nourished "
              "children grow similarly across ethnic groups (WHO MGRS Group, Acta "
              "Paediatrica, 2006).")),
        body("A third route keeps the standard and adjusts for parents. "
             "Karlsson and colleagues estimated maternal height-standardised stunting for "
             "67 low- and middle-income countries: average crude prevalence was 27.8% and "
             "standardised prevalence 23.3%, and Guatemala, Bangladesh and Nepal improved "
             "their ranking most after adjustment (J Epidemiol, 2022). Maternal height is itself "
             "partly the product of the mother's own childhood nutrition, so adjusting for "
             "it removes some of what a programme should care about."),
    ], compact=True),

    C("Birth order", "Birth order and son preference: Jayachandran and Pande, 2017", [
        {"t": "chart", "canvas": "nutBirthOrderChart",
         "title": "Stunted children under five by birth order, India, 2019-21 (%)",
         "source": "NFHS-5 India Report, IIPS and ICF, 2022, Table 10.1",
         "type": "bar",
         "data": {"labels": ["1st", "2nd-3rd", "4th-5th", "6th or more"],
                  "datasets": [{"label": "Stunted (%)", "data": [31.5, 36.2, 44.9, 48.6],
                                "backgroundColor": ["#10B981", "#F59E0B", "#EF4444",
                                                    "#B91C1C"]}]},
         "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:55 } } }"}},
        body("Using data on over 168,000 children, Jayachandran and Pande show that "
             "India's height disadvantage relative to Africa increases sharply with birth "
             "order. They attribute the steep gradient to favouritism toward eldest sons, "
             "which shapes fertility and how resources are shared among children; the "
             "gradient is steeper in high son-preference regions and religions, and an "
             "approximate calculation suggests it explains over half the India-Africa gap "
             "in average child height (American Economic Review, 107(9), 2017).", sm=True),
    ], compact=True),

    C("Sanitation", "Open defecation and child height: Spears", [
        body("Dean Spears documented a strong gradient between child height and "
             "sanitation. Across 140 country-years in 65 developing countries, sanitation "
             "alone linearly explains 54% of the variation in children's height, and in "
             "his decomposition open defecation can account for much or all of India's "
             "excess stunting (Spears, World Bank Policy Research Working Paper 6351, "
             "February 2013)."),
        tw(pp("cyan", "District evidence from India",
              "Using HUNGaMA 2011 stunting data and Census 2011 open defecation for 112 "
              "districts, Spears, Ghosh and Cumming found that a 10% increase in open "
              "defecation was associated with a 0.7 percentage point increase in stunting "
              "and severe stunting, and that open defecation could statistically account "
              "for 35-55% of the gap between low- and high-performing districts (PLoS "
              "One, 2013)."),
           pp("amber", "Why density matters",
              "Spears notes that in 2010, 86% of the poorest quintile of South Asians "
              "defecated in the open (WP 6351). Where people live densely, one "
              "household's open defecation contaminates its neighbours' environment, so "
              "the exposure is shared by the whole neighbourhood.")),
        hbox("The authors flag the limit themselves: these are observational and "
             "ecological analyses, vulnerable to residual confounding. Section 9 shows "
             "what randomised household WASH trials found.", "indigo"),
    ], compact=True),

    C("Standards, 2023", "The 2023 argument for customising the WHO standard", [
        body("Ghosh, Majumder, Sachdev, Kurpad and Thomas extracted 10,384 healthy "
             "under-five children, selected by the WHO MGRS criteria, from NFHS-3, NFHS-4, "
             "NFHS-5 and the CNNS. Their mean z-scores were significantly below zero (-0.52 "
             "to -0.79) and the spread of height- and weight-for-height z-scores was wider "
             "than the standard assumes. Applying age-specific corrections reduced NFHS-5 "
             "growth faltering by about half; they report a corrected excess risk of 15.5% "
             "for height-for-age (Indian Pediatrics, 2023)."),
        tw(pp("amber", "The case for",
              "If healthy Indian children do not centre on the WHO median, the standard "
              "overstates the burden, misdirects funds and labels healthy children "
              "malnourished. Planning needs a number that reflects true risk."),
           pp("cyan", "The case against",
              "A 'healthy' subsample in a population with widespread anaemia, infection "
              "and maternal short stature may still be growth-constrained, so its lower "
              "mean may record deprivation. A national yardstick also ends comparability "
              "with every other country and with India's own past.")),
        hbox("For practice: report on the WHO 2006 standard, which NFHS and the DHS Program "
             "use, and note the debate when you interpret levels. Trends measured on one "
             "standard are unaffected by the choice.", "green"),
    ], compact=True),

    C("Cut-offs", "Is anaemia over-diagnosed? The cut-off debate", [
        body("Sachdev and colleagues note that WHO's haemoglobin cut-offs were based on "
             "five studies of predominantly White adults done over 50 years ago. Using a "
             "healthy CNNS subsample of 8,087 children and adolescents (no iron, folate, "
             "B12 or retinol deficiency, no inflammation, no haemoglobin variants), they "
             "derived cut-offs usually 1-2 g/dL lower. Anaemia prevalence across the CNNS "
             "sample fell from 30.0% on WHO cut-offs to 10.8% on theirs (Lancet Global "
             "Health, 2021)."),
        tw(pp("amber", "Women of reproductive age",
              "A 2023 study tracking haemoglobin response to iron-folic acid in Indian "
              "women derived a putative cut-off of 10.8 g/dL (about 11), against the "
              "current adult value of 12 g/dL (Ghosh et al., European Journal of Clinical "
              "Nutrition, 2023)."),
           pp("cyan", "WHO's own revision",
              "WHO's Guideline on haemoglobin cutoffs to define anaemia in individuals and "
              "populations, published 5 March 2024, lowered the threshold for children "
              "aged 6-23 months to 10.5 g/dL and set 10.5 g/dL for the second trimester of "
              "pregnancy (as summarised by Gonzales and Suarez Moreno, Rev Peru Med Exp "
              "Salud Publica, 2024).")),
    ], compact=True),

    C("Blood samples", "Capillary and venous blood tell different stories", [
        tw(pp("red", "NFHS",
              "Capillary blood from a finger or heel prick, read on a portable "
              "haemoglobinometer. Children 6-59 months anaemic: 67.1% (NFHS-5 India "
              "Report, 2022)."),
           pp("cyan", "CNNS",
              "Venous whole blood, analysed with the cyanmethaemoglobin method and "
              "automated counters (CNNS 2016-18 National Report, 2019, Ch. 2 and 6). Kurpad "
              "and Sachdev put its anaemia prevalence at 30.7%, less than half the NFHS "
              "figure (Indian Pediatrics, 2022).")),
        quote("The burden of anemia in Indian children, based on capillary blood sampling, "
              "is believed to be profound and worsening (67.1%) according to the "
              "successive National Family Health Surveys. This might be an overestimate.",
              "Kurpad and Sachdev, Indian Pediatrics, 2022"),
        body("Kurpad and Sachdev add that only about a third of the CNNS anaemia was due to "
             "iron deficiency, and argue that the apparently worsening NFHS figures were "
             "read as a failure of iron supplementation and helped justify mandatory rice "
             "fortification. Their prescription: base prevention policy on the cause of "
             "anaemia, with precision and restraint.", sm=True),
    ], compact=True),

    C("Reading debates", "How to read a measurement debate without taking a side too early", [
        table(["Question to ask", "Applied to stunting", "Applied to anaemia"],
              [["What is the yardstick?", "WHO 2006 standard vs an Indian healthy sample",
                "WHO cut-offs vs Indian 5th percentiles"],
               ["What is the sample?", "MGRS optimal conditions vs selected NFHS children",
                "Venous CNNS vs capillary NFHS"],
               ["What changes if the critic is right?", "Level falls, trend unchanged",
                "Level falls, iron's share of causes matters more"],
               ["What is the policy stake?", "Targets, funding, district rankings",
                "Universal iron, rice fortification, sickle cell risk"],
               ["What does not change?", "Gradients by wealth, birth order, schooling",
                "Large gaps by sex among adolescents"]]),
        body("Measurement debates are often presented as a fight over whether India's "
             "problem is real. A sharper reading: the critics mostly challenge the level, "
             "while the gradients, which tell you who to reach, survive every yardstick. A "
             "practitioner can design for the gradients now and revisit levels when a "
             "consensus forms.", sm=True),
        hbox("Always state the standard, the blood sample type and the cut-off next to any "
             "figure you quote.", "indigo"),
    ], compact=True),

    # ===================== SECTION 06 =====================
    D("06", "Section Six", "The right to food: NFSA 2013 and the PDS"),

    C("Origins", "From a Supreme Court petition to a statute", [
        body("In 2001 the People's Union for Civil Liberties petitioned the Supreme Court, "
             "arguing that the right to life under Article 21 includes the right to food. "
             "In <em>PUCL v Union of India</em>, Writ Petition (Civil) No. 196 of 2001, "
             "the Court converted food schemes into legal entitlements through a series of "
             "interim orders (Birchfield and Corsi, 'The Right to Life Is the Right to Food', "
             "2010)."),
        tw(pp("cyan", "The order of 28 November 2001",
              "Directed states and union territories to provide every child in every "
              "government and government-assisted primary school with a prepared mid-day "
              "meal of at least 300 calories and 8-12 grams of protein each school day for "
              "a minimum of 200 days, and required states giving dry rations to start "
              "cooked meals in half their districts within three months and in the rest "
              "within a further three."),
           pp("green", "The statute",
              "The National Food Security Act 2013 (No. 20 of 2013) received assent on 10 "
              "September 2013 and is deemed in force from 5 July 2013 (s1(3)). Its long "
              "title describes food and nutritional security in a human life cycle "
              "approach.")),
        hbox("Much of what the 2001 orders demanded through the courts now sits in "
             "sections 4 to 6 of the Act and in Schedule II.", "indigo"),
    ], compact=True),

    C("Section 3", "Who is entitled to what: the core grain entitlement", [
        table(["Provision", "What it says"],
              [["s3(1)", "Each person in a priority household: 5 kg of foodgrains per month "
                "at Schedule I prices"],
               ["s3(1), proviso", "Antyodaya Anna Yojana households: 35 kg per household "
                "per month"],
               ["s3(2)", "Coverage up to 75% of the rural and 50% of the urban population"],
               ["s9", "Centre fixes each state's coverage, using published Census population "
                "figures"],
               ["s10", "States identify AAY and priority households under their own "
                "guidelines"],
               ["s11", "States must publish and display the list of eligible households"],
               ["Schedule I", "Rs 3, 2 and 1 per kg for rice, wheat and coarse grains for "
                "three years, then not above MSP"]]),
        body("Source: National Food Security Act 2013. State coverage ratios were "
             "computed by the erstwhile Planning Commission from NSS consumption data for "
             "2011-12; the maximum coverage is 81.34 crore persons, of whom around 80 crore "
             "are covered (NFSA portal, Department of Food and Public Distribution, "
             "accessed October 2026). Because s9 ties coverage to the latest published "
             "Census, the 2027 Census, with its 1 March 2027 reference date, will reopen "
             "the question of how many people each state may cover.", sm=True),
    ], compact=True),

    C("Life cycle", "Sections 4 to 6: mothers and children", [
        tw(pp("cyan", "s4: pregnant women and lactating mothers",
              "A free meal through the local anganwadi during pregnancy and six months "
              "after childbirth, meeting Schedule II standards; and maternity benefit of "
              "not less than Rs 6,000 in instalments. Women in regular government or PSU "
              "employment are excluded from the cash benefit."),
           pp("green", "s5 and s6: children",
              "Children 6 months to 6 years: an age-appropriate free meal through the "
              "anganwadi; exclusive breastfeeding promoted below 6 months. Children up to "
              "class VIII or aged 6-14: one free mid-day meal every school day. s6: "
              "anganwadis must identify malnourished children and feed them free.")),
        table(["Schedule II category", "Meal type", "Calories (kcal)", "Protein (g)"],
              [["Children 6 months-3 years", "Take home ration", "500", "12-15"],
               ["Children 3-6 years", "Morning snack and hot cooked meal", "500", "12-15"],
               ["Malnourished children 6 months-6 years", "Take home ration", "800",
                "20-25"],
               ["Lower primary", "Hot cooked meal", "450", "12"],
               ["Upper primary", "Hot cooked meal", "700", "20"],
               ["Pregnant women and lactating mothers", "Take home ration", "600", "18-20"]]),
    ], compact=True),

    C("Free grain", "From subsidised to free: PMGKAY", [
        body("The Pradhan Mantri Garib Kalyan Anna Yojana began as a COVID-19 relief "
             "measure. On 29 November 2023 the Cabinet decided to provide free foodgrains "
             "to about 81.35 crore beneficiaries for five years from 1 January 2024, at an "
             "estimated food subsidy of about Rs 11.80 lakh crore, through more than 5 "
             "lakh Fair Price Shops (PIB, 29 November 2023)."),
        stats([card("81.35 crore", "people entitled to free grain", "cyan",
                    "PIB, 29 November 2023"),
               card("Rs 11.80 lakh crore", "estimated subsidy over five years", "amber",
                    "PIB, 29 November 2023"),
               card("31 Dec 2028", "free grain runs to the end of 2028", "indigo",
                    "PIB, 29 November 2023 (five years from 1 January 2024)")]),
        hbox("Free cereal guarantees calories. It does less for the diversity gap seen in "
             "Section 4, which is why s12(2)(f) of the Act asks for diversification of PDS "
             "commodities over time.", "amber"),
    ], compact=True),

    C("Women and allowance", "Section 13 and section 8: two provisions with teeth", [
        tw(pp("green", "s13: women as heads of household",
              "The eldest woman aged 18 or above in every eligible household is the head "
              "of household for issuing the ration card. If there is no adult woman but a "
              "younger girl, the eldest man holds the card until she turns 18. The portal "
              "presents this as a measure for women (NFSA 2013, s13)."),
           pp("cyan", "s8: food security allowance",
              "If the entitled grain or meals are not supplied, the person is entitled to "
              "a food security allowance from the state government, under the Food "
              "Security Allowance Rules, 2015 (NFSA 2013, s8; NFSA portal).")),
        body("Section 13 matters for nutrition because it puts the household's food "
             "entitlement in a woman's name; Gender &amp; Development 101 covers the "
             "household bargaining research behind that choice. Section 8 matters because it turns a failure of supply into "
             "a claim against the state. Few beneficiaries know either provision, so an "
             "NGO's first nutrition-sensitive step in a block can be a ration card audit: "
             "whose name is on the card, and was the allowance paid when the shop was "
             "empty?"),
    ], compact=True),

    C("Accountability", "Grievance redress and accountability built into the Act", [
        table(["Section", "Mechanism", "Practical use"],
              [["s14", "Internal grievance redressal: call centres, helplines, nodal officers",
                "First port of call for a missing ration"],
               ["s15", "District Grievance Redressal Officer for each district",
                "Hears complaints on grain and meals; appeal lies to the State Commission"],
               ["s16", "State Food Commission: Chairperson and five members, with SC and ST "
                "representation", "Monitors implementation, hears appeals"],
               ["s28", "Periodic social audits of fair price shops and schemes",
                "Community scrutiny, published findings"],
               ["s29", "Vigilance Committees at state, district, block and shop level",
                "Report violations and malpractice to the DGRO"],
               ["s33", "Penalty on officials who fail to provide recommended relief",
                "Imposed by the State Commission"]]),
        body("Source: National Food Security Act 2013, ss 14-16, 28, 29 and 33. These "
             "mechanisms exist on paper in every state; their functioning varies widely. "
             "Governance &amp; Accountability 101 covers social audit methods.", sm=True),
    ], compact=True),

    C("PDS reform", "Digitising the PDS: what has changed", [
        stats([card("20.55 crore", "ration cards, data digitised", "cyan",
                    "PIB, DFPD Year End Review, 31 Dec 2025"),
               card("99.9%", "ration cards Aadhaar-seeded (at least one member)", "cyan",
                    "PIB, 31 Dec 2025"),
               card("99.8%", "of 5.51 lakh Fair Price Shops on ePoS devices", "cyan",
                    "PIB, 31 Dec 2025")]),
        tw(pp("green", "One Nation One Ration Card",
              "Inter-state portability started in 4 states in August 2019 and covers all "
              "36 states and UTs and about 79.8 crore NFSA beneficiaries. More than 195.9 "
              "crore portability transactions had been recorded by the end of 2025 (PIB, "
              "31 December 2025). Migrant workers can draw rations where they work."),
           pp("amber", "Legal basis and options",
              "Section 12 lists reforms: doorstep delivery, end-to-end computerisation, "
              "Aadhaar for targeting, transparency, preference for panchayats, SHGs and "
              "women's collectives as shop managers, and cash transfers or food coupons. "
              "Cash transfer of food subsidy started in Chandigarh and Puducherry in "
              "September 2015 (NFSA portal).")),
    ], compact=True),

    C("PDS debates", "Four live debates about the PDS", [
        table(["Debate", "One side", "The other side", "What to measure"],
              [["Targeting", "Universal coverage cuts exclusion errors",
                "Targeting saves fiscal space for other nutrition spending",
                "Exclusion of eligible households from lists"],
               ["Biometric authentication", "Reduces identity fraud and ghost cards",
                "Failed fingerprints deny rations to the eligible",
                "Share of transactions refused, by reason"],
               ["Cash or kind", "Cash widens choice, cuts handling costs",
                "Grain is protected from price rises and diversion within the home",
                "Food spending and diet diversity after the switch"],
               ["Cereals or diversity", "Cheap cereals are the most efficient calorie "
                "transfer", "Diets need pulses, oils, eggs, millets",
                "Dietary diversity of beneficiaries"]]),
        body("Each side has empirical support somewhere, and the answer differs by state "
             "capacity. For any reform proposal, ask what happens to the poorest household "
             "in the worst-run block, since that is where nutrition is decided. The NFSA "
             "itself leaves room: s12(2)(h) allows cash or coupons only in areas and in a "
             "manner the Centre prescribes.", sm=True),
    ], compact=True),

    # ===================== SECTION 07 =====================
    D("07", "Section Seven", "Programmes for mothers and children"),

    C("ICDS to Poshan 2.0", "From ICDS, 1975, to Mission Saksham Anganwadi and Poshan 2.0", [
        body("The Integrated Child Development Services, launched on 2 October 1975, built "
             "the Anganwadi network that delivers supplementary nutrition, health services "
             "and early childhood care (PIB, 11 October 2024). The Union Budget 2021-22 "
             "consolidated Anganwadi Services, the Scheme for Adolescent Girls and POSHAN "
             "Abhiyaan into Mission Saksham Anganwadi and Poshan 2.0 (PIB backgrounder, 14 "
             "April 2026)."),
        stats([card("8.69 crore", "women, adolescent girls and children benefited, as on 30 "
                    "Nov 2025", "cyan", "PIB, MWCD Year End Review, 9 Jan 2026"),
               card("~14 lakh", "Anganwadi Centres tracked, March 2026", "cyan",
                    "PIB backgrounder, 14 Apr 2026"),
               card("94,077", "of 2 lakh approved centres upgraded to Saksham Anganwadi",
                    "amber", "PIB, MWCD Year End Review, 9 Jan 2026")]),
        hbox("The mission's three verticals are nutrition support, early childhood care "
             "and education, and Anganwadi infrastructure (PIB backgrounder, 14 April "
             "2026).", "indigo"),
    ], compact=True),

    C("Supplementary nutrition", "What the Anganwadi provides, and to whom", [
        tw(pp("cyan", "Norms",
              "Supplementary nutrition goes to children 6 months to 6 years, pregnant "
              "women, lactating mothers and adolescent girls under the norms in Schedule "
              "II of the NFSA. The norms were revised in January 2023 from mainly calorie "
              "targets toward diet diversity, quality protein, healthy fats and "
              "micronutrients (PIB backgrounder, 14 April 2026)."),
           pp("amber", "Acute malnutrition",
              "MWCD and MoHFW issued a joint Protocol for Management of Malnutrition in "
              "Children. Anganwadi Workers screen children; those with severe acute "
              "malnutrition and medical complications go to Nutrition Rehabilitation "
              "Centres, and those without complications are managed at home with local "
              "nutritious food and medical support (PIB backgrounder, 14 April 2026).")),
        body("The design question at the centre is take home ration versus hot cooked "
             "meal. Hot cooked meals bring children to the centre and are eaten by the "
             "child; take home rations reach children under three who do not attend, but "
             "can be shared across the household, so monitoring should check who eats them. Poshan 2.0 added face recognition "
             "verification for take home ration distribution in the Poshan Tracker (PIB, 5 "
             "December 2025). Monitor how many eligible women are turned away when "
             "verification fails, since that is a new point of exclusion."),
    ], compact=True),

    C("POSHAN Abhiyaan", "POSHAN Abhiyaan, 2018: targets and convergence", [
        body("The Cabinet approved the National Nutrition Mission on 30 November 2017 with "
             "a three-year budget of Rs 9,046.17 crore from 2017-18 (PIB, 1 December 2017). "
             "The Prime Minister launched it at Jhunjhunu, Rajasthan, on International "
             "Women's Day, 8 March 2018 (PIB, 8 March 2018). It brings more than 26 "
             "ministries and departments under one framework (PIB backgrounder, 14 April "
             "2026)."),
        table(["Target (per year)", "Reduction", "Mission ambition"],
              [["Stunting", "2%", "From 38.4% (NFHS-4) to 25% by 2022"],
               ["Undernutrition", "2%", ""],
               ["Anaemia (children, women, adolescent girls)", "3%", ""],
               ["Low birth weight", "2%", ""]]),
        hbox("Outcome so far: NFHS-5 (2019-21) measured stunting at 35.5% and NFHS-6 "
             "(2023-24) at 29.3% (NFHS-6 India Fact Sheet, 2026), short of the 25% "
             "ambition. The mission's lasting contributions are its convergence "
             "plans, height measurement at Anganwadis, the ICT tracker and the annual "
             "Poshan Maah campaign.", "amber"),
    ], compact=True),

    C("Maternity benefit", "Maternity benefits: the NFSA promise and PMMVY", [
        tw(pp("cyan", "The legal floor",
              "NFSA s4(b) entitles every pregnant woman and lactating mother, outside "
              "regular government employment, to a maternity benefit of not less than Rs "
              "6,000, in instalments prescribed by the Centre. It exists to compensate "
              "partly for lost wages and to supplement nutrition (NFSA portal)."),
           pp("green", "The scheme",
              "Pradhan Mantri Matru Vandana Yojana was implemented in 2017 to deliver "
              "maternity benefits by direct cash transfer (PIB backgrounder, 14 April "
              "2026). By the end of 2025, 4.26 crore beneficiaries had received Rs 20,060 "
              "crore. Face authentication became mandatory for new PMMVY enrolments from "
              "21 May 2025 (PIB, MWCD Year End Review, 9 January 2026).")),
        body("Why cash for mothers matters for nutrition: a pregnant woman who must keep "
             "working in the last trimester eats less and rests less, and Section 3 showed "
             "how much stunting starts before birth. The meta-analyses in Section 9 find "
             "that cash transfers improve diet diversity and child height modestly. Check, "
             "for any scheme, whether the amount, eligibility and documentation meet the "
             "s4(b) floor for all pregnant women the Act covers."),
    ], compact=True),

    C("PM POSHAN", "PM POSHAN: the school meal", [
        body("In September 2021 the Cabinet approved the national scheme for PM POSHAN in "
             "schools, formerly the Mid-Day Meal Scheme, for 2021-22 to 2025-26. It covered "
             "about 11.80 crore children in 11.20 lakh government and government-aided "
             "schools, with a Central outlay of Rs 54,061.73 crore, Rs 31,733.17 crore from "
             "states and UTs and about Rs 45,000 crore of foodgrains (PIB, 29 September "
             "2021)."),
        tw(pp("green", "What changed in 2021",
              "Extension to pre-primary Bal Vatikas in government primary schools; Tithi "
              "Bhojan, where communities provide special food on festivals; and a "
              "mandatory social audit in every district (PIB, 29 September 2021)."),
           pp("amber", "Status (as of October 2026)",
              "The approved period ended with 2025-26. Check the Ministry of Education's "
              "current approval before citing the scheme's present outlay or coverage. The "
              "legal entitlement itself does not lapse: it sits in NFSA s5(1)(b).")),
        hbox("School meals are a nutrition-sensitive and education programme at once. The "
             "entitlement to a cooked meal was won through <em>PUCL v Union of India</em> "
             "(2001) before it was written into the 2013 Act.", "indigo"),
    ], compact=True),

    C("Convergence", "Who does what: nutrition is split across ministries", [
        table(["Ministry or body", "Main nutrition responsibilities"],
              [["Women and Child Development", "Mission Saksham Anganwadi and Poshan 2.0, "
                "POSHAN Abhiyaan, Poshan Tracker, PMMVY"],
               ["Health and Family Welfare", "Anemia Mukt Bharat, NFHS, Nutrition "
                "Rehabilitation Centres, joint malnutrition protocol with MWCD"],
               ["Food and Public Distribution", "NFSA, PDS and PMGKAY, One Nation One Ration "
                "Card, rice fortification in the PDS"],
               ["Education", "PM POSHAN school meals"],
               ["FSSAI", "Fortification of Foods Regulations 2018, Eat Right India"],
               ["States and UTs", "Identify households (NFSA s10), run Anganwadis and "
                "schools, appoint DGROs and State Food Commissions"]]),
        body("Sources: PIB releases cited in Sections 6 to 8; NFSA 2013. POSHAN Abhiyaan "
             "exists because this split produced many schemes that did not connect: the "
             "2017 Cabinet note said there was 'no dearth of schemes' and a lack of "
             "linkage between them (PIB, 1 December 2017). At district level, the "
             "practical test of convergence is whether the Anganwadi Worker, the ASHA, the "
             "ANM and the fair price shop dealer share one list of the same households and "
             "meet on a fixed day.", sm=True),
    ], compact=True),

    C("Delivery gaps", "Where programmes lose children between design and delivery", [
        flow(["ELIGIBLE: child or mother entitled under NFSA",
              "ENROLLED: registered at the Anganwadi or school",
              "SERVED: ration or meal actually received",
              "CONSUMED: eaten by the intended person",
              "EFFECTIVE: diet and growth improve"]),
        body("Each arrow is a place to lose people. Enrolment drops for migrant families "
             "and for children under three who do not attend centres. Service drops when "
             "supplies are late or verification fails. Consumption drops when a take home "
             "ration is shared or sold. Effect drops when the food lacks protein and "
             "micronutrients or the child is repeatedly ill. Monitoring that counts only "
             "the first two steps will report success while children stay short."),
        hbox("Programme Design 101 shows how to build a theory of change around a cascade "
             "like this and choose an indicator for each step.", "green"),
    ], compact=True),
]

FSSAI = "FSS (Fortification of Foods) Regulations, 2018, FSSAI compendium, 30.09.2021"

SLIDES_C = [

    # ===================== SECTION 08 =====================
    D("08", "Section Eight", "Anaemia, micronutrients and fortification"),

    C("Anemia Mukt Bharat", "Anemia Mukt Bharat, 2018: the 6x6x6 strategy", [
        body("Anemia Mukt Bharat was launched in 2018 to reduce anaemia across the life "
             "cycle (PIB explainer, 18 April 2025). It is implemented in all villages, "
             "blocks and districts through existing platforms, building on the National "
             "Iron Plus Initiative and Weekly Iron Folic Acid Supplementation for "
             "adolescents."),
        table(["Six beneficiary groups", "Six interventions"],
              [["Children 6-59 months", "Prophylactic iron folic acid supplementation"],
               ["Children 5-9 years", "Periodic deworming"],
               ["Adolescents 10-19 years", "Year-round behaviour change communication"],
               ["Women of reproductive age 15-49", "Testing with digital haemoglobinometers "
                "and point-of-care treatment"],
               ["Pregnant women", "Iron folic acid fortified foods in public programmes"],
               ["Lactating women", "Addressing non-nutritional causes in endemic pockets"]]),
        body("The six institutional mechanisms include inter-ministerial coordination, "
             "convergence with other ministries, supply chain strengthening, a National "
             "Centre of Excellence and Advanced Research on Anaemia Control, and the AMB "
             "dashboard (PIB, 6 August 2024).", sm=True),
    ], compact=True),

    C("AMB in practice", "What it takes to make iron supplementation work", [
        tw(pp("cyan", "Supply and compliance",
              "Supplementation works only if tablets or syrup reach people every week or "
              "day and are taken. One of the six interventions is year-round behaviour "
              "change communication to improve compliance with iron folic acid and "
              "deworming (PIB, 18 April 2025). Mothers who took IFA for 100 days or more "
              "in pregnancy rose from 44.1% to 54.9% between NFHS-5 and NFHS-6 (NFHS-6 "
              "India Fact Sheet, 2026). Track doses consumed as well as doses "
              "distributed."),
           pp("amber", "Causes beyond iron",
              "The strategy targets non-nutritional causes in endemic pockets, with a "
              "special focus on malaria, haemoglobinopathies and fluorosis (PIB, 18 April "
              "2025). "
              "The CNNS showed iron deficiency explains only part of anaemia, and NFHS-5 "
              "found deworming reached only 30% of children 6-59 months (CNNS 2016-18; "
              "NFHS-5, Ch. 10).")),
        body("NFHS-5 anaemia rose while the strategy ran, which supporters read as a call "
             "for more iron and critics read as evidence that the capillary measure and the "
             "cut-offs overstate the problem (Section 5). A district team does not need to "
             "settle that debate to act sensibly: test with a reliable method, find out "
             "what share of anaemic people are iron deficient, treat severe anaemia in "
             "pregnancy urgently, and screen for haemoglobin disorders where they are "
             "common before universal iron."),
        hbox("Anaemia is a symptom with several causes. A single-cause programme will "
             "plateau.", "indigo"),
    ], compact=True),

    C("Fortification law", "The FSSAI Fortification of Foods Regulations, 2018", [
        term("Fortification (reg. 2(1)(b))",
             "Deliberately increasing the content of essential micronutrients in a food so "
             "as to improve its nutritional quality and to provide public health benefit "
             "with minimal risk to health."),
        table(["Regulation", "What it provides"],
              [["Reg. 1(2)", "In force on publication; businesses to comply by 1 January 2019"],
               ["Reg. 2(1)(h)", "Staple foods include rice, wheat, wheat flour, atta, maida, "
                "oil, salt and milk"],
               ["Reg. 3(2)", "Mandatory fortification must rest on the severity and extent of "
                "public health need shown by accepted scientific evidence"],
               ["Reg. 3(3)", "FSSAI may specify mandatory fortification of a staple on the "
                "direction of the Government of India"],
               ["Reg. 7(2)", "Label must say 'fortified with ...', carry the +F logo, and "
                "may add 'Sampoorna Poshan Swasth Jeevan'"],
               ["Reg. 7(4)", "Iron-fortified food must carry a thalassaemia and sickle cell "
                "advisory (amended from 27 August 2021)"]]),
        body("Source: Food Safety and Standards (Fortification of Foods) Regulations, 2018, "
             "made under the Food Safety and Standards Act 2006, FSSAI compendium version "
             "III, 30 September 2021.", sm=True),
    ], compact=True),

    C("Rice fortification", "Fortified rice in every government scheme", [
        flow(["2019-22: pilot in 15 states; 4.30 lakh tonnes distributed in 11 states",
              "Aug 2021: Prime Minister announces fortified rice in welfare schemes",
              "2021-24: phased rollout, ICDS and PM POSHAN first, then TPDS",
              "March 2024: 100% of rice in government schemes fortified",
              "Oct 2024: Cabinet extends supply to December 2028"]),
        body("Fortified rice kernels carrying iron, folic acid and vitamin B12 are blended "
             "with ordinary custom-milled rice to FSSAI standards. About 406 lakh tonnes "
             "were distributed through the PDS between 2019-20 and 31 March 2024. The "
             "Cabinet made the initiative a 100% centrally funded Central Sector "
             "Initiative, estimated at Rs 2,565 crore a year (PIB, 11 October 2024)."),
        stats([card("28-42.5 mg", "iron per kg of rice (ferric pyrophosphate)", "cyan", FSSAI),
               card("65%", "of India's population for whom rice is a staple, per PIB",
                    "amber", "PIB, 11 October 2024")]),
    ], compact=True),

    C("Fortification debate", "The case for and against mandatory iron in rice", [
        tw(pp("green", "The government's case",
              "Rice reaches most poor households through the PDS, so fortifying it "
              "delivers micronutrients without changing behaviour. The PIB note cites a WHO "
              "meta-analysis that rice fortification can reduce the risk of iron "
              "deficiency by 35%, and estimates 16.6 million DALYs averted a year (PIB, 11 "
              "October 2024)."),
           pp("red", "The critics' case",
              "If the true prevalence of iron deficiency anaemia is only about 10%, adding "
              "iron to everyone's staple has limited benefit (Kurpad and Sachdev, Indian "
              "Pediatrics, 2022). People with sickle cell disease are advised by FSSAI's "
              "own label rule not to consume iron-fortified food, yet the PDS supplies "
              "fortified rice to all (FSS Fortification Regulations, reg. 7(4)).")),
        body("For a practitioner the actionable points are narrow. In districts with a "
             "high burden of sickle cell disease or thalassaemia, find out how affected "
             "households are told about the advisory and what alternative they receive. "
             "Everywhere, measure whether fortified kernels are actually present in the "
             "rice that reaches the household, since blending happens at the mill. Iron "
             "status, measured alongside anaemia, is the outcome that shows whether "
             "fortification works."),
    ], compact=True),

    C("What worked", "The fortification that worked: iodised salt", [
        body("Salt iodisation is the clearest fortification success in South Asia. The "
             "CNNS found adequate iodine status in all three age groups, with median "
             "urinary iodine concentrations of 213, 175 and 173 micrograms per litre, and "
             "adequate levels in every state except Tamil Nadu, which sat at the lower limit "
             "of excess intake (CNNS 2016-18 National Report, 2019, Ch. 7). NFHS-6 found "
             "94.2% of households using iodised salt (NFHS-6 India Fact Sheet, 2026). The "
             "PIB note on "
             "rice fortification cites iodised salt as the precedent for reducing goitre "
             "(PIB, 11 October 2024)."),
        table(["Vehicle", "Fortificants under the 2018 Regulations"],
              [["Salt", "Iodine; double fortified salt adds iron (850-1,100 ppm)"],
               ["Edible oil", "Vitamin A and vitamin D"],
               ["Rice", "Iron, folic acid, vitamin B12"],
               ["Atta (wheat flour)", "Iron, folic acid and vitamin B12, with optional zinc, "
                "vitamin A and B vitamins"],
               ["Milk", "Vitamin A and vitamin D"]]),
        body("Source: " + FSSAI + ". Why salt worked: one cheap nutrient, a vehicle "
             "everyone eats in steady amounts, few producers to regulate, and a deficiency "
             "that the nutrient alone corrects. Iron in rice meets fewer of those "
             "conditions.", sm=True),
    ], compact=True),

    C("Eat Right India", "Eat Right India: the food environment and the second burden", [
        body("FSSAI launched Eat Right India in July 2018 to promote safe, healthy and "
             "sustainable food through regulation, capacity building, collaboration and "
             "consumer awareness. It includes a campaign to remove industrial trans fats "
             "from the food chain, hygiene ratings and certification of railway stations "
             "and street food hubs (PIB, 9 July 2025)."),
        stats([card("12 lakh+", "food handlers trained under FoSTaC", "cyan",
                    "PIB, 9 July 2025 (as of 6 July 2025)"),
               card("284", "Eat Right Stations certified", "cyan", "PIB, 9 July 2025"),
               card("249", "Clean Street Food Hubs certified", "cyan", "PIB, 9 July 2025")]),
        hbox("Eat Right India addresses the second half of the double burden: food "
             "safety, fats, sugar and salt. It matters most for urban and richer groups, "
             "where NFHS-5 found overweight among women at 33% in urban areas and 39% in "
             "the richest quintile. Child undernutrition programmes rarely touch it; a "
             "double-duty plan needs both.", "amber"),
    ], compact=True),

    # ===================== SECTION 09 =====================
    D("09", "Section Nine", "What works: the intervention evidence"),

    C("Lancet 2013", "What ten direct interventions could and could not do", [
        body("The 2013 Lancet series updated the evidence on interventions for maternal "
             "and child undernutrition and modelled their effect in the 34 countries that "
             "hold 90% of the world's stunted children (Bhutta et al., Lancet, 2013)."),
        stats([card("15%", "fewer deaths of children under five if ten interventions reach "
                    "90% coverage", "green", "Bhutta et al., Lancet, 2013"),
               card("about 1/5", "of the stunting burden averted by the same package",
                    "amber", "Bhutta et al., Lancet, 2013"),
               card("Int$9.6 bn", "additional cost per year in the 34 countries", "cyan",
                    "Bhutta et al., Lancet, 2013")]),
        body("Two messages follow. First, the direct interventions save lives at a cost "
             "that is small relative to health budgets, so coverage is the binding "
             "constraint. Second, even universal coverage leaves most stunting in place, "
             "which is why the authors call for linking direct interventions with "
             "women's status, agriculture, food systems, education, employment, "
             "social protection and safety nets.", sm=True),
    ], compact=True),

    C("2021 update", "The 2021 update: what the evidence now supports", [
        table(["Intervention", "What the 2021 review found"],
              [["Antenatal multiple micronutrient supplements", "Stronger evidence of fewer "
                "stillbirths, low birthweight and small-for-gestational-age babies"],
               ["Supplementary food in food-insecure settings", "Evidence continues to "
                "support provision"],
               ["Community management of acute malnutrition", "Supported, including locally "
                "produced therapeutic and supplementary foods"],
               ["Small-quantity lipid-based nutrient supplements, 6-23 months",
                "Positive effects on child growth"],
               ["Childhood obesity prevention", "Integrated diet, exercise and behavioural "
                "therapy most effective; little LMIC evidence"],
               ["Indirect strategies", "Malaria prevention, preconception care and WASH "
                "promotion bring nutritional benefits"]]),
        body("Source: Keats et al., Effective interventions to address maternal and child "
             "malnutrition: an update of the evidence, Lancet Child and Adolescent Health, "
             "2021. The authors stress that the bigger problem is coverage, especially of "
             "the most vulnerable, and the growing double burden.", sm=True),
    ], compact=True),

    C("Feeding counselling", "Behaviour change at scale: Alive &amp; Thrive in Bangladesh", [
        body("Alive &amp; Thrive combined intensive interpersonal counselling by frontline "
             "workers, mass media and community mobilisation, with counselling delivered "
             "through a large non-governmental health programme. Twenty sub-districts were randomised to the intensive "
             "package or a lighter one, with surveys in 2010 and 2014."),
        tw(pp("green", "Breastfeeding",
              "Exclusive breastfeeding in the previous 24 hours rose from 48.5% to 87.6% in "
              "the intensive group, a difference-in-differences effect of 36.2 percentage "
              "points; early initiation rose 16.7 points more than in comparison areas "
              "(Menon et al., PLoS Medicine, 2016)."),
           pp("amber", "Complementary feeding and growth",
              "Minimum acceptable diet improved 22.0 points more, reaching 50.4%, and "
              "iron-rich food consumption 24.6 points more. Stunting fell in both groups "
              "by similar amounts, which the authors attribute to rapid secular "
              "improvement across Bangladesh (Menon et al., Journal of Nutrition, 2016).")),
        hbox("Counselling changed feeding a great deal and height little within four years. "
             "Behaviour change is necessary for growth, and it works faster on practices "
             "than on outcomes. Set targets accordingly.", "indigo"),
    ], compact=True),

    C("Maternal nutrition", "Adding nutrition to antenatal care: Bangladesh, 2015-16", [
        body("A second Alive &amp; Thrive evaluation integrated nutrition counselling, "
             "community mobilisation, free micronutrient supplements and weight-gain "
             "monitoring into an existing maternal, neonatal and child health programme in "
             "Bangladesh, and compared it with standard antenatal care in a "
             "cluster-randomised design (Nguyen et al., Journal of Nutrition, 2017)."),
        stats([card("+30 pp", "women eating 5 or more food groups a day", "green",
                    "Nguyen et al., J Nutr, 2017"),
               card("+9.8 pp", "consumption of iron and folic acid", "green",
                    "Nguyen et al., J Nutr, 2017"),
               card("+31 pp", "exclusive breastfeeding", "green",
                    "Nguyen et al., J Nutr, 2017")]),
        body("Coverage made the difference: more than 90% of women in the intervention "
             "group were visited at home for counselling. The Indian equivalent would be "
             "a home visit schedule for Anganwadi Workers and ASHAs with nutrition "
             "content; Poshan Tracker's home visit scheduler, integrated in April 2026, "
             "plans 23 structured visits from pregnancy to age three (PIB backgrounder, 14 "
             "April 2026). Whether the visits happen and what is said in them will "
             "decide whether it works.", sm=True),
    ], compact=True),

    C("Cash", "Cash transfers and child nutrition: two meta-analyses", [
        table(["Outcome", "Manley et al., 2020 (74 studies to 2018)",
               "Manley, Alderman and Gentilini, 2022 (129 estimates)"],
              [["Height-for-age z-score", "+0.03", "+0.024"],
               ["Stunting", "-2.1 percentage points", "-1.35 percentage points"],
               ["Wasting", "Not significant", "-1.31 percentage points"],
               ["Animal-source foods", "+4.5 points", "+6.72 points"],
               ["Dietary diversity", "+0.73", "+0.55"],
               ["Diarrhoea", "-2.7 points", "-1.74 points"]]),
        body("Sources: Manley et al., BMJ Global Health, 2020; Manley, Alderman and "
             "Gentilini, BMJ Global Health, 2022. Both cover programmes targeted to "
             "households with young children in countries below US$10,000 GDP per capita. "
             "The pattern is consistent: cash improves diets and reduces stunting, but by "
             "small amounts. The 2022 review found that well-targeted behaviour change "
             "communication alongside cash improved height-for-age.", sm=True),
        hbox("For India this bears on PMMVY, state maternity schemes and debates on "
             "converting the PDS to cash: cash helps diets, and it helps more with "
             "counselling attached.", "indigo"),
    ], compact=True),

    C("WASH trials", "Three large WASH trials, and a surprise", [
        table(["Trial", "Setting", "Household WASH effect on growth",
               "Nutrition arm effect on length-for-age"],
              [["WASH Benefits Bangladesh", "5,551 pregnant women, 720 clusters, rural "
                "Bangladesh", "None", "+0.25 z"],
               ["WASH Benefits Kenya", "8,246 women, 702 clusters, rural Kenya", "None",
                "+0.13 z"],
               ["SHINE", "5,280 women, 211 clusters, rural Zimbabwe", "None",
                "+0.16 z; stunting 35% to 27%"]]),
        body("Sources: Luby et al., Lancet Global Health, 2018; Null et al., Lancet Global "
             "Health, 2018; Humphrey et al., Lancet Global Health, 2019. In Bangladesh, "
             "sanitation, handwashing and nutrition reduced diarrhoea while water treatment "
             "did not; in Kenya no intervention reduced diarrhoea. Combining WASH with "
             "nutrition added nothing to growth beyond nutrition alone in all three.",
             sm=True),
        hbox("These trials tested household-level, elementary WASH: improved latrines, "
             "handwashing stations, chlorine. They did not test what Spears' work points "
             "to, which is a community where nobody defecates in the open.", "amber"),
    ], compact=True),

    C("Reading nulls", "What the WASH null results do and do not show", [
        tw(pp("cyan", "What they show",
              "Household-level elementary WASH, in rural settings with high background "
              "contamination, is unlikely to reduce stunting or anaemia, and adding it to "
              "feeding interventions does not add growth (Humphrey et al., 2019). The Kenya "
              "authors suggest higher adherence or lower baseline sanitation coverage "
              "might have made a difference (Null et al., 2018)."),
           pp("amber", "What they do not show",
              "They do not test community-wide sanitation, piped water, or the dense "
              "settings where open defecation is a neighbourhood exposure. Observational "
              "district evidence from India and these trials ask different questions, so "
              "both can be right (Spears, Ghosh and Cumming, 2013; Spears, 2013).")),
        body("This is a general lesson about evidence. A null result in a well-run "
             "trial is strong evidence about the intervention tested at the intensity "
             "tested. It is weak evidence about a different intervention with the same "
             "label. Before citing a trial to stop or start a programme, check that the "
             "programme you are deciding on is the thing the trial evaluated. Causal "
             "Inference 101 and Impact Evaluation 101 cover external validity."),
    ], compact=True),

    C("Biofortification", "Biofortification: breeding nutrients into the crop", [
        body("Biofortification breeds staple crops with higher micronutrient content, so "
             "farmers grow the nutrients without a processing step. The FSSAI regulations "
             "direct the Food Authority to encourage fortification including through "
             "conventional breeding or hybridisation (reg. 8(1))."),
        tw(pp("green", "Evidence from Maharashtra",
              "In a six-month randomised trial among 246 children aged 12-16, iron-"
              "biofortified pearl millet significantly improved serum ferritin and total "
              "body iron by four months. Iron-deficient children were 1.64 times more "
              "likely to become iron replete by six months (Finkelstein et al., Journal "
              "of Nutrition, 2015)."),
           pp("amber", "Limits",
              "Efficacy in a feeding trial, where children eat the millet daily, is "
              "different from effectiveness when farmers must choose to grow it and "
              "households to eat it. A later protocol tested iron- and zinc-"
              "biofortified pearl millet among 200 children aged 12-18 months in Mumbai "
              "slums (Mehta et al., BMJ Open, 2017).")),
        hbox("Biofortified millets fit naturally into PDS diversification under NFSA "
             "s12(2)(f) and into PM POSHAN menus in millet-eating states.", "indigo"),
    ], compact=True),

    # ===================== SECTION 10 =====================
    D("10", "Section Ten", "South Asia compared"),

    C("Five countries", "Child undernutrition across South Asia, latest national surveys", [
        {"t": "chart", "canvas": "nutSouthAsiaChart",
         "title": "Children under five, latest national survey (%)",
         "source": "India NFHS-6 2023-24 (provisional fact sheet, IIPS 2026); Pakistan NNS 2018; Bangladesh DHS 2022; Nepal DHS 2022 (DHS STATcompiler); Sri Lanka DHS 2016 (DCS, Ch. 11)",
         "type": "bar",
         "data": {"labels": ["Pakistan 2018", "India 2023-24", "Nepal 2022",
                             "Bangladesh 2022", "Sri Lanka 2016"],
                  "datasets": [
                      {"label": "Stunted", "data": [40.2, 29.3, 24.8, 23.6, 17.3],
                       "backgroundColor": "#EF4444"},
                      {"label": "Wasted", "data": [17.7, 19.0, 7.7, 11.0, 15.1],
                       "backgroundColor": "#F59E0B"},
                      {"label": "Underweight", "data": [28.9, 31.8, 18.7, 22.3, 20.5],
                       "backgroundColor": "#0EA5E9"}]},
         "options": {"__js__": "{ plugins:{legend:{position:'bottom'}}, scales:{ y:{ min:0, max:45, title:{display:true,text:'%'} } } }"}},
        body("Survey years differ by up to eight years, so read this as a snapshot of "
             "different years. The striking contrast is between stunting and wasting: Sri Lanka "
             "has the lowest stunting but wasting close to India's, and India's wasting is "
             "the highest of the five. India has the highest underweight share too.", sm=True),
    ], compact=True),

    C("Bangladesh and Nepal", "Bangladesh and Nepal nearly halved stunting in about fifteen years", [
        {"t": "chart", "canvas": "nutBdNpChart",
         "title": "Stunted children under five, DHS rounds (%)",
         "source": "DHS Program STATcompiler: Bangladesh DHS 2007-2022, Nepal DHS 2006-2022, India NFHS-3 to NFHS-5; India NFHS-6 (2023-24) provisional fact sheet, IIPS 2026",
         "type": "line",
         "data": {"labels": ["2006-07", "2011", "2014-16", "2017-21", "2022-24"],
                  "datasets": [
                      {"label": "Bangladesh", "data": [43.2, 41.3, 36.1, 30.8, 23.6],
                       "borderColor": "#10B981", "fill": False, "tension": 0.2},
                      {"label": "Nepal", "data": [49.3, 40.5, 35.8, None, 24.8],
                       "borderColor": "#6366F1", "fill": False, "tension": 0.2,
                       "spanGaps": True},
                      {"label": "India", "data": [48.0, None, 38.4, 35.5, 29.3],
                       "borderColor": "#EF4444", "fill": False, "tension": 0.2,
                       "spanGaps": True}]},
         "options": {"__js__": "{ plugins:{legend:{position:'bottom'}}, scales:{ y:{ min:0, max:55 } } }"}},
        body("Bangladesh fell from 43.2% (2007) to 23.6% (2022) and Nepal from 49.3% (2006) "
             "to 24.8% (2022); India fell from 48.0% (2005-06) to 29.3% (2023-24). Nepal's "
             "2016 value (35.8%) is plotted in the 2014-16 column, India's 2015-16 value "
             "there too, and India's 2023-24 value in the last column. The Alive &amp; Thrive evaluators describe Bangladesh's decline as "
             "a rapid positive secular trend (Menon et al., J Nutr, 2016).", sm=True),
    ], compact=True),

    C("Pakistan", "Pakistan: high stunting and a rising second burden", [
        body("Pakistan's National Nutrition Survey 2018 was the fifth since 1965 and the "
             "first to give district-representative estimates (NNS 2018 Key Findings "
             "Report, published by UNICEF Pakistan)."),
        stats([card("40.2%", "children under five stunted", "red", "NNS 2018 KFR"),
               card("17.7%", "wasted", "red", "NNS 2018 KFR"),
               card("9.5%", "overweight, up from 5% in 2011", "amber", "NNS 2018 KFR"),
               card("53.7%", "children under five anaemic", "red", "NNS 2018 KFR")], cols=4),
        tw(pp("cyan", "Within-country range",
              "Stunting ranges from 32.6% in Islamabad Capital Territory to 48.3% in the "
              "newly merged districts of Khyber Pakhtunkhwa. It improved from 48% in 1965 "
              "to 36.3% in 1994, then worsened to 43.7% by 2011 (NNS 2018 KFR)."),
           pp("amber", "Women",
              "14.4% of women of reproductive age are undernourished and 37.8% are "
              "overweight or obese, up from 28% in 2011; 41.7% are anaemic (NNS 2018 KFR). "
              "Pakistan shows the double burden as clearly as any country in the region.")),
    ], compact=True),

    C("Sri Lanka", "Sri Lanka: good services, stubborn wasting", [
        body("Sri Lanka's 2016 Demographic and Health Survey, by the Department of Census "
             "and Statistics, recorded 17.3% stunting, 15.1% wasting and 20.5% underweight "
             "among children under five (SLDHS 2016, Ch. 11, Table 11.1). Ninety percent "
             "of children were breastfed within an hour of birth and 82% of infants under "
             "six months were exclusively breastfed (SLDHS 2016, Ch. 11)."),
        tw(pp("red", "Inequality inside a good average",
              "Stunting was 32% in the estate (plantation) sector against 15% in urban and "
              "rural sectors, and 32% in Nuwara Eliya district against 11% in Polonnaruwa "
              "(SLDHS 2016, Ch. 11). The plantation workforce carries a burden that the "
              "national average hides."),
           pp("amber", "The wasting puzzle",
              "Wasting at 15.1% sits close to India's despite strong breastfeeding and "
              "health services. Wasting is highest among infants aged 0-5 months (19%) "
              "(SLDHS 2016, Ch. 11), which suggests that birthweight and maternal "
              "nutrition matter as much as complementary feeding.")),
    ], compact=True),

    C("Lessons", "Anaemia across South Asia, and what to take from the region", [
        table(["Country, survey", "Children anaemic", "Women anaemic"],
              [["India, NFHS-5 2019-21", "67.1% (6-59 months)", "57.0% (15-49)"],
               ["Pakistan, NNS 2018", "53.7% (under 5)", "41.7% (reproductive age)"],
               ["Bangladesh, DHS 2011", "51.3%", "42.4%"],
               ["Nepal, DHS 2022", "43.3%", "34.0%"]]),
        body("Sources: NFHS-5 India Report, 2022 (NFHS-6 anaemia not released as of "
             "October 2026); NNS 2018 KFR; DHS Program STATcompiler. "
             "Methods and years differ, and STATcompiler shows no Bangladesh DHS anaemia "
             "estimate after 2011, so compare cautiously.", sm=True),
        bullets(["<strong>Speed is possible.</strong> Bangladesh and Nepal show stunting can "
                 "fall by a point a year or more over fifteen years.",
                 "<strong>Averages hide groups.</strong> Sri Lanka's estates and "
                 "Pakistan's merged districts are the region's Meghalayas and Bihars.",
                 "<strong>Wasting is stubborn.</strong> It moved least everywhere and "
                 "starts in the first months of life.",
                 "<strong>The second burden is arriving.</strong> Pakistan's women and "
                 "India's urban rich already show it."], sm=True),
    ], compact=True),

    # ===================== SECTION 11 =====================
    D("11", "Section Eleven", "Practical application: a practitioner's toolkit"),

    C("Design checklist", "A design checklist for a nutrition programme", [
        tw([panel("cyan", "Diagnose", [bullets([
                "Which forms: stunting, wasting, anaemia, overweight, or several?",
                "Which ages: pregnancy, 0-6 months, 6-23 months, adolescents?",
                "Which causes dominate locally: diets, infection, care, maternal status?",
                "Which groups: caste, tribe, estate, migrant, urban poor?",
                "What do the latest NFHS round and the CNNS say for the district or state?"], sm=True)])],
           [panel("green", "Design", [bullets([
                "Link to entitlements first: ration card, ICDS, PMMVY, PM POSHAN",
                "Reach children before 6 months and mothers before birth",
                "Pair any food or cash with counselling",
                "Plan for SAM referral and NRC capacity",
                "Write the cascade: eligible, enrolled, served, consumed, effective"],
                sm=True)])]),
        tw([panel("amber", "Measure", [bullets([
                "Use the WHO 2006 standard; train and standardise measurers",
                "Report mean z-scores and prevalence with confidence intervals",
                "State blood sample type and haemoglobin cut-off"], sm=True)])],
           [panel("indigo", "Protect", [bullets([
                "Consent and ethics review for every survey",
                "Design for DPDP duties applying from 13 May 2027",
                "Refer every SAM child found; never measure without acting"],
                sm=True)])]),
    ], compact=True),

    C("Indicators", "Choosing indicators that match the programme", [
        table(["Programme aims to change", "Primary indicator", "Data source", "Pitfall"],
              [["Feeding practices, 6-23 months", "Minimum acceptable diet; minimum "
                "dietary diversity", "Programme survey using WHO-UNICEF 2021 questions",
                "Definition changed in 2021"],
               ["Acute malnutrition caseload", "SAM and MAM by MUAC and WHZ", "Screening "
                "registers; Poshan Tracker", "Different children by each method"],
               ["Linear growth", "Mean height-for-age z-score; stunting", "Baseline and "
                "endline anthropometry", "Changes slowly; needs large samples"],
               ["Anaemia", "Haemoglobin; anaemia prevalence", "Venous or capillary test",
                "Method and cut-off drive the level"],
               ["Entitlement access", "Households receiving full PDS, ICDS, PMMVY "
                "entitlement", "Household survey; ration card audit", "Self-report bias"],
               ["Maternal diet", "Women eating 5 or more food groups a day, as in Nguyen et "
                "al., 2017", "24-hour recall", "Seasonality"]]),
        body("Choose an indicator the programme can plausibly move within the funding "
             "period. A two-year feeding counselling project should be judged on feeding "
             "practices first and on stunting only as a long-term aim, as the Alive &amp; "
             "Thrive results show.", sm=True),
    ], compact=True),

    C("Decision table", "Matching the problem to the response", [
        table(["If the diagnosis is", "Prioritise", "Evidence"],
              [["High wasting, especially under 6 months", "Maternal nutrition, "
                "breastfeeding support, SAM screening and referral",
                "Victora et al., 2021; WHO 2023 guideline"],
               ["Low minimum acceptable diet", "Complementary feeding counselling, "
                "food access, eggs or pulses in rations", "Alive &amp; Thrive, J Nutr, 2016"],
               ["Poor households missing entitlements", "Ration cards, NFSA grievance "
                "routes, PMMVY enrolment", "NFSA 2013 ss 3-15"],
               ["High open defecation, dense settlement", "Community-wide sanitation "
                "with nutrition", "Spears, 2013 (observational); WASH trials"],
               ["High anaemia, uncertain cause", "Venous testing, iron status, "
                "haemoglobinopathy screening, deworming", "CNNS 2016-18; Kurpad and "
                "Sachdev, 2022"],
               ["Rising adult overweight", "Diet quality, Eat Right, waist and BP "
                "screening", "Popkin et al., 2020; NFHS-5"]]),
        hbox("Most districts have more than one row. Rank them by burden and by what the "
             "programme can reach, and say which rows you are not addressing.", "indigo"),
    ], compact=True),

    C("Worked example", "Illustrative: sizing a screening programme in one block", [
        body("<strong>Illustrative case.</strong> A block has 12,000 children aged 6-59 "
             "months. A recent survey estimates 18% wasting by weight-for-height and 4% "
             "severe acute malnutrition. All numbers on this slide are Illustrative."),
        table(["Step", "Calculation (Illustrative)", "Result"],
              [["Children with SAM at any one time", "12,000 x 4%", "480"],
               ["With MAM", "12,000 x (18% - 4%)", "1,680"],
               ["SAM with medical complications needing an NRC (assume 15%)",
                "480 x 15%", "72"],
               ["NRC beds if 72 admissions a year stay 14 days each", "72 x 14 / 365 beds "
                "occupied on an average day", "about 3"],
               ["Monthly MUAC screenings by Anganwadi Workers", "12,000 x 12", "144,000"]]),
        body("The arithmetic reveals the design problem. Prevalence is a snapshot, and "
             "new cases arise through the year, so the annual caseload is several times "
             "the point prevalence. Screening is the largest workload, and it falls on "
             "Anganwadi Workers who also run the centre. Budget tapes, training and "
             "supervision before promising coverage.", sm=True),
    ], compact=True),

    C("Targets", "Illustrative: setting a target you can defend", [
        body("<strong>Illustrative case.</strong> A district with 40% stunting is asked "
             "to reach 30% in three years. The question is whether that is realistic."),
        tw(pp("amber", "What history suggests",
              "India's stunting fell from 48.0% to 38.4% over about ten years between "
              "NFHS-3 and NFHS-4, under a point a year, and from 38.4% to 35.5% by NFHS-5 "
              "(DHS STATcompiler), then about 1.5 points a year to 29.3% in NFHS-6, 2023-24 "
              "(NFHS-6 India Fact Sheet, 2026). Bangladesh managed about 1.3 points a year "
              "between 2007 "
              "and 2022. A drop of 10 points in three years would be unprecedented at "
              "national scale in the region."),
           pp("green", "A defensible target (Illustrative)",
              "Commit to process and practice targets that the evidence links to growth: "
              "minimum acceptable diet from 15% to 25%, exclusive breastfeeding from 56% to "
              "80%, full PMMVY and ration card enrolment, SAM referral within a week. Set "
              "stunting at 1-1.5 points a year and measure it with a properly sized "
              "survey.")),
        hbox("POSHAN Abhiyaan's 'Mission 25 by 2022' asked for stunting to fall from 38.4% "
             "to 25%; NFHS-5 found 35.5% and NFHS-6 29.3% (PIB, 1 December 2017; NFHS-5; "
             "NFHS-6). Ambition is "
             "useful; a target that cannot be met discredits the monitoring that tracks "
             "it.", "indigo"),
    ], compact=True),

    # ===================== SECTION 12 =====================
    D("12", "Section Twelve", "Bringing it together"),

    C("Summary", "Ten ideas to take away", [
        tw([panel("cyan", "Understanding", [bullets([
                "Malnutrition has three faces: undernutrition, hidden hunger, overweight",
                "Stunting records history; wasting records crisis",
                "Causes run from diet and disease to food, care, services and power",
                "Growth faltering starts in the womb and peaks by age two",
                "India's levels are debated; its gradients are not"], sm=True)])],
           [panel("green", "Acting", [bullets([
                "NFSA 2013 makes food and meals legal entitlements with grievance routes",
                "Poshan 2.0, PM POSHAN, PMMVY and AMB are the delivery platforms",
                "Direct interventions save lives; most stunting needs wider change",
                "Counselling changes practices fast; height moves slowly",
                "Measure carefully, report the method, and act on what you find"],
                sm=True)])]),
        body("Behind each idea is a source you can open: NFHS-6 and NFHS-5, the CNNS, the NFSA, the "
             "FSSAI regulations, PIB releases and the Lancet series. Check the latest round "
             "and the latest scheme approval before you quote a number, since NFHS, scheme "
             "periods and the DPDP timetable all move.", sm=True),
    ], compact=True),

    C("Where next", "Where next: related 101 decks", [
        tw([panel("cyan", "Health and early childhood", [body(
                "<a href=\"/101-courses/maternal-health.html\">Maternal Health 101</a> for "
                "antenatal care and the continuum of care. "
                "<a href=\"/101-courses/child-development.html\">Child Development 101</a> "
                "for early stimulation and the first years. "
                "<a href=\"/101-courses/pub-health-basics.html\">Public Health 101</a> for "
                "epidemiology and health systems. "
                "<a href=\"/101-courses/bcc-comms.html\">Behaviour Change Communication "
                "101</a> for counselling and campaigns. "
                "<a href=\"/101-courses/child-rights.html\">Child Rights 101</a> for the "
                "rights framing of nutrition.", sm=True)])],
           [panel("green", "Methods and policy", [body(
                "<a href=\"/101-courses/survey-design.html\">Survey Design 101</a> and "
                "<a href=\"/101-courses/stats-without-code.html\">Statistics Without Code "
                "101</a> for weights and sampling. "
                "<a href=\"/101-courses/impact-eval.html\">Impact Evaluation 101</a> and "
                "<a href=\"/101-courses/causal-inference.html\">Causal Inference 101</a> "
                "for reading trials. "
                "<a href=\"/101-courses/programme-design.html\">Programme Design 101</a> for "
                "the delivery cascade. "
                "<a href=\"/101-courses/gender-dev.html\">Gender &amp; Development 101</a> "
                "for household bargaining. "
                "<a href=\"/101-courses/governance-accountability.html\">Governance &amp; "
                "Accountability 101</a> for social audits. "
                "<a href=\"/101-courses/data-protection-dpdp.html\">Data Protection &amp; "
                "the DPDP Act 101</a> for children's data.", sm=True)])]),
        hbox("Start with the deck that matches the gap you found in your own programme's "
             "cascade.", "indigo"),
    ], compact=True),

    # ===================== END =====================
    {"type": "end",
     "eyebrow": "Nutrition 101",
     "headline": "Measure carefully, reach children early, and use the law",
     "byline": "ImpactMojo 101 Series &middot; Free foundational learning for development "
               "practitioners in South Asia",
     "ctas": [{"label": "Maternal Health 101", "href": "/101-courses/maternal-health.html"},
              {"label": "Public Health 101", "href": "/101-courses/pub-health-basics.html"},
              {"label": "All 101 courses", "href": "/101-courses/"}],
     "meta": ["100 slides", "12 sections", "CC BY-NC-ND"]},
]

DECK = {
    "slug": "nutrition",
    "title": "Nutrition 101",
    "description": ("Nutrition 101: a free foundational course for development practitioners "
                    "in South Asia. Stunting, wasting, anaemia and overweight; the WHO Child "
                    "Growth Standards and z-scores; the UNICEF frameworks and the first 1,000 "
                    "days; India's numbers from NFHS-6, NFHS-5 and the CNNS; the Indian enigma debates "
                    "on birth order, sanitation, growth standards and anaemia cut-offs; the "
                    "National Food Security Act 2013 and the PDS; Poshan 2.0, PM POSHAN, "
                    "Anemia Mukt Bharat and rice fortification; the intervention evidence; "
                    "South Asian comparisons; and a practitioner toolkit. ImpactMojo, "
                    "CC BY-NC-ND."),
    "slides": SLIDES_A + SLIDES_B + SLIDES_C,
}
