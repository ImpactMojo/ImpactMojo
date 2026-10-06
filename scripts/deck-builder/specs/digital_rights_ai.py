# -*- coding: utf-8 -*-
"""
Digital Rights & AI 101 - ImpactMojo 101 Series (native deck spec)
One combined deck on digital rights and on AI and society, for development
practitioners in South Asia: rights online, the Indian constitutional cases,
internet shutdowns, blocking and platform rules, surveillance and facial
recognition, digital public infrastructure and access, online harms, what AI
systems are and how they fail, AI in welfare, work and elections, AI
governance, and a digital-rights and AI risk assessment for a programme.
Build: python3 scripts/deck-builder/build.py digital_rights_ai

Every figure and citation was checked against a source that was opened and
read (October 2026). The list is in the build report.
Companion decks: digital-ethics, data-protection-dpdp, genai-practitioners.
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


def quote(text, attr):
    return {"t": "quote", "text": text, "attr": attr}


def D(num, label, title):
    return {"type": "divider", "num": num, "label": label, "title": title}


def link(file, name):
    return '<a href="/101-courses/%s">%s 101</a>' % (file, name)


KIO25 = "Access Now, KeepItOn report on internet shutdowns in 2025 (31 March 2026)"
KIO24 = "Access Now, KeepItOn report on internet shutdowns in 2024"
NFHS6 = "IIPS, NFHS-6 (2023-24) National Fact Sheet, May 2026"
CMST = "MoSPI, Comprehensive Modular Survey: Telecom 2025 (NSS 80th round), press note 29 May 2025"

# ===================== SECTION 01: RIGHTS ONLINE =====================
S01 = [
    D("01", "Section One", "Rights online: the starting point"),

    C("Definition", "Digital rights are human rights exercised through technology", [
        body("A <strong>digital right</strong> is an existing human right as it applies when people speak, "
             "organise, learn, earn, prove who they are or receive welfare through a network. There is no "
             "separate catalogue. The right to free expression covers a WhatsApp forward. The right to "
             "privacy covers a biometric record. The right to food covers a ration card that depends on an "
             "online authentication. What changes online is scale, speed and who sits in the middle: a "
             "telecom operator, a platform, a government database."),
        term("Digital rights",
             "The rights to expression, information, privacy, association, equality and due process, and the "
             "economic and social rights that now depend on digital systems, applied to conduct that runs "
             "through networks, devices and data."),
        tw(pp("cyan", "Rights-holders", "Users and non-users alike: the woman whose ration needs a "
              "fingerprint match, the student whose exam centre loses its connection, the person who never "
              "went online but whose face is in a police database."),
           pp("indigo", "Duty-bearers", "The state first, through ministries, police and regulators. Then "
              "private intermediaries, which carry out state orders and write their own rules, and which "
              "human rights law increasingly expects to respect rights.")),
    ]),

    C("The texts", "Two articles of the 1948 Declaration that now govern the internet", [
        body("The Universal Declaration of Human Rights predates the internet by decades, yet two of its "
             "articles were drafted broadly enough to travel. Article 19 protects expression through "
             "<em>any media and regardless of frontiers</em>, which covers a post read in another country. "
             "Article 12 protects privacy and correspondence, which covers messages, call records and "
             "location data. Read them side by side, because most digital disputes set one against the "
             "other or against a claim of security."),
        tw([quote("Everyone has the right to freedom of opinion and expression; this right includes freedom "
                  "to hold opinions without interference and to seek, receive and impart information and "
                  "ideas through any media and regardless of frontiers.",
                  "Universal Declaration of Human Rights, Article 19 (1948)")],
           [quote("No one shall be subjected to arbitrary interference with his privacy, family, home or "
                  "correspondence, nor to attacks upon his honour and reputation.",
                  "Universal Declaration of Human Rights, Article 12 (1948)")]),
        hbox("The binding versions sit in Articles 19 and 17 of the International Covenant on Civil and "
             "Political Rights. Resolution 20/8, on the next slide, ties online expression to both texts.",
             "indigo"),
    ]),

    C("The UN position", "The Human Rights Council: the same rights offline and online", [
        body("The UN Human Rights Council settled the basic principle in 2012 and has repeated it since. "
             "Its resolutions are not treaties, so they do not bind a state the way a Covenant does. They "
             "matter because the Council adopted them without a vote, so no member objected to the wording, "
             "and because UN experts and national courts cite them "
             "when they read the treaties."),
        table(["Resolution", "Adopted", "What it says"], [
            ["20/8, The promotion, protection and enjoyment of human rights on the Internet",
             "5 July 2012, without a vote",
             "Affirms that the same rights that people have offline must also be protected online, in "
             "particular freedom of expression"],
            ["32/13, same title", "1 July 2016, without a vote",
             "Condemns unequivocally measures to intentionally prevent or disrupt access to or "
             "dissemination of information online in violation of international human rights law"],
        ]),
        body("Source: resolution texts A/HRC/RES/20/8 and A/HRC/RES/32/13, read on RightDocs (HURIDOCS). The "
             "2016 wording is the one advocates quote against internet shutdowns, covered in Section 03.",
             sm=True),
    ]),

    C("Four families", "Four families of digital rights a programme will meet", [
        body("Lists of digital rights run long. For field work four families cover almost every case. "
             "Each one has a home in the Indian Constitution, which is why later sections keep returning to "
             "Articles 14, 19 and 21. The examples are from South Asian practice and each one appears again "
             "later in the deck with its source."),
        table(["Family", "Constitutional home in India", "Where it shows up in development work"], [
            ["Access and connectivity", "No standalone right to internet access; Anuradha Bhasin (2020) protects speech and trade through the internet under Article 19(1)(a) and (g)",
             "Internet shutdowns, the gender gap in phone ownership, offline fallbacks for welfare"],
            ["Expression and information", "Article 19(1)(a), limited only by Article 19(2)",
             "Blocking orders, takedowns of NGO content, the fact check unit, deepfakes in elections"],
            ["Privacy and data", "Article 21, as read in Puttaswamy (2017)",
             "Beneficiary databases, biometric authentication, surveillance, facial recognition"],
            ["Equality and due process", "Articles 14 and 21",
             "Algorithms that cut people from welfare lists without notice or a hearing"],
        ]),
        hbox("A fifth set, economic and social rights, runs through all four: food, work and social security "
             "now reach many people only through digital systems.", "green"),
    ]),

    C("Why it matters", "Why a development programme cannot treat digital rights as somebody else's job", [
        body("Many programmes now deliver through digital channels: payments by direct benefit transfer, "
             "attendance by app, grievance by toll-free number and portal, training by WhatsApp. Each "
             "channel creates two kinds of exposure. The programme can be harmed by a rights violation it did "
             "not cause, such as a shutdown that stops payments. It can also cause harm itself, by collecting "
             "more data than it needs or by trusting a score it cannot explain."),
        tw(pp("amber", "Harms done to the programme", "A district shutdown during exams halts cash "
              "transfers. A blocking order takes down a campaign page. A platform removes a survivor support "
              "group after mass reporting. None of these is the programme's fault, and each needs a plan."),
           pp("red", "Harms done by the programme", "A beneficiary list leaks. A photo of a child is posted "
              "with her village named. An eligibility score drops a widow from a pension list. These are "
              "duties the organisation owes, and a donor or court will ask about them.")),
        hbox("The practical tool for both is the risk assessment in Section 11. The sections before it give "
             "you the law and the evidence you will need to fill it in.", "cyan"),
    ]),

    C("The test", "The three-part test for any limit on a digital right", [
        body("Most digital rights may be limited. Speech can be restricted for public order, privacy can "
             "yield to criminal investigation. What human rights law and the Indian Supreme Court both "
             "require is that a limit pass a test. The wording differs between the Human Rights Committee in "
             "Geneva and the Supreme Court in Delhi. The structure is the same, and it is the single most "
             "useful idea in this deck."),
        flow(["LEGALITY: a law, public and precise, authorises the measure",
              "LEGITIMATE AIM: the measure pursues a purpose the law allows, such as public order",
              "NECESSITY: no less restrictive measure would do the job",
              "PROPORTIONALITY: the harm to the right is in balance with the benefit"]),
        tw(pp("cyan", "In Indian law", "Puttaswamy (2017) set out legality, legitimate aim and "
              "proportionality for privacy. Anuradha Bhasin (2020) applied proportionality to internet "
              "suspension. Section 02 reads both."),
           pp("green", "How to use it", "Put any measure your programme faces, or proposes, through the "
              "four steps in order. A measure that fails at step one fails outright, however good its aim.")),
    ]),

    C("This deck and its neighbours", "How this deck fits with three other ImpactMojo decks", [
        body("This deck was written to sit beside three existing decks and to repeat as little of them as "
             "possible. It covers the rights side (courts, shutdowns, blocking, surveillance, access) and "
             "the society side of AI (bias, welfare automation, labour, elections, governance). The others "
             "go deeper on ethics, data protection compliance and day-to-day use of generative AI."),
        tw(pp("cyan", "Read alongside",
              link("digital-ethics.html", "Digital Ethics") + " covers privacy by design, Aadhaar and "
              "exclusion, data colonialism and misinformation. " +
              link("data-protection-dpdp.html", "Data Protection &amp; the DPDP Act") + " is the compliance "
              "manual for the 2023 Act and the 2025 Rules."),
           pp("indigo", "And for daily AI use",
              link("genai-practitioners.html", "GenAI for Practitioners") + " teaches prompting, hallucination "
              "checks and an organisational AI policy. This deck asks the prior question: whether an AI system "
              "should touch a decision about people at all.")),
        hbox("All dates and figures in this deck are stated as of October 2026. Law in this field moves "
             "monthly, so check the date on any rule before you rely on it.", "amber"),
    ]),
]

# ===================== SECTION 02: CONSTITUTIONAL LAW =====================
S02 = [
    D("02", "Section Two", "Speech and privacy in the Indian Constitution"),

    C("Article 19", "Article 19(1)(a) and the eight grounds in Article 19(2)", [
        body("Article 19(1)(a) guarantees every citizen freedom of speech and expression. Article 19(2) lets "
             "the state impose <strong>reasonable restrictions</strong> only on listed grounds. The list is "
             "closed: a restriction that does not fit one of the grounds fails, however sensible it looks. "
             "That is why so many digital speech cases turn on whether a law was tied to one of these words."),
        table(["Ground in Article 19(2)", "A digital case it has been used for"], [
            ["Sovereignty and integrity of India; security of the State", "Blocking of apps and accounts under IT Act s69A"],
            ["Friendly relations with foreign States", "Blocking of content about another country"],
            ["Public order", "Internet suspension during protests, the ground examined in Anuradha Bhasin"],
            ["Decency or morality", "Obscenity offences in IT Act ss67 and 67A"],
            ["Contempt of court; defamation", "Takedown of posts about judges or private persons"],
            ["Incitement to an offence", "Blocking of posts calling for violence"],
        ]),
        hbox("Annoyance, inconvenience and offence are absent from the list. That gap is what decided "
             "Shreya Singhal, on the next slide.", "amber"),
    ], compact=True),

    C("Shreya Singhal (2015)", "Shreya Singhal v Union of India (2015): section 66A falls", [
        body("Section 66A of the Information Technology Act 2000 made it an offence to send, by computer or "
             "phone, information that was grossly offensive, or that caused annoyance, inconvenience or "
             "insult. The Court found its expressions completely open-ended, so almost any critical post could "
             "fall within them. On 24 March 2015 the Supreme Court "
             "struck it down. The words were too vague for a citizen to know what was forbidden, and the "
             "harms they named did not fit any ground in Article 19(2)."),
        quote("Section 66A of the Information Technology Act, 2000 is struck down in its entirety being "
              "violative of Article 19(1)(a) and not saved under Article 19(2).",
              "Shreya Singhal v Union of India, Supreme Court, 24 March 2015, para 119"),
        tw(pp("cyan", "The vagueness point", "A criminal law must tell people in advance what is "
              "punishable. Words like annoyance depend on the reader, so the same post can be lawful in one "
              "police station and a crime in another."),
           pp("green", "The chilling point", "A vague law deters lawful speech, because people stay silent "
              "rather than risk arrest. The Court counted that deterrence as a harm in itself.")),
    ]),

    C("What survived", "What Shreya Singhal upheld, which matters as much as what it struck", [
        body("The same judgment upheld the two powers that now carry most online content control in India. "
             "Practitioners often remember only the first half of the case. The second half explains why "
             "blocking orders and takedown requests remain lawful in principle, and what conditions attach "
             "to them."),
        table(["Provision", "Holding in Shreya Singhal (2015)", "What it means now"], [
            ["IT Act s66A", "Struck down in its entirety", "No prosecution can rest on it; it is dead law"],
            ["IT Act s69A and the Blocking Rules 2009", "Constitutionally valid",
             "The Centre may block content for reasons in writing, through a committee procedure"],
            ["IT Act s79 (intermediary safe harbour)", "Valid, with s79(3)(b) read down",
             "A platform must act on actual knowledge from a court order or a government notification "
             "tied to Article 19(2)"],
            ["IT (Intermediaries Guidelines) Rules 2011", "Valid, subject to the same reading down",
             "Replaced in 2021 by the IT Rules, Section 04"],
        ]),
        hbox("The reading down of s79 is why a private complaint alone does not oblige a platform to remove "
             "your content. Keep this in mind when a takedown arrives (Section 04).", "indigo"),
    ]),

    C("Puttaswamy (2017)", "Puttaswamy v Union of India (2017): privacy is a fundamental right", [
        body("On 24 August 2017 a nine-judge bench of the Supreme Court held unanimously that privacy is "
             "protected by the Constitution. The case arose from the challenge to Aadhaar, when the Attorney "
             "General argued that two older benches had denied any such right. The Court overruled both. "
             "Every later argument about data, surveillance and digital identity in India starts from this "
             "order."),
        quote("The right to privacy is protected as an intrinsic part of the right to life and personal "
              "liberty under Article 21 and as a part of the freedoms guaranteed by Part III of the "
              "Constitution.",
              "Justice K.S. Puttaswamy (Retd) v Union of India, order of the nine-judge bench, 24 August 2017"),
        tw(pp("cyan", "What was overruled", "M P Sharma v Satish Chandra (eight judges) and Kharak Singh v "
              "State of UP (six judges), to the extent they held that the Constitution does not protect "
              "privacy."),
           pp("green", "What it covers", "The plurality opinion of Justice Chandrachud describes "
              "privacy as spatial control, decisional autonomy and informational control. Informational "
              "control is the part that governs databases and apps.")),
    ]),

    C("The test in Indian words", "Legality, legitimate aim, proportionality: Puttaswamy's three-fold test", [
        body("Puttaswamy did more than declare a right. The plurality opinion of Justice Chandrachud set out "
             "a <strong>three-fold requirement</strong> that any state intrusion on privacy must meet, and "
             "later benches have applied it to Aadhaar, to surveillance and to internet suspension. It is "
             "the Indian version of the test on slide 9, and it is the frame to use when a government scheme "
             "asks your programme for beneficiaries' data."),
        flow(["LAW: the intrusion must rest on a law, which an executive instruction does not satisfy",
              "NEED: the law must pursue a legitimate state aim",
              "PROPORTION: the means must be proportionate to the aim"]),
        tw(pp("indigo", "Why legality comes first", "A scheme guideline or an office memorandum is not a "
              "law passed by a legislature. Data collection that rests only on such a document is exposed at "
              "the first step."),
           pp("amber", "Legitimate aims the Court accepted", "The plurality opinion names a vital state "
              "interest in making sure scarce public resources reach those who qualify, which covers most "
              "welfare data collection. The aim is rarely the weak point; proportion usually is.")),
    ]),

    C("Aadhaar (2018)", "The Aadhaar judgment (2018): upheld for welfare, limited for private use", [
        body("A five-judge bench decided the Aadhaar challenge itself on 26 September 2018. The majority "
             "upheld the Aadhaar Act for welfare benefits and subsidies, applying the Puttaswamy test. It "
             "struck down the part of section 57 that let a body corporate or a private person demand "
             "Aadhaar authentication under a contract, which is why a phone company or a bank can no longer "
             "make Aadhaar a condition of service on its own say-so."),
        tw(pp("cyan", "What the majority accepted", "Using Aadhaar to target subsidies and benefits from "
              "the Consolidated Fund of India is a legitimate aim, and authentication for that purpose is "
              "proportionate."),
           pp("red", "What it did not settle", "Exclusion when authentication fails. The fingerprint that will "
              "not match, the network that drops, the elderly hand worn smooth by labour. These are failures "
              "of practice, and they are where programmes meet Aadhaar most often.")),
        hbox("This deck does not repeat the exclusion evidence. " +
             link("digital-ethics.html", "Digital Ethics") + " covers authentication failure and the case for "
             "a non-digital fallback in its Section 6.", "indigo"),
    ]),

    C("Anuradha Bhasin (2020)", "Anuradha Bhasin v Union of India (2020): the internet and proportionality", [
        body("After the changes to Jammu and Kashmir's status on 5 August 2019, the internet was suspended "
             "across the region. Anuradha Bhasin, executive editor of the Kashmir Times, could not publish "
             "the Srinagar edition. The Supreme Court decided her petition on 10 January 2020. It did not "
             "order the internet restored, which disappointed many. What it did was set rules that now bind "
             "every suspension order in India."),
        tw([panel("cyan", "What the Court held", [bullets([
                "Expression through the internet is part of Article 19(1)(a)",
                "Any restriction must satisfy Article 19(2) and be proportionate",
                "An order suspending internet services indefinitely is impermissible",
                "Suspension orders must be published so that people can challenge them"], sm=True)])],
           [panel("green", "What it directed", [bullets([
                "Publish all suspension orders in force and future orders",
                "Review committees to review suspensions every seven working days",
                "Review all existing suspension orders forthwith",
                "Revoke orders not in line with the judgment"], sm=True)])]),
        body("Source: Anuradha Bhasin v Union of India, Supreme Court, 10 January 2020, paras 26 and 152.",
             sm=True),
    ]),

    C("The region", "Four neighbours, four speech laws written since 2024", [
        body("India is one of several South Asian states rewriting online speech law at the same time. The "
             "neighbours are moving in different directions, and a regional programme cannot assume one "
             "country's rules carry across a border. Check the current status in each country before you "
             "rely on this table: two of these laws are under revision."),
        table(["Country", "Law", "What changed", "Status as of October 2026"], [
            ["Bangladesh", "Cyber Security Ordinance 2025", "Repealed the Cyber Security Act 2023; recognises "
             "internet access as a civic right", "Gazetted 21 May 2025 by the interim government; check its "
             "standing after the 2026 Parliament"],
            ["Pakistan", "Prevention of Electronic Crimes (Amendment) Act 2025",
             "New s26A: false information likely to cause fear, panic or unrest, up to three years and Rs 2 "
             "million fine", "In force from 29 January 2025"],
            ["Sri Lanka", "Online Safety Act No. 09 of 2024", "Created an Online Safety Commission over "
             "prohibited statements", "In force since February 2024; amendments under consultation in 2025"],
            ["Nepal", "Social media registration requirement", "At least 26 social media platforms blocked in 2025",
             "Triggered mass protests met with lethal force (Access Now 2026)"],
        ]),
        body("Sources: Prothom Alo (gazette report, May 2025); Deccan Herald/PTI, 29 January 2025; ICJ "
             "submission, 12 September 2025; " + KIO25 + ".", sm=True),
    ], compact=True),
]

# ===================== SECTION 03: INTERNET SHUTDOWNS =====================
S03 = [
    D("03", "Section Three", "Internet shutdowns in South Asia"),

    C("Definition", "What counts as a shutdown, and why the form matters", [
        body("A shutdown is a deliberate disruption of internet or mobile services by, or on the orders of, "
             "an authority, aimed at a population or a place. It need not be total. Some of the most "
             "damaging forms leave a connection in place but make it useless. The form matters to a "
             "programme because each one breaks different things, and because the legal route to challenge "
             "it differs."),
        tw([panel("red", "Full or regional blackout", [body(
                "All mobile and fixed internet off in a district or a state. Payments, telemedicine, online "
                "classes and grievance portals stop together. Voice calls and SMS may survive, which is why "
                "an SMS fallback is worth designing.", sm=True)]),
            panel("amber", "Mobile data only", [body(
                "Broadband stays on for offices and banks; mobile data goes off. Since most rural users are "
                "online only through mobile data, this falls hardest on them.", sm=True)])],
           [panel("indigo", "Throttling", [body(
                "Speeds cut to 2G levels. Text loads, video and document uploads fail. Harder to prove and "
                "easy for authorities to deny.", sm=True)]),
            panel("cyan", "Platform blocks", [body(
                "One or more apps blocked while the rest of the internet works. Nepal blocked at least 26 "
                "social media platforms in 2025 (" + KIO25 + ").", sm=True)])]),
    ], compact=True),

    C("The global count", "2025: the highest number of shutdowns ever recorded", [
        body("Access Now, a digital rights organisation that coordinates the #KeepItOn coalition, has "
             "counted shutdowns every year since 2016 from reports by its partners, network measurement and "
             "the press. Its count for 2025 was the highest in its records. The Asia Pacific region, which in "
             "its classification includes South Asia and Myanmar, accounted for most of them."),
        stats([
            {"num": "313", "label": "shutdowns worldwide in 2025", "color": "red", "source": KIO25},
            {"num": "52", "label": "countries imposed at least one", "color": "amber", "source": KIO25},
            {"num": "195", "label": "in Asia Pacific, across 11 countries", "color": "indigo", "source": KIO25},
        ]),
        tw(pp("cyan", "How to read the count", "A shutdown is counted per order or event, so one long "
              "regional blackout and one two-hour exam shutdown each count as one. The count measures how "
              "often authorities reach for the tool, which is different from how many people lose access."),
           pp("amber", "For comparison", "Access Now's 2024 report counted 296 shutdowns in 54 "
              "countries, a record at the time; its 2025 report revises the 2024 total to 304. Not a single day of 2025 passed without at least one shutdown somewhere (" + KIO24 +
              "; " + KIO25 + ").")),
    ]),

    C("South Asia", "Shutdowns in South Asia and Myanmar, 2024 and 2025", [
        tw([{"t": "chart", "canvas": "draiShutdowns", "type": "bar",
             "title": "Internet shutdowns counted by Access Now",
             "source": KIO24 + "; " + KIO25,
             "data": {"labels": ["Myanmar", "India", "Pakistan", "Nepal"],
                      "datasets": [
                          {"label": "2024", "data": [85, 84, 21, 1], "backgroundColor": "#6366F1"},
                          {"label": "2025", "data": [95, 65, 20, 2], "backgroundColor": "#0EA5E9"}]},
             "options": {"__js__": "{ plugins:{ legend:{ position:'bottom' } }, scales:{ y:{ beginAtZero:true } } }"}}],
           [body("Myanmar's military imposed at least 95 shutdowns in 2025, many in areas of active "
                 "conflict. India imposed 65, down from 84 in 2024, still more than one a "
                 "week. Pakistan imposed 20, against 21 in Access Now's 2024 report (revised to 22 in its 2025 report).", sm=True),
            body("Bangladesh imposed 5 shutdowns in 2024, including the blackout during the July quota-reform "
                 "protests. Access Now's 2025 release gives no Bangladesh count; it records instead that "
                 "advocacy there led to proposed legislation to prohibit shutdowns altogether.", sm=True)],
           ratio="a32"),
        hbox("India's fall from 84 to 65 is real. Read the trend with the level, and "
             "ask how many people each order reached, which the count does not show.", "amber"),
    ]),

    C("Why they happen", "Protests, conflict, exams: the stated reasons", [
        body("Authorities give a small set of reasons, and Access Now's annual reports track them. Each "
             "reason has a different link to the Article 19(2) grounds and a different answer under the "
             "proportionality test. An exam shutdown, for example, protects the integrity of a test by "
             "cutting off millions of people who are not sitting it, which is hard to call the least "
             "restrictive means."),
        table(["Stated reason", "South Asian example", "Proportionality question"], [
            ["Protests and political unrest", "Bangladesh, July 2024 quota-reform protests",
             "Was the blackout limited in area and time, and published?"],
            ["Active conflict", "Myanmar, most of its 95 shutdowns in 2025",
             "Did it cut off information people needed to stay safe?"],
            ["Exam cheating", "India: five exam shutdowns during government job exams in 2024, matching its "
             "2018 record", "Could invigilation or jammers in exam halls do the job instead?"],
            ["Religious events and security", "Pakistan: mobile suspensions during Muharram",
             "Was a targeted measure available?"],
            ["Platform regulation", "Nepal: 26 platforms blocked in 2025 over registration rules",
             "Was blocking the least restrictive way to enforce registration?"],
        ]),
        body("Sources: " + KIO24 + " (exams, Bangladesh, Pakistan); " + KIO25 + " (Myanmar, Nepal).", sm=True),
    ], compact=True),

    C("Programme impact", "What a shutdown breaks inside a development programme", [
        body("Shutdowns are often discussed as a free-speech issue. For a development programme they are "
             "also an operations issue. A shutdown in a district can stop the mechanisms that carry "
             "entitlements to people, and the people hit hardest are those with no alternative channel. The "
             "table is a planning aid: it lists functions that depend on connectivity and the fallback each "
             "one needs. It carries no figures because no reliable Indian estimate of these costs exists for "
             "recent years."),
        table(["Function", "What fails during a shutdown", "Fallback to plan in advance"], [
            ["Ration and pension authentication", "Online biometric match at the shop or the bank point",
             "Offline or manual authentication with a register, as allowed by the scheme"],
            ["Cash transfers and wages", "Payment confirmation and withdrawals at agents",
             "Cash advance policy and an agreed grace period with the department"],
            ["Monitoring and data collection", "Sync from field apps; dashboards go stale",
             "Apps that store offline; paper forms with later entry"],
            ["Helplines and grievance portals", "Chat and web channels",
             "Voice and SMS numbers, which often survive a data shutdown"],
            ["Remote learning and telemedicine", "Video sessions and uploads",
             "Downloaded content; radio; phone consultations"],
        ]),
    ], compact=True),

    C("The law in India", "The Telecommunications Act 2023 and the suspension rules", [
        body("Until 2024 shutdowns were ordered under section 5(2) of the Indian Telegraph Act 1885 and the "
             "2017 suspension rules that Anuradha Bhasin examined. The <strong>Telecommunications Act "
             "2023</strong> replaced the Telegraph Act. Its section 20, in force from 26 June 2024, lets the "
             "Central or a State Government suspend telecommunication services on the occurrence of a public "
             "emergency or in the interest of public safety. The Internet Freedom Foundation notes that "
             "section 20 is almost identical to the old section 5."),
        table(["Feature", "Telecommunications (Temporary Suspension of Services) Rules 2024"], [
            ["Who may order", "The Union Home Secretary or a State Home Secretary; in unavoidable cases a "
             "Joint Secretary to the Central Government or above, authorised by them, and confirmed within 24 hours"],
            ["How long", "At most 15 days per order"],
            ["Where", "The order must state the geographic area"],
            ["Review", "A review committee meets within five days and may set the order aside"],
            ["Publication", "The order must be published and state its reasons, which tracks Anuradha Bhasin"],
        ]),
        body("Sources: Telecommunications Act 2023, s20; Internet Freedom Foundation, 25 June 2024; "
             "Telecommunications (Temporary Suspension of Services) Rules 2024, G.S.R. 724(E), 22 November 2024, rr2, 3 and 5.", sm=True),
    ], compact=True),

    C("What to do", "A shutdown plan for a programme, in five steps", [
        body("A plan written before a shutdown is worth far more than one written during it, when phones are "
             "down and staff cannot reach each other. The five steps below fit on one page and can be added "
             "to any programme's risk register. Step four uses the publication duty from Anuradha Bhasin: an "
             "unpublished order is itself a breach of what the Supreme Court directed."),
        flow(["MAP: list every function that needs connectivity (use the table two slides back)",
              "FALLBACK: agree offline routes with the department before they are needed",
              "COMMUNICATE: a phone tree and an SMS list so staff and participants get instructions",
              "DOCUMENT: record dates, area and effects; ask for the order under the RTI Act if it is not published",
              "REPORT: share documented effects with a digital rights group or the State Human Rights Commission"]),
        tw(pp("cyan", "What documentation is for", "Courts decide on evidence. A log of missed payments, "
              "closed health sessions and cancelled exams turns a general complaint into a proportionality "
              "argument."),
           pp("amber", "A caution", "Staff should not use VPNs or satellite devices in a way that breaks a "
              "lawful order. Ask a lawyer before you advise anyone to work around a shutdown.")),
    ]),
]

# ===================== SECTION 04: BLOCKING AND PLATFORM RULES =====================
S04 = [
    D("04", "Section Four", "Blocking, intermediaries and platform rules"),

    C("The IT Act", "The four IT Act sections behind most online content control", [
        body("The Information Technology Act 2000 is the main statute for online content in India. Four of "
             "its sections do most of the work. Two let the state act directly (interception and blocking), "
             "one lets it collect traffic data for cyber security, and one sets the terms on which platforms "
             "escape liability for what users post. Learn these four numbers and most news stories about "
             "takedowns become readable."),
        table(["Section", "What it allows", "Who acts", "Penalty for non-compliance"], [
            ["s69", "Interception, monitoring or decryption of information in a computer resource",
             "Central or State Government", "Up to seven years for a person who fails to assist"],
            ["s69A", "Blocking public access to information",
             "Central Government, for reasons recorded in writing", "Up to seven years and fine for an "
             "intermediary that fails to comply"],
            ["s69B", "Monitoring and collecting traffic data for cyber security", "Central Government", "Up to three years and fine for an intermediary that fails to assist"],
            ["s79", "Safe harbour: an intermediary is not liable for third-party content if it meets "
             "conditions", "Platforms, subject to the IT Rules", "Loss of the safe harbour"],
        ]),
        body("Source: Information Technology Act 2000, ss69, 69A, 69B and 79, as amended (text read on Indian "
             "Kanoon).", sm=True),
    ], compact=True),

    C("Section 69A", "How a blocking order under section 69A works", [
        body("Section 69A lets the Central Government direct any agency or intermediary to block public "
             "access to information when it is satisfied that this is necessary or expedient in the interest "
             "of sovereignty and integrity, defence, security of the State, friendly relations with foreign "
             "States or public order, or to prevent incitement to a cognizable offence relating to these. The "
             "grounds track Article 19(2), which is one reason the Supreme Court upheld the section in 2015."),
        tw(pp("cyan", "The safeguards", "Reasons must be recorded in writing. The 2009 Blocking Rules route "
              "requests through a designated officer and a committee, and provide for a hearing to the "
              "originator or intermediary where they can be identified."),
           pp("red", "The weak point", "The Blocking Rules keep requests and actions confidential. The "
              "person whose content is blocked may never see the order or know the reason, which makes a "
              "challenge in court hard to mount.")),
        hbox("If your organisation's page or post disappears in India with a notice citing a legal demand, "
             "ask the platform for the order and the section relied on, and keep every message. Slide 36, at "
             "the end of this section, gives a full checklist.", "indigo"),
    ]),

    C("Safe harbour", "Section 79: why platforms are not liable for every post", [
        body("Section 79 protects an intermediary from liability for content it hosts or carries, provided "
             "it does not start or modify the transmission and it observes due diligence. The protection is "
             "lost if, on receiving actual knowledge, it fails to remove unlawful content. Shreya Singhal "
             "read <em>actual knowledge</em> narrowly: a court order, or a notification from the appropriate "
             "government, relating to the grounds in Article 19(2)."),
        tw([panel("green", "Why the narrow reading protects users", [body(
                "If any complaint counted as knowledge, platforms would remove anything reported to avoid "
                "risk. Mass reporting by a hostile group could then silence a women's rights page or a "
                "Dalit news channel without any legal finding.", sm=True)])],
           [panel("amber", "Why the state wants more", [body(
                "Governments argue that court orders are too slow for viral harm such as deepfakes or calls "
                "to violence. The 2021 IT Rules and their later amendments tighten the due diligence a "
                "platform must show to keep the safe harbour.", sm=True)])]),
        body("Due diligence is the lever. Each new obligation in the IT Rules is enforced by the threat that a "
             "platform which ignores it loses section 79 protection and becomes liable as if it had published "
             "the content itself.", sm=True),
    ]),

    C("The IT Rules 2021", "The IT Rules 2021: due diligence, grievance officers, traceability", [
        body("The Information Technology (Intermediary Guidelines and Digital Media Ethics Code) Rules 2021 "
             "replaced the 2011 guidelines. They set due diligence for all intermediaries and heavier duties "
             "for large social media intermediaries, and a code for digital news and streaming. For "
             "development organisations the parts that matter most are the grievance route a user can use "
             "and the rules on what users may not post."),
        tw([panel("cyan", "Duties that help users", [bullets([
                "Publish rules and a privacy policy in plain terms",
                "Appoint a grievance officer and act on complaints within set times",
                "Remove intimate images of a person on complaint, quickly",
                "Give notice and a chance to respond before some removals by large platforms"], sm=True)])],
           [panel("red", "Duties that raise rights concerns", [bullets([
                "Identify the first originator of messages on large messaging services, on order",
                "Rule 3(1)(b) lists categories of content users must not share, in broad words",
                "A government fact check unit added by the 2023 amendment, later struck down",
                "Shorter takedown deadlines added in 2026"], sm=True)])]),
        hbox("The originator rule is contested by messaging companies because end-to-end encryption would "
             "have to change to comply. Watch for court rulings on it.", "amber"),
    ]),

    C("Kunal Kamra (2024)", "The fact check unit and the Bombay High Court", [
        body("An amendment of 6 April 2023 to Rule 3(1)(b)(v) required platforms to make reasonable efforts "
             "not to host information about the business of the Central Government that a government fact "
             "check unit identified as fake, false or misleading. Comedian Kunal Kamra and others challenged "
             "it. The Bombay High Court's division bench split, so the case went to a third judge."),
        flow(["31 JAN 2024: split decision; Justice G.S. Patel strikes the rule down",
              "Justice Neela Gokhale upholds it, so the bench is divided",
              "20 SEP 2024: Justice A.S. Chandurkar, as third judge, agrees with Patel J",
              "26 SEP 2024: the bench declares the amendment unconstitutional and strikes it down"]),
        tw(pp("cyan", "Why it fell", "Justice Chandurkar found the rule violated Articles 14, 19(1)(a) and "
              "19(1)(g), went beyond the IT Act, and that the words fake, false or misleading, left undefined, "
              "were vague and overbroad."),
           pp("indigo", "The lesson", "The state may not be the judge of truth about its own business. The "
              "same vagueness reasoning that killed section 66A in 2015 decided this case.")),
        body("Source: Kunal Kamra v Union of India, Bombay High Court, judgment of 26 September 2024 reciting "
             "the third judge's opinion of 20 September 2024.", sm=True),
    ], compact=True),

    C("Synthetic media rules (2026)", "The 2026 amendment: labels for synthetic content and a three-hour clock", [
        body("On 10 February 2026 MeitY notified amendments to the IT Rules that bring <strong>synthetically "
             "generated information</strong>, including deepfakes, inside the rules. They took effect on 20 "
             "February 2026, giving platforms ten days to comply. Two changes matter for development "
             "organisations, which both make and suffer from synthetic media."),
        tw([panel("cyan", "Labels and provenance", [body(
                "Platforms that offer tools to create synthetic content must label it and carry provenance "
                "information, and must take reasonable technical steps to prevent synthetic content that "
                "breaks the law, such as child sexual abuse material or impersonation.", sm=True)])],
           [panel("amber", "Three hours", [body(
                "Intermediaries must act on government or court orders, including takedowns, within three "
                "hours of receipt. The earlier window was 36 hours. Three hours leaves little time to check "
                "whether an order is lawful.", sm=True)])]),
        body("If your programme uses AI-generated images or voices in awareness material, label them clearly "
             "now. The ECI applies similar rules to campaign material (Section 09). Source: IT (Intermediary Guidelines and Digital Media Ethics "
             "Code) Amendment Rules 2026, G.S.R. 120(E), Gazette of India, 10 February 2026, rules 1 and 3.", sm=True),
    ]),

    C("X Corp (2025)", "X Corp v Union of India (2025): the Sahyog portal challenge fails", [
        body("X Corp, formerly Twitter, asked the Karnataka High Court to declare that blocking orders can "
             "issue only under section 69A with its procedural safeguards, and that section 79(3)(b) gives no "
             "separate power to order takedowns. It also challenged the <strong>Sahyog portal</strong>, a "
             "government system through which many agencies send removal notices to platforms. On 24 "
             "September 2025 a single judge of the High Court rejected the petition."),
        tw(pp("cyan", "What the court held", "Notices under section 79(3)(b) and Rule 3(1)(d) through the "
              "portal are lawful. Article 19 is available only to citizens, so X Corp, a foreign company, could "
              "not rely on it. The court's view: a platform operating in India must follow Indian law."),
           pp("amber", "Why it matters to NGOs", "Removal notices through the portal can come from many "
              "agencies without the committee procedure of the Blocking Rules. Your content may be removed "
              "on a notice you never see. X Corp's appeal was pending before a division bench in 2026; check its "
              "status before relying on the ruling.")),
        body("Source: X Corp v Union of India, Karnataka High Court, WP 7405 of 2025, 24 September 2025, paras 17.7 "
             "and 25 (read on Indian Kanoon); MediaNama, March 2026, on the appeal.",
             sm=True),
    ]),

    C("When your content is removed", "A checklist for an organisation whose content is blocked or removed", [
        body("Development organisations post survivor testimony, reports on police conduct, election "
             "monitoring and campaign material. All of these can be removed, sometimes lawfully, sometimes "
             "through mass reporting, sometimes by mistake. The steps below follow the legal routes covered "
             "in this section, in the order they are usually useful."),
        table(["Step", "What to do", "Legal hook"], [
            ["1. Preserve", "Screenshot the notice, the content and the dates; export the page data", "Evidence for any later challenge"],
            ["2. Identify the basis", "Ask the platform which law or order it relied on", "IT Rules 2021 grievance process"],
            ["3. Platform appeal", "Use the platform's appeal and its India grievance officer", "IT Rules 2021, grievance officer duties"],
            ["4. Government route", "If a section 69A order is cited, ask for a hearing and the order", "Blocking Rules 2009"],
            ["5. Appellate committee", "Appeal a grievance officer's decision", "Grievance Appellate Committees under the IT Rules"],
            ["6. Court", "Writ petition in a High Court with a lawyer", "Articles 19(1)(a) and 226"],
        ]),
        hbox("Keep a backup of everything you publish. A removed page with no backup is lost even if you win "
             "the appeal.", "green"),
    ], compact=True),
]

# ===================== SECTION 05: SURVEILLANCE =====================
S05 = [
    D("05", "Section Five", "Surveillance, spyware and facial recognition"),

    C("Lawful interception", "Who can intercept communications in India, and who checks", [
        body("India has three statutory routes to intercept or monitor communications. All three are "
             "authorised by the executive and reviewed by executive committees. None requires a warrant from "
             "a judge before the interception begins. This is the feature digital rights groups criticise "
             "most, and it explains why the Pegasus case reached the Supreme Court: a person under "
             "surveillance has no way to know of it, and so no way to challenge it."),
        table(["Power", "Statute", "Authorised by"], [
            ["Interception, detention or disclosure of messages on a public emergency or in the interest of "
             "public safety", "Telecommunications Act 2023, s20(2)", "Central or State Government, or an "
             "officer specially authorised"],
            ["Interception, monitoring or decryption of information in a computer resource",
             "IT Act 2000, s69", "Central or State Government, or an officer specially authorised"],
            ["Monitoring and collecting traffic data", "IT Act 2000, s69B", "Central Government, for cyber security"],
        ]),
        tw(pp("cyan", "What the law requires", "Grounds tied to security and public order, reasons in "
              "writing, and review committees of senior officials."),
           pp("red", "What it lacks", "Prior judicial approval, notice to the person after the fact, and any "
              "published statistics on how many orders are issued each year.")),
    ], compact=True),

    C("Pegasus (2021)", "Manohar Lal Sharma v Union of India (2021): the Pegasus order", [
        body("In July 2021 an international media investigation reported that phone numbers of Indian "
             "journalists, opposition politicians and activists appeared on a list of possible targets for "
             "Pegasus, a spyware product sold to governments. Petitions reached the Supreme Court. The Union "
             "government declined to say on affidavit whether it had used the software, citing national "
             "security. On 27 October 2021 the Court appointed its own technical committee."),
        quote("National security cannot be the bugbear that the judiciary shies away from, by virtue of its "
              "mere mentioning.",
              "Manohar Lal Sharma v Union of India, Supreme Court, 27 October 2021, para 49"),
        tw(pp("cyan", "The committee", "Three technical experts, overseen by retired Supreme Court judge "
              "Justice R.V. Raveendran, assisted by former IPS officer Alok Joshi and a cyber security "
              "expert."),
           pp("indigo", "The principle", "The state may decline to share information that would harm "
              "security, but it must justify that refusal on oath. An omnibus claim of national security does "
              "not end judicial review.")),
    ]),

    C("What the committee found", "The Pegasus committee's report: malware, but no conclusion", [
        body("The committee examined phones submitted by people who believed they had been targeted and "
             "reported to the Supreme Court in 2022. On 25 August 2022 Chief Justice N.V. Ramana read parts "
             "of the report in court. The findings were inconclusive on the question that mattered most, and "
             "the Court recorded a finding about the government's conduct during the inquiry."),
        stats([
            {"num": "29", "label": "phones examined by the technical committee", "color": "cyan",
             "source": "LiveLaw, Pegasus probe committee report, 25 August 2022"},
            {"num": "5", "label": "found infected with some malware", "color": "amber",
             "source": "LiveLaw, 25 August 2022"},
            {"num": "0", "label": "conclusively shown to be Pegasus", "color": "red",
             "source": "LiveLaw, 25 August 2022"},
        ]),
        tw(pp("red", "On cooperation", "The Chief Justice read out that, according to the committee, the "
              "Government of India did not cooperate with it."),
           pp("indigo", "What a practitioner takes from this", "Spyware leaves few traces, and an "
              "investigation without the state's records can rarely settle who used it. Prevention is cheaper "
              "than proof: update phones and protect high-risk staff.")),
    ]),

    C("Facial recognition", "Facial recognition in Indian policing: what the police told the court", [
        body("Delhi Police obtained facial recognition software after the Delhi High Court, in <em>Sadhan "
             "Haldar v NCT of Delhi</em>, allowed it to help trace missing children. In a reply to an RTI "
             "request in February 2020, the police named that judgment as the legal basis for its use of the "
             "technology. By then the same software was being used in other policing, including at protests. "
             "Its accuracy, as the police and the government themselves reported, was low."),
        stats([
            {"num": "2%", "label": "accuracy reported by Delhi Police for the system on trial, 2018", "color": "red",
             "source": "Internet Freedom Foundation, Project Panoptic case study, citing affidavits in the Delhi High Court"},
            {"num": "&lt;1%", "label": "accuracy in 2019, when it could not tell boys from girls", "color": "amber",
             "source": "Internet Freedom Foundation, Project Panoptic, citing the Ministry of Women and Child Development"},
        ]),
        tw(pp("cyan", "Purpose drift", "A tool justified by one humane aim (finding missing children) moved "
              "to another (identifying people in crowds) without a new law or a new court order."),
           pp("red", "Legality gap", "No statute in India authorises police facial recognition as such. "
              "Under Puttaswamy, an intrusion must rest on a law; a court order about missing children is a "
              "thin base for crowd identification.")),
    ]),

    C("Chilling effects", "Why being watched changes what people do, and what that costs", [
        body("Surveillance harms people even when no one is arrested. Someone who believes a protest will be "
             "filmed and matched to a database may stay home. A health worker who believes her messages are "
             "read may stop reporting a supervisor's abuse. Courts call this the <strong>chilling "
             "effect</strong>, and the Supreme Court relied on it in Shreya Singhal. For development work it "
             "shows up as silence in exactly the places where voice is the point."),
        tw([panel("amber", "Where programmes see it", [bullets([
                "Low turnout at public hearings and social audits",
                "Community members refusing to be photographed or recorded",
                "Survivors avoiding online support groups",
                "Field staff unwilling to document police conduct"], sm=True)])],
           [panel("green", "What reduces it", [bullets([
                "Collect less: no faces or names where they add nothing",
                "Tell people exactly who will see their data, and keep to it",
                "Use end-to-end encrypted channels for sensitive reports",
                "Offer anonymous routes for grievances"], sm=True)])]),
        hbox("The point is practical. A programme that makes people feel watched will get worse data and "
             "less participation, whatever its intentions.", "indigo"),
    ]),

    C("Your own data", "Surveillance by design: what your programme collects can be used by others", [
        body("NGOs rarely think of themselves as surveillance actors. Yet many hold location data, phone "
             "numbers, photographs, caste and religion fields, and case notes on survivors and activists. "
             "That data can be demanded by authorities, stolen by attackers or shared by a vendor. The safest "
             "record is the one never made. The table sets common programme data against the way it could be "
             "misused."),
        table(["Data a programme often holds", "How it could be misused", "Safer design"], [
            ["GPS points of household visits", "Mapping of a minority settlement", "Store at village level unless needed"],
            ["Photos at community meetings", "Matching faces to protest footage", "Photograph hands and materials, or seek consent per photo"],
            ["Caste and religion fields", "Targeting, exclusion, profiling", "Collect only where the analysis needs it; separate from names"],
            ["Survivor case notes", "Exposure to the abuser or to police", "Encrypt, restrict access, delete on a schedule"],
            ["WhatsApp group membership", "Lists of activists", "Use broadcast lists; hide numbers; review admins"],
        ]),
        hbox("The DPDP duties that will require much of this (minimisation, security, erasure) apply from 13 May "
             "2027. Start now; " + link("data-protection-dpdp.html", "Data Protection &amp; the DPDP Act") +
             " has the templates.", "green"),
    ], compact=True),

    C("Digital identity", "Aadhaar and exclusion: the question to ask of any ID requirement", [
        body("Digital identity is where surveillance and welfare meet. A unique ID makes it easier to stop "
             "duplicate claims and to pay people directly. It also links records across systems, and when "
             "authentication fails the person carries the cost. The Aadhaar judgment of 2018 upheld its use "
             "for subsidies and benefits; it did not decide what happens to the person whose fingerprint will "
             "not match on the day the ration is due."),
        tw(pp("cyan", "The proportionality question", "For any ID requirement in your programme, ask whether "
              "the same aim could be met with less data or with an alternative proof. If yes, the requirement "
              "fails the third step of the Puttaswamy test as a matter of design, whatever a court might say."),
           pp("green", "Where to read more", link("digital-ethics.html", "Digital Ethics") + " covers Aadhaar "
              "enrolment, authentication failure and the case for a non-digital fallback in detail. This deck "
              "does not repeat it.")),
        flow(["NEED: is identity proof required for this benefit at all?",
              "MINIMUM: which proof, and how little data from it?",
              "FALLBACK: what happens when it fails, and who decides?"]),
    ]),
]

# ===================== SECTION 06: DPI AND ACCESS =====================
S06 = [
    D("06", "Section Six", "Digital public infrastructure and the divide"),

    C("What DPI is", "Digital public infrastructure: shared rails that others build on", [
        body("<strong>Digital public infrastructure (DPI)</strong> is the name India uses for shared digital "
             "systems, built or backed by the state, on which public and private services run. Identity, "
             "payments and document exchange are the classic three. The design choice is that many apps "
             "connect to one rail, so a farmer can be paid by any bank through UPI and show a certificate "
             "from any department through DigiLocker."),
        table(["System", "What it does", "Who runs it", "Rights question it raises"], [
            ["Aadhaar", "Unique identity and authentication", "UIDAI, a statutory authority",
             "Exclusion when authentication fails; linking of records"],
            ["UPI", "Instant account-to-account payments", "NPCI", "Fraud, grievance and redress for small users"],
            ["DigiLocker", "Issued documents held and shared digitally", "MeitY", "Consent to share, and who can see what"],
            ["ONDC", "Open network linking buyer and seller apps", "A government-backed network company",
             "Whether small sellers gain or the largest apps still dominate"],
        ]),
        hbox("DPI is infrastructure, so the rights questions are mostly about governance: who decides the "
             "rules, who hears complaints, and what happens to those who cannot use it.", "indigo"),
    ], compact=True),

    C("UPI", "UPI at scale: a public payment rail used billions of times a month", [
        body("The Unified Payments Interface lets any bank account send money to any other through a phone "
             "number or a QR code. It is run by the National Payments Corporation of India, which publishes "
             "monthly volumes. By 2026 it carries a large share of small payments in India, including many "
             "made by street vendors and self-help groups with whom development programmes work."),
        stats([
            {"num": "24.07 bn", "label": "UPI transactions in September 2026", "color": "cyan",
             "source": "NPCI data, reported by IANS, 1 October 2026"},
            {"num": "Rs 29.37 lakh cr", "label": "value of those transactions", "color": "green",
             "source": "NPCI data, reported by IANS, 1 October 2026"},
            {"num": "802 mn", "label": "average transactions per day in September 2026", "color": "indigo",
             "source": "NPCI data, reported by IANS, 1 October 2026"},
        ]),
        tw(pp("green", "What it made possible", "Low-cost transfers between ordinary accounts, payments to "
              "vendors without card machines, and a record of income that a woman running a small business "
              "can show a lender."),
           pp("red", "What it brought with it", "Fraud by fake payment requests and QR codes. NCRB counted "
              "fraud as the motive in 72.6% of cybercrime cases in 2024 (Section 07). Redress for a small loss "
              "is slow and often absent.")),
    ]),

    C("DigiLocker and ONDC", "DigiLocker and ONDC: documents and markets on shared rails", [
        body("Two other rails reach development work directly. DigiLocker holds documents issued by "
             "departments, such as mark sheets, driving licences and caste certificates, so that a person can "
             "share them without carrying paper. ONDC is a network that lets a seller listed on one app be "
             "found by a buyer on another. One is a document wallet, the other a market protocol, and each "
             "raises its own rights question."),
        tw([panel("cyan", "DigiLocker", [body(
                "The government told the Rajya Sabha in August 2026 that DigiLocker has more than 72.43 crore "
                "registered users, and that UMANG, the app for government services, has more than 11.66 "
                "crore. The rights question is consent: who asks for which document, and whether a person "
                "can refuse.", sm=True),
                body("Source: Free Press Journal, reporting a written reply by IT Minister Ashwini Vaishnaw, "
                     "August 2026.", sm=True)])],
           [panel("green", "ONDC", [body(
                "The promise is that a women's producer collective can sell through any buyer app, on terms it "
                "can compare. The test, for a programme, is whether its members' sales and "
                "margins rise. Order figures are published by ONDC and change monthly; use the latest "
                "release.", sm=True)])]),
        hbox("Both are opt-in for users. Watch for schemes that make them a condition of a benefit, which "
             "turns a convenience into a gate.", "amber"),
    ]),

    C("Governing DPI", "Five governance questions to ask of any digital rail", [
        body("India promotes its DPI model abroad, and other South Asian governments are building similar "
             "systems. Whether a rail serves people well depends less on the technology than on the rules "
             "around it. These five questions apply to a national system and equally to a state scheme portal "
             "or an NGO's own beneficiary app."),
        table(["Question", "What good looks like", "Warning sign"], [
            ["Who sets the rules?", "Rules made under a statute, published, open to comment",
             "Rules in circulars that change without notice"],
            ["Who hears complaints?", "A named grievance officer with time limits and an appeal",
             "A helpline that only logs calls"],
            ["What happens on failure?", "A manual fallback written into the scheme rules",
             "Benefit denied until the system works"],
            ["What data does it keep?", "Minimum data, stated retention, no reuse without law",
             "Logs kept indefinitely and shared across departments"],
            ["Can people opt out?", "An alternative route that is not punished",
             "Digital-only access to an entitlement"],
        ]),
    ], compact=True),

    C("Access by gender", "Who is online: women and men in NFHS-6 (2023-24)", [
        tw([{"t": "chart", "canvas": "draiNfhsNet", "type": "bar",
             "title": "Adults aged 15-49 who have ever used the internet (%)",
             "source": NFHS6,
             "data": {"labels": ["Urban", "Rural", "Total"],
                      "datasets": [
                          {"label": "Women", "data": [77.3, 58.6, 64.3], "backgroundColor": "#F59E0B"},
                          {"label": "Men", "data": [87.1, 77.1, 80.5], "backgroundColor": "#6366F1"}]},
             "options": {"__js__": "{ plugins:{ legend:{ position:'bottom' } }, scales:{ y:{ beginAtZero:true, max:100 } } }"}}],
           [body("The sixth National Family Health Survey, fielded in 2023-24 and published in May 2026, "
                 "found that 64.3% of women aged 15-49 had ever used the internet, almost double the 33.3% in "
                 "NFHS-5 (2019-21). For men the figure is 80.5%.", sm=True),
            body("The gap is widest in rural India: 58.6% of rural women against 77.1% of rural men. NFHS-6 "
                 "also found that 63.6% of women have a mobile phone they themselves use.", sm=True)],
           ratio="a32"),
        hbox("Ever used is a low bar. A woman who once watched a video on her husband's phone counts. "
             "Meaningful use, with her own device, privacy and skills, is lower, and no national survey "
             "measures it directly.", "amber"),
    ]),

    C("Access and skills", "The household picture: CMS Telecom 2025", [
        body("The Comprehensive Modular Survey: Telecom, part of the 80th round of the National Sample "
             "Survey, was fielded from January to March 2025 across 34,950 households. It measures household "
             "access and the digital skills of individuals. Its headline numbers are high, and the press "
             "note's own caveat applies: the survey is designed for national estimates, so state figures "
             "carry wide margins."),
        stats([
            {"num": "86.3%", "label": "households with internet access within the premises", "color": "cyan", "source": CMST},
            {"num": "85.5%", "label": "households with at least one smartphone", "color": "indigo", "source": CMST},
            {"num": "92.7%", "label": "rural 15-29 year olds who used the internet in the last three months (urban 95.7%)",
             "color": "green", "source": CMST},
            {"num": "85.1%", "label": "of 15-29 year olds sent a message with an attached file (77.7% in CAMS 2022-23)",
             "color": "amber", "source": CMST},
        ], cols=4),
        tw(pp("cyan", "Read carefully", "A household counts as connected when any member is. A household with one "
              "smartphone, held by a son, counts as connected while his mother and sister are not."),
           pp("indigo", "Skills are uneven", "Sending an attachment is a basic task. Filling an online form, "
              "spotting a fake payment request or changing privacy settings are harder, and they are what a "
              "digital-by-default scheme demands.")),
    ], compact=True),

    C("The regional gap", "South Asia's mobile internet gender gap, measured by GSMA", [
        body("The GSMA, the mobile industry's association, surveys women and men in low and middle income "
             "countries every year. Its 2026 report, published on 10 June 2026, found the gap narrowing "
             "slightly in 2025, with South Asia still among the two regions where it is widest. Use the "
             "current edition: methods change between reports, so comparing a 2025 figure with a 2026 figure "
             "can mislead."),
        stats([
            {"num": "25%", "label": "women in South Asia less likely than men to use mobile internet",
             "color": "red", "source": "GSMA, Mobile Gender Gap Report 2026 (10 June 2026)"},
            {"num": "810 mn", "label": "women in LMICs not using mobile internet", "color": "amber",
             "source": "GSMA, Mobile Gender Gap Report 2026"},
            {"num": "2&ndash;3x", "label": "how much wider the gap typically is in rural areas", "color": "indigo",
             "source": "GSMA, Mobile Gender Gap Report 2026"},
        ]),
        tw(pp("cyan", "The barriers GSMA reports", "Handset affordability, literacy and digital skills, "
              "and, once online, safety and security concerns, the cost of data and poor coverage."),
           pp("green", "For programme design", "If a service reaches women only through a smartphone app, "
              "assume a quarter fewer women than men can use it, and more in rural areas. Design a voice, SMS "
              "or assisted route from the start.")),
    ]),

    C("Meaningful access", "From ever online to meaningfully connected", [
        body("The surveys on the last three slides count whether people have used the internet. A rights "
             "approach asks a harder question: can a person use it to claim what they are owed, safely and on "
             "their own terms? That depends on device ownership, privacy within the household, language, "
             "skills, cost and safety. A woman who must ask her husband to fill her pension form online has "
             "access in the survey sense and none in the rights sense."),
        tw([panel("amber", "Five tests of meaningful access", [bullets([
                "Own device, used privately",
                "Affordable data for regular use",
                "Content and interfaces in her language",
                "Skills to complete the task without help",
                "Safety from harassment once online"], sm=True)])],
           [panel("green", "What a programme can do", [bullets([
                "Budget for devices or data where use is required",
                "Train on the actual task (a scheme form), with women trainers",
                "Offer assisted access points with privacy",
                "Measure use by each woman, beyond household connection"], sm=True)])]),
        hbox("For the wider case on the digital divide, including disability and language, see " +
             link("digital-ethics.html", "Digital Ethics") + " Section 7 and " +
             link("data-feminism.html", "Data Feminism") + ".", "indigo"),
    ]),
]

# ===================== SECTION 07: ONLINE HARMS =====================
S07 = [
    D("07", "Section Seven", "Online harms: gender-based violence and children"),

    C("The recorded picture", "Cybercrime in India: NCRB's 2024 figures", [
        body("The National Crime Records Bureau's <em>Crime in India 2024</em>, released on 7 May 2026, "
             "recorded more than one lakh cybercrime cases in a year for the first time. These are cases "
             "registered by police, so they measure what was reported and recorded, which is a fraction of "
             "what happened. Fraud dominates the count. Sexual exploitation is a small share of cases and a "
             "large share of the harm to women and children."),
        stats([
            {"num": "1,01,928", "label": "cybercrime cases registered in 2024, up 17.9% from 86,420 in 2023",
             "color": "red", "source": "NCRB, Crime in India 2024, Vol II, Table 9A.1"},
            {"num": "72.6%", "label": "of cases with fraud as the motive (73,987)", "color": "amber",
             "source": "NCRB, Crime in India 2024, Vol II, Table 9A.3"},
            {"num": "3,190", "label": "cases with sexual exploitation as the motive", "color": "indigo",
             "source": "NCRB, Crime in India 2024, Vol II, Table 9A.3"},
        ]),
        tw(pp("cyan", "Rate", "The cybercrime rate rose from 6.2 to 7.3 cases per lakh population "
              "between 2023 and 2024 (NCRB)."),
           pp("amber", "Why the count misleads", "Reporting depends on police capacity and on whether a "
              "victim trusts the station. States with better helplines record more crime. A high count can "
              "mean better access to justice.")),
    ]),

    C("Forms of harm", "Technology-enabled gender-based violence and the law that applies", [
        body("Violence against women increasingly runs through phones: images shared without consent, a "
             "partner tracking her location, threats in comments, fake profiles. Indian criminal law covers "
             "most of these, spread across two statutes. The Bharatiya Nyaya Sanhita 2023 replaced the "
             "Indian Penal Code from 1 July 2024 and carries the general offences; the IT Act carries the "
             "electronic ones."),
        table(["Form of harm", "Main provision", "What it covers"], [
            ["Capturing or sharing intimate images", "IT Act s66E; BNS s77 (voyeurism)",
             "Capturing, publishing or transmitting images of a private area or private act without consent"],
            ["Monitoring a woman's online activity", "BNS s78 (stalking)",
             "A man who monitors a woman's use of the internet, email or other electronic communication"],
            ["Publishing sexually explicit material", "IT Act ss67 and 67A", "Obscene and sexually explicit material in electronic form"],
            ["Material depicting children", "IT Act s67B; POCSO Act 2012", "Child sexual abuse material"],
            ["Impersonation and fake profiles", "IT Act s66D", "Cheating by personation using a computer resource"],
        ]),
        body("Sources: Bharatiya Nyaya Sanhita 2023 and Information Technology Act 2000, texts read on Indian "
             "Kanoon.", sm=True),
    ], compact=True),

    C("Stalking online", "BNS section 78: monitoring as stalking", [
        body("The stalking offence is worth reading in full because it names the most common form of digital "
             "control in intimate relationships. Many women do not know that a partner who installs tracking "
             "software, reads her messages or demands her passwords may be committing an offence. Note the "
             "limits too: the section is written for a man stalking a woman, and it carries an exception for "
             "lawful crime prevention."),
        quote("Any man who ... monitors the use by a woman of the internet, e-mail or any other form of "
              "electronic communication, commits the offence of stalking.",
              "Bharatiya Nyaya Sanhita 2023, section 78(1)(ii)"),
        tw(pp("cyan", "In a programme", "Safety planning with survivors should include a phone check: "
              "unknown apps, shared accounts, location sharing, and who knows the PIN. Train staff to do this "
              "gently and with consent."),
           pp("amber", "The gender limit", "The wording protects women from men. Harassment of trans persons "
              "or between women must be pursued under other provisions, such as criminal intimidation or IT "
              "Act s66E.")),
    ]),

    C("Barriers to redress", "Why women do not report, and what a programme can change", [
        body("The NCRB count of sexual exploitation cases is small next to the scale of harassment women "
             "describe. The gap has known causes. Each cause suggests a design response that a programme "
             "can take without waiting for police reform. Taken together, the pairs on this slide amount to a "
             "simple referral pathway that most women's groups can set up in a month."),
        tw([panel("red", "Why cases are not reported", [bullets([
                "Fear that family will take away her phone",
                "Shame, and fear the images will spread further",
                "Police who advise her to stay offline",
                "No knowledge of which law applies",
                "Platforms that do not respond in her language"], sm=True)])],
           [panel("green", "What helps", [bullets([
                "A trained contact who can explain options privately",
                "Help to report the content to the platform first, quickly",
                "A referral list of lawyers and the cybercrime portal",
                "Evidence preservation before deletion",
                "Peer support that does not depend on the platform"], sm=True)])]),
        hbox("The IT Rules 2021 require platforms to act on a complaint about intimate images of a person. "
             "That route is often faster than a police case, and can run alongside it.", "cyan"),
    ]),

    C("Children's rights online", "UN General Comment No. 25 (2021): children in the digital environment", [
        body("The Committee on the Rights of the Child issued <strong>General Comment No. 25</strong> on "
             "children's rights in relation to the digital environment, dated 2 March 2021. It reads the "
             "Convention on the Rights of the Child, which every South Asian state has ratified, into "
             "digital life. The Committee consulted children while drafting it, and its opening paragraph "
             "reports that children described digital technologies as vital to their lives."),
        tw([panel("cyan", "What the General Comment asks of states", [bullets([
                "Apply the best interests of the child to digital policy",
                "Protect children from exploitation and abuse online",
                "Protect their privacy, including from commercial profiling",
                "Secure their access to information and their right to be heard"], sm=True)])],
           [panel("amber", "The tension for programmes", [body(
                "Protection and participation pull against each other. Blocking every risk would cut "
                "children off from learning and from help. The General Comment asks for both, balanced by "
                "age and capacity, which is the same evolving capacities idea found in Article 5 of the "
                "Convention.", sm=True)])]),
        body("Source: CRC/C/GC/25, 2 March 2021, UN Treaty Body Database. For the wider framework see " +
             link("child-rights.html", "Child Rights") + ".", sm=True),
    ]),

    C("Children's data", "Children's data under the DPDP Act: what applies when", [
        body("The DPDP Act 2023 treats everyone under 18 as a child. Section 9 requires verifiable consent of "
             "a parent or lawful guardian before processing a child's personal data, and bars tracking, "
             "behavioural monitoring and targeted advertising directed at children. These are among the core "
             "duties, so they apply only from <strong>13 May 2027</strong> under G.S.R. 843(E) of 13 November "
             "2025. They are not in force as of October 2026."),
        table(["Date", "What commences (G.S.R. 843(E), 13 November 2025)"], [
            ["13 November 2025", "Definitions, the Data Protection Board (ss18-26), and s44(3) amending the RTI Act"],
            ["13 November 2026", "Section 6(9) and section 27(1)(d)"],
            ["13 May 2027", "Core duties and rights (ss3-17), including s9 on children and the s17 exemptions; "
             "penalties (ss27-34)"],
        ]),
        hbox("Do not wait for May 2027. A programme that photographs children, runs a WhatsApp group for "
             "adolescents or uses an EdTech app should already ask for parental consent and collect the "
             "minimum. " + link("data-protection-dpdp.html", "Data Protection &amp; the DPDP Act") +
             " covers the detail.", "amber"),
    ], compact=True),

    C("Safeguards", "Digital safeguarding for programmes that work with children", [
        body("Most child protection policies in NGOs were written for physical contact. Digital work adds new "
             "risks: staff in private chats with children, photos posted with locations, apps that collect "
             "data the organisation never sees. The table turns General Comment No. 25 and the coming DPDP "
             "duties into practice. It is a minimum; " +
             link("safeguarding-psea.html", "Safeguarding &amp; PSEA") + " has the full framework."),
        table(["Risk", "Safeguard", "Who checks"], [
            ["One-to-one chats between staff and children", "Group channels only, with two adults present", "Safeguarding lead"],
            ["Photos that reveal identity or location", "No faces or names of at-risk children; strip location data", "Communications team"],
            ["Third-party apps collecting children's data", "Review the app's privacy policy and data flows before use", "Programme manager"],
            ["Online abuse disclosed to staff", "Written reporting route, preserved evidence, referral list", "Safeguarding lead"],
            ["Children's own online safety", "Age-appropriate sessions on privacy and reporting, designed with them", "Education staff"],
        ]),
    ], compact=True),
]

# ===================== SECTION 08: WHAT AI IS =====================
S08 = [
    D("08", "Section Eight", "What AI systems are and how they fail"),

    C("Definition", "An AI system, explained for non-technical practitioners", [
        body("Most AI systems in public life are <strong>prediction machines</strong>. They learn patterns from "
             "past data and use them to produce an output for a new case: a score, a category, a match or a "
             "piece of text. They work by resemblance: they find what past "
             "cases with similar features looked like, which is powerful when the past is a good guide and "
             "harmful when the past was unfair."),
        term("AI system (working definition)",
             "Software that infers from the data it receives how to generate outputs such as predictions, "
             "content, recommendations or decisions, which can influence people or environments. This is "
             "close to the wording used in the EU AI Act and the OECD."),
        flow(["DATA: past records, labelled with an outcome",
              "TRAINING: the system finds patterns linking features to the outcome",
              "MODEL: the patterns, stored as numbers",
              "OUTPUT: a score or label for a new person",
              "DECISION: a human or a rule acts on the output"]),
        hbox("The decision step is where rights attach. Ask who acts on the output, and whether they can "
             "override it.", "indigo"),
    ]),

    C("Kinds of AI", "Four kinds of AI a development practitioner will meet", [
        body("The word AI covers systems that work in quite different ways and carry different risks. Sorting "
             "them by what they produce is more useful than sorting them by technique. Generative AI gets the "
             "headlines; scoring and matching systems make more decisions about poor people's lives. The "
             "examples are typical uses in South Asian programmes and public services."),
        table(["Kind", "What it produces", "Example in development", "Main rights risk"], [
            ["Scoring", "A number predicting risk or need", "Ranking households for a benefit; credit scoring for microloans",
             "Wrongful exclusion; bias from proxies"],
            ["Classification", "A category", "Flagging duplicate or ineligible beneficiaries", "False positives that cut people off"],
            ["Matching and recognition", "A link between two records or faces", "Facial recognition; record linkage across databases",
             "Wrong matches; surveillance"],
            ["Generative", "Text, images, audio", "Chatbots for scheme information; drafting reports",
             "Confident wrong answers; deepfakes"],
        ]),
        hbox("For safe daily use of generative tools, see " +
             link("genai-practitioners.html", "GenAI for Practitioners") + ". This deck focuses on systems that "
             "decide about people.", "cyan"),
    ], compact=True),

    C("Where bias enters", "Three doors through which bias enters an AI system", [
        body("Algorithmic bias is a systematic error that falls harder on some groups than others. It is rarely "
             "the result of a programmer's prejudice. It enters through ordinary choices that look technical. "
             "Each door below has a matching question you can ask a vendor or a government department, even "
             "if you cannot read a line of code."),
        tw([panel("amber", "1. The data", [body(
                "If past data under-represents a group, or records the effects of past discrimination, the "
                "system learns them. Ask: whose records trained this, and who is missing?", sm=True)]),
            panel("red", "2. The target", [body(
                "The outcome the system predicts may be a poor proxy for what you care about, such as cost for "
                "need. Ask: what exactly does the score predict?", sm=True)])],
           [panel("indigo", "3. The deployment", [body(
                "A system tested in one population is used on another, or staff treat a score as final. "
                "Ask: where was it tested, and who can override it?", sm=True)]),
            panel("green", "Your bargaining power", [body(
                "These questions belong in the terms of any procurement or partnership. A vendor that cannot "
                "answer them has not done the work.", sm=True)])]),
    ], compact=True),

    C("Obermeyer et al. (2019)", "A health algorithm that predicted cost and missed need", [
        body("Ziad Obermeyer and colleagues studied a commercial algorithm used by US health systems to pick "
             "patients for extra care. It was trained to predict future health care costs, on the reasoning "
             "that sicker people cost more. Because less money had been spent on Black patients with the same "
             "illness, the algorithm ranked them as lower risk. The paper appeared in <em>Science</em> in "
             "October 2019."),
        stats([
            {"num": "17.7%", "label": "share of Black patients flagged for extra help by the algorithm",
             "color": "red", "source": "Obermeyer, Powers, Vogeli and Mullainathan, Science 366:447-453 (2019)"},
            {"num": "46.5%", "label": "share if the disparity were remedied", "color": "green",
             "source": "Obermeyer et al., Science (2019)"},
        ]),
        tw(pp("cyan", "The general lesson", "The authors warn that convenient proxies for ground truth can "
              "be an important source of bias in many contexts. Cost stood in for illness; the gap between "
              "them was the history of unequal access."),
           pp("amber", "The South Asian parallel", "A targeting model trained on past scheme enrolment learns "
              "who was enrolled, which reflects who could reach the office. Households excluded before will be "
              "scored as less eligible.")),
    ]),

    C("Gender Shades (2018)", "Facial analysis error rates by gender and skin type", [
        tw([{"t": "chart", "canvas": "draiGenderShades", "type": "bar",
             "title": "Maximum error rates of commercial gender classifiers (%)",
             "source": "Buolamwini and Gebru, Gender Shades, PMLR 81 (2018)",
             "data": {"labels": ["Darker-skinned women", "Lighter-skinned men"],
                      "datasets": [{"label": "Maximum error rate (%)", "data": [34.7, 0.8],
                                    "backgroundColor": ["#EF4444", "#10B981"]}]},
             "options": {"__js__": "{ plugins:{ legend:{ display:false } }, scales:{ y:{ beginAtZero:true } } }"}}],
           [body("Joy Buolamwini and Timnit Gebru tested three commercial gender classification systems on a "
                 "new dataset balanced by gender and skin type. Darker-skinned women were the most "
                 "misclassified group, with error rates of up to 34.7%. The maximum error rate for "
                 "lighter-skinned men was 0.8%.", sm=True),
            body("The systems were sold as accurate because they were accurate on average. Averages hid the "
                 "group on which they failed, a group under-represented in the data used to build them.",
                 sm=True)], ratio="a32"),
        hbox("Ask for error rates broken down by gender, age and skin tone before any face-based system is "
             "used on your participants. Delhi Police's own reported figures are on the facial recognition "
             "slide in Section 05.", "amber"),
    ]),

    C("Errors and base rates", "Illustrative: why a 95% accurate fraud flag can still hurt most of the people it flags", [
        body("Accuracy figures mislead when the thing being detected is rare. Suppose a state uses a model to "
             "flag ineligible pension claimants, and suppose only 2% of 1,00,000 claimants are actually "
             "ineligible. The model is right 95% of the time for both groups. The numbers below are "
             "<strong>Illustrative</strong>, built to show the arithmetic; they describe no real scheme."),
        table(["Illustrative", "Actually ineligible (2,000)", "Actually eligible (98,000)"], [
            ["Flagged as ineligible", "1,900 (correct)", "4,900 (wrongly flagged)"],
            ["Not flagged", "100 (missed)", "93,100 (correct)"],
        ]),
        tw(pp("red", "The result", "Of 6,800 people flagged, 4,900, about 72%, are eligible. If flags lead "
              "to automatic suspension, most people cut off are entitled to the pension."),
           pp("green", "The design fix", "Treat a flag as a reason to check. Put the "
              "burden of verification on the department, and keep paying until the check is done.")),
        hbox("This is the arithmetic behind the Telangana case in Section 09.", "indigo"),
    ]),

    C("Opacity and contestability", "If you cannot see the reason, you cannot contest the decision", [
        body("Due process in Indian administrative law requires that a person affected by a decision be told "
             "the reason and be heard. Automated systems strain both. The reason may sit in a model nobody in "
             "the department can explain, or in a vendor contract marked confidential. A person dropped from "
             "a list may not even know that a system was involved. Contestability, the practical ability to "
             "challenge an output, has to be designed in."),
        tw([panel("red", "How opacity arises", [bullets([
                "Complex models whose logic is hard to state",
                "Trade secrecy claimed by vendors",
                "No notice that a system was used",
                "Staff who cannot override the output"], sm=True)])],
           [panel("green", "What contestability needs", [bullets([
                "Notice to the person that a system contributed",
                "A plain-language reason, with the data relied on",
                "A human review with power to reverse",
                "Continued benefit while review is pending"], sm=True)])]),
        hbox("Article 14 (non-arbitrariness) and the principles of natural justice give these needs a legal "
             "footing in India even without an AI statute.", "indigo"),
    ]),
]

# ===================== SECTION 09: AI IN WELFARE, WORK, ELECTIONS =====================
ALJ = "Tapasya, Kumar Sambhav and Divij Joshi, Al Jazeera with The Reporters' Collective, 24 January 2024"

S09 = [
    D("09", "Section Nine", "AI in welfare, work and elections"),

    C("Samagra Vedika", "Telangana's Samagra Vedika: an algorithm that decided who was poor", [
        body("Samagra Vedika is a data system that links records across Telangana's departments to build a "
             "profile of each resident. The state used it to find ineligible welfare claimants, for example "
             "people who owned a car. An investigation by Al Jazeera and The Reporters' Collective, supported "
             "by the Pulitzer Center's AI Accountability Network, found that it wrongly matched poor people to "
             "assets they did not own, and that officials trusted the system over the person."),
        stats([
            {"num": "1.86 mn+", "label": "food security cards cancelled by Telangana, 2014-2019", "color": "red",
             "source": ALJ},
            {"num": "142,086", "label": "fresh applications rejected without notice in the same period", "color": "amber",
             "source": ALJ},
        ]),
        tw(pp("cyan", "Bismillah Bee", "A 67-year-old widow in a Hyderabad slum was denied rations because "
              "the system matched her late husband Syed Ali, a rickshaw puller, to Syed Hyder Ali, a car "
              "owner. Her case reached the Supreme Court."),
           pp("red", "Where the burden fell", "Once excluded, people had to prove they were entitled. The "
              "algorithm's output was treated as the default truth, and the person as the one who had to "
              "rebut it.")),
    ]),

    C("The re-verification", "When the Supreme Court ordered a check, the errors showed", [
        body("In April 2022, in a case first filed by activist S.Q. Masood on behalf of excluded families, the "
             "Supreme Court ordered Telangana to verify in the field all 1.9 million cards deleted since 2016. "
             "The investigation obtained the progress figures to July 2022. Even on this partial count the "
             "error rate exceeded the state's own claim that wrong matches happened in under five per cent "
             "of cases and had mostly been corrected."),
        stats([
            {"num": "491,899", "label": "applications received for re-verification", "color": "cyan", "source": ALJ},
            {"num": "205,734", "label": "processed by July 2022", "color": "indigo", "source": ALJ},
            {"num": "15,471", "label": "approved, so wrongly rejected", "color": "red", "source": ALJ},
            {"num": "7.5%+", "label": "minimum share of processed cards wrongly rejected", "color": "amber", "source": ALJ},
        ], cols=4),
        hbox("The 7.5% is a floor. It counts only people who knew to apply, managed to apply, and had their "
             "case processed. Those who gave up are in no figure.", "amber"),
        body("The arithmetic is the illustrative base-rate table of Section 08 made real: a rare target, a "
             "system with errors, and a decision rule that cut people off on a flag.", sm=True),
    ], compact=True),

    C("Lessons", "Five design rules for automated eligibility, from the evidence", [
        body("Telangana is one case, and the same pattern appears wherever an automated flag is allowed to "
             "end a benefit. The rules below are drawn from the Samagra Vedika evidence, the Obermeyer study "
             "and the Puttaswamy test. They apply equally to a state system and to an NGO that scores "
             "households for a livelihoods programme or a scholarship."),
        table(["Rule", "Why", "What it looks like in practice"], [
            ["A flag starts a check, and the benefit continues meanwhile", "Errors concentrate on the poor, who cannot rebut them",
             "Benefit continues until a human verifies in the field"],
            ["Give notice and a reason", "Natural justice; Article 14", "A letter or SMS naming the data relied on"],
            ["Publish error rates", "Accuracy claims must be testable", "Share of flags overturned on review, each quarter"],
            ["Test on the people it will judge", "Gender Shades: averages hide failing groups", "Error rates by caste, gender, disability, district"],
            ["Keep a non-digital route", "Authentication and data fail", "A named officer who can approve on documents"],
        ]),
    ], compact=True),

    C("The labour behind AI", "Data work: the people who label what AI learns from", [
        body("AI systems learn from data that people have labelled: this image shows a pedestrian, this text "
             "is abusive, this answer is better than that one. Much of this work is done through online "
             "platforms and outsourcing firms, much of it in the Global South, including India. It is "
             "low-paid, often precarious, and sometimes harmful: moderators and labellers view violent and "
             "sexual material for hours."),
        stats([
            {"num": "US$1.32&ndash;2", "label": "hourly take-home pay of Kenyan workers labelling data for OpenAI via Sama",
             "color": "red", "source": "Billy Perrigo, TIME, 18 January 2023"},
            {"num": "142 &rarr; 777", "label": "digital labour platforms worldwide, 2010 to 2020", "color": "indigo",
             "source": "ILO, World Employment and Social Outlook 2021 (23 February 2021)"},
            {"num": "Half", "label": "of online platform workers earn less than US$2 an hour", "color": "amber",
             "source": "ILO, World Employment and Social Outlook 2021"},
        ]),
        tw(pp("cyan", "Why this is a rights issue", "Fair pay, safe work, freedom of association and social "
              "security apply to data workers as to any others. The ILO found platform workers often lack "
              "all four."),
           pp("green", "For livelihoods programmes", "Data work is offered to rural youth and women as a "
              "digital job. Check pay per hour actually worked, exposure to harmful content and who holds the "
              "contract before promoting it.")),
    ]),

    C("Workers and algorithms", "Gig work, algorithmic management and the new Labour Codes", [
        body("For delivery riders and drivers, the boss is often an algorithm: it allocates orders, sets pay "
             "per task, rates workers and can deactivate an account. The four Labour Codes came into force on "
             "21 November 2025. The Code on Social Security 2020, one of the four, defines gig workers "
             "(s2(35)) and platform workers (s2(61)) and provides for social security schemes for them (s114), "
             "the first national labour law in India to name them."),
        tw([panel("cyan", "What the Code on Social Security does", [body(
                "Recognises gig and platform workers as categories, provides for schemes on life and disability "
                "cover, health and old age (s114(1)), and for aggregator contributions of 1-2% of annual turnover, "
                "capped at 5% of what the aggregator pays these workers (s114(4)). The detail sits in "
                "rules and schemes, so check what has been notified in your state.", sm=True)])],
           [panel("amber", "What it leaves open", [body(
                "Algorithmic deactivation without a reason, opaque pay formulas, and ratings that punish "
                "workers for delays they did not cause. These are due process questions about an algorithm, "
                "and the Code says little about them.", sm=True)])]),
        hbox("For the wider labour picture, see " + link("work-labour-livelihoods.html", "Work, Labour &amp; "
             "Livelihoods") + ".", "indigo"),
    ]),

    C("Deepfakes and elections", "The Election Commission's rules on AI in campaigns", [
        body("Generative AI makes it cheap to put words in a candidate's mouth. The Election Commission of "
             "India has issued a sequence of advisories to political parties and, in 2026, directions to "
             "platforms. They use the Model Code of Conduct and the IT Act and IT Rules, since there is no "
             "election-specific AI statute. Each step tightened the last."),
        table(["Date", "Instrument", "Main requirement"], [
            ["January 2025", "Advisory to political parties", "Label images, video and audio generated or significantly altered by AI"],
            ["24 October 2025", "Advisory before the Bihar elections", "Labels such as AI-Generated covering at least 10% of the "
             "visible area; misleading synthetic content removed from party handles within three hours"],
            ["19 April 2026", "Instructions during the assembly elections in Assam, Kerala, Tamil Nadu, Puducherry and West Bengal",
             "Platforms to act on unlawful or misleading content, including AI material, within three hours of a "
             "report; over 11,000 posts or URLs acted on (removals, FIRs, clarifications, rebuttals) after the 15 March schedule"],
        ]),
        body("Sources: MediaNama, 17 January 2025, 28 October 2025 and 22 April 2026; All India Radio News, 25 October 2025; Scroll, April 2026.", sm=True),
    ], compact=True),

    C("Responding to a deepfake", "When a deepfake targets your staff, partners or community", [
        body("Deepfakes are used for more than elections. Voice clones of relatives ask for money. Fake "
             "videos of activists are used to discredit them. Synthetic intimate images are used against "
             "women journalists and community leaders. A response has to move fast, because the 2026 IT Rules "
             "give platforms three hours to act on an order, and harm spreads faster still."),
        flow(["SAVE: capture the content, link, account and time before it is deleted",
              "REPORT: to the platform as synthetic or impersonation content, and to its grievance officer",
              "COMPLAIN: the national cybercrime portal or police, citing IT Act s66D or s66E as relevant",
              "CORRECT: a short public statement from a trusted voice, without reposting the fake",
              "SUPPORT: care for the person targeted, who carries most of the harm"]),
        tw(pp("cyan", "Verification habits", "Check the source account, look for the original, use reverse "
              "image search, and be wary of audio that arrives without video."),
           pp("amber", "Your own use", "If you use synthetic voices or faces in campaigns, label them as the "
              "ECI and the IT Rules expect, and never imitate a real person.")),
    ]),
]

# ===================== SECTION 10: GOVERNING AI =====================
S10 = [
    D("10", "Section Ten", "Governing AI: the EU, India and global standards"),

    C("Four approaches", "Four ways to govern AI, and where South Asia sits", [
        body("Governments and international bodies have chosen different instruments. The European Union "
             "passed a binding regulation. India has chosen guidelines plus existing law, on the view that a "
             "separate AI law is not needed yet. UNESCO and the OECD set standards that states sign up to "
             "without enforcement. For a South Asian organisation all four can apply at once, depending on "
             "where its donors, users and vendors are."),
        table(["Instrument", "Type", "Adopted", "Binding?"], [
            ["EU AI Act, Regulation (EU) 2024/1689", "Regulation, risk-based", "In force 1 August 2024", "Yes, in the EU and for systems used there"],
            ["India AI Governance Guidelines", "Guidelines plus existing laws", "Released by MeitY, 5 November 2025", "No; existing laws are"],
            ["UNESCO Recommendation on the Ethics of AI", "Global standard", "November 2021, 193 member states", "No"],
            ["OECD AI Principles", "Intergovernmental principles", "May 2019, updated May 2024", "No"],
        ]),
        hbox("India is not an OECD member. Every South Asian state, as a UNESCO member, took part in adopting the "
             "UNESCO Recommendation.", "indigo"),
    ], compact=True),

    C("The EU's tiers", "The EU AI Act sorts AI systems into four levels of risk", [
        body("The EU AI Act regulates by use. The same model may be banned in one use and "
             "unregulated in another. Its four levels are set out by the European Commission. Several "
             "high-risk uses are exactly the ones development programmes care about: access to essential "
             "public services and benefits, education, and employment."),
        table(["Level", "Rule", "Examples given by the Commission"], [
            ["Unacceptable risk", "Banned (eight practices since February 2025; the 2026 Omnibus adds two from 2 December 2026)",
             "Social scoring; harmful manipulation; untargeted scraping of faces; emotion recognition at work and in education; from December 2026, AI that generates non-consensual intimate images or child sexual abuse material"],
            ["High risk", "Strict duties: risk management, data quality, human oversight, registration",
             "Access to essential public and private services, such as credit scoring; education; employment; law enforcement"],
            ["Transparency risk", "Disclosure duties", "Chatbots must say they are AI; deepfakes must be labelled"],
            ["Minimal or no risk", "No new rules", "Spam filters; AI in video games"],
        ]),
        body("Sources: European Commission, AI Act policy page (digital-strategy.ec.europa.eu), read October 2026; "
             "Regulation (EU) 2026/1744, Article 1(7) (EUR-Lex).",
             sm=True),
    ], compact=True),

    C("EU dates", "When each part of the EU AI Act applies, after the 2026 Omnibus", [
        body("The Act applies in stages. In July 2026 the EU adopted the Digital Omnibus on AI, Regulation (EU) "
             "2026/1744, published in the Official Journal on 24 July 2026 and in force from 27 July 2026. It "
             "postponed the main high-risk duties. Older summaries that give 2 August 2026 for the high-risk "
             "rules are now out of date."),
        table(["Date", "What applies"], [
            ["1 August 2024", "The Act enters into force"],
            ["2 February 2025", "Prohibited practices; AI literacy duty (since reworded by the Omnibus)"],
            ["2 August 2025", "Duties for general-purpose AI models"],
            ["2 August 2026", "Most transparency duties under Article 50"],
            ["2 December 2026", "Two new bans (AI-generated non-consensual intimate images; child sexual abuse material); "
             "marking deadline for generative systems already on the market"],
            ["2 December 2027", "High-risk systems in Annex III uses (postponed from 2 August 2026)"],
            ["2 August 2028", "High-risk AI in products under Annex I (postponed from 2 August 2027)"],
        ]),
        body("Sources: Regulation (EU) 2026/1744, OJ L, 24 July 2026, Articles 1 and 4 (EUR-Lex); European "
             "Commission AI Act page.", sm=True),
    ], compact=True),

    C("Why the EU matters here", "Why a South Asian NGO should know the EU AI Act", [
        body("The EU Act applies to providers and deployers who place AI on the EU market or whose AI outputs "
             "are used in the EU, wherever they are based. Most South Asian programmes will never be directly "
             "covered. The Act still reaches them in three ways, and it is the most detailed public statement "
             "of what responsible AI requires, which makes it a useful checklist even where it has no legal "
             "force."),
        tw([panel("cyan", "Indirect reach", [bullets([
                "European donors may write its standards into grant terms",
                "Vendors selling into the EU build to its rules",
                "Research partners in the EU must comply when outputs are used there"], sm=True)])],
           [panel("green", "Borrowing its ideas", [bullets([
                "Its high-risk list maps onto welfare, education and jobs",
                "Its duties (human oversight, data quality, logs) make a good procurement checklist",
                "Its bans name practices to avoid anywhere, such as social scoring"], sm=True)])]),
        hbox("In India, using the EU list as a benchmark is a choice with no legal force. Say so in your "
             "policy, so staff know which standard they are being held to.", "amber"),
    ]),

    C("India's guidelines", "The India AI Governance Guidelines (November 2025)", [
        body("MeitY released the India AI Governance Guidelines on 5 November 2025. They were drafted by a "
             "committee chaired by Prof. Balaraman Ravindran of IIT Madras. Their central position is that "
             "existing laws on information technology, data protection, consumer protection and criminal law "
             "can govern most AI uses, so a separate AI law is not needed at this stage given the current "
             "assessment of risks."),
        tw([panel("cyan", "The seven sutras", [bullets([
                "Trust is the foundation",
                "People first",
                "Innovation over restraint",
                "Fairness and equity",
                "Accountability",
                "Understandable by design",
                "Safety, resilience and sustainability"], sm=True)])],
           [panel("indigo", "Institutions proposed", [body(
                "An AI Governance Group (AIGG) for a whole-of-government approach, supported by a Technology "
                "and Policy Expert Committee, and an AI Safety Institute for technical expertise, with sector "
                "regulators keeping enforcement powers. The sutras are adapted from the RBI's FREE-AI "
                "committee report.", sm=True)])]),
        body("Source: India AI Governance Guidelines, MeitY, November 2025; PIB release 2186639, 5 November "
             "2025. Note the third sutra: India has chosen to favour innovation where risks are "
             "balanced.", sm=True),
    ]),

    C("IndiaAI Mission", "The IndiaAI Mission: public money for compute, data and models", [
        body("On 7 March 2024 the Union Cabinet approved the IndiaAI Mission, with a budget outlay of "
             "Rs 10,371.92 crore. Its components include public AI compute of 10,000 or more GPUs, better "
             "data quality, support for indigenous foundation models, startup financing and tools for safe and "
             "trusted AI. The rights questions sit inside these components: which data trains the models, "
             "and whose languages and needs are served."),
        stats([
            {"num": "Rs 10,371.92 cr", "label": "IndiaAI Mission outlay approved by the Cabinet", "color": "cyan",
             "source": "PIB, Cabinet approves IndiaAI Mission, 7 March 2024"},
            {"num": "10,000+", "label": "GPUs of public AI compute planned", "color": "indigo",
             "source": "PIB, 7 March 2024"},
        ]),
        tw(pp("green", "Opportunity", "Public compute and Indian-language models could make AI tools usable "
              "for people who do not read English, which matters for any chatbot a programme might deploy."),
           pp("amber", "Questions to ask", "Were people asked before their data trained a public model? Are "
              "models tested on dialects and on women's and Dalit speakers? Who audits the safe and trusted AI "
              "tools themselves?")),
    ]),

    C("Global standards", "UNESCO's Recommendation and the OECD Principles", [
        body("Two non-binding texts give shared vocabulary across countries. They are the standards a "
             "development organisation can cite in any South Asian country, because they do not depend on "
             "national law. Neither creates a remedy for a harmed person. Both are useful for writing an "
             "organisational AI policy that donors and partners will recognise."),
        tw([panel("cyan", "UNESCO Recommendation on the Ethics of AI (2021)", [body(
                "Adopted in November 2021 by UNESCO's 193 member states, the first global standard on AI "
                "ethics. It holds that AI must respect human rights and human dignity, grounded in principles "
                "such as transparency, fairness, environmental sustainability and human oversight.", sm=True)])],
           [panel("indigo", "OECD AI Principles (2019, updated 2024)", [body(
                "Adopted in May 2019 and updated in May 2024 to reflect new technology. They promote AI that "
                "is innovative and trustworthy and that respects human rights and democratic values.", sm=True)])]),
        body("Sources: UNESCO, Ethics of Artificial Intelligence page; OECD.AI, AI Principles overview; both read "
             "October 2026.", sm=True),
    ]),

    C("AI and the DPDP Act", "AI and personal data under the DPDP Act, phase by phase", [
        body("India has no AI statute, so the Digital Personal Data Protection Act 2023 is the main law that "
             "will govern AI built on personal data. Its commencement is staged under G.S.R. 843(E) of 13 "
             "November 2025, and the DPDP Rules 2025 (G.S.R. 846(E)) follow the same phasing. As of October "
             "2026 the duties that matter most for AI (notice, consent, purpose, accuracy, erasure) are "
             "<strong>not yet in force</strong>."),
        table(["AI question", "DPDP provision", "Applies from"], [
            ["May we train a model on beneficiary records?", "Consent or a legitimate use (ss4-7)", "13 May 2027"],
            ["Must the data be accurate if it drives a decision?", "Fiduciary duty on completeness and accuracy (s8)", "13 May 2027"],
            ["Children's data in an EdTech or chatbot tool", "s9: parental consent; no tracking or targeted ads", "13 May 2027"],
            ["Research use of personal data", "Exemption in s17(2)(b), on conditions", "13 May 2027"],
            ["Who will hear complaints?", "Data Protection Board (ss18-26)", "In force since 13 November 2025"],
        ]),
        hbox("Do not tell partners that the research exemption or any duty is already in force. Plan now so "
             "that systems comply on 13 May 2027.", "red"),
    ], compact=True),
]

# ===================== SECTION 11: PRACTICE =====================
S11 = [
    D("11", "Section Eleven", "A digital-rights and AI risk assessment for your programme"),

    C("When to assess", "When a programme should run a digital-rights and AI assessment", [
        body("An assessment is a structured set of questions asked before a digital tool goes live, and asked "
             "again when it changes. It need not be long. Its value lies in forcing the questions in this deck "
             "to be answered by named people before participants carry the risk. Run it at the triggers "
             "below, and keep the answers on file: a donor, an ethics committee or, from May 2027, the Data "
             "Protection Board may ask for them."),
        flow(["NEW TOOL: any app, portal, chatbot or dashboard that touches participants' data",
              "NEW USE: existing data used for a new purpose, such as targeting",
              "AUTOMATION: any score, flag or match that feeds a decision about a person",
              "SCALE-UP: a pilot moving to more districts or a new population",
              "INCIDENT: a breach, a shutdown, a complaint or a takedown"]),
        tw(pp("cyan", "Who should be in the room", "The programme lead, someone who handles data, a "
              "safeguarding or legal contact, and at least two people from the community the tool will serve."),
           pp("amber", "How long it takes", "For a small tool, a half-day workshop with this deck's checklists. "
              "For a system that scores people, longer, with a test on real cases before launch.")),
    ]),

    C("Checklist: rights", "Checklist part 1: the rights questions", [
        body("The first half of the assessment applies to every digital tool, whether or not it uses AI. Each "
             "question links back to a section of this deck, so a team that is unsure of an answer knows "
             "where to look. Answer in writing. A question marked no or unsure becomes an action with an "
             "owner and a date, entered in the programme's risk register."),
        table(["Question", "Section", "Yes / No / Unsure"], [
            ["Is there a lawful basis for every data field we collect, and could we do without any of them?", "02, 05", ""],
            ["Have we mapped what fails in a shutdown, with a fallback agreed with the department?", "03", ""],
            ["Do we have a plan if our content is blocked or removed, with backups?", "04", ""],
            ["Could our data help anyone watch or profile participants, and have we minimised it?", "05", ""],
            ["Can women, older people and non-readers use the tool without help, or with private help?", "06", ""],
            ["Do we have a route for online harassment and a children's safeguarding rule?", "07", ""],
            ["Will we meet the DPDP duties that apply from 13 May 2027?", "07, 10", ""],
        ]),
    ], compact=True),

    C("Checklist: AI", "Checklist part 2: the AI questions", [
        body("The second half applies when the tool includes a model that scores, classifies, matches or "
             "generates. These questions come from the failure cases in Sections 08 and 09 and from the "
             "duties the EU sets for high-risk systems, used here as a benchmark. A vendor or partner who "
             "cannot answer a question is itself a finding: write it down."),
        table(["Question", "Evidence to ask for"], [
            ["What exactly does the output predict, and is that the thing we care about?", "The target variable, in plain words"],
            ["On whose data was it trained and tested, and who is missing?", "Data description; test populations"],
            ["What are its error rates for women, older people, caste groups, disability?", "Disaggregated test results"],
            ["Who acts on the output, and can they override it?", "Process map; override records"],
            ["Will affected people be told, given a reason and able to contest?", "Notice text; review procedure"],
            ["What happens while a contested decision is reviewed?", "Written rule that benefits continue"],
            ["For generative tools: how are wrong answers caught and corrected?", "Testing log; escalation route"],
        ]),
    ], compact=True),

    C("Decision table", "From answers to action: a decision table", [
        body("A checklist produces findings; a team still has to decide. The table converts the pattern of "
             "answers into one of four decisions. It is deliberately conservative where a system decides "
             "about people's entitlements, because the evidence in Section 09 shows how errors fall on those "
             "least able to contest them. Adapt the thresholds to your setting, and record the decision and "
             "the reasons."),
        table(["Pattern of answers", "Risk level", "Decision"], [
            ["Information only; no personal data; no decision about people", "Low", "Proceed; review yearly"],
            ["Personal data, but no automated decision; minor gaps with owners", "Medium", "Proceed once actions are done"],
            ["Score or flag influences an entitlement; human review exists and works", "High",
             "Pilot with field verification of every adverse flag; publish error rates"],
            ["Score or flag can end an entitlement without review; or error rates unknown for key groups",
             "Unacceptable as designed", "Do not deploy; redesign so a flag only triggers a check"],
            ["Children's data or survivor data with any gap in consent or security", "High", "Pause until fixed"],
        ]),
        hbox("The unacceptable row is a design verdict, and redesign usually saves the project. A tool that "
             "helps staff decide whom to visit first is far safer than one that decides who is paid.", "amber"),
    ], compact=True),

    C("Worked example: the tool", "Illustrative worked example: a WhatsApp chatbot for pension eligibility", [
        body("<strong>Illustrative.</strong> A women's rights NGO in one district plans a WhatsApp chatbot. "
             "Widows type or speak a few answers (age, district, whether they hold a ration card) and the bot "
             "tells them which state and central pension schemes they may qualify for, and which documents to "
             "bring to the block office. Version two would add a <em>likely eligible</em> score that the NGO "
             "would share with the block office to speed up approvals. The NGO, the district and the figures "
             "in this example are made up for teaching."),
        tw([panel("cyan", "What the team wants", [bullets([
                "Reach widows who cannot visit the office",
                "Cut wasted trips for missing documents",
                "Help the block office prioritise applications"], sm=True)])],
           [panel("amber", "What the assessment must test", [bullets([
                "Can widows without their own phone use it?",
                "Is answer quality checked against scheme rules?",
                "What happens to a widow scored as unlikely?",
                "What data does WhatsApp and the vendor see?"], sm=True)])]),
        hbox("Note the shift between versions. Version one gives information to the person. Version two passes a "
             "judgment about her to an authority. The assessment treats them as two different tools.", "indigo"),
    ]),

    C("Worked example: findings", "Illustrative worked example: what the assessment found", [
        body("<strong>Illustrative.</strong> The team ran both checklists in a half-day workshop with six widows "
             "from two villages, the block office's data entry operator and the NGO's programme lead. The "
             "table records the main findings and the actions agreed. Each action has an owner, which is the "
             "difference between an assessment and a discussion."),
        table(["Finding", "Risk", "Action agreed"], [
            ["Four of six widows use a son's phone", "Exclusion; no privacy", "Add a missed-call voice line and assisted help at self-help group meetings"],
            ["Bot answers drafted from a 2024 scheme circular", "Wrong eligibility advice", "Monthly check against current rules; date shown in every answer"],
            ["Version two score trained on past approvals", "Learns who reached the office before (Obermeyer pattern)", "Drop the score; send a document checklist instead"],
            ["Chats kept by the vendor indefinitely", "Data exposure; future DPDP breach", "Contract: delete after 90 days; no reuse for training"],
            ["No route if a widow is wrongly told she is ineligible", "Lost entitlement", "Every answer ends with a helpline number and 'you may still apply'"],
        ]),
    ], compact=True),

    C("Worked example: decision", "Illustrative worked example: the decision and how it will be monitored", [
        body("<strong>Illustrative.</strong> Using the decision table, the team rated version one Medium and "
             "version two Unacceptable as designed. It launched version one after the agreed actions and "
             "replaced the score with a document checklist that the widow herself carries to the office. The "
             "block office gets nothing from the bot, which removes the risk that a score quietly becomes a "
             "gate. The team set four indicators to watch."),
        tw([panel("green", "Monitoring indicators", [bullets([
                "Share of users who are women using their own phone",
                "Applications filed per 100 users, by village",
                "Answers found wrong at the monthly check",
                "Complaints received and resolved"], sm=True)])],
           [panel("cyan", "Review triggers", [bullets([
                "Any proposal to share chat data with the government",
                "A change in scheme rules",
                "A shutdown lasting more than a day in the district",
                "The DPDP duties commencing on 13 May 2027"], sm=True)])]),
        hbox("The final design does less than version two promised, and it carries far less risk of cutting "
             "an entitled widow off. Teams that run this assessment often reach the same trade.", "amber"),
    ]),
]

# ===================== SECTION 12: SUMMING UP =====================
S12 = [
    D("12", "Section Twelve", "Summing up and where next"),

    C("Ten points", "Ten points to carry from this deck", [
        tw([panel("cyan", "Rights online", [bullets([
                "The same rights apply offline and online (HRC 20/8, 2012)",
                "Any limit must pass legality, legitimate aim, necessity and proportionality",
                "Privacy is a fundamental right (Puttaswamy, 2017); section 66A is dead law (Shreya Singhal, 2015)",
                "Indefinite internet suspension is impermissible and orders must be published (Anuradha Bhasin, 2020)",
                "India imposed 65 shutdowns in 2025: plan offline fallbacks before you need them"], sm=True)])],
           [panel("green", "AI and society", [bullets([
                "An AI system predicts from past data, and inherits the past's unfairness",
                "Check what a score predicts: cost stood in for illness in Obermeyer (2019)",
                "Ask for error rates by group: averages hid a 34.7% error in Gender Shades (2018)",
                "A flag should start a check while the benefit continues (Telangana, 2014-2022)",
                "DPDP core duties apply from 13 May 2027; the EU high-risk rules from 2 December 2027"], sm=True)])]),
        body("Each point carries its source on the slide where it was introduced. If you remember one method "
             "from the whole deck, make it the four-step test on slide 9: it works for a shutdown order, a "
             "takedown, a surveillance request and an eligibility algorithm alike, and it is the frame the "
             "Supreme Court itself uses. The checklists in Section 11 are that test turned into questions a "
             "programme team can answer.", sm=True),
    ], compact=True),

    C("Glossary", "Words used in this deck", [
        body("Terms in the order they appear. Several are legal terms with a precise meaning in Indian law, "
             "and using them loosely in a proposal or a court filing causes confusion. Where a term comes from "
             "a statute, the section is given so that you can read it in full. The others are terms of art in "
             "digital rights and AI research."),
        table(["Term", "Meaning"], [
            ["Intermediary", "A service that carries or hosts others' content, such as a telecom operator or social media platform (IT Act s2(1)(w))"],
            ["Safe harbour", "Protection from liability for user content, on conditions (IT Act s79)"],
            ["Blocking order", "A direction to block public access to information (IT Act s69A)"],
            ["Suspension", "A temporary shutdown of telecom services (Telecommunications Act 2023, s20)"],
            ["Proportionality", "The test that a limit on a right is no greater than needed for a legitimate aim"],
            ["Synthetically generated information", "AI-generated or altered content that appears real (IT Rules, 2026 amendment)"],
            ["Proxy", "A measurable variable used in place of the thing a model should predict"],
            ["High-risk AI system", "In the EU AI Act, a system in a listed sensitive use, subject to strict duties"],
        ]),
    ], compact=True),

    C("Questions practitioners ask", "Questions practitioners ask, answered briefly", [
        tw([panel("cyan", "Can we be prosecuted for sharing a post that turns out to be false?", [body(
                "Not under section 66A, which is gone. Other offences, such as defamation or promoting enmity "
                "under the BNS, can apply. Check before sharing, and correct quickly.", sm=True)]),
            panel("indigo", "Does the DPDP Act stop us using AI on beneficiary data today?", [body(
                "Its core duties apply only from 13 May 2027. Ethics, donor terms and Puttaswamy apply now. "
                "Design as if the duties were already in force.", sm=True)])],
           [panel("green", "Is it safe to use a free chatbot with participants?", [body(
                "Only for general information with no personal data, after checking its answers in your "
                "language. Section 11 and " + link("genai-practitioners.html", "GenAI for Practitioners") +
                " explain why.", sm=True)]),
            panel("amber", "Can we refuse a department's demand for our beneficiary list?", [body(
                "Ask for the law that requires it and the purpose. Without a law, Puttaswamy's first step "
                "fails. Get legal advice before refusing.", sm=True)])]),
        body("These answers are general information as of October 2026 and are not legal advice for a "
             "particular case. Laws, rules and judgments in this field change often, and several of those "
             "cited here are under appeal or revision.", sm=True),
    ]),

    C("Where next", "Where next: related 101 decks", [
        tw([panel("cyan", "Go deeper on digital topics", [body(
                link("digital-ethics.html", "Digital Ethics") + " for privacy by design, Aadhaar and "
                "misinformation. " +
                link("data-protection-dpdp.html", "Data Protection &amp; the DPDP Act") + " for compliance "
                "step by step. " +
                link("genai-practitioners.html", "GenAI for Practitioners") + " for safe daily use of AI "
                "tools. " +
                link("data-feminism.html", "Data Feminism") + " for power in data. " +
                link("post-truth-101.html", "Post-Truth Politics") + " for disinformation.", sm=True)])],
           [panel("green", "Rights, ethics and practice", [body(
                link("human-rights.html", "Human Rights") + " for the treaties and the UN system. " +
                link("ind-constitution.html", "Indian Constitution") + " for Articles 14, 19 and 21. " +
                link("research-ethics.html", "Research Ethics") + " for consent in studies. " +
                link("child-rights.html", "Child Rights") + " and " +
                link("safeguarding-psea.html", "Safeguarding &amp; PSEA") + " for children online. " +
                link("governance-accountability.html", "Governance &amp; Accountability") + " for RTI and "
                "grievance routes.", sm=True)])]),
        hbox("Suggested order: Human Rights, then Data Protection &amp; the DPDP Act, then GenAI for "
             "Practitioners. Read Child Rights before any digital programme with children.", "indigo"),
    ], compact=True),
]

TITLE = {"type": "title",
         "main": "Digital<br>Rights<br>&amp; AI 101",
         "sub": "Rights online, internet shutdowns, platform rules, surveillance, digital public "
                "infrastructure, and what AI means for welfare, work and elections: law, evidence and a "
                "risk assessment for development practitioners in South Asia",
         "tags": ["100 Slides", "South Asia Focus", "Free Forever", "Rights and AI"]}

TOC = {"type": "toc", "label": "Agenda", "title": "What we cover",
       "items": [
           {"name": "Rights online: the starting point"},
           {"name": "Speech and privacy in the Indian Constitution"},
           {"name": "Internet shutdowns in South Asia"},
           {"name": "Blocking, intermediaries and platform rules"},
           {"name": "Surveillance, spyware and facial recognition"},
           {"name": "Digital public infrastructure and the divide"},
           {"name": "Online harms: gender-based violence and children"},
           {"name": "What AI systems are and how they fail"},
           {"name": "AI in welfare, work and elections"},
           {"name": "Governing AI: the EU, India and global standards"},
           {"name": "A digital-rights and AI risk assessment"},
           {"name": "Summing up and where next"},
       ]}

END = {"type": "end",
       "eyebrow": "Digital Rights &amp; AI 101",
       "headline": "Test every limit, check every score, keep a way back for people",
       "byline": "ImpactMojo 101 Series &middot; Free foundational learning for development practitioners "
                 "in South Asia",
       "ctas": [{"label": "Digital Ethics 101", "href": "/101-courses/digital-ethics.html"},
                {"label": "All 101 courses", "href": "/101-courses/"}],
       "meta": ["100 slides", "12 sections", "CC BY-NC-ND"]}

DECK = {
    "slug": "digital-rights-ai",
    "title": "Digital Rights &amp; AI 101",
    "description": ("Digital Rights & AI 101: a free foundational course for development practitioners in "
                    "South Asia. Rights online under the UDHR and UN Human Rights Council resolutions, "
                    "Puttaswamy, Shreya Singhal and Anuradha Bhasin, internet shutdowns in India, Pakistan, "
                    "Bangladesh, Nepal and Myanmar, the Telecommunications Act 2023, IT Act blocking and the IT "
                    "Rules, Pegasus and facial recognition, digital public infrastructure and the gender gap, "
                    "online harms, algorithmic bias, AI in welfare and elections, the EU AI Act, India's AI "
                    "governance guidelines and a programme risk assessment. ImpactMojo, CC BY-NC-ND."),
    "slides": ([TITLE, TOC] + S01 + S02 + S03 + S04 + S05 + S06 + S07 + S08 + S09 + S10 + S11 + S12
               + [END]),
}
