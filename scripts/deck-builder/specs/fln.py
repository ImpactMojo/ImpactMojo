# -*- coding: utf-8 -*-
"""
Foundational Literacy & Numeracy 101: ImpactMojo 101 Series (native deck spec)
How children learn to read and calculate in the early grades, how South Asia measures it, what
Indian policy promises and what the evidence says works.
Build: python3 scripts/deck-builder/build.py fln

Sources opened while writing (October 2026):
- ASER Centre, ASER 2024 National findings: https://asercentre.org/wp-content/uploads/2022/12/ASER-2024-National-findings.pdf
- Pratham, ASER 2026 page (ASER 2024 is the latest report): https://pratham.org/aser-2026/
- ASER 2024 report cards (rural): all-India https://asercentre.org/wp-content/uploads/2022/12/India.pdf ;
  states, e.g. https://asercentre.org/wp-content/uploads/2022/12/Himachal-Pradesh-3.pdf , Kerala-1, Odisha-1,
  Uttar-Pradesh-1, Bihar-2, Madhya-Pradesh-1, Telangana-1 (same path). Table 4 (reading levels by grade)
  and Table 5 (Std III reading by school type, 2018 to 2024) checked on 6 October 2026.
- World Bank press release, 23 June 2022, State of Global Learning Poverty 2022 Update:
  https://www.worldbank.org/en/news/press-release/2022/06/23/70-of-10-year-olds-now-in-learning-poverty-unable-to-read-and-understand-a-simple-text
- World Bank WDI API, SE.LPV.PRIM (last updated 13 July 2026):
  https://api.worldbank.org/v2/country/IND/indicator/SE.LPV.PRIM?format=json
- National Education Policy 2020: https://www.education.gov.in/sites/upload_files/mhrd/files/NEP_Final_English_0.pdf
- NIPUN Bharat document (PIB, July 2021): https://static.pib.gov.in/WriteReadData/specificdocs/documents/2021/jul/doc20217531.pdf
- PIB, Major achievements: implementation of NEP 2020 (July 2023):
  https://static.pib.gov.in/WriteReadData/specificdocs/documents/2023/jul/doc2023726228501.pdf
- MoE and NCERT, Foundational Learning Study 2022: National Report (92 pp.), hosted by AIR:
  https://www.air.org/sites/default/files/2022-09/National-Report-Benchmarking-ORF-Numeracy-India-2022.pdf
- PIB, 30 December 2022 (FLS fieldwork 23 to 26 March and 4 to 6 April 2022): https://pib.gov.in/PressReleasePage.aspx?PRID=1887647
- Careers360 on NIPUN launch: https://news.careers360.com/education-ministry-launches-nipun-initiative-for-literacy-numeracy-class-3
- NCERT, PARAKH Rashtriya Sarvekshan 2024: National Report (July 2025): https://parakh.ncert.gov.in/sites/default/files/2025-07/REPORT_India_IND.pdf
- PIB, 9 January 2025 (survey held 4 December 2024): https://pib.gov.in/PressReleasePage.aspx?PRID=2091737
- PIB, 17 December 2025 and 29 July 2026 (Rajya Sabha replies: NIPUN Bharat goal now FLN by the end of Grade 2,
  lakshya from Balvatika up to Grade 2): https://pib.gov.in/PressReleasePage.aspx?PRID=2205275 and
  https://pib.gov.in/PressReleasePage.aspx?PRID=2291340
- NCERT, Vidya Pravesh guidelines (July 2021): https://diksha.gov.in/assets/docs/vidyapravesh.pdf
- RTI International, EGRA Toolkit Second Edition (2016):
  https://s3.us-west-2.amazonaws.com/ierc-v2-publicfiles/public/public/resources/EGRA%20Toolkit%20V2%202016.pdf
- EGMA toolkit (Platas et al., RTI 2014): https://docs.opendeved.net/lib/XHDM4J9D and
  https://www.taclmeasurementlibrary.teachforall.org/node/208
- RTE Act 2009 (as enacted): https://en.wikisource.org/wiki/Right_of_Children_to_Free_and_Compulsory_Education_Act,_2009
  (India Code and education.gov.in did not respond from outside India on 6 October 2026)
- RTE (Amendment) Act 2019, Gazette of India Extraordinary No. 1, 11 January 2019, via PRS: https://prsindia.org/files/bills_acts/bills_parliament/2017/Right%20of%20Children%20to%20Free%20and%20Compulsory%20Education%20(Amendment)%20Act,%202019.pdf
- Article 350A: https://www.constitutionofindia.net/articles/article-350a-facilities-for-instruction-in-mothertongue-at-primary-stage/
- State of Karnataka v Associated Management of English Medium Primary and Secondary Schools (2014) 9 SCC 485:
  https://globalfreedomofexpression.columbia.edu/cases/karnataka-v-associated-management-english-medium-primary-secondary-schools/
- DPDP Act 2023 ss 9, 17(2)(b): https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf
  (commencement: ss 3-17 apply from 13 May 2027, G.S.R. 843(E), 13 November 2025)
- Pritchett and Beatty (2015), IJED 40: 276-288: https://ideas.repec.org/a/eee/injoed/v40y2015icp276-288.html
- Pritchett (2013), The Rebirth of Education, CGD: https://www.cgdev.org/publication/9781933286778-rebirth-education-schooling-aint-learning
- RISE Programme: https://riseprogramme.org/
- Nag (2007), J Research in Reading 30(1): 7-22, abstract via Crossref, doi 10.1111/j.1467-9817.2006.00329.x
- Nag and Snowling (2012), Scientific Studies of Reading 16(5): 404-423, abstract via OpenAlex, doi 10.1080/10888438.2011.576352
- Nag (2014), Frontiers in Psychology 5: 866: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2014.00866/full
- Siegler and Ramani (2008), Developmental Science 11(5): 655-661, abstract via Crossref, doi 10.1111/j.1467-7687.2008.00714.x
- Banerjee et al. (2025), Nature 639: 673-681, abstract via OpenAlex/Europe PMC, doi 10.1038/s41586-024-08502-w
- Banerjee, Cole, Duflo and Linden (2007), QJE 122(3): https://ideas.repec.org/a/oup/qjecon/v122y2007i3p1235-1264..html
- Banerjee, Banerji, Duflo, Glennerster and Khemani, NBER w14311 (2008) and AEJ: Policy 2(1) (2010):
  https://www.nber.org/system/files/working_papers/w14311/w14311.pdf
- Banerjee et al., NBER w22746 (2016): https://www.nber.org/system/files/working_papers/w22746/w22746.pdf
  and JEP 31(4): 73-102 (2017): https://ideas.repec.org/a/aea/jecper/v31y2017i4p73-102.html
- J-PAL TaRL case study (published September 2019, updated August 2022): https://www.povertyactionlab.org/case-study/teaching-right-level-improve-learning
- Muralidharan, Singh and Ganimian (2019), AER 109(4): https://ideas.repec.org/a/aea/aecrev/v109y2019i4p1426-60.html
  and NBER w22923: https://www.nber.org/system/files/working_papers/w22923/w22923.pdf
- GEEAP 2023 Smart Buys: https://documents1.worldbank.org/curated/en/099008110232520373/pdf/IDU-9401bfdd-f4ff-486b-84b4-570be4f65543.pdf
- Kraft, Blazar and Hogan (2018), RER 88(4): 547-588, abstract via OpenAlex, doi 10.3102/0034654318759268
- Popova, Evans, Breeding and Arancibia (2022), WBRO 37(1): 107-136, abstract via OpenAlex, doi 10.1093/wbro/lkab006
- Banerji, Berry and Shotland (2017), AEJ: Applied 9(4): 303-337, abstract via OpenAlex, doi 10.1257/app.20150390
- CAMRIS International, Nepal EGRP Performance Evaluation 2019 (USAID, February 2020):
  https://docs.aiddata.org/ad4/pdfs/usaid-archive/txt/PA00WGR4.txt
- Sehar Saeed (ITA), UKFIET, 28 May 2026, on ASER Pakistan 2025:
  https://www.ukfiet.org/2026/beyond-enrolment-pakistans-real-education-crisis-is-learning/
- Makwana (August 2025), Journal of Indian Education (NCERT): https://ejournals.ncert.gov.in/index.php/jie/article/download/5614/5377/10415
"""


def S(label, title, blocks, **kw):
    d = {"type": "content", "label": label, "title": title, "blocks": blocks}
    d.update(kw)
    return d


def B(html, sm=False):
    d = {"t": "body", "html": html}
    if sm:
        d["cls"] = "sm"
    return d


def H(color, html):
    return {"t": "hbox", "color": color, "html": html}


def P(color, title, html):
    return {"t": "panel", "color": color, "title": title, "blocks": [B(html, sm=True)]}


def TC(left, right, ratio="half"):
    return {"t": "twocol", "ratio": ratio, "left": left, "right": right}


def T(head, rows):
    return {"t": "table", "head": head, "rows": rows}


def BL(items, color="", sm=True):
    d = {"t": "bullets", "items": items, "sm": sm}
    if color:
        d["color"] = color
    return d


def TERM(word, d):
    return {"t": "term", "word": word, "def": d}


def FL(steps):
    return {"t": "flow", "steps": steps}


def ST(cards, cols=None):
    d = {"t": "stats", "cards": cards}
    if cols:
        d["cols"] = cols
    return d


def C(num, label, color="cyan", source=None):
    d = {"num": num, "label": label, "color": color}
    if source:
        d["source"] = source
    return d


def Q(text, attr):
    return {"t": "quote", "text": text, "attr": attr}


def DIV(num, word, title):
    return {"type": "divider", "num": num, "label": "Section " + word, "title": title}


def L(path, name):
    return '<a href="/101-courses/' + path + '">' + name + '</a>'


ASER = "ASER Centre, ASER 2024 National findings (rural India); the latest ASER report as of October 2026"
ASERRC = "ASER Centre, ASER 2024 report cards (rural), all-India and state Tables 4 and 5"
NEP = "National Education Policy 2020, Ministry of Education"
NIPUN = "NIPUN Bharat mission document, Ministry of Education (published by PIB, July 2021)"
PIB23 = "PIB, Major achievements: implementation of NEP 2020 (July 2023)"
WDI = "World Bank, World Development Indicators, SE.LPV.PRIM (updated 13 July 2026)"
WBLP = "World Bank and partners, The State of Global Learning Poverty: 2022 Update (press release, 23 June 2022)"
EGRA = "RTI International, EGRA Toolkit, Second Edition (USAID, 2016)"
FLS = "Ministry of Education and NCERT, Foundational Learning Study 2022: National Report (September 2022)"
PRK = "NCERT, PARAKH Rashtriya Sarvekshan 2024: National Report (July 2025)"
GEEAP = "Global Education Evidence Advisory Panel, 2023 Cost-Effective Approaches to Improve Global Learning"
TARL16 = "Banerjee, Banerji, Berry, Duflo, Kannan, Mukerji, Shotland and Walton, NBER Working Paper 22746 (2016); JEP 31(4), 2017"
RTE = "Right of Children to Free and Compulsory Education Act 2009 (No. 35 of 2009)"

DECK = {
    "slug": "fln",
    "title": "Foundational Literacy & Numeracy 101",
    "description": ("Foundational Literacy &amp; Numeracy 101: a free foundational course for development "
                    "practitioners in South Asia. Learning profiles and learning poverty, how children "
                    "learn to read in alphabetic and akshara scripts, early number sense, ASER 2024, "
                    "FLS 2022, PARAKH, EGRA and EGMA, NEP 2020, NIPUN Bharat, Vidya Pravesh and the RTE "
                    "Act, Teaching at the Right Level and the GEEAP smart buys, mother tongue and "
                    "multilingual classrooms, teachers, coaching and parents, and a practitioner "
                    "toolkit. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== TITLE =====================
        {"type": "title",
         "main": "Foundational<br>Literacy &amp;<br>Numeracy 101",
         "sub": "How children learn to read and calculate in the early grades, how South Asia "
                "measures it, and what policy and evidence say about helping every child get there",
         "tags": ["100 Slides", "South Asia Focus", "Free Forever", "NIPUN Bharat to TaRL"]},

        # ===================== TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What we cover",
         "items": [
             {"name": "Why the early grades decide later learning"},
             {"name": "How children learn to read"},
             {"name": "Scripts of South Asia: alphabets and aksharas"},
             {"name": "Early number sense"},
             {"name": "Measuring foundational learning"},
             {"name": "Indian policy: NEP 2020, NIPUN Bharat and the RTE Act"},
             {"name": "Programmes and evidence"},
             {"name": "Mother tongue and multilingual classrooms"},
             {"name": "Teachers, materials, coaching and families"},
             {"name": "A practitioner's toolkit"},
             {"name": "Debates and where next"},
         ]},

        # ===================== SECTION 01 =====================
        DIV("01", "One", "Why the early grades decide later learning"),

        S("Definitions", "What foundational literacy and numeracy mean", [
            B("Foundational literacy and numeracy, usually shortened to FLN, is the set of skills a "
              "child needs before school subjects can be learned at all: reading a simple text with "
              "understanding, writing words and short sentences, and handling numbers and the four "
              "operations. India's National Education Policy 2020 gives the working definition in "
              "paragraph 2.1, and the NIPUN Bharat mission document of July 2021 breaks it into "
              "components that teachers can teach and assessors can measure."),
            TC([TERM("Foundational literacy",
                     "NEP 2020 para 2.1: \"the ability to read and comprehend basic text\". NIPUN "
                     "Bharat lists five parts: oral language, decoding, reading fluency, reading "
                     "comprehension and writing.")],
               [TERM("Foundational numeracy",
                     "NEP 2020 para 2.1: \"the ability to carry out basic addition and subtraction "
                     "with Indian numerals\". NIPUN Bharat describes it as the ability to reason and "
                     "apply simple numerical concepts in daily problem solving.")]),
            H("cyan", "The word foundational is literal. Every later subject, from science to social "
              "studies, assumes a child can read the textbook and handle the numbers in it."),
        ]),

        S("The grade 3 turning point", "Learning to read, then reading to learn", [
            B("Curricula in South Asia, as elsewhere, assume that children spend the first two or "
              "three years of school learning how to read and calculate, and from then on use those "
              "skills to learn everything else. The NIPUN Bharat document puts the idea in one line "
              "and uses it to justify its focus on the end of Grade 3."),
            Q("Grade 3 is the inflection point by which children are expected to \"learn to read\" so "
              "that they can \"read to learn\" after that.", NIPUN),
            TC([P("red", "Children who fall behind, get left behind",
                  "That is the heading NIPUN Bharat gives this argument. A Grade 4 lesson on plants "
                  "assumes the child can read the chapter. A child who cannot is now behind in "
                  "science as well as in reading, and the gap compounds each year.")],
               [P("green", "Why the early years are the cheap years",
                  "A class of six-year-olds learning aksharas together is the normal business of "
                  "Grade 1. Teaching the same skill to a twelve-year-old means a separate group, "
                  "separate time and materials pitched below the age of the learner.")]),
        ]),

        S("Learning profiles", "What each year of school adds to what a child can do", [
            TERM("Learning profile",
                 "The relationship between years of schooling and the skills a child has. A steep "
                 "profile means each grade adds a lot; a shallow profile means children move up "
                 "grades while learning little."),
            B("Lant Pritchett and Amanda Beatty, in \"Slow down, you're going too fast: matching "
              "curricula to student skill levels\" (International Journal of Educational Development "
              "40, 2015, pages 276 to 288), note that learning profiles are often shockingly shallow "
              "in developing countries. Their model shows that two countries with identical potential "
              "learning can end with very different outcomes when the curriculum moves faster than "
              "children can follow."),
            TC([P("amber", "The mechanism",
                  "Each year the textbook moves on. A child who did not master the previous step "
                  "now faces material that assumes it, learns almost nothing from the new lesson, "
                  "and falls further behind.")],
               [P("green", "The counterintuitive conclusion",
                  "Pritchett and Beatty conclude that there is greater learning potential if "
                  "curricula and teachers slow down to match where children actually are. "
                  "Section 7 shows programmes built on that idea.")]),
        ]),

        S("Within-grade spread", "One grade, five or six grade levels of preparation", [
            B("Karthik Muralidharan, Abhijeet Singh and Alejandro Ganimian assessed middle-school "
              "students from low-income neighbourhoods in Delhi before evaluating an adaptive "
              "software programme (NBER Working Paper 22923, 2016, later American Economic Review "
              "2019). Their baseline data show how far a single classroom can stretch."),
            ST([C("2.5", "grade levels below grade 6 standard in mathematics, for the average grade 6 "
                  "student", "red", "Muralidharan, Singh and Ganimian, NBER WP 22923 (2016)"),
                C("4.5", "grade levels behind by grade 9, so the deficit grows with schooling", "amber",
                  "Muralidharan, Singh and Ganimian, NBER WP 22923 (2016)"),
                C("5 to 6", "grade levels spanned by students in the same grade", "indigo",
                  "Muralidharan, Singh and Ganimian, NBER WP 22923 (2016)")], cols=3),
            TC([B("A teacher who teaches to the textbook is teaching the top of that range. The "
                  "children at the bottom, often first-generation learners, sit through lessons "
                  "they cannot follow.", sm=True)],
               [B("Foundational gaps are the base of this spread. A child who cannot decode in "
                  "Grade 3 arrives in Grade 6 unable to read the mathematics word problem at "
                  "all.", sm=True)]),
        ]),

        S("Learning poverty", "The global measure: reading by age 10", [
            TERM("Learning poverty",
                 "The World Bank's indicator: the share of children of late primary age (about 10) "
                 "who cannot read and understand a simple age-appropriate text, adjusted for "
                 "children out of school, who are counted as not reading."),
            ST([C("70%", "of 10-year-olds in low- and middle-income countries estimated to be in "
                  "learning poverty after the pandemic", "red", WBLP),
                C("57%", "the same estimate before the pandemic", "amber", WBLP),
                C("78%", "predicted share for South Asia, up from 60% before the pandemic", "indigo",
                  WBLP)], cols=3),
            TC([B("The 2022 Update was produced by the World Bank with UNESCO, UNICEF, the UK's "
                  "FCDO, USAID and the Gates Foundation. The press release calls the 70% an "
                  "estimate and the regional figures predictions, because they were simulated "
                  "from school closure data.", sm=True)],
               [B("Read these as the scale of the problem. For a country's measured figure, use "
                  "the World Development Indicators series on the next slide and quote the year "
                  "the underlying assessment was done.", sm=True)]),
        ]),

        S("South Asia", "Learning poverty country by country, with the data year", [
            B("The World Bank publishes learning poverty by country in its World Development "
              "Indicators (series SE.LPV.PRIM). The figures below are the most recent value for "
              "each country in the series as last updated on 13 July 2026. The data years differ "
              "widely, because each estimate rests on whichever learning assessment the country "
              "last ran that meets the World Bank's standard."),
            T(["Country or region", "Learning poverty (%)", "Data year", "How to read it"],
              [["India", "56.1", "2017", "Rests on an assessment from before NEP 2020 and NIPUN Bharat"],
               ["Bangladesh", "51.2", "2022", "The most recent data year in the region"],
               ["Pakistan", "79.5", "2019", "Highest in the region; four in five children"],
               ["Sri Lanka", "14.8", "2015", "Lowest in the region by a wide margin"],
               ["Nepal", "No estimate", "None", "No qualifying assessment in the series"],
               ["South Asia (region)", "55.8", "2019", "Before the pandemic school closures"]]),
            H("amber", "Never compare these as if they were one year. India's figure is nearly a "
              "decade old, and the regional predictions on the previous slide suggest pandemic "
              "closures raised the numbers after 2019. Source: " + WDI + "."),
        ], compact=True),

        S("The systems argument", "Schooling ain't learning: Pritchett and the RISE programme", [
            B("Lant Pritchett's book The Rebirth of Education: Schooling Ain't Learning (Center for "
              "Global Development, 2013) argued that the enrolment drive of the 1990s and 2000s had "
              "built school systems that were good at getting children into classrooms and weak at "
              "making sure they learned. The Research on Improving Systems of Education (RISE) "
              "programme, funded by UK Aid, Australian Aid and the Gates Foundation, took the "
              "argument into country studies."),
            TC([P("indigo", "What RISE studied",
                  "Country research teams in seven countries: Ethiopia, India, Indonesia, Nigeria, "
                  "Pakistan, Tanzania and Vietnam. The RISE site frames the question as how the "
                  "parts of an education system fail to work together to produce learning.")],
               [P("cyan", "What it means for FLN",
                  "A foundational learning mission touches every part of the system: what "
                  "curricula ask for, what teachers are trained and rewarded for, what is measured "
                  "and what is reported upward. Fixing one part while the others pull the "
                  "other way rarely holds.")]),
            H("green", "This course keeps both levels in view: what happens between a teacher and "
              "a child, and what the system around them rewards."),
        ]),

        S("Course map", "How this course is organised", [
            B("The sections follow the order a practitioner meets the problem in the field. First "
              "how reading and number skills develop, including what is distinctive about South "
              "Asian scripts. Then how they are measured, what Indian law and policy promise, and "
              "what the evidence says works. The last sections turn to language, teachers and "
              "families, and end with tools you can use on Monday."),
            FL(["HOW CHILDREN LEARN: reading, scripts, number sense",
                "HOW WE KNOW: ASER, FLS, PARAKH, EGRA and EGMA",
                "WHAT IS PROMISED: NEP 2020, NIPUN Bharat, RTE Act",
                "WHAT WORKS: TaRL, structured pedagogy, adaptive software",
                "WHAT YOU DO: diagnostic, decision table, worked example"]),
            TC([B("Statistics carry their source and year on the slide. Where a figure could not "
                  "be checked against a source that was opened, it has been left out.", sm=True)],
               [B("Teaching examples that are invented to illustrate a method are labelled "
                  "Illustrative. Everything else is drawn from a named document.", sm=True)]),
        ]),

        # ===================== SECTION 02 =====================
        DIV("02", "Two", "How children learn to read"),

        S("The components", "Five components that reading research agrees on", [
            B("The EGRA Toolkit (RTI International for USAID, second edition 2016) builds its "
              "assessment on the US National Reading Panel report of 2000 and later reviews. It "
              "states that five components are generally accepted as necessary to master reading: "
              "phonological awareness, phonics, vocabulary, fluency and comprehension. Higher-order "
              "skills build on lower-order ones."),
            T(["Component", "What the child does", "A classroom sign in a Hindi-medium Grade 1"],
              [["Phonological awareness", "Hears and plays with the sound parts of spoken words",
                "Claps the three beats in kamal (क-म-ल) and says which word starts with the same sound"],
               ["Phonics (symbol to sound)", "Links written symbols to the sounds they stand for",
                "Says the sound of क and of कि when shown the card"],
               ["Vocabulary", "Knows what words mean", "Explains what a word in the story means in her own words"],
               ["Fluency", "Reads accurately, quickly and with expression",
                "Reads a short passage aloud without stopping at each akshara"],
               ["Comprehension", "Builds meaning from text", "Says what happened in the story and why"]]),
            H("cyan", "Comprehension is the goal. The other four are the route to it, and a child "
              "can be stuck at any one of them."),
        ], compact=True),

        S("Oral language", "Reading rests on the language a child can already speak", [
            B("Before a child can understand a written sentence she has to understand the same "
              "sentence spoken aloud. NIPUN Bharat lists oral language development first among its "
              "literacy components and describes it as listening comprehension, oral vocabulary and "
              "extended conversation skills. It adds that experiences in oral language are important "
              "for developing skills of reading and writing."),
            TC([P("green", "When home and school language match",
                  "Decoding gives the child access to words she already knows. Reading the word for "
                  "mango calls up a meaning she has had for years, and comprehension follows quickly.")],
               [P("red", "When they differ",
                  "A child who decodes perfectly in a language she does not speak reads sounds "
                  "without meaning. She may pass a fluency test and fail every comprehension "
                  "question. Section 8 returns to this.")]),
            H("indigo", "Practical test: read a short story aloud to the child and ask questions. If "
              "she cannot answer when listening, the problem is language, and more phonics will not "
              "fix it. The EGRA listening comprehension subtask measures exactly this."),
        ]),

        S("Phonological awareness", "Hearing the parts of words before reading them", [
            TERM("Phonological awareness",
                 "The ability to notice and work with the sound units of spoken language, from "
                 "whole words to syllables, to the start and end of syllables, to single sounds "
                 "(phonemes). It is about hearing, and needs no print."),
            B("The EGRA Toolkit describes awareness developing from larger units such as syllables "
              "and onset and rime towards the smallest unit, the phoneme. It assesses it orally, for "
              "example by asking children to identify the first or last sound of a word."),
            TC([BL(["Syllable: how many beats in ka-ma-la?",
                    "Rhyme: which word sounds like mala? kala or ghar?",
                    "Initial sound: which word starts like mitti?",
                    "Blending: put together k and a. What do you get?"], color="cyan")],
               [B("In English the phoneme is the unit the script writes, so phoneme awareness is "
                  "the main target. In akshara scripts the written unit is closer to the syllable, "
                  "and research from Kannada, covered in Section 3, finds that phoneme awareness "
                  "emerges later and grows with print knowledge.", sm=True)]),
        ]),

        S("Decoding", "Turning written symbols into spoken words", [
            Q("Involves deciphering written words based on understanding the relationship between "
              "symbols and their sounds.", NIPUN + ", definition of decoding"),
            B("A child who can decode can read a word she has never seen before. The EGRA Toolkit "
              "distinguishes two routes into a word: a lexical route, which recognises familiar "
              "words as wholes and is faster, and a sublexical route, which builds the word from its "
              "parts and is the only way into a new word. EGRA uses a nonword reading subtask, made "
              "of invented but pronounceable words, precisely so that the child cannot rely on "
              "memory and must decode."),
            TC([P("amber", "Why invented words",
                  "A child who has memorised the class reader can recite it without decoding. "
                  "Invented words separate real decoding skill from memory of a familiar text.")],
               [P("green", "What it means in class",
                  "Practice should include new combinations of known symbols, every day, so that "
                  "children learn to work words out. Reading the same lesson aloud ten times "
                  "trains memory more than decoding.")]),
        ]),

        S("Fluency", "Accuracy, speed and expression", [
            Q("Refers to the ability to read a text with accuracy, speed (automaticity), expression "
              "(prosody), and comprehension that allows children to make meaning from the text. Many "
              "children recognise aksharas, but read them laboriously, one-by-one.",
              NIPUN + ", definition of reading fluency"),
            TC([B("Fluency matters because attention is limited. A child who spends all her effort "
                  "on working out each akshara has nothing left for holding the sentence in mind "
                  "and building its meaning. When decoding becomes automatic, attention is freed "
                  "for comprehension. That is why fluency is measured, usually as words read "
                  "correctly per minute.", sm=True)],
               [ST([C("45 to 60", "words per minute, read with meaning, NIPUN Bharat goal for Grade 2",
                      "cyan", NIPUN),
                    C("60", "words per minute at least, read with meaning, NIPUN Bharat goal for "
                      "Grade 3", "green", NIPUN)], cols=1)]),
            H("amber", "A speed target without the words read with meaning is a trap: children can be "
              "drilled to bark at print. NIPUN Bharat attaches meaning to both targets."),
        ]),

        S("Comprehension", "Making meaning is the point of reading", [
            B("The EGRA Toolkit quotes the RAND Reading Study Group's definition: comprehension is "
              "the process of simultaneously extracting and constructing meaning through "
              "interaction and involvement with written language. NIPUN Bharat's definition is "
              "close to it: constructing meaning from a text and thinking critically about it, "
              "including retrieving information and interpreting texts."),
            TC([P("cyan", "Literal questions",
                  "Who went to the market? What did she buy? The answer is in the text. These "
                  "check that the child has extracted the information at all.")],
               [P("indigo", "Inferential questions",
                  "Why was she happy when she came home? The answer needs the text plus the "
                  "child's own reasoning. These check that she is building meaning.")]),
            B("A good early grade reading check asks both. EGRA's oral reading fluency subtask is "
              "followed by comprehension questions on the same passage, and ASER's story level "
              "is a Std II text the child must read, though ASER does not test comprehension at "
              "that level. Know which one your tool measures before you report it as reading with "
              "understanding.", sm=True),
        ]),

        S("Fluency and comprehension", "Why slow reading and weak understanding travel together", [
            B("Fluency and comprehension are measured separately but are connected in a simple way. "
              "A reader holds a limited amount in working memory. The EGRA Toolkit notes that oral "
              "reading fluency has been shown to be predictive of reading comprehension, which is "
              "why it sits at the centre of most early grade assessments."),
            T(["Reading speed (Illustrative)", "Time to read a 60-word story", "What usually happens"],
              [["10 words per minute", "6 minutes", "By the last line the first is forgotten; few questions answered"],
               ["30 words per minute", "2 minutes", "Literal questions answered, inference shaky"],
               ["60 words per minute", "1 minute", "The story is held in mind as a whole; most questions answered"]]),
            TC([B("The speeds and outcomes in the table are an Illustrative teaching example. "
                  "They come from no study and show the mechanism only.", sm=True)],
               [B("Benchmarks must be set per language, because languages differ in word length and "
                  "scripts differ in visual density. A word in Malayalam or Kannada is often longer "
                  "than a word in Hindi.", sm=True)]),
        ], compact=True),

        S("Writing", "Writing grows alongside reading", [
            B("Reading and writing draw on the same knowledge of how symbols map to sounds, and each "
              "strengthens the other. NIPUN Bharat treats writing as a literacy component covering "
              "the competencies of writing aksharas and words as well as writing for expression. "
              "The EGRA Toolkit includes dictation as an additional subtask, in which the assessor "
              "says letters or words and the child writes them."),
            TC([P("green", "Early writing tasks that build reading",
                  "Writing one's own name; copying then writing aksharas from memory; writing "
                  "words the teacher dictates; labelling pictures; writing one sentence about "
                  "a story heard.")],
               [P("amber", "A common gap",
                  "Copying from the blackboard keeps children busy and looks like writing. It "
                  "tests the eye and hand more than knowledge of sounds. Dictation reveals what "
                  "a child actually knows.")]),
            H("cyan", "NIPUN Bharat's seventh objective adds assessment through portfolios, group work, "
              "projects and oral presentations, so a child's written work becomes evidence of "
              "progress as well as practice."),
        ]),

        S("The pathway", "The reading pathway at a glance", [
            B("Put together, the components form a pathway. Children do not finish one stage before "
              "starting the next, and good classrooms work on several at once, but a child stuck at "
              "an early stage cannot benefit from instruction aimed at a later one. Diagnosis means "
              "finding the earliest stage where the child is stuck."),
            FL(["Oral language and listening comprehension",
                "Phonological awareness",
                "Symbol knowledge (letters or aksharas)",
                "Decoding words",
                "Fluent reading of text",
                "Comprehension and writing"]),
            T(["If the child...", "She is probably stuck at", "Start with"],
              [["Cannot name most aksharas", "Symbol knowledge", "Daily systematic symbol-sound practice"],
               ["Knows aksharas, cannot read words", "Blending and decoding", "Combining known symbols into words"],
               ["Reads words, stumbles on sentences", "Fluency", "Repeated reading of short, easy texts"],
               ["Reads fluently, cannot answer questions", "Language or comprehension", "Talk, vocabulary and questioning"]]),
        ], compact=True),

        # ===================== SECTION 03 =====================
        DIV("03", "Three", "Scripts of South Asia: alphabets and aksharas"),

        S("Writing systems", "Three kinds of script in South Asian classrooms", [
            B("Most reading research was done in English, an alphabetic script. Most South Asian "
              "children learn to read first in a different kind of script, and many learn two or "
              "three scripts by the end of primary school. The kind of script shapes what is hard "
              "to learn and in what order."),
            T(["Type", "What a symbol stands for", "Examples in the region"],
              [["Alphabet", "A single sound (phoneme), consonant or vowel", "English, taught in most schools"],
               ["Abjad", "Mainly consonants; short vowels are usually left unwritten",
                "Urdu in Perso-Arabic script, used in Pakistan and parts of India"],
               ["Alphasyllabary (akshara script)",
                "A consonant with an inherent vowel, changed by vowel signs and joined into conjuncts",
                "Devanagari (Hindi, Marathi, Nepali), Bengali, Gurmukhi, Gujarati, Odia, Tamil, "
                "Telugu, Kannada, Malayalam, Sinhala"]]),
            H("indigo", "Sonali Nag's work, which the next slides draw on, uses alphasyllabary and "
              "akshara language as the research terms for the third group."),
        ], compact=True),

        S("The akshara", "What an akshara is", [
            TC([B("An akshara is the written unit of an alphasyllabary. A consonant symbol carries an "
                  "inherent vowel, so क is read ka. Other vowels are written as signs (matras) "
                  "attached above, below, before or after the consonant. Two or more consonants "
                  "can fuse into a conjunct.", sm=True),
                T(["Akshara", "Reading", "What changed"],
                  [["क", "ka", "Consonant with inherent vowel"],
                   ["का", "kaa", "Vowel sign after"],
                   ["कि", "ki", "Vowel sign written before, read after"],
                   ["कु", "ku", "Vowel sign below"],
                   ["क्ष", "ksha", "Conjunct of k and sha"]])],
               [P("amber", "Why this is harder than it looks",
                  "The child must learn the base consonants, the vowel signs and how each sign "
                  "attaches to each consonant, plus the conjuncts, some of which look little like "
                  "their parts. In कि the vowel sign is written before the consonant but sounded "
                  "after it."),
                P("green", "Why it is also an advantage",
                  "The script is largely consistent: once a child knows how an akshara is "
                  "written, she can usually pronounce it. English spelling is far less "
                  "consistent.")]),
        ], compact=True),

        S("Nag 2007", "Akshara knowledge takes longer to acquire", [
            B("Sonali Nag studied 5 to 10 year olds learning to read Kannada, a South Indian "
              "akshara script (\"Early reading in Kannada: the pace of acquisition of orthographic "
              "knowledge and phonemic awareness\", Journal of Research in Reading 30(1), 2007, "
              "pages 7 to 22). She tested two hypotheses against the pace reported for English."),
            TC([P("cyan", "Hypothesis (a)", "Akshara knowledge acquisition would take longer than "
                  "letter knowledge in English."),
                P("cyan", "Hypothesis (b)", "Phoneme awareness would be slower to emerge.")],
               [Q("The study found these hypotheses to hold true across grades and in both "
                  "low-achieving and effective schools.", "Nag (2007), abstract"),
                B("The second clause matters. Slow progress was found in effective schools too, so "
                  "the pace reflects the script as well as the quality of teaching.", sm=True)]),
            H("amber", "Implication for planners: a target or a timeline copied from English-language "
              "research will be too fast for akshara languages, and teachers held to it will be "
              "judged to fail."),
        ]),

        S("Nag and Snowling 2012", "In akshara scripts, phoneme awareness grows with print", [
            B("Sonali Nag and Margaret Snowling followed up with 9 to 12 year old readers of Kannada "
              "(\"Reading in an alphasyllabary: implications for a language universal theory of "
              "learning to read\", Scientific Studies of Reading 16(5), 2012, pages 404 to 423)."),
            TC([BL(["Less fluent readers with lower orthographic knowledge were at floor on "
                    "phoneme tasks",
                    "More fluent readers with greater orthographic knowledge showed significant "
                    "phonemic awareness",
                    "Orthographic knowledge, phoneme awareness and rapid naming each independently "
                    "predicted reading rate"], color="indigo")],
               [TERM("Rapid automatised naming (RAN)",
                     "How quickly a child names a row of familiar items such as colours, pictures "
                     "or digits. It indexes how fast the brain retrieves names from symbols, and "
                     "predicts reading speed across languages.")]),
            B("The authors suggest that akshara literacy builds a dual representation, at the "
              "syllable and the phoneme level, and that learning symbol-sound mappings is a "
              "universal part of learning to read. For teaching: begin with syllable-level "
              "awareness, and expect phoneme awareness to grow as children learn the script.", sm=True),
        ]),

        S("Scale of the script", "Hundreds of symbols and years of learning", [
            B("In a 2014 paper in Frontiers in Psychology (volume 5, article 866), Nag argues against "
              "what she calls alphabetism: treating the alphabet as the model of how all reading "
              "works. She notes that in akshara languages the number of akshara in use and "
              "encountered in print still runs into hundreds, and that symbol learning continues "
              "well into middle school and beyond, while in alphabetic scripts it is typically "
              "complete within the first year."),
            TC([P("red", "Where planners go wrong",
                  "Programmes adapted from English materials introduce a few letters a week and "
                  "expect the code to be complete within months. In Hindi or Telugu that leaves "
                  "most vowel sign combinations and conjuncts untaught.")],
               [P("green", "What a script-aware plan does",
                  "Sequences the symbol set explicitly, teaches the most frequent aksharas and "
                  "conjuncts first, plans to keep teaching symbols through Grade 3 and later, and "
                  "sets fluency benchmarks from data in that language.")]),
            H("cyan", "The NIPUN Bharat literacy definitions already use the word akshara, which is "
              "a useful anchor when arguing for script-specific materials."),
        ]),

        S("Teaching aksharas", "Teaching moves that suit akshara scripts", [
            B("No single sequence has been agreed across South Asian languages, and the research base "
              "is far thinner than for English. The moves below follow from the properties of the "
              "script and from Nag's findings. Adapt them to the language and test them."),
            T(["Teaching move", "Why it fits the script"],
              [["Teach the vowel sign system as a pattern (the full set on one consonant, then the next)",
                "The same signs attach to every consonant, so the pattern generalises"],
               ["Use syllable-level games before phoneme games",
                "Syllable awareness comes first in akshara readers (Nag 2007; Nag and Snowling 2012)"],
               ["Introduce high-frequency conjuncts early and explicitly",
                "Conjuncts are frequent in real texts and often do not look like their parts"],
               ["Read connected text from the first weeks",
                "Symbol drill alone does not build fluency or meaning"],
               ["Keep symbol teaching going in Grades 2 and 3",
                "Akshara learning continues for years (Nag 2014)"]]),
            H("indigo", "Many states use the traditional chart of a consonant combined with each "
              "vowel sign, called barakhadi in Hindi. Used as a reference, it shows the system. Used "
              "as daily chanting with no reading, it trains recitation."),
        ], compact=True),

        S("Second scripts", "English and other second scripts", [
            B("Many South Asian children learn two or three scripts in primary school: a regional "
              "akshara script, English, and in some places Urdu or a second Indian script. NEP 2020 "
              "para 4.12 sets the order: early reading and writing in the mother tongue, with skills "
              "developed for reading and writing in other languages in Grade 3 and beyond."),
            TC([P("cyan", "What transfers",
                  "The idea that print stands for speech, phonological awareness, comprehension "
                  "strategies and the habit of reading. A child who reads well in one script "
                  "learns a second faster.")],
               [P("amber", "What has to be learned again",
                  "The symbols themselves, the direction of writing for Urdu, and English's "
                  "inconsistent spelling, where one letter can stand for several sounds.")]),
            H("red", "English-medium instruction from Grade 1 for children who do not speak English "
              "asks them to learn an unfamiliar script, an inconsistent spelling system and a new "
              "language all at once. Section 8 covers what law and policy say about the choice."),
        ]),

        # ===================== SECTION 04 =====================
        DIV("04", "Four", "Early number sense"),

        S("Scope", "What foundational numeracy covers", [
            B("NIPUN Bharat lists the major aspects and components of early mathematics. Arithmetic "
              "is one of them, but the list starts before counting and runs to shapes, measurement "
              "and data. A numeracy programme that teaches only sums leaves most of it out."),
            T(["Component (NIPUN Bharat)", "What it includes"],
              [["Pre-number concepts", "Sorting, matching, comparing and ordering objects; more and less"],
               ["Numbers and operations on numbers",
                "Counting, the number system and base ten; computing up to three-digit numbers in "
                "her own way and with standard algorithms"],
               ["Shapes and spatial understanding", "Recognising and describing shapes and positions"],
               ["Measurement", "Comparing and measuring length, weight, capacity, time and money"],
               ["Data handling", "Interpreting simple data and information in daily life"],
               ["Patterns", "Identifying and extending patterns from repeating shapes to numbers"]]),
            H("cyan", "The source is the NIPUN Bharat mission document (Ministry of Education, July "
              "2021). The wording in the right column is condensed from its numeracy panel."),
        ], compact=True),

        S("Number sense", "Number sense comes before arithmetic", [
            TERM("Number sense",
                 "An intuitive grasp of quantity: knowing that the last number counted tells how "
                 "many, that 8 is more than 5 and by roughly how much, that numbers sit in order "
                 "on a line, and that a quantity can be split and recombined."),
            B("Children arrive in Grade 1 with very different amounts of this. Robert Siegler and "
              "Geetha Ramani found that the numerical magnitude knowledge of preschoolers from "
              "low-income families lagged behind that of more affluent peers before school even "
              "began (Developmental Science 11(5), 2008, pages 655 to 661). They attribute part of "
              "the gap to differing experience of informal number activities such as board games."),
            TC([BL(["Counting with one-to-one correspondence",
                    "Cardinality: the last count word is the total",
                    "Comparing two quantities or two numerals",
                    "Placing numbers on a line"], color="green")],
               [B("Children who cannot yet do these will learn written sums as symbol drills. "
                  "They may get 4 + 3 right on paper and still not know whether 7 sweets are "
                  "more than 5.", sm=True)]),
        ]),

        S("Board games", "A cheap way to build number sense", [
            B("In the second experiment of Siegler and Ramani (2008), preschoolers from low-income "
              "families played a simple board game with squares numbered 1 to 10 in a line, moving "
              "a token and saying the numbers aloud. A comparison group played the same game with "
              "colours in place of numbers."),
            ST([C("4 x 15 min", "sessions of the numbered board game", "cyan",
                  "Siegler and Ramani (2008), Developmental Science 11(5)"),
                C("Gap closed", "the game eliminated the differences in numerical estimation "
                  "proficiency", "green", "Siegler and Ramani (2008)"),
                C("No effect", "from the same game played with colours in place of numbers", "amber",
                  "Siegler and Ramani (2008)")], cols=3),
            TC([B("The authors conclude that playing numerical board games offers an inexpensive "
                  "means for reducing the gap in numerical knowledge between less and more affluent "
                  "children when they begin school.", sm=True)],
               [B("The study was in the United States, with small samples. For South Asian "
                  "anganwadis and Balvatika classes it supports a low-cost idea worth testing: "
                  "linear number games such as a numbered snakes and ladders track.", sm=True)]),
        ]),

        S("Place value", "Place value is where many children stall", [
            B("ASER's arithmetic tasks climb in four steps: recognising numbers 1 to 9, recognising "
              "numbers 11 to 99, a two-digit subtraction with borrowing, and a three-digit by "
              "one-digit division. The jump from the second to the third step is a jump into place "
              "value: borrowing only makes sense if the child understands that the 4 in 43 means "
              "four tens."),
            ST([C("33.7%", "of Std III children in rural India could at least do a two-digit "
                  "subtraction in 2024", "amber", ASER),
                C("30.7%", "of Std V children could do a three-digit by one-digit division in 2024",
                  "red", ASER),
                C("45.8%", "of Std VIII children could do the same division in 2024", "indigo", ASER)],
              cols=3),
            TC([B("More than half of rural Std VIII children could not do a division expected in "
                  "Std III or IV. Gaps that open at place value persist for years.", sm=True)],
               [B("Teaching move: build tens with bundles of ten sticks or straws, trade ten ones "
                  "for one ten physically, and only then write the borrowing procedure.", sm=True)]),
        ]),

        S("Market maths", "Children who calculate at work and children who calculate at school", [
            B("Abhijit Banerjee, Esther Duflo, Elizabeth Spelke and colleagues surveyed 1,436 children "
              "working in markets in Kolkata and Delhi (\"Children's arithmetic skills do not transfer "
              "between applied and academic mathematics\", Nature 639, 2025, pages 673 to 681). "
              "Nearly all used complex arithmetic effectively at work, yet could not solve abstract "
              "problems of equal or lesser complexity in the format used in school."),
            TC([P("amber", "School children, the mirror image",
                  "471 children with no market experience, enrolled in nearby schools, did better "
                  "on simple abstract problems. Only 1% could answer an applied market problem that "
                  "more than one third of working children solved.")],
               [P("cyan", "What the authors conclude",
                  "Both groups were unable to transfer their skills to new contexts. The paper "
                  "highlights the importance of curricula that bridge the gap between intuitive "
                  "and formal maths.")]),
            H("green", "For FLN: start from the arithmetic children already do with money, measures "
              "and trade, and connect it explicitly to written numbers and procedures."),
        ]),

        S("Concrete to abstract", "Teaching number with objects, pictures and then symbols", [
            B("A common sequence in early mathematics teaching moves from concrete objects, to "
              "pictures of them, to written symbols. Each step is linked to the previous one so "
              "that the symbol keeps its meaning. The routine below is an Illustrative example of "
              "how one Grade 2 lesson on subtraction might use it."),
            FL(["CONCRETE: 43 sticks as 4 bundles of ten and 3 loose; take away 17",
                "PICTORIAL: draw 4 tens and 3 ones; cross out, opening a ten when needed",
                "SYMBOLIC: write 43 - 17 and record the regrouping",
                "TALK: children explain why a ten was opened",
                "APPLY: a market problem with rupee notes and coins"]),
            TC([B("Illustrative. The materials are free or cheap: sticks, stones, bottle caps, "
                  "paper money. What costs time is the teacher's preparation.", sm=True)],
               [B("The link to Section 2: a numeracy lesson is also a language lesson. Word "
                  "problems need reading, and explanations need vocabulary such as more, fewer, "
                  "tens and left over.", sm=True)]),
        ]),

        S("Numeracy targets", "NIPUN Bharat's numeracy goals by grade", [
            B("NIPUN Bharat sets learning goals, which it calls lakshya, from Balvatika (the "
              "pre-school year before Grade 1) to Grade 3. The numeracy goals below are as printed "
              "in the 2021 mission document; the Ministry has since moved the end point to Grade 2. "
              "They describe what a child should do by the end of each year, so they double as a "
              "checklist for a classroom diagnostic."),
            T(["Stage", "Numeracy lakshya (NIPUN Bharat, July 2021)"],
              [["Balvatika", "Recognises and reads numerals up to 10; arranges numbers, objects, "
                "shapes or events in a sequence"],
               ["Grade 1", "Reads and writes numbers up to 99; performs simple addition and subtraction"],
               ["Grade 2", "Reads and writes numbers up to 999; subtracts numbers up to 99"],
               ["Grade 3", "Reads and writes numbers up to 9999; solves simple multiplication problems"]]),
            TC([B("Compare with ASER 2024: only a third of rural Std III children could do the "
                  "two-digit subtraction that NIPUN Bharat expects by the end of Grade 2.", sm=True)],
               [B("The gap between the goal and the measured level is the size of the task facing "
                  "teachers, and the reason grouping by level matters (Section 7).", sm=True)]),
        ], compact=True),

        # ===================== SECTION 05 =====================
        DIV("05", "Five", "Measuring foundational learning"),

        S("Assessing orally", "Why foundational skills are tested one child at a time", [
            B("A written test assumes the child can read the questions. For a child who cannot yet "
              "read, every written test is a reading test, and it records zero without saying "
              "where the child is stuck. The EGRA Toolkit gives this as its reason for assessing "
              "orally: a paper test tells us only what children do not know, while an oral one shows "
              "where they are in the reading acquisition process and detects early growth."),
            TC([P("cyan", "One-on-one, oral, short",
                  "ASER, EGRA, EGMA and the FLS all sit an assessor with one child. The child "
                  "reads aloud or answers aloud, and the assessor records what she can do. Each "
                  "test takes minutes.")],
               [P("indigo", "Floor-level by design",
                  "Tests that place a child on a ladder of skills, from letters upward, show where "
                  "she is. A grade-level test only shows that she is below grade, which a teacher "
                  "usually already knows.")]),
            H("amber", "The cost of oral testing is people and time. Large surveys pay it with "
              "volunteers (ASER) or trained field investigators (FLS, EGRA). A classroom version "
              "takes a teacher about a day for a class of 40."),
        ]),

        S("ASER", "ASER: the household survey of learning", [
            B("The Annual Status of Education Report is a household survey of rural India run "
              "with Pratham. In each district a local organisation or institution conducts it, and "
              "children are tested at home, so children who are out of school or absent are "
              "counted. Reading and arithmetic tasks are given one-on-one to every sampled child "
              "aged 5 to 16, and the method has remained the same since 2006, which allows "
              "comparison over time."),
            ST([C("6,49,491", "children reached in ASER 2024", "cyan", ASER),
                C("17,997", "villages surveyed", "green", ASER),
                C("605", "rural districts covered", "indigo", ASER),
                C("15,728", "government schools with primary sections visited", "amber", ASER)], cols=4),
            TC([T(["Reading ladder", "Arithmetic ladder"],
                  [["Letters", "Numbers 1 to 9"], ["Words", "Numbers 11 to 99"],
                   ["Std I paragraph", "Two-digit subtraction with borrowing"],
                   ["Std II story", "Three-digit by one-digit division"]])],
               [B("The child is marked at the highest level she reaches comfortably. As of October "
                  "2026, ASER 2024 is the latest report; Pratham's page for ASER 2026 describes the "
                  "next survey as in preparation.", sm=True)]),
        ], compact=True),

        S("ASER 2024 reading", "Reading in government schools has recovered past 2018", [
            B("ASER 2024 reports that reading levels in government schools improved in every "
              "elementary grade since 2022, and that for Std III they are the highest since the "
              "survey began. The chart shows the share of government school children in Std III and "
              "Std V who can read a Std II level text."),
            {"t": "chart", "canvas": "flnAserRead",
             "title": "Government school children who can read a Std II level text (%), rural India",
             "source": ASER,
             "type": "bar",
             "data": {"labels": ["2018", "2022", "2024"],
                      "datasets": [{"label": "Std III", "data": [20.9, 16.3, 23.4],
                                    "backgroundColor": "#0369A1"},
                                   {"label": "Std V", "data": [44.2, 38.5, 44.8],
                                    "backgroundColor": "#047857"}]},
             "options": {"__js__": "{ plugins:{legend:{position:'bottom'}}, scales:{ y:{ min:0, max:60, title:{display:true,text:'% of children'} } } }"}},
            H("amber", "The level is still low. In 2024 more than three in four government school "
              "Std III children could not read a Std II text. Across all schools the figure was "
              "27.1% (" + ASERRC + ")."),
        ]),

        S("ASER 2024 arithmetic", "Arithmetic reached its highest level in over a decade", [
            B("ASER 2024 describes basic arithmetic as improving substantially in both government "
              "and private schools, reaching the highest level in over a decade. The gains were "
              "largest in government schools between 2022 and 2024. The school observations in the "
              "same report show FLN directives, training and materials reaching most of them."),
            T(["Indicator (rural India)", "2018", "2022", "2024"],
              [["Std III, can at least subtract (all schools)", "28.2%", "25.9%", "33.7%"],
               ["Std III, can at least subtract (government schools)", "20.9%", "20.2%", "27.6%"],
               ["Std V, can divide (all schools)", "27.9%", "25.6%", "30.7%"],
               ["Std VIII, can divide (all schools)", "44.1%", "44.7%", "45.8%"]]),
            TC([B("Source: " + ASER + ". Subtraction means a two-digit numerical subtraction with "
                  "borrowing; division means three digits by one digit.", sm=True)],
               [B("The Std VIII line barely moves. Children who missed the foundations before the "
                  "FLN push have not caught up, which is an argument for remedial programmes in "
                  "upper primary too.", sm=True)]),
        ], compact=True),

        S("Before Grade 1", "Before Grade 1: pre-primary enrolment is rising", [
            B("Foundational learning starts before school. ASER 2024 records whether children aged 3 "
              "to 5 are enrolled in an anganwadi centre, a government pre-primary class or a private "
              "LKG or UKG. Enrolment has risen steadily since 2018, and anganwadi centres remain the "
              "largest provider: since 2018 more than half of all children aged 3 and 4 have been "
              "enrolled in one."),
            {"t": "chart", "canvas": "flnPrePrimary",
             "title": "Children enrolled in any pre-primary institution, by age (%), rural India",
             "source": ASER,
             "type": "line",
             "data": {"labels": ["2018", "2022", "2024"],
                      "datasets": [{"label": "Age 3", "data": [68.1, 75.8, 77.4],
                                    "borderColor": "#0369A1", "backgroundColor": "#0369A1"},
                                   {"label": "Age 4", "data": [76.0, 82.0, 83.4],
                                    "borderColor": "#047857", "backgroundColor": "#047857"},
                                   {"label": "Age 5", "data": [58.4, 62.1, 71.4],
                                    "borderColor": "#B45309", "backgroundColor": "#B45309"}]},
             "options": {"__js__": "{ plugins:{legend:{position:'bottom'}}, scales:{ y:{ min:40, max:100, title:{display:true,text:'% enrolled'} } } }"}},
            TC([B("Age 5 is lower because many five-year-olds are already in Std I, though the "
                  "share of underage children in Std I fell to 16.7% in 2024.", sm=True)],
               [B("Meghalaya and Uttar Pradesh had the highest share of 3-year-olds enrolled "
                  "nowhere, over 50%. Enrolment shows a child is registered; what happens in "
                  "the anganwadi matters as much.", sm=True)]),
        ]),

        S("Spread in Std III", "Inside a Std III classroom: five reading levels at once", [
            B("The headline share of children reading a Std II text hides how the rest are spread. "
              "ASER reports the full distribution. In 2024, across all rural schools, Std III "
              "children were spread across every level of the reading ladder."),
            {"t": "chart", "canvas": "flnSpread",
             "title": "Highest reading level of Std III children, rural India, 2024 (%)",
             "source": ASERRC,
             "type": "bar",
             "data": {"labels": ["Not even letters", "Letters", "Words", "Std I text", "Std II text"],
                      "datasets": [{"label": "% of Std III children",
                                    "data": [8.2, 22.6, 22.2, 20.0, 27.0],
                                    "backgroundColor": "#4F46E5"}]},
             "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:35, title:{display:true,text:'% of children'} } } }"}},
            H("indigo", "Nearly a third of Std III children could not yet read words. One lesson pitched "
              "at the Std III textbook reaches only the top group, which is the whole case for "
              "grouping children by level."),
        ]),

        S("States", "States differ by a factor of seven", [
            B("National averages hide very different state systems. The table shows the share of "
              "government school children in Std III who could read a Std II level text, from the "
              "ASER 2024 state report cards (Table 5). The national findings name "
              "Himachal Pradesh, Uttarakhand, Kerala, Uttar Pradesh, Haryana, Odisha and Maharashtra "
              "as states with gains of more than 10 percentage points since 2022."),
            T(["State (government schools, Std III)", "2018", "2022", "2024"],
              [["Himachal Pradesh", "47.4%", "23.0%", "49.7%"],
               ["Kerala", "43.4%", "31.6%", "44.4%"],
               ["Odisha", "34.9%", "26.7%", "37.7%"],
               ["Uttar Pradesh", "12.3%", "16.4%", "27.9%"],
               ["Bihar", "12.3%", "12.9%", "20.1%"],
               ["Madhya Pradesh", "10.4%", "7.9%", "14.8%"],
               ["Telangana", "12.6%", "6.3%", "6.8%"]]),
            H("cyan", "Uttar Pradesh more than doubled its 2018 level by 2024. Telangana barely moved "
              "after the pandemic fall. Gaps this wide between states point to state programmes "
              "and how well they are delivered."),
        ], compact=True),

        S("FLS 2022", "The Foundational Learning Study 2022", [
            B("The Ministry of Education and NCERT ran the Foundational Learning Study in March and "
              "April 2022 and published national, state and district reports on 6 September 2022 "
              "(PIB, 30 December 2022). It tested Grade 3 children one-on-one in 20 languages and placed them on four "
              "levels of the Global Proficiency Framework: below partially meets, partially meets, "
              "meets and exceeds global minimum proficiency."),
            ST([C("86,000+", "Grade 3 students assessed, in about 10,000 schools", "cyan", FLS),
                C("20", "languages, each with its own reading benchmarks", "indigo", FLS),
                C("42%", "met global minimum proficiency in numeracy; a further 10% exceeded it",
                  "green", FLS),
                C("11%", "could not complete the most basic grade-level numeracy tasks", "red", FLS)],
              cols=4),
            TC([B("In literacy, the share who could not complete the most basic tasks was highest "
                  "in Tamil (42%) and Konkani (38%), and lowest in Punjabi (7%) and Mizo (12%), from the "
                  "national report.", sm=True)],
               [B("Compare languages with care. Each language's sample is also a state's school "
                  "system, so the gap mixes script, teaching and administration.", sm=True)]),
        ], compact=True),

        S("PARAKH", "NAS, PARAKH and the national school survey", [
            B("India's government-run learning survey was the National Achievement Survey (NAS). "
              "NEP 2020 led to a National Assessment Centre, PARAKH, set up in NCERT as an "
              "independent constituent unit on 8 February 2023 (PIB, July 2023). Its first national "
              "survey, PARAKH Rashtriya Sarvekshan, tested Grades 3, 6 and 9 on 4 December 2024."),
            TC([ST([C("5,99,026", "Class 3 students tested in PARAKH Rashtriya Sarvekshan 2024",
                      "cyan", PRK),
                    C("27,741", "schools in the Class 3 sample (74,229 across Classes 3, 6 and 9)", "indigo", PRK),
                    C("64 and 60", "average Class 3 scores (%) in language and mathematics", "green",
                      PRK)], cols=1)],
               [P("amber", "Why PARAKH and ASER disagree",
                  "PARAKH tests children in school, on written items spanning the grade's "
                  "competencies, and reports an average score. ASER tests children at home on a "
                  "floor-level ladder and reports the share who reach a level. A 64% average and "
                  "a 23% reading rate can both be true. Quote each with its method.")]),
        ]),

        S("EGRA and EGMA", "EGRA and EGMA: the international toolkits", [
            B("The Early Grade Reading Assessment (EGRA) and the Early Grade Mathematics Assessment "
              "(EGMA) are oral, one-on-one instruments developed by RTI International with USAID "
              "funding and adapted to each language. The EGRA Toolkit second edition dates from "
              "2016; the EGMA toolkit by Platas, Ketterlin-Geller, Brombacher and Sitabkhan from "
              "2014. Nepal used a nationally representative EGRA in 2014 to set initial "
              "reading benchmarks."),
            T(["EGRA core subtasks", "EGMA core subtasks"],
              [["Listening comprehension", "Number identification"],
               ["Letter (or akshara) identification", "Number discrimination (which is bigger)"],
               ["Nonword reading", "Missing number (number patterns)"],
               ["Oral reading fluency with comprehension", "Addition and subtraction, levels 1 and 2"],
               ["Phonological awareness; familiar word reading", "Word problems"]]),
            H("red", "The EGRA Toolkit states that EGRA is not intended to be a high-stakes "
              "accountability measure to determine student grade promotion or to evaluate "
              "individual teachers. Using it that way invites teaching to the test."),
        ], compact=True),

        # ===================== SECTION 06 =====================
        DIV("06", "Six", "Indian policy: NEP 2020, NIPUN Bharat and the RTE Act"),

        S("NEP 2020", "NEP 2020 makes foundational learning the first priority", [
            B("Chapter 2 of the National Education Policy 2020 is titled \"Foundational Literacy and "
              "Numeracy: An Urgent &amp; Necessary Prerequisite to Learning\". Paragraph 2.1 "
              "estimates that over 5 crore children in elementary school had not attained "
              "foundational literacy and numeracy. Paragraph 2.2 sets the priority."),
            Q("The highest priority of the education system will be to achieve universal "
              "foundational literacy and numeracy in primary school by 2025. The rest of this Policy "
              "will become relevant for our students only if this most basic learning requirement "
              "(i.e., reading, writing, and arithmetic at the foundational level) is first achieved.",
              NEP + ", para 2.2"),
            TC([BL(["A National Mission on FLN, set up on priority",
                    "State and UT implementation plans with stage-wise targets",
                    "Teacher vacancies filled; PTR under 30:1, under 25:1 in disadvantaged areas"],
                   color="cyan")],
               [BL(["A 3-month play-based school preparation module for Grade 1 (para 2.5)",
                    "A national repository of FLN resources on DIKSHA (para 2.6)",
                    "Peer tutoring and trained community volunteers (para 2.7)"], color="green")]),
        ], compact=True),

        S("Foundational stage", "The 5+3+3+4 structure and the foundational stage", [
            B("NEP 2020 replaces the old 10+2 description of schooling with a 5+3+3+4 curricular "
              "structure covering ages 3 to 18 (para 4.2). The first five years form the "
              "Foundational Stage: three years of anganwadi or pre-school plus Grades 1 and 2, "
              "covering ages 3 to 8, taught through flexible, multilevel, play and activity-based "
              "learning."),
            TC([T(["Stage", "Years", "Ages"],
                  [["Foundational", "3 years pre-school + Grades 1 to 2", "3 to 8"],
                   ["Preparatory", "Grades 3 to 5", "8 to 11"],
                   ["Middle", "Grades 6 to 8", "11 to 14"],
                   ["Secondary", "Grades 9 to 12", "14 to 18"]])],
               [P("indigo", "Why it matters for FLN",
                  "It puts pre-school and the first two grades under one curriculum, so the "
                  "anganwadi and the primary school are planned as one stage. NEP 2020 para 1.1 "
                  "justifies the focus on the early years with the claim that over 85% of a "
                  "child's cumulative brain development occurs before age 6.")]),
            H("amber", "The policy has no statutory force. Early childhood care sits in Article 45 of the "
              "Constitution as a directive principle, so the stage rests on schemes and budgets "
              "with no enforceable right behind the first three years."),
        ], compact=True),

        S("NIPUN Bharat", "NIPUN Bharat: the national mission", [
            B("The Department of School Education and Literacy launched the National Initiative for "
              "Proficiency in Reading with Understanding and Numeracy (NIPUN Bharat) on 5 July 2021, "
              "under the centrally sponsored scheme Samagra Shiksha (PIB, July 2023). The NEP target "
              "year of 2025 became 2026-27 in the mission."),
            Q("The vision of the Mission is to create an enabling environment to ensure universal "
              "acquisition of foundational literacy and numeracy, so that by 2026-27 every child "
              "achieves the desired learning competencies in reading, writing and numeracy at the "
              "end of Grade III and not later than Grade V.", NIPUN),
            TC([P("cyan", "Five tiers",
                  "National, state, district, block or cluster, and school, with the School "
                  "Management Committee and community at the base. The Department is the national "
                  "implementing agency, headed by a Mission Director.")],
               [P("green", "Four areas of focus",
                  "Access and retention in the foundational years; teacher capacity building; "
                  "high quality student and teacher resources; and tracking each child's progress "
                  "towards learning outcomes (PIB, July 2023).")]),
            H("amber", "The goal has moved. By December 2025 the Ministry was describing the mission as "
              "ensuring foundational literacy and numeracy by the end of Grade 2, with lakshya from "
              "Balvatika up to Grade 2, in line with the Foundational Stage (Rajya Sabha replies, PIB, "
              "17 December 2025 and 29 July 2026). Those replies state no target year."),
        ], compact=True),

        S("Lakshya", "NIPUN Bharat's literacy goals by grade", [
            B("NIPUN Bharat expresses its targets as lakshya, learning goals for each year from "
              "Balvatika to Grade 3. The literacy goals below are as printed in the mission "
              "document. The Ministry now says the lakshya run from Balvatika up to Grade 2 (PIB, 29 July "
              "2026); the revised list was not available to check, so the 2021 goals are shown."),
            T(["Stage", "Literacy lakshya (NIPUN Bharat, July 2021)"],
              [["Balvatika", "Recognises letters and corresponding sounds; reads simple words "
                "comprising at least 2 to 3 alphabets"],
               ["Grade 1", "Reads small sentences of at least 4 to 5 simple words in an age-appropriate "
                "unknown text"],
               ["Grade 2", "Reads with meaning, 45 to 60 words per minute"],
               ["Grade 3", "Reads with meaning, at least 60 words per minute"]]),
            TC([B("The targets use an unknown text, which rules out reciting the class reader, and "
                  "attach meaning to speed. Both are sound measurement choices.", sm=True)],
               [B("One national words-per-minute figure across 20-plus languages sits uneasily "
                  "with Nag's evidence on akshara scripts and with FLS 2022, which set benchmarks "
                  "per language.", sm=True)]),
        ], compact=True),

        S("School readiness", "Vidya Pravesh: twelve weeks to get ready for Grade 1", [
            B("NEP 2020 para 2.5 notes that many children fall behind within the first weeks of "
              "Grade 1 because they had no quality pre-school. NCERT's response is Vidya Pravesh, "
              "guidelines for a three-month play-based school preparation module (July 2021), "
              "described as an essential component of NIPUN Bharat. It runs for about 12 weeks at "
              "the start of Grade 1, four hours a day, and covers pre-literacy, pre-numeracy, "
              "cognitive and social skills."),
            ST([C("1,80,13,930", "students took part in Vidya Pravesh in 2022-23", "cyan", PIB23),
                C("8,77,793", "schools in which it ran that year", "indigo", PIB23),
                C("16.7%", "of Std I children were underage (5 or below) in 2024, the lowest ever, "
                  "against 25.6% in 2018", "green", ASER)], cols=3),
            H("amber", "ASER 2024 found more than 75% of government primary schools reporting a "
              "school readiness programme before Std I in both the previous and current year. "
              "Reporting that a programme ran is a different thing from children being ready; "
              "check what was done in the room."),
        ], compact=True),

        S("Curriculum and materials", "The NCF for the Foundational Stage and Jadui Pitara", [
            B("The National Curriculum Framework for the Foundational Stage (NCF-FS) was launched on "
              "20 October 2022. The Ministry describes it as the first ever integrated curriculum "
              "framework for children aged 3 to 8 in India, a direct outcome of the 5+3+3+4 "
              "structure. Jadui Pitara, a play-based learning and teaching kit based on it, followed "
              "on 20 February 2023 (PIB, July 2023)."),
            TC([P("cyan", "What a framework does",
                  "Sets the goals, competencies and pedagogy for the stage. States write their own "
                  "curricula and textbooks from it, in their own languages, because education is "
                  "on the Concurrent List.")],
               [P("green", "What a kit does",
                  "Puts materials in the room: games, puppets, story cards, workbooks. A kit is "
                  "only as good as the routine a teacher builds around it.")]),
            H("indigo", "For a practitioner the useful question in any state is simple: which "
              "materials reached which classrooms, and does the timetable give them daily time?"),
        ]),

        S("The RTE Act", "What the RTE Act 2009 says about foundational learning", [
            B("The Right of Children to Free and Compulsory Education Act 2009 gives content to "
              "Article 21A. It does not use the phrase foundational literacy, but several sections "
              "speak directly to how the early grades are taught and assessed."),
            T(["Provision", "What it requires", "FLN relevance"],
              [["s 29(2)(e)", "Learning through activities, discovery and exploration in a child "
                "friendly and child-centred manner", "The legal basis for activity-based pedagogy"],
               ["s 29(2)(f)", "Medium of instruction shall, as far as practicable, be in the "
                "child's mother tongue", "The statutory anchor for mother tongue teaching"],
               ["s 29(2)(h)", "Comprehensive and continuous evaluation of the child's understanding",
                "Ongoing classroom assessment"],
               ["s 24(1)(d)", "Teachers to assess the learning ability of each child and supplement "
                "additional instruction as required", "A duty to diagnose and remediate"],
               ["s 4, proviso", "A child admitted to an age-appropriate class has a right to special "
                "training to be at par with others", "Catch-up for late entrants"]]),
            H("cyan", "Source: " + RTE + ". Section 24(1)(d) is the closest the Act comes to a "
              "teacher's legal duty to teach at the right level."),
        ], compact=True),

        S("Detention", "No detention, and its partial reversal in 2019", [
            B("Section 16 of the RTE Act as enacted said no child shall be held back in any class or "
              "expelled until the completion of elementary education. Critics argued that automatic "
              "promotion moved children up without the foundations. The Right of Children to Free "
              "and Compulsory Education (Amendment) Act 2019 (No. 1 of 2019, assent 10 January 2019) "
              "substituted a new section 16."),
            TC([BL(["s 16(1): a regular examination in Class 5 and Class 8 at the end of every year",
                    "s 16(2): a child who fails gets additional instruction and a re-examination "
                    "within two months",
                    "s 16(3): the appropriate Government may allow schools to hold back a child who "
                    "fails the re-examination, or may decide not to hold back",
                    "s 16(4): no child shall be expelled"], color="cyan")],
               [P("amber", "Why this is an FLN question",
                  "Holding back a Class 5 child who cannot read does nothing for the reading. The "
                  "additional instruction in s 16(2) is the part that could help, and it comes "
                  "three grades after NIPUN Bharat's Grade 3 goal. Remediation earlier is cheaper "
                  "than detention later.")]),
        ]),

        S("Status", "Where the targets stand, as of October 2026", [
            B("NEP 2020's target of universal foundational literacy and numeracy in primary school "
              "by 2025 has passed. NIPUN Bharat's 2021 document set 2026-27, the current school "
              "year, as its target year; Ministry replies since December 2025 describe the goal as "
              "FLN by the end of Grade 2 and give no year. The most recent independent national "
              "measure is ASER 2024."),
            ST([C("27.1%", "of rural Std III children (all schools) could read a Std II text in 2024",
                  "red", ASERRC),
                C("33.7%", "of rural Std III children could do a two-digit subtraction in 2024",
                  "amber", ASER),
                C("80%+", "of government schools visited had a government directive to run FLN "
                  "activities with Std I to II/III", "green", ASER)], cols=3),
            TC([B("Progress since 2022 is real and largest in government schools, which received "
                  "the directives, training and materials. ASER reports more than 75% of schools "
                  "received teaching-learning material or funds for it.", sm=True)],
               [B("Universal FLN within a few years would need the Std III reading rate to go "
                  "from about one in four to nearly all children. The largest two-year rise in "
                  "the state table earlier, Himachal Pradesh's from 23.0% to 49.7%, was about "
                  "27 points.", sm=True)]),
        ]),
        # ===================== SECTION 07 =====================
        DIV("07", "Seven", "Programmes and evidence"),

        S("Smart buys", "What the evidence panel rates as good value", [
            B("The Global Education Evidence Advisory Panel (GEEAP), convened by the FCDO, the World "
              "Bank, UNICEF and USAID, published its 2023 update on cost-effective approaches to "
              "improve learning in low- and middle-income countries. It searched over 13,000 "
              "additional studies and draws on over 550 evaluations in all. Two of its three Great "
              "Buys are about how teaching is organised."),
            T(["GEEAP category", "Examples relevant to FLN"],
              [["Great Buys", "Information on the benefits, costs and quality of education; structured "
                "pedagogy (lesson plans, learning materials and ongoing teacher support); targeting "
                "teaching instruction by learning level, in or out of school"],
               ["Good Buys", "Parent-directed early stimulation (ages 0 to 3); quality pre-primary "
                "education (ages 3 to 5)"],
               ["Promising but limited evidence", "Personalised adaptive software where hardware is "
                "already in schools; community-hired staff added to teaching teams; mobile phones"],
               ["Bad Buys", "Hardware such as laptops or tablets alone; textbooks, extra teachers to cut "
                "class size, buildings, grants or libraries alone, when other problems are not addressed"]]),
            H("amber", "Disclosure worth knowing: the panel is co-chaired by Abhijit Banerjee and includes "
              "Rukmini Banerji of Pratham and Karthik Muralidharan, whose programmes and studies are "
              "among those it rates."),
        ], compact=True),

        S("Teaching at the Right Level", "Teaching at the Right Level: the idea", [
            Q("Teaching at the right level (TaRL) is an approach developed by the Indian NGO Pratham "
              "that aims to build foundational skills in math and reading for all children before "
              "exiting primary school.", "J-PAL, TaRL case study (2019, updated August 2022)"),
            B("The approach regroups children by what they can do, measured with a simple ASER-style "
              "oral test, for a dedicated part of the day. Each group works on the next skill it "
              "needs using activities, games and short texts, and children move up as soon as they "
              "are ready. J-PAL counts six randomised evaluations in seven Indian states "
              "and reports that the approach has reached over 60 million children in India and "
              "Africa."),
            FL(["ASSESS: one-on-one oral test, a few minutes per child",
                "GROUP: by level, across grades if needed",
                "TEACH: level-appropriate activities, daily, for a fixed period",
                "REASSESS: every few weeks; regroup",
                "RETURN: to grade-level teaching once the foundations are in place"]),
        ], compact=True),

        S("Balsakhi", "The first evidence: Vadodara and Mumbai, 2007", [
            B("Abhijit Banerjee, Shawn Cole, Esther Duflo and Leigh Linden evaluated two programmes "
              "in urban Indian schools (\"Remedying education: evidence from two randomized "
              "experiments in India\", Quarterly Journal of Economics 122(3), 2007). The first hired "
              "young women from the community, balsakhis, to teach children lagging behind in basic "
              "literacy and numeracy. The second gave children computer-assisted mathematics."),
            ST([C("0.28 SD", "rise in average test scores from the remedial programme, largest for "
                  "the weakest children", "green", "Banerjee, Cole, Duflo and Linden (2007), QJE 122(3)"),
                C("0.47 SD", "rise in mathematics from computer-assisted learning", "cyan",
                  "Banerjee, Cole, Duflo and Linden (2007)"),
                C("About 0.10 SD", "the remaining gain one year after the programmes ended", "amber",
                  "Banerjee, Cole, Duflo and Linden (2007)")], cols=3),
            TC([TERM("SD (standard deviation)",
                     "Effect sizes in education are reported in standard deviations of the test "
                     "score, so studies with different tests can be compared. 0.2 SD is usually "
                     "read as a meaningful gain for a large programme.")],
               [B("Two lessons from the first study still hold. Teaching weaker children at their "
                  "level works even with lightly trained tutors. And gains fade unless the "
                  "regular classroom builds on them.", sm=True)]),
        ], compact=True),

        S("Jaunpur", "Volunteers and reading camps in Jaunpur, Uttar Pradesh", [
            B("Banerjee, Banerji, Duflo, Glennerster and Khemani tested three ways of involving "
              "communities in Jaunpur district (\"Pitfalls of participatory programs\", NBER Working "
              "Paper 14311, 2008; American Economic Journal: Economic Policy 2(1), 2010). Two gave "
              "information or trained villagers in a testing tool. The third trained local youth "
              "volunteers to run reading camps outside school."),
            TC([P("red", "Information and testing tools",
                  "No impact on community involvement, teacher effort or learning outcomes inside "
                  "the school. Villagers did not use the knowledge to press the school.")],
               [P("green", "Reading camps",
                  "A child who could read nothing at baseline and attended a camp was 60 percentage "
                  "points more likely to decipher letters a year later. One who could read letters "
                  "but not words was 26 points more likely to read and understand a story.")]),
            H("cyan", "The paper reports that after a year all camp attendees who could not read at "
              "all could decipher letters, and 35% of those who started at letters could read and "
              "understand a story. Source: NBER Working Paper 14311."),
        ]),

        S("Scaling in government", "Taking TaRL into government schools", [
            B("Pratham's model worked with volunteers. The question for policy was whether it could "
              "work inside government schools with government teachers. Banerjee, Banerji, Berry, "
              "Duflo, Kannan, Mukerji, Shotland and Walton report a series of trials in four states."),
            T(["State", "Model tested", "Result"],
              [["Bihar and Uttarakhand", "Training government teachers in the method, with Pratham support",
                "Not adopted by teachers despite well-received training"],
               ["Haryana", "Government resource persons trained by Pratham supported teachers; a "
                "dedicated hour for level-based teaching", "Language gain of 0.15 SD"],
               ["Uttar Pradesh", "Pratham volunteers ran 40-day learning camps in school, during school "
                "hours, plus 10-day summer camps", "Gains of 0.61 to 0.70 SD in language and maths"]]),
            TC([B("Source: " + TARL16 + ". Effects are on all students enrolled at baseline.", sm=True)],
               [B("The papers disclose that Rukmini Banerji, a co-author, is CEO of Pratham, and was "
                  "not involved in data collection or analysis.", sm=True)]),
            H("indigo", "The failures matter as much as the successes. A method that is not given "
              "protected time, mentoring and a mandate does not survive contact with a regular "
              "timetable."),
        ], compact=True),

        S("Adaptive software", "Mindspark: software that teaches at the child's level", [
            B("Muralidharan, Singh and Ganimian evaluated Mindspark, an adaptive computer programme "
              "used in after-school centres in Delhi, through a lottery that gave some applicants a "
              "voucher (\"Disrupting education? Experimental evidence on technology-aided "
              "instruction in India\", American Economic Review 109(4), 2019). The software tests "
              "each child and serves content at her actual level, which in their sample was often "
              "several grades below the one she was enrolled in."),
            ST([C("0.37 SD", "higher mathematics scores for lottery winners after 4.5 months", "green",
                  "Muralidharan, Singh and Ganimian (2019), AER 109(4)"),
                C("0.23 SD", "higher Hindi scores over the same period", "cyan",
                  "Muralidharan, Singh and Ganimian (2019)"),
                C("Rs 200", "subsidised monthly fee per student at the centres", "indigo",
                  "Muralidharan, Singh and Ganimian, NBER WP 22923 (2016)")], cols=3),
            TC([B("Absolute gains were similar for all students, so relative gains were much larger "
                  "for academically weaker students, whose learning without the programme was "
                  "close to zero.", sm=True)],
               [B("GEEAP rates this kind of software promising, with limited evidence at scale, "
                  "and only where the hardware is already in schools.", sm=True)]),
        ], compact=True),

        S("Structured pedagogy", "Structured pedagogy: lesson plans, materials and support together", [
            TERM("Structured pedagogy",
                 "GEEAP's definition: a package that includes structured lesson plans, learning "
                 "materials and ongoing teacher support. The parts work as a set; any one alone is "
                 "weaker."),
            B("Nepal ran a national version for reading. Its National Early Grade Reading Program, a "
              "five-year, USD 71 million programme from 2014/15 to 2019/20, aimed to improve reading "
              "in Nepali for children in Grades 1 to 3 of all community (government-funded) schools "
              "in all 77 districts. USAID supported it through a USD 53.8 million contract with RTI "
              "International that worked in 16 target districts (CAMRIS International, Early Grade "
              "Reading Program Performance Evaluation 2019, February 2020)."),
            TC([P("cyan", "What a teacher receives",
                  "A daily lesson plan for each period; graded readers and practice sheets for "
                  "every child; a coach or mentor who visits and observes; short assessments to "
                  "check progress.")],
               [P("amber", "Where it goes wrong",
                  "Scripts too rigid for multigrade rooms; books that arrive after the term starts; "
                  "coaching visits that become inspections. Each is a delivery failure that an "
                  "evaluation of the design will not show.")]),
        ], compact=True),

        S("Neighbours", "Foundational learning in Pakistan, Bangladesh, Nepal and Sri Lanka", [
            B("India's neighbours face the same problem at different levels. Pakistan runs its own "
              "ASER, led by Idara-e-Taleem-o-Aagahi (ITA), on the same household model. The table "
              "brings together what could be checked, with the year each figure refers to."),
            T(["Country", "Measure", "Figure", "Source"],
              [["Pakistan", "Learning poverty", "79.5% (2019)", "World Bank WDI"],
               ["Pakistan", "Class 5 children who can read a Class 2 level text in Urdu or Sindhi",
                "51% (2025)", "ASER Pakistan 2025, reported by Sehar Saeed (ITA), UKFIET, 28 May 2026"],
               ["Bangladesh", "Learning poverty", "51.2% (2022)", "World Bank WDI"],
               ["Sri Lanka", "Learning poverty", "14.8% (2015)", "World Bank WDI"],
               ["Nepal", "National early grade reading programme", "Grades 1 to 3, all 77 districts, 2014/15 to 2019/20",
                "CAMRIS International for USAID (2020)"]]),
            H("cyan", "Sri Lanka's figure, from an older assessment, shows that far lower learning "
              "poverty has been recorded within South Asia. Compare data years before drawing "
              "conclusions across countries."),
        ], compact=True),

        S("Inputs alone", "What does not work on its own", [
            B("GEEAP's Bad Buys include things every school needs. Textbooks, teachers, buildings and libraries "
              "are all needed. The panel's finding is that funding them alone, when other problems "
              "are not addressed, has repeatedly failed to raise learning or has done so at high "
              "cost. Hardware such as laptops and tablets without a change in teaching is in the "
              "same category."),
            TC([P("red", "The input trap",
                  "A district buys graded readers for every school. Teachers, never shown how to use "
                  "them in a daily reading period, keep them in a cupboard to protect them from "
                  "damage. The inventory is complete and the learning is unchanged.")],
               [P("green", "The fix",
                  "Tie every input to a routine: a reading period in the timetable, a teacher "
                  "shown how to run it, and a quick check of whether children are reading the "
                  "books. Input plus practice plus feedback.")]),
            H("amber", "ASER 2024 counted books other than textbooks being used by students in 51.3% "
              "of government primary schools, up from 36.9% in 2018. Being used is the right thing "
              "to count."),
        ]),

        # ===================== SECTION 08 =====================
        DIV("08", "Eight", "Mother tongue and multilingual classrooms"),

        S("The language gap", "The language gap at the classroom door", [
            Q("It is well understood that young children learn and grasp nontrivial concepts more "
              "quickly in their home language/mother tongue.", NEP + ", para 4.11"),
            B("Many South Asian children start school in a language they do not speak at home: a "
              "tribal child in Odisha taught in Odia, a Bhojpuri-speaking child taught in standard "
              "Hindi, a child in Pakistan taught in Urdu or English when the home language is "
              "Pashto or Saraiki. Section 2 showed why this matters: a child can decode a language "
              "she does not understand, and comprehension, the point of reading, stays out of reach."),
            TC([P("cyan", "What NEP 2020 says",
                  "Wherever possible, the medium of instruction until at least Grade 5, and "
                  "preferably till Grade 8 and beyond, will be the home language, mother tongue, "
                  "local language or regional language, in public and private schools alike.")],
               [P("amber", "What it qualifies",
                  "Wherever possible. Where materials do not exist, teachers should still talk "
                  "with children in the home language and use a bilingual approach, including "
                  "bilingual teaching-learning materials.")]),
        ], compact=True),

        S("The law", "What the law says about mother tongue instruction", [
            B("Policy, statute, the Constitution and the Supreme Court each say something different, "
              "and they do not carry the same force. A practitioner designing an FLN programme in a "
              "minority language needs to know which is which."),
            T(["Source", "What it says", "Force"],
              [["Article 350A (inserted by the Constitution (Seventh Amendment) Act 1956)",
                "It shall be the endeavour of every State and local authority to provide adequate "
                "facilities for instruction in the mother tongue at the primary stage to children of "
                "linguistic minority groups", "An obligation of endeavour; the President may issue directions"],
               ["RTE Act 2009, s 29(2)(f)", "Medium of instruction shall, as far as practicable, be in "
                "the child's mother tongue", "Binds the academic authority setting the curriculum"],
               ["NEP 2020, para 4.11", "Home language or mother tongue as medium at least to Grade 5, "
                "wherever possible", "Policy; not enforceable in court"],
               ["State of Karnataka v Associated Management of English Medium Primary and Secondary "
                "Schools (2014) 9 SCC 485", "The State cannot compel the mother tongue as medium of "
                "instruction on unaided and minority schools", "Binding Constitution Bench judgment"]]),
        ], compact=True),

        S("The 2014 judgment", "Associated Management (2014): parents choose the medium", [
            B("Karnataka had made the mother tongue or Kannada the compulsory medium of instruction "
              "in primary classes as a condition of recognising schools. On 6 May 2014 a Constitution "
              "Bench of the Supreme Court, in a judgment delivered by Justice A.K. Patnaik, struck "
              "down that requirement for unaided and minority schools."),
            TC([BL(["Mother tongue, in Article 350A, means the language of the linguistic minority "
                    "group to which the child belongs, as decided by the parent or guardian",
                    "The right to choose the medium of instruction is part of freedom of speech and "
                    "expression under Article 19(1)(a)",
                    "Articles 19(1)(g), 29 and 30 protect the choice in private and minority "
                    "institutions"], color="indigo")],
               [P("amber", "What it means for FLN",
                  "Government schools can be asked to teach in the mother tongue; private unaided "
                  "and minority schools cannot be compelled. NEP 2020's call for private schools to "
                  "follow mother tongue instruction rests on persuasion. Demand for English medium "
                  "among parents is a fact any programme has to work with.")]),
            H("cyan", "Case summary drawn from Columbia University's Global Freedom of Expression "
              "database entry for the judgment, (2014) 9 SCC 485."),
        ], compact=True),

        S("Multilingual rooms", "Teaching in classrooms with several languages", [
            B("A teacher in a Delhi resettlement colony, a Jharkhand village or a tea garden in Assam "
              "may have children speaking four or five home languages. Mother tongue instruction "
              "for each is impossible. NEP 2020 and the government's own description of Vidya "
              "Pravesh point to a multilingual approach instead."),
            Q("Focus is also given on learning in mother tongue or home language and allowing as many "
              "languages as children bring to the classroom, including sign language.",
              PIB23 + ", on Vidya Pravesh"),
            TC([BL(["Let children answer in any language at first",
                    "Build vocabulary lists in two languages with children's help",
                    "Use bilingual storybooks and picture cards"], color="green")],
               [BL(["Recruit local teachers or assistants who speak children's languages (NEP 2020 "
                    "para 2.3 asks for this)",
                    "Teach the school language orally before teaching children to read it",
                    "Include sign language for deaf children"], color="cyan")]),
        ], compact=True),

        S("Tribal languages", "Tribal languages in early grades: Odisha and others", [
            B("Several states have run mother tongue based multilingual education (MTB-MLE) for "
              "tribal children. Gautam Makwana's review of studies published between 2013 and 2024 "
              "(Journal of Indian Education, NCERT, August 2025) reports that Odisha has run MTB-MLE "
              "in languages such as Kui, Saora and Santali, that Chhattisgarh has piloted primers in "
              "Gondi and Halbi, and that Jharkhand has promoted tribal languages in early childhood "
              "education."),
            TC([P("green", "What the review finds",
                  "MTB-MLE improves early literacy and student engagement. The usual design starts "
                  "in the mother tongue, then adds the state language, then English.")],
               [P("red", "What holds it back",
                  "Gaps in teacher training, resource availability and community participation, "
                  "and a lack of sustained political and financial commitment that limits scale.")]),
            H("amber", "The evidence is mostly government reports and field studies, with few "
              "rigorous impact evaluations in India. Treat claims of large gains with care, and "
              "build an evaluation into any new programme."),
        ]),

        S("Language and outcomes", "Why language gaps show up in the test results", [
            B("FLS 2022 assessed Grade 3 reading in 20 languages. The share of children who could "
              "not complete the most basic grade-level tasks ranged from 7% in Punjabi to 42% in "
              "Tamil (FLS 2022 National Report). Language is one cause among several, because each "
              "language sample is also a state school system, but the variation is a reminder that "
              "one national benchmark does not fit all scripts."),
            TC([P("indigo", "Three sources of the gap",
                  "Script complexity (Section 3); mismatch between the home language and the "
                  "school language; and the quality of teaching and materials in that language.")],
               [P("cyan", "Separating them",
                  "Ask children to listen to a story and answer questions, as EGRA's listening "
                  "comprehension subtask does. A child who understands when listening but cannot "
                  "read has a decoding problem. One who cannot understand either has a language "
                  "problem.")]),
            H("green", "For reporting: always state the language of assessment beside any reading "
              "figure. A Grade 3 result in English, Hindi and Tamil measures three different things."),
        ]),

        S("Choosing a language", "Choosing the language of an FLN programme", [
            B("A practical decision table for an NGO or district team. It assumes a government "
              "school system; for private schools, the 2014 judgment means the choice rests with "
              "the school and parents."),
            T(["Situation", "First reading language", "What else to do"],
              [["Home language is the state language", "State language", "Oral English from early "
                "grades; reading English from Grade 3 (NEP 2020 para 4.12)"],
               ["Home language is a dialect close to the state language", "State language",
                "Accept home language talk in class; teach standard vocabulary explicitly"],
               ["Home language is a distinct tribal or minority language with a script and materials",
                "Home language", "Bridge to the state language by Grade 3; train local teachers"],
               ["Home language has no materials", "State language, taught with bilingual support",
                "Local assistants, bilingual word lists, oral storytelling in the home language"],
               ["Many home languages in one room", "State language", "Multilingual routines; group "
                "children by language for oral work"]]),
            H("amber", "Illustrative guidance, built from NEP 2020 paras 4.11 and 4.12 and RTE Act "
              "s 29(2)(f). Test locally before adopting."),
        ], compact=True),

        # ===================== SECTION 09 =====================
        DIV("09", "Nine", "Teachers, materials, coaching and families"),

        S("Teachers", "What teachers need to teach foundational skills", [
            B("NIPUN Bharat relies on the existing teacher workforce. Its main training channel is "
              "NISHTHA, NCERT's integrated in-service training programme, with FLN-specific modules. "
              "The mission document says these will include a module on bridging the language "
              "barrier and teaching in the mother tongue, and one on peer learning and on using "
              "parents as volunteers in schools."),
            TC([P("cyan", "Knowledge",
                  "How reading and number develop (Sections 2 to 4); how the local script works; "
                  "how to run a one-on-one diagnostic; how to group and regroup children.")],
               [P("green", "Practice",
                  "Daily routines for a reading and a maths period; questioning that checks "
                  "understanding; managing several groups at once; keeping simple records.")]),
            H("indigo", "The RTE Act already requires this. Section 24(1)(d) makes it a teacher's "
              "duty to assess the learning ability of each child and supplement additional "
              "instruction as required. Training should make that duty doable."),
        ]),

        S("Coaching", "Coaching works, and gets weaker at scale", [
            B("Matthew Kraft, David Blazar and Dylan Hogan meta-analysed 60 studies of teacher "
              "coaching with causal designs (\"The effect of teacher coaching on instruction and "
              "achievement\", Review of Educational Research 88(4), 2018, pages 547 to 588). Much of "
              "the evidence comes from literacy coaching for pre-kindergarten and elementary teachers "
              "in the United States."),
            ST([C("0.49 SD", "pooled effect of coaching on teachers' instructional practice", "green",
                  "Kraft, Blazar and Hogan (2018), RER 88(4)"),
                C("0.18 SD", "pooled effect on students' academic achievement", "cyan",
                  "Kraft, Blazar and Hogan (2018)"),
                C("A fraction", "average effects of larger effectiveness trials, against smaller "
                  "efficacy trials", "amber", "Kraft, Blazar and Hogan (2018)")], cols=3),
            TC([B("Coaching means an expert observes a teacher's lesson, gives specific feedback "
                  "and models the practice, repeatedly. In India the role usually falls to cluster "
                  "and block resource persons.", sm=True)],
               [B("The scale finding is the warning. A coach with 15 schools can visit often; one "
                  "with 60 schools and administrative duties becomes an inspector.", sm=True)]),
        ], compact=True),

        S("Training at scale", "What training looks like when governments run it", [
            B("Anna Popova, David Evans, Mary Breeding and Violeta Arancibia coded 33 rigorously "
              "evaluated teacher professional development programmes and then 139 government-funded "
              "programmes at scale in 14 countries (\"Teacher professional development around the "
              "world: the gap between evidence and practice\", World Bank Research Observer 37(1), "
              "2022, pages 107 to 136)."),
            TC([P("green", "Features of programmes with larger learning gains",
                  "Participation linked to career incentives; a specific subject focus; lesson "
                  "enactment (teachers practise the lesson during training); initial face-to-face "
                  "training. Implementers also rate follow-up visits as among the most effective "
                  "features.")],
               [P("red", "What at-scale programmes looked like",
                  "Fewer incentives to participate, fewer chances to practise new skills, and less "
                  "follow-up once teachers return to their classrooms. The typical government "
                  "programme differs sharply from the ones the evidence supports.")]),
            H("cyan", "Checklist for any FLN training design: is it subject-specific, do teachers "
              "practise in the session, and who visits the classroom afterwards?"),
        ]),

        S("Small schools", "Small schools and multigrade classrooms", [
            B("FLN materials are often designed for one teacher with one grade. ASER 2024's school "
              "visits show that is not the typical classroom in rural government schools. The RTE "
              "Act's Schedule allows two teachers for a primary school of up to sixty children, so a "
              "small school is by law a multigrade school."),
            ST([C("52.1%", "of government primary schools had fewer than 60 students in 2024, up from "
                  "44% in 2022", "amber", ASER),
                C("Two-thirds", "of Std I and Std II classrooms were multigrade", "red", ASER),
                C("2", "teachers required by the RTE Act Schedule for up to 60 children in Classes 1 "
                  "to 5", "indigo", RTE + ", Schedule")], cols=3),
            TC([B("Multigrade is an advantage for level-based grouping: the teacher is already "
                  "teaching more than one level, and grouping by skill across grades is "
                  "natural.", sm=True)],
               [B("It is a problem for grade-by-grade lesson scripts. Any structured pedagogy "
                  "package for rural India needs a multigrade version.", sm=True)]),
        ], compact=True),

        S("Materials", "Books children can actually read", [
            B("Children learn to read by reading, and they need many easy texts in a language they "
              "know. NEP 2020 para 2.8 calls for enjoyable and inspirational books in all local and "
              "Indian languages, and for school and public libraries, particularly in villages. "
              "NIPUN Bharat adds digital content on DIKSHA, including read-along material, "
              "comprehension items and children's literature from local lore and folk tales."),
            TC([P("cyan", "Graded readers",
                  "Short books ordered by difficulty, so each child reads at her level. Level 1 "
                  "uses only the aksharas taught so far. Without them, a child's only text is a "
                  "textbook several levels too hard.")],
               [P("amber", "Libraries alone",
                  "GEEAP lists libraries among inputs that do not work alone. A shelf of books "
                  "helps when a daily reading period puts them in children's hands and someone "
                  "listens to children read.")]),
            H("green", "ASER 2024: books other than textbooks were being used by students in 51.3% of "
              "government primary schools, against 36.9% in 2018 and 43.9% in 2022."),
        ]),

        S("Time on task", "Teacher and student time", [
            B("Every FLN method assumes that a teacher and the children are in the room, on task, "
              "for a set period each day. ASER 2024 records attendance on the day of its school "
              "visit, and the RTE Act sets rules on staffing and on taking teachers away from "
              "teaching."),
            T(["Measure or rule", "What it says", "Source"],
              [["Teacher attendance", "87.5% in 2024 (85.1% in 2018)", ASER],
               ["Student attendance", "75.9% in 2024 (72.4% in 2018)", ASER],
               ["Pupil-teacher ratio", "Maintained as per the Schedule; teachers not to be deployed "
                "elsewhere", "RTE Act 2009, s 25"],
               ["Non-educational duties", "Only the decennial census, disaster relief and elections",
                "RTE Act 2009, s 27"],
               ["Vacancies", "Not to exceed 10% of sanctioned strength", "RTE Act 2009, s 26"],
               ["PTR goal", "Under 30:1 in every school; under 25:1 in disadvantaged areas",
                "NEP 2020, para 2.3"]]),
            H("indigo", "Section 27 matters this year: the Census of India has a reference date of 1 "
              "March 2027, and census duty is one of the three permitted deployments. Plan FLN "
              "calendars around it."),
        ], compact=True),

        S("Families", "Mothers, households and children's learning", [
            B("Rukmini Banerji, James Berry and Marc Shotland randomly assigned households in India "
              "to adult literacy classes for mothers, training for mothers on helping children learn "
              "at home, or both (\"The impact of maternal literacy and participation programs\", "
              "American Economic Journal: Applied Economics 9(4), 2017, pages 303 to 337)."),
            TC([P("green", "What happened",
                  "All three interventions had significant but modest impacts on children's maths "
                  "scores. Mothers' own scores in language and maths rose, as did a range of "
                  "measures of their involvement in their children's education.")],
               [P("cyan", "What it suggests",
                  "Mothers with little schooling can support learning at home when shown how. "
                  "Effects on children were small, so family programmes work best "
                  "alongside classroom change.")]),
            H("amber", "ASER 2024 found almost 90% of 14 to 16 year olds had a smartphone at home. "
              "Phones open a channel to families for reading activities, with the caveat that "
              "GEEAP still lists mobile phone learning as promising with limited evidence."),
        ]),

        S("Community and data", "Community roles, their limits, and children's data", [
            B("NIPUN Bharat gives panchayats and School Management Committees roles: baseline "
              "analysis to identify struggling learners, ensuring enrolment, connecting volunteer "
              "parents to schools. The Jaunpur study is the caution. Giving communities information "
              "about learning did not, by itself, change what happened in schools."),
            TC([P("indigo", "What works better",
                  "Specific tasks with a clear product: a volunteer runs a reading camp; parents "
                  "listen to a child read for ten minutes; a mela or reading day shows families "
                  "what their child can do. NIPUN Bharat lists school readiness melas and reading "
                  "competitions among community activities.")],
               [P("red", "Children's data",
                  "Child-wise tracking apps hold personal data of children. Under the Digital "
                  "Personal Data Protection Act 2023, s 9(1) will require verifiable parental "
                  "consent before processing a child's data, and s 9(3) will bar tracking or "
                  "behavioural monitoring of children. Section 9 applies from 13 May 2027 "
                  "(G.S.R. 843(E), 13 November 2025); design systems to that standard now.")]),
            H("cyan", "Research use: from 13 May 2027, DPDP Act s 17(2)(b) will exempt processing "
              "necessary for research, archiving or statistical purposes, if the data are not used "
              "for decisions about a specific person and the prescribed standards are met. The "
              "DPDP Rules 2025 follow the same phasing, so treat both as the standard to prepare for."),
        ], compact=True),

        # ===================== SECTION 10 =====================
        DIV("10", "Ten", "A practitioner's toolkit"),

        S("Diagnostic", "A five-minute classroom diagnostic", [
            B("A teacher or programme worker can place every child on a reading and an arithmetic "
              "ladder in about five minutes each, using the same logic as ASER. Make one card in "
              "the school language. Test children one at a time, away from the others, and mark "
              "the highest level each child reaches comfortably."),
            T(["Step", "Reading card", "Number card"],
              [["1", "Ten aksharas: child reads any five", "Numbers 1 to 9: child reads any five"],
               ["2", "Ten common words: child reads any five", "Numbers 11 to 99: child reads any five"],
               ["3", "A four-sentence paragraph at Grade 1 level", "Two two-digit subtractions with borrowing"],
               ["4", "A short story at Grade 2 level", "Two three-digit by one-digit divisions"],
               ["5", "Two questions about the story", "One word problem read aloud by the tester"]]),
            TC([B("Steps 1 to 4 follow the ASER ladder. Step 5 adds comprehension and application, "
                  "which ASER does not test at that level.", sm=True)],
               [B("Repeat at the start, middle and end of the year. Record levels on one class "
                  "sheet so the teacher can see the spread at a glance.", sm=True)]),
        ], compact=True),

        S("Grouping", "From the diagnostic to groups: an Illustrative class", [
            B("Illustrative example. A Grade 3 government school class in a Hindi-medium block has 40 "
              "children. The teacher runs the diagnostic in the first week of the session. Her "
              "results, which roughly follow the ASER 2024 national spread for Std III, are below."),
            T(["Reading level", "Children", "Group and focus"],
              [["Cannot read aksharas", "4", "Group A: sounds, symbols, oral games"],
               ["Aksharas only", "9", "Group A: blending aksharas into words"],
               ["Words", "9", "Group B: short sentences, decodable texts"],
               ["Grade 1 paragraph", "8", "Group C: fluency with short stories"],
               ["Grade 2 story", "10", "Group D: comprehension, writing, grade-level work"]]),
            TC([P("cyan", "Running the groups",
                  "One hour a day for reading. The teacher works directly with Group A, the largest "
                  "need. Groups C and D read in pairs and answer written questions. Group B "
                  "practises with a peer tutor from Group D.")],
               [P("green", "Moving up",
                  "Reassess every three weeks with the same card. A child moves group when she "
                  "reaches the next level. By term end the aim is that Group A is empty.")]),
        ], compact=True),

        S("Choosing an assessment", "Which assessment for which question", [
            B("The most common measurement mistake in FLN work is using a tool built for one "
              "question to answer another. Start from the decision the data will inform, then pick "
              "the instrument."),
            T(["Your question", "Tool", "Why"],
              [["Which children in this class need what?", "ASER-style one-on-one card",
                "Fast, floor-level, places every child; teachers can run it"],
               ["Did our programme raise reading in these 200 schools?", "Adapted EGRA or EGMA, "
                "with a comparison group", "Detailed subtasks, sensitive to change, comparable over time"],
               ["How is the state doing against NIPUN goals?", "State census assessment or PARAKH "
                "results", "Large samples, linked to curriculum competencies"],
               ["How does rural learning compare over time and across states?", "ASER reports",
                "Same household method since 2006, includes out-of-school children"],
               ["Is this child ready for Grade 1?", "Observation during Vidya Pravesh",
                "Play-based; a test is the wrong tool at age 6"]]),
            H("red", "Never use a sample survey to judge an individual teacher or school. EGRA's own "
              "toolkit warns against high-stakes use."),
        ], compact=True),

        S("Decision table", "Which intervention, in which situation", [
            B("A decision table for programme design, built from the evidence in Section 7. Each row "
              "names a common field situation and the option with the strongest support. Treat it "
              "as a starting point for a theory of change, then test it."),
            T(["Situation", "Strongest option", "Evidence"],
              [["Most children in Grades 3 to 5 far below grade level", "Level-based grouping for a "
                "fixed daily period (TaRL)", "Haryana and UP trials; GEEAP Great Buy"],
               ["Teachers willing but unsure how to teach reading", "Structured pedagogy: lesson plans, "
                "readers, coaching", "GEEAP Great Buy"],
               ["Government will not give protected time", "Short intensive camps run by trained "
                "volunteers", "UP learning camps; Jaunpur reading camps"],
               ["Many children start Grade 1 without pre-school", "School readiness programme; quality "
                "pre-primary", "Vidya Pravesh; GEEAP Good Buy"],
               ["Computers already in schools, idle", "Adaptive software in scheduled sessions",
                "Mindspark; GEEAP promising"],
               ["Home language differs from school language", "Mother tongue or bilingual early "
                "reading", "NEP 2020 para 4.11; RTE s 29(2)(f)"]]),
        ], compact=True),

        S("Worked example", "Illustrative worked example: planning a block FLN programme", [
            B("Illustrative example, invented to show the steps; the figures describe no real "
              "block. A block in eastern Uttar Pradesh has 120 government primary schools and 6,000 "
              "children in Grades 3 to 5. A baseline using the ASER card finds that 30% of them can "
              "read a Grade 2 story."),
            FL(["DIAGNOSE: test all 6,000 children in the first month",
                "DESIGN: one dedicated hour daily, groups by level, Grades 3 to 5 together",
                "SUPPORT: 8 block resource persons, each coaching 15 schools fortnightly",
                "MATERIALS: one set of graded readers and number kits per school",
                "REVIEW: reassess at day 60 and day 120; regroup; report by school"]),
            TC([P("cyan", "Target",
                  "Raise the share reading a Grade 2 story from 30% to 50% in one year. The UP "
                  "learning camps' 0.61 to 0.70 SD gains are an upper benchmark from intensive camps; "
                  "Haryana's 0.15 SD is a sober benchmark for a teacher-led hour.")],
               [P("amber", "Risks to plan for",
                  "Census duty in early 2027 (RTE s 27); teacher transfers mid-year; the dedicated "
                  "hour eaten by exam preparation; materials arriving late.")]),
        ], compact=True),

        S("Costing and checking", "Illustrative worked example: costs and monitoring", [
            B("Continuing the Illustrative block example. All figures are invented for the exercise "
              "and should be replaced with local prices. The point is the structure: cost every "
              "component, divide by children reached, and decide in advance what will be checked."),
            T(["Component (Illustrative)", "Cost (Rs)", "Basis"],
              [["Graded readers and number kits", "6,00,000", "Rs 5,000 per school x 120 schools"],
               ["Two-day training for 240 teachers", "4,80,000", "Rs 2,000 per teacher"],
               ["Coaching travel for 8 resource persons", "3,84,000", "Rs 4,000 per month x 12 months x 8"],
               ["Assessment rounds (3) and data entry", "1,80,000", "Rs 10 per child per round x 3 rounds"],
               ["Total", "16,44,000", "About Rs 274 per child per year for 6,000 children"]]),
            TC([BL(["Share of schools running the daily hour (spot checks)",
                    "Share of children reassessed on time",
                    "Coaching visits made against planned"], color="cyan")],
               [BL(["Share of children moving up at least one level",
                    "Share reading a Grade 2 story at endline",
                    "Gap between girls and boys, and between social groups"], color="green")]),
        ], compact=True),

        S("Before you scale", "A checklist before taking a pilot to scale", [
            B("The TaRL scale-up trials showed that a method that works with volunteers can fail with "
              "government teachers, and succeed again when redesigned. Kraft and colleagues found "
              "coaching effects shrink at scale. Use this checklist before expanding any FLN pilot."),
            TC([BL(["Was the pilot run by the people who will run it at scale?",
                    "Does the timetable protect daily time for it, by order?",
                    "Is there a coach for every 15 to 20 schools, with time to visit?",
                    "Are materials in the language children speak, and graded?",
                    "Is there a version for multigrade classrooms?"], color="cyan")],
               [BL(["Is the assessment simple enough for teachers to run themselves?",
                    "Was the evaluation independent of the implementer?",
                    "Do costs per child hold at 10 times the size?",
                    "Is children's data collected with consent and kept to purpose, ready for DPDP Act s 9 "
                    "from 13 May 2027?",
                    "Who in government owns it after the funder leaves?"], color="green")]),
            H("amber", "A yes to every question does not guarantee success. A no to any of them is a "
              "known reason for failure."),
        ]),

        # ===================== SECTION 11 =====================
        DIV("11", "Eleven", "Debates and where next"),

        S("Open debates", "Questions the field has not settled", [
            B("Some questions in foundational learning remain open, and practitioners will meet "
              "strong views on each. The table summarises the debate and what the evidence covered "
              "in this course can and cannot say."),
            T(["Question", "One view", "Another view", "What we know"],
              [["One speed benchmark for all languages?", "Simple, comparable, easy to monitor",
                "Ignores script differences", "Akshara learning is slower (Nag 2007); FLS 2022 set "
                "benchmarks per language"],
               ["English medium from Grade 1?", "Parents demand it for mobility",
                "Children cannot read what they do not understand", "Parents' choice is protected for "
                "private schools (2014 judgment); NEP 2020 favours the mother tongue"],
               ["Technology for FLN?", "Adapts to each child at low marginal cost",
                "Hardware alone has failed repeatedly", "Mindspark worked; GEEAP rates hardware alone "
                "a Bad Buy"],
               ["Deadlines like 2025 or 2026-27?", "Focus effort and attention",
                "Encourage inflated reporting", "NEP 2025 target passed; ASER 2024 shows real but "
                "partial progress"]]),
        ], compact=True),

        S("Reporting", "Common mistakes when reporting foundational learning", [
            B("Foundational learning numbers are quoted widely in proposals, news reports and "
              "government documents, and they are often misread. Each mistake below appears "
              "regularly."),
            T(["Mistake", "Why it misleads", "Do this instead"],
              [["Comparing an ASER share with a PARAKH average", "Different samples, tests and metrics",
                "Quote each with its method and year"],
               ["Quoting learning poverty without its data year", "India's figure rests on 2017 data",
                "State the data year beside the figure"],
               ["Reporting words per minute alone", "Speed without meaning can be drilled",
                "Report fluency with comprehension"],
               ["Calling 70% learning poverty a measured figure", "It was a simulation for 2022",
                "Call it an estimate, as the World Bank does"],
               ["Treating 'programme implemented' as 'children learned'", "Directives and kits are inputs",
                "Report learning outcomes measured on children"],
               ["Ignoring the language of assessment", "Results differ by language and script",
                "Name the language every time"]]),
        ], compact=True),

        S("Summary", "Ten things to take away", [
            TC([BL(["Foundational skills are the base for everything a school teaches; grade 3 is "
                    "the turning point",
                    "Learning profiles in South Asia are shallow and classrooms span five or six "
                    "grade levels",
                    "Reading needs oral language, sound awareness, symbol knowledge, decoding, "
                    "fluency and comprehension",
                    "Akshara scripts take longer to master than alphabets; plan and benchmark "
                    "accordingly",
                    "Number sense and place value come before written procedures"], color="cyan")],
               [BL(["ASER 2024: about one in four rural Std III children reads a Std II text",
                    "NEP 2020 made FLN the first priority; NIPUN Bharat set 2026-27 and now aims at the end of Grade 2",
                    "Teaching at the right level and structured pedagogy are GEEAP Great Buys",
                    "Mother tongue teaching has legal backing in Article 350A and RTE s 29(2)(f), "
                    "limited by the 2014 judgment",
                    "Teachers need practice, coaching and time; inputs alone rarely change learning"],
                   color="green")]),
            Q("Grade 3 is the inflection point by which children are expected to \"learn to read\" so "
              "that they can \"read to learn\" after that.", NIPUN),
            B("Each figure above is sourced on the slide where it first appears. Quote the year "
              "with it: ASER 2026 and later state results will move these numbers.", sm=True),
        ]),

        S("Glossary", "Terms used in this course", [
            B("A short reference list of the terms and acronyms that recur in Indian and South Asian "
              "foundational learning work, with the slide section where each is explained."),
            T(["Term", "Meaning"],
              [["FLN", "Foundational literacy and numeracy: reading with understanding and basic arithmetic"],
               ["Akshara", "The written unit of an alphasyllabary: consonant plus vowel sign, or a conjunct"],
               ["ORF", "Oral reading fluency, usually correct words per minute"],
               ["ASER", "Annual Status of Education Report, Pratham's household survey of rural learning"],
               ["FLS", "Foundational Learning Study 2022, NCERT and Ministry of Education, Grade 3"],
               ["PARAKH", "National Assessment Centre in NCERT, set up 8 February 2023"],
               ["EGRA / EGMA", "Early Grade Reading and Mathematics Assessments, RTI toolkits"],
               ["NIPUN Bharat", "National FLN mission launched 5 July 2021; set 2026-27 for Grade 3, now aims at the end of Grade 2"],
               ["Vidya Pravesh", "Twelve-week play-based school preparation module for Grade 1"],
               ["TaRL", "Teaching at the Right Level, Pratham's level-based grouping method"],
               ["Learning poverty", "Share of 10-year-olds unable to read and understand a simple text"]]),
        ], compact=True),

        S("Where next", "Related ImpactMojo 101 decks", [
            B("Foundational learning connects to child development, education systems, rights and "
              "evaluation methods. These decks take each thread further, in the same format and "
              "with the same South Asian focus."),
            TC([BL(["Education systems: " + L("education-policy.html", "Education Policy 101") + ", "
                    + L("edu-pedagogy.html", "Education &amp; Pedagogy 101"),
                    "Early years: " + L("child-development.html", "Child Development 101") + ", "
                    + L("sel-basics.html", "SEL Basics 101"),
                    "Who gets left out: " + L("inclusive-education.html", "Inclusive Education 101")
                    + ", " + L("disability-inclusion.html", "Disability Inclusion 101") + ", "
                    + L("social-margins.html", "Social Margins 101"),
                    "Rights: " + L("child-rights.html", "Child Rights 101") + ", "
                    + L("ind-constitution.html", "Indian Constitution 101")], color="cyan")],
               [BL(["Evidence: " + L("impact-eval.html", "Impact Evaluation 101") + ", "
                    + L("causal-inference.html", "Causal Inference 101") + ", "
                    + L("cost-effectiveness.html", "Cost Effectiveness 101"),
                    "Measurement: " + L("irt-basics.html", "Item Response Theory 101") + ", "
                    + L("survey-design.html", "Survey Design 101") + ", "
                    + L("mel-basics.html", "MEL Basics 101"),
                    "Design: " + L("programme-design.html", "Programme Design 101") + ", "
                    + L("toc-workbench.html", "Theory of Change 101"),
                    "Data: " + L("data-protection-dpdp.html", "Data Protection &amp; the DPDP Act 101")],
                   color="green")]),
            H("indigo", "Item Response Theory 101 explains how large learning surveys place different "
              "test forms on one scale; Cost Effectiveness 101 shows how to compare programmes per "
              "rupee."),
        ]),

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Foundational Literacy &amp; Numeracy 101 &middot; Complete",
         "headline": "Find where each child is,<br>then teach from there",
         "byline": "Reading and number are the base every later lesson stands on. Test one child at "
                   "a time, teach at the level you find, give teachers time and coaching, use the "
                   "language children speak, and report what children can do. Explore the rest of "
                   "the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
