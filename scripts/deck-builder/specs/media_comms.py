# -*- coding: utf-8 -*-
"""
Media & Communications 101 - ImpactMojo 101 Series (native deck spec)
How media works in South Asia and how development practitioners communicate
research and programmes through it: ownership and market structure, radio and
community media, platforms and messaging apps, press freedom and the
Constitution, the legal frame for communicators, communication for development
theory, writing for different audiences, working with journalists, visual
ethics and consent, crisis communication, accessibility, measurement, and a
practitioner toolkit.
Build: python3 scripts/deck-builder/build.py media_comms

Every figure and citation was checked against a source that was opened and
read in October 2026; the list with URLs is in the build report.
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


TRAI_Q4 = ("TRAI, Indian Telecom Services Performance Indicator Report, January-March 2026 "
           "(Press Release 76/2026, 22 June 2026)")
PB_AR = "Prasar Bharati Annual Report 2024-25 (figures as on 31 March 2025)"
NFHS6 = "NFHS-6 (2023-24) India Fact Sheet, MoHFW and IIPS, May 2026, provisional (read from the OpenCity mirror)"
DNR25 = "Reuters Institute Digital News Report 2025, India page"
DNR26 = "Reuters Institute Digital News Report 2026, India page"
RSF26 = "RSF World Press Freedom Index 2026 and 2025, country pages (rsf.org)"
MOM = "RSF and DataLEADS, Media Ownership Monitor India, research November 2018 to May 2019"

# ===================== SECTION 01: WHY MEDIA MATTERS =====================
S01 = [
    D("01", "Section One", "Why media matters for development work"),

    C("The starting point", "Research that nobody hears changes nothing", [
        body("Development organisations produce a great deal of evidence: surveys, evaluations, "
             "policy briefs, programme reports. Most of it is read by a few hundred people. The "
             "decisions it is meant to inform are taken by officials, legislators, funders, "
             "journalists and families who will never open the PDF. Media is the set of channels "
             "through which evidence reaches those people, gets argued over, and either changes "
             "a decision or fades. A practitioner who understands how those channels work, who "
             "owns them, what the law allows and how journalists decide what is news can plan "
             "for that journey from the first day of a study."),
        tw(pp("cyan", "What this deck is for", "Programme staff, researchers and communications "
              "officers in South Asian NGOs, think tanks, foundations and government programmes "
              "who need to put findings and programme stories in front of the public and of "
              "decision-makers, accurately and safely."),
           pp("indigo", "What it covers", "The media market and its owners, radio and community "
              "media, platforms and WhatsApp, press freedom and the Constitution, the laws a "
              "communicator can break, communication for development theory, writing, working "
              "with journalists, images and consent, crises, access, measurement and a toolkit.")),
    ]),

    C("Four jobs", "Four jobs communication does in a development programme", [
        body("It helps to separate the different things an organisation asks of its "
             "communication, because each one needs a different audience, channel and measure. "
             "Mixing them up is the commonest reason a communication plan produces a lot of "
             "activity and no visible change."),
        table(["Job", "Typical audience", "Example", "What success looks like"], [
            ["Inform the public", "Citizens, service users", "Explainer on how to claim a ration card",
             "People know the steps and use them"],
            ["Influence policy", "Officials, legislators, courts", "Launch of an evaluation of a state scheme",
             "The finding is cited in a decision or a debate"],
            ["Change behaviour", "Households, frontline workers", "Radio drama on handwashing",
             "Practice changes, measured in the field"],
            ["Account and be accountable", "Funders, communities, the press", "Annual report, response to criticism",
             "Trust holds and errors are corrected in public"],
        ]),
        hbox("Behaviour change communication has its own deck. This one concentrates on news media, "
             "public communication of research, and the legal and ethical frame around both.", "indigo"),
    ]),

    C("A two-way street", "Media is also where your organisation gets examined", [
        body("Communication is often treated as something an organisation does to the media. The "
             "traffic runs the other way too. Journalists investigate NGOs, question evaluation "
             "results, report on misuse of funds and on harm done to the people a programme serves. "
             "A field photograph of a child that was shared without consent, or a press release that "
             "overstated a pilot result, can become the story. The same channels that carry your "
             "evidence will carry criticism of it, and they reward organisations that answer quickly, "
             "correct errors openly and can show their working."),
        tw(pp("green", "Proactive work", "Planning launches, briefing reporters, writing op-eds, "
              "building relationships with beat journalists before there is anything to sell."),
           pp("amber", "Reactive work", "Answering a hostile query by deadline, issuing a correction, "
              "handling a crisis in a field site, responding to a viral claim about your programme.")),
        hbox("Plan for both. Most organisations budget only for the first and meet the second "
             "unprepared.", "amber"),
    ]),

    C("Women online", "The audience is changing fast: women's phone and internet use", [
        body("Who can be reached through which channel is shifting quickly in India. The sixth "
             "National Family Health Survey, fielded in 2023-24 and released in May 2026, records "
             "a sharp rise in women's digital access since NFHS-5 (2019-21). These are provisional "
             "figures for women and men aged 15-49."),
        stats([
            {"num": "64.3%", "label": "women aged 15-49 who have ever used the internet (33.3% in NFHS-5)",
             "color": "cyan", "source": NFHS6},
            {"num": "80.5%", "label": "men aged 15-49 who have ever used the internet (51.2% in NFHS-5)",
             "color": "indigo", "source": NFHS6},
            {"num": "63.6%", "label": "women who have a mobile phone they themselves use (53.9% in NFHS-5)",
             "color": "green", "source": NFHS6},
        ]),
        body("The gaps remain large. Among women, 77.3% in urban areas and 58.6% in rural areas have "
             "ever used the internet; 77.6% of urban and 57.4% of rural women have a phone they use "
             "themselves. A campaign that relies on a smartphone alone will miss roughly a third of "
             "women, and more in rural districts.", sm=True),
    ], compact=True),

    C("Reach versus influence", "The biggest audience is rarely the one that decides", [
        body("Reach is how many people a message touches. Influence is whether the people who "
             "control a decision take it seriously. The two are often in tension. A district "
             "collector may never watch the prime-time debate that reaches millions, but will read "
             "a two-paragraph item in the local edition of a Hindi daily and a WhatsApp forward "
             "from a trusted colleague. A ministry joint secretary may read an op-ed in an English "
             "paper with a modest circulation because her minister does."),
        tw(pp("cyan", "Ask first", "Who takes the decision we want to influence? What do they read, "
              "watch and listen to? Whom do they trust? Which language? Which time of year is the "
              "decision taken (budget, monsoon session, scheme revision)?"),
           pp("indigo", "Then choose", "The outlet and format follow from those answers. A national "
              "television slot can matter less than a regional language daily, a trade journal, or "
              "a briefing note handed over at the right meeting.")),
        hbox("Media coverage is a means. Write down the decision or behaviour you want to change "
             "before you write down the outlets you want to be in.", "green"),
    ]),

    C("Vocabulary", "Paid, earned, shared and owned media", [
        body("Communications professionals sort channels into four groups, often shortened to "
             "PESO. The framework is used, among others, by AMEC, the international association "
             "for communication measurement, in its Integrated Evaluation Framework. Each group "
             "has a different cost, a different level of control and a different kind of "
             "credibility, and most development campaigns combine at least three."),
        table(["Type", "What it is", "Control", "Credibility"], [
            ["Paid", "Advertising, sponsored posts, boosted content", "High: you choose words and timing",
             "Low: readers know it is paid"],
            ["Earned", "News coverage, interviews, op-eds accepted by an editor", "Low: the journalist decides",
             "High: an independent filter applied"],
            ["Shared", "Social media posts and forwards by others", "Very low once it travels",
             "Depends on who shares it"],
            ["Owned", "Your website, reports, newsletter, podcast", "Full", "Depends on your reputation"],
        ]),
        hbox("Source: AMEC Integrated Evaluation Framework (amecorg.com/amecframework), which "
             "groups its output measures across paid, earned, shared and owned channels.", "indigo"),
    ], compact=True),

    C("A note on scope", "Why this deck leans on India, and where it does not", [
        body("Most learners on ImpactMojo work in India, so most of the law and market data here is "
             "Indian. Bangladesh, Nepal, Pakistan and Sri Lanka appear where the comparison changes "
             "how a practitioner should behave: press freedom rankings, legal risks for journalists "
             "and the platforms people use. The law sections describe the position as of October "
             "2026. Media law moves quickly, and two rules discussed here were stayed or struck "
             "down by courts within three years of being notified, so check the current status "
             "before you rely on any provision."),
        tw(pp("amber", "What this deck is", "An orientation for practitioners: what the structures "
              "are, where the risks sit, and how to do the routine work well."),
           pp("red", "What this deck cannot do", "Replace legal advice on a specific publication, "
              "or an editor's judgement on a specific story. When the stakes are high (a "
              "defamation risk, a child's identity, a court order) consult a lawyer before "
              "publishing.")),
    ]),
]

# ===================== SECTION 02: STRUCTURE AND OWNERSHIP =====================
S02 = [
    D("02", "Section Two", "How the media market works in South Asia"),

    C("Scale", "India's media system is very large and very fragmented", [
        body("India has one of the largest media systems in the world by almost any count. The "
             "numbers matter to a practitioner because they explain why 'getting into the media' is "
             "a matter of choosing among thousands of outlets, most of them regional and in "
             "languages other than English."),
        stats([
            {"num": "1.54 lakh", "label": "registered publications, 2024-25 (60,143 in 2004-05)",
             "color": "cyan", "source": "PIB backgrounder, National Press Day 2025, 16 Nov 2025"},
            {"num": "917", "label": "private satellite TV channels permitted by MIB, March 2026",
             "color": "indigo", "source": TRAI_Q4},
            {"num": "390", "label": "operational private FM channels in 120 cities, March 2026",
             "color": "green", "source": TRAI_Q4},
            {"num": "1,092.79 m", "label": "internet subscriptions, end of March 2026",
             "color": "amber", "source": TRAI_Q4},
        ], cols=4),
        body("Subscriptions count connections, and one person can hold several, so the internet "
             "figure is larger than the number of people online. The same PIB backgrounder notes "
             "that the Press Sewa Portal, which digitised periodical registration under the "
             "Press and Registration of Periodicals Act 2023, onboarded 40,000 publishers in six "
             "months.", sm=True),
    ], compact=True),

    C("Who registers what", "The regulators a communicator meets", [
        body("No single regulator covers Indian media. Print, broadcasting, cable, radio and online "
             "news each sit under different laws and bodies, and a communicator who works across "
             "formats deals with several of them."),
        table(["Medium", "Main law or instrument", "Body"], [
            ["Newspapers and periodicals", "Press and Registration of Periodicals Act 2023",
             "Press Registrar General of India (PRGI, formerly RNI)"],
            ["Press ethics", "Press Council Act 1978", "Press Council of India (PCI)"],
            ["Cable TV content", "Cable Television Networks (Regulation) Act 1995, s5 programme code",
             "Ministry of Information and Broadcasting (MIB)"],
            ["Tariffs, carriage, telecom", "TRAI Act 1997", "Telecom Regulatory Authority of India"],
            ["Public broadcasting", "Prasar Bharati (Broadcasting Corporation of India) Act 1990", "Prasar Bharati (Akashvani, Doordarshan)"],
            ["Online platforms and digital news", "IT Act 2000; IT Rules 2021", "MeitY; MIB for digital news publishers"],
        ]),
        body("Sources: PIB National Press Day 2025 backgrounder (PRGI and PCI); Cable Television "
             "Networks (Regulation) Act 1995, s5; IT Rules 2021, Part III and Appendix.", sm=True),
    ], compact=True),

    C("Ownership study", "Who owns India's media: the Media Ownership Monitor", [
        body("The best systematic study of ownership is the <strong>Media Ownership Monitor "
             "India</strong>, carried out by Reporters Without Borders (RSF) and the Delhi-based "
             "DataLEADS from November 2018 to May 2019. It analysed 58 "
             "leading outlets with the largest audience shares across print, television, radio "
             "and online. Its headline finding: ownership looks plural at the national level and "
             "is highly concentrated once you look at regional language markets."),
        tw(pp("cyan", "Hindi print", "Four outlets, Dainik Jagran, Hindustan, Amar Ujala and Dainik "
              "Bhaskar, captured 76.45% of readership share in the national Hindi language market."),
           pp("indigo", "Regional print", "In each regional language segment studied, the top two "
              "newspapers held more than half of readership. Eenadu and Sakshi together reached "
              "71.13% of audiences in the Telugu market.")),
        hbox("Source: " + MOM + " (rsf.org). The figures describe the market at the time of the "
             "study and have not been updated by the project since.", "amber"),
    ]),

    C("What concentration means", "Why ownership concentration matters to a communicator", [
        body("A concentrated regional market changes the practical work. If two newspapers reach "
             "most readers of a language, their editors' interests, owners' business links and "
             "political ties shape what gets covered in that state. The Media Ownership Monitor "
             "described the laws on media concentration as 'largely incoherent, unsystematic, "
             "insufficient and largely ineffective', and rated audience concentration a high "
             "risk, noting among other things that television audience data come from an "
             "industry-led body, BARC."),
        tw([panel("amber", "Practical consequences", [bullets([
                "A story the dominant paper declines may not run anywhere in that language",
                "Owners with business interests in mining, real estate or politics may avoid "
                "stories that touch them",
                "Local reporters, often poorly paid stringers, may depend on the goodwill of "
                "officials you are criticising"], sm=True)])],
           [panel("green", "What practitioners do", [bullets([
                "Map who owns the main outlets in your state before a launch",
                "Build relationships with more than one outlet per language",
                "Use owned channels and community media so that a single editor's decision "
                "is never the only route"], sm=True)])]),
    ]),

    C("Money", "Where media revenue comes from, and why it matters", [
        body("Most Indian news outlets depend on advertising, and a large share of it comes from "
             "governments. RSF's 2026 India profile notes that the media are funded mainly by "
             "advertising revenue, of which the government is the main source. The Media Ownership "
             "Monitor rated political control over media funding as a high risk. When a state "
             "government is a newspaper's largest advertiser, criticism of that government's "
             "schemes carries a commercial cost for the paper."),
        tw(pp("indigo", "What this means for evidence", "A study critical of a flagship state scheme "
              "may be harder to place in outlets that carry heavy state advertising. That is a "
              "reason to brief several outlets and to publish the full study on your own site "
              "the same day."),
           pp("cyan", "What this means for you", "Do not offer paid placement or 'advertorial' in "
              "exchange for coverage. Paid content presented as news misleads readers, and the "
              "Press Council's Norm 2 says advertisements must be clearly distinguishable from "
              "news content; Norm 29 deals with paid news.")),
        body("Sources: RSF India country page, 2026 (economic context); Media Ownership Monitor "
             "India, findings page (indicator ratings); PCI Norms of Journalistic Conduct 2022.", sm=True),
    ]),

    C("Language", "A media system in many languages", [
        body("India's media market is a set of language markets. The 2011 Census grouped 19,569 raw "
             "mother tongue returns into 121 languages, 22 of them in the Eighth Schedule. Hindi was "
             "returned by 43.63% of the population, Bengali by 8.03%, Marathi by 6.86%, Telugu by "
             "6.70%, Tamil by 5.70%, Gujarati by 4.58% and Urdu by 4.19%. English-language media reach a small, "
             "influential slice of this audience."),
        {"t": "chart", "canvas": "mcLangChart",
         "title": "Speakers as share of population, largest scheduled languages, Census 2011 (%)",
         "source": "Census of India 2011, Paper 1 of 2018, Language (C-16), Statement 4",
         "type": "bar",
         "data": {"labels": ["Hindi", "Bengali", "Marathi", "Telugu", "Tamil", "Gujarati", "Urdu"],
                  "datasets": [{"label": "% of population", "data": [43.63, 8.03, 6.86, 6.70, 5.70, 4.58, 4.19],
                                "backgroundColor": "#0EA5E9"}]},
         "options": {"__js__": "{ indexAxis:'y', plugins:{legend:{display:false}}, scales:{ x:{ min:0, max:50, title:{display:true,text:'% of population'} } } }"}},
        body("These are the most recent published language figures; the next Census has a "
             "reference date of 1 March 2027. Release translations the same day as the English "
             "version, or the regional press will report someone else's summary of your work.", sm=True),
    ], compact=True),

    C("The English problem", "English-language coverage reaches a narrow public", [
        body("Many development organisations judge a launch by whether it appeared in two or "
             "three English national dailies. Those papers matter for national policy circles, "
             "funders and the diplomatic community. They are a narrow window onto the public. A "
             "study about a district's health system that appears only in English will rarely be "
             "read by the district's health staff, its legislators or the families concerned."),
        tw([panel("cyan", "English national press", [bullets([
                "Read by central officials, judges, funders, academics",
                "Sets the frame for national debate",
                "Small share of total readership"], sm=True)])],
           [panel("green", "Language press and broadcast", [bullets([
                "Read and heard by state and district officials, legislators, families",
                "Often closer to the people your programme serves",
                "Needs translated materials and spokespeople who speak the language"], sm=True)])]),
        hbox("Budget for translation and for a spokesperson in each language you need. A "
             "translated two-page summary is cheaper than any amount of advertising and lands "
             "where decisions about your programme are made.", "indigo"),
    ]),

    C("Region", "Media systems across South Asia differ, and so does the risk", [
        body("Neighbouring countries share many features: large state broadcasters, a commercial "
             "press, rapid growth in mobile internet. They differ in the legal and political risks "
             "journalists face. RSF's 2026 country profiles note, for example, that Pakistan's "
             "Prevention of Electronic Crimes Act 2016 was strengthened by amendments in 2025; that "
             "Bangladesh's Cyber Security Act was introduced months before the January 2024 "
             "election as a copy of the earlier Digital Security Act; that Nepal's Public Service "
             "Broadcasting Act 2024 merged Radio Nepal and Nepal Television; and that Sri Lanka's "
             "1973 Press Council law lets the president name most of the Council's members."),
        tw(pp("amber", "For regional programmes", "A press strategy that works in Kathmandu may "
              "expose a partner in Dhaka or Lahore to legal risk. Ask local partners what the "
              "current law allows, and let them decide whether to be quoted."),
           pp("cyan", "Source", "RSF country pages for Pakistan, Bangladesh, Nepal and Sri Lanka, "
              "legal framework sections, consulted October 2026.")),
    ]),
]

# ===================== SECTION 03: BROADCAST, RADIO, COMMUNITY MEDIA =====================
S03 = [
    D("03", "Section Three", "Broadcast, radio and community media"),

    C("Public broadcaster", "Akashvani and Doordarshan: reach that nothing else matches", [
        body("Prasar Bharati runs Akashvani (All India Radio) and Doordarshan. For a development "
             "communicator, the public broadcaster matters because its signal reaches places and "
             "people that commercial media and the internet still miss, and because it broadcasts "
             "in many languages and dialects."),
        stats([
            {"num": "98%", "label": "population covered by Akashvani's transmitters (90% of area)",
             "color": "cyan", "source": PB_AR},
            {"num": "591", "label": "Akashvani broadcasting centres; 755 transmitters",
             "color": "indigo", "source": PB_AR},
            {"num": "23 + 181", "label": "languages and dialects in which Akashvani broadcasts",
             "color": "green", "source": PB_AR},
            {"num": "381", "label": "channels on DD FreeDish in 2025, incl. 265 educational",
             "color": "amber", "source": PB_AR},
        ], cols=4),
        body("At Independence, the same report notes, six radio stations covered 11% of the "
             "population. DD FreeDish is a free-to-air satellite service that needs no monthly "
             "subscription, so it reaches households that do not pay for cable or pay DTH.", sm=True),
    ], compact=True),

    C("Radio news", "Only the public broadcaster may originate radio news", [
        body("Radio in India is split into three tiers: public service radio (Akashvani), "
             "commercial FM, and community radio. The rules on news differ sharply between them. "
             "The Media Ownership Monitor described a state monopoly on radio news: private FM "
             "stations may broadcast music and entertainment but may not produce their own news "
             "and current affairs. The 2024 community radio guidelines likewise bar stations from "
             "broadcasting news and current affairs except content sourced from Akashvani, in its "
             "original form or translated."),
        tw(pp("cyan", "What it means for a launch", "A private FM station can run a public service "
              "announcement or an interview framed as information, but you should not expect it "
              "to carry a news story about your study. Akashvani's regional news units can."),
           pp("indigo", "Community radio", "A community station can discuss your programme in a "
              "phone-in, a drama or a local talk show, provided the programme is not news and "
              "current affairs or political in nature. Read the category list in the guidelines.")),
        body("Sources: RSF and DataLEADS, Media Ownership Monitor India (2019); MIB, Revised Policy "
             "Guidelines for setting up Community Radio Stations in India, 13 February 2024, para on "
             "content (g).", sm=True),
    ]),

    C("Community radio", "Community radio: a third tier built for local voice", [
        body("India approved a community radio policy in December 2002, open at first only to "
             "established educational institutions. The policy was reconsidered in 2006 to admit "
             "non-profit organisations such as civil society and voluntary groups, and amended "
             "in 2017, 2018, 2022 and February 2024. The first station was inaugurated on 1 "
             "February 2004, according to a PIB backgrounder for World Radio Day 2026."),
        table(["Rule in the 2024 guidelines", "What it says"], [
            ["Who may apply", "A not-for-profit legal entity with at least three years of service to the local community"],
            ["Local content", "At least 50% of content generated with the participation of the local community"],
            ["Range", "5-10 km, with a transmitter of up to 100 W ERP (up to 250 W on proven need)"],
            ["Advertising", "Limited local advertising, capped at 12 minutes per hour of broadcast"],
            ["News", "Only Akashvani news, unedited or faithfully translated"],
        ]),
        body("Source: MIB, Revised Policy Guidelines for setting up Community Radio Stations in India, "
             "13 February 2024; PIB, World Radio Day 2026 backgrounder, 12 February 2026.", sm=True),
    ], compact=True),

    C("How many stations", "Counting community radio stations: two official numbers", [
        body("Official counts of community radio stations differ depending on the source and the "
             "date. A PIB backgrounder published on 12 February 2026 said India had 528 community "
             "radio stations. TRAI's performance indicator report for January-March 2026 says 564 "
             "community radio stations were operational on 31 March 2026. The gap may reflect new "
             "stations, a difference between licensed and operational stations, or the date each "
             "count was taken."),
        stats([
            {"num": "528", "label": "community radio stations, PIB figure, February 2026",
             "color": "indigo", "source": "PIB, World Radio Day 2026 backgrounder, 12 Feb 2026"},
            {"num": "564", "label": "operational community radio stations, 31 March 2026",
             "color": "cyan", "source": TRAI_Q4},
        ]),
        hbox("A practical rule for any statistic you publish: name the source and the date, and if "
             "two official sources disagree, say which one you used and why. Readers trust a "
             "communicator who shows the seams.", "amber"),
    ]),

    C("Using community radio", "Working with a community radio station well", [
        body("Community radio stations are run by local organisations, often with a few paid staff "
             "and volunteers. They broadcast in local languages and dialects, and their audiences "
             "know the presenters. That makes them well suited to explaining entitlements, "
             "carrying farmers' or women's voices, and discussing a programme with the people it "
             "serves. It also means they are easily overloaded by NGOs that want free airtime."),
        tw([panel("green", "Do", [bullets([
                "Offer content the station's community wants, in its language and format",
                "Bring local people to speak alongside your staff",
                "Respect the station's editorial control and its programme code",
                "Pay for production costs where you are asking for a series"], sm=True)])],
           [panel("red", "Avoid", [bullets([
                "Sending a press release and expecting it to be read out",
                "Asking the station to carry political messaging or news",
                "Recording community members without informed consent",
                "Treating the station as a free advertising slot"], sm=True)])]),
        body("Source for the editorial limits: MIB community radio guidelines, 2024 (programme and "
             "advertising code, ban on news and current affairs other than Akashvani's).", sm=True),
    ]),

    C("Satellite to village", "Early lessons from India's broadcasting experiments", [
        body("India has a long record of using broadcasting for development, and the early "
             "experiments still shape debate. The Satellite Instructional Television Experiment "
             "(SITE) of 1975-76 used NASA's ATS-6 satellite to carry development programmes to "
             "around 2,400 villages in six states, reaching about 200,000 people, according to "
             "ISRO. It was followed by the Kheda Communications Project in Gujarat, which ISRO "
             "describes as a field laboratory for need-based and locale-specific programming."),
        tw(pp("cyan", "What SITE tested", "Whether centrally produced television could carry "
              "messages on agriculture, health and family planning to rural audiences at scale. "
              "ISRO also credits SITE with training 50,000 primary school science teachers in a year."),
           pp("indigo", "What Kheda added", "ISRO describes the Kheda Communications Project as a "
              "field laboratory for need-based and locale-specific programme transmission in "
              "Kheda district, Gujarat: content shaped around one district's problems.")),
        hbox("The shift from SITE to Kheda mirrors the shift in development communication theory "
             "covered in Section 07: from broadcasting messages to people towards producing them "
             "with people. Source: ISRO, Genesis page (isro.gov.in).", "green"),
    ]),

    C("Television", "Television: pay channels, free channels and the decline of pay DTH", [
        body("Television remains a mass medium, but how households receive it is changing. TRAI "
             "reports that of 908 permitted satellite channels available for downlinking in India, "
             "342 were pay channels on 31 March 2026 and the remaining 566 were treated as free-to-air. "
             "Pay DTH active subscribers fell from 50.99 million at the end of December 2025 to "
             "49.05 million at the end of March 2026, not counting DD FreeDish."),
        table(["Indicator, India", "Figure", "Date"], [
            ["Private satellite TV channels permitted by MIB", "917", "31 March 2026"],
            ["Satellite pay TV channels", "342 (238 SD, 104 HD)", "31 March 2026"],
            ["Pay DTH active subscribers", "49.05 million", "31 March 2026"],
            ["DD FreeDish channels", "381, including 265 educational", "2025"],
        ]),
        body("Sources: " + TRAI_Q4 + "; " + PB_AR + ". For a programme, the practical point is "
             "that free satellite television and public broadcasting reach households that "
             "neither pay for television nor use much mobile data.", sm=True),
    ], compact=True),
]

# ===================== SECTION 04: PLATFORMS AND MISINFORMATION =====================
S04 = [
    D("04", "Section Four", "Platforms, messaging apps and misinformation"),

    C("Where news is found", "Video platforms and messaging apps lead for online news users", [
        body("The Reuters Institute's Digital News Report surveys online news users each year. Its "
             "India sample is mainly English-speaking and online, which the Institute itself "
             "describes as a small subset of a larger and more diverse media market. Read the "
             "figures as a picture of urban, connected, English-using audiences, which are also "
             "the audiences most policy-makers belong to."),
        {"t": "chart", "canvas": "mcDnrChart",
         "title": "Share of respondents using each platform for news, India, 2025 (%)",
         "source": DNR25 + " (reutersinstitute.politics.ox.ac.uk)",
         "type": "bar",
         "data": {"labels": ["YouTube", "WhatsApp", "Instagram", "Facebook"],
                  "datasets": [{"label": "% using for news", "data": [55, 46, 37, 36],
                                "backgroundColor": "#6366F1"}]},
         "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:70, title:{display:true,text:'% of respondents'} } } }"}},
        body("The 2026 report puts YouTube's share at around 58%. It also notes the popularity of "
             "news creators on YouTube among its respondents. For a communicator, a ten-minute "
             "explainer by a trusted creator may reach more of this audience than a newspaper "
             "article, and it will be judged on different terms.", sm=True),
    ], compact=True),

    C("Trust", "Trust in news is low and uneven across brands", [
        body("The 2026 Digital News Report found overall trust in news in India at 39%, eighteenth "
             "of 48 markets, after a fall of four percentage points. At brand level, legacy print "
             "publishers and public broadcasters kept relatively high trust. The 2025 report added "
             "that brands seen as either extremely critical or extremely uncritical of people in "
             "power tend to score lower in a polarised environment."),
        stats([
            {"num": "39%", "label": "overall trust in news, India, 2026",
             "color": "amber", "source": DNR26},
            {"num": "18 / 48", "label": "India's position among markets surveyed, 2026",
             "color": "indigo", "source": DNR26},
            {"num": "-4 pp", "label": "change in overall trust from the previous year",
             "color": "red", "source": DNR26},
        ]),
        tw(pp("cyan", "Why it matters", "Coverage in a low-trust outlet may persuade few people "
              "outside its existing audience, and may make your work look partisan to everyone else."),
           pp("green", "What to do", "Aim for outlets trusted across political lines, publish your "
              "data and method so readers can check, and correct errors in the open.")),
    ], compact=True),

    C("Closed channels", "Messaging apps work differently from public media", [
        body("On a newspaper website or a public social media feed, a false claim and its correction "
             "sit in the same public space. In a messaging app they do not. Messages travel through "
             "private and group chats, often end-to-end encrypted, and are trusted because of who "
             "forwarded them: a relative, a caste or village group, a colleague. A correction "
             "published elsewhere may never reach the groups where the claim travelled."),
        table(["Feature", "Public platform", "Messaging app"], [
            ["Visibility", "Posts are public and searchable", "Content sits in private chats"],
            ["Trust signal", "Brand, account, follower count", "The person who forwarded it"],
            ["Correction", "Can be attached to the original", "Has to travel the same chain"],
            ["Monitoring", "Possible with public tools", "Only through members who share content"],
        ]),
        hbox("Design for this. Make the true version easy to forward: short, in the local language, "
             "with a source the group already trusts, ideally as a voice note or image card.", "green"),
    ], compact=True),

    C("Evidence", "WhatsApp misinformation and mob violence: the LSE study", [
        body("The most cited Indian study on messaging-app misinformation is <em>WhatsApp "
             "Vigilantes</em> by Shakuntala Banaji and Ram Bhat, with Anushi Agarwal, Nihal "
             "Passanha and Mukti Sadhana Pravin, published by the London School of Economics in "
             "2019. It examined how misinformation circulated on WhatsApp connects to lynchings and "
             "vigilante violence in India."),
        tw(pp("indigo", "Method", "Fieldwork in Madhya Pradesh, Uttar Pradesh, Karnataka and "
              "Maharashtra in 2019. About 275 WhatsApp users reached through 65 in-depth "
              "interviews, 16 focus groups and 10 expert interviews, and more than 1,000 "
              "pieces of content shared voluntarily by respondents."),
           pp("cyan", "Scope", "Users in metropolises, medium-sized cities, district headquarters, "
              "small towns and villages, with expert interviews in fact-checking, law enforcement, "
              "academia, NGOs and journalism.")),
        body("Source: Banaji, S. and Bhat, R. et al. (2019), <em>WhatsApp Vigilantes: An exploration "
             "of citizen reception and circulation of WhatsApp misinformation linked to mob violence "
             "in India</em>, LSE Department of Media and Communications.", sm=True),
    ]),

    C("What the study found", "Prejudice drove the sharing more than digital illiteracy", [
        body("The study's central finding challenges a common assumption in development "
             "programmes: that people forward false messages because they cannot tell true from "
             "false. The authors found prejudice and ideology to be the larger driver, and they "
             "also found that sharing patterns followed caste, religion and gender. In their words:"),
        quote("In a majority of instances, misinformation and disinformation which contributes to the "
              "formation of mobs that engage in lynching and other discriminatory violence appears to "
              "be spread largely for reasons of prejudice and ideology rather than out of ignorance "
              "or digital illiteracy.",
              "Banaji and Bhat et al., WhatsApp Vigilantes, LSE, 2019, executive summary"),
        tw(pp("amber", "Implication for programmes", "Digital literacy training alone will not stop "
              "hateful misinformation. The authors call for critical media literacy that "
              "emphasises constitutional values and human rights."),
           pp("cyan", "Other recommendations", "Easier in-app reporting and tracking, clearer "
              "penalties for sharing misinformation, and joint action by platforms, governments, "
              "civil society and users.")),
    ], compact=True),

    C("Responding", "When misinformation targets your programme", [
        body("Sooner or later a false claim will circulate about a programme: that a vaccine "
             "drive is a sterilisation scheme, that a survey is collecting data to take away "
             "ration cards, that a women's group is a front for conversion. The response that "
             "works is fast, local and specific, and it comes from people the community already "
             "trusts."),
        flow(["DETECT: field staff and partners report claims they hear",
              "ASSESS: how far has it spread, who believes it, what harm can it do",
              "RESPOND: a short, forwardable correction from a trusted local voice",
              "FOLLOW UP: answer questions in person, record what changed"]),
        tw(pp("green", "Write the correction well", "Lead with the accurate fact, give the source, "
              "explain briefly why the false claim is wrong, and end with what people can do. "
              "Avoid repeating the false claim in the headline or image."),
           pp("red", "Do not", "Argue with individuals in large groups, mock people who believed "
              "the claim, or issue a long denial in English when the rumour is circulating in "
              "Bhojpuri.")),
    ]),

    C("Shutdowns", "Plan for the internet being switched off", [
        body("South Asia has some of the world's most frequent internet shutdowns. Access Now's "
             "#KeepItOn report, released on 31 March 2026, recorded at least 313 shutdowns in 52 "
             "countries in 2025, of which 195 were in 11 Asia-Pacific countries. A campaign that "
             "depends on mobile data can go dark in a district during protests, exams or "
             "elections."),
        {"t": "chart", "canvas": "mcShutChart",
         "title": "Internet shutdowns recorded in 2025, selected countries",
         "source": "Access Now and #KeepItOn coalition, Rising repression meets global resistance: "
                   "Internet shutdowns in 2025, press release 31 March 2026",
         "type": "bar",
         "data": {"labels": ["Myanmar", "India", "Pakistan", "Nepal"],
                  "datasets": [{"label": "Shutdowns", "data": [95, 65, 20, 2],
                                "backgroundColor": "#EF4444"}]},
         "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:100, title:{display:true,text:'Shutdowns recorded'} } } }"}},
        body("Myanmar's figure is 'at least 95'. The same release notes that in Bangladesh sustained "
             "advocacy led to proposed legislation to prohibit shutdowns altogether. Keep an offline "
             "route for every critical message: radio, printed material, frontline workers.", sm=True),
    ], compact=True),
]

# ===================== SECTION 05: PRESS FREEDOM =====================
S05 = [
    D("05", "Section Five", "Press freedom and the Constitution"),

    C("The index", "Press freedom in South Asia: RSF's 2026 rankings", [
        body("Reporters Without Borders publishes the World Press Freedom Index each year, ranking "
             "180 countries and territories. "
             "Every major South Asian country except Nepal sits in the lower part of the table, "
             "and India fell six places."),
        table(["Country", "Rank 2026 (of 180)", "Score 2026", "Rank 2025", "RSF category 2026"], [
            ["Nepal", "87", "54.80", "90", "Difficult"],
            ["Sri Lanka", "134", "40.77", "139", "Difficult"],
            ["Bangladesh", "152", "33.05", "149", "Very serious"],
            ["Pakistan", "153", "32.61", "158", "Very serious"],
            ["India", "157", "31.96", "151", "Very serious"],
        ]),
        body("Source: " + RSF26 + ". Categories follow RSF's score bands: below 40 is 'very "
             "serious', 40 to 55 'difficult'. India's 2025 score was 32.96.", sm=True),
    ], compact=True),

    C("Reading the index", "What the RSF index measures and what it does not", [
        body("RSF scores each country on five contextual indicators: political context, legal "
             "framework, economic context, sociocultural context and safety. The score combines a "
             "quantitative tally of abuses against journalists and media with a qualitative "
             "analysis based on answers from press freedom specialists (journalists, researchers, "
             "academics and human rights defenders) to a questionnaire available in 25 languages."),
        tw(pp("cyan", "Use it for", "A comparable, annually updated signal of the environment "
              "journalists and media face, and its direction of travel. It is useful for risk "
              "assessment before a regional campaign."),
           pp("amber", "Be careful", "Part of the score rests on expert perceptions, and a few "
              "points of score can move a country many places. Cite the indicator and its method "
              "alongside any rank, and treat small moves in rank with caution.")),
        hbox("Source: RSF, methodology used for compiling the World Press Freedom Index 2026 "
             "(rsf.org). When you cite an index in your own reports, name the edition, the method and "
             "the date, as you would for a survey.", "indigo"),
    ]),

    C("Article 19(1)(a)", "The press is free because speech is free", [
        body("The Indian Constitution has no separate clause on the press. Article 19(1)(a) "
             "guarantees all citizens the right to freedom of speech and expression, and the "
             "Supreme Court has read freedom of the press into it. RSF's India profile makes the "
             "same point: press freedom is not mentioned as such, but is protected through the "
             "right to free expression."),
        quote("Freedom of speech and of the press lay at the foundation of all democratic "
              "organisations, for without free political discussion no public education, so "
              "essential for the proper functioning of the processes of popular government, is "
              "possible.",
              "Romesh Thappar v State of Madras, decided 26 May 1950, 1950 SCR 594, AIR 1950 SC 124 "
              "(Patanjali Sastri J)"),
        body("The case concerned a ban on the entry and circulation in Madras of <em>Cross Roads</em>, "
             "a weekly printed in Bombay. The Court struck the ban down because the restriction then "
             "permitted by Article 19(2) did not extend to the public safety and public order "
             "grounds the state relied on.", sm=True),
    ], compact=True),

    C("Article 19(2)", "The eight grounds on which speech may be restricted", [
        body("Article 19(2) lets the state impose <strong>reasonable restrictions</strong> on free "
             "speech, but only in the interests of listed grounds. Parliament widened the clause "
             "soon after Romesh Thappar: the Constitution (First Amendment) Act of 18 June 1951 "
             "added friendly relations with foreign States, public order and incitement to an "
             "offence. Sovereignty and integrity of India were added later."),
        tw([panel("cyan", "The grounds today", [bullets([
                "Sovereignty and integrity of India",
                "Security of the State",
                "Friendly relations with foreign States",
                "Public order",
                "Decency or morality",
                "Contempt of court",
                "Defamation",
                "Incitement to an offence"], sm=True)])],
           [panel("indigo", "What 'reasonable' requires", [body(
                "A restriction must fall within one of the grounds, have a close link to it, and be "
                "proportionate. In Anuradha Bhasin (2020) the Supreme Court applied the test of "
                "proportionality to internet suspensions. Any law that limits what you publish "
                "has to pass these tests, and courts have struck down several that did not.",
                sm=True)])]),
        body("Sources: Constitution of India, Article 19(2), current text; Constitution (First "
             "Amendment) Act 1951, s3.", sm=True),
    ]),

    C("Shreya Singhal 2015", "Shreya Singhal: the end of section 66A", [
        body("Section 66A of the Information Technology Act 2000 punished sending 'grossly "
             "offensive' or 'menacing' messages, or information known to be false, for the "
             "purpose of causing annoyance or inconvenience. It was used to arrest people over "
             "social media posts. On 24 March 2015, in <em>Shreya Singhal v Union of India</em> "
             "(AIR 2015 SC 1523), the Supreme Court struck it down in its entirety as violating "
             "Article 19(1)(a) and not saved by Article 19(2)."),
        table(["Provision", "Holding"], [
            ["IT Act s66A", "Struck down in its entirety"],
            ["IT Act s69A and the 2009 Blocking Rules", "Upheld as constitutionally valid"],
            ["IT Act s79 (intermediary safe harbour)", "Valid, with s79(3)(b) read down to actual knowledge from a court order or government notification"],
        ]),
        quote("There are three concepts which are fundamental in understanding the reach of this most "
              "basic of human rights. The first is discussion, the second is advocacy, and the third "
              "is incitement.",
              "Shreya Singhal v Union of India, 24 March 2015, para 13"),
    ], compact=True),

    C("Anuradha Bhasin 2020", "Anuradha Bhasin: internet speech and shutdown orders", [
        body("After communications were suspended in Jammu and Kashmir on 4 August 2019, the "
             "executive editor of the <em>Kashmir Times</em> challenged the restrictions. On 10 January 2020, in "
             "<em>Anuradha Bhasin v Union of India</em> (AIR 2020 SC 1308), the Supreme Court "
             "declared that freedom of speech and the freedom to practise a profession or carry "
             "on a business over the internet enjoy constitutional protection under Articles "
             "19(1)(a) and 19(1)(g)."),
        tw([panel("cyan", "Directions", [bullets([
                "Publish all orders suspending telecom services, so they can be challenged",
                "Indefinite suspension of internet is impermissible under the 2017 Suspension Rules",
                "Suspension is for a temporary duration only",
                "Orders must be proportionate and are subject to judicial review"], sm=True)])],
           [panel("green", "Why it matters to communicators", [body(
                "If your programme or partner relies on mobile data in an area under a suspension "
                "order, the order should be public. Ask for it. Its duration and stated reasons "
                "are what you would rely on in any challenge or advocacy.", sm=True)])]),
        body("Source: Anuradha Bhasin v Union of India, 10 January 2020, operative directions; "
             "Temporary Suspension of Telecom Services (Public Emergency or Public Service) "
             "Rules 2017.", sm=True),
    ]),

    C("Defamation stands", "Criminal defamation survived constitutional challenge", [
        body("Unlike some democracies, India keeps defamation as a crime as well as a civil "
             "wrong. In <em>Subramanian Swamy v Union of India</em>, decided on 13 May 2016, a "
             "bench of Justices Dipak Misra and Prafulla C. Pant upheld the constitutional "
             "validity of sections 499 and 500 of the Indian Penal Code and section 199 of the "
             "Code of Criminal Procedure. The Court treated reputation as part of the right to "
             "life under Article 21, to be balanced against free speech."),
        tw(pp("amber", "Then", "IPC ss 499-500 defined and punished defamation; CrPC s199 required "
              "a complaint by the person aggrieved."),
           pp("cyan", "Now", "The Bharatiya Nyaya Sanhita 2023 carries the offence in s356, and the "
              "Bharatiya Nagarik Suraksha Sanhita 2023 carries the complaint rule in s222. Section "
              "06 reads both.")),
        hbox("For an NGO, a defamation complaint can be filed in a court far from your office, by "
             "an official or company you criticised. Legal cost and time are the real penalty. "
             "Check facts and wording before publication, every time.", "red"),
    ]),

    C("Safety", "Journalists face real danger, and partners share it", [
        body("Press freedom rankings rest partly on violence against journalists. RSF's 2026 India "
             "profile states that with an average of two to three journalists killed because of "
             "their work every year, India is one of the world's most dangerous countries for "
             "media professionals. Local reporters and stringers who cover land, mining, sand, "
             "elections or caste violence are the most exposed."),
        tw(pp("red", "Your duty of care", "If a journalist relies on your data, your field staff or "
              "your community contacts, your choices affect their safety and your partners' safety. "
              "Do not put a source's name or village in a story without their informed agreement."),
           pp("green", "Practical steps", "Agree how sources will be described before an interview, "
              "store contact lists securely, and have a plan for what you will do if a journalist "
              "or community member who spoke to you is threatened.")),
        body("Source: RSF India country page (safety indicator), consulted October 2026.", sm=True),
    ]),
]

# ===================== SECTION 06: LEGAL FRAME =====================
S06 = [
    D("06", "Section Six", "The legal frame for communicators"),

    C("Risk map", "Eight legal risks every communicator should know", [
        body("Most communicators will never be sued or prosecuted. Those who are usually walked "
             "into one of a small number of well-known traps. This table maps them to the law "
             "and to the later slides that explain each one."),
        table(["Risk", "Main law (India)", "Typical trigger"], [
            ["Defamation", "BNS 2023 s356; BNSS 2023 s222", "Naming an official or company with an unproven allegation"],
            ["Identifying a rape or child victim", "BNS s72; JJ Act 2015 s74; POCSO 2012 s23", "A photograph, village name or school in a case study"],
            ["Online content rules", "IT Act 2000; IT Rules 2021", "Digital news content, platform takedown orders"],
            ["Broadcast content", "Cable TV Networks (Regulation) Act 1995, s5", "A TV spot breaching the programme code"],
            ["Copyright", "Copyright Act 1957, ss 17, 52", "Using a photograph you did not commission or license"],
            ["Personal data", "DPDP Act 2023 (duties from 13 May 2027)", "Publishing identifiable data or photos without consent"],
            ["Election period", "RP Act 1951, ss 126, 126A, 127A", "Campaign-like messaging close to polls"],
            ["Contempt of court", "Contempt of Courts Act 1971", "Commenting on pending cases in a way that prejudges them"],
        ]),
    ], compact=True),

    C("Defamation: the offence", "BNS section 356: what counts as defamation", [
        body("Section 356(1) of the Bharatiya Nyaya Sanhita 2023 says that whoever, by words spoken "
             "or intended to be read, or by signs or visible representations, makes or publishes "
             "any imputation concerning any person, intending to harm or knowing or having reason "
             "to believe that it will harm that person's reputation, is said to defame that person, "
             "except in the excepted cases. Section 356(2) makes it punishable with simple "
             "imprisonment of up to two years, or fine, or both, or community service."),
        tw(pp("amber", "Who can be defamed", "Explanation 2 says it may amount to defamation to make "
              "an imputation concerning a company or an association or collection of persons. A "
              "report criticising a named contractor or hospital chain is within reach."),
           pp("indigo", "Who can complain", "BNSS s222(1): no court takes cognizance except on a "
              "complaint by a person aggrieved. That is why complaints are often filed far from "
              "the publisher, wherever the complainant chooses.")),
        body("Sources: Bharatiya Nyaya Sanhita 2023, s356 (MHA official text); Bharatiya Nagarik "
             "Suraksha Sanhita 2023, s222. The BNS replaced the Indian Penal Code, whose ss 499-500 "
             "carried the same offence.", sm=True),
    ]),

    C("Defamation: the defences", "The exceptions a careful communicator relies on", [
        body("Section 356 lists ten exceptions. Four matter most to development communicators, "
             "because they protect accurate reporting of evidence and fair criticism of public "
             "action. Each depends on facts you can prove and good faith you can show, so keep "
             "your notes, data and drafts."),
        table(["Exception", "What it protects", "What you need"], [
            ["1. Truth for public good", "A true imputation that it is for the public good to publish",
             "Evidence of truth; a public interest reason"],
            ["2 and 3. Public conduct", "Good faith opinion on the public conduct of a public servant or any person touching a public question",
             "Opinion tied to the public conduct in question"],
            ["4. Court reports", "A substantially true report of the proceedings of a court",
             "Accurate reporting of what was said and decided"],
            ["9. Protection of interests", "A good faith imputation made to protect someone's interests or for the public good",
             "Care in checking; limited circulation where possible"],
        ]),
        hbox("A rule of thumb: describe what the data show, attribute every allegation to its "
             "source, give the person or body criticised a chance to respond before publication, "
             "and print their response. Source: BNS 2023, s356, Exceptions 1-10.", "green"),
    ], compact=True),

    C("IT Rules 2021", "Digital news publishers and the IT Rules 2021", [
        body("The Information Technology (Intermediary Guidelines and Digital Media Ethics Code) "
             "Rules 2021 were notified as G.S.R. 139(E) on 25 February 2021. Part III applies a "
             "Code of Ethics to publishers of news and current affairs content online. The Code, in "
             "the Appendix, incorporates the Press Council of India's Norms of Journalistic Conduct "
             "and the Programme Code under section 5 of the Cable Television Networks (Regulation) "
             "Act 1995."),
        flow(["LEVEL I: self-regulation by the publisher (grievance decided within 15 days)",
              "LEVEL II: self-regulating body of publishers",
              "LEVEL III: oversight mechanism of the Central Government"]),
        tw(pp("amber", "Under challenge", "On 14 August 2021 the Bombay High Court stayed Rule 9(1) "
              "and 9(3), which require adherence to the Code of Ethics, in a petition by the "
              "digital portal The Leaflet (Bar and Bench, 14 August 2021). Check the current "
              "position before relying on these rules."),
           pp("cyan", "Does it apply to you", "An NGO's website is not usually a news publisher. "
              "If your organisation runs a news portal or regular current affairs video channel, "
              "take advice on whether Part III applies.")),
    ], compact=True),

    C("Fact check unit", "The 2023 fact check unit amendment and Kunal Kamra", [
        body("On 6 April 2023 the government amended Rule 3(1)(b)(v) of the IT Rules so that "
             "intermediaries had to make reasonable efforts against content which, in respect of "
             "any business of the Central Government, is identified as fake, false or misleading "
             "by a fact check unit notified by the Ministry. The satirist Kunal Kamra and others "
             "challenged it in the Bombay High Court."),
        flow(["31 Jan 2024: split verdict (Patel J strikes down, Gokhale J upholds)",
              "20 Mar 2024: Union notifies PIB's unit as the fact check unit",
              "21 Mar 2024: Supreme Court stays that notification",
              "20 Sep 2024: tie-breaker Chandurkar J agrees with Patel J",
              "26 Sep 2024: Division Bench strikes the amendment down by majority"]),
        body("Chandurkar J found the amended rule violative of Articles 14, 19(1)(a) and 19(1)(g), "
             "ultra vires the IT Act, vague in the phrase 'fake or false or misleading', and failing "
             "the test of proportionality (Bombay High Court, final judgment of 26 September 2024, "
             "quoting his opinion). The Union's appeal was listed in the Supreme Court on 10 March "
             "2026, which issued notice and declined to stay the High Court's judgment (Internet "
             "Freedom Foundation, 11 March 2026). Check its current status before relying on it.",
             sm=True),
    ], compact=True),

    C("Press Council norms", "The Press Council's Norms of Journalistic Conduct", [
        body("The Press Council of India is a statutory body under the Press Council Act 1978, set "
             "up to preserve press freedom and improve standards. It publishes Norms of Journalistic "
             "Conduct, last revised as a 2022 edition. They set the standard for newspapers, and through the IT "
             "Rules Appendix they are also the reference for digital news publishers. They are a "
             "useful checklist for any organisation that publishes."),
        table(["Norm (2022 edition)", "What it requires"], [
            ["9. Corrections", "Publish a correction promptly and with due prominence, with apology or regret in serious lapses"],
            ["34. Pre-publication verification", "Check imputations against a citizen with the person concerned and carry their version"],
            ["41. Right of reply", "Publish the reply of a person or body criticised"],
            ["42. Right to privacy", "No names or photographs of victims of rape, abduction or sexual assault on children"],
            ["39(b). Reporting suicide", "No method, no location details, no sensational headlines, no photographs"],
        ]),
        body("Sources: Press Council of India, Norms of Journalistic Conduct, 2022 edition; PIB "
             "National Press Day 2025 backgrounder (PCI's statutory basis).", sm=True),
    ], compact=True),

    C("Broadcast and elections", "Television content and election-period rules", [
        body("Two sets of rules catch development communicators by surprise. The first governs "
             "television. Section 5 of the Cable Television Networks (Regulation) Act 1995 says no "
             "person shall transmit or re-transmit a programme through a cable service unless it "
             "conforms to the prescribed programme code; section 20 lets the Central Government "
             "prohibit a cable network's operation in the public interest. A public service "
             "spot is a programme too."),
        tw([panel("indigo", "Representation of the People Act 1951", [bullets([
                "s126: no display of election matter by television or similar apparatus in a polling "
                "area during the 48 hours ending with the close of poll",
                "s126A: no publication of exit poll results during the period the Election "
                "Commission notifies",
                "s127A: every election pamphlet or poster must carry the printer's and "
                "publisher's names and addresses"], sm=True)])],
           [panel("amber", "Practical rule", [body(
                "Pause campaign-style communication on voting, entitlements or schemes in the "
                "days before polling in an area, and avoid anything that could read as support "
                "for a party or candidate. Check the Election Commission's current Model Code "
                "instructions for the election in question.", sm=True)])]),
    ]),

    C("Copyright", "Who owns the photograph, and when you may quote", [
        body("Section 17 of the Copyright Act 1957 makes the author the first owner of copyright, "
             "with exceptions. Under s17(b), when a photograph is taken for valuable consideration "
             "at the instance of any person, that person is the first owner unless there is an "
             "agreement to the contrary. Section 52(1)(a) allows fair dealing with a work for "
             "private or personal use including research, for criticism or review, and for "
             "reporting current events and current affairs."),
        tw(pp("cyan", "Commissioned work", "If you pay a photographer to cover your programme, you "
              "will usually own the copyright unless the contract says otherwise. Write the "
              "contract anyway: it should also settle credit, reuse by the photographer, and how "
              "consent of the people photographed was obtained."),
           pp("amber", "Other people's work", "Fair dealing covers quoting a report to review it or "
              "a news photograph to report on events. It does not cover lifting a stock image or a "
              "journalist's photograph for your fundraising brochure.")),
        body("Sources: Copyright Act 1957, s17 and s52(1)(a) (text as amended).", sm=True),
    ]),

    C("Personal data", "The DPDP Act: what is in force and what is coming", [
        body("The Digital Personal Data Protection Act 2023 commences in stages under G.S.R. 843(E) "
             "of 13 November 2025, with the DPDP Rules 2025 (G.S.R. 846(E)) following the same "
             "phasing. As of October 2026, the definitions, the Data Protection Board (ss 18-26) "
             "and s44(3), which amends RTI Act s8(1)(j), are in force. Section 6(9) and s27(1)(d) "
             "follow on 13 November 2026."),
        table(["Provision", "Commencement"], [
            ["Definitions, Data Protection Board (ss 18-26), s44(3)", "13 November 2025 (in force)"],
            ["s6(9) and s27(1)(d)", "13 November 2026"],
            ["Duties and rights (ss 3-17, incl. s9 on children and s17 exemptions such as s17(2)(b) for research)", "13 May 2027"],
            ["Penalties (ss 27-34)", "13 May 2027"],
        ]),
        hbox("For communicators: the consent duties do not apply yet, but programmes running into "
             "2027 should already treat photographs, testimonies, mailing lists and WhatsApp groups "
             "as personal data and record consent. The Data Protection &amp; the DPDP Act deck "
             "covers the detail.", "indigo"),
    ], compact=True),
]

# ===================== SECTION 07: COMMUNICATION FOR DEVELOPMENT =====================
S07 = [
    D("07", "Section Seven", "Communication for development: theory and critique"),

    C("Origins", "The modernisation model: media as a multiplier", [
        body("Communication for development (often shortened to C4D) began as an applied field in "
             "the 1950s and 1960s, within modernisation theory. Two books defined it. Daniel "
             "Lerner's <em>The Passing of Traditional Society: Modernizing the Middle East</em> "
             "(Free Press, 1958) tied the spread of mass media to the modernisation of "
             "'traditional' societies. Wilbur Schramm's <em>Mass Media and "
             "National Development: The Role of Information in the Developing Countries</em> "
             "(Stanford University Press and UNESCO, 1964) examined the part mass media could "
             "play in economic and social development in developing countries."),
        term("Communication for development",
             "The planned use of communication (media, interpersonal channels, participatory "
             "processes) to support social and economic change, from informing people about "
             "services to enabling communities to shape the decisions that affect them."),
        tw(pp("cyan", "The core assumption", "Information flows from experts and the state to the "
              "public. More media exposure leads to new attitudes, which lead to new behaviour."),
           pp("indigo", "Where India fits", "SITE (1975-76) was designed in this spirit: centrally "
              "produced programmes on farming, health and family planning beamed to villages.")),
    ]),

    C("Diffusion", "Diffusion of innovations: how practices spread", [
        body("A second strand, associated above all with Everett Rogers, studied how new practices "
             "spread through a social system: through mass media to early adopters, then through "
             "interpersonal networks to everyone else. The flow below is a simplified sequence. "
             "The idea explains why a farmer is more likely to adopt a seed variety after a "
             "neighbour has used it than after hearing a radio advertisement."),
        flow(["AWARENESS: media tells people a practice exists",
              "INTEREST: people seek out more information",
              "TRIAL: early adopters try it",
              "ADOPTION: neighbours copy what they see working"]),
        tw(pp("green", "What still holds", "Interpersonal channels and trusted local adopters matter "
              "more than media alone for practice change. Community health workers and self-help "
              "groups carry messages further than posters."),
           pp("amber", "What it missed", "Why some people cannot adopt even when persuaded: they lack "
              "land, credit, time or power within the household. The model tended to blame "
              "'laggards' for structural barriers.")),
    ]),

    C("The critique", "Rogers and the decline of the dominant model", [
        body("By the 1970s the modernisation model was under attack, including from its own "
             "authors. In April 1976 Everett Rogers edited a special issue of the journal "
             "<em>Communication Research</em> on new perspectives in communication and "
             "development. His own article in it, 'Communication and Development: The Passing of "
             "the Dominant Paradigm' (vol 3, no 2, pp 213-240), describes the dominant model, the "
             "factors behind its decline in intellectual circles after about 1970, and the "
             "emerging alternatives."),
        table(["Criticism", "What it meant in practice"], [
            ["Top-down", "Messages designed in capitals, for audiences never consulted"],
            ["Deficit view", "Poor people treated as lacking information, when they lacked resources or power"],
            ["Blind to structure", "Land, caste, gender and class barriers left out of the analysis"],
            ["Pro-innovation bias", "The new practice assumed good; harms and local knowledge ignored"],
            ["Media-centric", "Exposure counted as success, whatever happened afterwards"],
        ]),
        body("The critique carried weight because Rogers had popularised the diffusion model "
             "himself, in <em>Diffusion of Innovations</em> (Free Press, 1962). His article set out the model, the factors behind its decline "
             "and the alternatives then emerging, which the next slides follow.", sm=True),
    ], compact=True),

    C("Freire", "Paulo Freire and the turn to dialogue", [
        body("The Brazilian educator Paulo Freire's <em>Pedagogy of the Oppressed</em> was first "
             "published in 1970, in English by Herder and Herder in New York and in Spanish in "
             "Montevideo. Freire "
             "called conventional teaching the 'banking' model, in which the teacher deposits "
             "knowledge into passive students. He argued for education through dialogue, in which "
             "people examine their own situation, name its causes and act on it together."),
        tw([panel("red", "Banking model in communication", [bullets([
                "Experts decide the message",
                "Audiences receive and are expected to comply",
                "Success means people repeat the message"], sm=True)])],
           [panel("green", "Dialogic model", [bullets([
                "Communities define the problem with you",
                "Communication is a conversation that changes both sides",
                "Success means people act on their own analysis, including against the programme"],
                sm=True)])]),
        hbox("Freire's influence runs through adult literacy campaigns, community radio, "
             "participatory video and participatory research across South Asia. See the "
             "Participatory Methods deck for the research side.", "indigo"),
    ]),

    C("Participatory communication", "Participatory communication in practice", [
        body("Participatory communication puts the production of media, as well as its "
             "reception, in the hands of the people a programme serves. In South Asia it takes "
             "familiar forms: community radio run by local organisations; the Kheda "
             "Communications Project's locale-specific programming; participatory video; women's groups "
             "producing their own audio; street theatre devised with the audience."),
        table(["Dimension", "Diffusion approach", "Participatory approach"], [
            ["Who defines the problem", "Experts and agencies", "Communities, with outside support"],
            ["Direction", "One-way, centre to periphery", "Horizontal and two-way"],
            ["Media used", "Mass media campaigns", "Local, low-cost, community-owned media"],
            ["Time scale", "Campaign weeks or months", "Long-term processes"],
            ["Success measure", "Reach and recall", "Voice, collective action, decisions changed"],
        ]),
        hbox("Most real programmes combine both. A mass media campaign can tell people that a "
             "scheme exists; a participatory process can reveal why they still cannot use it.", "cyan"),
    ], compact=True),

    C("Today's approaches", "Four families of development communication today", [
        body("The field now uses several labels, often overlapping. Knowing which one you are "
             "doing helps you choose methods and measures, and avoids promising a funder behaviour "
             "change from what is really a media relations exercise."),
        table(["Approach", "Aim", "Typical tools", "Deck to see"], [
            ["Social and behaviour change communication", "Change individual and social practices",
             "Formative research, interpersonal counselling, mass media drama", "Behaviour Change Communication"],
            ["Media advocacy", "Change a policy or institutional decision", "News coverage, op-eds, briefings",
             "Advocacy Basics"],
            ["Research communication", "Get evidence used by decision-makers", "Briefs, launches, data stories", "This deck"],
            ["Participatory and community media", "Give communities voice and control", "Community radio, video, theatre",
             "Participatory Methods"],
        ]),
        body("All four need the same groundwork: a clear objective, a known audience, a message "
             "tested with that audience, a channel the audience uses and trusts, and a way to tell "
             "whether anything changed.", sm=True),
    ], compact=True),

    C("Limits of participation", "Participation has its own failure modes", [
        body("Participatory communication can fail too, and the failures are harder to see than a "
             "badly designed poster. Village meetings are dominated by those who already hold "
             "power. 'Community voice' in a donor report may be three quotations selected by "
             "programme staff. A community radio station licensed to an NGO may become the NGO's "
             "public relations channel."),
        tw([panel("amber", "Warning signs", [bullets([
                "The same few people speak at every meeting",
                "Women, Dalit and Adivasi members appear only in photographs",
                "Community-produced content never criticises the programme",
                "Decisions were taken before the consultation began"], sm=True)])],
           [panel("green", "Safeguards", [bullets([
                "Separate meetings for groups who will not speak in mixed settings",
                "Pay people for their time and expertise",
                "Publish what the community said, including criticism",
                "Show what changed as a result, or explain why nothing did"], sm=True)])]),
        hbox("The test of participation is whether the people consulted could change the plan. "
             "If they could not, call it consultation and report it as such.", "indigo"),
    ]),
]

# ===================== SECTION 08: WRITING =====================
S08 = [
    D("08", "Section Eight", "Writing for different audiences"),

    C("Audience first", "One finding, four audiences, four documents", [
        body("A single study usually needs several written products, because the people who need "
             "it read differently. A district health officer needs to know what to do on Monday; a "
             "journalist needs a story with a new fact and a human face; a funder needs to know "
             "whether the money worked; a community needs to know what was found about them and "
             "what happens next."),
        table(["Reader", "What they need", "Format", "Length guide"], [
            ["Official or legislator", "The decision the evidence supports", "Policy brief or note", "Two to four pages"],
            ["Journalist", "News, numbers, a person, a quote", "Press release and fact sheet", "One page plus annexe"],
            ["General public", "What it means for them, in their language", "Explainer, video, radio piece", "Short"],
            ["Community studied", "What was found, what happens next", "Meeting, poster, audio in local language", "As short as possible"],
            ["Funder or peer", "Method, results, limits", "Full report and data", "As long as needed"],
        ]),
        hbox("Write the full report first, then the brief, then the release. Each shorter document "
             "should link to the longer one so readers can check.", "green"),
    ], compact=True),

    C("Press release", "The anatomy of a press release", [
        body("A press release is written in news style so that a journalist can lift sentences from "
             "it. It uses the inverted pyramid: the most important fact first, then supporting "
             "detail, then background. Journalists receive many releases a day and decide in a few "
             "seconds whether to read past the first paragraph."),
        flow(["HEADLINE: the finding, with a number, in plain words",
              "FIRST PARAGRAPH: who found what, where, when and why it matters",
              "SECOND PARAGRAPH: the strongest supporting evidence",
              "QUOTE: one spokesperson saying something worth quoting",
              "DETAIL AND METHOD: sample, dates, limits",
              "NOTES: contact, link to the study, embargo time"]),
        tw(pp("green", "Good habits", "One page. Date and place line. A named contact who will "
              "answer the phone. Numbers rounded sensibly with the source stated. The report "
              "shared as a link."),
           pp("red", "Common faults", "A headline that names the organisation and not the "
              "finding, three paragraphs of background before the news, quotes from five "
              "dignitaries, and jargon such as 'capacity building' and 'convergence'.")),
    ]),

    C("A worked release", "Illustrative press release: before and after", [
        body("The example below is <strong>Illustrative</strong>: the organisation, study and "
             "figures are invented for teaching. It shows how the same content reads when it "
             "is organised around the finding."),
        tw([panel("red", "Before", [body(
                "<em>XYZ Foundation releases report on adolescent health.</em> XYZ Foundation, "
                "working since 2004 for the upliftment of communities, in convergence with "
                "line departments, organised a state-level dissemination workshop on Tuesday "
                "in the gracious presence of dignitaries. The study covered various aspects "
                "of adolescent health and made several recommendations.", sm=True)])],
           [panel("green", "After", [body(
                "<em>Two in five girls in surveyed blocks miss school during periods, study "
                "finds (Illustrative).</em> A survey of 1,200 girls aged 12-17 in four blocks "
                "of a Bihar district found that 41% had missed at least one school day in the "
                "past month because of menstruation. Schools without a working girls' toilet "
                "reported twice the rate of absence. The study, by XYZ Foundation, recommends "
                "repairing toilets in the 63 schools it lists.", sm=True)])]),
        hbox("The 'after' version has a number, a place, a comparison, a cause the reader can "
             "picture and a specific ask. Every one of those must be true and checkable in "
             "your real release.", "amber"),
    ]),

    C("Op-eds", "Writing an opinion piece that an editor will accept", [
        body("An op-ed is an argument signed by an author, published on a newspaper's opinion "
             "page or website. Editors accept pieces that are timely, make one clear argument, "
             "carry evidence the author is qualified to present, and are written for a general "
             "reader. Check each paper's submission guidelines for length and exclusivity; many "
             "ask that a piece is not offered elsewhere at the same time."),
        tw([panel("cyan", "Structure that works", [bullets([
                "Hook: a news event, a date, a decision due soon",
                "Argument: one sentence stating what should happen",
                "Evidence: two or three facts, each with its source",
                "Counter-argument: the strongest objection, answered",
                "Close: the specific action and who should take it"], sm=True)])],
           [panel("amber", "Before you submit", [bullets([
                "Check that you may publish under your name, and in what capacity",
                "Clear any data with its owner and any partner named",
                "Disclose interests, such as funding from a party to the debate",
                "Write a two-line pitch email with the argument in the first sentence"], sm=True)])]),
        hbox("Time pieces to decisions: the budget, a parliamentary session, the anniversary of a "
             "scheme, the release of official data such as an NFHS round or a PLFS report.", "indigo"),
    ]),

    C("Explainers", "Explainers: answering the questions readers actually have", [
        body("An explainer helps a reader understand an issue, a scheme or a dataset, without "
             "arguing a position. It suits development organisations well because it uses their "
             "expertise without asking an editor to publish advocacy. Good explainers are built "
             "from the reader's questions, in the order the reader would ask them."),
        table(["Reader's question", "What the answer needs"], [
            ["What is it?", "A plain definition in one or two sentences"],
            ["Why now?", "The news hook or decision that makes it current"],
            ["Who does it affect, and how many?", "Numbers with source and date"],
            ["What does the evidence say?", "The main findings, with their limits"],
            ["What are the arguments?", "Each side stated fairly"],
            ["What happens next, and what can I do?", "Dates, entitlements, where to apply"],
        ]),
        body("Explainers work well as short videos, audio for community radio, illustrated WhatsApp "
             "cards and web pages. The same question list serves all of them.", sm=True),
    ], compact=True),

    C("Data stories", "Writing a data story without misleading", [
        body("A data story builds an argument around numbers. Development organisations make the "
             "same mistakes repeatedly: they report a percentage without its base, mix up "
             "percentages and percentage points, or present a provisional figure as final. Take "
             "women's internet use from NFHS-6 as a worked case."),
        tw(pp("red", "Weak", "'Internet use among women has risen by 93%.' Technically derivable "
              "(33.3 to 64.3 is a 93% relative rise) but it hides the level, and readers will "
              "think 93% of women are online."),
           pp("green", "Better", "'Almost two in three women aged 15-49 have used the internet, up "
              "from one in three in 2019-21: a rise of 31 percentage points (NFHS-6, 2023-24, "
              "provisional). The gap with men remains: 80.5% of men have done so.'")),
        bullets(["State the level, the change and the comparison group",
                 "Say 'percentage points' for differences between percentages",
                 "Give the survey round, the years and whether figures are provisional",
                 "Show the rural-urban split when it changes the story (58.6% rural, 77.3% urban)"],
                sm=True),
        body("Source for all figures: " + NFHS6 + ".", sm=True),
    ], compact=True),

    C("Plain language", "Plain language rules for development writing", [
        body("Development writing is full of words that mean something to insiders and nothing to "
             "anyone else. Journalists will not translate them for you; they will skip the "
             "release. Plain language is also a matter of respect for the people your programme "
             "serves, who should be able to read what is written about them."),
        table(["Instead of", "Write", "Why"], [
            ["Beneficiaries", "Women farmers, students, families", "Name the people"],
            ["Capacity building", "Training, mentoring, equipment", "Say what was done"],
            ["Convergence with line departments", "Working with the health and education departments", "Name the bodies"],
            ["Significant improvement", "Attendance rose from 62% to 78%", "Give the numbers"],
            ["Vulnerable populations", "Landless households, people living alone over 60", "Be specific"],
            ["Rs 2,50,00,000", "Rs 2.5 crore", "Use the unit readers use"],
        ]),
        hbox("Indian readers use lakh and crore. International readers do not. When writing for "
             "both, give the Indian unit and the equivalent in millions in brackets once.", "cyan"),
    ], compact=True),
]

# ===================== SECTION 09: WORKING WITH JOURNALISTS =====================
S09 = [
    D("09", "Section Nine", "Working with journalists and platforms"),

    C("How newsrooms work", "Understand the newsroom before you pitch to it", [
        body("A news story passes through several people. Reporters cover beats such as health, "
             "education or the state legislature; desks and editors decide what runs and where; "
             "district stringers, often paid per story, feed regional editions. Deadlines are "
             "tight, staff are stretched, and a reporter may be covering three stories on the "
             "day your study is released."),
        tw([panel("cyan", "What reporters need from you", [bullets([
                "A clear news angle in the first sentence",
                "Data they can check, with the source",
                "A spokesperson available on the day, in the right language",
                "People affected who have agreed to speak",
                "Photographs with consent and credits"], sm=True)])],
           [panel("amber", "What they do not want", [bullets([
                "Long PDFs with the news on page 40",
                "Requests to see or approve the story before publication",
                "Pressure through their editors or owners",
                "Calls at deadline asking whether they got the release"], sm=True)])]),
        hbox("Build relationships with beat reporters before you need them: send them useful data, "
             "answer their questions on other stories, and never mislead them.", "green"),
    ]),

    C("What is news", "What makes something news", [
        body("Editors choose stories using a set of news values. A study is not news because it was "
             "completed. It becomes news when it tells readers something new, about something "
             "that matters to them, at a moment when they are paying attention."),
        table(["News value", "Question an editor asks", "How a study can meet it"], [
            ["Novelty", "Is this new?", "A first-time figure, a reversal of a trend"],
            ["Impact", "How many people does it affect, and how much?", "Scale with numbers and places"],
            ["Proximity", "Is it about our readers' area?", "District and state breakdowns"],
            ["Timeliness", "Why today?", "Link to a budget, a session, an anniversary"],
            ["Conflict", "Is there a dispute?", "Findings that contradict official claims"],
            ["Human interest", "Is there a person in it?", "A consenting individual whose case illustrates the data"],
        ]),
        body("A regional editor will ask whether your study has district figures for the "
             "paper's circulation area. If it does, lead your pitch to that paper with them.", sm=True),
    ], compact=True),

    C("Embargoes", "How embargoes work, and when to use one", [
        body("An embargo is an agreement that a journalist receives material in advance and does "
             "not publish before a stated date and time. It gives reporters time to read a study, "
             "check it and interview people, which produces better coverage. It depends entirely on "
             "trust: there is no legal force behind a press embargo."),
        tw(pp("green", "Use one when", "The study is complex, you are releasing to several outlets "
              "at once, you want time for reporters to seek reactions from officials, or a joint "
              "launch with partners needs a fixed moment."),
           pp("amber", "Handle with care", "State the embargo in the subject line and at the top of "
              "each document, with time zone (for example 00:01 IST, 14 March). Send only to "
              "journalists you trust. Assume it may break, and prepare.")),
        flow(["Send embargoed material 2-5 days ahead",
              "Offer briefings and interviews before the embargo",
              "Publish the report on your website at embargo time",
              "Send the public release to everyone else"]),
    ], compact=True),

    C("Interviews", "Giving interviews: on the record and off it", [
        body("Interview terms should be agreed before the conversation starts, never after. "
             "Different outlets and journalists use the terms in slightly different ways, so state "
             "what you mean. If you are not sure, assume everything you say is on the record."),
        table(["Term", "Usual meaning", "Use it for"], [
            ["On the record", "Quotable with your name and role", "Almost everything an organisation says"],
            ["On background", "Usable, attributed to a description such as 'a researcher involved in the study'",
             "Context you cannot say officially"],
            ["Off the record", "Not to be published or attributed", "Rarely; it binds only if agreed beforehand"],
        ]),
        tw(pp("cyan", "Prepare", "Three messages you want to land, each with a fact. Likely hard "
              "questions and honest answers. The numbers, with sources, on one card."),
           pp("amber", "In the interview", "Answer the question asked, briefly. Say 'I don't know, "
              "I'll check' when you don't. Avoid speculating about individuals or ongoing "
              "court cases.")),
    ], compact=True),

    C("Corrections", "When a story gets it wrong", [
        body("Errors happen. A reporter misreads a table, a headline turns 'in surveyed blocks' "
             "into 'in Bihar', or a quote is attached to the wrong person. How you respond affects "
             "both the correction and your future relationship with the outlet. The Press "
             "Council's 2022 norms say a newspaper should, on its own motion, publish a correction "
             "promptly and with due prominence once an error is detected or confirmed."),
        flow(["Check: is it a factual error or a framing you dislike?",
              "Contact the reporter politely with the exact correction and evidence",
              "If unresolved, write to the editor or readers' editor",
              "For print, complain to the Press Council of India (Press Council Act 1978, s14)"]),
        tw(pp("green", "Your own errors", "Correct them faster than you would expect of others: "
              "fix the web page, add a dated note saying what changed, and tell journalists who "
              "used the wrong figure."),
           pp("red", "Do not", "Threaten legal action over an honest mistake, demand the story be "
              "taken down, or attack the reporter on social media.")),
        body("Source: Press Council of India, Norms of Journalistic Conduct 2022, Norm 9.", sm=True),
    ], compact=True),

    C("Organisational social media", "Running your organisation's social media accounts", [
        body("Social media lets an organisation publish directly, answer questions and respond "
             "to criticism. It also creates risks: a post that names a survivor, a staff member's "
             "personal comment read as the organisation's view, a hacked account. Treat the "
             "accounts as publishing channels with an editor, a policy and a log."),
        tw([panel("cyan", "Policy basics", [bullets([
                "Who may post, and who approves sensitive posts",
                "Rules on photographs of programme participants (consent on file)",
                "Response times and who answers complaints",
                "How staff identify personal opinions on their own accounts"], sm=True)])],
           [panel("indigo", "Security basics", [bullets([
                "Two-factor authentication on every account",
                "Organisation-owned logins, never one staff member's phone",
                "A plan for a hacked or impersonated account",
                "Archive posts and replies for accountability"], sm=True)])]),
        hbox("Write social media posts in the languages your audiences use. A post in English "
             "about a programme in Odisha will not reach the people it describes.", "green"),
    ]),

    C("Sharing data", "Working with data journalists", [
        body("Data journalism teams at Indian outlets and independent data organisations analyse "
             "official and NGO datasets. Giving them well-documented data can produce more "
             "accurate and more lasting coverage than a press release. It also exposes your "
             "methods to scrutiny, which is a good thing if the work is sound."),
        table(["Share", "Why"], [
            ["A clean dataset with a codebook", "So variables are not misread"],
            ["Sample design, weights and dates", "So estimates are calculated correctly"],
            ["Known limitations", "So the story does not overclaim"],
            ["A contact who can answer technical questions", "So errors are caught before publication"],
            ["The terms of use and licence", "So reuse is clear"],
        ]),
        hbox("Never share individual-level data that could identify a respondent. Aggregate, "
             "remove direct identifiers and check that small cells cannot reveal a person or a "
             "household. See the Research Ethics and Data Protection decks.", "red"),
    ], compact=True),
]

# ===================== SECTION 10: IMAGES, CONSENT, CRISIS, ACCESS =====================
S10 = [
    D("10", "Section Ten", "Images, consent, crises and access"),

    C("Image ethics", "The pictures development organisations take", [
        body("Development communication has a long habit of showing poor people as helpless: "
             "the malnourished child, the woman in the doorway, the queue for relief. These "
             "images raise money and attention, and they strip the people in them of agency and "
             "context. Codes written by NGO networks try to change the habit. The Dóchas Guide to "
             "Ethical Communications (2023), from the Irish network of development NGOs, updates "
             "its 2006 Code of Conduct on Images and Messages and the 2014 illustrated guide to it."),
        table(["Dóchas commitment (2023)", "What it asks of an organisation"], [
            ["Authentic representation", "Show people as they are, in context, with their own capabilities"],
            ["Contributor-led stories, locally led content", "Let people shape how their story is told"],
            ["Informed consent", "Explain use, reach and risk; respect refusal and withdrawal"],
            ["Upholding standards and doing no harm", "Assess and avoid risk to contributors"],
        ]),
        body("Source: Dóchas Guide to Ethical Communications, 2023, as listed by developmenteducation.ie. "
             "The commitments apply equally to photographs, video, case studies and quotations.", sm=True),
    ], compact=True),

    C("Informed consent", "Consent for images and stories is a process", [
        body("Consent obtained by a field officer who asks 'photo le sakte hain?' while handing out "
             "a kit is not informed consent. People must understand who will see the image, where, "
             "for how long and with what risk, and must be able to refuse without losing any "
             "service. Power matters: a person who depends on your programme may find it hard to "
             "say no."),
        flow(["EXPLAIN: purpose, outlets, reach (online is permanent and global)",
              "ASK: in the person's language, separately from any service",
              "RECORD: written or audio consent, with the specific uses",
              "RESPECT: refusal, and withdrawal later, with a named contact"]),
        tw(pp("green", "Good practice", "A consent form in the local language read aloud; a copy "
              "left with the person; a register linking each image to its consent record; a "
              "review before reuse in a new context."),
           pp("amber", "Looking ahead", "Under the DPDP Act, consent duties apply from 13 May 2027. "
              "Building a consent register now means programmes will already meet the "
              "standard when the duties begin.")),
    ]),

    C("Children", "Children in images and stories: law and guidance", [
        body("Indian law sets hard limits on identifying children in certain situations, and the "
             "UNICEF guidelines for journalists set a wider ethical standard. A programme that "
             "photographs children should know both."),
        table(["Rule", "What it says"], [
            ["JJ Act 2015, s74", "No report shall disclose the name, address, school or any particular that may identify a child in conflict with law, a child in need of care and protection, or a child victim or witness, nor publish their picture"],
            ["POCSO Act 2012, s23(2)", "No media report shall disclose a child's identity, including name, address, photograph, family details, school or neighbourhood"],
            ["UNICEF principle", "Protect the best interests of each child over any other consideration, including advocacy for children's issues"],
            ["UNICEF principle", "Do not publish a story or image that might put the child, siblings or peers at risk, even when identities are changed or obscured"],
        ]),
        body("Sources: Juvenile Justice (Care and Protection of Children) Act 2015, s74; POCSO Act 2012, "
             "s23; UNICEF, Guidelines for journalists reporting on children (unicef.org). Both "
             "statutes allow disclosure only on recorded reasons by the Board, Committee or Special "
             "Court.", sm=True),
    ], compact=True),

    C("Survivors", "Survivors of sexual violence: never identify", [
        body("Section 72(1) of the Bharatiya Nyaya Sanhita 2023 punishes whoever prints or publishes "
             "the name or any matter which may make known the identity of a victim of rape and "
             "related offences, with imprisonment of up to two years and fine. The Supreme Court "
             "went further in <em>Nipun Saxena v Union of India</em> (11 December 2018, (2019) 2 "
             "SCC 703)."),
        quote("No person can print or publish in print, electronic, social media, etc. the name of "
              "the victim or even in a remote manner disclose any facts which can lead to the victim "
              "being identified and which should make her identity known to the public at large.",
              "Nipun Saxena v Union of India, 11 December 2018, direction 1 of the operative "
              "directions (Deepak Gupta J, for Lokur and Gupta JJ)"),
        tw(pp("red", "Remote identification", "A blurred face with a named village, a husband's "
              "name, a school uniform or a distinctive house can identify a survivor. The test is "
              "whether anyone could work out who she is."),
           pp("indigo", "Also binding", "PCI Norm 42 (2022): names, photographs or other "
              "particulars leading directly or indirectly to the identity of such victims shall "
              "not be published.")),
    ], compact=True),

    C("Dignity checklist", "A dignity check before any image is published", [
        body("Codes and laws set minimum standards. A short check before publication catches most "
             "problems. Run it on every photograph, video and case study, including those in "
             "donor reports, which are often shared far more widely than intended."),
        tw([panel("green", "Ask yes to all", [bullets([
                "Would the person be comfortable seeing this image with this caption?",
                "Is the caption accurate about who, where and when?",
                "Is there a consent record for this specific use?",
                "Does the image show the person acting, speaking or working, where possible?",
                "Is the photographer credited?"], sm=True)])],
           [panel("red", "Stop if any is yes", [bullets([
                "Could the person or family be identified as a survivor, patient or child in a protected situation?",
                "Is the person shown in distress, undress or grief they did not choose to share?",
                "Does the image imply a person is a 'beneficiary' of something they did not receive?",
                "Is it a stock or another organisation's image used as if it were your programme?"],
                sm=True)])]),
        hbox("When in doubt, do not publish, or use an illustration. A drawing can tell a "
             "survivor's story without putting her at risk.", "indigo"),
    ]),

    C("Crisis principles", "Crisis communication: six principles", [
        body("A crisis for a development organisation might be a death in a programme, an outbreak "
             "at a facility you support, allegations of abuse by staff, a data breach or a flood "
             "in your field area. The US Centers for Disease Control and Prevention's Crisis and "
             "Emergency Risk Communication (CERC) manual, first published in 2002 and updated in "
             "2018, gives six principles that public health agencies worldwide use."),
        table(["CERC principle", "In practice for an NGO"], [
            ["Be first", "Communicate early, even if only to say what you know and when you will update"],
            ["Be right", "Give accurate information, and say clearly what is not yet known"],
            ["Be credible", "Be honest; do not minimise, speculate or hide bad news"],
            ["Express empathy", "Acknowledge harm and fear before giving facts"],
            ["Promote action", "Tell people what they can do to protect themselves"],
            ["Show respect", "Treat affected people and communities with dignity"],
        ]),
        body("Source: CDC, CERC Introduction, 2018 Update (stacks.cdc.gov).", sm=True),
    ], compact=True),

    C("Crisis playbook", "The first 24 hours of a crisis", [
        body("Most crisis damage comes from silence, contradictory statements or a defensive tone "
             "in the first day. A short playbook, agreed in advance, prevents that. The example "
             "steps below assume an incident at a field site; adapt them to your organisation."),
        flow(["0-2 HOURS: ensure safety and care for those affected; inform leadership",
              "2-6 HOURS: confirm facts; name one spokesperson; issue a holding statement",
              "6-24 HOURS: inform families, partners, funders and authorities as required",
              "DAY 2 ONWARDS: regular updates; investigation; publish what changes"]),
        tw(pp("cyan", "A holding statement says", "What happened as far as known, that the people "
              "affected are the priority, what the organisation is doing, and when the next update "
              "will come. It is short and signed by a named person."),
           pp("red", "It never", "Blames the people affected, names a survivor or a child, "
              "speculates on cause, or says 'no comment'. Legal advice shapes the wording; it "
              "should not replace communication.")),
        hbox("Safeguarding incidents need a survivor-centred process first. See the Safeguarding "
             "&amp; PSEA deck before writing any public statement about one.", "amber"),
    ], compact=True),

    C("Accessibility and language", "Accessible communication is a legal duty and good practice", [
        body("Section 42 of the Rights of Persons with Disabilities Act 2016 requires the appropriate "
             "government to take measures so that all content in audio, print and electronic media is "
             "in accessible format, and that persons with disabilities have access to electronic "
             "media through audio description, sign language interpretation and close captioning. "
             "Organisations that communicate with the public should meet the same standard."),
        tw([panel("cyan", "Accessible formats", [bullets([
                "Captions on every video; transcripts for audio",
                "Indian Sign Language interpretation for key announcements",
                "Alt text on images; tagged, readable PDFs",
                "Sufficient colour contrast; text that is not locked in images",
                "Easy-read versions for people with intellectual disabilities"], sm=True)])],
           [panel("green", "Language access", [bullets([
                "Publish in every language your audience speaks, beyond English and Hindi",
                "Use audio for audiences with low literacy",
                "Test translations with native speakers from the community",
                "Keep numbers and names consistent across versions"], sm=True)])]),
        body("Sources: RPwD Act 2016, s42; Census 2011 language data (Section 02).", sm=True),
    ]),
]

# ===================== SECTION 11: PRACTICE =====================
S11 = [
    D("11", "Section Eleven", "Measuring and planning: a practitioner toolkit"),

    C("Measuring", "Measure what communication changed as well as what it produced", [
        body("Most communication reports count outputs: releases sent, articles published, "
             "followers gained. Those numbers say little about whether anything changed. AMEC's "
             "Integrated Evaluation Framework moves from objectives through inputs, activities, "
             "outputs, outtakes and outcomes to impact on organisational objectives. It defines "
             "outtakes as the response and reactions of target audiences to the activity, and "
             "outcomes as the effect of the communication on the target audience."),
        flow(["OBJECTIVES", "INPUTS and ACTIVITIES", "OUTPUTS: what was published and where",
              "OUTTAKES: audience response", "OUTCOMES: change in the audience", "IMPACT: on the organisation's objectives"]),
        tw(pp("indigo", "Barcelona Principles", "AMEC published Barcelona Principles 3.0 in July "
              "2020 and a fourth iteration, 4.0, in 2025. Its resource centre also runs a 'Say No "
              "to AVEs' campaign against advertising value equivalents, which price coverage as if it "
              "were advertising."),
           pp("cyan", "For development work", "The impact stage is the decision, practice or "
              "service change your programme exists for. Link communication indicators to the "
              "programme's results framework.")),
        body("Source: AMEC, Integrated Evaluation Framework and Barcelona Principles pages "
             "(amecorg.com), consulted October 2026.", sm=True),
    ], compact=True),

    C("Indicators", "Indicators at each stage, for a research launch", [
        body("The table gives example indicators for a study launch aimed at a state policy "
             "decision. Choose a few at each stage, set them before the launch, and collect the "
             "evidence as you go. Media monitoring alone covers only the outputs row."),
        table(["Stage", "Example indicator", "How to collect"], [
            ["Outputs", "Articles in target outlets, by language; broadcast mentions", "Media monitoring log"],
            ["Outputs", "Accuracy of coverage: share of items stating the finding correctly", "Content check against the study"],
            ["Outtakes", "Downloads of the brief; questions from officials; requests for briefings", "Web analytics; correspondence log"],
            ["Outcomes", "Officials who can state the main finding; mentions in assembly questions or notes", "Short interviews; legislative records"],
            ["Impact", "Change in the scheme guideline, budget or practice the study addressed", "Document review; contribution analysis"],
        ]),
        hbox("Accuracy is an indicator worth tracking. Ten articles that misstate your finding "
             "are worse than two that get it right.", "amber"),
    ], compact=True),

    C("Template", "A one-page communication plan template", [
        body("A communication plan does not need to be long. One page that answers the questions "
             "below, agreed by programme, research and leadership staff, prevents most launch "
             "failures. Fill it in at the start of a study, months before release."),
        table(["Heading", "Question to answer", "Example entry"], [
            ["Objective", "What decision or behaviour should change?", "State revises toilet maintenance norms for girls' schools"],
            ["Audiences", "Who decides, who influences, who is affected?", "Education secretary; MLAs; district officers; parents"],
            ["Messages", "What one sentence should each audience remember?", "Broken toilets keep girls out of school"],
            ["Messengers", "Who is credible to each audience?", "Head teachers; a girl who consents; the lead researcher"],
            ["Channels", "Where does each audience get information?", "Hindi dailies; briefing meeting; community radio"],
            ["Timing", "When is the decision taken?", "Before the supplementary budget"],
            ["Risks", "What could go wrong, and for whom?", "Identification of a girl; school named and shamed"],
            ["Measures", "How will we know it worked?", "Guideline revised; coverage accuracy"],
        ]),
    ], compact=True),

    C("Risk table", "A media-risk decision table", [
        body("Before publishing anything sensitive, run it through this table. It turns the legal "
             "and ethical sections of this deck into decisions. Where the answer points to "
             "'stop', do not publish until the problem is fixed or a lawyer has advised."),
        table(["If the content...", "Risk", "Decision"], [
            ["Names a person, company or official in connection with wrongdoing", "Defamation (BNS s356)",
             "Publish only with evidence, a request for response, and their reply included"],
            ["Could identify a survivor of sexual violence", "BNS s72; Nipun Saxena", "Stop. Remove all identifying detail"],
            ["Shows or describes a child in a protected situation", "JJ Act s74; POCSO s23", "Stop. Remove identity, or do not publish"],
            ["Uses a photograph you did not take or commission", "Copyright Act 1957", "Use only with a licence or within fair dealing"],
            ["Shows identifiable adults", "Consent; DPDP duties from 13 May 2027", "Publish only with recorded consent for this use"],
            ["Comments on a case before a court", "Contempt of Courts Act 1971", "Report facts of proceedings; avoid prejudging"],
            ["Concerns voting or a candidate close to a poll", "RP Act ss 126, 126A", "Pause or seek advice"],
        ]),
    ], compact=True),

    C("Worked example: setup", "Illustrative worked example: launching a district study", [
        body("This example is <strong>Illustrative</strong>: the organisation, study and numbers are "
             "invented to show how the tools fit together. A Lucknow-based research NGO has "
             "completed a household survey on the use of a state maternity cash scheme in two "
             "districts of Uttar Pradesh. The study finds that many eligible women did not "
             "receive the second instalment, mostly because of bank account errors."),
        tw(pp("cyan", "Objective", "The state's women and child development department changes the "
              "payment verification step before the next financial year."),
           pp("indigo", "Audiences", "Principal secretary and scheme director (decide); district "
              "officers and MLAs from the two districts (influence); anganwadi workers and "
              "women in the districts (affected).")),
        tw(pp("green", "Core message", "One in three eligible mothers in the surveyed villages "
              "missed the second instalment because of fixable bank errors (Illustrative)."),
           pp("amber", "Known risks", "Survey households could be identified from village case "
              "studies; officials may read the study as an attack; a provisional figure could be "
              "misreported as state-wide.")),
    ]),

    C("Worked example: plan", "Illustrative worked example: sequence and channels", [
        body("The NGO sequences the launch so that the people who must act hear the findings "
             "first and are not surprised by press coverage. That respects the department and "
             "makes a constructive response more likely. All dates and numbers are Illustrative."),
        flow(["WEEK -3: private briefing for the scheme director, with the data",
              "WEEK -1: embargoed release to Hindi and English reporters on the beat",
              "LAUNCH DAY: full report, brief and data online; Hindi release; radio interview",
              "WEEK +1: district meetings with anganwadi workers and community radio phone-in",
              "WEEK +4: op-ed timed to budget discussions"]),
        table(["Audience", "Channel", "Product", "Language"], [
            ["Department", "Meeting", "Four-page brief with district tables", "Hindi and English"],
            ["Reporters", "Embargoed email, briefing call", "Release, fact sheet, data file", "Hindi and English"],
            ["Women in the districts", "Community radio, anganwadi meetings", "Audio explainer on how to fix account errors", "Awadhi and Hindi"],
        ]),
    ], compact=True),

    C("Worked example: results", "Illustrative worked example: risks handled and what was measured", [
        body("Three problems arise, all Illustrative, and each maps onto a slide earlier in this deck. "
             "The way they are handled matters as much as the coverage."),
        table(["What happened", "Response", "Deck section"], [
            ["A daily headlined the finding as 'one in three UP mothers'", "Polite correction request with the sampling note; the web version was fixed", "09: corrections"],
            ["A reporter asked to photograph a woman from a case study", "Declined; offered a consenting anganwadi worker instead", "10: consent"],
            ["A district officer said the data were wrong", "Shared the method and data; offered a joint field check", "08: data stories"],
        ]),
        tw(pp("cyan", "Outputs and outtakes", "Coverage in six Hindi and two English outlets, five of "
              "them stating the finding accurately; 40 brief downloads from government addresses; "
              "two requests for district tables (Illustrative)."),
           pp("green", "Outcome and impact", "The department issued a circular adding a bank account "
              "check at the first instalment. The NGO records this as a contribution, alongside "
              "other pressures, without claiming sole credit (Illustrative).")),
    ], compact=True),

    C("Checklist", "A pre-publication checklist for any public material", [
        body("Use this list before a release, op-ed, report, social media post or video goes out. "
             "It takes ten minutes and catches the errors that cause most corrections, complaints "
             "and harm."),
        tw([panel("cyan", "Accuracy", [bullets([
                "Every number has a source, a year and a base",
                "Findings are stated at the level the sample supports",
                "Provisional figures are labelled",
                "Quotes are checked with the speaker",
                "Anyone criticised has been asked to respond"], sm=True)])],
           [panel("red", "Safety and law", [bullets([
                "No survivor or protected child can be identified, even remotely",
                "Consent is recorded for every identifiable person",
                "Images are owned, licensed or fair dealing",
                "Wording on named people meets the defamation exceptions",
                "Election-period and court-case rules checked"], sm=True)])]),
        tw(pp("green", "Reach", "Versions exist in the languages your audiences use; video is "
              "captioned; documents are accessible."),
           pp("indigo", "Accountability", "A named contact; a correction policy; the full study and "
              "data linked from every shorter product.")),
    ]),
]

# ===================== SECTION 12: SUMMING UP =====================
S12 = [
    D("12", "Section Twelve", "Summing up and where next"),

    C("Key ideas", "Ten ideas to take away", [
        body("The deck has covered a wide field. These ten points are the ones most likely to "
             "change how a practitioner works on Monday morning."),
        table(["#", "Idea"], [
            ["1", "Start from the decision or behaviour you want to change, then choose audiences and channels"],
            ["2", "India's media are many language markets, regionally concentrated and dependent on advertising"],
            ["3", "Akashvani, DD FreeDish and community radio reach people the internet still misses"],
            ["4", "Messaging apps need forwardable, local, trusted corrections; prejudice drives much misinformation"],
            ["5", "Press freedom rests on Article 19(1)(a), limited only on the eight grounds in Article 19(2)"],
            ["6", "Defamation is still a crime (BNS s356); truth for the public good and fair comment are your defences"],
            ["7", "Never identify a survivor or a child in a protected situation, even remotely"],
            ["8", "Write for each reader: a brief, a release, an explainer, a community version"],
            ["9", "Treat journalists as professionals: news values, embargoes, clear terms, fast corrections"],
            ["10", "Measure outcomes and accuracy as well as outputs, and report what changed"],
        ]),
    ], compact=True),

    C("Where next", "Where next: related 101 decks", [
        tw([panel("cyan", "Communication and evidence", [body(
                "<a href=\"/101-courses/bcc-comms.html\">Behaviour Change Communication 101</a> for "
                "campaigns aimed at practice change. "
                "<a href=\"/101-courses/advocacy-basics.html\">Advocacy Basics 101</a> for media "
                "advocacy within a wider campaign. "
                "<a href=\"/101-courses/data-viz.html\">Data Visualization 101</a> for charts that "
                "survive a newspaper page. "
                "<a href=\"/101-courses/post-truth-101.html\">Post-Truth Politics 101</a> for "
                "misinformation and its politics. "
                "<a href=\"/101-courses/academic-writing.html\">Academic Writing &amp; Publishing "
                "101</a> for the long-form version of your findings.", sm=True)])],
           [panel("green", "Law, ethics and participation", [body(
                "<a href=\"/101-courses/ind-constitution.html\">Indian Constitution 101</a> for "
                "Article 19 in context. "
                "<a href=\"/101-courses/digital-rights-ai.html\">Digital Rights &amp; AI 101</a> for "
                "platforms, takedowns and shutdowns. "
                "<a href=\"/101-courses/data-protection-dpdp.html\">Data Protection &amp; the DPDP Act "
                "101</a> for consent and personal data. "
                "<a href=\"/101-courses/safeguarding-psea.html\">Safeguarding &amp; PSEA 101</a> "
                "before you tell any survivor's story. "
                "<a href=\"/101-courses/participatory-methods.html\">Participatory Methods 101</a> "
                "and <a href=\"/101-courses/visual-eth.html\">Visual Ethnography 101</a> for "
                "community-led media.", sm=True)])]),
        hbox("Suggested order: Advocacy Basics, then Data Visualization, then Safeguarding &amp; "
             "PSEA. Read Data Protection &amp; the DPDP Act before the duties begin on 13 May "
             "2027.", "indigo"),
    ], compact=True),
]

TITLE = {"type": "title",
         "main": "Media &amp;<br>Communications<br>101",
         "sub": "How media works in South Asia and how to communicate research and programmes "
                "through it: ownership, radio and platforms, press freedom and the law, writing, "
                "journalists, images and consent, crises and measurement",
         "tags": ["100 Slides", "South Asia Focus", "Free Forever", "Media and the Law"]}

TOC = {"type": "toc", "label": "Agenda", "title": "What we cover",
       "items": [
           {"name": "Why media matters for development work"},
           {"name": "How the media market works in South Asia"},
           {"name": "Broadcast, radio and community media"},
           {"name": "Platforms, messaging apps and misinformation"},
           {"name": "Press freedom and the Constitution"},
           {"name": "The legal frame for communicators"},
           {"name": "Communication for development: theory and critique"},
           {"name": "Writing for different audiences"},
           {"name": "Working with journalists and platforms"},
           {"name": "Images, consent, crises and access"},
           {"name": "Measuring and planning: a practitioner toolkit"},
           {"name": "Summing up and where next"},
       ]}

END = {"type": "end",
       "eyebrow": "Media &amp; Communications 101",
       "headline": "Know the decision, know the audience, check the law, tell it straight",
       "byline": "ImpactMojo 101 Series &middot; Free foundational learning for development practitioners "
                 "in South Asia",
       "ctas": [{"label": "Advocacy Basics 101", "href": "/101-courses/advocacy-basics.html"},
                {"label": "All 101 courses", "href": "/101-courses/"}],
       "meta": ["100 slides", "12 sections", "CC BY-NC-ND"]}

DECK = {
    "slug": "media-comms",
    "title": "Media & Communications 101",
    "description": ("Media & Communications 101: a free foundational course for development "
                    "practitioners in South Asia who communicate research and programmes. Media "
                    "ownership and markets, Akashvani and community radio, platforms, WhatsApp and "
                    "misinformation, RSF press freedom rankings, Article 19, Romesh Thappar, Shreya "
                    "Singhal and Anuradha Bhasin, defamation under BNS s356, the IT Rules and the "
                    "fact check unit case, Press Council norms, copyright, DPDP, election rules, "
                    "C4D theory and Freire, writing releases, op-eds and data stories, working with "
                    "journalists, image ethics and consent, crisis communication, accessibility and "
                    "measurement. ImpactMojo, CC BY-NC-ND."),
    "slides": ([TITLE, TOC] + S01 + S02 + S03 + S04 + S05 + S06 + S07 + S08 + S09 + S10 + S11 + S12
               + [END]),
}
