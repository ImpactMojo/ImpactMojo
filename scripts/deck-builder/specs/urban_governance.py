# -*- coding: utf-8 -*-
"""
Urban Development and Municipal Governance 101 (ImpactMojo 101 Series, native deck spec)
What counts as urban in India, how fast and where the country urbanises, the 74th Amendment
and the Twelfth Schedule, how municipalities are elected and staffed, municipal finance and
Finance Commission grants, the urban missions, slums and street vendors, urban work and the
job guarantee debate, heat and floods, participation, and what research has found.
Build: python3 scripts/deck-builder/build.py urban_governance
"""

SRC = "font-size:11px;opacity:.85"


def src(text):
    """A small source line under a block."""
    return {"t": "body", "cls": "sm", "html": text}


NOLEG = {"plugins": {"legend": {"display": False}}}

DECK = {
    "slug": "urban-governance",
    "title": "Urban Development and Municipal Governance 101",
    "description": ("Urban Development and Municipal Governance 101 is a free foundational course "
                    "for Indian development practitioners. It covers statutory and census towns, "
                    "Census 2027, the 74th Amendment and the Twelfth Schedule, municipal elections "
                    "and staff, property tax and Finance Commission grants, municipal bonds, AMRUT, "
                    "the Smart Cities Mission, PMAY-Urban, Swachh Bharat Mission-Urban, street "
                    "vendors, urban job guarantees, heat and floods, ward committees and the research "
                    "evidence. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Urban Development and<br>Municipal Governance 101",
         "sub": "How Indian towns are defined, governed, financed and lived in, from the 74th "
                "Amendment to the 16th Finance Commission",
         "tags": ["Urban Governance", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What we cover",
         "items": [
             {"name": "What counts as urban"},
             {"name": "How fast and where India urbanises"},
             {"name": "The 74th Amendment and the Twelfth Schedule"},
             {"name": "Who runs a town, from councils to staff"},
             {"name": "Municipal finance"},
             {"name": "Transfers, Finance Commissions and borrowing"},
             {"name": "The urban missions"},
             {"name": "Slums, housing and street vendors"},
             {"name": "Urban work and the job guarantee debate"},
             {"name": "Heat, floods and the municipal role"},
             {"name": "Participation and what research has found"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What counts as urban"},

        {"type": "content", "label": "Two Kinds of Town",
         "title": "India has two kinds of town, and only one of them has a municipality",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "term", "word": "Statutory town",
                        "def": "Every administrative unit that a state law defines as urban, such as a "
                        "municipal corporation, municipality, cantonment board, notified town area "
                        "committee, town panchayat or nagar palika. The Registrar General treats all "
                        "of them as urban without applying any test."},
                       {"t": "body", "html": "A statutory town exists because a state government "
                        "issued a notification under its municipal law. That notification brings an "
                        "urban local body, a municipal budget, property tax under a municipal act and "
                        "eligibility for urban programmes. Most of this course is about statutory "
                        "towns, because they are the places with an elected urban government."}],
              "right": [{"t": "term", "word": "Census town",
                         "def": "A place with no municipal status that meets three tests together: "
                         "at least 5,000 people, at least 75 per cent of male main workers outside "
                         "agriculture, and a density of at least 400 persons per square kilometre."},
                        {"t": "body", "html": "A census town is a statistical category. The Census "
                         "counts its people as urban, while the state continues to govern it as a "
                         "village through a gram panchayat under the 73rd Amendment. The same "
                         "settlement can therefore be urban in national statistics and rural in its "
                         "budget, its schemes and its building rules."},
                        {"t": "hbox", "color": "amber", "html": "Definitions as given by the Ministry "
                         "of Home Affairs in Lok Sabha Unstarred Question 6458, 7 May 2013, Annexure II."}]},
         ]},

        {"type": "content", "label": "The Tests", "compact": True,
         "title": "The Census tests for urban places, and what each one measures",
         "blocks": [
             {"t": "table",
              "head": ["Category", "Rule used by the Census", "What it captures", "What it leaves out"],
              "rows": [
                  ["Census town, population test", "At least 5,000 persons", "Settlement size", "Large villages just under the line, however non-farm their economy"],
                  ["Census town, workforce test", "At least 75 per cent of male main workers in non-agricultural work", "A shift out of farming", "Women's work, because only male main workers are counted"],
                  ["Census town, density test", "At least 400 persons per sq km (1,000 per sq mile)", "Compact settlement", "Hill and forest settlements spread over large village areas"],
                  ["City", "A town of 1,00,000 persons or more", "Size class", "Nothing about governance"],
                  ["Outgrowth", "A village or hamlet with urban features, contiguous to a statutory town, outside its limits", "Spillover around towns", "Its residents remain under rural administration"],
                  ["Urban agglomeration", "A town and its outgrowths, or contiguous towns, with at least one statutory town and a total population of at least 20,000 (2001 rule)", "The functional city", "It has no government of its own"]]},
             {"t": "body", "cls": "sm", "html": "Rules from the Ministry of Home Affairs answer to "
              "Lok Sabha Unstarred Question 6458 (7 May 2013), Annexure II. Any area not classified "
              "as urban is rural, and the revenue village is the basic unit. The three census-town "
              "tests must all be met at once, so a settlement of 20,000 people that fails the "
              "density test stays rural in the Census."},
         ]},

        {"type": "content", "label": "Where the City Ends",
         "title": "How the Census draws a city's edge with outgrowths and agglomerations",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "body", "html": "An outgrowth is a village, a hamlet or an enumeration "
                        "block made of them, with clear boundaries, that has grown up next to a "
                        "statutory town but outside its legal limits. The Census gives railway "
                        "colonies, university campuses, port areas and military camps as examples. To "
                        "count as an outgrowth, the place must have urban infrastructure (paved roads, "
                        "electricity, taps, drainage, schools, post offices, clinics, banks) and must "
                        "touch the core town."},
                       {"t": "body", "html": "An urban agglomeration joins a town and its outgrowths, "
                        "or two or more contiguous towns, into one unit for counting. It must contain at "
                        "least one statutory town. This is the closest the Census comes to the city "
                        "that people commute across every day, and it is a unit that no single council "
                        "governs."}],
              "right": [{"t": "panel", "color": "cyan", "title": "Why the edge matters for governance", "html":
                         "A household in an outgrowth may be counted in a city's population while its "
                         "water, roads and building permissions come from a gram panchayat or a district "
                         "office. A city plan prepared by the municipality covers only the municipal "
                         "area, so the fastest-growing edges are often outside it. Articles 243ZD and "
                         "243ZE (section 03) were written to plan across this boundary through district "
                         "and metropolitan planning committees."},
                        src("Definitions from MHA, Lok Sabha Unstarred Question 6458, 7 May 2013.")]},
         ]},

        {"type": "content", "label": "Census Towns", "title": "Census towns multiplied between 2001 and 2011",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "3,894", "label": "census towns identified in Census 2011, against 1,362 in Census 2001", "color": "cyan", "source": "World Bank, Report AUS7449, 2015"},
                 {"num": "15%", "label": "of India's urban population lived in census towns in 2011, and 36% of the population of towns under 1 lakh", "color": "amber", "source": "Same report, Executive Summary"},
                 {"num": "~1/3", "label": "of urban growth of about 9 crore people in 2001 to 2011 came from new census towns, that is, from reclassification", "color": "green", "source": "Same report"}]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The 2011 count of urban population rose partly because "
                        "thousands of large villages crossed the three tests. Nobody moved for that "
                        "part of the increase. The settlements changed what their people did for a "
                        "living, and the Census changed their label."}],
              "right": [{"t": "body", "html": "The Ministry of Housing and Urban Affairs counted "
                         "4,378 statutory towns when it approved AMRUT 2.0 in October 2021. That number "
                         "moves whenever states notify new municipalities or merge villages into old "
                         "ones, so always ask which year and which list a town count comes from."}]},
             src("Mukhopadhyay and Zérah, <em>Understanding India's Urban Frontier: What is behind the "
                 "emergence of Census Towns in India?</em>, World Bank Report AUS7449, 28 August 2015. "
                 "Cabinet release on AMRUT 2.0, 12 October 2021."),
         ]},

        {"type": "content", "label": "Fieldwork", "compact": True,
         "title": "Census towns are urban in the Census and rural in governance",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A World Bank study led by Partha Mukhopadhyay and "
                        "Marie-Hélène Zérah, with a research team coordinated by the Centre for Policy "
                        "Research, studied census towns in Bihar, West Bengal, Odisha and Jharkhand. "
                        "It found an everyday bazaar economy serving surrounding villages, small "
                        "town-specific trades often rooted in caste occupations, and five new "
                        "activities common to every site, namely para-transit, construction, private "
                        "education, private health care and mobile phone services."},
                       {"t": "body", "html": "Controlling for size, the study found little evident "
                        "difference in service provision between census towns and statutory towns. "
                        "Built-up growth spilled outside settlement boundaries everywhere, helped by "
                        "the absence of building regulations and lower taxes outside towns."}],
              "right": [{"t": "panel", "color": "amber", "title": "Who wants urban status", "html":
                         "The push for municipal status came mostly from local elites and traders. "
                         "Poorer groups resisted it. In Erein, Odisha, Dalit, Muslim and tribal "
                         "residents were apprehensive about losing rural welfare schemes. In Bihar, "
                         "where access to those schemes was poor, the argument for staying rural was "
                         "weaker."},
                        {"t": "hbox", "color": "cyan", "html": "The report's policy conclusion is to "
                         "plan at the panchayat, tehsil or district level, because the rural and urban "
                         "split that structures all public programmes does not match how these places "
                         "work. It names more active district planning committees as one option."},
                        src("World Bank Report AUS7449 (2015), Executive Summary, paragraphs 5 to 17.")]},
         ]},

        {"type": "content", "label": "Reclassification", "compact": True,
         "title": "What changes when a village becomes a statutory town",
         "blocks": [
             {"t": "table",
              "head": ["Matter", "Governed as a village (census town or outgrowth)", "Governed as a statutory town"],
              "rows": [
                  ["Constitutional part", "Part IX, panchayats (73rd Amendment)", "Part IXA, municipalities (74th Amendment)"],
                  ["Wage employment", "Covered by the rural employment guarantee, now the VB-G RAM G Act, which applies to rural areas notified by the Centre", "No national guarantee. Some states run their own urban schemes (section 09)"],
                  ["Housing scheme", "Rural housing scheme", "PMAY-Urban 2.0, which covers statutory towns as per Census 2011 and towns notified later"],
                  ["Finance Commission money", "Rural local body grants", "Urban local body grants, including the 16th Finance Commission's urbanisation premium"],
                  ["Building and land rules", "Often no building regulation", "Municipal building bye-laws and property tax"],
                  ["Elected body", "Gram panchayat", "Nagar panchayat, municipal council or corporation"]]},
             {"t": "body", "cls": "sm", "html": "Workers in Himachal Pradesh's newly urban areas told "
              "a researcher that reclassification took away the rural job guarantee and called the "
              "state's urban scheme the 'Shahri NREGA' (Choragudi, Ideas for India, 21 March 2022). "
              "The 16th Finance Commission set aside ₹10,000 crore to reward states that merge "
              "peri-urban villages into municipalities and adopt a rural-to-urban transition policy "
              "(PRS summary, 1 February 2026). PMAY-U 2.0 Operational Guidelines, paragraph 2.1. "
              "Kulkarni, Ideas for India, 7 January 2026, on the notified-area rule."},
         ]},

        {"type": "content", "label": "Census 2027",
         "title": "Census 2027 is running now, in two phases",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Item", "Census 2027"],
                        "rows": [
                            ["Reference date", "00:00 hours, 1 March 2027. For Ladakh and snow-bound areas of Jammu and Kashmir, Himachal Pradesh and Uttarakhand, 1 October 2026"],
                            ["Phase 1", "Houselisting and Housing Census, one 30-day window per state between April and September 2026, after 15 days of online self-enumeration"],
                            ["Phase 2", "Population Enumeration, February 2027"],
                            ["Caste", "To be enumerated in the second phase"],
                            ["Boundaries", "Administrative units frozen as on 1 January 2026"],
                            ["Cost", "₹11,718.24 crore, approved by the Cabinet on 12 December 2025"],
                            ["Count", "The 16th Census, and the 8th since Independence"]]}],
              "right": [{"t": "body", "html": "The Registrar General's Circular No. 1 of 13 August "
                         "2025 asked states to report every change to districts, sub-districts, towns, "
                         "wards and villages since 2010, up to the freezing of boundaries on 31 December "
                         "2025. Circular No. 2 asked for a list of villages that could become new census "
                         "towns. The screening tests in its proforma use 2011 data, asking for 4,000 people or "
                         "more, density of at least 400 per sq km, and under 25 per cent of male main "
                         "workers in agriculture."},
                        {"t": "hbox", "color": "amber", "html": "For urban work this means two things. "
                         "Town boundaries in Census 2027 are those of 31 December 2025, and the census "
                         "town tests are the 2011 tests, so 2011 and 2027 urban figures can be compared "
                         "directly."},
                        src("Directorate of Census Operations, Maharashtra, press conference deck, 30 "
                            "April 2026 (PIB). RGI Census 2027 Circulars No. 1 and 2.")]},
         ]},

        {"type": "content", "label": "Houselisting", "compact": True,
         "title": "The houselisting questions an urban practitioner will use",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["Group", "Questions in Phase 1 of Census 2027"],
                        "rows": [
                            ["The building", "Material of floor, wall and roof, use of the house, condition of the house"],
                            ["The household", "Number of persons, sex of the head, whether the head is SC, ST or other, ownership status, number of dwelling rooms, married couples"],
                            ["Water and sanitation", "Main source of drinking water and its availability, access to and type of latrine, waste water outlet, bathing facility"],
                            ["Energy", "Main source of lighting, kitchen and LPG or PNG connection, main cooking fuel"],
                            ["Assets", "Radio, television, internet access, computer, phone, bicycle or two-wheeler, car"],
                            ["Food", "Main cereal consumed"]]}],
              "right": [{"t": "body", "html": "Phase 1 asks 34 questions about every census house. "
                         "Released at ward level, these give a municipality its first full count since "
                         "2011 of households without a latrine of their own, without piped water on "
                         "the premises, living in one room or renting. Those are the denominators for "
                         "AMRUT tap targets, sanitation planning and rental housing."},
                        {"t": "hbox", "color": "green", "html": "Ask the state Directorate of Census "
                         "Operations when ward-level houselisting tables will be released, and request "
                         "ward maps that match the frozen boundaries."},
                        src("Question list from the Directorate of Census Operations, Maharashtra, 30 April 2026, slides 9 and 10.")]},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "How fast and where India urbanises"},

        {"type": "content", "label": "The Long Run", "compact": True,
         "title": "India's urban share has risen by about 0.3 points a year for six decades",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "chart", "canvas": "ugUrbShare", "type": "line",
                        "title": "Urban population, per cent of total, India, 1960 to 2025",
                        "source": "World Bank, World Development Indicators, SP.URB.TOTL.IN.ZS (UN World Urbanization Prospects basis), accessed 14 October 2026",
                        "data": {"labels": ["1960", "1965", "1970", "1975", "1980", "1985", "1990", "1995", "2000", "2005", "2010", "2015", "2020", "2025"],
                                 "datasets": [{"label": "Urban share (%)",
                                               "data": [17.9, 18.6, 19.7, 21.5, 23.5, 24.7, 25.6, 26.6, 27.6, 29.1, 30.9, 32.5, 34.1, 35.7],
                                               "borderColor": "#0369A1", "backgroundColor": "rgba(3,105,161,0.10)",
                                               "fill": True, "tension": 0.25, "pointRadius": 3}]},
                        "options": {"plugins": {"legend": {"display": False}},
                                    "scales": {"y": {"min": 0, "max": 40, "title": {"display": True, "text": "% urban"}}}}}],
              "right": [{"t": "body", "html": "The World Bank series rises from 17.9 per cent in 1960 "
                         "to 35.7 per cent in 2025. Between censuses it is an estimate built from the "
                         "United Nations' projections, which use the Census definition of urban. The "
                         "2010 value, 30.9 per cent, sits close to the Census 2011 figure of 31.2 per "
                         "cent."},
                        {"t": "body", "html": "The pace is slow by Asian standards and steady. Nothing "
                         "in this line shows a sudden urban transition, and the step that does appear "
                         "in 2001 to 2011 owes a third of its people to reclassified villages."},
                        {"t": "hbox", "color": "amber", "html": "Figures after 2011 are projections "
                         "until Census 2027 results arrive."}]},
         ]},

        {"type": "content", "label": "Census 2011",
         "title": "37.7 crore urban residents in 2011, and the first decade in which towns grew by more people than villages",
         "blocks": [
             {"t": "stats", "cols": 4, "cards": [
                 {"num": "37,71,06,125", "label": "urban population, Census 2011", "color": "cyan", "source": "MHA, LS USQ 6458, 2013"},
                 {"num": "31.2%", "label": "of India's population urban in 2011, up from 27.8% in 2001", "color": "amber", "source": "MHA; World Bank AUS7449"},
                 {"num": "35 to 50", "label": "cities of 10 lakh or more, 2001 to 2011", "color": "green", "source": "HPEC report, 2011"},
                 {"num": "~60 crore", "label": "urban population projected for 2031 under the present definition", "color": "indigo", "source": "HPEC report, 2011"}]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The 2011 rural population was 83,34,63,448. The World "
                        "Bank's census-town study notes that 2001 to 2011 was the first decade in "
                        "which the absolute increase in urban population exceeded the increase in "
                        "rural population."}],
              "right": [{"t": "body", "html": "The High Powered Expert Committee on urban "
                         "infrastructure, chaired by Isher Judge Ahluwalia, expected 87 cities of a "
                         "million or more by 2031 and growth through the absorption of surrounding "
                         "municipalities and large villages into metropolitan areas."}]},
             src("Ministry of Home Affairs, Lok Sabha Unstarred Question 6458, 7 May 2013, Annexure I "
                 "(final Census 2011 figures released 30 April 2013). HPEC, <em>Report on Indian Urban "
                 "Infrastructure and Services</em>, March 2011, Executive Summary, paragraph 6."),
         ]},

        {"type": "content", "label": "States", "compact": True,
         "title": "Urban shares by state ranged from 10 per cent to 97 per cent in 2011",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "chart", "canvas": "ugStateShare", "type": "bar",
                        "title": "Urban population as per cent of total, selected states, Census 2011",
                        "source": "Census 2011 final figures, as tabled by MHA in Lok Sabha USQ 6458, 7 May 2013",
                        "data": {"labels": ["Delhi", "Goa", "Mizoram", "Tamil Nadu", "Kerala", "Maharashtra", "Gujarat", "Karnataka", "Punjab", "Haryana", "Andhra P. (undivided)", "West Bengal", "Madhya P.", "Rajasthan", "Uttar P.", "Odisha", "Assam", "Bihar", "Himachal P."],
                                 "datasets": [{"label": "% urban",
                                               "data": [97.5, 62.2, 52.1, 48.4, 47.7, 45.2, 42.6, 38.7, 37.5, 34.9, 33.4, 31.9, 27.6, 24.9, 22.3, 16.7, 14.1, 11.3, 10.0],
                                               "backgroundColor": "#0369A1"}]},
                        "options": {"indexAxis": "y", "plugins": {"legend": {"display": False}},
                                    "scales": {"x": {"min": 0, "max": 100}}}}],
              "right": [{"t": "body", "html": "The southern and western states are the most urban "
                         "of the large states, and the northern and eastern states the least urban. Himachal Pradesh and Bihar were about "
                         "one-tenth urban in 2011."},
                        {"t": "body", "html": "The national figure of 31.2 per cent therefore hides two "
                         "different policy problems. In Tamil Nadu and Kerala, half the population "
                         "lives in places classed as urban and the question is how to govern a "
                         "continuous rural-urban belt. In Bihar and Uttar Pradesh, small towns have "
                         "very little municipal capacity to absorb growth that has barely begun."},
                        {"t": "hbox", "color": "amber", "html": "Andhra Pradesh figures are for the "
                         "undivided state, before Telangana was formed in 2014."}]},
         ]},

        {"type": "content", "label": "International", "compact": True,
         "title": "By the international yardstick India is less urban than its neighbours report",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "chart", "canvas": "ugIntl", "type": "bar",
                        "title": "Urban population as per cent of total, 2024",
                        "source": "World Bank, World Development Indicators, SP.URB.TOTL.IN.ZS, accessed 14 October 2026",
                        "data": {"labels": ["Bangladesh", "India", "Pakistan", "Indonesia", "China", "Brazil"],
                                 "datasets": [{"label": "% urban, 2024",
                                               "data": [32.7, 35.4, 39.2, 58.8, 65.9, 87.9],
                                               "backgroundColor": ["#94A3B8", "#0369A1", "#94A3B8", "#94A3B8", "#94A3B8", "#94A3B8"]}]},
                        "options": {"plugins": {"legend": {"display": False}},
                                    "scales": {"y": {"min": 0, "max": 100}}}}],
              "right": [{"t": "body", "html": "Each country reports urban population on its own "
                         "definition, and the World Bank passes those definitions through. Brazil counts "
                         "the urban and suburban zones of every municipal and district centre, Mexico "
                         "any locality of 2,500 people, Argentina any centre of 2,000. India asks a "
                         "census town for 5,000 people, a density test and a workforce test together, "
                         "which is demanding by comparison."},
                        {"t": "body", "html": "The HPEC report made the point with a counterfactual. "
                         "If Indian villages of more than 10,000 people were classed as urban, the "
                         "country would have been over 35 per cent urban in 2010 instead of about 30, "
                         "still well below China at 45 per cent and Indonesia at 54 per cent in that "
                         "year."},
                        src("HPEC, March 2011, paragraph 1.1.1 and Box 1.1, citing United Nations (2007) for national definitions.")]},
         ]},

        {"type": "content", "label": "Absolute Numbers", "compact": True,
         "title": "The largest urban populations are in big states with modest urban shares",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "table",
                        "head": ["State", "Urban population, 2011", "Urban share"],
                        "rows": [
                            ["Maharashtra", "5.08 crore", "45.2%"],
                            ["Uttar Pradesh", "4.45 crore", "22.3%"],
                            ["Tamil Nadu", "3.49 crore", "48.4%"],
                            ["West Bengal", "2.91 crore", "31.9%"],
                            ["Andhra Pradesh (undivided)", "2.82 crore", "33.4%"],
                            ["Gujarat", "2.57 crore", "42.6%"],
                            ["Karnataka", "2.36 crore", "38.7%"],
                            ["Madhya Pradesh", "2.01 crore", "27.6%"],
                            ["Rajasthan", "1.70 crore", "24.9%"],
                            ["NCT of Delhi", "1.64 crore", "97.5%"],
                            ["Kerala", "1.59 crore", "47.7%"],
                            ["Bihar", "1.18 crore", "11.3%"]]}],
              "right": [{"t": "body", "html": "Uttar Pradesh is less than a quarter urban, yet only "
                         "Maharashtra had more urban residents in 2011. Programme money allocated by "
                         "urban population, as most Finance Commission grants are, therefore flows in "
                         "large amounts to states where urban councils are weakest."},
                        {"t": "body", "html": "Rounded from the exact counts: Maharashtra "
                         "5,08,18,259, Uttar Pradesh 4,44,95,063, Tamil Nadu 3,49,17,440, Bihar "
                         "1,17,58,016."},
                        src("Census 2011 final population by residence, MHA, LS USQ 6458, 7 May 2013, Annexure I.")]},
         ]},

        {"type": "content", "label": "Urban Work", "compact": True,
         "title": "Half of urban workers hold regular jobs, and two in five work for themselves",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "chart", "canvas": "ugStatus", "type": "bar",
                        "title": "Urban workers by status in employment, current weekly status, 2025 (%)",
                        "source": "MoSPI, PLFS annual 2025 (calendar year), all ages, persons, urban. Retrieved through the MoSPI data API",
                        "data": {"labels": ["Own-account worker or employer", "Helper in household enterprise", "Regular wage or salary", "Casual labour"],
                                 "datasets": [{"label": "% of urban workers",
                                               "data": [32.2, 6.1, 49.3, 11.3],
                                               "backgroundColor": ["#0369A1", "#38BDF8", "#047857", "#B45309"]}]},
                        "options": {"plugins": {"legend": {"display": False}},
                                    "scales": {"y": {"min": 0, "max": 60}}}}],
              "right": [{"t": "body", "html": "In the 2025 Periodic Labour Force Survey, manufacturing "
                         "employed 20.3 per cent of urban workers (usual status), trade and repair 19.6 "
                         "per cent, construction 10.0 per cent, transport and storage 6.8 per cent and "
                         "education 5.4 per cent. Agriculture still employed 7.5 per cent of urban "
                         "workers."},
                        {"t": "body", "html": "Two-thirds of urban workers (66 per cent) worked in "
                         "proprietary and partnership enterprises. Government, local bodies and public "
                         "enterprises together employed 10.1 per cent, and private and public limited "
                         "companies 17.2 per cent."},
                        {"t": "hbox", "color": "amber", "html": "Regular pay does not mean formal "
                         "terms. In PLFS 2023-24, 55.7 per cent of urban regular wage and salaried "
                         "employees had no written job contract, 43.7 per cent were not eligible for "
                         "paid leave and 49.4 per cent had no social security benefit."}]},
         ]},

        {"type": "content", "label": "Women's Work", "compact": True,
         "title": "Urban women are the least likely group in India to be in the labour force",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "chart", "canvas": "ugLfpr", "type": "bar",
                        "title": "Labour force participation rate, age 15 and above, usual status, 2025 (%)",
                        "source": "MoSPI, PLFS annual 2025 (calendar year), All India. Retrieved through the MoSPI data API",
                        "data": {"labels": ["Rural", "Urban"],
                                 "datasets": [{"label": "Men", "data": [80.5, 76.2], "backgroundColor": "#0369A1"},
                                              {"label": "Women", "data": [45.9, 27.7], "backgroundColor": "#B45309"}]},
                        "options": {"scales": {"y": {"min": 0, "max": 100}}}}],
              "right": [{"t": "body", "html": "In 2025, 27.7 per cent of urban women aged 15 and above "
                         "were working or seeking work, against 45.9 per cent of rural women. For men "
                         "the rural and urban rates were close, at 80.5 and 76.2 per cent."},
                        {"t": "body", "html": "Several urban services bear on this gap, among them safe and cheap "
                         "public transport, street lighting, public toilets, childcare and water at "
                         "home that does not need to be fetched. Most of these appear in the Twelfth "
                         "Schedule or in the urban missions. Rural women's participation is counted "
                         "with work on family farms, which has no urban equivalent of the same size."},
                        {"t": "hbox", "color": "cyan", "html": "The all-India female rate in 2025, "
                         "rural and urban together, was 40.0 per cent."}]},
         ]},

        {"type": "content", "label": "Reading the Numbers", "compact": True,
         "title": "Five urban figures that answer five different questions",
         "blocks": [
             {"t": "table",
              "head": ["Figure", "Source", "Definition behind it", "Use it for"],
              "rows": [
                  ["31.2% urban, 2011", "Census 2011", "Statutory towns plus census towns", "Official comparisons and allocations based on the last Census"],
                  ["35.4% urban, 2024", "World Bank, from UN projections", "National definition, projected", "Cross-country comparison, with caution"],
                  ["Over 35% in 2010", "HPEC counterfactual", "Villages over 10,000 people counted as urban", "Showing how the definition shapes the total"],
                  ["15% of urban population", "World Bank census-town study", "People in census towns governed as villages", "Estimating the urban population without a municipality"],
                  ["4,378 statutory towns", "MoHUA, AMRUT 2.0 approval, 2021", "Towns with an urban local body at that date", "Programme coverage counts"]]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The Census figure is the only one built from a "
                        "complete count. The others are projections, counterfactuals or administrative "
                        "lists, and each was made for a different purpose."}],
              "right": [{"t": "body", "html": "When two urban numbers disagree, check the unit "
                         "(people, towns or local bodies), the year, and whether census towns are "
                         "inside or outside the count."}]},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "The 74th Amendment and the Twelfth Schedule"},

        {"type": "content", "label": "Part IXA",
         "title": "The 74th Amendment gave municipalities a place in the Constitution",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Before 1992, municipalities existed only under state "
                        "laws, which alone set their term, their powers and their taxes. The "
                        "Constitution (Seventy-fourth Amendment) Act, 1992 inserted Part IXA, Articles "
                        "243P to 243ZG, and the Twelfth Schedule. Together they require every state to "
                        "constitute elected municipalities, hold their elections on a fixed cycle "
                        "through a State Election Commission, reserve seats, set up a State Finance "
                        "Commission and create planning committees for districts and metropolitan "
                        "areas."},
                       {"t": "body", "html": "The companion 73rd Amendment did the same for rural "
                        "panchayats in Part IX. The two parts were written in parallel, which is why "
                        "Article 243Y gives the panchayat finance commission of Article 243-I the job "
                        "of reviewing municipal finances as well."}],
              "right": [{"t": "panel", "color": "cyan", "title": "What the Amendment fixed and what it left to states", "html":
                         "It fixed the existence of municipalities, their five-year term, direct "
                         "election of councillors, reservation, the election and finance commissions "
                         "and the planning committees. It left to state legislatures the decisive "
                         "matters, such as which functions and taxes a municipality gets, how its mayor is "
                         "chosen, who appoints its staff and how much the state transfers. Most of "
                         "this section is about that division."},
                        src("Texts of Articles 243P to 243ZG and the Twelfth Schedule as reproduced by "
                            "the Constitution of India as published by the Legislative Department (legislative.gov.in).")]},
         ]},

        {"type": "content", "label": "The Articles", "ultra-compact": True,
         "title": "Part IXA article by article",
         "blocks": [
             {"t": "table",
              "head": ["Article", "What it provides", "Left to the state legislature"],
              "rows": [
                  ["243P", "Definitions. A metropolitan area has 10 lakh people or more, in one or more districts, with two or more municipalities or panchayats", "Notification of metropolitan and municipal areas by the Governor"],
                  ["243Q", "Three kinds of municipality, the nagar panchayat, municipal council and municipal corporation", "Which kind each town is"],
                  ["243R", "All seats filled by direct election from wards", "Representation of MPs, MLAs and experts, and the manner of electing the chairperson"],
                  ["243S", "Wards committees in municipalities of 3 lakh people or more", "Composition, territory and how seats are filled"],
                  ["243T", "Reservation for SCs, STs and women, including chairpersons", "Rotation, chairperson rules, backward classes"],
                  ["243U", "Five-year term, and elections within six months of a dissolution", "Grounds for dissolution"],
                  ["243W", "Powers and responsibilities, including Twelfth Schedule matters", "Everything that is actually devolved"],
                  ["243X", "Taxes and funds", "Which taxes, which assignments and which grants"],
                  ["243Y", "State Finance Commission review of municipal finances", "Whether recommendations are accepted"],
                  ["243Z", "Audit of municipal accounts", "Who audits and how"],
                  ["243ZA", "State Election Commission conducts elections", "All other election law"],
                  ["243ZD, 243ZE", "District and Metropolitan Planning Committees", "Composition, functions, chairperson"]]},
         ]},

        {"type": "content", "label": "Article 243Q",
         "title": "Three kinds of municipality, chosen by the Governor",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Type", "For", "Common names"],
                        "rows": [
                            ["Nagar panchayat", "A transitional area, 'an area in transition from a rural area to an urban area'", "Town panchayat, notified area"],
                            ["Municipal council", "A smaller urban area", "Municipality, nagar palika parishad"],
                            ["Municipal corporation", "A larger urban area", "Mahanagar palika, nagar nigam"]]},
                       {"t": "body", "cls": "sm", "html": "Article 243Q(2) lets the Governor classify "
                        "an area by its population, density, revenue generated for local administration, "
                        "share of non-agricultural employment, economic importance or other factors."}],
              "right": [{"t": "body", "html": "There is no national population threshold for any "
                         "type, so a corporation in one state can be smaller than a council in another. "
                         "The classification matters because it decides which state municipal law, and "
                         "so which powers, council size and officers, apply to the town."},
                        {"t": "panel", "color": "amber", "title": "The industrial township exception", "html":
                         "The proviso to Article 243Q(1) lets the Governor declare an area an "
                         "industrial township when an industrial establishment provides or proposes "
                         "to provide its municipal services. No elected municipality is then "
                         "constituted there, so residents have no municipal council to vote for."}]},
         ]},

        {"type": "content", "label": "Twelfth Schedule", "ultra-compact": True,
         "title": "The eighteen functions in the Twelfth Schedule",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["No.", "Function"],
                        "rows": [
                            ["1", "Urban planning including town planning"],
                            ["2", "Regulation of land-use and construction of buildings"],
                            ["3", "Planning for economic and social development"],
                            ["4", "Roads and bridges"],
                            ["5", "Water supply for domestic, industrial and commercial purposes"],
                            ["6", "Public health, sanitation conservancy and solid waste management"],
                            ["7", "Fire services"],
                            ["8", "Urban forestry, protection of the environment and promotion of ecological aspects"],
                            ["9", "Safeguarding the interests of weaker sections of society, including persons with disabilities"]]}],
              "right": [{"t": "table",
                         "head": ["No.", "Function"],
                         "rows": [
                             ["10", "Slum improvement and upgradation"],
                             ["11", "Urban poverty alleviation"],
                             ["12", "Urban amenities and facilities such as parks, gardens, playgrounds"],
                             ["13", "Promotion of cultural, educational and aesthetic aspects"],
                             ["14", "Burials and burial grounds, cremations, cremation grounds and electric crematoriums"],
                             ["15", "Cattle pounds, prevention of cruelty to animals"],
                             ["16", "Vital statistics including registration of births and deaths"],
                             ["17", "Public amenities including street lighting, parking lots, bus stops and public conveniences"],
                             ["18", "Regulation of slaughter houses and tanneries"]]},
                        src("Twelfth Schedule, Article 243W. Item 9 is paraphrased; the Schedule's own words "
                            "are older terms for disability.")]},
         ]},

        {"type": "content", "label": "Article 243W",
         "title": "Article 243W lets each state decide how much of the Schedule to hand over",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "quote", "text": "Subject to the provisions of this Constitution, the "
                        "Legislature of a State may, by law, endow (a) the Municipalities with such "
                        "powers and authority as may be necessary to enable them to function as "
                        "institutions of self-government...",
                        "attr": "Constitution of India, Article 243W"},
                       {"t": "body", "html": "The operative word is 'may'. Article 243W permits states "
                        "to devolve the eighteen functions and does not require it. A state can list a "
                        "function in its municipal act while leaving the staff, money and decisions "
                        "with a state department or a development authority."}],
              "right": [{"t": "stats", "cols": 1, "cards": [
                  {"num": "4 of 18", "label": "functions fully under the autonomous control of urban local bodies, on average, in the CAG's 2024 performance audits across 18 states", "color": "red", "source": "CAG compendium, 2024, as reported by Business Standard, 22 October 2025"}]},
                        {"t": "body", "html": "The CAG found most functions performed with regular "
                         "interference from the state government or parastatal agencies, often with no "
                         "representation of the local body."},
                        {"t": "hbox", "color": "amber", "html": "When a programme says it will work "
                         "'through the municipality', first find out which agency in that town "
                         "actually holds the function."}]},
         ]},

        {"type": "content", "label": "Elections",
         "title": "Councils are elected for five years, through a State Election Commission",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Article 243R requires every seat in a municipality to "
                        "be filled by direct election from territorial wards. State law may add "
                        "non-voting experts in municipal administration, and voting members such as "
                        "the area's MPs and MLAs and the chairpersons of wards committees. The manner "
                        "of electing the chairperson or mayor is left entirely to state law."},
                       {"t": "body", "html": "Article 243U fixes the term at five years from the first "
                        "meeting. A council can be dissolved early only after a reasonable opportunity "
                        "of being heard, and a fresh election must then be completed within six months. "
                        "Elections must be completed before the term ends."}],
              "right": [{"t": "panel", "color": "cyan", "title": "Article 243ZA", "html":
                         "The superintendence, direction and control of electoral rolls and of all "
                         "municipal elections is vested in the State Election Commission set up under "
                         "Article 243K. The Election Commission of India has no role in municipal "
                         "polls. In many states the state government delimits wards and rotates reserved "
                         "seats, and this is where delays begin (section 04)."},
                        {"t": "hbox", "color": "amber", "html": "Article 243ZG bars courts from "
                         "interfering in municipal electoral matters except through an election "
                         "petition under state law."},
                        src("Articles 243R, 243U, 243ZA and 243ZG, Constitution of India.")]},
         ]},

        {"type": "content", "label": "Planning Committees",
         "title": "The planning committees are the least used part of the Amendment",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Article 243ZD requires a District Planning Committee in "
                        "every state to consolidate panchayat and municipal plans into a draft "
                        "development plan for the district. At least four-fifths of its members must "
                        "be elected from among district panchayat members and municipal councillors, "
                        "in proportion to rural and urban population."},
                       {"t": "body", "html": "Article 243ZE requires a Metropolitan Planning "
                        "Committee for every metropolitan area, with at least two-thirds of members "
                        "elected from councillors and panchayat chairpersons. Its plan must consider "
                        "spatial planning, sharing of water, integrated infrastructure and "
                        "environmental conservation, and the chairperson forwards it to the state."}],
              "right": [{"t": "table",
                         "head": ["Finding", "Source"],
                         "rows": [
                             ["Only 10 of the 18 audited states had constituted District Planning Committees, and only 3 had prepared annual district plans", "CAG, 2024, via Business Standard"],
                             ["Of 9 states required to form Metropolitan Planning Committees, only 3 had done so, and only 3 plans existed", "CAG, 2024, via Business Standard"],
                             ["Bengaluru's MPC was constituted in 2014, met three times by 2020 and had prepared no comprehensive plan", "CAG (2020), cited by PRS"]]},
                        {"t": "hbox", "color": "amber", "html": "The World Bank census-town study "
                         "recommends planning above the settlement level. These committees are the "
                         "constitutional place to do that."}]},
         ]},

        {"type": "content", "label": "Money Articles",
         "title": "Articles 243X and 243Y leave municipal money to state law",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Route in Article 243X", "What it means in practice"],
                        "rows": [
                            ["(a) authorise the municipality to levy and collect taxes, duties, tolls and fees", "Property tax, advertisement tax, profession tax in some states, fees and charges"],
                            ["(b) assign state-collected taxes", "Shares of stamp duty, entertainment tax and similar"],
                            ["(c) grants-in-aid from the state's Consolidated Fund", "Salaries, devolution grants, scheme shares"],
                            ["(d) constitute municipal funds", "Rules for crediting and withdrawing money"]]}],
              "right": [{"t": "body", "html": "Under Article 243Y, the state's finance commission "
                         "must recommend how state taxes are shared with municipalities, which taxes "
                         "they may levy or keep, what grants they receive and how their finances can "
                         "improve. The Governor must lay each report before the legislature with a "
                         "memorandum on action taken."},
                        {"t": "body", "html": "Union Finance Commissions have used their grants to "
                         "enforce this. The 15th Finance Commission said no local body grants would be "
                         "released after March 2024 to a state that had not constituted its finance "
                         "commission and acted on it. The 16th makes timely constitution of the State "
                         "Finance Commission an entry condition for all local body grants."},
                        src("Articles 243X and 243Y. PRS summaries of the 15th and 16th Finance Commission reports.")]},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Who runs a town, from councils to staff"},

        {"type": "content", "label": "Offices", "compact": True,
         "title": "Four offices in a municipality, chosen in four different ways",
         "blocks": [
             {"t": "table",
              "head": ["Office", "How it is filled", "Typical powers", "Answers to"],
              "rows": [
                  ["Councillor (corporator)", "Direct election from a ward (Article 243R)", "Votes on the budget, by-laws and resolutions, sits on committees, takes ward complaints", "Ward voters"],
                  ["Mayor or chairperson", "Set by state law. Elected directly by voters in some states, by councillors in others", "Presides over the council. Executive powers vary from ceremonial to a mayor-in-council", "Voters or the council"],
                  ["Commissioner or chief officer", "Appointed by the state government", "Executive head for staff, contracts, tax collection and budget preparation", "The state government, in practice"],
                  ["Standing and ward committees", "Elected from among councillors, and in wards committees as state law provides", "Financial sanction, scrutiny, ward-level works", "The council"]]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The CAG's 2024 audits found a directly elected mayor in "
                        "only five of the states examined. Everywhere else the mayor is chosen by and "
                        "from the council."}],
              "right": [{"t": "body", "html": "Bengaluru's 2024 law gives each new corporation a mayor "
                         "with a 30-month term and a government-appointed commissioner for two years "
                         "(PRS). Business Standard reported the CAG figure on 22 October 2025."}]},
         ]},

        {"type": "content", "label": "Executive Power",
         "title": "Executive power sits with the mayor in some cities and the commissioner in others",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Model", "Where it is used", "How it works"],
                        "rows": [
                            ["Commissioner system", "Delhi, Mumbai", "Executive power vests in the appointed commissioner. The council deliberates and sanctions"],
                            ["Mayor-in-council", "Kolkata. Madhya Pradesh corporations under the 2003 Act", "The mayor and up to 10 elected members exercise executive power (Kolkata). In Madhya Pradesh the council sanctions contracts up to a limit and appoints some staff"],
                            ["Apex authority over corporations", "Bengaluru, Greater Bengaluru Governance Act, 2024", "Up to seven corporations under an authority chaired by the Chief Minister"]]}],
              "right": [{"t": "body", "html": "The Second Administrative Reforms Commission (2007) "
                         "found that mayors in most states had only a peripheral role. It recommended "
                         "that executive power be exercised by the elected mayor and that large cities "
                         "could have a mayor's cabinet drawn from councillors."},
                        {"t": "body", "html": "The HPEC (2011) recommended a unified command under an "
                         "accountable mayor, with the commissioner acting as a city manager recruited "
                         "through a transparent selection process led by the mayor."},
                        {"t": "hbox", "color": "amber", "html": "In a commissioner city, a petition to "
                         "councillors moves slowly unless the commissioner's office acts on it. Map "
                         "both offices before planning any engagement."},
                        src("PRS, analysis of the Greater Bengaluru Governance Bill, 2024. HPEC, March 2011.")]},
         ]},

        {"type": "content", "label": "Missing Councils",
         "title": "Many municipalities have no elected council at all",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "61%", "label": "of 2,625 urban local bodies in 17 states audited by the CAG had no elected council (about 1,600)", "color": "red", "source": "CAG, 2024, via Business Standard"},
                 {"num": "6 months", "label": "the constitutional limit for holding an election after a council is dissolved (Article 243U)", "color": "cyan", "source": "Constitution of India"},
                 {"num": "April 2015", "label": "the last election to the Bruhat Bengaluru Mahanagara Palike before an administrator took charge at the end of its term", "color": "amber", "source": "PRS"}]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The CAG traced much of the delay to delimitation. Where "
                        "the state government draws ward boundaries and fixes reserved seats, the State "
                        "Election Commission cannot notify an election until the state has finished. "
                        "Administrators appointed by the state run the town meanwhile."}],
              "right": [{"t": "body", "html": "The Second Administrative Reforms Commission "
                         "recommended giving delimitation and reservation of wards to State Election "
                         "Commissions. PRS notes that Kerala, West Bengal and Maharashtra have done so, "
                         "while Andhra Pradesh, Haryana, Punjab, Rajasthan, Tamil Nadu and Uttar Pradesh "
                         "keep the power with the state government."}]},
         ]},

        {"type": "content", "label": "Staff",
         "title": "One municipal post in three is vacant",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Municipalities rarely decide their own staffing. The "
                        "CAG's 2024 audits found staff requirements assessed by state governments, "
                        "frequent underestimation, and one in three sanctioned posts vacant across the "
                        "18 states. Shimla Municipal Corporation needed 720 personnel and was "
                        "sanctioned 20 new posts."},
                       {"t": "body", "html": "A field study of Himachal Pradesh's urban employment "
                        "scheme found that Dharamshala Municipal Corporation had 69 permanent "
                        "employees, unchanged since it was upgraded to a corporation. Officials named "
                        "this as the reason few urban local bodies in the state were providing work."}],
              "right": [{"t": "term", "word": "Sanctioned post",
                         "def": "A post that the state government has approved for a municipality. "
                         "A vacancy rate is measured against sanctioned posts, so where the state "
                         "sanctions too few posts, as in Shimla, even a full roll would leave the work "
                         "understaffed."},
                        {"t": "hbox", "color": "amber", "html": "Swachh Bharat Mission-Urban reported "
                         "over 10 lakh municipal officials and staff trained, and 5.5 lakh sanitation "
                         "workers linked to welfare schemes, by October 2021."},
                        src("CAG, 2024, via Business Standard, 22 October 2025. Choragudi, Ideas for India, "
                            "21 March 2022. Cabinet release on SBM-U 2.0, October 2021.")]},
         ]},

        {"type": "content", "label": "Case: Bengaluru", "compact": True,
         "title": "Bengaluru replaced one corporation with an authority and up to seven corporations",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The Greater Bengaluru Governance Bill was introduced on "
                        "23 July 2024, referred to a select committee and passed by both houses in "
                        "March 2025. It replaces the BBMP Act, 2020, and came into effect on 15 May "
                        "2025. The Greater Bengaluru Authority it creates is chaired by the Chief Minister."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "The Authority is chaired by the Chief Minister, with an appointed Chief Commissioner as member secretary and MPs, MLAs, mayors and agency heads as members.",
                           "Each corporation needs more than 10 lakh people, more than 5,000 people per sq km and over ₹300 crore of local revenue.",
                           "Each corporation has up to 150 wards, a mayor and deputy mayor for 30 months, and a commissioner appointed for two years.",
                           "Each ward committee is chaired by the councillor with 14 other members."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Three-tier, four-tier, three-tier", "html":
                         "Under the Karnataka Municipal Corporations Act, 1976, Bengaluru had the BBMP, "
                         "ward committees and area sabhas. The BBMP Act, 2020 added zonal committees. "
                         "The 2024 law has the Authority, corporations and ward committees. The area "
                         "sabhas, where every voter of a polling area could propose priorities and "
                         "identify scheme beneficiaries, were removed by the select committee."},
                        src("PRS Legislative Research, analysis of the Greater Bengaluru Governance Bill, "
                            "2024. The Hindu, 15 May 2025, on the Act taking effect.")]},
         ]},

        {"type": "content", "label": "Case: Issues", "ultra-compact": True,
         "title": "The issues PRS raised about the Bengaluru law apply to most Indian cities",
         "blocks": [
             {"t": "table",
              "head": ["Provision", "What it does", "Why it matters for self-government"],
              "rows": [
                  ["Chief Minister heads the Authority and the Metropolitan Planning Committee", "Puts state ministers in charge of municipal coordination and planning", "Planning is a Twelfth Schedule function, and under Article 243ZE the MPC chair forwards the plan to the state, and here the chair is a state minister"],
                  ["State may dissolve a corporation", "For incompetence, abuse of power or failing to follow directions", "Elected councils can be removed by the government above them"],
                  ["Prior approvals", "Sale or long lease of property, contracts and many regulations need state or Authority approval", "Devolved powers that need permission are partly devolved"],
                  ["Property tax rates", "Set by the government in consultation with the Authority", "In Delhi, Kerala and Maharashtra, corporations set their own rates"],
                  ["Area sabhas removed", "Drops the neighbourhood assembly of voters", "Removes the most local channel of participation"],
                  ["Commissioner's contracts", "Need prior government approval. Under the 2020 Act they needed the mayor's approval", "Moves control from the elected mayor to the state"]]},
             src("PRS Legislative Research, Part B, Key Issues and Analysis, Greater Bengaluru Governance Bill, 2024."),
         ]},

        {"type": "content", "label": "Parastatals",
         "title": "Parastatal agencies do municipal work outside the municipality",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "In most large cities, development authorities, water "
                        "boards, transport corporations and housing boards perform Twelfth Schedule "
                        "functions under their own state laws. PRS notes that in Bengaluru most of these "
                        "public authorities, including the Bangalore Development Authority, were set up "
                        "before the 74th Amendment. They are accountable to state departments, and "
                        "elected councils are often divested of the functions as a result."},
                       {"t": "body", "html": "The CAG's 2020 audit of the 74th Amendment in Karnataka "
                        "recommended that such authorities be made accountable to urban local bodies. "
                        "The 2024 Bengaluru law gives its Authority power to direct them, without "
                        "changing whom they answer to."}],
              "right": [{"t": "panel", "color": "cyan", "title": "Special purpose vehicles", "html":
                         "The Smart Cities Mission ran its projects through special purpose vehicles "
                         "(SPVs) created for the mission in each city. After the mission's financial "
                         "closure on 31 March 2025, the Ministry advised that SPVs must finish all "
                         "ongoing projects by December 2025 (section 07). An SPV is one more executive "
                         "body beside the council, with its own board."},
                        {"t": "hbox", "color": "amber", "html": "As a practical test, for each service you "
                         "work on, write down which body signs the contract, which body collects the "
                         "charge and which body takes complaints. They are often three different bodies."},
                        src("PRS, GBG Bill analysis. ETV Bharat, 12 December 2025, quoting a MoHUA official.")]},
         ]},

        {"type": "content", "label": "Article 243T",
         "title": "Reservation puts women, Dalits and Adivasis on councils and in mayors' chairs",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "color": "cyan", "items": [
                  "Seats are reserved for Scheduled Castes and Scheduled Tribes in every municipality in proportion to their population in the municipal area, and may rotate between wards (243T(1)).",
                  "Not less than one-third of SC and ST seats are reserved for women of those communities (243T(2)).",
                  "Not less than one-third of all directly elected seats, counting those SC and ST women's seats, are reserved for women (243T(3)).",
                  "Chairperson offices are reserved for SCs, STs and women in the manner state law provides (243T(4)).",
                  "States may reserve seats and chairpersonships for backward classes (243T(6))."]}],
              "right": [{"t": "body", "html": "Article 243T(5) ends the SC and ST reservations at the "
                         "same time as reservations in Parliament and assemblies under Article 334. The "
                         "reservation of chairpersonships for women is outside that sunset clause."},
                        {"t": "body", "html": "Rotation means a ward reserved for a woman this term may "
                         "be general next term, so a sitting councillor may be unable to contest the "
                         "same ward again. The Constitution sets one-third as a floor, and a state law "
                         "may reserve more."},
                        {"t": "hbox", "color": "amber", "html": "Backward class reservation is not "
                         "required by Part IXA. Article 243T(6) only says that nothing in the Part "
                         "prevents a state from providing it, so its extent differs by state."},
                        src("Article 243T, Constitution of India.")]},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Municipal finance"},

        {"type": "content", "label": "Scale",
         "title": "Municipal corporations raise about 0.6 per cent of GDP",
         "blocks": [
             {"t": "stats", "cols": 4, "cards": [
                 {"num": "0.6%", "label": "of GDP: revenue receipts of 232 municipal corporations, 2023-24 (budget), the same as in 2019-20", "color": "cyan", "source": "RBI, Nov 2024"},
                 {"num": "₹1,70,722 cr", "label": "total revenue receipts of those corporations, 2023-24 (budget)", "color": "indigo", "source": "RBI, Nov 2024"},
                 {"num": "0.8%", "label": "of GDP: their budgeted capital spending, ₹2,39,403 crore, 61.5% of total spending", "color": "green", "source": "RBI, Nov 2024"},
                 {"num": "₹11,532", "label": "budgeted capital spending per person in those corporations, 2023-24", "color": "amber", "source": "RBI, Nov 2024"}]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The Reserve Bank's November 2024 <em>Report on "
                        "Municipal Finances</em> compares this with the Centre, which collects 9.2 per "
                        "cent of GDP, and the states, which collect 14.6 per cent. Municipal "
                        "corporations are India's largest and richest urban local bodies, so the "
                        "figure for all municipalities is lower per head."}],
              "right": [{"t": "body", "html": "The HPEC put total revenue of urban local bodies at "
                         "0.9 per cent of GDP in 2007-08, against 6 per cent for urban local "
                         "governments in South Africa and 7.4 per cent in Brazil. In the RBI's tables the "
                         "latest year is a budget estimate, so the capital figure is a plan."}]},
             src("RBI, <em>Report on Municipal Finances</em>, Chapter II, 13 November 2024. HPEC, "
                 "March 2011, paragraph 5.2.1."),
         ]},

        {"type": "content", "label": "Revenue Mix", "compact": True,
         "title": "Six-tenths of corporation revenue is their own, and transfers make up most of the rest",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "chart", "canvas": "ugRevMix", "type": "doughnut",
                        "title": "Revenue receipts of 232 municipal corporations, 2023-24 (budget), %",
                        "source": "RBI, Report on Municipal Finances, Chapter II, November 2024. 'Other' is the remainder after own revenue (61.9%) and transfers (31.2%)",
                        "data": {"labels": ["Own tax revenue", "Own non-tax revenue", "State transfers", "Central transfers", "Other receipts"],
                                 "datasets": [{"data": [30.0, 31.9, 28.7, 2.5, 6.9],
                                               "backgroundColor": ["#0369A1", "#38BDF8", "#B45309", "#F59E0B", "#94A3B8"]}]},
                        "options": {"plugins": {"legend": {"position": "right"}}}}],
              "right": [{"t": "body", "html": "Own revenue was 61.9 per cent of the corporations' "
                         "receipts in 2023-24, up from 59.0 per cent in 2019-20. Taxes were 30.0 per "
                         "cent and non-tax revenue, mostly fees and user charges, about 32 per cent. "
                         "State transfers were 28.7 per cent and central transfers 2.5 per cent."},
                        {"t": "body", "html": "Looking at all urban local bodies, the HPEC found "
                         "the own-revenue share falling from 63 per cent in "
                         "2002-03 to 53 per cent in 2007-08, with some reduced to near-departments of "
                         "the state whose salaries the state paid."},
                        {"t": "hbox", "color": "amber", "html": "A high own-revenue share can mean "
                         "strong taxes or tiny transfers. Read the share beside the total."}]},
         ]},

        {"type": "content", "label": "Property Tax", "compact": True,
         "title": "Property tax is the main municipal tax, and India collects very little of it",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "chart", "canvas": "ugPropTax", "type": "bar",
                        "title": "Property tax of 232 municipal corporations, ₹ crore",
                        "source": "RBI, Report on Municipal Finances, Chapter II, November 2024",
                        "data": {"labels": ["2019-20", "2023-24 (budget)"],
                                 "datasets": [{"label": "₹ crore", "data": [18389, 32450],
                                               "backgroundColor": ["#94A3B8", "#0369A1"]}]},
                        "options": {"plugins": {"legend": {"display": False}},
                                    "scales": {"y": {"min": 0}}}}],
              "right": [{"t": "body", "html": "Property tax was 19.0 per cent of the corporations' "
                         "revenue receipts in 2023-24 and over 60 per cent of their own tax revenue. "
                         "The RBI's 2022 report put it at 0.09 to 0.11 per cent of GDP over 2017-18 to "
                         "2019-20, much lower than in OECD countries."},
                        {"t": "bullets", "color": "cyan", "items": [
                            "Undervaluation of properties.",
                            "Incomplete property registers.",
                            "Policy gaps.",
                            "Weak administration and collection."]},
                        src("Causes as listed in RBI, <em>Report on Municipal Finances</em>, Chapter II, 10 November 2022.")]},
         ]},

        {"type": "content", "label": "Assessment", "compact": True,
         "title": "How property tax is assessed, and what reforms have tried",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Reform", "What it changes", "Source"],
                        "rows": [
                            ["Self-assessment", "Owners declare area, use and type using published rates. Bengaluru introduced an optional scheme in 2000 with six land value zones", "HPEC Box 5.5"],
                            ["Area-based system", "Tax on the constructed area of a building, with rates by location and type", "HPEC recommendations"],
                            ["Coverage and collection targets", "JNNURM required over 85% of properties on the register and over 90% collection", "HPEC Box 1.5, JNNURM reforms"],
                            ["Vacant land tax", "0.5 to 1% of the ready-reckoner capital value of vacant land", "HPEC paragraph 5.2.20"],
                            ["Floor rates", "States notify minimum rates and raise collection with GSDP growth", "15th Finance Commission"],
                            ["Mapping", "Satellite imagery and geo-coding to find unassessed buildings", "RBI, 2022"]]}],
              "right": [{"t": "body", "html": "Bengaluru's self-assessment scheme classified "
                         "properties into zones using the guidance values of the Department of Stamps "
                         "and Registration. Tax yield rose 33 per cent in 2001. About a third of the "
                         "increase came from revaluation, and some taxpayers paid 2.5 times more than "
                         "before, yet compliance costs fell because the method was simple."},
                        {"t": "body", "html": "The 15th Finance Commission made a floor rate and growth "
                         "in collection an entry condition for urban grants after 2021-22. The 16th "
                         "links part of its local body performance grant to minimum growth in own "
                         "source revenue."},
                        src("HPEC, March 2011, Box 5.5 citing NIUA (2009). PRS summaries of the 15th and 16th FC reports.")]},
         ]},

        {"type": "content", "label": "User Charges",
         "title": "Water and waste services are paid for mostly from other money",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Non-tax revenue was about 30 per cent of municipal "
                        "corporation revenue in the RBI's 2022 report, dominated by fees and user "
                        "charges. Property tax and grants pay for most of what remains of service "
                        "costs."},
                       {"t": "body", "html": "AMRUT 2.0 made this an explicit reform. States are to "
                        "meet 20 per cent of water demand from recycled water, reduce non-revenue "
                        "water to under 20 per cent and reform property tax, user charges and credit "
                        "worthiness, with incentives for municipalities that do. JNNURM had earlier "
                        "asked for full recovery of operation and maintenance costs of water supply and "
                        "solid waste management through user charges."}],
              "right": [{"t": "term", "word": "Non-revenue water",
                         "def": "Water that a utility produces but does not bill, through leakage, theft, "
                         "unmetered public use and billing errors. AMRUT 2.0 set a target of under "
                         "20 per cent."},
                        {"t": "panel", "color": "amber", "title": "The equity question", "html":
                         "A charge that recovers costs raises bills for households that already "
                         "have a connection, while those without one gain nothing until they are "
                         "connected. Lifeline tariffs, a low price for the first block of consumption, "
                         "are one answer. Connecting households comes first, which is what AMRUT 2.0's "
                         "2.68 crore tap target is about."},
                        src("RBI 2022. Cabinet release on AMRUT 2.0, 12 October 2021. HPEC, JNNURM mandatory reforms.")]},
         ]},

        {"type": "content", "label": "Spending", "compact": True,
         "title": "What the spending figures show, and why RBI and CAG figures differ",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Measure", "Value", "Source"],
                        "rows": [
                            ["Revenue to capital spending ratio, municipal corporations, 2017-18", "2.4", "RBI, 2022"],
                            ["Same ratio, Centre, 2017-18", "7.1", "RBI, 2022"],
                            ["Same ratio, states, 2017-18", "5.9", "RBI, 2022"],
                            ["Capital share of corporation spending, 2017-18 to 2019-20 (budget)", "about 30% rising to 42%", "RBI, 2022"],
                            ["Capital share, 2023-24 (budget)", "61.5%", "RBI, 2024"],
                            ["Share of ULB funds spent on development, 18 states", "29%", "CAG, 2024, via Business Standard"],
                            ["Gap between resources and expenditure, 11 states", "42%", "CAG, 2024, via Business Standard"]]}],
              "right": [{"t": "body", "html": "The RBI's numbers say corporations spend a larger "
                         "share on capital works than the Centre or states. The CAG's numbers say "
                         "most local bodies spend little on development and cannot cover their costs. "
                         "Both are true, because they cover different bodies and because the RBI "
                         "series uses budget estimates."},
                        {"t": "body", "html": "The HPEC projected ₹19.9 lakh crore of operation and "
                         "maintenance needs for new and old assets over twenty years, and asked that "
                         "policy focus on the services that flow from assets as well as on building "
                         "them. A mission that builds an asset hands its upkeep to the municipality."},
                        src("RBI, <em>Report on Municipal Finances</em>, 2022 and 2024. Business Standard, 22 October 2025, on the CAG compendium.")]},
         ]},

        {"type": "content", "label": "Accounts and Audit",
         "title": "Without published accounts, no money from the Finance Commission",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Article 243Z lets state law provide for the "
                        "maintenance and audit of municipal accounts. JNNURM's mandatory reforms "
                        "required accrual-based double-entry accounting and annual balance sheets, "
                        "because cash books record receipts and payments but not what a town owns, "
                        "owes or is owed."},
                       {"t": "body", "html": "The 15th Finance Commission made the publication of "
                        "provisional and audited accounts in the public domain an entry condition for "
                        "local body grants. The 16th Finance Commission repeats it as one of three "
                        "entry conditions for every local body grant from 2026-27."}],
              "right": [{"t": "panel", "color": "cyan", "title": "Why accounts come before bonds", "html":
                         "A lender or a credit rating agency needs audited accounts that show what a "
                         "municipality owns, owes and collects. Pune's 2017 bond carried AA+ ratings "
                         "from CARE and India Ratings and pledged property tax for repayment."},
                        {"t": "hbox", "color": "green", "html": "For a researcher, the published annual "
                         "accounts and budget books of a municipality are the first documents to "
                         "collect. Ask for actual figures as well as budget estimates."},
                        src("Article 243Z. HPEC Box 1.5, JNNURM reforms. PRS summaries of the 15th and 16th FC. ORF, Ramanath Jha, 3 September 2019.")]},
         ]},

        {"type": "content", "label": "Dependence",
         "title": "Revenue autonomy depends on rules states set",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "A municipality's own revenue depends on three state "
                        "decisions. These are which taxes it may levy under Article 243X, who sets "
                        "the rates, and which agency collects. The HPEC recommended abolishing octroi and entry tax "
                        "in all states and giving municipalities a constitutionally fixed share of "
                        "state taxes on goods and services."},
                       {"t": "body", "html": "PRS notes that in Delhi, Kerala and Maharashtra "
                        "municipal corporations set their own property tax rates, while the 2024 "
                        "Bengaluru law gives the rate-setting power to the state government. Karnataka's "
                        "2020 performance audit found that state control of rates had constrained "
                        "urban local bodies."}],
              "right": [{"t": "table",
                         "head": ["Measure of dependence", "Value"],
                         "rows": [
                             ["Transfers in corporation receipts, 2017-18 to 2019-20", "34.8% to 39.1%"],
                             ["Central transfers in corporation receipts, same years", "under 5%"],
                             ["State transfers, 2023-24 (budget)", "28.7%"],
                             ["Grants from the Centre to corporations, 2022-23 (revised)", "₹14,731 crore"],
                             ["Grants from states to corporations, 2022-23 (revised)", "₹41,872 crore"]]},
                        src("RBI, <em>Report on Municipal Finances</em>, 2022 and 2024. PRS, GBG Bill analysis. HPEC recommendations.")]},
         ]},

        {"type": "content", "label": "RBI Advice",
         "title": "What the Reserve Bank recommends",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "2022 report", "blocks": [
                  {"t": "bullets", "color": "cyan", "items": [
                      "Extend property tax coverage, revise rates regularly and improve assessment.",
                      "Use satellite imagery and geo-coding to find and value properties.",
                      "State governments to help smaller corporations build institutional capacity.",
                      "Develop a municipal bond market. Bonds were under a tenth of corporation borrowing, and gross borrowing was under 0.05 per cent of GDP."]}]}],
              "right": [{"t": "panel", "color": "green", "title": "2024 report", "blocks": [
                  {"t": "bullets", "color": "green", "items": [
                      "State-specific strategies for municipal revenue, through reform of local taxes, better enforcement and new non-tax sources.",
                      "Timely, adequate and rule-based transfers from higher tiers of government.",
                      "Training in financial management to build capacity."]}]},
                        {"t": "body", "html": "Both reports cover only municipal corporations, 201 in "
                         "2022 and 232 in 2024, because consistent budget data were not available for "
                         "smaller municipalities. The RBI dropped 20 of 221 corporations from the 2022 "
                         "sample for incomplete data."},
                        src("RBI, <em>Report on Municipal Finances</em>, Chapter II, 10 November 2022 and 13 November 2024.")]},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Transfers, Finance Commissions and borrowing"},

        {"type": "content", "label": "15th Finance Commission",
         "title": "The 15th Finance Commission gave urban local bodies ₹1,21,055 crore for 2021-26",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Grant, 2021-26", "₹ crore"],
                        "rows": [
                            ["Rural local bodies", "2,36,805"],
                            ["Urban local bodies", "1,21,055"],
                            ["Health grants through local governments", "70,051"],
                            ["Incubation of new cities", "8,000"],
                            ["Shared municipal services", "450"],
                            ["Total for local governments", "4,36,361"]]},
                       {"t": "body", "cls": "sm", "html": "Grants other than health were distributed "
                        "among states by population (90 per cent weight) and area (10 per cent)."}],
              "right": [{"t": "body", "html": "Two entry conditions applied. Local bodies had to "
                         "publish provisional and audited accounts. For urban bodies after 2021-22, the "
                         "state also had to notify minimum floor rates of property tax and improve "
                         "collection. A third rule withheld all local body grants after March 2024 from "
                         "any state that had not constituted its State Finance Commission and acted on "
                         "its recommendations."},
                        {"t": "body", "html": "The Commission also set aside ₹8,000 crore for the "
                         "incubation of new cities, outside the ₹1,21,055 crore for existing urban "
                         "local bodies."},
                        src("PRS, Report Summary, Report of the 15th Finance Commission for 2021-26.")]},
         ]},

        {"type": "content", "label": "16th Finance Commission", "compact": True,
         "title": "The 16th Finance Commission nearly triples urban grants for 2026-31",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Urban local body grant, 2026-31", "₹ crore", "Conditions"],
                        "rows": [
                            ["Basic grant", "2,32,125", "Half untied. Half tied to sanitation and solid waste and/or water management"],
                            ["Performance grant", "58,032", "State part for minimum transfers to local bodies from own resources. Local body part for minimum own-revenue growth"],
                            ["Special infrastructure component", "56,100", "Wastewater systems in cities of 10 to 40 lakh people (Census 2011)"],
                            ["Urbanisation premium", "10,000", "One-time, for merging peri-urban villages into adjoining ULBs and a rural-to-urban transition policy"],
                            ["Total urban", "3,56,257", "Entry conditions apply"]]}],
              "right": [{"t": "body", "html": "The report was tabled on 1 February 2026 and covers "
                         "2026-27 to 2030-31. Rural local bodies get ₹4,35,236 crore, local governments "
                         "₹7,91,493 crore in all, and states keep 41 per cent of the divisible pool."},
                        {"t": "body", "html": "Three entry conditions apply to all local body grants: "
                         "local bodies constituted as the Constitution requires, a test that a town "
                         "run by an administrator may fail, provisional and audited accounts published, and the "
                         "State Finance Commission constituted on time."},
                        {"t": "hbox", "color": "cyan", "html": "Eligible cities for the special "
                         "infrastructure component include Pune, Jaipur, Lucknow, Kanpur, Nagpur, "
                         "Indore, Bhopal, Visakhapatnam, Patna and Vadodara."},
                        src("PRS Legislative Research, Report Summary, Report of the 16th Finance Commission for 2026-31, 1 February 2026.")]},
         ]},

        {"type": "content", "label": "Comparison", "compact": True,
         "title": "Local body grants, 15th and 16th Finance Commissions",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "chart", "canvas": "ugFcGrants", "type": "bar",
                        "title": "Finance Commission grants to local bodies, ₹ crore, five-year totals",
                        "source": "PRS Report Summaries of the 15th (2021-26) and 16th (2026-31) Finance Commission reports. 15th FC rural and urban figures exclude health grants of ₹70,051 crore",
                        "data": {"labels": ["15th FC, 2021-26", "16th FC, 2026-31"],
                                 "datasets": [{"label": "Rural local bodies", "data": [236805, 435236], "backgroundColor": "#047857"},
                                              {"label": "Urban local bodies", "data": [121055, 356257], "backgroundColor": "#0369A1"}]},
                        "options": {"scales": {"y": {"min": 0, "title": {"display": True, "text": "₹ crore"}}}}}],
              "right": [{"t": "body", "html": "Urban grants rise from ₹1,21,055 crore to ₹3,56,257 "
                         "crore across the two awards, and the urban share of the rural and urban total "
                         "from about a third to about 45 per cent."},
                        {"t": "body", "html": "Spread over five years and more than 4,000 statutory "
                         "towns, the money is still small beside investment needs (slide on "
                         "investment needs below). Its weight lies in the conditions, which push states "
                         "to hold elections, publish accounts and set up finance commissions."},
                        {"t": "hbox", "color": "amber", "html": "Janaagraha's analysis, reported by "
                         "Business Standard, puts the untied share of urban grants at 52 per cent "
                         "under the 16th FC against 21 per cent under the 15th, counting the 15th "
                         "FC's urban total differently from the table here."}]},
         ]},

        {"type": "content", "label": "State Finance Commissions",
         "title": "State Finance Commissions decide most of the money municipalities receive",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "State transfers were 28.7 per cent of corporation "
                        "receipts in 2023-24, more than ten times central transfers. Those transfers "
                        "are meant to follow a State Finance Commission's recommendations under Article "
                        "243Y: a share of state taxes, assigned taxes, grants-in-aid and measures to "
                        "improve municipal finances."},
                       {"t": "body", "html": "Because Union Finance Commission grants now depend on "
                        "timely State Finance Commissions, states that had let them lapse have reason "
                        "to constitute them. A report that is constituted, written, tabled and then "
                        "ignored still meets the letter of the condition."}],
              "right": [{"t": "panel", "color": "cyan", "title": "Questions to ask about a state's SFC", "blocks": [
                  {"t": "bullets", "color": "cyan", "items": [
                      "When was the latest State Finance Commission constituted and for which period?",
                      "Was its report laid before the legislature with an action taken memorandum, as Article 243Y(2) requires?",
                      "What share of state tax revenue did it recommend for municipalities, and what share was transferred?",
                      "Are transfers formula-based and predictable, or released scheme by scheme?",
                      "Does the formula reward own-revenue effort, or penalise it?"]}]},
                        src("RBI, Nov 2024. Article 243Y. PRS summaries of the 15th and 16th Finance Commission reports.")]},
         ]},

        {"type": "content", "label": "Municipal Bonds", "compact": True,
         "title": "Municipal bonds remain tiny: ₹4,204 crore outstanding in March 2024",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "₹4,204 cr", "label": "municipal bonds outstanding on 31 March 2024, 0.01% of GDP", "color": "cyan", "source": "RBI, Nov 2024"},
                 {"num": "₹694 cr", "label": "raised through green municipal bonds over four years", "color": "green", "source": "RBI, Nov 2024"},
                 {"num": "₹100 cr", "label": "Union incentive proposed for a single issue above ₹1,000 crore", "color": "amber", "source": "Budget speech, 1 Feb 2026"}]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "SEBI's regulations for issue and listing of debt "
                        "securities by municipalities date from 15 July 2015. Pune Municipal "
                        "Corporation issued ₹200 crore in 2017 at 7.59 per cent for ten years, a revenue "
                        "bond with property tax pledged, rated AA+ by CARE and India Ratings, "
                        "oversubscribed six times, with no state guarantee, to part-fund a 24x7 water "
                        "supply project."}],
              "right": [{"t": "body", "html": "The 2026-27 Budget speech kept the AMRUT incentive for "
                         "issues up to ₹200 crore for small and medium towns. Borrowing from financial "
                         "institutions was ₹13,364 crore in 2023-24, 5.2 per cent of total corporation "
                         "receipts, revenue and capital together, so banks and state agencies still lend more than bond markets."}]},
             src("RBI, Nov 2024. SEBI regulations page, 15 July 2015. Ramanath Jha, ORF Expert Speak, 3 "
                 "September 2019. Union Budget 2026-27, speech paragraph 46."),
         ]},

        {"type": "content", "label": "Challenge Funds",
         "title": "The Union is moving urban money into competitive funds",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Urban Challenge Fund (Budget 2025-26)", "html":
                         "A ₹1 lakh crore fund for 'Cities as Growth Hubs', 'Creative Redevelopment of "
                         "Cities' and 'Water and Sanitation'. It finances up to 25 per cent of the cost "
                         "of bankable projects, on condition that at least 50 per cent comes from bonds, "
                         "bank loans and public-private partnerships. ₹10,000 crore was proposed for "
                         "2025-26."},
                       {"t": "panel", "color": "green", "title": "City Economic Regions (Budget 2026-27)", "html":
                         "Mapping of city economic regions by growth drivers, with ₹5,000 crore per "
                         "region over five years, given through a challenge mode with reform-cum-results "
                         "based financing. The speech names Tier II and Tier III cities and temple "
                         "towns."}],
              "right": [{"t": "body", "html": "A challenge fund rewards the cities that can prepare "
                         "bankable projects and raise half the money elsewhere. Those are cities with "
                         "audited accounts, a credit rating and staff who can write a detailed project "
                         "report."},
                        {"t": "body", "html": "Small municipalities, which the CAG found short of staff "
                         "and often without councils, are least able to compete. A practitioner "
                         "working with a small town should check whether it has the project "
                         "preparation support that competitive funds assume."},
                        src("Union Budget 2025-26, speech paragraphs 57 to 59. Union Budget 2026-27, speech paragraph 39.")]},
         ]},

        {"type": "content", "label": "Investment Needs", "compact": True,
         "title": "Estimates of what Indian cities need to invest",
         "blocks": [
             {"t": "table",
              "head": ["Estimate", "Period", "Amount", "Notes"],
              "rows": [
                  ["HPEC, all urban investment", "2012 to 2031", "₹39.2 lakh crore at 2009-10 prices", "₹34.1 lakh crore asset creation, ₹4.1 lakh crore renewal including slums, ₹1 lakh crore capacity building"],
                  ["HPEC, eight infrastructure sectors", "2012 to 2031", "₹31 lakh crore", "Water, sewerage, solid waste, storm drains, roads, urban transport, street lights, traffic support"],
                  ["HPEC, operation and maintenance", "2012 to 2031", "₹19.9 lakh crore", "For new and old assets"],
                  ["HPEC target for annual investment", "2011-12 to 2031-32", "0.7% of GDP rising to 1.1%", "Plus a Union commitment of 0.25% of GDP a year"],
                  ["Janaagraha, based on a World Bank report", "2021 to 2036", "₹61.4 lakh crore", "About 1.2% of GDP a year"]]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Set against these numbers, 16th Finance Commission urban "
                        "grants of ₹3.56 lakh crore over five years are a small fraction of need. The "
                        "rest has to come from state budgets, municipal revenue and borrowing."}],
              "right": [{"t": "body", "html": "The HPEC's maintenance estimate of ₹19.9 lakh crore is "
                         "about half its capital estimate. It proposed that the Union fund 0.25 per cent "
                         "of GDP a year for twenty years, against 0.10 per cent at the time."}]},
             src("HPEC, March 2011, Executive Summary and Chapter 3. Business Standard, 15 February 2026, reporting Janaagraha."),
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "The urban missions"},

        {"type": "content", "label": "Overview", "ultra-compact": True,
         "title": "Five Union urban schemes a practitioner meets in 2026",
         "blocks": [
             {"t": "table",
              "head": ["Scheme", "Approved", "Money", "Main target", "Status in October 2026"],
              "rows": [
                  ["AMRUT 2.0", "Cabinet, 12 October 2021, for 2021-22 to 2025-26", "₹2,77,000 crore indicative, central share ₹76,760 crore", "Tap connections in all 4,378 statutory towns, sewerage or septage in 500 AMRUT cities", "Extended to March 2027 (Standing Committee, August 2026)"],
                  ["Smart Cities Mission", "2015, 100 cities chosen in four rounds, January 2016 to June 2018", "₹48,000 crore central budget", "Area-based projects through city SPVs", "Financially closed 31 March 2025, remaining projects due by December 2025"],
                  ["PMAY-Urban 2.0", "Cabinet, August 2024, five years", "₹10 lakh crore investment, ₹2.30 lakh crore government assistance", "1 crore houses for EWS, LIG and MIG families", "Running, together with the completion of PMAY-U 1.0"],
                  ["SBM-Urban 2.0", "Launched 1 October 2021, for 2021-22 to 2025-26", "₹1,41,600 crore, central share ₹36,465 crore", "Garbage-free towns, ODF+ for all statutory towns, used water in towns under 1 lakh", "Approved to 2025-26. Check the Ministry for any extension"],
                  ["PM SVANidhi", "Union scheme of the Ministry of Housing and Urban Affairs", "Loans through banks", "Credit for street vendors", "Over 68 lakh vendors benefited by February 2025, revamp announced"]]},
             src("Cabinet releases on AMRUT 2.0 and SBM-U 2.0 (October 2021). PIB backgrounder on SCM, December 2024. "
                 "PIB release on PMAY-U 2.0, August 2024. Union Budget 2025-26 speech, paragraph 50. PRS summary of the "
                 "Standing Committee report, 4 August 2026."),
         ]},

        {"type": "content", "label": "AMRUT 2.0", "compact": True,
         "title": "AMRUT 2.0 aims at a tap in every urban household",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The first AMRUT, launched in June 2015 for 500 cities, "
                        "reported 1.1 crore household tap connections and 85 lakh sewer or septage "
                        "connections by October 2021, with 1,210 MLD of a planned 6,000 MLD sewage "
                        "treatment capacity built and 1,700 flooding points eliminated."},
                       {"t": "body", "html": "AMRUT 2.0 extended the water goal to every statutory "
                        "town, with targets of 2.68 crore tap connections and 2.64 crore sewer or "
                        "septage connections. Each city prepares a water balance plan and a city water "
                        "action plan. These are summed into a State Water Action Plan, which the "
                        "Ministry approves, and central funds are released in three tranches against "
                        "it."}],
              "right": [{"t": "panel", "color": "cyan", "title": "Conditions and reforms", "blocks": [
                  {"t": "bullets", "color": "cyan", "items": [
                      "Projects worth 10 per cent of the total in cities above 10 lakh people to be done through public-private partnership.",
                      "20 per cent of water demand to be met from recycled water.",
                      "Non-revenue water to be cut below 20 per cent.",
                      "Reforms of property tax, user charges and credit worthiness, rewarded with incentives.",
                      "Pey Jal Survekshan, a competitive ranking of city water services."]}]},
                        src("Cabinet release on AMRUT 2.0, 12 October 2021 (pmindia.gov.in).")]},
         ]},

        {"type": "content", "label": "AMRUT Progress", "compact": True,
         "title": "Five years in, a sixth of AMRUT 2.0 sewerage projects were complete",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "chart", "canvas": "ugAmrut", "type": "bar",
                        "title": "AMRUT 2.0 sewerage and septage projects, as reported in August 2026",
                        "source": "PRS summary of the Standing Committee on Housing and Urban Affairs report on sewerage and septage coverage, presented 4 August 2026",
                        "data": {"labels": ["Planned", "Under implementation", "Completed"],
                                 "datasets": [{"label": "Projects", "data": [594, 398, 104],
                                               "backgroundColor": ["#94A3B8", "#F59E0B", "#047857"]}]},
                        "options": {"plugins": {"legend": {"display": False}}, "scales": {"y": {"min": 0}}}}],
              "right": [{"t": "body", "html": "The Standing Committee found ₹22,763 crore of ₹66,060 "
                         "crore committed central assistance released, 34 per cent. Of 11.3 crore urban "
                         "households, 3.5 crore were connected to sewers and 2.9 crore relied on septic "
                         "tanks or other septage systems, and 68 per cent of surveyed septic tanks were "
                         "not properly lined."},
                        {"t": "body", "html": "Estimates of how much wastewater is treated differ: 28 "
                         "per cent in a 2022 NITI Aayog report, 43 per cent by the Ministry. Of 22,891 "
                         "MLD of treatment capacity, 6,013 MLD of treated water was reused. The "
                         "Committee also recorded that unsafe manual cleaning of sewers and septic tanks "
                         "continues despite the legal ban."},
                        {"t": "hbox", "color": "amber", "html": "AMRUT 2.0 has been extended to March "
                         "2027."}]},
         ]},

        {"type": "content", "label": "Smart Cities", "compact": True,
         "title": "The Smart Cities Mission closed with most projects built and 18 cities fully done",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "chart", "canvas": "ugScm", "type": "doughnut",
                        "title": "Smart Cities Mission projects, 1 December 2025",
                        "source": "ETV Bharat, 12 December 2025, quoting Ministry of Housing and Urban Affairs data: 8,064 projects worth ₹1,64,811 crore",
                        "data": {"labels": ["Completed (7,741)", "Ongoing (323)"],
                                 "datasets": [{"data": [7741, 323], "backgroundColor": ["#047857", "#F59E0B"]}]},
                        "options": {"plugins": {"legend": {"position": "bottom"}}}}],
              "right": [{"t": "body", "html": "The mission chose 100 cities in four rounds between "
                         "January 2016 and June 2018, gave each five years and extended the deadline to "
                         "June 2024 and then to 31 March 2025, its financial closure. By December 2024 "
                         "the Union had released ₹46,419 crore of its ₹48,000 crore budget."},
                        {"t": "body", "html": "By 1 December 2025, 7,741 projects worth ₹1,55,386 "
                         "crore were complete and 323 worth ₹9,425 crore were ongoing. In March 2025 "
                         "only 18 cities had completed every project, among them Agra, Varanasi, "
                         "Madurai, Coimbatore, Udaipur, Pune, Surat and Vadodara."},
                        src("PIB backgrounder, December 2024. Down To Earth, 2025, citing the mission dashboard and PIB. ETV Bharat, 12 December 2025.")]},
         ]},

        {"type": "content", "label": "Smart Cities Lessons",
         "title": "What the Smart Cities Mission leaves municipalities to manage",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The mission's method was area-based development: "
                        "improve a selected part of each city to serve as a model. Its reported outputs "
                        "include operational Integrated Command and Control Centres in all 100 cities, "
                        "more than 83,000 CCTV cameras, 1,700 km of 'smart roads', 23,000 public "
                        "bicycles, 1,500 buses, 9,400 smart classrooms and 35,000 affordable housing "
                        "units built by 23 cities."},
                       {"t": "body", "html": "The Ministry listed the causes of delay reported by "
                        "states as legal issues, clearances from other departments, land acquisition, "
                        "construction in hilly areas, a shortage of vendors in small and medium cities, "
                        "centralised decision-making in a few cities, and under-use of the command "
                        "centres."}],
              "right": [{"t": "panel", "color": "amber", "title": "Questions for the years after", "blocks": [
                  {"t": "bullets", "color": "amber", "items": [
                      "Who pays to run a command centre, its cameras and its software now that the mission has closed?",
                      "Were SPV assets transferred to the municipality, with staff to run them?",
                      "Did area-based projects serve the parts of the city where most poor households live?",
                      "Are the 199 PPP projects worth ₹9,200 crore monitored by anyone in the council?"]}]},
                        src("PIB backgrounder on SCM, December 2024. ETV Bharat, 12 December 2025. Down To Earth, 2025.")]},
         ]},

        {"type": "content", "label": "PMAY-Urban 2.0", "ultra-compact": True,
         "title": "PMAY-Urban 2.0 has four routes to a house",
         "blocks": [
             {"t": "table",
              "head": ["Vertical", "For whom", "Assistance"],
              "rows": [
                  ["Beneficiary-Led Construction (BLC)", "EWS families with their own vacant land. States may give land rights (pattas) to the landless", "₹2.50 lakh per house in AHP and BLC, shared by Centre and state"],
                  ["Affordable Housing in Partnership (AHP)", "EWS families buying houses built with states, cities, public or private agencies", "As above, plus a Technology Innovation Grant of ₹1,000 per sq m"],
                  ["Affordable Rental Housing (ARH)", "Working women, industrial workers, urban migrants and others who rent", "Uses vacant government-funded houses or new construction, grant of ₹3,000 per sq m for new technology"],
                  ["Interest Subsidy Scheme (ISS)", "EWS, LIG and MIG families taking loans up to ₹25 lakh for a house worth up to ₹35 lakh", "4% subsidy on the first ₹8 lakh for up to 12 years, maximum ₹1.80 lakh in five yearly instalments"]]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Eligibility is by annual household income: EWS up to ₹3 "
                        "lakh, LIG ₹3 to 6 lakh, MIG ₹6 to 9 lakh, with no pucca house anywhere in "
                        "India. The central to state sharing is 60:40 for most states, 90:10 for the "
                        "north-eastern and Himalayan states and UTs with legislatures, and 100:0 for "
                        "UTs without legislatures."}],
              "right": [{"t": "body", "html": "The scheme names as special focus groups sanitation "
                         "workers (safai karmi), street vendors identified under PM SVANidhi, artisans "
                         "under PM-Vishwakarma, anganwadi workers, building and construction workers "
                         "and residents of slums and chawls."}]},
             src("PIB release on PMAY-U 2.0 (PRID 2043927) and PIB backgrounder, 10 August 2024. PMAY-U 2.0 Operational Guidelines."),
         ]},

        {"type": "content", "label": "PMAY Progress", "compact": True,
         "title": "One crore houses completed under PMAY-Urban, and fewer occupied",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "chart", "canvas": "ugPmay", "type": "bar",
                        "title": "PMAY-U and PMAY-U 2.0 houses, lakh, as on 28 September 2026",
                        "source": "Ministry of Housing and Urban Affairs, 'Achievement under PMAY-U & PMAY-U 2.0', pmay-urban.gov.in, as on 28 September 2026",
                        "data": {"labels": ["Sanctioned", "Grounded", "Completed", "Occupied"],
                                 "datasets": [{"label": "Lakh houses", "data": [125.31, 119.26, 100.48, 98.05],
                                               "backgroundColor": ["#94A3B8", "#38BDF8", "#0369A1", "#047857"]}]},
                        "options": {"plugins": {"legend": {"display": False}}, "scales": {"y": {"min": 0}}}}],
              "right": [{"t": "body", "html": "By 28 September 2026 the two phases together had "
                         "sanctioned 125.31 lakh houses with committed investment of ₹9.01 lakh crore. "
                         "Of ₹2,08,720 crore of committed central assistance, ₹1,82,128 crore had been "
                         "released. In August 2024, before the second phase began, the Ministry had "
                         "reported 1.18 crore sanctioned and 85.5 lakh completed."},
                        {"t": "body", "html": "The Ministry reports completion and occupation "
                         "separately because a finished house is not always lived in. Section 08 "
                         "reports an Indian study of why households offered new houses on the edge of "
                         "a city did not stay."},
                        {"t": "hbox", "color": "amber", "html": "The 2.43 lakh gap between completed "
                         "and occupied houses is small in percentage terms and large in households."}]},
         ]},

        {"type": "content", "label": "SBM-Urban 2.0", "compact": True,
         "title": "Swachh Bharat Mission-Urban 2.0 moved from toilets to waste and used water",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Item", "SBM-U 2.0 (approved October 2021)"],
                        "rows": [
                            ["Outlay", "₹1,41,600 crore for 2021-22 to 2025-26, central share ₹36,465 crore, 2.5 times the ₹14,623 crore central share of the first phase (whose total outlay was ₹62,009 crore)"],
                            ["Centre to state share", "25:75 in cities over 10 lakh, 33:67 for 1 to 10 lakh, 50:50 under 1 lakh"],
                            ["Sanitation", "All statutory towns at least ODF+, towns under 1 lakh ODF++, 3.5 lakh more toilets"],
                            ["Solid waste", "Every town at least 3-star garbage free, 100% scientific management of municipal solid waste"],
                            ["Legacy waste", "Remediate all dumpsites, freeing 14,000 acres under 15 crore tonnes of old waste"],
                            ["Used water", "Systems in every town under 1 lakh people, which AMRUT does not cover"]]}],
              "right": [{"t": "body", "html": "At approval the Ministry reported 70 lakh household, "
                         "community and public toilets built, urban India declared open defecation free "
                         "in 2019, waste processing up from 18 per cent in 2014 to 70 per cent, "
                         "door-to-door collection in 97 per cent of wards and source segregation in 85 "
                         "per cent. These are the Ministry's own figures."},
                        {"t": "body", "html": "Swachh Survekshan, the annual ranking begun in 2016, "
                         "covers over 4,000 urban local bodies and had collected over 7 crore citizen "
                         "responses by 2021. Read what a ranking rewards before treating it as a "
                         "measure of the service residents receive."},
                        src("Cabinet release on SBM-U 2.0, 12 October 2021 (pmindia.gov.in).")]},
         ]},

        {"type": "content", "label": "Street Vendor Credit",
         "title": "PM SVANidhi lends to street vendors, and the Act protects where they sell",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "PM SVANidhi (Prime Minister Street Vendor's AtmaNirbhar "
                        "Nidhi) is a Union scheme of bank loans for street vendors. The Union Budget of February 2025 said the scheme had benefited "
                        "more than 68 lakh street vendors 'giving them respite from high-interest "
                        "informal sector loans', and announced a revamp with larger bank loans, "
                        "UPI-linked credit cards with a ₹30,000 limit and capacity building."},
                       {"t": "body", "html": "The same speech announced a scheme for the "
                        "socio-economic upliftment of urban workers, and PMAY-U 2.0 gives vendors "
                        "identified under PM SVANidhi priority for housing."}],
              "right": [{"t": "panel", "color": "amber", "title": "Credit does not settle space", "html":
                         "A loan helps a vendor buy stock. It does not protect the pitch where the "
                         "stock is sold. That protection comes from a survey and a certificate of "
                         "vending under the Street Vendors Act, 2014, administered by a Town Vending "
                         "Committee (section 08). Practitioners working with vendors should check "
                         "both whether loans were received and whether the town has completed its "
                         "survey and issued certificates."},
                        src("Union Budget 2025-26, speech paragraphs 49 and 50. PMAY-U 2.0 Operational Guidelines, paragraph 3.4.")]},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Slums, housing and street vendors"},

        {"type": "content", "label": "Definitions",
         "title": "What a slum is in the schemes, and what a municipality is asked to do about it",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "term", "word": "Slum (PMAY-U 2.0)",
                        "def": "A compact area of at least 300 population or about 60 to 70 households "
                        "of poorly built congested tenements, in unhygienic environment usually with "
                        "inadequate infrastructure and lacking in proper sanitary and drinking water "
                        "facilities."},
                       {"t": "body", "html": "The definition sets a minimum size and describes "
                        "conditions. It says nothing about legal status, land ownership or how long "
                        "residents have lived there, which are settled by state slum laws and by "
                        "each town's own lists."}],
              "right": [{"t": "panel", "color": "cyan", "title": "Tenable and untenable", "html":
                         "PMAY-U 2.0 distinguishes tenable slums, which can be redeveloped where they "
                         "stand, from untenable ones, such as those on hazardous land, which may be "
                         "resettled. In-situ redevelopment of tenable slums on public land runs through "
                         "the AHP vertical. A tenable slum whose households build under BLC must be "
                         "delisted after its infrastructure deficit is met by the state or town."},
                        {"t": "hbox", "color": "amber", "html": "'Slum improvement and upgradation' and "
                         "'urban poverty alleviation' are items 10 and 11 of the Twelfth Schedule."},
                        src("PMAY-U 2.0 Operational Guidelines, definitions and paragraphs 5.1.14 and 5.2.")]},
         ]},

        {"type": "content", "label": "Slum Shares", "compact": True,
         "title": "Slum shares in the 2001 Census ranged from a fifth to over half in big cities",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "chart", "canvas": "ugSlum", "type": "bar",
                        "title": "Slum population as per cent of city population, selected million-plus cities, Census 2001",
                        "source": "Slum Census of India 2001, as tabulated in HPEC (2011), Table A19",
                        "data": {"labels": ["Greater Mumbai", "Faridabad", "Meerut", "Nagpur", "Kolkata", "Thane", "Ludhiana", "Surat", "Pune", "Chennai", "Delhi", "Hyderabad", "Ahmedabad", "Bangalore", "Patna"],
                                 "datasets": [{"label": "% in slums",
                                               "data": [54.1, 46.5, 44.1, 35.9, 32.5, 27.8, 22.5, 20.9, 19.4, 18.9, 18.7, 17.2, 13.5, 10.0, 0.3],
                                               "backgroundColor": "#B45309"}]},
                        "options": {"indexAxis": "y", "plugins": {"legend": {"display": False}},
                                    "scales": {"x": {"min": 0, "max": 60}}}}],
              "right": [{"t": "body", "html": "Patna's figure of 0.3 per cent is far below every "
                         "other city in the table. A figure that low should be checked against how "
                         "settlements were listed in that city before it is used for comparison."},
                        {"t": "body", "html": "The HPEC assumed that 25 per cent of the urban "
                         "population lives in slums, which gave ₹8.5 lakh crore of its investment "
                         "estimate for slum residents at universal service standards."},
                        {"t": "hbox", "color": "amber", "html": "These are 2001 figures, shown because "
                         "they are the city series this course could verify. Use the Census 2011 slum "
                         "tables and, when released, Census 2027 houselisting data for current work."}]},
         ]},

        {"type": "content", "label": "Approaches", "compact": True,
         "title": "Four ways to deal with a slum, and their risks",
         "blocks": [
             {"t": "table",
              "head": ["Approach", "What happens", "Route in PMAY-U 2.0", "Main risk"],
              "rows": [
                  ["Upgrading in place", "Water, drains, paving, toilets and lights brought into the settlement. Houses stay", "Infrastructure from state or town funds, with BLC for houses", "Without tenure, residents may still face eviction later"],
                  ["In-situ redevelopment", "Low-rise settlement replaced by flats on the same land", "AHP, on government or ULB land", "Upkeep costs of multi-storey buildings fall on residents"],
                  ["Resettlement", "Households moved to a new site", "For untenable slums, with land as the state provides", "Distance from work, schools and networks"],
                  ["Rental housing", "Rooms or flats for rent, for migrants and workers", "ARH", "Rents and eligibility rules may not fit short-stay workers"]]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Most programmes combine these. Upgrading keeps "
                        "people where their work is, and resettlement moves them away from it, so the "
                        "order in which the approaches are tried matters."}],
              "right": [{"t": "body", "html": "The next slide reports a long-run test of what "
                         "resettlement does to the people who receive a new house."}]},
         ]},

        {"type": "content", "label": "Evidence: Relocation",
         "title": "A housing lottery in an Indian city brought better houses and no economic gain",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Sharon Barnhardt, Erica Field and Rohini Pande studied "
                        "a lottery that offered slum residents of an Indian city improved housing on the "
                        "city's periphery. Because the houses were allotted by lottery, winners and "
                        "losers can be compared as in an experiment."},
                       {"t": "body", "html": "Fourteen years later, winners reported better housing but "
                        "no change in tenure security, family income or human capital. They reported "
                        "more isolation from family and caste networks and less informal insurance."}],
              "right": [{"t": "stats", "cols": 2, "cards": [
                  {"num": "34%", "label": "of winners never took up the subsidised house", "color": "amber", "source": "Barnhardt, Field and Pande, AEJ: Applied, 2017"},
                  {"num": "32%", "label": "of winners eventually left it", "color": "red", "source": "Same study"}]},
                        {"t": "quote", "text": "Our results suggest negligible long-run economic value of "
                         "this expensive public program and point to the importance of considering "
                         "social networks in housing programs for the poor.",
                         "attr": "Barnhardt, Field and Pande, 'Moving to Opportunity or Isolation?', <em>American Economic Journal: Applied Economics</em> 9(1), 2017"}]},
         ]},

        {"type": "content", "label": "Why Slums Persist",
         "title": "Economists who study slums describe a poverty trap",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Benjamin Marx, Thomas Stoker and Tavneet Suri reviewed "
                        "the economics of slums in the developing world in 2013. They argue that "
                        "poverty in contemporary slums resembles a poverty trap. Three mechanisms keep "
                        "residents from using the economic opportunities of being near a city. They are "
                        "thresholds in human capital, inertia in investment, and a 'policy trap'."},
                       {"t": "body", "html": "They also test the competing view that slums are a "
                        "transitory feature of fast-growing economies, by examining economic growth, "
                        "urban growth and slum growth, and whether living standards improve within "
                        "slums and across generations. They discuss why standard policy approaches "
                        "have often failed to slow the growth of slums."}],
              "right": [{"t": "panel", "color": "cyan", "title": "What this means for municipal practice", "blocks": [
                  {"t": "bullets", "color": "cyan", "items": [
                      "Service connections (water, toilets, lights) can be extended without first deciding title, as upgrading programmes do.",
                      "Ask what tenure a scheme confers. The relocation study found no gain in tenure security even for lottery winners.",
                      "Resettlement that breaks networks can cancel the gain from a better house (previous slide).",
                      "Count renters as well as owners when listing households for any scheme."]}]},
                        src("Marx, Stoker and Suri, 'The Economics of Slums in the Developing World', <em>Journal of Economic Perspectives</em> 27(4), 2013.")]},
         ]},

        {"type": "content", "label": "Street Vendors Act", "ultra-compact": True,
         "title": "The Street Vendors Act, 2014 protects vendors once a town has surveyed them",
         "blocks": [
             {"t": "table",
              "head": ["Section", "Rule"],
              "rows": [
                  ["3(1)", "The Town Vending Committee surveys all existing street vendors, and repeats the survey at least once every five years"],
                  ["3(2)", "Vendors found in the survey are accommodated in vending zones on a norm of two and a half per cent of the population of the ward, zone, town or city"],
                  ["3(3)", "No street vendor shall be evicted or relocated until the survey is complete and certificates of vending are issued to all"],
                  ["4", "Every surveyed vendor aged 14 or more gets a certificate of vending. Earlier licences count as certificates"],
                  ["18(3)", "No relocation or eviction without thirty days' notice"],
                  ["22", "The Town Vending Committee is chaired by the commissioner. At least 40 per cent of members are vendors elected by vendors, one-third of them women, and at least 10 per cent are from NGOs and community organisations"],
                  ["27", "A vendor trading within the certificate's terms cannot be prevented by police or any other authority"]]},
             {"t": "body", "cls": "sm", "html": "The Act is No. 7 of 2014. It received the President's "
              "assent on 4 March 2014 and was published in the Gazette of India on 5 March 2014. "
              "Text from the Gazette copy held by PRS Legislative Research."},
         ]},

        {"type": "content", "label": "Implementation",
         "title": "Why the Street Vendors Act is hard to implement",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The Act makes the survey the gate to every protection. "
                        "Until the Town Vending Committee has surveyed and certified vendors, section "
                        "3(3) bars eviction, but vendors also hold no certificate to show a police "
                        "officer. A town that never completes the survey leaves both the protection "
                        "and the regulation unused."},
                       {"t": "body", "html": "When the Bill was before Parliament, PRS noted that "
                        "street vending was then regulated under state municipal laws, and that "
                        "Parliament's power to legislate depended on whether the Bill was read as "
                        "about vendors' rights (Concurrent List) or municipal zoning (State List)."}],
              "right": [{"t": "panel", "color": "amber", "title": "Gaps PRS identified in the Bill", "blocks": [
                  {"t": "bullets", "color": "amber", "items": [
                      "No principles for issuing certificates, allocating vending zones or deciding the number of vendors per zone.",
                      "No requirement to consult stakeholders on the street vending plan, which the local authority prepares every five years.",
                      "The Standing Committee asked for railway land to be covered, for scheme provisions to be written into the law and for the Town Vending Committee to be consulted on the plan."]}]},
                        src("PRS Legislative Research, Bill page and analysis, Street Vendors Bill, 2012. Street Vendors Act, 2014, sections 3, 21 and 22.")]},
         ]},

        {"type": "content", "label": "Renting",
         "title": "Housing policy is built around owners, and many urban residents rent",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Three of PMAY-U 2.0's four verticals help a household "
                        "own a house. The fourth, Affordable Rental Housing, is for working women, "
                        "industrial workers, urban migrants and others who need to rent. It uses vacant "
                        "government-funded houses and new construction."},
                       {"t": "body", "html": "Census 2027's houselisting asks every household about "
                        "ownership status, the number of rooms and the number of married couples living "
                        "in them. Those three answers, by ward, show where renting and crowding are "
                        "concentrated."}],
              "right": [{"t": "panel", "color": "cyan", "title": "Finance for low-income buyers", "html":
                         "PMAY-U 2.0 raised the corpus of the Credit Risk Guarantee Fund Trust from "
                         "₹1,000 crore to ₹3,000 crore to guarantee housing loans to EWS and LIG "
                         "borrowers, and moved its management from the National Housing Bank to the "
                         "National Credit Guarantee Trustee Company."},
                        {"t": "hbox", "color": "amber", "html": "A housing count that leaves out "
                         "tenants, hostels and workers living at worksites will undercount need in "
                         "every growing town."},
                        src("PIB release on PMAY-U 2.0 (PRID 2043927). DCO Maharashtra, Census 2027 deck, 30 April 2026.")]},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Urban work and the job guarantee debate"},

        {"type": "content", "label": "Unemployment", "compact": True,
         "title": "Urban unemployment is highest among young women",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "chart", "canvas": "ugUr", "type": "bar",
                        "title": "Unemployment rate, urban, usual status, 2025 (%)",
                        "source": "MoSPI, PLFS annual 2025 (calendar year), All India, urban. Retrieved through the MoSPI data API",
                        "data": {"labels": ["Age 15 and above", "Age 15 to 29"],
                                 "datasets": [{"label": "Men", "data": [4.2, 11.8], "backgroundColor": "#0369A1"},
                                              {"label": "Women", "data": [6.4, 18.9], "backgroundColor": "#B45309"},
                                              {"label": "All persons", "data": [4.8, 13.6], "backgroundColor": "#94A3B8"}]},
                        "options": {"scales": {"y": {"min": 0, "max": 20}}}}],
              "right": [{"t": "body", "html": "In 2025, 4.8 per cent of the urban labour force aged 15 "
                         "and above was unemployed by usual status, against 2.4 per cent in rural "
                         "areas. Among urban 15 to 29 year olds the rate was 13.6 per cent, and among "
                         "young urban women 18.9 per cent."},
                        {"t": "body", "html": "An unemployment rate counts only people without work "
                         "who are seeking it. Irregular and low-paid work, which an employment "
                         "guarantee is designed to supplement, does not show up in it, so the case "
                         "for an urban guarantee rests on more than open unemployment."},
                        {"t": "hbox", "color": "amber", "html": "Urban women who are not in the labour "
                         "force at all, 72 per cent of those aged 15 and above, do not appear in any "
                         "unemployment rate."}]},
         ]},

        {"type": "content", "label": "The Proposal", "compact": True,
         "title": "Jean Drèze's DUET proposal makes public institutions the employers of urban workers",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "In September 2020, after months of lockdown, Jean Drèze "
                        "proposed Decentralised Urban Employment and Training (DUET). He pointed to a "
                        "crisis of urban informal employment and to the poor maintenance of schools, "
                        "colleges, health centres, bus stands, parks and offices, which would need "
                        "cleaning and repair as they reopened."},
                       {"t": "flow", "steps": [
                           "State issues job stamps to approved public institutions",
                           "Institution arranges work and hires from registered workers",
                           "Placement agency assigns workers to limit collusion",
                           "State pays the minimum wage straight to the worker's account"]}],
              "right": [{"t": "panel", "color": "cyan", "title": "Design features", "blocks": [
                  {"t": "bullets", "color": "cyan", "items": [
                      "All urban residents over 18 may register, with registration drives in low-income neighbourhoods.",
                      "Skilled and unskilled work, with an unskilled assistant attached to each skilled worker for training.",
                      "A list of permissible works broad enough to be useful, and narrow enough not to displace existing jobs.",
                      "An independent municipal authority to monitor, inspect, audit and evaluate the works.",
                      "A path to a guarantee, with the municipality as employer of last resort for anyone who finds no work with other employers."]}]},
                        src("Jean Drèze, 'DUET: A proposal for an urban work programme', Ideas for India, 9 September 2020.")]},
         ]},

        {"type": "content", "label": "State Schemes", "compact": True,
         "title": "States that have legislated or run urban employment schemes",
         "blocks": [
             {"t": "table",
              "head": ["State", "Scheme", "Entitlement", "Source"],
              "rows": [
                  ["Himachal Pradesh", "Mukhyamantri Shahri Ajeevika Guarantee Yojana, from May 2020", "120 days of wage employment a year for every household in a ULB area, at ₹300 a day, unemployment allowance if no work in 15 days, skill training after 30 days", "Choragudi, Ideas for India, 2022"],
                  ["Rajasthan", "Indira Gandhi Urban Employment Guarantee Scheme, made a right in the Minimum Guaranteed Income Bill, 2023", "At least 125 days a year for every adult in urban areas, minimum wages paid weekly or within a fortnight, work within 15 days or an unemployment allowance, worksite within the ward, adjoining wards or 5 km", "Bill No. 26 of 2023, sections 3 to 6"],
                  ["Kerala, Odisha, Jharkhand", "State urban employment schemes", "Similar schemes in operation in 2022", "Choragudi, 2022"],
                  ["Tamil Nadu", "Urban employment scheme", "Announced by 2022", "Choragudi, 2022"]]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Himachal Pradesh's scheme had an annual outlay of ₹100 "
                        "crore, cut to ₹5 crore for 2022-23. Choragudi wrote that 'the meagre outlay of "
                        "Rs. 5 crore this year renders the promise of employment guarantee hollow.'"}],
              "right": [{"t": "body", "html": "Rajasthan's 2023 Bill gives the right to every adult, "
                         "where Himachal Pradesh and the rural guarantee give it to a household. The "
                         "executive officer of the local body is the implementing officer in towns."}]},
         ]},

        {"type": "content", "label": "Himachal on the Ground",
         "title": "What Himachal Pradesh's urban scheme looked like to its workers",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Krishna Priya Choragudi interviewed workers in "
                        "Dharamshala in person and in Palampur, Baijnath-Piprola and Shimla by phone "
                        "in late 2021. Works included kuhls (hill irrigation channels), retaining walls "
                        "near roads and streams, levelling and clearing of public land. Some projects "
                        "abandoned by contractors on risky terrain were finished by scheme workers."},
                       {"t": "body", "html": "Women were the majority of applicants. Of 7,593 approved "
                        "applications by 20 February 2022, nearly half came from Scheduled Caste and "
                        "Scheduled Tribe workers. Women told her that contractors preferred men and "
                        "migrants willing to take lower wages."}],
              "right": [{"t": "panel", "color": "amber", "title": "Implementation problems", "blocks": [
                  {"t": "bullets", "color": "amber", "items": [
                      "Few urban local bodies were actively providing work. Officials cited capacity, and Dharamshala had 69 permanent staff.",
                      "Some applicants had received no work a year after applying.",
                      "Most who worked got fewer than 60 days and waited one to two months for full wages.",
                      "None of the workers interviewed knew of the unemployment allowance or the skill training provisions."]}]},
                        src("Krishna Priya Choragudi, 'Examining Himachal's urban employment guarantee', Ideas for India, 21 March 2022.")]},
         ]},

        {"type": "content", "label": "Design Choices", "compact": True,
         "title": "Design choices for an urban employment guarantee",
         "blocks": [
             {"t": "table",
              "head": ["Choice", "Options seen in Indian practice", "What follows"],
              "rows": [
                  ["Who holds the right", "Household (Himachal Pradesh, rural guarantee) or each adult (Rajasthan Bill)", "An individual right gives women a claim of their own"],
                  ["Who provides work", "The municipality alone, or many public institutions (DUET)", "Many employers spread the administrative load beyond thin municipal staff"],
                  ["Days", "100, 120 or 125 days a year", "More days only matter if work is actually offered"],
                  ["Wage", "State minimum wage, paid weekly or within a fortnight", "Delays, as in Himachal Pradesh, drive workers away"],
                  ["Works", "Maintenance of public buildings and spaces, water channels, green works, sanitation", "A list that is too narrow produces no work. One that is too broad displaces regular jobs"],
                  ["Money", "State budget, with no Union share", "The budget can be cut in a single year"]]},
             {"t": "body", "cls": "sm", "html": "Rows draw on Drèze (2020), Choragudi (2022) and the "
              "Rajasthan Minimum Guaranteed Income Bill, 2023. The right-hand column is this course's "
              "reading of the design trade-offs."},
         ]},

        {"type": "content", "label": "The Rural Guarantee",
         "title": "The change to the rural guarantee alters the urban debate",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The Viksit Bharat Guarantee for Rozgar and Ajeevika "
                        "Mission (Gramin) Act, 2025 came into force on 1 July 2026, and section 37 repealed the Mahatma Gandhi National Rural "
                        "Employment Guarantee Act, 2005 from that date. Ashwini Kulkarni's reading of the Bill "
                        "identifies four changes that matter for towns and their edges."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Workdays per household rise from 100 to 125 a year.",
                           "Work is suspended for 60 days during sowing and harvest, on dates the state sets.",
                           "The Centre funds 60 per cent of total cost and the state 40 per cent, or 90 and 10 in the North Eastern and Himalayan States (section 22). Under the 2005 Act the Centre paid all unskilled wages.",
                           "The Act applies only to rural areas that the Centre notifies."]}],
              "right": [{"t": "panel", "color": "amber", "title": "Why urban practitioners should care", "html":
                         "Census towns and outgrowths are rural in law. Whether they are notified "
                         "under the new Act decides whether their residents have any statutory "
                         "work guarantee. Peri-urban villages merged into municipalities, which the 16th "
                         "Finance Commission's urbanisation premium encourages, leave the rural "
                         "guarantee altogether and enter towns that have none unless the state "
                         "provides one."},
                        src("The VB-G RAM G Act, 2025 (Act 36 of 2025), ss. 22 and 37, and S.O. 2382(E) of 11 May 2026; Ashwini Kulkarni, 'VB-G RAM G Bill, 2025: Decoding the new rural employment scheme', Ideas for India, 7 January 2026. PRS, 16th FC summary.")]},
         ]},

        {"type": "content", "label": "Who Employs", "compact": True,
         "title": "Most urban workers work in small proprietary firms, which is where any guarantee competes",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "chart", "canvas": "ugEnt", "type": "bar",
                        "title": "Urban workers by type of enterprise, usual status, 2025 (%)",
                        "source": "MoSPI, PLFS annual 2025 (calendar year), urban, persons. Retrieved through the MoSPI data API",
                        "data": {"labels": ["Proprietary and partnership", "Public or private ltd company", "Govt, local body, PSU", "Employer's household", "Trust or non-profit", "Other"],
                                 "datasets": [{"label": "% of urban workers", "data": [66.0, 17.2, 10.1, 3.5, 1.5, 1.6],
                                               "backgroundColor": "#0369A1"}]},
                        "options": {"indexAxis": "y", "plugins": {"legend": {"display": False}}, "scales": {"x": {"min": 0, "max": 70}}}}],
              "right": [{"t": "body", "html": "Two-thirds of urban workers are in proprietary and "
                         "partnership enterprises. A public works guarantee paying the state minimum "
                         "wage would compete with these employers for the same workers."},
                        {"t": "body", "html": "Whether that competition lifts wages at the bottom or "
                         "costs small firms their workers is an open question. The Indian urban schemes "
                         "described here have been too small and too unevenly run to answer it."},
                        {"t": "hbox", "color": "amber", "html": "'Other' combines cooperative "
                         "societies (0.4%), autonomous bodies (0.2%) and other types (1.0%)."}]},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Heat, floods and the municipal role"},

        {"type": "content", "label": "Defining Heat",
         "title": "How a heatwave is declared, and how Ahmedabad turned it into alerts",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["IMD rule", "Heatwave declared when"],
                        "rows": [
                            ["Normal maximum below 40°C", "The maximum is 5°C or more above the 30-year normal"],
                            ["Normal maximum above 40°C", "The maximum is 4°C or more above normal"],
                            ["Any station", "The maximum is above 45°C, whatever the normal"]]},
                       src("India Meteorological Department rule as given in Azhar et al., <em>PLoS ONE</em> 9(3), 2014.")],
              "right": [{"t": "table",
                         "head": ["Ahmedabad alert", "Forecast maximum"],
                         "rows": [
                             ["Yellow, hot day advisory", "41.1°C to 43°C"],
                             ["Orange, heat alert day", "43.1°C to 44.9°C"],
                             ["Red, extreme heat alert day", "45°C or more"]]},
                        {"t": "body", "html": "Azhar and colleagues argue that the IMD definitions may "
                         "underestimate the health impact of heat, because the thresholds do not "
                         "account for observed effects on health. A city alert system can set its own "
                         "thresholds from local health data."},
                        src("Ahmedabad Heat Action Plan, 2019 update, easy read version (NRDC and AMC).")]},
         ]},

        {"type": "content", "label": "Ahmedabad 2010", "compact": True,
         "title": "The May 2010 heatwave in Ahmedabad killed 1,344 more people than usual",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "chart", "canvas": "ugHeat", "type": "bar",
                        "title": "All-cause deaths in Ahmedabad, 1 to 31 May",
                        "source": "Azhar et al., 'Heat-Related Mortality in India: Excess All-Cause Mortality Associated with the 2010 Ahmedabad Heat Wave', PLoS ONE 9(3): e91831, 2014",
                        "data": {"labels": ["Reference (mean of May 2009 and May 2011)", "May 2010"],
                                 "datasets": [{"label": "Deaths", "data": [3118, 4462],
                                               "backgroundColor": ["#94A3B8", "#B91C1C"]}]},
                        "options": {"plugins": {"legend": {"display": False}}, "scales": {"y": {"min": 0}}}}],
              "right": [{"t": "body", "html": "Temperatures reached 46.8°C. All-cause deaths in May "
                         "2010 were 4,462 against a reference of 3,118, an excess of 1,344 or 43.1 per "
                         "cent. In the hottest week, 19 to 25 May, mortality rate ratios were 1.76 and "
                         "2.12 against comparison weeks."},
                        {"t": "body", "html": "The study used all-cause death counts provided by the "
                         "Ahmedabad Municipal Corporation. Registration of births and deaths is item 16 "
                         "of the Twelfth Schedule, so the evidence for heat planning came from a "
                         "municipal function."},
                        {"t": "hbox", "color": "amber", "html": "Deaths rose with temperature even "
                         "in a city used to heat, which is why the authors argued for early warning."}]},
         ]},

        {"type": "content", "label": "Heat Action Plan",
         "title": "Ahmedabad's Heat Action Plan, the first in India",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "After the 2010 heatwave, the Ahmedabad Municipal "
                        "Corporation and partners prepared India's first Heat Action Plan in 2013 and "
                        "update it periodically. The plan works through four strategies."},
                       {"t": "bullets", "color": "cyan", "items": [
                           "Public awareness and outreach from March to June, by text message, radio, social media and person-to-person contact with vulnerable groups.",
                           "An early warning system that passes IMD forecasts to agencies, hospitals, emergency responders, community groups and media.",
                           "Training of primary medical officers, paramedics and community health staff to recognise and treat heat illness.",
                           "Reducing exposure, including a city-wide cool roofs programme with mandatory, voluntary and low-income housing measures."]}],
              "right": [{"t": "stats", "cols": 1, "cards": [
                  {"num": "2,380", "label": "deaths estimated avoided in 2014 and 2015, compared with a 2007 to 2010 baseline", "color": "green", "source": "Hess et al., 2018, as summarised in the 2019 plan"}]},
                        {"t": "body", "html": "Cool roofs can keep indoor temperatures 2 to 5°C lower "
                         "than traditional roofs, according to the plan. Most of its measures, "
                         "such as messaging, coordination with hospitals, drinking water and first aid "
                         "at anganwadis, and building rules, are municipal tasks."},
                        src("Ahmedabad Heat Action Plan 2019 update, easy read version. Hess et al., <em>Journal of Environmental and Public Health</em>, 2018.")]},
         ]},

        {"type": "content", "label": "Drains",
         "title": "Storm water drains covered less than a fifth of urban roads",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "stats", "cols": 2, "cards": [
                  {"num": "under 20%", "label": "of the urban road network covered by storm water drains", "color": "red", "source": "MoUD (2010), cited in HPEC Box 2.4"},
                  {"num": "1,700", "label": "flooding points reported eliminated under the first AMRUT, 2015 to 2021", "color": "green", "source": "Cabinet release on AMRUT 2.0, 2021"}]},
                       {"t": "body", "html": "The HPEC's service norm was a storm water drain network "
                        "covering the full length of every road on both sides, in all cities. It costed "
                        "water supply, sewerage, solid waste and storm water drains together at ₹8 lakh "
                        "crore, 20 per cent of its ₹39.2 lakh crore estimate for 2012 to 2031."}],
              "right": [{"t": "body", "html": "When rain exceeds what drains can carry, the "
                         "governance questions concern what happens to the water next, including "
                         "whether rivers and lakes have room for it, whether low-lying land has been "
                         "built over, and whether warnings reach people in time."},
                        {"t": "panel", "color": "cyan", "title": "Who holds the pieces", "html":
                         "Storm water drains are among the eight sectors the HPEC costed for urban "
                         "local bodies. Reservoirs and tanks may be run by a state department, as "
                         "Chennai's were in 2015 (next slide). Land use in large cities may sit with "
                         "development authorities, as in Bengaluru (section 04). Flooding crosses all "
                         "of these boundaries."},
                        src("HPEC, March 2011, Executive Summary paragraph 16, Box 2.4 and service norms. Cabinet release on AMRUT 2.0, 12 October 2021.")]},
         ]},

        {"type": "content", "label": "Chennai 2015",
         "title": "Chennai, December 2015: the CAG called the floods a man-made disaster",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "The CAG's report, 'Flood management and response in "
                        "Chennai and its suburban areas', was submitted to the Tamil Nadu government in "
                        "March 2016 and tabled in the Assembly in July 2018. The state's Water "
                        "Resources Department drew most of its criticism."},
                       {"t": "bullets", "color": "red", "items": [
                           "On 1 December 2015 at 2 pm, with Chembarambakkam tank holding 3.377 tmc and room for 0.268 tmc more, discharge was raised from 12,000 to 20,960 cusecs. The CAG said 12,000 could have been held for six more hours.",
                           "Discharge of 29,000 cusecs ran for 21 hours on 1 and 2 December into the Adyar river.",
                           "The CAG found the increase was made to save patta land that had been allowed in the tank's foreshore area from submergence.",
                           "The tank's operating rules had not been revised for 23 years, and the Adyar had not been desilted."]}],
              "right": [{"t": "panel", "color": "amber", "title": "The lesson for urban governance", "html":
                         "The decisions the CAG examined in Chennai were taken by a state department "
                         "that manages a reservoir, about land in a tank's foreshore. Flood planning "
                         "that stops at municipal limits, or at municipal departments, will miss where "
                         "much of the risk is created."},
                        src("The Hindu, 'CAG terms 2015 Chennai floods a man-made disaster', July 2018, reporting the CAG report.")]},
         ]},

        {"type": "content", "label": "Preparing", "compact": True,
         "title": "Steps a municipality can take before the next heatwave or flood",
         "blocks": [
             {"t": "flow", "steps": [
                 "Map who is exposed, by ward",
                 "Set alert thresholds from local data",
                 "Name the agency for each action",
                 "Rehearse before the season",
                 "Count deaths and damage afterwards"]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Heat", "blocks": [
                  {"t": "bullets", "color": "cyan", "items": [
                      "Use ward-level houselisting data (roof material, rooms, drinking water) from Census 2027 to find crowded homes with hot roofs and no water on the premises.",
                      "Adopt colour-coded alerts tied to IMD forecasts, as Ahmedabad's yellow, orange and red alerts are.",
                      "Agree in advance with hospitals and primary health staff who does what on a red alert day.",
                      "Track all-cause deaths from the municipal death register each summer, the measure Azhar et al. used."]}]}],
              "right": [{"t": "panel", "color": "amber", "title": "Floods", "blocks": [
                  {"t": "bullets", "color": "amber", "items": [
                      "List every reservoir, tank and lake that drains through the town and the agency that operates it, as the Chennai audit shows.",
                      "Ask whether operating rules for those reservoirs have been revised, which the CAG found had not happened for 23 years at Chembarambakkam.",
                      "Use AMRUT 2.0's city water balance plan to include storm water and water bodies in the same plan as supply.",
                      "Remediate legacy dumpsites, an SBM-U 2.0 target, and keep drains clear of solid waste."]}]},
                        src("Ahmedabad Heat Action Plan 2019. Azhar et al., 2014. The Hindu on the CAG Chennai report, July 2018. Cabinet releases on AMRUT 2.0 and SBM-U 2.0. DCO Maharashtra, Census 2027 questions.")]},
         ]},

        {"type": "content", "label": "Climate and Budgets", "compact": True,
         "title": "Money for climate risk in a municipal budget",
         "blocks": [
             {"t": "table",
              "head": ["Source", "What it can pay for", "Amount and rule"],
              "rows": [
                  ["16th FC basic grants, tied half", "Sanitation and solid waste, water management", "Half of ₹2,32,125 crore, 2026-31"],
                  ["16th FC special infrastructure component", "Wastewater systems in cities of 10 to 40 lakh", "₹56,100 crore"],
                  ["Disaster management grants", "State disaster response and mitigation funds", "Corpus of ₹2,04,401 crore, Centre's share ₹1,55,916 crore. Sharing 90:10 for north-eastern and Himalayan states, 75:25 elsewhere"],
                  ["AMRUT 2.0", "Water bodies, recycled water, green spaces, drainage", "Indicative ₹2,77,000 crore over the mission"],
                  ["Green municipal bonds", "Projects with environmental benefits", "₹694 crore raised over four years to March 2024"],
                  ["Municipal own funds", "Heat alerts, drinking water points, cool roofs, desilting", "Low-cost measures from the town's own budget"]]},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Heat plans need little capital and depend on "
                        "coordination. Flood protection needs large capital and depends on control of "
                        "land and water bodies outside the municipality's hands."}],
              "right": [{"t": "body", "html": "Item 8 of the Twelfth Schedule, urban forestry and "
                         "protection of the environment, is the constitutional basis for municipal "
                         "climate work."}]},
             src("PRS, 16th FC summary. Cabinet release on AMRUT 2.0. RBI, Nov 2024."),
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Participation and what research has found"},

        {"type": "content", "label": "Ward Committees",
         "title": "Wards committees and area sabhas give residents a voice below the council",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "body", "html": "Article 243S requires wards committees in every "
                        "municipality of three lakh people or more. A committee may cover one ward or "
                        "several, the councillor of each ward in it is a member, and where it covers "
                        "several wards the members elect one of those councillors as chairperson. The "
                        "state law decides everything else."},
                       {"t": "body", "html": "JNNURM required states to enact a Community Participation "
                        "Law and a Public Disclosure Law as mandatory reforms. Under such laws, area "
                        "sabhas bring together every voter of a polling area. Bengaluru had them under "
                        "the 1976 and 2020 Acts, where area sabhas proposed development priorities and "
                        "identified beneficiaries for schemes."}],
              "right": [{"t": "panel", "color": "amber", "title": "What the 2024 Bengaluru law kept and dropped", "html":
                         "Each ward committee is chaired by the councillor with 14 other members. Its "
                         "functions include preparing ward development plans, ensuring tax collection "
                         "and maintaining services such as solid waste, sewerage, water supply and "
                         "street lighting. The area sabhas were removed by the select committee, "
                         "although the Bill as introduced had kept them."},
                        src("Article 243S. HPEC Box 1.5, JNNURM reforms. PRS, GBG Bill analysis.")]},
         ]},

        {"type": "content", "label": "Other Channels",
         "title": "Channels through which residents reach the municipality",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "table",
                        "head": ["Channel", "Who takes part", "What it can decide"],
                        "rows": [
                            ["Ward elections", "All voters", "Who represents the ward"],
                            ["Wards committee", "Councillors and members under state law", "Ward works and plans"],
                            ["Area sabha", "All voters of a polling area, where law provides", "Proposals and beneficiary lists"],
                            ["Town Vending Committee", "At least 40% vendors elected by vendors", "Surveys, certificates, vending plan"],
                            ["Swachhata App", "Any resident", "Complaints. Over 2 crore resolved by 2021"],
                            ["Swachh Survekshan feedback", "Any resident", "A ranking input. Over 7 crore responses by 2021"]]}],
              "right": [{"t": "body", "html": "Only the first four channels have any legal standing in "
                         "decisions, and only elections are guaranteed by the Constitution. Apps and "
                         "survey feedback collect complaints and opinions and pass them to officials."},
                        {"t": "body", "html": "Participation fails quietly when the council itself is "
                         "absent. In a town run by an administrator, wards committees have no "
                         "councillors to sit on them."},
                        {"t": "hbox", "color": "green", "html": "Before organising residents around "
                         "a ward plan, find out whether the ward committee exists, when it last met and "
                         "whether its minutes are public."},
                        src("Article 243S. Street Vendors Act, 2014, s. 22. SBM-U 2.0 Cabinet release, October 2021.")]},
         ]},

        {"type": "content", "label": "Research (1)", "ultra-compact": True,
         "title": "What research has found on definitions, finance and institutions",
         "blocks": [
             {"t": "table",
              "head": ["Study", "Finding"],
              "rows": [
                  ["Mukhopadhyay and Zérah, World Bank (2015)", "3,894 census towns in 2011 against 1,362 in 2001. About a third of urban growth came from reclassification. Little difference in services between census towns and statutory towns of the same size. Elites pushed for urban status and poorer groups resisted it"],
                  ["HPEC, chaired by Isher Judge Ahluwalia (2011)", "₹39.2 lakh crore of urban investment needed over 2012 to 2031. ULB revenue 0.9% of GDP against 6% in South Africa and 7.4% in Brazil. Recommended an accountable mayor with a city manager"],
                  ["RBI, Report on Municipal Finances (2022)", "Property tax 0.09 to 0.11% of GDP, far below OECD countries. Corporations' revenue to capital spending ratio of 2.4 against 7.1 for the Centre"],
                  ["RBI, Report on Municipal Finances (2024)", "Corporation revenue 0.6% of GDP, unchanged since 2019-20. Municipal bonds 0.01% of GDP"],
                  ["CAG performance audits, 18 states (2024)", "4 of 18 functions fully devolved on average. 61% of 2,625 ULBs in 17 states without an elected council. One post in three vacant. 29% of funds spent on development"],
                  ["PRS on the Greater Bengaluru Governance Bill (2025)", "Apex authority chaired by the Chief Minister, state power to dissolve corporations and set property tax rates, area sabhas removed"]]},
         ]},

        {"type": "content", "label": "Research (2)", "ultra-compact": True,
         "title": "What research has found on housing, heat and work",
         "blocks": [
             {"t": "table",
              "head": ["Study", "Finding"],
              "rows": [
                  ["Barnhardt, Field and Pande, <em>AEJ: Applied</em> (2017)", "A housing lottery moving slum residents to the periphery of an Indian city improved housing but not income, tenure security or human capital after 14 years. 34% of winners never moved and 32% later left. Winners were more isolated from family and caste networks"],
                  ["Marx, Stoker and Suri, <em>JEP</em> (2013)", "Poverty in slums resembles a poverty trap, with human capital thresholds, investment inertia and a policy trap keeping residents from using the city's opportunities"],
                  ["Azhar et al., <em>PLoS ONE</em> (2014)", "1,344 excess deaths (43.1%) in Ahmedabad in May 2010. The authors argue that IMD heatwave thresholds may underestimate health effects"],
                  ["Hess et al. (2018), as summarised in the Ahmedabad plan", "An estimated 2,380 deaths avoided in 2014 and 2015 after the Heat Action Plan, against a 2007 to 2010 baseline"],
                  ["Choragudi, Ideas for India (2022)", "Himachal Pradesh's urban guarantee built useful assets and employed mostly women, but few ULBs offered work, wages were late and the budget was cut from ₹100 crore to ₹5 crore"],
                  ["Drèze, Ideas for India (2020)", "Proposed job stamps through public institutions as a decentralised step towards an urban employment guarantee"],
                  ["CAG on the Chennai floods (tabled 2018)", "Reservoir releases and foreshore land use decided by a state department turned heavy rain into a disaster"]]},
         ]},

        {"type": "content", "label": "Practice",
         "title": "A checklist for working with an Indian municipality",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Status and power", "blocks": [
                  {"t": "bullets", "color": "cyan", "items": [
                      "Is the place a statutory town, a census town or an outgrowth? Check against the Census 2027 frozen boundaries.",
                      "Is there an elected council, or an administrator? When is the next election due under Article 243U?",
                      "For your issue, does the municipality, a parastatal, a state department or an SPV hold the function?",
                      "Does the commissioner, the mayor-in-council or the state sign contracts?",
                      "Is there a wards committee, and does it meet?"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "Money and evidence", "blocks": [
                  {"t": "bullets", "color": "green", "items": [
                      "Get the latest budget book and audited accounts, and compare budget estimates with actuals.",
                      "Find the property tax register's coverage and collection rate.",
                      "Check whether the state meets the 16th Finance Commission's entry conditions.",
                      "Find the town's AMRUT 2.0 water action plan and its PMAY-U progress by vertical.",
                      "Ask whether a street vendor survey has been completed and certificates issued.",
                      "Ask for the heat action plan and the flood contingency plan, and who is named in each."]}]},
                        {"t": "hbox", "color": "amber", "html": "Every item on this list can be "
                         "answered from a public document or a right to information request."}]},
         ]},

        {"type": "content", "label": "Sources (1)", "ultra-compact": True,
         "title": "Sources for this course (1 of 2)",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "sm": True, "items": [
                  "<a href='https://web.archive.org/web/20240414063418/https://www.mha.gov.in/MHA1/Par2017/pdfs/par2013-pdfs/ls-070513/6458.pdf'>MHA, Lok Sabha Unstarred Question 6458, 7 May 2013: Census 2011 population by residence and urban definitions</a>",
                  "<a href='https://cprindia.org/wp-content/uploads/2022/02/Census0Town0Final0Report.pdf'>Mukhopadhyay and Zérah, Understanding India's Urban Frontier, World Bank Report AUS7449, 2015</a>",
                  "<a href='https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/may/doc202651861301.pdf'>Directorate of Census Operations, Maharashtra, Census 2027 press conference, 30 April 2026 (PIB)</a>",
                  "<a href='https://dhulecorporation.org/wp-content/uploads/2026/03/Census%202027%20Circular%20No%201%20English.pdf'>Registrar General of India, Census 2027 Circular No. 1, 13 August 2025</a>",
                  "<a href='https://data.worldbank.org/indicator/SP.URB.TOTL.IN.ZS?locations=IN'>World Bank, World Development Indicators, urban population (% of total)</a>",
                  "<a href='https://www.mospi.gov.in/'>MoSPI, Periodic Labour Force Survey, annual 2025 and 2023-24</a>",
                  "<a href='https://icrier.org/pdf/FinalReport-hpec.pdf'>High Powered Expert Committee, Report on Indian Urban Infrastructure and Services, March 2011</a>",
                  "<a href='https://legislative.gov.in/constitution-of-india/'>Constitution of India, Part IXA and the Twelfth Schedule (Legislative Department)</a>",
                  "<a href='https://www.business-standard.com/opinion/columns/india-s-urban-crisis-deepens-as-states-choke-city-level-governance-125102200921_1.html'>Business Standard, 22 October 2025, on the CAG compendium of 74th Amendment audits</a>",
                  "<a href='https://prsindia.org/bills/states/the-greater-bengaluru-governance-bill-2024'>PRS Legislative Research, Greater Bengaluru Governance Bill, 2024</a>",
                  "<a href='https://www.thehindu.com/news/cities/bangalore/karnataka-greater-bengaluru-governance-act-2024-to-govern-city-from-may-15/article69575536.ece'>The Hindu, Greater Bengaluru Governance Act, 2024, to govern city from May 15, 15 May 2025</a>",
                  "<a href='https://www.rbi.org.in/Scripts/PublicationsView.aspx?id=22741'>RBI, Report on Municipal Finances, Chapter II, 13 November 2024</a>",
                  "<a href='https://www.rbi.org.in/scripts/PublicationsView.aspx?id=21361'>RBI, Report on Municipal Finances, Chapter II, 10 November 2022</a>",
                  "<a href='https://prsindia.org/policy/report-summaries/report-15th-finance-commission-2021-26'>PRS, Report Summary, 15th Finance Commission for 2021-26</a>",
                  "<a href='https://prsindia.org/files/policy/policy_committee_reports/16th_FC_Report_Summary.pdf'>PRS, Report Summary, 16th Finance Commission for 2026-31</a>"]}],
              "right": [{"t": "bullets", "sm": True, "items": [
                  "<a href='https://www.business-standard.com/politics/tracking-the-shift-urban-local-govts-see-a-230-rise-in-grant-allocations-126021500812_1.html'>Business Standard, 15 February 2026, reporting Janaagraha on 16th FC urban grants</a>",
                  "<a href='https://www.sebi.gov.in/legal/regulations/jul-2015/sebi-issue-and-listing-of-debt-securities-by-municipalities-regulations-2015-last-amended-on-february-15-2017-_34611.html'>SEBI (Issue and Listing of Debt Securities by Municipalities) Regulations, 2015</a>",
                  "<a href='https://www.orfonline.org/expert-speak/urban-local-bodies-municipal-bonds-due-diligence-55073'>Ramanath Jha, ORF Expert Speak, 3 September 2019, on Pune's municipal bond</a>",
                  "<a href='https://www.indiabudget.gov.in/budget2025-26/doc/budget_speech.pdf'>Union Budget 2025-26, Budget Speech</a>",
                  "<a href='https://www.indiabudget.gov.in/doc/budget_speech.pdf'>Union Budget 2026-27, Budget Speech, 1 February 2026</a>",
                  "<a href='https://www.pmindia.gov.in/en/news_updates/cabinet-approves-the-atal-mission-for-rejuvenation-and-urban-transformation-amrut-2-0-till-2025-26/'>Cabinet approves AMRUT 2.0 till 2025-26, October 2021</a>",
                  "<a href='https://prsindia.org/policy/report-summaries/review-of-sewerage-and-septage-coverage-in-cities-under-amrut-amrut-2-0'>PRS, Standing Committee report on sewerage and septage under AMRUT, 4 August 2026</a>",
                  "<a href='https://static.pib.gov.in/WriteReadData/specificdocs/documents/2024/dec/doc20241210468201.pdf'>PIB, Smart Cities Mission backgrounder, December 2024</a>",
                  "<a href='https://www.downtoearth.org.in/governance/after-a-decade-of-its-launch-only-18-out-of-100-cities-have-completed-smart-cities-mission-projects-but-there-are-some-positive-takeaways'>Down To Earth, 2025, on Smart Cities completion</a>",
                  "<a href='https://www.etvbharat.com/en/bharat/jharkhand-chandigarh-and-nagaland-only-states-completing-all-smart-city-projects-enn25121204754'>ETV Bharat, 12 December 2025, on Smart Cities projects</a>"]}]},
         ]},

        {"type": "content", "label": "Sources (2)", "ultra-compact": True,
         "title": "Sources for this course (2 of 2)",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "sm": True, "items": [
                  "<a href='https://pib.gov.in/PressReleasePage.aspx?PRID=2043927'>PIB, Cabinet approves PMAY-Urban 2.0, August 2024</a>",
                  "<a href='https://static.pib.gov.in/WriteReadData/specificdocs/documents/2024/aug/doc2024810372701.pdf'>PIB backgrounder, PMAY-Urban 2.0, 10 August 2024</a>",
                  "<a href='https://pmaymis.gov.in/PMAYMIS2_2024/Operational-Guidelines-of-PMAY-U-2.pdf'>MoHUA, PMAY-U 2.0 Operational Guidelines</a>",
                  "<a href='https://pmay-urban.gov.in/'>MoHUA, Achievement under PMAY-U and PMAY-U 2.0, as on 28 September 2026 (pmay-urban.gov.in)</a>",
                  "<a href='https://www.pmindia.gov.in/en/news_updates/cabinet-approves-the-continuation-of-swachh-bharat-mission-urban-sbm-u-till-2025-26-for-sustainable-outcomes/'>Cabinet approves SBM-Urban 2.0 till 2025-26, October 2021</a>",
                  "<a href='https://prsindia.org/files/bills_acts/bills_parliament/2012/Street_Vendors__Act,_2014.pdf'>Street Vendors (Protection of Livelihood and Regulation of Street Vending) Act, 2014, Gazette text (PRS)</a>",
                  "<a href='https://prsindia.org/billtrack/the-street-vendors-protection-of-livelihood-and-regulation-of-street-vending-bill-2012'>PRS, Street Vendors Bill, 2012, analysis</a>",
                  "<a href='https://www.aeaweb.org/articles?id=10.1257/app.20150397'>Barnhardt, Field and Pande, Moving to Opportunity or Isolation?, AEJ: Applied Economics, 2017</a>",
                  "<a href='https://www.aeaweb.org/articles?id=10.1257/jep.27.4.187'>Marx, Stoker and Suri, The Economics of Slums in the Developing World, JEP, 2013</a>"]}],
              "right": [{"t": "bullets", "sm": True, "items": [
                  "<a href='https://www.ideasforindia.in/topics/poverty-inequality/duet-a-proposal-for-an-urban-work-programme'>Jean Drèze, DUET: A proposal for an urban work programme, Ideas for India, 9 September 2020</a>",
                  "<a href='https://www.ideasforindia.in/topics/poverty-inequality/examining-himachal-s-urban-employment-guarantee'>Krishna Priya Choragudi, Examining Himachal's urban employment guarantee, Ideas for India, 21 March 2022</a>",
                  "<a href='https://prsindia.org/files/bills_acts/bills_states/rajasthan/2023/Bill26of2023Rajasthan.pdf'>Rajasthan Minimum Guaranteed Income Bill, 2023 (PRS)</a>",
                  "<a href='https://www.ideasforindia.in/topics/poverty-inequality/vb--g-ram-g-bill-2025-decoding-the-new-rural-employment-scheme'>Ashwini Kulkarni, VB-G RAM G Bill, 2025, Ideas for India, 7 January 2026</a>",
                  "<a href='https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0091831'>Azhar et al., Heat-Related Mortality in India, PLoS ONE, 2014</a>",
                  "<a href='https://www.nrdc.org/sites/default/files/ahmedabad-heat-action-plan-2018.pdf'>Ahmedabad Heat Action Plan, 2019 update, easy read version (NRDC)</a>",
                                    "<a href='https://www.thehindu.com/news/cities/chennai/2015-floods-a-man-made-disaster-cag/article24374953.ece'>The Hindu, CAG terms 2015 Chennai floods a man-made disaster, July 2018</a>"]},
                        {"t": "hbox", "color": "amber", "html": "Left out because no primary source for "
                         "them could be opened are Census 2011 slum totals, the detailed loan terms of PM SVANidhi, and the CAG compendium's "
                         "figures beyond those reported by Business Standard."}]},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Urban Development and Municipal Governance 101 &middot; Complete",
         "headline": "Find out who holds the function,<br>then follow the money.",
         "byline": "A town is a set of agencies, laws and budgets as well as a place. Check its status, "
                   "its council, its accounts and its plans before designing anything for it. Explore "
                   "the rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free forever", "ImpactMojo 101 Series"]},
    ],
}
