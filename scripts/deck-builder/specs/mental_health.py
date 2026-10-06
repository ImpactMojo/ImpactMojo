# -*- coding: utf-8 -*-
"""
Mental Health 101 - ImpactMojo 101 Series (native deck spec)
Mental health for development practitioners in South Asia: definitions and
ICD-11, the burden (WHO, GBD India, NMHS 2015-16), suicide and the NCRB data,
social determinants and stigma, the Mental Healthcare Act 2017 and the BNS,
India's programmes (NMHP, DMHP, Tele-MANAS, NSPS), the region's laws, task
sharing and its trials, children, work and emergencies, measurement and
research ethics, and a practitioner's toolkit.
Build: python3 scripts/deck-builder/build.py mental_health

Every figure, section and case was checked in a source that was opened and
read (October 2026); the list is in the build report. Suicide content follows
WHO's 2023 media guidance: no method detail, help-seeking information given.
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


WHO_MD = "WHO fact sheet, Mental disorders (updated 11 September 2026)"
WHO_MH = "WHO fact sheet, Mental health: strengthening our response (updated 11 September 2026)"
WMHR = "WHO, World mental health report, 2022 (news release, 17 June 2022)"
GBD = ("India State-Level Disease Burden Initiative Mental Disorders Collaborators, "
       "Lancet Psychiatry 2020;7(2):148-61")
NMHS = "NMHS 2015-16 (NIMHANS), as reported in Murthy, Indian J Psychiatry 2017;59(1):21-26"
ADSI = "NCRB, Accidental Deaths and Suicides in India 2024, Chapter 2"
MHCA = "Mental Healthcare Act, 2017 (Act 10 of 2017)"
PIB25 = "PIB backgrounder, Advancing Mental Healthcare in India, 7 February 2025"
PIB26 = "PIB, Update on Tele-MANAS, 6 February 2026"
HELP = ("If this material raises anything difficult for you, Tele-MANAS (14416 or "
        "1-800-891-4416) is free and runs round the clock in India.")

# ===================== SECTION 01: WHAT MENTAL HEALTH IS =====================
S01 = [
    D("01", "Section One", "What mental health is, and what a disorder is"),

    C("Definition", "WHO's definition starts with well-being", [
        body("The World Health Organization does not define mental health as the absence of "
             "illness. Its fact sheet, updated in September 2026, describes a positive state that "
             "everyone has to some degree, including people who live with a diagnosed condition. "
             "The definition matters for programmes because it widens the target: a livelihood or "
             "education project can protect mental health even if it never treats anyone."),
        quote("Mental health is a state of mental well-being that enables people to cope with the "
              "stresses of life, realize their abilities, learn and work well, and contribute to "
              "their community.", WHO_MH),
        tw(pp("cyan", "Intrinsic value", "WHO says mental health has value in itself and calls it "
              "a basic human right. Feeling settled, safe and able to think clearly is part of a "
              "good life whatever it does for income."),
           pp("green", "Instrumental value", "Mental health also makes other things possible: "
              "learning in school, holding a job, caring for children, taking part in a gram sabha. "
              "Its loss shows up in all of these.")),
        body("WHO also describes mental health as a continuum that each person experiences "
             "differently, shaped at any moment by individual, family, community and structural "
             "factors.", sm=True),
    ]),

    C("Terms", "Mental health conditions, disorders and psychosocial disability", [
        body("Practitioners meet three overlapping terms, and the difference decides who a "
             "programme is designed for. WHO's mental disorders fact sheet (September 2026) sets "
             "them out. The narrowest is a disorder that meets diagnostic criteria. The broadest "
             "is a mental health condition, which includes distress and disability that may never "
             "reach a diagnosis."),
        term("Mental disorder",
             "A clinically significant disturbance in an individual's cognition, emotional "
             "regulation, or behaviour, usually associated with distress or impairment in "
             "important areas of functioning (WHO, Mental disorders fact sheet)."),
        tw(pp("indigo", "Mental health condition", "WHO's broader term covers mental disorders, "
              "psychosocial disabilities and other mental states with significant distress, "
              "impairment in functioning, or risk of self-harm."),
           pp("amber", "Psychosocial disability", "The barriers a person with a long-term mental "
              "health condition meets in society: exclusion from work, school, housing or a vote. "
              "The disability lies in the interaction, so a programme can reduce it.")),
        hbox("Use the term that fits the activity. A screening survey estimates disorders. A "
             "community programme usually works with distress and functioning, and should say so "
             "in its indicators.", "cyan"),
    ]),

    C("Classification", "ICD-11 gives clinicians and researchers one shared language", [
        body("The International Classification of Diseases is WHO's system for coding illness and "
             "death. Its eleventh revision was approved by the World Health Assembly in 2019 and "
             "became effective for health reporting in January 2022. WHO's 2022 release note says "
             "it holds around 17,000 unique codes and is fully digital. Mental conditions sit in "
             "the grouping for mental, behavioural and neurodevelopmental disorders."),
        tw(pp("cyan", "The diagnostic manual", "On 8 March 2024 WHO published the Clinical "
              "descriptions and diagnostic requirements for ICD-11 mental, behavioural and "
              "neurodevelopmental disorders (CDDR), an 852-page manual written for psychiatrists, "
              "primary care doctors, nurses, social workers and students."),
           pp("green", "Why it matters in India", "Section 3(1) of the Mental Healthcare Act, "
              "2017 says mental illness shall be determined by nationally or internationally "
              "accepted medical standards, including the latest edition of WHO's International "
              "Classification of Disease, as notified by the Central Government.")),
        hbox("For programme staff the practical point is modest. You will not diagnose. You will "
             "read referral notes, research papers and records coded in ICD terms, and you need to "
             "know where those words come from.", "indigo"),
    ]),

    C("Indian law", "How the Mental Healthcare Act defines mental illness", [
        body("The Mental Healthcare Act, 2017 (Act 10 of 2017) received assent on 7 April 2017 "
             "and came into force on 29 May 2018. Its definition in section 2(1)(s) sets the "
             "threshold for every right and duty that follows, so it is worth reading in full."),
        quote("\"Mental illness\" means a substantial disorder of thinking, mood, perception, "
              "orientation or memory that grossly impairs judgment, behaviour, capacity to recognise "
              "reality or ability to meet the ordinary demands of life, mental conditions associated "
              "with the abuse of alcohol and drugs ...", MHCA + ", section 2(1)(s)"),
        tw(pp("amber", "What it excludes", "The same clause excludes intellectual disability "
              "(the Act uses the older term), which is dealt with under the Rights of Persons with "
              "Disabilities Act, 2016."),
           pp("red", "What cannot be grounds", "Section 3(3) bars determining mental illness on "
              "the basis of political, economic or social status, caste, religion, or "
              "non-conformity with moral, social, cultural or political values. Section 3(5) says "
              "a diagnosis alone does not mean a person is of unsound mind.")),
    ]),

    C("A working map", "The conditions a development programme will meet most", [
        body("WHO's September 2026 fact sheet gives 2023 global estimates for the main disorders. "
             "The table pairs each with what WHO says helps. Every row has an effective treatment, "
             "which is why the gap between need and care is the central problem in this field."),
        table(["Condition (WHO, 2023)", "People affected worldwide", "What WHO says helps"], [
            ["Anxiety disorders", "470 million, incl. 146 million children and adolescents",
             "Psychological treatment; medicines depending on age and severity"],
            ["Depression", "322 million, incl. 43 million children and adolescents",
             "Psychological treatment; medicines depending on age and severity"],
            ["Bipolar disorder", "36 million",
             "Psychoeducation, social functioning support, medicines"],
            ["Schizophrenia", "About 27 million (1 in 300)",
             "Medicines, psychoeducation, family interventions, rehabilitation"],
            ["Eating disorders", "18 million, incl. 4.7 million children and adolescents",
             "Family-based and psychological care"],
        ]),
        body("WHO notes that people with schizophrenia die on average nine years earlier than the "
             "general population. Source: " + WHO_MD
             + ".", sm=True),
    ], compact=True),

    C("Rights", "Disability rights changed the starting point", [
        body("The Mental Healthcare Act opens by citing the UN Convention on the Rights of Persons "
             "with Disabilities, which India signed on 30 March 2007 and ratified on 1 October 2007, and says the "
             "Act aligns Indian law with it. The older Mental Health Act, 1987 was mainly about "
             "admitting and detaining people. The 2017 Act begins with capacity and choice."),
        tw(pp("cyan", "Capacity is presumed", "Section 4(1) deems every person, including a person "
              "with mental illness, to have capacity to make treatment decisions if they can "
              "understand the relevant information, appreciate its consequences, or communicate a "
              "decision. Section 4(3) adds that a decision others see as wrong does not by itself "
              "show incapacity."),
           pp("green", "Disability law alongside", "The PIB backgrounder of 7 February 2025 notes "
              "that the Rights of Persons with Disabilities Act, 2016 widened the definition of "
              "disability to include mental illness, bringing protections against "
              "discrimination in education and employment.")),
        hbox("For a programme, the rights frame means the person is the decision-maker about "
             "their own care. Family members and staff support that decision; they do not replace "
             "it unless the law's narrow conditions are met.", "indigo"),
    ]),

    C("Language", "Words that reduce stigma, and words that add to it", [
        body("Language in reports, posters and training sessions shapes whether people seek help. "
             "WHO's 2023 resource for media professionals explains that the phrase \"committed "
             "suicide\" implies criminality and adds to the stigma felt by bereaved families. It "
             "recommends \"died by suicide\" or \"took their own life\". The same logic applies to "
             "descriptions of illness."),
        table(["Avoid", "Prefer", "Reason"], [
            ["\"committed suicide\"", "\"died by suicide\"", "Removes the suggestion of a crime"],
            ["\"successful\" or \"failed\" attempt", "\"suicide attempt\"",
             "WHO: these imply death is a desirable outcome"],
            ["\"a schizophrenic\", \"mental patient\"", "\"a person living with schizophrenia\"",
             "The person comes before the diagnosis"],
            ["\"pagal\", \"mad\", \"crazy\"", "Plain description of what the person is going through",
             "Slurs keep people from asking for help"],
            ["\"suffering from\"", "\"living with\" or \"has\"", "Avoids defining a life by illness"],
        ]),
        hbox("Ask people with lived experience which words they use for themselves, and use those "
             "in programme material.", "green"),
    ], compact=True),
]

# ===================== SECTION 02: THE BURDEN =====================
S02 = [
    D("02", "Section Two", "How large the burden is"),

    C("Global picture", "More than a billion people live with a mental health condition", [
        stats([card("1.2 billion", "people living with a mental disorder in 2023, nearly 1 in 7",
                    "cyan", WHO_MD),
               card("1 in 6", "years lived with disability caused by mental disorders", "indigo",
                    WMHR),
               card("71%", "of people with psychosis worldwide who receive no mental health "
                    "service", "red", WMHR)], cols=3),
        body("WHO's World mental health report, published in June 2022, was the largest review of "
             "the subject since 2001. It found that mental disorders are the leading cause of "
             "disability and that people with severe conditions die 10 to 20 years earlier than "
             "the general population, mostly from preventable physical disease. It also found the "
             "money going to the wrong place: 2 out of every 3 dollars of government spending on "
             "mental health went to stand-alone psychiatric hospitals rather than community "
             "services."),
        hbox("The 2022 report also counted 20 countries that still criminalise attempted suicide. "
             "Section 07 shows where South Asia's neighbours stand.", "amber"),
    ]),

    C("Care gap", "Effective treatment exists, and most people never receive it", [
        body("The care gap is the share of people with a condition who receive no care, or care "
             "too poor to help. WHO's 2022 report put numbers on it for two conditions, and the "
             "gap is widest where incomes are lowest. Coverage figures alone hide quality: a "
             "person may see a doctor once, receive a prescription and never return."),
        tw(pp("red", "Psychosis", "About 70% of people with psychosis are reported to be treated "
              "in high-income countries. In low-income countries the figure is 12%."),
           pp("amber", "Depression", "Even in high-income countries only one third of people with "
              "depression receive formal care. Minimally adequate treatment ranges from 23% in "
              "high-income countries to 3% in low- and lower-middle-income countries.")),
        body("WHO's 2026 fact sheet repeats the pattern: only 40% of people with "
             "psychosis and about one third of people with depression receive formal mental health "
             "care. Stigma, too few trained staff and too little public money explain much of it.",
             sm=True),
        hbox("Source: " + WMHR + "; " + WHO_MD + ".", "cyan"),
    ]),

    C("India: GBD", "One in seven Indians lived with a mental disorder in 2017", [
        stats([card("197.3 million", "people in India with a mental disorder in 2017 (95% UI "
                    "178.4-216.4 million)", "cyan", GBD),
               card("45.7 million", "with depressive disorders", "indigo", GBD),
               card("44.9 million", "with anxiety disorders", "amber", GBD),
               card("2.5% to 4.7%", "share of India's total DALYs from mental disorders, 1990 to "
                    "2017", "red", GBD)], cols=4),
        body("The India State-Level Disease Burden Initiative applied the Global Burden of Disease "
             "method to every state. Almost all of this burden is years lived with disability "
             "rather than early death, because GBD counts suicide deaths under injuries. The study "
             "also found that disorders that begin mainly in childhood were more common in the less "
             "developed northern states, and those that begin mainly in adulthood in the more "
             "developed southern states. It reported a modest state-level correlation between depression "
             "prevalence and the suicide death rate, for women and for men."),
        hbox("GBD estimates are models built from all available data. Use them for scale and "
             "comparison, and use surveys for programme baselines.", "indigo"),
    ]),

    C("India: what drives the burden", "Depression and anxiety account for over half of India's mental health DALYs", [
        {"t": "chart", "canvas": "gbdIndiaDalys",
         "title": "Share of mental disorder DALYs in India by disorder, 2017 (%)",
         "source": GBD,
         "type": "bar",
         "data": {"labels": ["Depressive", "Anxiety", "Idiopathic intellectual disability",
                             "Schizophrenia", "Bipolar", "Conduct", "Autism spectrum", "Eating",
                             "ADHD", "Other"],
                  "datasets": [{"label": "% of mental disorder DALYs",
                                "data": [33.8, 19.0, 10.8, 9.8, 6.9, 5.9, 3.2, 2.2, 0.3, 8.0],
                                "backgroundColor": "#0EA5E9"}]},
         "options": {"__js__": "{ indexAxis:'y', plugins:{legend:{display:false}}, "
                               "scales:{ x:{min:0,max:40} } }"}},
        body("Depressive disorders made up 33.8% of the mental disorder burden and anxiety "
             "disorders 19.0%. Together they explain why so much global mental health work in "
             "South Asia focuses on common mental disorders in primary care and in the "
             "community. The severe disorders, schizophrenia and bipolar disorder, add another "
             "16.7%, and their families carry long periods of care.", sm=True),
    ], compact=True),

    C("Neurology and substances", "Mental, neurological and substance use disorders are planned together", [
        body("WHO's Mental Health Gap Action Programme (mhGAP) groups mental, neurological and "
             "substance use disorders because the same primary care workers meet all three and "
             "the same scarce specialists support them. WHO's mhGAP page states that these "
             "disorders account for 14% of the global burden of disease, and that 75% of people "
             "affected in many low-income countries do not have access to the treatment they "
             "need."),
        tw(pp("cyan", "What the guide covers", "WHO's mhGAP page names depression, schizophrenia, "
              "epilepsy and suicide prevention among its concerns. Version 2.0 of the guide has "
              "revised modules for psychoses, child and adolescent mental and behavioural "
              "disorders and disorders due to substance use, and a Marathi edition exists."),
           pp("amber", "Why alcohol and drugs sit here", "NMHS 2015-16 found treatment gaps of "
              "86.3% for alcohol use disorder and 91.8% for tobacco use. The MHCA's own definition "
              "of mental illness includes conditions associated with the abuse of alcohol and "
              "drugs.")),
        hbox("The mhGAP Intervention Guide, version 2.0 (WHO, 2016), turns this into algorithms "
             "for doctors, nurses and other health workers in non-specialist settings, such as a "
             "primary health centre.", "green"),
        body("Source: WHO, Mental Health Gap Action Programme page and mhGAP Intervention Guide "
             "2.0 (accessed October 2026); " + NMHS + ".", sm=True),
    ], compact=True),

    C("India: NMHS", "The National Mental Health Survey 2015-16", [
        body("The Ministry of Health commissioned NIMHANS, Bengaluru to run India's first "
             "national survey of mental disorders. It covered 12 states in six regions and "
             "drew a sample of 34,802 adults from 43 districts, about 3,000 per state, using "
             "structured diagnostic tools. "
             "It remains the only national measurement of prevalence and treatment gap."),
        stats([card("10.6%", "adults with a current mental disorder", "cyan", NMHS),
               card("13.7%", "lifetime prevalence of any mental morbidity", "indigo", NMHS),
               card("7.3%", "adolescents aged 13-17 with a mental disorder", "amber", NMHS),
               card("0.9%", "at high risk of suicide in the past month (0.7% moderate)", "red",
                    NMHS)], cols=4),
        tw(pp("cyan", "Who was more affected", "Prevalence was higher in urban metros and in "
              "lower income quintiles. Current depression was 3.0% among women and 2.4% among "
              "men. Lifetime prevalence ranged from 8.1% in Assam to 19.9% in Manipur."),
           pp("amber", "How to read it", "These are survey estimates from 12 states using "
              "structured interviews. The GBD figure of 197 million is a modelled estimate for "
              "all India, so the two sources answer different questions.")),
    ], compact=True),

    C("India: treatment gap", "Between 70% and 92% of people received no treatment", [
        {"t": "chart", "canvas": "nmhsGap",
         "title": "Treatment gap by condition, NMHS 2015-16 (%)",
         "source": NMHS,
         "type": "bar",
         "data": {"labels": ["Tobacco use", "Alcohol use disorder", "Common mental disorders",
                             "Psychosis", "Severe mental disorders", "Bipolar affective disorder"],
                  "datasets": [{"label": "Treatment gap (%)",
                                "data": [91.8, 86.3, 85.0, 75.5, 73.6, 70.4],
                                "backgroundColor": "#EF4444"}]},
         "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{min:0,max:100} } }"}},
        body("The treatment gap is the share of people with a condition who had received no "
             "treatment. For common mental disorders such as depression and anxiety it was 85%. "
             "Murthy's review notes that in most cases a government facility was the main "
             "source of care for those who did get treatment, which means public services are "
             "where scale-up has to happen. The PIB backgrounder of February 2025 cites an "
             "Indian Journal of Psychiatry estimate of 0.75 psychiatrists per 100,000 people.",
             sm=True),
    ], compact=True),

    C("Status, October 2026", "The second national survey and what to use until it reports", [
        body("Public reporting from 2025 and 2026 describes a second National Mental Health "
             "Survey run by NIMHANS for the Ministry of Health, designed to cover all states and "
             "union territories and both adolescents and adults. As of October 2026 we could not "
             "find a published report or an official prevalence figure from it, so this deck uses "
             "the 2015-16 survey for India's national numbers."),
        tw(pp("cyan", "Until NMHS-2 publishes", "Use NMHS 2015-16 for prevalence and treatment gap, "
              "stating the year and the 12-state coverage. Use GBD for state comparisons and "
              "trends. Use NCRB for recorded suicides, with the caveats in Section 03."),
           pp("amber", "When it does publish", "Check the sampling frame, the age bands, the "
              "instruments and whether results are given by district or social group. Do not "
              "compare a new figure with 10.6% until you know the two used the same tools.")),
        hbox("Time-sensitive: confirm the status of NMHS-2 with NIMHANS or the Ministry before "
             "quoting it in a proposal.", "amber"),
    ]),
]

# ===================== SECTION 03: SUICIDE =====================
S03 = [
    D("03", "Section Three", "Suicide: what the numbers show and what they miss"),

    C("Global", "More than 720,000 people die by suicide each year", [
        body("This section discusses suicide as a public health problem. It follows WHO's media "
             "guidance: no methods, no locations, and information on where to get help. " + HELP),
        stats([card("727,000", "deaths by suicide worldwide in 2021", "indigo",
                    "WHO fact sheet, Suicide (updated 28 August 2026)"),
               card("3rd", "leading cause of death among people aged 15-29, 2021", "red",
                    "WHO fact sheet, Suicide (updated 28 August 2026)"),
               card("73%", "of global suicides in low- and middle-income countries, 2021", "amber",
                    "WHO fact sheet, Suicide (updated 28 August 2026)")], cols=3),
        body("WHO stresses that many suicides happen impulsively in moments of crisis, such as "
             "financial problems, relationship disputes or chronic pain, as well as among people "
             "with depression or alcohol use disorders. A prior suicide attempt is a strong risk "
             "factor. The suicide rate is the only mental health indicator in the Sustainable "
             "Development Goals.", sm=True),
    ]),

    C("India: NCRB", "India recorded 1,70,746 suicides in 2024", [
        body("The National Crime Records Bureau publishes <em>Accidental Deaths and Suicides in "
             "India</em> (ADSI) from police records sent by states. The 2024 edition is the latest "
             "we could find as of October 2026. It reported 1,70,746 suicides, 0.4% fewer than in "
             "2023, and a rate of 12.2 per lakh population."),
        stats([card("12.2", "suicides per lakh population in 2024", "cyan", ADSI),
               card("73.5 : 26.5", "male to female ratio of suicide deaths, 2024", "indigo", ADSI),
               card("49.0%", "of suicides reported from five states: Maharashtra, Tamil Nadu, "
                    "Madhya Pradesh, Karnataka and West Bengal", "amber", ADSI)], cols=3),
        tw(pp("cyan", "Age", "People aged 18 to under 30 accounted for 33.1% of suicides and those "
              "30 to under 45 for 32.5%. NCRB lists family problems, love affairs, illness and "
              "failure in examination as the main causes recorded for children under 18."),
           pp("amber", "Reading state shares", "Uttar Pradesh holds 17.0% of India's population and "
              "reported 5.4% of suicides. Differences this large partly reflect how well each "
              "state's police record and report deaths.")),
    ], compact=True),

    C("Trend", "Recorded suicides rose from 2020 to 2023 and levelled in 2024", [
        {"t": "chart", "canvas": "adsiTrend",
         "title": "Suicides recorded in India and rate per lakh, 2020-2024",
         "source": ADSI + ", List 2.1",
         "type": "bar",
         "data": {"labels": ["2020", "2021", "2022", "2023", "2024"],
                  "datasets": [{"type": "bar", "label": "Suicides (thousands)",
                                "data": [153.1, 164.0, 170.9, 171.4, 170.7],
                                "backgroundColor": "#6366F1", "yAxisID": "y"},
                               {"type": "line", "label": "Rate per lakh",
                                "data": [11.3, 12.0, 12.4, 12.3, 12.2],
                                "borderColor": "#EF4444", "backgroundColor": "#EF4444",
                                "yAxisID": "y1"}]},
         "options": {"__js__": "{ scales:{ y:{min:0,position:'left'}, y1:{min:0,max:15,"
                               "position:'right',grid:{drawOnChartArea:false}} } }"}},
        body("NCRB computes rates on projected population for non-census years. The 2022 rate "
             "of 12.4 was the highest in the five years shown. The National Suicide Prevention "
             "Strategy measures its target against 2020, so the trend since then is the one a "
             "programme manager should watch.", sm=True),
    ], compact=True),

    C("Recorded causes", "What police records list as causes, 2024", [
        body("ADSI assigns each death a cause from police records. Family problems and illness "
             "together account for over half. These categories describe the trigger an "
             "investigating officer recorded, which is a narrow view of a decision with many "
             "causes. WHO's media guidance warns against reducing a suicide to a single factor."),
        table(["Recorded cause (NCRB)", "Share of suicides, 2024"], [
            ["Family problems (other than marriage related)", "33.5%"],
            ["Illness (physical and mental)", "17.9%"],
            ["Drug abuse or alcoholic addiction", "7.6%"],
            ["Marriage related issues", "5.0%"],
            ["Love affairs", "4.6%"],
            ["Bankruptcy or indebtedness", "4.4%"],
            ["Unemployment", "1.5%"],
            ["Failure in examination", "1.2%"],
            ["Causes not known", "10.1%"],
        ]),
        body("Source: " + ADSI + ", Figure 2.6. NCRB notes that women's share was higher among "
             "deaths recorded under physical abuse, dowry-related issues and infertility.", sm=True),
    ], compact=True),

    C("Who died", "Daily wage earners were nearly a third of those who died", [
        {"t": "chart", "canvas": "adsiProfession",
         "title": "Suicides by profession of the person, India 2024 (%)",
         "source": ADSI + ", Figure 2.8",
         "type": "doughnut",
         "data": {"labels": ["Daily wage earners", "Housewives", "Self-employed",
                             "Professionals and salaried", "Unemployed", "Students",
                             "Farming sector", "Retired", "Others"],
                  "datasets": [{"data": [31.0, 13.0, 10.5, 9.9, 8.7, 8.5, 6.2, 0.5, 11.8],
                                "backgroundColor": ["#EF4444", "#6366F1", "#F59E0B", "#0EA5E9",
                                                    "#10B981", "#8B5CF6", "#84CC16", "#94A3B8",
                                                    "#CBD5E1"]}]},
         "options": {"__js__": "{ plugins:{ legend:{ position:'right' } } }"}},
        body("Housewives made up 48.9% of women who died by suicide (22,113 of 45,245). The farming "
             "sector accounted for 10,546 deaths: 4,633 farmers or cultivators and 5,913 "
             "agricultural labourers. The occupational pattern points to insecure work and unpaid "
             "domestic work as places to look for risk, which is where development programmes "
             "already operate.", sm=True),
    ], compact=True),

    C("Caveats", "Why the recorded figure is a floor", [
        body("NCRB counts deaths that police record as suicide. Several things keep deaths out of "
             "that count, and they work in one direction, so the true number is higher. WHO's "
             "suicide fact sheet notes that only some 80 member states have good-quality vital "
             "registration data, and that stigma and the illegality of suicidal behaviour in some "
             "countries make under-reporting worse for suicide than for most causes of death."),
        tw([panel("amber", "Sources of under-count", [bullets([
                "Families report a death as an accident or illness to avoid police and stigma",
                "Rural deaths are certified without a medical cause",
                "Deaths among women may be recorded under other heads",
                "States differ in how thoroughly police compile records"], sm=True)])],
           [panel("cyan", "How to use NCRB well", [bullets([
                "Quote the edition year and say it is police-recorded data",
                "Compare trends within one state over time; avoid ranking states",
                "Treat the cause categories as recorded triggers",
                "Pair it with the Medical Certification of Cause of Death and studies"], sm=True)])]),
        hbox("ADSI does not record suicide attempts. NMHS found 0.9% of adults at high suicide "
             "risk in the past month, a much larger group than those who die.", "indigo"),
    ], compact=True),

    C("Facts to lead with", "Six facts about suicide that change how staff respond", [
        body("WHO's 2023 media resource lists common misconceptions about suicide and the facts "
             "that answer them. The six facts below come from its "
             "Annex 4 and are the ones field staff most need."),
        table(["Fact (WHO, 2023)", "What it means for a field worker"], [
            ["Talking openly can give a person other options or time to rethink",
             "Asking directly about suicidal thoughts is safe and can help"],
            ["People who talk about suicide may act on it", "Take every mention seriously"],
            ["People who are suicidal are often ambivalent and want relief from pain",
             "Support at the right moment can tip the balance toward living"],
            ["Acute risk is often short-term", "Getting through the crisis matters most"],
            ["Most suicides are preceded by verbal or behavioural warning signs",
             "Learn the signs and act on them"],
            ["Many people who are suicidal have no mental health condition",
             "Debt, violence, pain and loss can be enough; screen widely"],
        ]),
        hbox("WHO adds that suicidal behaviour is never the result of a single factor. Avoid "
             "explaining any death by one cause, in conversation or in a report.", "indigo"),
        body("Source: WHO, Preventing suicide: a resource for media professionals, update 2023, "
             "Annex 4. " + HELP, sm=True),
    ], compact=True),

    C("Prevention evidence", "Restricting the most toxic means saved lives in Sri Lanka", [
        body("WHO's LIVE LIFE initiative (2021) names four interventions with the best evidence: "
             "limit access to the means of suicide, work with the media on responsible reporting, "
             "build socio-emotional life skills in adolescents, and identify, assess, manage and "
             "follow up anyone affected by suicidal behaviour. WHO calls banning highly hazardous "
             "pesticides a particularly inexpensive and cost-effective intervention."),
        tw(pp("green", "The Sri Lanka evidence", "Gunnell and colleagues (Int J Epidemiol, 2007) "
              "found that restrictions on importing and selling the most toxic class of pesticides "
              "in 1995 and on endosulfan in 1998 coincided with falls in suicide in men and women "
              "of all ages: 19,769 fewer suicides in 1996-2005 than in 1986-95."),
           pp("cyan", "What this means for programmes", "Agricultural and livelihoods projects can "
              "support safer storage, the switch to less toxic products and the regulation of "
              "hazardous ones. This is a policy and farm-practice question, handled through "
              "agriculture departments and farmer groups.")),
        hbox("Means restriction works because many suicidal crises are brief. Putting time and "
             "distance between a person in crisis and a lethal means gives the crisis a chance to "
             "pass.", "indigo"),
    ]),
]

# ===================== SECTION 04: DETERMINANTS AND STIGMA =====================
S04 = [
    D("04", "Section Four", "Social determinants: poverty, debt, caste, gender and stigma"),

    C("Poverty", "Poverty and common mental disorders feed each other", [
        body("Vikram Patel and Arthur Kleinman reviewed community studies from six low- and "
             "middle-income countries in the <em>Bulletin of the World Health Organization</em> "
             "(2003). Most found that indicators of poverty were associated with common mental "
             "disorders, and the most consistent link was with low education. The evidence for a "
             "link with income alone was weaker."),
        tw(pp("red", "Poverty to illness", "Patel and Kleinman point to insecurity and "
              "hopelessness, rapid social change, the risk of violence and physical ill-health as "
              "the routes by which poor people become more vulnerable."),
           pp("amber", "Illness to poverty", "The direct and indirect costs of mental ill-health "
              "worsen a household's economic condition: lost days of work, spending on care and "
              "debt. The two together form a vicious cycle.")),
        quote("Common mental disorders need to be placed alongside other diseases associated with "
              "poverty by policy-makers and donors.", "Patel and Kleinman, Bull World Health Organ "
              "2003;81(8):609-15"),
        body("They also suggested that investments such as education and microcredit may have "
             "unanticipated benefits for mental health.", sm=True),
    ]),

    C("Which poverty", "Some dimensions of poverty matter more than others", [
        body("Crick Lund and colleagues systematically reviewed 115 studies (<em>Social Science "
             "&amp; Medicine</em>, 2010). In community studies, 73% of bivariate and 79% of "
             "multivariate analyses found a positive association between poverty and common "
             "mental disorders. The detail is more useful than the headline, because it tells a "
             "programme which lever to pull."),
        table(["Poverty dimension", "Association with common mental disorders (Lund et al., 2010)"], [
            ["Education", "Relatively consistent and strong"],
            ["Food insecurity", "Relatively consistent and strong"],
            ["Housing", "Relatively consistent and strong"],
            ["Social class and socio-economic status", "Relatively consistent and strong"],
            ["Financial stress", "Relatively consistent and strong"],
            ["Income, employment", "More equivocal"],
            ["Consumption", "Particularly equivocal"],
        ]),
        hbox("Financial stress and food insecurity matter more than the level of income. A cash "
             "transfer that arrives late and unpredictably may do less for mental health than a "
             "smaller one that arrives on time.", "green"),
    ], compact=True),

    C("A framework", "Five areas of social determinants, mapped to the SDGs", [
        body("In 2018 Lund and colleagues, with Vikram Patel and WHO's Shekhar Saxena among the "
             "authors, published a systematic review of reviews in <em>Lancet Psychiatry</em>. "
             "They built a framework aligned with the Sustainable Development Goals and reviewed "
             "289 articles under five areas. The framework helps a programme team ask where its "
             "own work touches mental health."),
        table(["Area", "Examples", "Where programmes act"], [
            ["Demographic", "Age, sex, ethnicity", "Targeting adolescents, older people, women"],
            ["Economic", "Income, debt, unemployment, inequality", "Livelihoods, social protection, credit"],
            ["Neighbourhood", "Housing, safety, infrastructure", "Urban upgrading, water, lighting"],
            ["Environmental events", "Disasters, conflict, climate change", "Disaster response, migration support"],
            ["Social and cultural", "Social support, education, discrimination", "Schools, collectives, anti-discrimination work"],
        ]),
        body("Source: Lund et al., Lancet Psychiatry 2018;5(4):357-69. The \"Where programmes act\" "
             "column is our teaching gloss.", sm=True),
    ], compact=True),

    C("Debt and land", "Debt, crop loss and insecure work", [
        body("Indebtedness appears in the NCRB data as a recorded cause for 4.4% of suicides in "
             "2024, and the farming sector accounted for 10,546 deaths, 6.2% of the total. NCRB "
             "reports that 36.1% of farming-sector suicides were in Maharashtra and 28.1% in "
             "Karnataka. Daily wage earners were 31.0% of all suicides. These figures place the "
             "issue inside the work of rural livelihoods, credit and labour programmes."),
        tw([panel("amber", "Pressure points to watch", [bullets([
                "Repayment dates on loans from moneylenders and microfinance groups",
                "Crop failure, price crashes and delayed procurement payments",
                "Delays in wage payments under rural employment schemes",
                "Migration that leaves families without support"], sm=True)])],
           [panel("green", "What programmes can do", [bullets([
                "Train field staff to notice distress and refer, Section 11",
                "Build grievance and rescheduling options into credit products",
                "Link crop insurance claims with outreach visits",
                "Keep wage and benefit payments on time"], sm=True)])]),
        hbox("Rural wage employment changed on 1 July 2026, when the Viksit Bharat G RAM G Act, "
             "2025 replaced MGNREGA with a 125-day entitlement. Watch how payment timeliness works "
             "under the new law.", "indigo"),
    ], compact=True),

    C("Caste and religion", "Discrimination has a mental health cost of its own", [
        body("Aashish Gupta and Diane Coffey analysed 10,125 adults in WHO's Study on Global "
             "Ageing and Adult Health in India (<em>Population Research and Policy Review</em>, "
             "2020). They found large gaps in self-reported mental health between higher caste "
             "Hindus and two marginalised groups, Scheduled Castes and Muslims. Differences in "
             "socio-economic status could not fully explain the gaps, especially for Muslims."),
        tw(pp("red", "Policy implication drawn by the authors", "Policies need to move beyond "
              "redistribution and address discrimination against Scheduled Castes and Muslims. "
              "Income support alone will not close the gap."),
           pp("indigo", "Higher education", "Komanapalli and Rao (<em>Transcultural "
              "Psychiatry</em>, 2021) argue that when Dalit students die by suicide, institutions "
              "often describe the death as personal problems or depression, which can deflect "
              "attention from caste discrimination.")),
        hbox("A mental health programme that ignores caste can end up treating the effects of "
             "discrimination while leaving its cause in place. Collect data by social group, with "
             "consent, and design for the people the data show are left out.", "amber"),
    ]),

    C("Gender", "Gender shapes who becomes unwell and who is counted", [
        body("WHO's depression fact sheet (updated 11 September 2026) reports that depression is about 1.5 times more "
             "common among women than men, and that more than 10% of pregnant women and women who "
             "have just given birth experience depression worldwide. NMHS 2015-16 found current "
             "depression in 3.0% of women and 2.4% of men. The WHO 2022 report names childhood "
             "sexual abuse and bullying as major causes of depression."),
        tw(pp("cyan", "What the suicide data show", "Men are about three quarters of recorded "
              "suicides in India. Women's deaths cluster among housewives (48.9% of women's "
              "suicides in 2024) and in causes recorded as marriage or dowry related. Both patterns "
              "point to the household as a place of risk."),
           pp("green", "What programmes can do", "Maternal health programmes can screen for "
              "perinatal depression; the Thinking Healthy Programme in Section 08 shows the effect "
              "is large. Gender-based violence services can add mental health support and "
              "referral, with safety planning first.")),
        hbox("Men's distress is often expressed as alcohol use, anger or withdrawal, and men seek "
             "help less. Outreach through work sites and men's groups reaches people that clinic "
             "screening misses.", "indigo"),
    ]),

    C("Stigma", "Stigma is often described as worse than the condition", [
        body("The Lancet Commission on Ending Stigma and Discrimination in Mental Health, "
             "co-chaired by Graham Thornicroft and launched on 10 October 2022, drew on more than "
             "50 experts, including people with lived experience. King's College London's "
             "summary reports that many people with lived experience describe stigma as worse than "
             "the condition itself."),
        tw(pp("green", "What works best", "The Commission's review of the evidence found that "
              "social contact between people with and without lived experience of mental health "
              "conditions is the most effective way to reduce stigma and discrimination."),
           pp("cyan", "Who should lead", "The report concludes that people with lived experience "
              "must be supported to play active and central roles in stigma reduction. Its "
              "recommendations include decriminalising suicide and training health staff.")),
        table(["Form of stigma", "How it shows in South Asian settings"], [
            ["Public", "Marriage prospects of a family harmed by a member's diagnosis"],
            ["Self", "A person stops going to a clinic to avoid being seen there"],
            ["Structural", "Laws, insurance exclusions and institutional practices that treat mental illness differently"],
        ]),
        body("Source for the Commission: Thornicroft et al., Lancet 2022;400:1438-80; KCL news, "
             "10 October 2022. The table is our teaching summary.", sm=True),
    ], compact=True),
]

# ===================== SECTION 05: LAW IN INDIA =====================
S05 = [
    D("05", "Section Five", "The law in India: the Mental Healthcare Act and the BNS"),

    C("Overview", "The Mental Healthcare Act, 2017 at a glance", [
        body("The Act replaced the Mental Health Act, 1987. It came into force on 29 May 2018 "
             "and was extended to the Union territories of Jammu and Kashmir and Ladakh by "
             "notification in October 2019. Its preamble ties it to the CRPD. For practitioners, "
             "the useful way to read it is by the rights it creates and the duties it places on "
             "government."),
        table(["Section", "What it provides"], [
            ["s4", "Presumption of capacity to make mental healthcare decisions"],
            ["s5", "Right to make an advance directive"],
            ["s14", "Right to appoint a nominated representative"],
            ["s18", "Right to access mental healthcare from public services"],
            ["s19", "Right to community living"],
            ["s21", "Equality with physical illness, including insurance (s21(4))"],
            ["s23", "Right to confidentiality"],
            ["s29", "Duty to run promotion, prevention and suicide reduction programmes"],
            ["s95", "Prohibited procedures, including chaining"],
            ["s99", "Consent and safeguards in research"],
            ["s115", "Presumption of severe stress in attempted suicide"],
        ]),
        body("Source: " + MHCA + ", as published (52 pages). Read the sections themselves before "
             "advising anyone.", sm=True),
    ], compact=True),

    C("Section 18", "Section 18 makes access to care a legal right", [
        quote("Every person shall have a right to access mental healthcare and treatment from "
              "mental health services run or funded by the appropriate Government.",
              MHCA + ", section 18(1)"),
        body("Section 18(2) says what the right means: services of affordable cost and good "
             "quality, in sufficient quantity, geographically accessible, without discrimination "
             "on grounds including gender, sexual orientation, religion, caste, class or "
             "disability, and acceptable to persons with mental illness and their families."),
        tw(pp("cyan", "Services that must exist", "Section 18(4) lists outpatient and inpatient "
              "care, half-way homes and supported accommodation, support for families and "
              "home-based rehabilitation, hospital and community rehabilitation, and child and old "
              "age mental health services."),
           pp("green", "How services must be delivered", "Section 18(5) requires integration into "
              "general healthcare at all levels, care that lets people live in the community, "
              "long-term institutional care only as a last resort, and services close enough that "
              "no one has to travel long distances.")),
        hbox("A right written this way gives programmes a standard to measure public services "
             "against, and gives communities a basis for a grievance or petition.", "indigo"),
    ]),

    C("Equality and dignity", "Community living, parity and protection from abuse", [
        tw([panel("cyan", "Section 19: community living", [body(
                "Every person with mental illness has a right to live in, be part of and not be "
                "segregated from society. No one may remain in a mental health establishment only "
                "because they have no family, are not accepted by their family, are homeless or "
                "lack community facilities. Government must provide half-way homes and group "
                "homes within a reasonable period.", sm=True)])],
           [panel("green", "Section 21: equality with physical illness", [body(
                "Emergency services, ambulances and living conditions for mental illness must "
                "match those for physical illness. Section 21(2) says a child under three should "
                "ordinarily stay with a mother receiving care. Section 21(4) requires every "
                "insurer to cover mental illness on the same basis as physical illness.", sm=True)])]),
        panel("red", "Section 95: prohibited procedures", [body(
            "Electro-convulsive therapy without muscle relaxants and anaesthesia is banned, as is "
            "ECT for minors except with guardian consent and Board permission. Sterilisation as a "
            "treatment for mental illness is banned. No person with mental illness may be chained "
            "in any manner or form.", sm=True)]),
        hbox("Chaining still occurs in some faith-healing sites and homes. Section 95(1)(d) is "
             "the provision to cite when reporting it.", "amber"),
    ], compact=True),

    C("Planning ahead", "Advance directives and nominated representatives", [
        body("Two tools let a person decide in advance how they want to be treated if they later "
             "lose capacity. They are among the Act's most rights-protective provisions, and few "
             "people know about them."),
        tw([panel("cyan", "Advance directive (section 5)", [bullets([
                "Any adult may write one, whatever their past illness",
                "It can say how the person wishes, and does not wish, to be treated",
                "It can name nominated representatives in order of preference",
                "It applies only when the person lacks capacity, and stops when capacity returns",
                "A decision made while the person has capacity overrides it"], sm=True)])],
           [panel("green", "Nominated representative (section 14)", [bullets([
                "Any adult may appoint one in writing on plain paper, signed or thumb-printed",
                "The representative must be an adult and consent in writing",
                "If none is appointed, the Act sets an order of precedence",
                "The representative supports the person's decisions and has rights to information"],
                sm=True)])]),
        hbox("A community programme can help people write advance directives while they are well, "
             "with the person's chosen supporter present. Keep a copy only with consent.", "indigo"),
    ], compact=True),

    C("Admission", "Admission, emergency treatment and review", [
        body("Most people with mental illness are treated as outpatients. When admission is "
             "considered, the Act sets graded routes, each with safeguards, and Mental Health "
             "Review Boards constituted by the State Authority (section 73) hear applications "
             "and appeals. Practitioners who accompany a person to hospital should know which "
             "route is being used."),
        table(["Route", "Section", "Key safeguard"], [
            ["Independent admission", "s86", "An adult asks to be admitted, of their own free "
             "will, and understands the purpose"],
            ["Admission of a minor", "s87", "Application by the nominated representative and two "
             "independent examinations"],
            ["Supported admission, up to 30 days", "s89", "Two independent examinations; risk of "
             "harm to self or others or inability to care for self; least restrictive option, "
             "taking any advance directive into account"],
            ["Emergency treatment", "s94", "Only to prevent death, serious harm or serious "
             "damage; limited to 72 hours or until assessment, whichever is earlier; no ECT"],
        ]),
        hbox("Supported admission is the exception. Section 18(5)(c) says long-term institutional "
             "care is a last resort, after community treatment has been tried.", "amber"),
        body("Source: " + MHCA + ", sections 73, 86, 87, 89 and 94. Section 94(4) allows up to "
             "seven days during a declared disaster or emergency.", sm=True),
    ], compact=True),

    C("Section 115", "Attempted suicide: from crime to care", [
        quote("Notwithstanding anything contained in section 309 of the Indian Penal Code any "
              "person who attempts to commit suicide shall be presumed, unless proved otherwise, to "
              "have severe stress and shall not be tried and punished under the said Code.",
              MHCA + ", section 115(1)"),
        body("Section 115(2) then places a duty on government to provide care, treatment and "
             "rehabilitation to a person who has attempted suicide, to reduce the risk of a "
             "further attempt. The law therefore moved the response from the police station to "
             "the health system."),
        tw(pp("indigo", "The history", "In P. Rathinam v Union of India (1994) a Division Bench of "
              "the Supreme Court held section 309 IPC unconstitutional. A Constitution Bench "
              "overruled it in Gian Kaur v State of Punjab (21 March 1996), holding that section "
              "309 did not violate Article 14 or 21."),
           pp("green", "Why the presumption matters", "Before 2018 a hospital could hesitate to "
              "treat a person after an attempt for fear of a police case. The presumption lets "
              "emergency staff treat first.")),
    ]),

    C("BNS 2023", "The Bharatiya Nyaya Sanhita has no general offence of attempted suicide", [
        body("The Bharatiya Nyaya Sanhita, 2023 replaced the Indian Penal Code from 1 July 2024. "
             "It carries no equivalent of section 309 IPC. The offences that remain concern "
             "abetment and one narrow form of attempt."),
        table(["BNS section", "Offence", "Punishment"], [
            ["s107", "Abetment of suicide of a child, a person of unsound mind, a delirious person "
             "or an intoxicated person", "Death, life imprisonment or up to 10 years, and fine"],
            ["s108", "Abetment of suicide", "Up to 10 years and fine"],
            ["s226", "Attempt to commit suicide with intent to compel or restrain a public servant "
             "from discharging official duty", "Simple imprisonment up to 1 year, fine, both, or "
             "community service"],
        ]),
        tw(pp("amber", "Reading s226 carefully", "Section 226 reaches only an attempt made with intent "
              "to compel or restrain a public servant, as in a protest aimed at an official. An "
              "attempt made in distress, without that intent, falls outside it."),
           pp("cyan", "What has not changed", "Section 115 of the MHCA still requires care. Its "
              "text refers to section 309 IPC; with no matching BNS offence, the duty of care in "
              "s115(2) is what matters in practice.")),
        body("Source: Bharatiya Nyaya Sanhita, 2023 (Act 45 of 2023), Gazette of India, 25 "
             "December 2023.", sm=True),
    ], compact=True),

    C("The courts", "The Supreme Court treats mental health as part of Article 21", [
        body("In <em>Sukdeb Saha v State of Andhra Pradesh</em> (2025 INSC 893, decided 25 July "
             "2025), a bench of Justices Vikram Nath and Sandeep Mehta heard the case of a "
             "17-year-old student whose death occurred while she was preparing for NEET at a "
             "coaching institute in Visakhapatnam. The Court held that "
             "mental health is an integral part of the right to life under Article 21 and found a "
             "regulatory vacuum on student suicide prevention."),
        table(["Guideline (summarised from the judgment)", "Who it binds"], [
            ["Adopt a uniform mental health policy drawing on UMMEED, MANODARPAN and the NSPS",
             "All educational institutions"],
            ["Engage at least one trained counsellor, psychologist or social worker",
             "Institutions with 100 or more students"],
            ["No batch segregation by academic performance or public shaming",
             "All institutions, coaching centres in particular"],
            ["Written referral protocols; helplines including Tele-MANAS displayed",
             "Hostels, classrooms, websites"],
        ]),
        body("Source: the judgment, Supreme Court of India, Criminal Appeal arising out of SLP "
             "(Crl.) No. 6378 of 2024, 25 July 2025, paras 31-38. The Court directed states to act on the guidelines and set "
             "up district monitoring.", sm=True),
    ], compact=True),

    C("Research and police", "Duties of police and rules for research", [
        tw([panel("cyan", "Section 100: police", [body(
                "The Act gives police officers duties toward persons with mental illness who are "
                "homeless or wandering, or at risk to themselves or others: take them into "
                "protection, inform them of the reasons, and bring them to a public health "
                "facility for assessment. Section 103 covers prisoners with mental illness.",
                sm=True)])],
           [panel("green", "Section 99: research", [body(
                "Researchers must obtain free and informed consent from all persons with mental "
                "illness. Research with interventions on a person who cannot consent needs the "
                "State Mental Health Authority's permission and five conditions, including ethics "
                "committee approval. Consent can be withdrawn at any time.", sm=True)])]),
        body("These two provisions matter to development practitioners in different ways. "
             "Outreach workers who find a homeless person in crisis can involve police under a "
             "statutory duty of care. Evaluators planning a trial or survey that includes people "
             "with mental illness must build section 99 into their protocol, alongside the ICMR "
             "guidelines covered in Section 10."),
        hbox("Section 23 also gives a right to confidentiality, which applies to programme records "
             "as much as hospital ones.", "indigo"),
    ]),
]

# ===================== SECTION 06: PROGRAMMES IN INDIA =====================
S06 = [
    D("06", "Section Six", "India's programmes: from 1982 to Tele-MANAS"),

    C("NMHP and DMHP", "The National and District Mental Health Programmes", [
        body("India launched the National Mental Health Programme (NMHP) in 1982, with the aim "
             "of making mental healthcare part of general healthcare instead of confining it to "
             "specialised hospitals. The District Mental Health Programme (DMHP) brought "
             "community services to the district level. The PIB backgrounder of 7 February 2025 "
             "reports that the DMHP covers 767 districts."),
        tw([panel("cyan", "What a DMHP provides", [bullets([
                "Outpatient services and counselling",
                "Suicide prevention and awareness activities",
                "A 10-bed inpatient facility at district level",
                "Outreach, medicines and continuing care for severe disorders"], sm=True)])],
           [panel("amber", "Where it falls short", [bullets([
                "Posts sanctioned and posts filled are different numbers",
                "Medicines run out at primary level",
                "Few districts reach villages beyond the district hospital",
                "Funds through the National Health Mission compete with other priorities"],
                sm=True)])]),
        body("The right-hand column lists common implementation problems for a programme team to "
             "check locally, as a checklist to verify in each district.", sm=True),
        hbox("Ask the district: is the psychiatrist post filled, which days does the team visit "
             "community health centres, and which medicines are in stock this month?", "green"),
    ]),

    C("Primary care", "Mental health in Ayushman Arogya Mandirs and the workforce", [
        body("Under Ayushman Bharat, more than 1.73 lakh sub health centres and primary health "
             "centres have been upgraded to Ayushman Arogya Mandirs, and mental health services "
             "are part of their package of comprehensive primary care (PIB backgrounder, "
             "February 2025). This is where most people in rural India will first meet the "
             "health system."),
        stats([card("1.73 lakh+", "health centres upgraded to Ayushman Arogya Mandirs", "cyan",
                    PIB25),
               card("25", "Centres of Excellence sanctioned in 2024 to train postgraduates", "indigo",
                    PIB25),
               card("47", "government-run mental hospitals, including three central institutes",
                    "amber", PIB25)], cols=3),
        tw(pp("cyan", "Training at scale", "The PIB backgrounder notes that the iGOT-Diksha "
              "platform has been used since 2020 to train doctors, nurses, frontline workers and "
              "community volunteers in mental healthcare."),
           pp("green", "Where programmes fit", "ASHAs, anganwadi workers and community health "
              "officers already visit homes. Teaching them to notice distress and refer adds "
              "mental health to a visit that is happening anyway.")),
    ], compact=True),

    C("Tele-MANAS", "Tele-MANAS: a national helpline in 20 languages", [
        body("The Government launched the National Tele Mental Health Programme on 10 October "
             "2022. Callers dial 14416 or 1-800-891-4416 free of charge, at any hour, and are "
             "routed to a counsellor in their state's language, with referral to psychiatrists "
             "and to in-person services when needed."),
        stats([card("32.84 lakh+", "calls handled since launch, as of 2 February 2026", "cyan", PIB26),
               card("53", "Tele-MANAS cells set up in 36 states and union territories", "indigo",
                    PIB26),
               card("20", "languages offered, chosen by the states", "green", PIB26)], cols=3),
        tw(pp("cyan", "What has been added", "A mobile app was launched on World Mental Health Day, "
              "10 October 2024, and later extended to ten more regional languages. Video "
              "consultation has been added, and a dedicated cell at AFMC Pune serves the armed "
              "forces and their families (PIB, February 2026)."),
           pp("amber", "Using it in a programme", "Print the number on every training handout, "
              "ID card and poster. Test it in your district's language before you rely on it. "
              "Record referrals, with consent, so you can follow up.")),
    ], compact=True),

    C("NSPS 2022", "India's first National Suicide Prevention Strategy", [
        body("The Ministry of Health and Family Welfare issued the National Suicide Prevention "
             "Strategy in 2022, the country's first. Its goal is to reduce suicide mortality by "
             "10% by 2030, compared with 2020. It follows WHO's South-East Asia regional strategy "
             "and sets out a path it calls REDS."),
        table(["REDS", "What the strategy intends"], [
            ["Reinforce", "Leadership, partnerships and institutional capacity"],
            ["Enhance (the strategy's own term)", "The capacity of health services to provide suicide prevention services"],
            ["Develop", "Community resilience and societal support; reduce stigma"],
            ["Strengthen", "Surveillance and evidence generation"],
        ]),
        flow(["Within 3 years: effective surveillance mechanisms for suicide",
              "Within 5 years: psychiatric OPDs offering suicide prevention through the DMHP in "
              "all districts",
              "Within 8 years: a mental well-being curriculum in all educational institutions"]),
        body("Source: Ministry of Health and Family Welfare, National Suicide Prevention Strategy "
             "(2022), section 5.1. The strategy also calls for media reporting guidelines and "
             "restricting access to means.", sm=True),
    ], compact=True),

    C("Schools", "Manodarpan, UMMEED and the school as a setting", [
        body("The Ministry of Education's Manodarpan initiative was inaugurated on 21 July 2020 to "
             "provide psychosocial support to students, teachers and parents during the COVID-19 "
             "pandemic and after it, including a toll-free tele-counselling line. In 2023 the "
             "Ministry circulated draft guidelines called UMMEED for schools on preventing "
             "suicide, built around a school wellness team that identifies students at risk and "
             "responds first."),
        tw(pp("cyan", "What the Supreme Court added", "In Sukdeb Saha (2025) the Court told "
              "institutions to draw on UMMEED, Manodarpan and the NSPS when writing their policies, "
              "and set a counsellor requirement for institutions with 100 or more students."),
           pp("green", "What WHO recommends", "WHO's mental health fact sheet (2026) says "
              "school-based social and emotional learning programmes are especially effective "
              "across all income levels. Section 09 covers child and adolescent mental health in "
              "more depth.")),
        hbox("Education programmes can add mental health without new staff: train teachers to "
             "notice, set up a referral route, and stop practices such as ranking students in "
             "public.", "indigo"),
    ]),

    C("The care pathway", "How the pieces are meant to connect", [
        body("Each programme covers one step. A person in a village should be able to move "
             "through the steps below, and a development programme's job is often to make the "
             "connections work where they break."),
        flow(["Community: ASHA, teacher, SHG member or volunteer notices distress",
              "First contact: Tele-MANAS 14416 or the Ayushman Arogya Mandir",
              "Primary care: assessment, counselling, basic medicines",
              "District: DMHP team, psychiatrist, 10-bed inpatient unit",
              "Specialist: medical college department or mental hospital",
              "Return: follow-up and rehabilitation in the community"]),
        tw(pp("amber", "Where it usually breaks", "Between notice and first contact (shame, cost "
              "of travel), and between district and return (no follow-up, medicines stop)."),
           pp("green", "What a programme can add", "Accompaniment to the first visit, travel "
              "support, reminders for follow-up, and a named contact who checks in after "
              "discharge.")),
    ], compact=True),

    C("Money and gaps", "Funding follows hospitals, need sits in the community", [
        body("WHO's 2022 report found that globally two of every three government dollars spent "
             "on mental health went to stand-alone psychiatric hospitals. Section 18(5)(c) of the "
             "Mental Healthcare Act points the other way: long-term institutional care only as a "
             "last resort. Budget analysis tells you which way a state is moving."),
        table(["Question to ask of a state budget", "Why it matters"], [
            ["How much of the mental health line goes to hospitals versus the DMHP?",
             "Shows whether money follows the community-care mandate"],
            ["Are DMHP funds released in the first half of the year?", "Late release delays hiring and medicines"],
            ["Are half-way homes and supported housing funded?", "Required by sections 18(4) and 19(3)"],
            ["Is the State Mental Health Authority funded and meeting?", "It oversees rights and research permissions"],
        ]),
        hbox("Public Finance &amp; Budgeting 101 shows how to read a state budget and its "
             "demand for grants.", "indigo"),
    ], compact=True),
]

# ===================== SECTION 07: SOUTH ASIA =====================
S07 = [
    D("07", "Section Seven", "Law and programmes across South Asia"),

    C("Bangladesh", "Bangladesh: a new mental health law, an old criminal provision", [
        body("Bangladesh's Mental Health Act, 2018 (Act 60 of 2018), dated 14 November 2018, "
             "repealed the Lunacy Act, 1912. Its preamble says the old law had lost relevance and "
             "that a new law was needed to secure care, dignity, property rights, rehabilitation "
             "and overall welfare for people with mental health problems."),
        tw(pp("red", "Attempted suicide", "Section 309 of the Penal Code, 1860, \"Attempt to commit "
              "suicide\", still appears in the Penal Code on the Government's official laws website "
              "(bdlaws.minlaw.gov.bd, checked October 2026)."),
           pp("cyan", "For programmes", "Where attempted suicide is a crime, people and families "
              "avoid hospitals after an attempt. NGOs in Bangladesh need clear protocols on "
              "confidentiality and on whom staff are and are not obliged to inform.")),
        hbox("Bangladesh and India share a Penal Code ancestry. India removed the general offence "
             "in practice through MHCA s115 and then in the BNS; Bangladesh had not done so as of "
             "October 2026.", "amber"),
        body("Sources: Mental Health Act 2018 and Penal Code 1860, bdlaws.minlaw.gov.bd.", sm=True),
    ]),

    C("Pakistan", "Pakistan: decriminalised in 2022, contested in 2026", [
        body("Pakistan's Mental Health Ordinance, 2001 replaced the Lunacy Act, 1912. After the "
             "18th constitutional amendment in 2010, health became a provincial subject, and "
             "provinces passed their own laws: Sindh in 2013 and Punjab in 2014 (Tareen and "
             "Tareen, <em>BJPsych International</em>, 2016)."),
        flow(["December 2022: Criminal Laws (Amendment) Act omits section 325 PPC, the offence "
              "of attempted suicide",
              "18 May 2026: Federal Shariat Court holds the omission repugnant to Islam and says "
              "s325 stands restored",
              "June 2026: Pakistan Psychiatric Society appeals to the Shariat Appellate Bench of "
              "the Supreme Court"]),
        tw(pp("amber", "Status as of October 2026", "Article 203D of the Constitution says a Federal "
              "Shariat Court decision does not take effect while an appeal against it is pending; "
              "for decisions after the 26th Amendment (2024) the appeal is to be decided within "
              "twelve months, after which the decision takes effect unless the Supreme Court "
              "suspends it. The appeal was pending in the reports we could find. Check the "
              "current legal position before advising any programme in Pakistan."),
           pp("green", "Evidence from Pakistan", "Pakistan produced two of the best-known "
              "task-sharing trials, Thinking Healthy in Rawalpindi and Problem Management Plus in "
              "Peshawar, both in Section 08.")),
        body("Sources: Dawn, 18 May 2026 and 24 June 2026; Constitution of Pakistan, Article 203D; Tareen and Tareen 2016.", sm=True),
    ]),

    C("Nepal", "Nepal: policy without a dedicated mental health act", [
        body("Nepal adopted a national mental health policy in 1996. Singh and Khadka "
             "(<em>BJPsych International</em>, 2022) note that implementation stayed weak and a "
             "Mental Health Act never came into existence. The government launched the National "
             "Mental Health Strategy and Action Plan in December 2020, with WHO technical "
             "support."),
        stats([card("35 of 77", "districts to which mental health services had been extended", "cyan", "WHO Results Report, Nepal country story (2022)"),
               card("1,700+", "health workers trained in mental health, incl. 938 female community "
                    "health volunteers", "green", "WHO Results Report, Nepal country story (2022)")],
              cols=2),
        tw(pp("indigo", "Why Nepal is worth watching", "Its integration into primary care under "
              "WHO's Special Initiative for Mental Health relied on training existing health "
              "workers and volunteers, a model close to what Indian states attempt."),
           pp("amber", "A gap to note", "Without a statute, rights such as consent, review of "
              "involuntary admission and parity in insurance rest on policy, which is easier to "
              "change or ignore than law.")),
        body("Attempted suicide is no offence in Nepal. The National Penal (Code) Act, 2017 "
             "punishes only abetment, under section 185: up to five years and a fine of up to "
             "Rs 50,000. Source: Muluki Aparadh Samhita 2074, s185, official Nepali text published by the "
             "Nepal Law Commission (lawcommission.gov.np).",
             sm=True),
    ], compact=True),

    C("Sri Lanka", "Sri Lanka: a colonial ordinance and a draft bill", [
        body("Sri Lanka still runs on the Mental Diseases Ordinance, whose origins lie in 1873. "
             "<em>The Morning</em> (29 March 2026) reported that a concept paper for a new Mental "
             "Health Bill had been presented to Cabinet and that public consultations had begun, "
             "including sessions at the Human Rights Commission of Sri Lanka. The draft would "
             "shift the law from custody toward rights and community care."),
        tw(pp("green", "A regional lesson on suicide", "Sri Lanka's restrictions on the most "
              "toxic pesticides in 1995 and 1998 coincided with 19,769 fewer suicides in "
              "1996-2005 than in the previous decade (Gunnell et al., 2007). It is one of the "
              "strongest pieces of evidence anywhere for regulation as suicide prevention."),
           pp("cyan", "For programmes", "Until a new law passes, practitioners should treat "
              "rights protections as policy commitments and check the bill's progress before "
              "citing it.")),
        body("Attempted suicide is no longer an offence. Section 302 of the Penal Code, "
             "\"Attempt to commit suicide\", was repealed by section 4 of the Penal Code "
             "(Amendment) Act, No. 29 of 1998; abetment of suicide remains an offence under "
             "section 299. Source: Penal Code (Cap. 19), 1956 revised edition and the consolidated "
             "text noting the repeal.", sm=True),
        hbox("The common thread across the region is colonial-era law being replaced slowly, "
             "with rights language arriving first in policy and later, if at all, in statute.",
             "indigo"),
    ]),

    C("Comparison", "South Asia side by side, October 2026", [
        table(["Country", "Main mental health law", "Attempted suicide", "Notes"], [
            ["India", "Mental Healthcare Act 2017", "No general offence in BNS 2023; MHCA s115 "
             "presumes severe stress", "Tele-MANAS, DMHP in 767 districts, NSPS 2022"],
            ["Bangladesh", "Mental Health Act 2018", "Penal Code s309 still listed",
             "Repealed Lunacy Act 1912"],
            ["Pakistan", "Mental Health Ordinance 2001; provincial acts", "s325 PPC omitted 2022; "
             "FSC held it restored May 2026; appeal pending (Art. 203D)", "Health devolved after 2010"],
            ["Nepal", "No dedicated act (as of 2021 review)", "No offence; Penal Code 2017 s185 "
             "punishes abetment only",
             "Strategy and Action Plan 2020"],
            ["Sri Lanka", "Mental Diseases Ordinance (1873 origins)", "Penal Code s302 repealed "
             "by Act No. 29 of 1998",
             "Draft Mental Health Bill before Cabinet, 2026"],
        ]),
        body("WHO's 2022 report counted 20 countries that still criminalised attempted suicide. "
             "Sources are on the country slides.", sm=True),
        hbox("Laws in this table were changing during 2026. Recheck before using it in a "
             "policy brief.", "amber"),
    ], compact=True),
]

# ===================== SECTION 08: TASK SHARING =====================
S08 = [
    D("08", "Section Eight", "Task sharing: the evidence from South Asia and beyond"),

    C("The idea", "Task sharing puts trained lay workers at the centre of care", [
        body("With few psychiatrists and psychologists, waiting for specialists means most people "
             "are never treated. Task sharing trains people without professional mental health "
             "qualifications, such as community health workers, lay counsellors and volunteers, "
             "to deliver structured psychological help, with supervision from specialists. WHO's "
             "2026 mental health fact sheet names task sharing with non-specialist providers in "
             "primary care as part of community-based care."),
        term("Task sharing",
             "Moving specific, well-defined tasks from specialists to non-specialist workers "
             "who receive training and ongoing supervision, while specialists keep complex cases "
             "and support the system."),
        tw(pp("cyan", "What makes it work", "A short structured manual; training with role-play; "
              "weekly supervision; clear rules for when to refer; and fidelity checks on recorded "
              "sessions."),
           pp("amber", "What makes it fail", "Adding counselling to an already overloaded worker "
              "without time or pay; training without supervision; and no specialist to refer "
              "the people who need more.")),
        hbox("WHO's mhGAP Intervention Guide, version 2.0 (2016), gives non-specialist health "
             "workers algorithms for priority mental, neurological and substance use "
             "conditions.", "green"),
    ]),

    C("Thinking Healthy", "Thinking Healthy: lady health workers treat perinatal depression in Pakistan", [
        body("Atif Rahman and colleagues trained Pakistan's community-based primary health "
             "workers to deliver a cognitive behaviour therapy-based intervention to depressed "
             "mothers during routine home visits. The cluster-randomised trial ran in 40 Union "
             "Council clusters in rural Rawalpindi (<em>Lancet</em>, 2008)."),
        stats([card("23% vs 53%", "mothers with major depression at 6 months, intervention vs "
                    "control", "green", "Rahman et al., Lancet 2008;372:902-9"),
               card("27% vs 59%", "with major depression at 12 months", "cyan",
                    "Rahman et al., Lancet 2008;372:902-9")], cols=2),
        tw(pp("cyan", "Design", "903 mothers in their third trimester with perinatal depression. "
              "In control clusters, untrained health workers made the same number of visits, so "
              "the effect is not explained by attention alone."),
           pp("amber", "What did not change", "Infant weight and height, the primary outcomes, "
              "did not differ significantly at 6 or 12 months. Reporting this keeps the evidence "
              "accurate: the trial cut maternal depression by more than half.")),
    ], compact=True),

    C("HAP and PREMIUM", "The Healthy Activity Program in Goa's primary health centres", [
        body("The PREMIUM programme, led by Vikram Patel at Sangath, developed brief "
             "psychological treatments that lay counsellors could deliver. The Healthy Activity "
             "Program (HAP), based on behavioural activation, was tested in a randomised trial in "
             "ten primary health centres in Goa with adults whose PHQ-9 score indicated "
             "moderately severe to severe depression (<em>Lancet</em>, 2017)."),
        stats([card("64% vs 39%", "in remission (PHQ-9 below 10) at 3 months, HAP plus enhanced "
                    "usual care vs enhanced usual care", "green",
                    "Patel et al., Lancet 2017;389:176-85"),
               card("$9,333", "incremental cost per QALY gained (2015 international dollars), 87% "
                    "chance of being cost-effective", "cyan", "Patel et al., Lancet 2017;389:176-85")],
              cols=2),
        tw(pp("green", "Other benefits", "HAP also reduced disability, days out of work, suicidal "
              "thoughts or attempts, and intimate partner physical violence reported by women."),
           pp("indigo", "Its sister trial", "Counselling for Alcohol Problems (CAP), tested in the "
              "same centres with men who drank harmfully, was published alongside it "
              "(Nadkarni et al., Lancet 2017;389:186-95).")),
    ], compact=True),

    C("CAP", "Counselling for Alcohol Problems: lay counsellors and harmful drinking", [
        body("Alcohol is a large and neglected part of men's mental health in South Asia, and it "
             "drives violence and debt in households. Abhijit Nadkarni and colleagues tested "
             "Counselling for Alcohol Problems (CAP), a brief psychological treatment delivered by "
             "lay counsellors, with 377 men aged 18-65 whose AUDIT score of 12-19 indicated "
             "harmful drinking, in ten primary health centres in Goa (<em>Lancet</em>, 2017)."),
        stats([card("36% vs 26%", "in remission (AUDIT below 8) at 3 months, CAP plus enhanced "
                    "usual care vs enhanced usual care alone", "green",
                    "Nadkarni et al., Lancet 2017;389:186-95"),
               card("42% vs 18%", "abstinent in the past 14 days", "cyan",
                    "Nadkarni et al., Lancet 2017;389:186-95"),
               card("$217", "incremental cost per additional remission, 85% chance of being "
                    "cost-effective", "indigo", "Nadkarni et al., Lancet 2017;389:186-95")], cols=3),
        tw(pp("amber", "What did not change", "Among men who still drank, daily consumption did "
              "not fall. The trial found no effect on disability, days unable to work or "
              "intimate partner violence at three months."),
           pp("cyan", "Reading the result", "CAP helped some men stop. Others kept drinking at "
              "the same level, which is why a CAP-type service needs follow-up and links to "
              "family support.")),
    ], compact=True),

    C("PM+", "Problem Management Plus in conflict-affected Peshawar", [
        body("WHO developed Problem Management Plus (PM+) as a brief psychological intervention "
             "for adults in communities affected by adversity. Rahman and colleagues tested it in "
             "three primary care centres in Peshawar, Pakistan, with 346 adults who had high "
             "psychological distress and impaired functioning (<em>JAMA</em>, 2016). Lay health "
             "workers delivered five weekly 90-minute sessions."),
        table(["Component", "What it teaches"], [
            ["Problem solving", "Breaking a practical problem into steps and acting on one"],
            ["Behavioural activation", "Returning to activities that give pleasure or purpose"],
            ["Strengthening social support", "Reconnecting with people who can help"],
            ["Stress management", "A simple breathing technique for physical tension"],
        ]),
        body("At three months, anxiety scores on the Hospital Anxiety and Depression Scale were "
             "lower by 2.77 points and depression scores by 2.98 points in the PM+ group than "
             "with enhanced usual care. Post-traumatic stress symptoms and functional impairment "
             "also improved. 78.9% of participants were women. Source: Rahman et al., JAMA "
             "2016;316(24):2609-17.", sm=True),
    ], compact=True),

    C("Friendship Bench", "The Friendship Bench: grandmothers and problem-solving in Zimbabwe", [
        body("The Friendship Bench is the best-known task-sharing model outside South Asia, and "
             "its design has influenced programmes in India. Lay health workers, many of them "
             "older women, deliver six sessions of problem-solving therapy on a bench in the "
             "grounds of a primary care clinic, with an optional peer support group."),
        stats([card("13.7% vs 49.9%", "with depression symptoms (PHQ-9) at 6 months, intervention "
                    "vs control", "green", "Chibanda et al., JAMA 2016;316(24):2618-26"),
               card("573", "clinic attenders randomised across 24 clinics in Harare", "cyan",
                    "Chibanda et al., JAMA 2016;316(24):2618-26")], cols=2),
        tw(pp("cyan", "Who took part", "86.4% were women and 41.7% were living with HIV. "
              "Participants screened positive on a locally validated Shona symptom "
              "questionnaire."),
           pp("amber", "Lessons for South Asia", "Use a screening tool validated in the local "
              "language, hold sessions where people already go, and pick counsellors whom the "
              "community already trusts.")),
    ], compact=True),

    C("Atmiyata", "Atmiyata: village volunteers in Mehsana, Gujarat", [
        body("Atmiyata, developed by the Centre for Mental Health Law and Policy in Pune, trains "
             "volunteer community champions to identify distress, offer brief counselling and "
             "connect people to social benefits and care. It was evaluated in a stepped-wedge "
             "cluster randomised trial across 645 villages in Mehsana district between April 2017 "
             "and August 2019 (Pathare et al., <em>PLoS One</em>, 2023)."),
        stats([card("OR 2.2", "recovery from depression or anxiety symptoms at 3 months", "green",
                    "Pathare et al., PLoS One 2023;18(6):e0285385"),
               card("OR 3.0", "effect sustained at 8-month follow-up", "cyan",
                    "Pathare et al., PLoS One 2023;18(6):e0285385")], cols=2),
        tw(pp("cyan", "How it was measured", "1,191 participants, 85% followed up at 3 months. "
              "Outcomes used the GHQ-12, PHQ-9, GAD-7 and SRQ-20, quality of life, disability "
              "and social participation."),
           pp("green", "Why it is relevant", "Atmiyata links mental health with welfare "
              "entitlements, so it works through the same village structures that livelihoods "
              "and social protection programmes use.")),
    ], compact=True),

    C("Comparison", "Six task-sharing models compared", [
        table(["Model", "Where", "Who delivers", "Main finding"], [
            ["Thinking Healthy", "Rawalpindi, Pakistan", "Lady health workers",
             "Major depression 23% vs 53% at 6 months"],
            ["HAP (PREMIUM)", "Goa, India", "Lay counsellors", "Remission 64% vs 39% at 3 months"],
            ["CAP (PREMIUM)", "Goa, India", "Lay counsellors", "Harmful drinking in men; published 2017"],
            ["PM+", "Peshawar, Pakistan", "Lay health workers", "Lower anxiety and depression at 3 months"],
            ["Friendship Bench", "Harare, Zimbabwe", "Lay health workers",
             "Depression symptoms 13.7% vs 49.9%"],
            ["Atmiyata", "Mehsana, Gujarat", "Village volunteers", "OR 2.2 for recovery at 3 months"],
        ]),
        body("All six were tested against a comparison group, used a structured manual and "
             "supervised their workers. None replaced specialists: each kept a route to "
             "psychiatric care for people who needed it. The differences in outcome measures "
             "mean the effect sizes cannot be ranked against one another.", sm=True),
        hbox("Before adopting a model, check that your setting has what the trial had: "
             "supervisors, time in workers' schedules, and a referral destination.", "amber"),
    ], compact=True),

    C("Scaling up", "From trial to routine service", [
        body("A trial shows what works under supervision and with research funding. Routine "
             "services rarely have either. The Lancet Commission on global mental health and "
             "sustainable development (Patel et al., <em>Lancet</em> 2018;392:1553-98) argued for "
             "mental health as part of the SDGs and for task sharing at scale. The hard part is "
             "keeping quality when a programme grows."),
        tw([panel("cyan", "Questions before scaling", [bullets([
                "Who supervises counsellors after the research team leaves?",
                "Is counselling paid work, or added to an existing job?",
                "Which department owns it: health, women and child, or panchayat?",
                "How will fidelity be checked without recorded sessions?"], sm=True)])],
           [panel("green", "Signs a programme is ready", [bullets([
                "A government partner has a budget line for it",
                "Supervision is built into a public cadre's job description",
                "Referral to the DMHP has been tested in practice",
                "Outcomes are tracked with a validated measure"], sm=True)])]),
        hbox("Impact Evaluation 101 covers how to test a model again in a new setting before "
             "committing to scale.", "indigo"),
    ], compact=True),
]

# ===================== SECTION 09: SETTINGS =====================
S09 = [
    D("09", "Section Nine", "Children, work and emergencies"),

    C("Adolescents", "One in seven adolescents lives with a mental disorder", [
        stats([card("1 in 7", "10-19-year-olds worldwide with a mental disorder", "cyan",
                    "WHO fact sheet, Adolescent mental health (2025)"),
               card("7.3%", "Indian adolescents aged 13-17 with a mental disorder (subsample in four "
                    "states), higher in urban metros", "indigo", NMHS),
               card("3rd", "leading cause of death at ages 15-29: suicide", "red",
                    "WHO fact sheet, Adolescent mental health (2025)")], cols=3),
        body("WHO notes that adolescent mental health conditions account for 15% of the global "
             "burden of disease in this age group and remain largely unrecognised and untreated. "
             "It lists violence, especially sexual violence and bullying, harsh parenting and "
             "severe socio-economic problems among the risks. NMHS found current anxiety "
             "disorders in 3.6% and depressive disorders in 0.8% of Indian adolescents."),
        tw(pp("cyan", "Protective factors", "Good sleep, exercise, problem-solving and "
              "interpersonal skills, and supportive families, schools and communities (WHO)."),
           pp("amber", "Examination pressure", "NCRB recorded failure in examination as one of "
              "the main causes of suicide among children under 18 in 2024, alongside family "
              "problems, love affairs and illness.")),
    ], compact=True),

    C("Children", "What child and adolescent programmes can do", [
        body("Most of what protects young people's mental health lies outside clinics. WHO's "
             "2026 fact sheet names laws and policies, support for caregivers, school "
             "programmes and safer community and online settings. Section 18(4)(e) of the "
             "Mental Healthcare Act requires child mental health services, and Section 87 "
             "restricts admission of a minor to a mental health establishment."),
        table(["Setting", "What to add", "Evidence or authority"], [
            ["Early childhood", "Caregiver support; screening mothers for depression",
             "Thinking Healthy (Rahman et al., 2008)"],
            ["School", "Social and emotional learning; a counsellor; referral route",
             "WHO fact sheet 2026; Sukdeb Saha (2025)"],
            ["Coaching centres and hostels", "No public ranking; helplines displayed",
             "Sukdeb Saha (2025)"],
            ["Child protection", "Mental health support for children in care or after abuse",
             "WHO fact sheet 2026"],
            ["Online", "Safe reporting of suicide; moderation of harmful content",
             "WHO media guidance 2023"],
        ]),
        hbox("Child Rights 101 and SEL Basics 101 cover the legal and classroom sides in "
             "detail.", "green"),
    ], compact=True),

    C("Work", "Decent work protects mental health, poor work harms it", [
        stats([card("12 billion", "working days lost each year to depression and anxiety", "red",
                    "WHO fact sheet, Mental health at work (updated 15 September 2026)"),
               card("US$ 1 trillion", "a year in lost productivity", "amber",
                    "WHO fact sheet, Mental health at work (updated 15 September 2026)"),
               card("16%", "working-age adults estimated to have a mental disorder in 2023",
                    "indigo", "WHO fact sheet, Mental health at work (updated 15 September 2026)")], cols=3),
        body("WHO lists risks at work including excessive workloads, long or inflexible hours, "
             "low control over one's work, job insecurity, inadequate pay, discrimination, and "
             "violence, harassment or bullying. Its guidelines on mental health at work recommend "
             "organisational interventions, manager training, worker training, support to return "
             "to work and help in gaining employment."),
        tw(pp("cyan", "Informal work", "Most South Asian workers have no employer policy at all. "
              "For daily wage earners, 31% of recorded suicides in India in 2024, mental health "
              "at work means timely wages, safe conditions and freedom from harassment."),
           pp("green", "Indian law to use", "The four Labour Codes in force since 21 November "
              "2025 and the Sexual Harassment of Women at Workplace Act, 2013 set duties that "
              "bear on psychosocial risks. Work, Labour &amp; Livelihoods 101 covers them.")),
    ], compact=True),

    C("Practitioner wellbeing", "Staff who work with distress need care too", [
        body("Field staff hear disclosures of violence, debt and grief, and counsellors carry "
             "suicide risk. WHO's 2023 media guidance recognises that professionals covering "
             "suicide may themselves be affected, and the same holds for programme staff. "
             "Organisations owe staff the protections they promote for others."),
        tw([panel("amber", "Warning signs in a team", [bullets([
                "Cynicism about participants and the work",
                "Rising sick leave and turnover",
                "Staff avoiding difficult visits",
                "Irritability, poor sleep, more alcohol use"], sm=True)])],
           [panel("green", "What an organisation can do", [bullets([
                "Regular supervision that includes the worker's own reactions",
                "Caseload limits for counsellors and outreach workers",
                "Paid leave after a critical incident",
                "Confidential access to counselling, including Tele-MANAS"], sm=True)])]),
        hbox("WHO's guidance recommends manager training so that supervisors can recognise "
             "distress in the people they supervise and respond. Start there.", "indigo"),
    ]),

    C("Emergencies", "Emergencies: distress is common, disorder is not", [
        body("WHO's fact sheet on mental health in emergencies says almost everyone affected by "
             "an emergency experiences psychological distress, which usually improves over time. "
             "One in five people (22%) who experienced war or conflict in the previous ten years "
             "has depression, anxiety, post-traumatic stress disorder, bipolar disorder or "
             "schizophrenia. People with severe conditions are especially vulnerable when "
             "services break down."),
        tw(pp("cyan", "IASC guidelines (2007)", "The Inter-Agency Standing Committee Guidelines on "
              "Mental Health and Psychosocial Support in Emergency Settings give action sheets "
              "for coordination, assessment, protection, health services, education, food, "
              "shelter and water."),
           pp("green", "India's guidelines (2009)", "The National Disaster Management Authority "
              "issued National Disaster Management Guidelines on Psycho-Social Support and Mental "
              "Health Services in Disasters in December 2009.")),
        body("WHO co-chairs the IASC MHPSS Reference Group, which supports technical working "
             "groups in more than 55 countries.", sm=True),
        hbox("In emergencies, do not start by counselling everyone. Restore safety, basic "
             "services and community supports first; most people recover with those.", "amber"),
    ]),

    C("The pyramid", "The IASC intervention pyramid: four layers at once", [
        body("The IASC guidelines arrange support as a pyramid. Everyone needs the base; fewer "
             "people need each layer above it. WHO's Kobe centre stresses that all four "
             "complementary layers should be available at the same time."),
        table(["Layer", "What it involves", "Example"], [
            ["4. Specialised services", "Mental health care by specialists",
             "Psychiatrist treats psychosis after a cyclone"],
            ["3. Focused non-specialised supports", "Basic mental health care by primary care "
             "doctors; emotional and practical support by community workers",
             "Trained ASHA runs PM+ sessions"],
            ["2. Community and family supports", "Activating social networks, traditional "
             "supports, child-friendly spaces", "Women's groups restart weekly meetings"],
            ["1. Basic services and security", "Basic services delivered safely and in ways that "
             "protect dignity", "Fair, transparent food distribution"],
        ]),
        tw(pp("cyan", "Psychological first aid", "WHO's 2011 field guide describes humane, "
              "supportive and practical help built on three action principles: look, listen and "
              "link. Any helper can use it, with or without clinical training."),
           pp("amber", "Do no harm", "Avoid one-off debriefing sessions, labelling people as "
              "traumatised, and collecting stories you cannot follow up.")),
        body("Sources: IASC guidance note (2012) citing the 2007 Guidelines; WHO, Psychological "
             "first aid: guide for field workers (2011).", sm=True),
    ], compact=True),

    C("Psychological first aid", "Psychological first aid: look, listen and link", [
        body("WHO, War Trauma Foundation and World Vision International published "
             "<em>Psychological first aid: guide for field workers</em> on 2 October 2011. It "
             "describes humane, supportive and practical help for people who have just been "
             "through a seriously distressing event, in ways that respect their dignity, culture "
             "and abilities. Hindi, Sinhala, Tamil and Urdu are among its language versions."),
        flow(["LOOK: check safety, people with urgent basic needs, and people in serious "
              "distress",
              "LISTEN: approach, ask about needs and concerns, listen and help people feel calm",
              "LINK: help people meet basic needs, get information and connect with loved ones "
              "and services"]),
        tw(pp("green", "Who can give it", "Any helper who has had a short orientation: teachers, "
              "volunteers, panchayat members, relief staff. The fact sheet on emergencies "
              "recommends orienting frontline workers in it."),
           pp("amber", "What it avoids", "Pressing people to tell their story, giving false "
              "promises, and acting as a therapist. People who need more are linked to "
              "focused or specialised care in the upper layers of the pyramid.")),
        body("The three action principles are named in the guide (WHO, 2011). The descriptions "
             "in each step are our summary.", sm=True),
    ], compact=True),
]

# ===================== SECTION 10: MEASUREMENT AND ETHICS =====================
S10 = [
    D("10", "Section Ten", "Measuring mental health, and researching it ethically"),

    C("PHQ-9", "The PHQ-9 scores depression in nine questions", [
        body("The Patient Health Questionnaire-9 asks how often in the past two weeks a person "
             "has been bothered by each of the nine criteria for major depression, scored 0 (not "
             "at all) to 3 (nearly every day). Kroenke, Spitzer and Williams validated it with "
             "6,000 patients in US primary care and obstetrics clinics (<em>J Gen Intern Med</em>, "
             "2001)."),
        table(["PHQ-9 score", "Severity band (Kroenke et al., 2001)"], [
            ["5-9", "Mild"],
            ["10-14", "Moderate"],
            ["15-19", "Moderately severe"],
            ["20-27", "Severe"],
        ]),
        tw(pp("cyan", "Accuracy in the original study", "A score of 10 or more had 88% sensitivity "
              "and 88% specificity for major depression against a mental health professional's "
              "interview."),
           pp("red", "Item 9 needs a protocol", "The ninth item asks about thoughts of being "
              "better off dead or of self-harm. Any positive answer needs an immediate, "
              "pre-agreed response by the interviewer. Never collect it without one.")),
        hbox("HAP in Goa used PHQ-9 above 14 to enrol people with moderately severe to severe "
             "depression and below 10 to define remission.", "indigo"),
    ], compact=True),

    C("GAD-7 and SRQ-20", "Two more tools: the GAD-7 and the SRQ-20", [
        tw([panel("cyan", "GAD-7", [body(
                "Spitzer and colleagues developed this seven-item anxiety scale in 15 US primary "
                "care clinics (<em>Arch Intern Med</em>, 2006). At the chosen cut point it had 89% "
                "sensitivity and 82% specificity for generalised anxiety disorder. A later "
                "systematic review (Kroenke et al., 2010) gives 10 as the optimal cut point and "
                "5, 10 and 15 as mild, moderate and severe.", sm=True)])],
           [panel("green", "SRQ-20", [body(
                "WHO's Self-Reporting Questionnaire has 20 questions answered yes or no, and can "
                "be self-administered or read out by an interviewer. WHO's user's guide, compiled "
                "by M. Beusenberg and J. Orley (Geneva, 1994), reviews studies using it. Its "
                "yes/no format suits low-literacy settings.", sm=True)])]),
        body("Each tool has a job. The PHQ-9 tracks depression severity over time, the GAD-7 does "
             "the same for anxiety, and the SRQ-20 screens for common mental disorders more "
             "broadly. Atmiyata in Gujarat used all three together with the GHQ-12."),
        hbox("A screening score is a flag, never a diagnosis. Say \"screened positive\" in reports, "
             "and \"has depression\" only after a clinical assessment.", "amber"),
    ], compact=True),

    C("Validation", "A tool is only as good as its validation in your language", [
        body("A questionnaire translated word for word can miss how distress is expressed locally, "
             "for example as tiredness, body aches or \"tension\". Validation compares the tool "
             "against a diagnostic interview in the same population. Two Indian studies show why "
             "this matters."),
        tw(pp("cyan", "Goa, 2008", "Patel and colleagues compared five questionnaires (GHQ-12, "
              "PHQ-9, K10, K6 and SRQ-20) against a structured lay diagnostic interview with 598 "
              "primary care attenders (<em>Psychol Med</em> 2008;38:221-8). All discriminated "
              "moderately to well, but positive predictive values were only 51% to 77% at the "
              "best cut-offs, so cut-offs should be set for each setting."),
           pp("green", "Kangra, 2026", "Fellmeth and colleagues adapted six measures into Hindi "
              "and tested them with 480 perinatal and non-perinatal women in rural Himachal "
              "Pradesh (<em>BMJ Open</em> 2026;16:e111111). Among non-perinatal women the PHQ-9 "
              "Hindi had an AUROC of 0.91. Tiredness and body weakness were the most endorsed "
              "symptoms.")),
        hbox("Before using any scale, search for a validation in your language and population. "
             "If none exists, say so in the report and treat cut-offs as provisional.", "amber"),
    ], compact=True),

    C("Local idioms", "Listening for how people describe distress", [
        body("Scales count symptoms that clinicians defined. People describe distress in their "
             "own words, often through the body. The Kangra study (Fellmeth et al., 2026) found "
             "tiredness and body weakness were the symptoms most endorsed by women with common "
             "mental disorders, and concluded that measures asking about fatigue and somatic "
             "symptoms may help identify them in that setting."),
        tw([panel("cyan", "Qualitative work before the survey", [bullets([
                "Free-listing: ask people to name kinds of worry and illness",
                "Key informant interviews with ASHAs, healers and teachers",
                "Cognitive interviewing to test each translated item",
                "Check whether \"tension\" or a local word carries the meaning"], sm=True)])],
           [panel("green", "Why it matters for programmes", [bullets([
                "A scale in the wrong words under-counts need",
                "Local terms make awareness material understood",
                "Respecting local explanations builds trust for referral",
                "It shows where faith healers are the first contact"], sm=True)])]),
        hbox("Qualitative Methods 101 and Mixed Methods 101 show how to run this groundwork "
             "and combine it with a validated scale.", "indigo"),
    ], compact=True),

    C("Indicators", "Choosing indicators for a mental health component", [
        body("Programmes often report the number of people trained or sessions held. Those are "
             "outputs. The table suggests indicators at each level, all of which can be "
             "disaggregated by sex, age, caste and disability. The examples are a teaching "
             "summary, drawn from the tools and trials in this deck."),
        table(["Level", "Indicator", "Source"], [
            ["Outcome", "Mean change in PHQ-9 or GAD-7 score at 3 months",
             "Validated tool, local language"],
            ["Outcome", "Share in remission (PHQ-9 below 10)", "As used in HAP"],
            ["Outcome", "Functioning or disability score", "WHODAS 2.0, as in PM+"],
            ["Output", "People referred who reached a service within 30 days", "Referral register"],
            ["Process", "Counsellor sessions reviewed in supervision", "Supervision log"],
            ["Equity", "Coverage of people screened positive, by social group", "Programme MIS"],
        ]),
        hbox("Measure functioning as well as symptoms. People judge recovery by whether they can "
             "work, care and take part again.", "green"),
    ], compact=True),

    C("Research ethics", "ICMR's guidelines treat mental illness as a vulnerability that needs safeguards", [
        body("The ICMR National Ethical Guidelines for Biomedical and Health Research Involving "
             "Human Participants (October 2017) list people with mental illness among vulnerable "
             "groups needing additional safeguards set by the ethics committee. They are equally "
             "clear that vulnerable groups have a right to be included, so that research benefits "
             "reach them."),
        quote("Presence of a mental disorder is not synonymous with incapacity of understanding "
              "or inability to provide informed consent.", "ICMR National Ethical Guidelines, "
              "2017, section 6.8"),
        tw(pp("cyan", "Section 6.8.1", "During consent, prospective participants must be told how "
              "the researcher will respond to suicidal ideation or other risks of harm to "
              "themselves or others."),
           pp("green", "Together with the MHCA", "Section 99 of the Mental Healthcare Act requires "
              "free and informed consent, State Authority permission where a person cannot "
              "consent, and the right to withdraw at any time.")),
    ]),

    C("A distress protocol", "What enumerators must do when a respondent is at risk", [
        body("Any survey that asks about mood, violence or suicidal thoughts will meet people in "
             "distress. A distress protocol, agreed with the ethics committee before fieldwork, "
             "tells enumerators exactly what to do. It protects the respondent and the "
             "enumerator."),
        flow(["Pause the interview and acknowledge what was said",
              "Ask directly and calmly about immediate safety",
              "Offer Tele-MANAS (14416) and a named local service",
              "If risk is immediate, stay with the person and contact the supervisor",
              "Supervisor arranges referral and records it without identifying details",
              "Debrief the enumerator the same day"]),
        tw(pp("amber", "Prepare in advance", "Map services in each district, train enumerators "
              "with role-play, and give each team a supervisor reachable by phone."),
           pp("cyan", "Asking does not cause harm", "WHO's media guidance lists as a myth the belief "
              "that talking about suicide is a bad idea and can be read as encouragement. Its "
              "answer: talking openly can give a person other options or the time to rethink.")),
    ], compact=True),

    C("Data protection", "Mental health data are among the most sensitive a programme holds", [
        body("A leaked list of people who screened positive for depression can cost someone a "
             "marriage or a job. The Mental Healthcare Act already gives a right to "
             "confidentiality (section 23). The Digital Personal Data Protection Act, 2023 "
             "commences in stages under G.S.R. 843(E) of 13 November 2025: its core duties, "
             "rights and exemptions (sections 3-17) and penalties apply only from 13 May 2027. "
             "Treat them now as the standard to prepare for."),
        tw([panel("cyan", "Rules of thumb", [bullets([
                "Collect only what the analysis needs",
                "Separate names from responses at the point of collection",
                "Encrypt devices; restrict access to named staff",
                "Never share lists of individuals with officials without consent"], sm=True)])],
           [panel("amber", "The research exemption, from 13 May 2027", [bullets([
                "DPDP s17(2)(b) will exempt processing for research, archiving or statistics",
                "Only if the conditions in the Act and the 2025 Rules are met",
                "It is not in force before 13 May 2027",
                "Ethics review and consent duties under ICMR and MHCA s99 apply now"],
                sm=True)])]),
        hbox("Data Protection &amp; the DPDP Act 101 explains the exemption's conditions in "
             "detail.", "indigo"),
    ], compact=True),
]

# ===================== SECTION 11: PRACTITIONER TOOLKIT =====================
S11 = [
    D("11", "Section Eleven", "A practitioner's toolkit"),

    C("Integrating MHPSS", "Adding mental health and psychosocial support to a programme", [
        body("Most development practitioners will not run a mental health programme. They will "
             "add mental health and psychosocial support (MHPSS) to a livelihoods, education, "
             "health or protection programme. The steps below adapt the IASC pyramid and the "
             "task-sharing evidence to that situation."),
        flow(["Map: which services exist in the district, and do they work?",
              "Protect: check that the core programme does not add stress (late payments, public "
              "shaming)",
              "Train: teach staff to notice distress, respond and refer",
              "Link: agree a referral route with the DMHP and Tele-MANAS",
              "Add: a structured intervention (PM+, HAP) only if supervision exists",
              "Monitor: referrals completed, outcomes, and harms"]),
        tw(pp("green", "Start small", "A one-day training and a tested referral route help more "
              "people than an ambitious counselling component that collapses when funding ends."),
           pp("amber", "Budget in full", "Supervision, staff care and travel support for "
              "referrals cost money. Put them in the budget from the start.")),
    ], compact=True),

    C("Referral pathway", "Building a referral pathway that people actually complete", [
        body("A referral pathway is a written agreement on who refers whom, to which service, "
             "with what information, and how the outcome comes back. Without one, staff either "
             "refer nobody or refer people to services that do not answer."),
        table(["Element", "What to write down"], [
            ["Services", "Name, address, days and hours, phone, languages, cost"],
            ["Criteria", "What kind of need goes to which service"],
            ["Consent", "How the person agrees to the referral and what is shared"],
            ["Urgent route", "What to do for immediate risk, any hour"],
            ["Follow-up", "Who checks within a week that the person reached the service"],
            ["Review", "Test every number each quarter; update the sheet"],
        ]),
        tw(pp("cyan", "Test it", "Before launch, a staff member calls each service and visits the "
              "nearest one. Record what actually happened."),
           pp("green", "Accompany", "For a first visit, offer someone to go along. Travel cost and "
              "fear of being seen are the two most common reasons people do not arrive.")),
    ], compact=True),

    C("Safe messaging", "Talking and writing about suicide safely", [
        body("Programme newsletters, social media posts, case studies and donor reports all "
             "count as public communication. WHO's <em>Preventing suicide: a resource for media "
             "professionals</em> (update 2023) gives a short list of dos and don'ts that apply "
             "to them."),
        tw([panel("green", "Do", [bullets([
                "Give accurate information on where and how to seek help",
                "Share stories of coping and recovery",
                "Educate with facts about suicide and its prevention",
                "Take care when speaking with bereaved families",
                "Recognise that writers may themselves be affected"], sm=True)])],
           [panel("red", "Don't", [bullets([
                "Use sensational language in headlines",
                "Describe the method or name the location",
                "Report details of notes",
                "Reduce a death to a single cause",
                "Use photographs, video or social media links of the person"], sm=True)])]),
        hbox("WHO reports that widely shared stories of a suicide are often followed by more "
             "suicides, while stories of overcoming a crisis can lead to fewer. Lead with the "
             "second kind.", "indigo"),
    ], compact=True),

    C("Decision table", "What to do when a participant is in distress", [
        body("Field staff need clear rules. This decision table is a teaching tool to adapt with "
             "a local mental health professional and the referral pathway; it is not a clinical "
             "protocol."),
        table(["What you notice", "What you do", "Who acts"], [
            ["Worry or low mood that does not stop daily life",
             "Listen, normalise, share Tele-MANAS and self-help options", "Any trained staff"],
            ["Low mood or anxiety for two weeks or more, affecting work or care",
             "Offer referral to the Ayushman Arogya Mandir or DMHP; follow up in a week",
             "Field staff with supervisor"],
            ["Talk of hopelessness or of not wanting to live",
             "Ask directly about suicidal thoughts; make a safety plan; same-day referral",
             "Supervisor or counsellor"],
            ["Immediate risk to life", "Stay with the person, call 112 or the nearest hospital "
             "and Tele-MANAS; do not leave them alone", "Whoever is present"],
            ["Signs of psychosis, mania or confusion", "Do not argue; ensure safety; arrange "
             "medical assessment", "Supervisor with family"],
            ["Disclosure of violence", "Safety first; refer to One Stop Centre or protection "
             "services; offer mental health support", "Trained staff"],
        ]),
    ], compact=True),

    C("Illustrative case, part 1", "Illustrative case: a self-help group member under debt pressure", [
        hbox("Illustrative. This case is invented for teaching and combines common patterns. It "
             "describes no real person.", "amber"),
        body("Sunita, 34, belongs to a women's self-help group run by a livelihoods programme in "
             "a district of Vidarbha. Her husband, a cultivator, has lost two cotton crops. The "
             "family owes money to a moneylender and to the group. At the monthly meeting she "
             "says little, has missed two repayments, and tells the community resource person "
             "that she cannot sleep and feels the family would be better off without her."),
        tw([panel("cyan", "What the worker did well", [bullets([
                "Spoke to her privately after the meeting",
                "Asked directly whether she had thoughts of ending her life",
                "Did not promise to keep a risk to life secret",
                "Called the supervisor the same day"], sm=True)])],
           [panel("red", "What the programme had got wrong", [bullets([
                "Repayments were collected in public, with names read out",
                "No rescheduling option existed",
                "Staff had no referral sheet",
                "The nearest DMHP clinic day was unknown"], sm=True)])]),
        body("The case shows how the core programme can add stress, and how one trained worker "
             "made the difference.", sm=True),
    ], compact=True),

    C("Illustrative case, part 2", "Illustrative case: what happened next", [
        flow(["Same day: supervisor visits with the worker; a simple safety plan is agreed with "
              "Sunita and her sister",
              "Next day: call to Tele-MANAS with Sunita's consent; counsellor arranges a "
              "psychiatric review",
              "Week 1: accompanied visit to the DMHP clinic; follow-up date set",
              "Week 2: group agrees a repayment holiday; crop insurance claim is filed",
              "Month 3: PHQ-9 repeated by the counsellor; Sunita back at meetings"]),
        tw(pp("green", "Programme changes that followed", "Repayments were made private, a "
              "hardship rescheduling rule was added, every staff member received a referral "
              "sheet, and two staff per block were trained in PM+ with DMHP supervision."),
           pp("indigo", "What made it work", "A trained first responder, a tested route to care, "
              "a supervisor who acted the same day, and the programme's willingness to change "
              "its own rules.")),
        hbox("Illustrative. In real cases, record only what the person agrees to, store it "
             "securely, and share it only with those who need it to help.", "amber"),
    ], compact=True),

    C("Training plan", "A one-day orientation for field staff", [
        hbox("Illustrative. A sample agenda for adaptation with a local mental health "
             "professional; it is not a certified curriculum.", "amber"),
        table(["Session", "Content", "Method"], [
            ["1. What mental health is", "WHO definition, continuum, common conditions in "
             "plain words", "Discussion of staff's own words for distress"],
            ["2. Noticing", "Changes in mood, sleep, work, withdrawal; local idioms",
             "Case vignettes"],
            ["3. Responding", "Listening, asking directly about suicidal thoughts, safety "
             "planning", "Role-play in pairs with feedback"],
            ["4. Referring", "The pathway sheet, Tele-MANAS 14416, consent, follow-up",
             "Practice call to a service"],
            ["5. Doing no harm", "Confidentiality, safe messaging, the programme's own "
             "stressors", "Review of a real programme process"],
            ["6. Looking after yourself", "Supervision, warning signs, where staff can get help",
             "Group discussion"],
        ]),
        body("Follow the day with monthly supervision, where staff bring cases and their own "
             "reactions. Training without supervision fades within weeks; the task-sharing "
             "trials in Section 08 all paired the two.", sm=True),
    ], compact=True),

    C("Checklist", "A checklist before you launch a mental health component", [
        tw([panel("cyan", "Design", [bullets([
                "Services in the district mapped and tested",
                "Referral pathway written and agreed",
                "Core programme checked for added stress",
                "People with lived experience involved in design",
                "Budget covers supervision and staff care"], sm=True)])],
           [panel("green", "Delivery and data", [bullets([
                "All staff trained to notice, respond and refer",
                "Distress protocol approved by an ethics committee",
                "Validated tools in the local language",
                "Data minimised, encrypted, access restricted",
                "Safe messaging rules for all communication"], sm=True)])]),
        body("Check the law in your country: the MHCA and BNS in India, and the changing "
             "positions in Bangladesh, Pakistan, Nepal and Sri Lanka summarised in Section 07. "
             "Check the time-sensitive facts too: NMHS-2, Tele-MANAS coverage, and Pakistan's "
             "pending appeal were all moving as of October 2026."),
        hbox("If you can tick only three boxes, make them the referral pathway, staff training "
             "and the distress protocol.", "amber"),
    ], compact=True),
]

# ===================== SECTION 12: SUMMING UP =====================
S12 = [
    D("12", "Section Twelve", "Summing up and where next"),

    C("Summary", "Eight points to carry into practice", [
        tw([panel("cyan", "On the problem", [bullets([
                "Mental health is well-being, and disorders sit on a continuum with it",
                "India: 10.6% of adults with a current disorder, 70-92% untreated (NMHS 2015-16)",
                "1,70,746 recorded suicides in 2024, an undercount (NCRB)",
                "Poverty, debt, caste and gender all shape risk"], sm=True)])],
           [panel("green", "On the response", [bullets([
                "MHCA 2017 makes care a right (s18) and attempted suicide a matter for care (s115)",
                "Tele-MANAS 14416, DMHP and the NSPS are the public routes",
                "Trained lay workers with supervision can halve depression",
                "Every programme can notice, respond, refer and avoid harm"], sm=True)])]),
        body("The common thread across the deck is the gap between effective care and the people "
             "who need it. Most of that gap sits outside hospitals, in villages, schools, "
             "workplaces and camps where development programmes already work. " + HELP),
    ]),

    C("Where next", "Where next: related 101 decks", [
        tw([panel("cyan", "Health and people", [body(
                "<a href=\"/101-courses/pub-health-basics.html\">Public Health 101</a> for "
                "health systems and primary care. "
                "<a href=\"/101-courses/social-determinants-health.html\">Social Determinants of "
                "Health 101</a> for the causes behind the causes. "
                "<a href=\"/101-courses/maternal-health.html\">Maternal Health 101</a> for "
                "perinatal care. "
                "<a href=\"/101-courses/child-rights.html\">Child Rights 101</a> and "
                "<a href=\"/101-courses/sel-basics.html\">SEL Basics 101</a> for children and "
                "schools. "
                "<a href=\"/101-courses/disability-inclusion.html\">Disability Inclusion 101</a> "
                "for psychosocial disability.", sm=True)])],
           [panel("green", "Methods and practice", [body(
                "<a href=\"/101-courses/survey-design.html\">Survey Design 101</a> for "
                "questionnaires and validation. "
                "<a href=\"/101-courses/research-ethics.html\">Research Ethics 101</a> for consent "
                "and distress protocols. "
                "<a href=\"/101-courses/impact-eval.html\">Impact Evaluation 101</a> for testing "
                "interventions. "
                "<a href=\"/101-courses/safeguarding-psea.html\">Safeguarding &amp; PSEA 101</a> "
                "and <a href=\"/101-courses/data-protection-dpdp.html\">Data Protection &amp; the "
                "DPDP Act 101</a> for protecting participants. "
                "<a href=\"/101-courses/caste-studies.html\">Caste Studies 101</a> and "
                "<a href=\"/101-courses/gender-dev.html\">Gender &amp; Development 101</a> for "
                "the determinants.", sm=True)])]),
        hbox("Suggested order: Public Health, then Social Determinants of Health, then Research "
             "Ethics before any fieldwork that asks about mood or suicide.", "indigo"),
    ], compact=True),
]

TITLE = {"type": "title",
         "main": "Mental<br>Health<br>101",
         "sub": "What mental health and mental disorders are, how large the burden is, what the "
                "law says and what works: the Mental Healthcare Act, Tele-MANAS, task sharing, "
                "suicide prevention and practical tools for practitioners in South Asia",
         "tags": ["100 Slides", "South Asia Focus", "Free Forever", "Care in Community"]}

TOC = {"type": "toc", "label": "Agenda", "title": "What we cover",
       "items": [
           {"name": "What mental health is, and what a disorder is"},
           {"name": "How large the burden is"},
           {"name": "Suicide: what the numbers show and what they miss"},
           {"name": "Social determinants: poverty, debt, caste, gender and stigma"},
           {"name": "The law in India: the Mental Healthcare Act and the BNS"},
           {"name": "India's programmes: from 1982 to Tele-MANAS"},
           {"name": "Law and programmes across South Asia"},
           {"name": "Task sharing: the evidence from South Asia and beyond"},
           {"name": "Children, work and emergencies"},
           {"name": "Measuring mental health, and researching it ethically"},
           {"name": "A practitioner's toolkit"},
           {"name": "Summing up and where next"},
       ]}

END = {"type": "end",
       "eyebrow": "Mental Health 101",
       "headline": "Notice, respond, refer, and change what causes harm",
       "byline": "ImpactMojo 101 Series &middot; Free foundational learning for development "
                 "practitioners in South Asia &middot; Tele-MANAS 14416",
       "ctas": [{"label": "Public Health 101", "href": "/101-courses/pub-health-basics.html"},
                {"label": "All 101 courses", "href": "/101-courses/"}],
       "meta": ["100 slides", "12 sections", "CC BY-NC-ND"]}

DECK = {
    "slug": "mental-health",
    "title": "Mental Health 101",
    "description": ("Mental Health 101: a free foundational course for development practitioners "
                    "in South Asia. WHO definitions and ICD-11, the burden from WHO, GBD India and "
                    "the National Mental Health Survey, suicide and the NCRB data, social "
                    "determinants and stigma, the Mental Healthcare Act 2017 and the BNS, NMHP, "
                    "DMHP, Tele-MANAS and the National Suicide Prevention Strategy, law in "
                    "Bangladesh, Pakistan, Nepal and Sri Lanka, task sharing (Thinking Healthy, "
                    "HAP, PM+, Friendship Bench, Atmiyata), children, work and emergencies, "
                    "PHQ-9, GAD-7 and SRQ-20, research ethics, and a practitioner's toolkit. "
                    "ImpactMojo, CC BY-NC-ND."),
    "slides": ([TITLE, TOC] + S01 + S02 + S03 + S04 + S05 + S06 + S07 + S08 + S09 + S10 + S11
               + S12 + [END]),
}
