# -*- coding: utf-8 -*-
"""
Disaster Risk and Heat Resilience 101 -- ImpactMojo 101 Series (native deck spec)
Hazard, exposure and vulnerability; the Sendai Framework; India's Disaster Management Act 2005
and the 2025 amendment; the response and mitigation funds and the Finance Commissions;
cyclones and Odisha's record; floods, landslides, lightning and drought; heat; early warning
and anticipatory action; relief, recovery and the people relief misses; insurance and social
protection in a shock; monitoring and evaluating preparedness.
Build: python3 scripts/deck-builder/build.py disaster_heat

House style: no em dashes, sentence-case headings, every statistic sourced on the slide,
every law cited by Act, year and section, teaching examples labelled Illustrative.

Sources opened while writing (October 2026):
- UNDRR, What is the Sendai Framework: https://www.undrr.org/implementing-sendai-framework/what-sendai-framework
- Sendai Framework text: https://www.undrr.org/media/16176/download
- Disaster Management Act 2005 (NIDM copy): https://nidm.gov.in/PDF/En_DM_act2005.pdf
- Disaster Management (Amendment) Act 2025, Gazette of 29 March 2025:
  https://www.thc.nic.in/Central%20Governmental%20Acts/Disaster%20Management%20Act,%202005.pdf
- PRS Bill track: https://prsindia.org/billtrack/the-disaster-management-amendment-bill-2024
- Sixteenth Finance Commission Report, Vol I, ch 11: https://www.indiabudget.gov.in/doc/16fcvol1.pdf
- Economic Survey 2021-22, para 2.35: https://www.indiabudget.gov.in/economicsurvey/ebook_es2022/files/basic-html/page90.html
- Cyclone Fani DLNA (Govt of Odisha, 2019): https://www.osdma.org/wp-content/uploads/2019/08/Cyclone-Fani-2019-Odisha-DLNA-Report.pdf
- IMD heat wave definitions: https://mausam.imd.gov.in/pdfs/heatcolduser/Definition.pdf
- Knowlton et al. 2014, IJERPH 11(4):3473: https://doi.org/10.3390/ijerph110403473
- Azhar et al. 2014, PLoS One 9(3):e91831: https://doi.org/10.1371/journal.pone.0091831
- Hess et al. 2018, J Environ Public Health 7973519: https://doi.org/10.1155/2018/7973519
- Sherwood and Huber 2010, PNAS 107(21):9552: https://doi.org/10.1073/pnas.0913352107
- Vecellio et al. 2022, J Appl Physiol 132(2):340: https://doi.org/10.1152/japplphysiol.00738.2021
- ILO 2019, Working on a Warmer Planet: https://www.ilo.org/sites/default/files/wcmsp5/groups/public/@dgreports/@dcomm/@publ/documents/publication/wcms_711919.pdf
- Pillai and Dalal 2023, CPR heat action plan assessment: https://cprindia.org/wp-content/uploads/2023/03/Heat-Report_27March-23_Updated-Table.pdf
- Human Rights Watch 2005, After the Deluge: https://www.hrw.org/reports/2005/india0505/india0505.pdf
- Pakistan Floods 2022 PDNA: https://www.pc.gov.pk/uploads/downloads/PDNA-2022.pdf
- VB-G RAM G Act 2025 (Act 36 of 2025): https://www.indiacode.nic.in/bitstream/123456789/22478/1/a2025-36.pdf
- SCC Online, 12 May 2026: https://www.scconline.com/blog/post/2026/05/12/vbgramg-act-implemented-from-1-july-2026/
- ThePrint, 7 August 2026: https://theprint.in/india/house-panel-recommends-record-rs-2-84-lakh-crore-disaster-fund-heatwaves-lightning-on-disaster-list/3008901/
"""


# ---------------------------------------------------------------------------
# Small helpers so the spec stays readable
# ---------------------------------------------------------------------------
def C(label, title, *blocks, **kw):
    d = {"type": "content", "label": label, "title": title, "blocks": list(blocks)}
    d.update(kw)
    return d


def D(num, label, title):
    return {"type": "divider", "num": num, "label": label, "title": title}


def B(html, sm=False):
    b = {"t": "body", "html": html}
    if sm:
        b["cls"] = "sm"
    return b


def H(color, html):
    return {"t": "hbox", "color": color, "html": html}


def P(color, title, html):
    return {"t": "panel", "color": color, "title": title, "blocks": [B(html, sm=True)]}


def TW(left, right, ratio="half"):
    return {"t": "twocol", "ratio": ratio, "left": left, "right": right}


def T(head, rows):
    return {"t": "table", "head": head, "rows": rows}


def BL(items, color="", sm=True):
    b = {"t": "bullets", "items": items}
    if color:
        b["color"] = color
    if sm:
        b["sm"] = True
    return b


def TERM(word, d):
    return {"t": "term", "word": word, "def": d}


def ST(cards, cols=None):
    return {"t": "stats", "cols": cols or len(cards), "cards": cards}


def CARD(num, label, color="cyan", source=None):
    c = {"num": num, "label": label, "color": color}
    if source:
        c["source"] = source
    return c


def FLOW(*steps):
    return {"t": "flow", "steps": list(steps)}


def Q(text, attr):
    return {"t": "quote", "text": text, "attr": attr}


def CH(canvas, ctype, title, source, data, options):
    return {"t": "chart", "canvas": canvas, "type": ctype, "title": title, "source": source,
            "data": data, "options": {"__js__": options}}


# Short source labels used on many slides
SENDAI = "Sendai Framework for Disaster Risk Reduction 2015-2030, UNDRR"
DMA = "Disaster Management Act 2005 (Act 53 of 2005)"
DMA25 = "Disaster Management (Amendment) Act 2025 (Act 10 of 2025), Gazette of India, 29 March 2025"
FC16 = "Report of the Sixteenth Finance Commission, Vol. I, ch. 11 (November 2025)"
FANI = "Government of Odisha, Cyclone Fani Damage, Loss and Needs Assessment (2019)"
IMD = "India Meteorological Department, heat wave and warm night definitions"
ILO = "ILO, Working on a Warmer Planet (2019), Table 6.2, Southern Asia, 1995 and 2030 (projections)"
CPR = "Pillai and Dalal, How is India Adapting to Heatwaves?, CPR (March 2023)"
HRW = "Human Rights Watch, After the Deluge: India's Reconstruction Following the 2004 Tsunami (May 2005)"
PDNA = "Government of Pakistan et al., Pakistan Floods 2022 Post-Disaster Needs Assessment"
VBG = "VB-G RAM G Act 2025 (Act 36 of 2025)"

SLIDES = []

# ===================== S1 TITLE, S2 TOC =====================
SLIDES += [
    {"type": "title",
     "main": "Disaster Risk and<br>Heat Resilience 101",
     "sub": "Hazard, exposure and vulnerability, the Sendai Framework, India's Disaster "
            "Management Act and its funds, cyclones, floods, drought and heat, early warning, "
            "relief and the people it misses, insurance and shock-responsive social protection",
     "tags": ["Disaster Risk", "Heat", "South Asia Focus", "100 Slides", "Free Access"]},

    {"type": "toc", "label": "Agenda", "title": "What we cover",
     "items": [
         {"name": "Hazard, exposure and vulnerability"},
         {"name": "The Sendai Framework 2015-2030"},
         {"name": "India's disaster law and institutions"},
         {"name": "Paying for disasters: the funds"},
         {"name": "Cyclones and Odisha's record"},
         {"name": "Floods, landslides and lightning"},
         {"name": "Drought"},
         {"name": "Heat"},
         {"name": "Early warning and anticipatory action"},
         {"name": "Relief, recovery and who relief misses"},
         {"name": "Insurance and social protection in a shock"},
         {"name": "Monitoring preparedness, and sources"},
     ]},
]

# ===================== SECTION 01: HAZARD, EXPOSURE, VULNERABILITY =====================
SLIDES += [
    D("01", "Section One", "Hazard, exposure and vulnerability"),

    C("Definition", "A disaster is what happens when a hazard meets people who cannot cope",
      TW([TERM("Disaster (DM Act 2005, s. 2(d))",
               "A catastrophe, mishap, calamity or grave occurrence arising from natural or man "
               "made causes, or by accident or negligence, which results in substantial loss of "
               "life or human suffering or damage to property or the environment, and is of such "
               "a nature or magnitude as to be beyond the coping capacity of the community of "
               "the affected area."),
          B("The last clause carries the idea that runs through this course. A cyclone over an "
            "empty sea is weather. The same cyclone over villages of thatched houses, with no "
            "shelter and no warning, is a disaster. The wind is the same in both cases. What "
            "differs is who is in its path and what they have to protect themselves with. The "
            "2025 amendment added an Explanation to s. 2(d) saying that man made causes do not "
            "include law and order situations.")],
         [B("Disaster risk practice therefore separates three things that are often run "
            "together in news reports and in project documents. The hazard is the physical "
            "event. Exposure is the people and assets in the place where it happens. "
            "Vulnerability is the set of conditions that decide how badly those people and "
            "assets are hurt. Each one can be changed by a different kind of action, and a "
            "programme that does not say which one it is working on usually cannot show that "
            "it worked."),
          H("amber", "Practitioners often call these natural disasters. The Act's definition, "
            "and this course, treat the hazard as natural and the disaster as the result of "
            "where people live, what they own and how they are governed.")])),

    C("The three parts", "The definitions now written into Indian law",
      T(["Term", "What the Act says (as amended in 2025)", "What changes it"],
        [["Hazard, s. 2(gc)", "A process or phenomenon relating to a disaster that may cause loss "
          "of life, injury or other health impacts, damage to property, social and economic "
          "disruption, or environmental degradation", "Mostly outside human control in the short "
          "run. Some hazards are made worse by people: deforestation and landslides, paved "
          "cities and flooding, emissions and heat."],
         ["Exposure, s. 2(gb)", "The situation of people, buildings, infrastructure, production "
          "capacities and other tangible assets, the environment and natural resources located "
          "in hazard-prone areas", "Land use rules, zoning, relocation, evacuation, where "
          "schools and hospitals are built"],
         ["Vulnerability, s. 2(w)", "Conditions determined by physical, social, economic and "
          "environmental factors or processes which increase the susceptibility of an "
          "individual, community, asset, infrastructure or system to the impact of hazard",
          "Housing quality, income, savings, health, caste and gender relations, access to "
          "information, social protection"],
         ["Disaster risk, s. 2(ea)", "Potential loss of life, injury, damage, disruption and "
          "degradation in a specific period, determined probabilistically as a function of "
          "hazard, exposure, vulnerability and capacity", "Reducing any of the first three, or "
          "raising capacity"],
         ["Resilience, s. 2(oc)", "The ability of a system, community or society exposed to "
          "hazards to resist, absorb, respond to and recover from the effects of a hazard in a "
          "timely and efficient manner", "Everything above, plus recovery systems"]]),
      B("Source: " + DMA25 + ", s. 2. These definitions were added in 2025. The 2005 Act had "
        "no definition of hazard, exposure, vulnerability or disaster risk.", sm=True),
      compact=True),

    C("The risk equation", "Why the three parts are multiplied, not added",
      TW([B("Risk analysts write disaster risk as a product: risk = hazard &times; exposure "
            "&times; vulnerability. The Sixteenth Finance Commission built its Disaster Risk "
            "Index for allocating money to States on exactly this rule, and explained why. "
            "Disaster risk only exists when hazard, exposure and vulnerability intersect. A "
            "severe hazard over an empty place carries no risk to people. A large, poor "
            "population in a place no hazard reaches carries none either."),
          B("The product form has a practical consequence. If any one term falls towards zero, "
            "risk falls towards zero, whatever the other two are doing. Moving a village out of "
            "a floodplain cuts exposure. Building a cyclone shelter and warning people in time "
            "cuts vulnerability for the hours that matter. Neither changes the hazard."),
          B("Source: " + FC16 + ", paras 11.48 to 11.51.", sm=True)],
         [T(["Term in the FC-16 index", "Measured by"],
            [["Hazard", "Ten disasters scored by quintile from IMD, CWC, GSI, NCS, BIS and "
              "Agriculture Ministry data: flood, drought, cyclone, earthquake, landslide, "
              "hailstorm, cold wave, cloudburst, lightning, heatwave"],
             ["Exposure", "Projected State population, October 2026"],
             ["Vulnerability", "State per-capita income, average of 2018-19 to 2023-24, "
              "leaving out 2020-21"],
             ["Weighting", "Hazard scores weighted by each disaster's share of past "
              "expenditure; index then multiplied out"]]),
          H("cyan", "A State-level index uses income as its vulnerability measure because it is "
            "available for every State. Inside a district, a programme needs finer measures: "
            "housing material, who has a phone, who cannot walk to a shelter.")])),

    C("Illustration", "Two villages, one cyclone",
      TW([P("cyan", "Village A (Illustrative)",
            "Pucca houses, a multipurpose cyclone shelter 800 metres away, a trained village "
            "task force, a siren tower, a fair price shop stocked before landfall, and fishing "
            "boats hauled up two days earlier on official advice. Most families have a mobile "
            "phone and received the warning in Odia. The same wind blows the roofs off two cattle "
            "sheds and floods the fields for a week."),
          P("red", "Village B (Illustrative)",
            "Kutcha houses on a low sandbar, the nearest shelter 6 km away across a creek, "
            "landless households who work for daily wages and have no savings, older people "
            "living alone, and a hamlet of migrant salt-pan workers who are not on the panchayat "
            "list. The warning arrives, but nobody comes to move the people who cannot walk.")],
         [B("The hazard is identical. Exposure is higher in B because of where the houses stand. "
            "Vulnerability is higher in B because of what the houses are made of, who lives in "
            "them, and who the warning and transport systems were designed for. The loss in B "
            "will be measured in lives. The loss in A will be measured in crops and roofs."),
          BL(["Every disaster assessment that reports one district-level death toll averages A "
              "and B together and hides the difference.",
              "Every preparedness plan has to say how it will reach the people in B who are "
              "least visible to it: the migrants, the disabled, older people alone, and "
              "households outside the official lists.",
              "Section 10 returns to this with documented cases from the 2004 tsunami and "
              "Cyclone Fani."], "amber")])),

    C("Hazard types", "The hazards a South Asian practitioner meets",
      T(["Hazard", "Speed of onset", "Main harm", "Where in South Asia"],
        [["Tropical cyclone and storm surge", "Days of warning, hours of impact", "Wind, surge "
          "flooding, saline intrusion", "Bay of Bengal coasts: Odisha, Andhra Pradesh, West "
          "Bengal, Bangladesh, Myanmar; Arabian Sea coasts: Gujarat, Sindh"],
         ["Riverine flood", "Days", "Inundation, loss of crops and houses, disease",
          "Ganga and Brahmaputra basins, Indus plain in Pakistan"],
         ["Flash flood, cloudburst, GLOF", "Minutes to hours", "Sudden deaths, destroyed roads and "
          "bridges", "Himalaya and hill States, northern Pakistan, Nepal, Bhutan"],
         ["Landslide", "Minutes, often after days of rain", "Deaths, cut-off settlements",
          "Western Ghats, Himalaya, North-East"],
         ["Lightning", "Seconds", "Deaths of people working or sheltering outdoors",
          "Across India, high in central and eastern States"],
         ["Drought", "Months to years", "Crop and income loss, water scarcity, distress migration",
          "Rainfed districts of the Deccan, Rajasthan, Bundelkhand, Balochistan"],
         ["Heatwave and humid heat", "Days, with warning", "Heatstroke, deaths of older and "
          "outdoor-working people, lost work hours", "North and central India, Pakistan's "
          "Sindh and Punjab, coastal cities in humid heat"],
         ["Earthquake and tsunami", "No warning for earthquakes; minutes to hours for tsunami",
          "Building collapse; coastal inundation", "Himalayan arc, Gujarat, Andaman and Nicobar"]]),
      B("Geographic notes are general. Hazard maps for a specific district come from IMD, CWC, "
        "GSI and the State Disaster Management Authority, which the Finance Commission also "
        "used for its hazard scores (" + FC16 + ", para 11.49).", sm=True),
      compact=True),

    C("Slow and fast", "Slow-onset hazards are disasters too, and they are financed differently",
      TW([B("A cyclone has a landfall time. A drought has no single day on which it begins, and "
            "a heatwave builds over a week. Public systems are better at responding to events "
            "with a date. Rescue teams, relief camps and ex gratia payments are designed for "
            "the cyclone. Drought and heat harm people through lost income, debt, migration "
            "and illness spread over months, and that harm is easier to miss and harder to "
            "count."),
          B("The financing shows the bias. Of what States spent on notified disasters from "
            "2019-20 to 2023-24, floods took 55.09 per cent and drought 17.26 per cent. Heat "
            "was not on the national list of notified disasters at all. It was a State-specific "
            "disaster in eleven States, paid for out of a 10 per cent window in each State's "
            "response fund (" + FC16 + ", paras 11.44, 11.65, 11.66).")],
         [CH("dhExpChart", "bar", "Disaster-wise expenditure of States, 2019-20 to 2023-24 (% of total)",
             "Sixteenth Finance Commission Report, Vol. I, Figure 11.5, from the MHA National "
             "Disaster Management Information System",
             {"labels": ["Flood", "Drought", "State-specific", "Cyclone", "Landslide", "Hailstorm",
                         "Cold wave/frost", "Pest attack", "Fire", "Cloudburst"],
              "datasets": [{"label": "% of expenditure",
                            "data": [55.09, 17.26, 13.27, 6.94, 2.59, 1.94, 1.12, 0.94, 0.51, 0.32],
                            "backgroundColor": "#0EA5E9"}]},
             "{ indexAxis:'y', plugins:{legend:{display:false}}, scales:{ x:{ min:0, max:60, title:{display:true,text:'% of State disaster expenditure'} } } }"),
          B("Earthquake accounted for 0.002 per cent and is left off the chart.", sm=True)]),
      compact=True),

    C("Compounding", "Hazards arrive together, and one makes the next worse",
      TW([B("Disaster risk practice used to plan for one hazard at a time. Recent events in "
            "South Asia rarely arrive alone. Pakistan's 2022 floods combined torrential rain, "
            "riverine, urban and flash flooding, accelerated glacial melt and landslides. About "
            "33 million people were affected, one in seven Pakistanis, and nearly 8 million "
            "were displaced (" + PDNA + ")."),
          B("Heat and drought reinforce each other: hot days dry soil faster, and dry soil heats "
            "faster. A cyclone in the middle of a pandemic forces shelters to choose between "
            "crowding and distancing. A flood that destroys a primary health centre removes "
            "the place where heatstroke cases would have been treated the following summer.")],
         [T(["Combination", "What it does"],
            [["Heat followed by extreme rain", "Dry, hard soil runs off faster; flash floods"],
             ["Cyclone followed by flood", "Surge and river flooding after landfall; saline "
              "fields for years"],
             ["Drought followed by heat", "Water scarcity at the time people most need water"],
             ["Disaster during an epidemic", "Shelters become transmission sites; health staff "
              "are diverted"],
             ["Repeated small events", "Each one erodes savings, so the next does more harm"]]),
          H("amber", "The Sixteenth Finance Commission notes that States asked for more money "
            "because heavy rainfall, heatwaves and cloudbursts were making droughts, landslides "
            "and floods more severe (" + FC16 + ", para 11.24).")])),

    C("For practitioners", "Questions to ask of any disaster risk programme",
      TW([BL(["Which hazard is it about, and how was the hazard mapped? Whose data, at what "
              "resolution, for which years?",
              "Who is exposed? Has the programme counted people who are not on household "
              "lists: migrants, people in informal settlements, nomadic and pastoral groups?",
              "What makes people here vulnerable, and how was that established? Was there a "
              "vulnerability assessment, or a list copied from a guideline?",
              "Which of the three terms does the intervention change? A shelter, an embankment, "
              "a warning system and a cash transfer act on different terms.",
              "What happens to the person who cannot read the warning, cannot walk to the "
              "shelter, or will lose a day's wage by going?"], "cyan")],
         [B("These questions come before any discussion of law or money, because the law and the "
            "money follow from the answers. A district plan that cannot answer them is a list "
            "of departments and phone numbers. A plan that can answer them tells an officer "
            "where to send the boat first."),
          H("green", "For the climate science behind changing hazards, see ImpactMojo's "
            "<a href=\"https://www.impactmojo.in/101-courses/climate-essentials.html\">Climate "
            "Essentials 101</a>. For who bears environmental harm and why, see "
            "<a href=\"https://www.impactmojo.in/101-courses/env-justice.html\">Environmental "
            "Justice 101</a>.")])),
]

# ===================== SECTION 02: SENDAI =====================
SLIDES += [
    D("02", "Section Two", "The Sendai Framework 2015-2030"),

    C("Origins", "From Hyogo to Sendai",
      TW([B("The Sendai Framework for Disaster Risk Reduction 2015-2030 was adopted on 18 March "
            "2015 at the Third UN World Conference on Disaster Risk Reduction in Sendai, Japan, "
            "and endorsed by the UN General Assembly. It replaced the Hyogo Framework for Action "
            "2005-2015, and was the outcome of consultations that began in March 2012 and "
            "intergovernmental negotiations from July 2014 to March 2015."),
          B("It is not a treaty and creates no binding obligations. Its force comes from "
            "reporting: countries report against 38 global indicators through the online "
            "Sendai Framework Monitor, and UNDRR is charged with supporting implementation, "
            "follow-up and review. It sits alongside the Paris Agreement, the Addis Ababa "
            "Action Agenda, the New Urban Agenda and the Sustainable Development Goals.")],
         [T(["Feature", "Hyogo 2005-2015", "Sendai 2015-2030"],
            [["Focus", "Building resilience of nations and communities", "Managing risk, not "
              "only managing disasters"],
             ["Targets", "None quantified at global level", "Seven global targets, 38 indicators"],
             ["Hazards covered", "Mainly natural", "Natural and man-made, including "
              "environmental, technological and biological"],
             ["Health", "Limited", "Health resilience promoted throughout"],
             ["State role", "Primary", "Primary, with responsibility shared with local "
              "government, private sector and others"]]),
          B("Source: UNDRR, What is the Sendai Framework; " + SENDAI + ", foreword.", sm=True)])),

    C("Goal", "One outcome and one goal",
      TW([Q("The substantial reduction of disaster risk and losses in lives, livelihoods and "
            "health and in the economic, physical, social, cultural and environmental assets of "
            "persons, businesses, communities and countries.",
            "Sendai Framework, para 16, expected outcome"),
          Q("Prevent new and reduce existing disaster risk through the implementation of "
            "integrated and inclusive economic, structural, legal, social, health, cultural, "
            "educational, environmental, technological, political and institutional measures "
            "that prevent and reduce hazard exposure and vulnerability to disaster, increase "
            "preparedness for response and recovery, and thus strengthen resilience.",
            "Sendai Framework, para 17, goal")],
         [B("Read the goal as three instructions. Prevent new risk: do not build the next "
            "school on the floodplain. Reduce existing risk: retrofit the school that is "
            "already there. Strengthen resilience: prepare to respond and recover when the "
            "remaining risk becomes a disaster."),
          B("The first instruction is the cheapest and the most often ignored. Most risk in "
            "fast-growing South Asian cities is being created now, by where housing, roads and "
            "industry are built. A framework that only funds response will keep paying for "
            "risk that planning decisions made yesterday."),
          H("cyan", "The goal names exposure and vulnerability explicitly. It says nothing about "
            "stopping hazards, because most cannot be stopped.")])),

    C("Seven targets", "The seven global targets, verbatim in substance",
      T(["Target", "What it asks for", "By"],
        [["(a) Mortality", "Substantially reduce global disaster mortality, aiming to lower the "
          "average per 100,000 mortality rate in 2020-2030 compared with 2005-2015", "2030"],
         ["(b) Affected people", "Substantially reduce the number of affected people, aiming to "
          "lower the average per 100,000 in 2020-2030 compared with 2005-2015", "2030"],
         ["(c) Economic loss", "Reduce direct disaster economic loss in relation to global GDP",
          "2030"],
         ["(d) Infrastructure and services", "Substantially reduce damage to critical "
          "infrastructure and disruption of basic services, among them health and educational "
          "facilities, including by developing their resilience", "2030"],
         ["(e) Strategies", "Substantially increase the number of countries with national and "
          "local disaster risk reduction strategies", "2020"],
         ["(f) Cooperation", "Substantially enhance international cooperation to developing "
          "countries through adequate and sustainable support", "2030"],
         ["(g) Early warning", "Substantially increase the availability of and access to "
          "multi-hazard early warning systems and disaster risk information and assessments "
          "to people", "2030"]]),
      B("Source: " + SENDAI + ", para 18. Targets (a) to (d) are outcomes and are measured with "
        "loss data. Targets (e) to (g) are about means. Target (e) carried an earlier deadline "
        "because strategies were meant to be in place before the outcomes could move.",
        sm=True),
      compact=True),

    C("Four priorities", "Four priorities for action",
      TW([T(["Priority", "In plain terms"],
            [["1. Understanding disaster risk", "Know the hazard, who is exposed, who is "
              "vulnerable and what capacity exists. Use the knowledge for prevention, "
              "mitigation, preparedness and response."],
             ["2. Strengthening disaster risk governance", "Laws, institutions, plans and "
              "national platforms that assign responsibility at every level."],
             ["3. Investing in disaster risk reduction for resilience", "Public and private "
              "money for structural measures (shelters, embankments) and non-structural "
              "measures (land use rules, insurance, social protection)."],
             ["4. Preparedness and Build Back Better", "Prepare for response, act in "
              "anticipation of events, and use recovery to reduce future risk."]])],
         [B("The fourth priority contains the phrase that became a slogan, Build Back Better. "
            "UNDRR describes recovery, rehabilitation and reconstruction as a critical "
            "opportunity to integrate risk reduction into development. In practice that means "
            "a house rebuilt after a cyclone should be able to withstand the next one, and a "
            "school rebuilt after a flood should be on a plinth."),
          B("The same priority asks countries to take action in anticipation of events. That "
            "sentence is the basis for the anticipatory action discussed in section 09.",
            sm=True),
          H("amber", "The priorities are a checklist for reading a State disaster management "
            "plan. A plan that lists response equipment in detail and says nothing about "
            "priority 1 has skipped the step that decides where the equipment should go.")])),

    C("Whose framework", "The groups the framework names",
      TW([B("Paragraph 7 says governments should engage women, children and youth, persons with "
            "disabilities, poor people, migrants, indigenous peoples, volunteers, practitioners "
            "and older persons in designing and implementing policies, plans and standards."),
          B("Paragraph 36 goes further. It says persons with disabilities and their "
            "organisations are critical in assessing disaster risk and in designing plans "
            "tailored to specific requirements, taking into account universal design. It says "
            "older persons should be included in designing policies and early warning, and "
            "that migrants contribute to the resilience of communities and their knowledge "
            "can be useful in designing disaster risk reduction. Paragraph 27(h) asks that "
            "local authorities be given the regulatory and financial means to work with civil "
            "society, communities, indigenous peoples and migrants.")],
         [T(["Group", "Where named", "Why it matters in South Asia"],
            [["Persons with disabilities", "Paras 7, 32, 36(a)(iii)", "Shelters, warnings and "
              "evacuation transport are rarely designed for them"],
             ["Older persons", "Paras 7, 36(a)(iv)", "Highest heat mortality; least able to "
              "evacuate"],
             ["Migrants", "Paras 7, 27(h), 36(a)(vi)", "Often absent from household lists used "
              "for relief"],
             ["Women", "Paras 7, 32, 36", "Relief often paid to male heads of household"],
             ["Indigenous peoples", "Paras 7, 27(h)", "Adivasi land and forest rights shape "
              "exposure"]]),
          B("Source: " + SENDAI + ". Caste is not named in the framework. In South Asia it "
            "decides who is reached by relief, as section 10 shows.", sm=True)])),

    C("Measuring it", "How Sendai progress is measured",
      TW([B("UNDRR's Sendai Framework Monitor captures progress that member states report "
            "themselves against 38 indicators. A sub-system, DesInventar Sendai, lets countries "
            "build disaster loss databases to collect the data for targets (a) to (d): deaths, "
            "affected people, economic loss and damage to infrastructure."),
          B("Self-reporting is the framework's weakness. A country that records few heat "
            "deaths will appear to be meeting target (a) on heat whatever is actually happening. "
            "Loss databases are only as complete as the death certificates, revenue records and "
            "damage surveys that feed them."),
          B("Source: UNDRR, What is the Sendai Framework, section on monitoring scope.", sm=True)],
         [T(["Level", "What is measured", "Who defines it"],
            [["Outcome", "Global targets (a) to (g), 38 indicators", "Agreed globally; "
              "comparable"],
             ["Output", "Reduction of risk and increase in resilience", "National targets"],
             ["Input", "Public policy measures implementing the four priorities", "National "
              "indicators"],
             ["Custom", "Country-chosen targets reported in national DRR reports",
              "Member states"]]),
          H("cyan", "India's 2025 amendment requires a national disaster database and State "
            "databases covering disaster assessment, fund allocation, expenditure, plans and a "
            "risk register (" + DMA25 + ", s. 2(da) and s. 6(2)(v)). That is the domestic "
            "source a Sendai report should draw on.")])),

    C("Reading Sendai locally", "What Sendai asks of a district",
      T(["Sendai element", "District-level question", "Evidence a district can produce"],
        [["Target (a) mortality", "How many people died in disasters each year, by hazard, age "
          "and sex?", "Ex gratia records, death registration, hospital records"],
         ["Target (b) affected", "How many households were displaced, lost crops, lost work?",
          "Relief registers, crop loss surveys"],
         ["Target (d) services", "Which schools, health centres and roads were damaged, and for "
          "how long were they closed?", "Department damage reports"],
         ["Target (e) strategy", "Is there a district disaster management plan, updated, with "
          "a hazard and vulnerability assessment?", "The plan itself"],
         ["Target (g) early warning", "What share of villages received the last warning, by "
          "what channel, how long before impact?", "SMS logs, siren records, community "
          "surveys"],
         ["Priority 1", "Is there a hazard map and a list of vulnerable people by village?",
          "Maps, registers of older and disabled people"],
         ["Priority 4", "Were rebuilt houses and schools built to resist the next event?",
          "Engineering inspection"]]),
      B("Illustrative. The table is a way of translating global targets into records an Indian "
        "district already keeps or could keep.", sm=True),
      compact=True),
]

# ===================== SECTION 03: LAW AND INSTITUTIONS =====================
EPW = ("Jos Chathukulam, Disaster Management (Amendment) Act, 2025: Old Wine in a New Bottle?, "
       "Economic and Political Weekly, 26 July 2025, Vol. 60, No. 30")

SLIDES += [
    D("03", "Section Three", "India's disaster law and institutions"),

    C("The Act", "The Disaster Management Act 2005 builds three tiers of authority",
      TW([T(["Tier", "Body", "Chair", "Section"],
            [["National", "National Disaster Management Authority (NDMA)", "Prime Minister, ex "
              "officio", "s. 3"],
             ["National", "National Executive Committee", "Union Home Secretary", "s. 8, s. 10"],
             ["National", "National Crisis Management Committee", "Cabinet Secretary",
              "s. 8A (2025)"],
             ["National", "High Level Committee (central assistance)", "Minister in charge of "
              "disaster management", "s. 8B (2025)"],
             ["State", "State Disaster Management Authority (SDMA)", "Chief Minister, ex officio",
              "s. 14"],
             ["State", "State Executive Committee", "Chief Secretary", "s. 20"],
             ["District", "District Disaster Management Authority (DDMA)", "Collector or District "
              "Magistrate; elected local representative as co-chair", "s. 25"],
             ["City", "Urban Disaster Management Authority", "Municipal Commissioner",
              "s. 41A (2025)"]])],
         [B("Before 2005 India handled disasters through relief codes and relief commissioners "
            "in the States. The Act gave disaster management a statute, permanent bodies at "
            "each level, plans that must be written and approved, a specialist force and "
            "statutory funds. It applies to natural and man-made disasters alike."),
          B("The chairs show where the Act places authority. The national and State bodies are "
            "headed by the elected head of government. The district body, which does most of the "
            "work, is headed by the Collector, an appointed civil servant, with an elected "
            "representative of the local authority as co-chair."),
          B("Sources: " + DMA + ", ss. 3, 14, 25; " + DMA25 + ", ss. 8A, 8B, 41A; " + FC16 +
            ", paras 11.3 to 11.7 for the NEC and SEC chairs.", sm=True)]),
      compact=True),

    C("The district", "The DDMA is where plans meet people",
      TW([B("Section 25 requires every State to establish a DDMA for every district. Its members "
            "are the Collector as chair, the elected representative of the local authority as "
            "co-chair, the chief executive officer of the DDMA, the Superintendent of Police, "
            "the Chief Medical Officer and up to two other members. Since 2025 those two may be "
            "district officers, disaster management experts or people from civil society "
            "organisations (s. 25(2)(f), as substituted). Where a zila "
            "parishad exists, its chairperson is co-chair. In Sixth Schedule tribal areas the "
            "Chief Executive Member of the autonomous district council is co-chair."),
          B("The DDMA prepares the district disaster management plan, coordinates departments, "
            "and monitors whether local authorities comply. The Sixteenth Finance Commission "
            "calls DDMAs the critical hubs for planning, coordination and implementation, and "
            "notes that local authorities, including panchayats, municipalities and autonomous "
            "district councils, are responsible for their own plans and for relief and "
            "reconstruction in their areas (" + FC16 + ", paras 11.7, 11.8, 11.14).")],
         [P("amber", "A criticism worth knowing",
            "Jos Chathukulam argues in EPW that a DDMA headed by a bureaucrat, with the elected "
            "local functionary only as co-chair, is a sign of centralisation. He notes that in "
            "Kerala district panchayat presidents are DDMA co-chairs, but that during COVID-19 "
            "the Collectors ran DDMA meetings and the presidents' role was rare. He also argues "
            "that neither the 2005 Act nor the 2025 amendment provides financial allocations "
            "to the lower levels of administration."),
          B("Source: " + EPW + ".", sm=True),
          H("cyan", "For a practitioner, the DDMA's plan and its meeting minutes are public "
            "documents in most States. Read them before designing a district programme.")])),

    C("2025 amendment", "What the Disaster Management (Amendment) Act 2025 changed",
      T(["Change", "Provision", "What it means"],
        [["Definitions added", "s. 2: hazard, exposure, vulnerability, disaster risk, "
          "evacuation, recovery, rehabilitation, resilience, response, prevention, disaster "
          "database", "Indian law now uses the same risk vocabulary as Sendai"],
         ["Disaster risk reduction inside disaster management", "Explanation to s. 2(e)",
          "Reducing exposure and vulnerability and improving preparedness are part of the "
          "statutory meaning of disaster management"],
         ["Plans made by the Authorities", "ss. 6(2)(b), 11(2) for NDMA; ss. 18(2)(b), 23 for SDMAs",
          "NDMA and SDMAs coordinate the preparation and approval of plans, which earlier sat "
          "with the executive committees"],
         ["New NDMA functions", "s. 6(2)(k) to (w)", "Periodic stock-take of all risks including "
          "emerging risks from extreme climate events, preparedness assessment of each State, "
          "post-disaster audit, a national disaster database, minimum standards of relief"],
         ["NDMA staff", "New s. 5", "NDMA may specify its own staff with Central Government "
          "approval, and appoint experts"],
         ["NCMC and HLC made statutory", "ss. 8A, 8B", "Existing committees given a footing in "
          "law"],
         ["Urban authorities", "s. 41A", "States may create Urban Disaster Management "
          "Authorities for capitals and municipal corporation cities"],
         ["State response forces", "s. 44A", "States may constitute a State Disaster Response "
          "Force"],
         ["Relief standards and non-discrimination", "ss. 12, 13, 19 omitted; s. 61 amended",
          "Standards moved into NDMA and SDMA functions; compensation dropped from the "
          "non-discrimination clause"],
         ["Power over persons", "New s. 60A", "Union or State may by notification require anyone "
          "to act or refrain in relation to a hazard, for up to six months, with a penalty of up "
          "to ₹10,000"],
         ["Plan review", "ss. 11(4), 23(5), 31(4)", "National and State plans reviewed every three "
          "years and updated every five; district plans reviewed at least every two years"],
         ["Law and order excluded", "Explanation to s. 2(d)", "Man made causes do not include law "
          "and order situations"]]),
      B("Source: " + DMA25 + ". The Bill was introduced in the Lok Sabha on 1 August 2024, "
        "passed by the Lok Sabha on 12 December 2024 and by the Rajya Sabha on 25 March 2025 "
        "(PRS Legislative Research, Bill track), and received the President's assent on 29 "
        "March 2025.", sm=True),
      compact=True),

    C("Cities and forces", "Urban authorities and State response forces",
      TW([TERM("Urban Disaster Management Authority, s. 41A",
               "A State may, by notification, constitute a separate authority for its capital "
               "and for every city with a Municipal Corporation, except the National Capital "
               "Territory of Delhi and the Union territory of Chandigarh. The Municipal "
               "Commissioner chairs it and the District Collector is vice chair. It prepares and "
               "implements an Urban Plan for disaster management."),
          B("Cities had been planned for through district plans drawn for mostly rural "
            "districts. Urban flooding, heat islands, building collapse and fire behave "
            "differently, and the municipal corporation controls drains, building permits and "
            "street-level services. Placing the authority with the Municipal Commissioner puts "
            "it with the body that controls those levers. Note the word may: the Act enables "
            "these authorities and does not require them.")],
         [TERM("State Disaster Response Force, s. 44A",
               "A State may constitute a State Disaster Response Force for specialist response to "
               "a threatening disaster situation or disaster, with functions and service "
               "conditions set by the State. The 2005 Act provided only the National Disaster "
               "Response Force (s. 44)."),
          B("Many States had already raised such forces before the amendment gave them a legal "
            "basis. Odisha created the Odisha Disaster Rapid Action Force after the 1999 super "
            "cyclone and had 10 units by 2019 (" + FANI + ", ch. 15). The Sixteenth Finance "
            "Commission describes State forces as an important first line of defence alongside "
            "the NDRF (" + FC16 + ", para 11.15)."),
          H("amber", "A note on initials. NDRF means both the National Disaster Response Force "
            "(s. 44) and the National Disaster Response Fund (s. 46). SDRF means both State "
            "forces and State funds. Check which one a document means.")])),

    C("Severe disasters", "How a State gets central money after a severe disaster",
      FLOW("State meets the first costs from its State Disaster Response Fund",
           "State submits a memorandum seeking central assistance",
           "Inter-Ministerial Central Team visits and assesses damage",
           "Inter-Ministerial Group, chaired by the Union Home Secretary, scrutinises",
           "High Level Committee approves assistance from the National Disaster Response Fund"),
      TW([B("For a calamity of severe nature, an Inter-Ministerial Central Team assesses the damage "
            "and recommends assistance. The Inter-Ministerial Group headed by the Union Home "
            "Secretary, or the Secretary, Agriculture for agricultural disasters, scrutinises the "
            "assessment, and the High Level Committee of Cabinet Ministers gives final approval "
            "(" + FC16 + ", para 11.11). The 2025 amendment wrote the High Level Committee into "
            "the Act at s. 8B, as the body that provides assistance under s. 46 and approves "
            "mitigation assistance under s. 47.")],
         [B("Sequence matters for people waiting for help. A State's own fund can be spent at "
            "once. Central money comes only after a memorandum, a team visit, scrutiny and "
            "approval. Several States told the Finance Commission that NDRF approval and "
            "disbursal were delayed (" + FC16 + ", para 11.29). After Cyclone Fani, the MHA "
            "sanctioned an advance of ₹340.87 crore to Odisha on the decision of the National "
            "Crisis Management Committee (" + FANI + ", executive summary)."),
          H("cyan", "A district practitioner rarely sees this process, but its timing decides "
            "when reconstruction money reaches the village.")]),
      compact=True),

    C("Rights in the Act", "What the Act promises to people affected by disaster",
      TW([TERM("Minimum standards of relief, now s. 6(2)(w)",
               "The NDMA recommends guidelines for minimum standards of relief, which may "
               "include the minimum requirements in relief camps for shelter, food, drinking "
               "water, medical cover and sanitation, special provision for widows and orphans, "
               "ex gratia for loss of life, and assistance for damaged houses and for restoring "
               "livelihoods. Each SDMA lays down State standards, which may not be lower than the "
               "national minimum (s. 18(2)(o))."),
          TERM("Prohibition against discrimination, s. 61",
               "While providing relief to the victims of disaster, there shall be no "
               "discrimination on the ground of sex, caste, community, descent or religion.")],
         [B("In the 2005 Act the minimum standards sat in s. 12, which said the guidelines shall "
            "include those items. The 2025 amendment omitted ss. 12, 13 and 19 and moved the "
            "standards into the functions of the NDMA and SDMAs, where the list may include them. "
            "Section 13, also omitted, had let the NDMA recommend relief in loan repayment."),
          B("The amendment also deleted the words compensation and from s. 61. Before 2025 the "
            "ban on discrimination covered compensation and relief. It now names relief only. "
            "The list of grounds does not include disability, age or migrant status, so those "
            "groups rely on the general law and on the plans."),
          B("Sources: " + DMA + ", ss. 12, 13, 61; " + DMA25 + ", ss. 5, 9, 10, 11, 37 of the "
            "amending Act.", sm=True),
          H("red", "A practitioner documenting exclusion from relief should cite s. 61 as it now "
            "stands, and should not assume it reaches compensation.")])),

    C("Plans", "The plan is the document that turns the law into action",
      T(["Plan", "Prepared by", "What to look for when reading it"],
        [["National Plan", "NDMA, after 2025, through its coordination of preparation and "
          "approval (s. 6(2)(b))", "Hazard-wise responsibilities of Union ministries"],
         ["State Plan", "SDMA, in consultation with local, district and urban authorities and "
          "people's representatives (s. 23(2))", "The exposure of each part of the State and the "
          "vulnerability of its people, assets and livelihoods (s. 23(4)(a))"],
         ["District Plan", "DDMA, approved by the SDMA (s. 18(2)(ca))", "Village-level lists of "
          "vulnerable people, shelters, routes, stockpiles, contact persons; s. 31(4) now requires "
          "review at least every two years"],
         ["Urban Plan", "Urban Disaster Management Authority, s. 41A(4)", "Drainage, heat, "
          "building safety, informal settlements"],
         ["Departmental plans", "Each ministry and department", "Whether schools, hospitals and "
          "roads are built to resist local hazards"],
         ["Heat action plans", "State, district or city authorities", "Not created by the Act. "
          "Section 08 shows most do not state their legal basis."]]),
      TW([B("A plan that has not been updated since it was first written is common. A useful "
            "test is whether the plan names people and places or only departments and "
            "telephone numbers.", sm=True)],
         [H("amber", "The 2025 amendment requires NDMA to undertake post-disaster audits of "
            "preparedness and response in a State after a severe disaster (s. 6(2)(u)). Those "
            "audits, once published, are a new source of evidence on whether plans worked.")]),
      compact=True),

    C("Reading the law", "What the amendment did not do",
      TW([B("Jos Chathukulam's EPW commentary argues that most of the 2025 amendment strengthens "
            "a centralised, top-down approach. His points are that the new staffing and "
            "regulation powers of the NDMA, the statutory status of the NCMC and HLC, and the "
            "removal of the specified purposes for which the National Disaster Response Fund "
            "may be used all concentrate authority, that local governments are given no larger "
            "role, and that the amendment contains no comprehensive provisions for pandemics "
            "or for the particular vulnerability of women, persons with disabilities and "
            "marginalised groups."),
          B("Source: " + EPW + ".", sm=True)],
         [B("The government's case for the amendment rests on clarity and data: definitions "
            "aligned with Sendai, plans prepared by the Authorities themselves, a national and "
            "State disaster database, preparedness assessments and post-disaster audits. Both "
            "readings can be true at once. A database and an audit power are useful tools, and "
            "who controls them decides whom they serve."),
          BL(["Ask whether your State has notified an Urban Disaster Management Authority for "
              "its cities, and who sits on it.",
              "Ask whether the State has published its disaster database, and whether it "
              "records deaths by sex, age and social group.",
              "Ask whether panchayats have their own disaster plans and any money to act on "
              "them."], "cyan")])),
]

# ===================== SECTION 04: FUNDS =====================
SLIDES += [
    D("04", "Section Four", "Paying for disasters: the funds"),

    C("The funds", "Four statutory funds, two national and two in each State",
      TW([T(["Fund", "Section", "Used for"],
            [["National Disaster Response Fund (NDRF)", "s. 46", "Central assistance to States "
              "for severe disasters; after 2025, for different aspects of disaster management"],
             ["National Disaster Mitigation Fund (NDMF)", "s. 47", "Projects exclusively for "
              "mitigation, applied by NDMA"],
             ["State Disaster Response Fund (SDRF)", "s. 48(1)(a)", "Relief and response in the "
              "State, first call after any notified disaster"],
             ["State Disaster Mitigation Fund (SDMF)", "s. 48(1)(c)", "Mitigation projects in the "
              "State"],
             ["District response and mitigation funds", "s. 48(1)(b), (d)", "Provided in the Act; "
              "the Fifteenth Finance Commission found them not practical"]])],
         [B("The Act provided mitigation funds from 2005. They existed on paper only until the "
            "Fifteenth Finance Commission recommended they be constituted with real money. As a "
            "result, the Sixteenth Finance Commission reports that all the funds envisaged under "
            "the Act have been constituted by all the States and the Union, except the district "
            "funds (" + FC16 + ", para 11.1)."),
          B("Money flows in through the Finance Commission. Each Commission recommends how "
            "much goes into the State funds for its five-year award period, how it is split "
            "between the Union and the States, and how it is shared among States."),
          H("amber", "States contribute 25 per cent of SDRF and SDMF, and the Union 75 per cent. "
            "For north-eastern and Himalayan States the split is 90:10 (" + FC16 +
            ", para 11.61).")])),

    C("History", "From margin money to mitigation funds",
      T(["Commission", "What it introduced"],
        [["Second Finance Commission", "Margin money for calamities of moderate nature, based on "
          "average relief spending of the previous decade"],
         ["Eighth", "50 per cent Union contribution; fire to be treated as a disaster like flood, "
          "cyclone and earthquake"],
         ["Ninth", "Calamity Relief Fund, 75 per cent Union and 25 per cent State"],
         ["Tenth", "National Fund for Calamity Relief for severe calamities"],
         ["Eleventh", "Dissolved the national fund after its corpus ran out in three years; "
          "created a National Calamity Contingency Fund with ₹500 crore"],
         ["Twelfth", "Added landslides, avalanches, cloudbursts and pest attacks to the notified "
          "list"],
         ["Thirteenth", "Merged the old funds into the SDRF and NDRF under the 2005 Act"],
         ["Fourteenth", "Let States spend up to 10 per cent of SDRF on locally significant "
          "disasters not on the national list"],
         ["Fifteenth", "Mixed a Disaster Risk Index with past spending; created the mitigation "
          "funds; set sub-windows and earmarked allocations"],
         ["Sixteenth", "Expanded the risk index to ten hazards; moved preparedness to the "
          "mitigation funds; recommended heatwave and lightning as national disasters"]]),
      B("Source: " + FC16 + ", paras 11.16 to 11.19, 11.55, 11.56, 11.73.", sm=True),
      compact=True),

    C("Growth", "State disaster fund allocations, by Finance Commission",
      TW([CH("dhFcChart", "bar", "Allocation to State disaster funds, by Finance Commission award (₹ crore)",
             "FC-11 to FC-15 from Sixteenth Finance Commission Report, Vol. I, Figure 11.1; FC-16 "
             "from para 11.54 (SDRF and SDMF, 2026-27 to 2030-31). Nominal rupees.",
             {"labels": ["FC-11", "FC-12", "FC-13", "FC-14", "FC-15 (2021-26)", "FC-16 (2026-31)"],
              "datasets": [{"label": "₹ crore", "data": [11007, 21333, 33581, 61219, 160153, 204401],
                            "backgroundColor": ["#94A3B8", "#94A3B8", "#94A3B8", "#94A3B8",
                                                "#0EA5E9", "#6366F1"]}]},
             "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, title:{display:true,text:'₹ crore'} } } }")],
         [B("Each five-year award has been larger than the last. The Fifteenth Commission's "
            "₹1,60,153 crore for 2021-26 was a 161 per cent increase. The Sixteenth "
            "Commission's ₹2,04,401 crore for 2026-31 is divided 80:20 into ₹1,63,521 crore for "
            "State response funds and ₹40,880 crore for State mitigation funds."),
          B("The figures are nominal. Part of the rise is inflation, and part is that the "
            "Commissions moved from funding relief alone to funding mitigation and "
            "reconstruction as well. The chart does not show what was released or spent."),
          ST([CARD("₹2,04,401 cr", "SDRF and SDMF, 2026-31", "indigo", "FC-16 para 11.54"),
              CARD("₹79,406 cr", "NDRF and NDMF, 2026-31", "cyan", "FC-16 para 11.60")], 2)],
         "a32"),
      compact=True),

    C("FC-16 formula", "How the Sixteenth Finance Commission shares money among States",
      TW([B("Each State's allocation is 70 per cent based on its average past expenditure on "
            "disasters from 2011-12 to 2023-24, leaving out the COVID-19 years 2020-21 and "
            "2021-22, and 30 per cent based on its score on the Disaster Risk Index. The base "
            "year allocation rises by 5 per cent a year."),
          B("The risk index multiplies a hazard score across ten disasters, an exposure score "
            "from projected population, and a vulnerability score from per-capita income. "
            "Expenditure data come from the major head 2245 accounts of each State, adjusted to "
            "remove transfers between funds and releases from the national fund."),
          B("Source: " + FC16 + ", paras 11.49 to 11.54, Box 11.1.", sm=True)],
         [T(["Design choice", "Consequence to watch"],
            [["70 per cent past spending", "States that spent more in the past get more. A State "
              "that under-spent on a slow disaster such as heat or drought is not compensated."],
             ["30 per cent risk index", "Rewards measured hazard, exposure and low income"],
             ["Per-capita income as vulnerability", "Poorer States score higher, but poor "
              "districts inside richer States are invisible"],
             ["Population as exposure", "Crops and infrastructure assumed to track population"],
             ["SDRF balance cap", "Releases withheld if unspent SDRF exceeds the last three "
              "years' allocations (para 11.58)"]]),
          H("amber", "Commentators have argued the new formula under-serves vulnerable hill and "
            "north-eastern States. Treat any claim about winners and losers by checking the "
            "State-wise Annexures 11.3 and 11.4 of the report.")])),

    C("Windows", "What the money can be spent on",
      TW([B("Under the Fifteenth Commission, the response fund had three sub-windows: Response "
            "and Relief (40 per cent), Recovery and Reconstruction (30 per cent) and "
            "Preparedness and Capacity Building (10 per cent), with the remaining 20 per cent "
            "going to the mitigation fund. The Economic Survey 2021-22 summarised the 80:20 "
            "division between response and mitigation for both State and national funds."),
          B("The Sixteenth Commission keeps 80:20 but changes the inside. States get full "
            "flexibility between Response and Relief and Recovery and Reconstruction, and "
            "Preparedness and Capacity Building moves to the mitigation funds, on the reasoning "
            "that preparedness happens before a disaster and response after it. Money may not "
            "be shifted between the response and mitigation funds because they are separate "
            "funds under the Act."),
          B("Sources: " + FC16 + ", paras 11.40, 11.55, 11.56, Summary (ii); Economic Survey "
            "2021-22, Vol. 2, para 2.35.", sm=True)],
         [CH("dhWindowChart", "bar", "NDRF sub-windows under FC-15: allocation and release to 31 July 2025 (₹ crore)",
             "Sixteenth Finance Commission Report, Vol. I, Table 11.1, from MHA",
             {"labels": ["Response and relief", "Recovery and reconstruction",
                         "Preparedness and capacity", "Fire services modernisation",
                         "Erosion resettlement"],
              "datasets": [
                  {"label": "Allocation", "data": [27385, 20539, 6846, 5000, 1000], "backgroundColor": "#94A3B8"},
                  {"label": "Released", "data": [14855, 818.74, 2778.58, 1214.68, 0], "backgroundColor": "#0EA5E9"}]},
             "{ indexAxis:'y', scales:{ x:{ min:0, title:{display:true,text:'₹ crore'} } } }")]),
      compact=True),

    C("Mitigation money", "Mitigation funds were created, and spent slowly",
      TW([CH("dhNdmfChart", "bar", "NDMF earmarked allocations under FC-15 and releases to 31 July 2025 (₹ crore)",
             "Sixteenth Finance Commission Report, Vol. I, Table 11.2, from MHA",
             {"labels": ["Urban flooding, 7 cities", "Erosion mitigation", "Drought-prone, 12 States",
                         "Landslide risk project", "Forest fire project", "Seismic and landslide, 10 States",
                         "Lightning safety", "Community DRR in PRIs", "GLOF programme"],
              "datasets": [
                  {"label": "Allocation", "data": [2500, 1500, 1200, 1000, 818.92, 750, 186.78, 163.32, 150], "backgroundColor": "#94A3B8"},
                  {"label": "Released", "data": [709.54, 0, 350, 4.54, 0, 0, 0, 0, 27.73], "backgroundColor": "#10B981"}]},
             "{ indexAxis:'y', scales:{ x:{ min:0, title:{display:true,text:'₹ crore'} } } }")],
         [B("Of ₹13,693 crore allocated to the National Disaster Mitigation Fund under the "
            "Fifteenth Commission, four earmarked allocations covered drought-prone States, "
            "seismic and landslide risk, urban flooding in the seven most populous cities, and "
            "erosion. By 31 July 2025, three of the nine earmarked lines in the table had "
            "released any money at all."),
          B("Central releases to States for their mitigation funds were around 80 per cent of "
            "allocation in 2021-22 to 2024-25, against 95 to 100 per cent for response funds. "
            "MHA and NDMA attributed the gap to delays in States constituting the funds and in "
            "issuing guidelines (" + FC16 + ", paras 11.37, 11.38, 11.41, 11.42)."),
          H("cyan", "For a practitioner, this is an opening. Mitigation money exists and is "
            "under-used. District proposals with a clear hazard, a costed project and a "
            "monitoring plan are what the funds were waiting for.")]),
      compact=True),

    C("Where it goes", "What relief spending actually buys",
      TW([B("The MHA's National Disaster Management Information System now records State "
            "expenditure against each disaster, which the Sixteenth Commission called granular "
            "data available for the first time. After removing COVID-19 spending, more than "
            "half of relief expenditure went on agricultural inputs (55.6 per cent), followed by "
            "ex gratia payments to people (23.4 per cent) and infrastructure (13 per cent)."),
          B("Relief spending by States rose from ₹11,070 crore in 2011-12 to ₹25,638 crore in "
            "2023-24, with peaks in the COVID-19 years (" + FC16 + ", paras 11.39, 11.43, 11.44)."),
          H("amber", "Agricultural input subsidy goes to people who farm land, and ex gratia goes "
            "to the families of people who died. Landless workers who lost wages, and families "
            "whose members fell ill, appear in neither line.")],
         [CH("dhReliefChart", "doughnut", "Composition of State relief expenditure, excluding COVID-19 (%)",
             "Sixteenth Finance Commission Report, Vol. I, para 11.44, from NDMIS; other is the "
             "remainder",
             {"labels": ["Agricultural inputs", "Ex gratia to people", "Infrastructure", "Other"],
              "datasets": [{"data": [55.6, 23.4, 13.0, 8.0],
                            "backgroundColor": ["#10B981", "#EF4444", "#0EA5E9", "#94A3B8"]}]},
             "{ scales:{ x:{display:false}, y:{display:false} }, plugins:{ legend:{ position:'right' } } }")]),
      compact=True),

    C("Notified list", "Which disasters the national funds pay for",
      TW([B("SDRF money can be spent on the disasters on the Union Government's notified list: "
            "cyclone, drought, earthquake, fire, flood, tsunami, hailstorm, landslide, avalanche, "
            "cloudburst, pest attack, frost and cold wave. States may spend up to 10 per cent of "
            "SDRF on locally significant disasters they have notified with transparent norms "
            "approved by the State Executive Committee (" + FC16 + ", para 11.65)."),
          B("Eleven States had notified heatwave and sixteen had notified lightning as "
            "State-specific disasters. The Sixteenth Commission recommended adding both to the "
            "national list (paras 11.66, 11.71, 11.73). In August 2026 the Parliamentary "
            "Standing Committee on Home Affairs made the same recommendation (ThePrint, 7 "
            "August 2026). Check the current MHA list before advising a State, because the "
            "notification is a separate step from the recommendation.")],
         [T(["Disaster", "On national list", "Note"],
            [["Flood, cyclone, drought", "Yes", "Most of the spending"],
             ["Earthquake, tsunami", "Yes", ""],
             ["Landslide, cloudburst, avalanche", "Yes", "Added by FC-12"],
             ["Fire", "Yes", "Treated as a disaster since FC-8"],
             ["Hailstorm, frost, cold wave, pest attack", "Yes", ""],
             ["Heatwave", "Recommended by FC-16", "State-specific in 11 States"],
             ["Lightning", "Recommended by FC-16", "State-specific in 16 States; 2,887 of "
              "8,060 deaths from forces of nature in 2022 (NCRB, cited in FC-16)"]]),
          B("The lightning figure is NCRB data as quoted by the Commission, para 11.70.", sm=True)]),
      compact=True),
]
