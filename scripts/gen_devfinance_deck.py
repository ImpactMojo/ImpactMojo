#!/usr/bin/env python3
"""Development Finance 101 - the money that arrives from outside the budget.

The platform already teaches how the Indian state raises and spends its own
money (Political Economy 101, Public Finance & Budgeting 101, the Budget and
Fiscal Analysis Studio). This deck covers what none of those reach: multilateral
and bilateral lenders, project and infrastructure finance, the shift from
lending to de-risking private capital, climate finance accounting, and the
complaint mechanisms an affected community can actually use.

India-first where the law is Indian: NaBFID, the National Monetisation
Pipeline, RFCTLARR 2013 and the EIA Notification 2006 get their own module
before the global architecture is generalised.

Every figure carries its source and year on the slide. Institutional facts and
statutory thresholds change; section 11 tells the learner to check the primary
source rather than trust a deck.
"""
import deck_builder as db

slides = []
content = lambda inner: slides.append(('content', inner))
divider = lambda n, l, t: slides.append(('divider', (n, l, t)))

# Closing paragraphs for slides that were thin on the first pass. Keyed by
# slide title so the addition sits beside the content it extends rather than
# being threaded back through a long expression.
EXTRA = {}

def sec(label, title, body):
    if title in EXTRA:
        body = body + '<p class="slide-para">%s</p>' % EXTRA[title]
    content('<div class="section-label">%s</div><div class="slide-title md">%s</div>%s' % (label, title, body))

def hbox(text, tone='amber'):
    return '<div class="hbox %s"><div class="hbox-text">%s</div></div>' % (tone, text)

def table(headers, rows):
    h = ''.join('<th>%s</th>' % x for x in headers)
    b = ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % c for c in r) for r in rows)
    return '<table class="ctable"><thead><tr>%s</tr></thead><tbody>%s</tbody></table>' % (h, b)

def bullets(items):
    return '<ul class="bullet-list">%s</ul>' % ''.join('<li>%s</li>' % i for i in items)

def stats(cards):
    c = ''.join('<div class="stat-card"><div class="stat-number">%s</div>'
                '<div class="stat-label">%s</div></div>' % (n, l) for n, l in cards)
    return '<div class="stat-grid">%s</div>' % c

def terms(pairs):
    return ''.join('<div class="term-box"><span class="term-word">%s</span>'
                   '<span class="term-def">%s</span></div>' % (w, d) for w, d in pairs)

def quote(text, attr):
    return ('<div class="quote-block"><div class="quote-text">%s</div>'
            '<div class="quote-attr">%s</div></div>' % (text, attr))

def flow(steps):
    out = []
    for i, s in enumerate(steps):
        if i: out.append('<div class="flow-arrow">&rarr;</div>')
        out.append('<div class="flow-step"><div class="flow-num">%02d</div>'
                   '<div class="flow-label">%s</div></div>' % (i + 1, s))
    return '<div class="flow">%s</div>' % ''.join(out)

def twocol(a_title, a_body, b_title, b_body):
    return ('<div class="two-col"><div class="col-panel"><div class="col-panel-title">%s</div>%s</div>'
            '<div class="col-panel"><div class="col-panel-title">%s</div>%s</div></div>'
            % (a_title, a_body, b_title, b_body))

def p(text):
    return '<p class="slide-para">%s</p>' % text

SRC = '<div class="chart-source">%s</div>'

EXTRA.update({
 "The map of mechanisms":
   "A complication worth anticipating: a large project often has several financiers, and they need not share a standard. A transmission line might take senior debt from one development bank, a partial risk guarantee from another, equity from a bilateral fund and commercial debt from domestic banks. Each financier owes its own policies, each mechanism has its own jurisdiction, and a harm caused by the project as a whole may not map neatly onto any one of them. Establish early which institution financed the component that produced the harm, because that is the first question the mechanism will ask.",
 "Results-based and policy-based lending":
   "Policy-based lending deserves particular care because its disbursement trigger is a policy action rather than a physical output. That makes verification political rather than technical: whether a tariff order was issued, whether a law was notified, whether an agency was established. Each can be satisfied formally while leaving the intended substance untouched, and the incentive to satisfy it formally is created by the disbursement itself. Read the condition to see whether it specifies an outcome or merely an instrument, because the two behave very differently once money depends on them.",
 "Reading a case file":
   "Read at least one case that the mechanism declined to register, alongside the ones it investigated. The eligibility decisions are where the boundaries of the system are actually drawn, and they are more informative than the substantive findings about what the mechanism will and will not treat as its business. A refusal on time limits, or on the ground that the harm was not connected to a policy the institution owed, tells you more about how to draft a future complaint than a successful investigation does.",
 "Where Indian project information lives":
   "Two of these sources are systematically underused. Parliamentary and assembly answers are given under an obligation of accuracy and are often the only place a specific figure appears in public, and they are searchable by subject. CAG reports are slow, arriving years after the events they examine, but they are produced by an authority with statutory access to records that no outside researcher can obtain, and their findings carry weight in forums where an advocacy report would not. Both reward the patience of searching them properly.",
 "A checklist for any climate finance claim":
   "Apply the checklist to a friendly source as well as a hostile one. The discipline is worth little if it is used only to attack figures you already doubt, and a claim from an organisation whose conclusions you share is exactly the one you are least likely to interrogate. If your own side's number fails the same four questions, you need to know that before an opponent tells you, because the cost of discovering it in public is much higher than the cost of checking.",
 "Adequacy and direction are different questions":
   "There is a third question the two above tend to crowd out: predictability. A commitment that arrives in unpredictable amounts at unpredictable times cannot be planned against, and a ministry cannot build a multi-year adaptation programme on a flow it cannot forecast. Predictability rarely features in headline reporting because it is harder to express as a single figure, but for the officials who have to spend the money it frequently matters more than the total does.",
 "Who publishes what":
   "Read these in a deliberate order. Start with the treaty body's assessment, because it sets out the definitional problems most candidly and will make the other sources legible. Then take the OECD series for the official totals and their disaggregation. Then the shadow report, which recalculates the same underlying data and shows you where the two methods part company. Reading them in the reverse order tends to leave a reader with a conclusion and no sense of how it was reached.",
 "Grace periods and why they flatter":
   "The same logic applies to concession length. A thirty-year concession signed today allocates revenue for a period longer than most of the officials signing it will remain in post, and longer than any demand forecast can responsibly project. Long tenors are frequently necessary, because the asset lasts that long and the capital has to be recovered over its life. The point is that length is not a neutral technical parameter: it determines how far into the future present decisions bind, and who will be around to be answerable for them.",
 "Consent, and what it does and does not mean":
   "Note also what consent attaches to. A consent threshold is generally measured against affected families at a defined point in time, which means the composition of the affected group is itself a contested question, decided by the survey that precedes the vote. Who is counted as affected determines both the denominator and who has a say, and disputes about a project's consent are very often disputes about that survey rather than about the vote it produced.",
 "Five questions before you use any number here":
   "A sixth question, for figures about India specifically: is the number for the Union or for the general government? Union figures exclude state spending, and in sectors where states do most of the spending, a Union figure quoted as a national one can understate the real total severalfold. The same trap appears in reverse with schemes that are centrally sponsored but state-implemented, where the Union release and the actual expenditure are different numbers reported by different bodies.",
})

# ---------------------------------------------------------------- title + toc
slides.append(('title', None))
TOC = [
    ("Why the Shape of the Money Matters", "3&ndash;11"),
    ("The Institutions and Who Decides", "12&ndash;21"),
    ("Instruments: What a Loan Actually Is", "22&ndash;31"),
    ("From Lending to De-risking", "32&ndash;41"),
    ("How a Project Gets Financed", "42&ndash;51"),
    ("India's Own Architecture", "52&ndash;62"),
    ("Land, Environment and Consent", "63&ndash;71"),
    ("Climate Finance and Its Accounting", "72&ndash;82"),
    ("Accountability: Who Can Complain", "83&ndash;90"),
    ("Following the Money in Practice", "91&ndash;96"),
    ("What to Check Before You Cite", "97&ndash;100"),
]
slides.append(('toc', TOC))

# ============================================================ 01
divider(1, "Module One", "Why the Shape of the Money Matters")

sec("Framing", "Two numbers, one disagreement",
    p("Developed countries reported providing <strong>US$115.9 billion</strong> of climate finance in 2022. "
      "Oxfam and CARE, working from the same underlying reporting, put the real value at "
      "<strong>US$28&ndash;35 billion</strong>. Neither figure is a mistake, and neither side is accused of "
      "inventing data. They are answers to two different questions, and the gap between them is almost "
      "entirely a question of instrument.") +
    p("A loan is reported at face value. Ten million dollars lent counts identically to ten million dollars "
      "given, even though one is repaid with interest and one is not. Compute the grant equivalent instead, "
      "netting out repayment and interest, and the headline falls by roughly two thirds.") +
    hbox("This is the argument the whole course is about. Development finance debates that look like "
         "disagreements over facts are usually disagreements over what the facts are counting.") +
    SRC % "Oxfam and CARE, Climate Finance Shadow Report 2025, reporting year 2022.")

sec("Framing", "What this course covers, and what it does not",
    twocol("In scope",
           bullets(["Money that reaches a country from outside its own budget",
                    "Multilateral and bilateral lenders, and how their decisions are made",
                    "Project and infrastructure finance, including PPPs",
                    "The Indian institutional architecture: NaBFID, monetisation, viability gap funding",
                    "Climate finance and the accounting choices inside the headline numbers",
                    "Complaint and accountability mechanisms"]),
           "Covered elsewhere on ImpactMojo",
           bullets(["How the Indian state raises and allocates its own revenue &mdash; <em>Public Finance &amp; Budgeting 101</em>",
                    "Institutions, rents and collective action &mdash; <em>Political Economy 101</em>",
                    "Tracing budget lines Centre to beneficiary &mdash; <em>Budget &amp; Fiscal Analysis Studio</em>",
                    "Corporate money under Section 135 &mdash; <em>CSR &amp; ESG 101</em>",
                    "The evidence base and reading list &mdash; the <em>Political Economy of Development Finance</em> Deep Dive"])) +
    p("The division is deliberate. A practitioner who understands the Union Budget still cannot read a "
      "concession agreement, and the two skills are taught by different literatures."))

sec("Framing", "Who this is for",
    p("Three audiences, with different reasons to be here. People working in organisations affected by a "
      "financed project, who need to know what documents exist and who is obliged to produce them. People "
      "designing or evaluating programmes funded through these channels, who need to read the conditions "
      "attached. And researchers and students who need the institutional vocabulary before the critical "
      "literature makes sense.") +
    twocol("You will be able to",
           bullets(["Name the main lenders and say how each is governed",
                    "Read a loan's concessionality rather than its headline size",
                    "Explain what de-risking means and identify it in a contract",
                    "Trace an Indian infrastructure project to its financing sources",
                    "Locate the statutory documents a project must produce",
                    "File, or advise on filing, a complaint to an accountability mechanism"]),
           "You will not be able to",
           bullets(["Price a bond or model a debt sustainability analysis",
                    "Practise as a project finance lawyer",
                    "Substitute this for the primary documents, which change",
                    "Assume any figure here is current without checking its source year"])))

sec("Concepts", "Four words used loosely, defined precisely",
    terms([("Development finance",
            "Public or publicly-backed money provided on terms more favourable than a commercial lender would offer, or into places a commercial lender would not go. The favourable terms are the definition, not the intention."),
           ("Concessionality",
            "How much better than market terms a loan is, expressed as a grant element. A grant is 100% concessional. A loan at market rate is 0%, however development-minded its purpose."),
           ("Mobilisation",
            "Private capital that a public intervention is claimed to have caused to flow. The contested word is caused: capital that would have come anyway is not mobilised, merely accompanied."),
           ("De-risking",
            "Public absorption of risks a private investor will not carry, so that a project's cash flows become predictable enough to invest in. Guarantees, offtake commitments and revenue floors are the common forms.")]))

sec("Concepts", "Why concessionality is the number that matters",
    p("Two countries each receive a headline US$100 million. One receives a grant. The other receives a "
      "twenty-year loan at a market rate. The press releases look the same; the fiscal consequences do not.") +
    table(["Instrument", "Headline", "Repaid", "Grant element", "What it does to debt"],
          [["Grant", "US$100m", "Nothing", "100%", "None"],
           ["Highly concessional loan", "US$100m", "Principal, long grace, minimal interest", "High", "Adds to stock, light service burden"],
           ["Loan near market terms", "US$100m", "Principal plus commercial interest", "Low or nil", "Adds to stock and to annual service"],
           ["Guarantee", "Nil until called", "Nothing unless triggered", "n/a", "Contingent liability, invisible until it is not"]]) +
    hbox("A guarantee costs nothing until it costs everything. Contingent liabilities are the line item that "
         "does not appear in a headline finance figure and does appear in a fiscal crisis."))

sec("Concepts", "Three questions to ask of any finance announcement",
    flow(["Who bears the risk?", "Who repays, and when?", "What was given up to get it?"]) +
    p("The first question locates the guarantee, the offtake agreement or the revenue floor. The second "
      "separates a grant from a loan and a loan from a contingent liability. The third is the one most "
      "reporting omits: a financing package is negotiated, and the concessions given in exchange &mdash; a "
      "tariff formula, a procurement rule, a regulatory commitment &mdash; are part of its price.") +
    hbox("None of the three can be answered from a press release. All three can usually be answered from "
         "the loan agreement, the concession agreement, or the appraisal document, which are more often "
         "public than practitioners assume.", "teal"))

sec("History", "How the system was built, in one slide",
    table(["Period", "Dominant model", "What it assumed"],
          [["1944&ndash;1960s", "Reconstruction then project lending", "States build infrastructure; capital is the binding constraint"],
           ["1980s", "Structural adjustment", "Policy, not capital, is the binding constraint"],
           ["1990s&ndash;2000s", "Governance and institutions", "Rules and capacity are the binding constraint"],
           ["2015&ndash;present", "Mobilising private capital", "Public money is too small; its job is to make projects investible"]]) +
    p("Each shift redefined what the money was <em>for</em>, and each left institutional residue behind. The "
      "safeguard policies and complaint mechanisms of module nine are residue from the project-lending era. "
      "The conditionality literature is residue from adjustment. Both still operate inside an architecture "
      "now organised around the fourth row."))

sec("History", "Why the last row changed the questions",
    twocol("When a bank lends to a state",
           bullets(["The borrower is a government",
                    "Repayment risk is sovereign",
                    "Accountability runs through the lender's own policies",
                    "The public record is the loan agreement",
                    "The contested question is conditionality"]),
           "When public money de-risks a private project",
           bullets(["The borrower may be a special purpose vehicle",
                    "Risk is allocated by contract, clause by clause",
                    "Accountability depends on which entity is bound",
                    "The public record is fragmented across agreements",
                    "The contested question is who carries the downside"])) +
    p("This is why a course written twenty years ago would be a poor guide today. The critical vocabulary of "
      "conditionality still applies, but it no longer describes where most of the decisions are made."))

sec("Framing", "What to hold on to from module one",
    bullets(["A finance figure is a construct. Ask what it counts before comparing it to anything.",
             "Concessionality, not headline size, determines what a loan does to a country.",
             "A guarantee is real money with an invisible balance sheet entry.",
             "The system's centre of gravity has moved from lending to states towards making projects investible for private capital.",
             "The documents that answer the hard questions usually exist, and are more often public than assumed."]) +
    hbox("Everything after this module is detail on those five points.") +
    p("One caution before going further. None of the five points implies that development finance is a bad thing or that the institutions act in bad faith. The argument of this course is narrower and more useful than that: the form money takes has consequences that its headline size conceals, and those consequences fall on people who were not party to the negotiation. A practitioner who can read the form is in a position to say what those consequences are, specifically, with a document behind the claim. A practitioner who cannot is left arguing about intentions, which is an argument nobody wins."))

# ============================================================ 02
divider(2, "Module Two", "The Institutions and Who Decides")

sec("Institutions", "The main categories, and how they differ",
    table(["Type", "Examples", "Owned by", "Lends to"],
          [["Multilateral development bank", "World Bank (IBRD, IDA), ADB, AIIB, NDB", "Member states, by subscription", "Sovereigns, and via private arms to firms"],
           ["Bilateral agency", "JICA, KfW, AFD, USAID historically", "One state", "Partner governments and projects"],
           ["National development bank", "NaBFID, BNDES, CDB", "Its own state", "Domestic projects and firms"],
           ["Private arm of an MDB", "IFC, MIGA", "Member states", "Private firms, via loans, equity, guarantees"],
           ["Climate fund", "GCF, GEF, Adaptation Fund", "Contributing states, treaty-linked", "Accredited entities, which on-lend"]]) +
    p("The distinction that matters most for accountability is the fourth row. When an MDB lends through its "
      "private arm, the borrower is a company, the safeguard regime is different, and the complaint "
      "mechanism is a different body."))

sec("Institutions", "Voting: why it is not one country one vote",
    p("At the IBRD, voting power is tied to capital subscription. A member's share of the votes reflects its "
      "share of the capital, adjusted by a small allocation of basic votes given equally to all members. The "
      "distribution is published, and the Articles of Agreement set the framework.") +
    twocol("What follows from subscription-weighted voting",
           bullets(["Large shareholders hold structural influence over policy",
                    "Special majorities give some members an effective veto over amendments",
                    "Capital increases are themselves political events, because they reset shares",
                    "Borrowing members' collective weight is smaller than their number"]),
           "What does not follow",
           bullets(["That every decision is dictated by the largest shareholder",
                    "That staff have no independent influence &mdash; Woods argues they do",
                    "That borrower governments are passive; domestic coalitions shape outcomes",
                    "That the Board votes often &mdash; much is settled by consensus before it reaches them"])) +
    SRC % "IBRD Articles of Agreement; World Bank published subscriptions and voting power tables.")

sec("Institutions", "The prohibition that sits awkwardly with everything else",
    quote("The Bank and its officers shall not interfere in the political affairs of any member; nor shall "
          "they be influenced in their decisions by the political character of the member.",
          "IBRD Articles of Agreement, Article IV, Section 10 (paraphrased)") +
    p("Read this beside a safeguard policy requiring free, prior and informed consultation with indigenous "
      "peoples, or a governance loan conditioned on procurement reform, and the tension is immediate. A "
      "great deal of the institutional and legal literature on the MDBs is an attempt to reconcile the "
      "political-prohibition clause with lending practice that is unavoidably political.") +
    hbox("You do not need to resolve the tension. You need to know it exists, because it explains why "
         "safeguards are framed as technical standards rather than as rights."))

sec("Institutions", "IDA and IBRD: the same bank, different terms",
    table(["", "IBRD", "IDA"],
          [["Borrowers", "Middle-income and creditworthy lower-income countries", "The poorest countries, by income and creditworthiness tests"],
           ["Funding", "Bond issuance against callable capital", "Donor replenishments plus reflows and market borrowing"],
           ["Terms", "Near-market, long maturity", "Highly concessional: grants, or credits with long grace periods"],
           ["Implication", "Adds to debt at modest cost", "Adds little or nothing to debt service"]]) +
    p("Graduation from IDA to IBRD is therefore a large event in a country's public finances, and the "
      "eligibility thresholds are a live political question. India's own transition out of IDA eligibility "
      "is a useful worked case for anyone studying how the terms change when a country crosses a line."))

sec("Institutions", "The newer banks, and what they changed",
    twocol("AIIB and the New Development Bank",
           bullets(["Established in the mid-2010s with substantial non-Western shareholding",
                    "Infrastructure-focused mandates",
                    "Framed as faster and less conditional than the incumbents",
                    "Have their own safeguard frameworks and complaint mechanisms"]),
           "What to test rather than assume",
           bullets(["Whether approval is in fact faster, measured against comparable projects",
                    "Whether safeguard standards are weaker in text or only in resourcing",
                    "Whether their existence has changed incumbent behaviour, which is the more interesting question",
                    "Whether their complaint mechanisms have received and acted on cases"])) +
    hbox("The arrival of alternative lenders is often asserted to have created competitive pressure on "
         "standards. That is a testable empirical claim, and it should be tested rather than repeated."))

sec("Evidence", "Conditionality: what the data shows",
    p("The standard institutional account is that the conditionality of the structural adjustment era was "
      "substantially reformed, with fewer conditions and more attention to social protection. Kentikelenis, "
      "Stubbs and King coded the actual conditions attached to IMF programmes across three decades and found "
      "the reform is largely presentational.") +
    bullets(["The count of conditions changed more than their substantive reach",
             "Conditions continued to extend into labour markets, public employment and social policy",
             "Stated attention to social protection appeared more in framing than in binding requirements",
             "The coding scheme is published, which is what makes the finding disputable rather than rhetorical"]) +
    SRC % "Kentikelenis, Stubbs and King, Review of International Political Economy 23(4), 2016.")

sec("Evidence", "Why the coded-conditions method is worth learning",
    twocol("The method",
           bullets(["Obtain the programme documents",
                    "Code every condition by policy area, using a published scheme",
                    "Distinguish binding conditions from stated intentions",
                    "Count and compare across time and country"]),
           "Why it transfers",
           bullets(["The same approach works on MDB loan covenants",
                    "And on concession agreements, where obligations hide in schedules",
                    "It converts a rhetorical dispute into a countable one",
                    "It produces evidence a ministry or a court can engage with"])) +
    p("For a practitioner in an advocacy organisation this is the single most portable technique in the "
      "module: if you disagree with an institution's account of its own behaviour, code its documents."))

sec("Institutions", "Staff, boards and borrowers",
    p("Woods's argument in <em>The Globalizers</em> is that outcomes are produced by the interaction of three "
      "things, not by any one of them: the professional norms of staff, the voting arithmetic of the board, "
      "and the domestic coalitions inside the borrowing country. The same conditions imposed on two "
      "countries produce different results because the third factor differs.") +
    hbox("The practical consequence is that a campaign aimed only at the lender is aimed at one of three "
         "actors. Where the domestic coalition is the binding constraint, pressure in Washington changes "
         "nothing.", "teal") +
    p("The reverse error is just as common and less discussed. Where a domestic government genuinely wants a reform that its own coalition blocks, an external condition can supply political cover: the reform proceeds and the blame is exported to the lender. This is one reason conditionality persists despite poor evidence of its effectiveness on paper. It is doing work the published rationale does not describe, and a study that measures only the stated objective will find it failing while the actual function succeeds."))

sec("Institutions", "Module two summary",
    bullets(["Lenders differ by ownership, borrower and instrument, and the private arms differ most",
             "Voting is weighted by subscription, and the distribution is published",
             "The political-prohibition clause explains why safeguards read as technical standards",
             "IDA and IBRD terms differ enough that graduation is a fiscal event",
             "Conditionality reform is measurably more presentational than substantive",
             "Outcomes come from staff, board and domestic coalition together"]) +
    p("The thread connecting these is that the institutional detail is not decoration around the politics; it is where the politics happens. Voting weights determine whose preferences survive a contested policy revision. The political-prohibition clause determines the register in which a social standard must be written to be adoptable at all. And the difference between IDA and IBRD terms determines whether a ministry of finance can afford a programme that a line ministry wants. Someone campaigning on any of these without knowing which body decides what will aim at the wrong target, and the institutions are under no obligation to correct them."))

# ============================================================ 03
divider(3, "Module Three", "Instruments: What a Loan Actually Is")

sec("Instruments", "The instrument menu",
    table(["Instrument", "Who is on the hook", "When money moves", "Typical use"],
          [["Sovereign loan", "The state", "On disbursement", "Programme or project lending"],
           ["Sub-sovereign loan", "State or municipal body, often with sovereign guarantee", "On disbursement", "Urban infrastructure"],
           ["Corporate loan", "A company", "On disbursement", "Private arm lending"],
           ["Equity", "Investor shares in upside and downside", "At investment", "Firm-level, funds"],
           ["Guarantee", "Guarantor, only if called", "On default or trigger", "Credit enhancement"],
           ["Political risk insurance", "Insurer, on covered event", "On claim", "Cross-border investment"],
           ["Results-based finance", "Borrower until results verified", "On verified result", "Service delivery programmes"]]) +
    p("Most confusion in public debate comes from treating the first and the fifth rows as the same thing."))

sec("Instruments", "Reading a loan: the six terms that decide everything",
    twocol("The commercial terms",
           bullets(["<strong>Principal</strong> &mdash; the amount",
                    "<strong>Interest</strong> &mdash; fixed or floating, and over what benchmark",
                    "<strong>Maturity</strong> &mdash; total life of the loan",
                    "<strong>Grace period</strong> &mdash; years before principal repayment begins",
                    "<strong>Fees</strong> &mdash; commitment, front-end, administrative",
                    "<strong>Currency</strong> &mdash; and therefore who bears exchange risk"]),
           "Why currency is the quiet one",
           p("A loan denominated in a hard currency and serviced from revenue earned in rupees carries an "
             "exchange risk that sits with the borrower and appears nowhere in the interest rate. A currency "
             "movement can make an affordable loan unaffordable without a single term changing.") +
           p("Ask, of any foreign-currency infrastructure loan: what currency is the project's revenue in, and "
             "who absorbs the mismatch?")))

sec("Instruments", "Grace periods and why they flatter",
    p("A long grace period makes the early years of a loan look painless, which is precisely the period a "
      "political cycle covers. The repayment burden arrives later, frequently after the government that "
      "signed has left office.") +
    hbox("This is not an argument against grace periods, which exist for good reasons when a project takes "
         "years to generate revenue. It is an argument for looking at the full repayment profile rather "
         "than the first five years.") +
    p("The test to apply: plot the debt service year by year over the full maturity and ask which "
      "administration faces the peak."))

sec("Instruments", "Guarantees and contingent liabilities",
    twocol("Why governments like them",
           bullets(["No cash leaves the treasury on signing",
                    "They may sit outside headline debt statistics",
                    "They can unlock private finance at lower cost",
                    "The cost, if any, falls in a future year"]),
           "Why auditors and economists worry",
           bullets(["The liability is real but unpriced in public reporting",
                    "Correlated triggers mean several may be called at once",
                    "They shift risk to the public without a visible appropriation",
                    "Disclosure practice varies widely between jurisdictions"])) +
    p("The question to ask of any guarantee is not whether it will be called, but what has to happen for it "
      "to be called, and how correlated that event is with everything else going wrong at the same time."))

sec("Instruments", "Results-based and policy-based lending",
    table(["", "Investment lending", "Policy-based lending", "Results-based lending"],
          [["Money follows", "Project expenditure", "Policy actions completed", "Verified results"],
           ["Main risk", "Implementation", "Reform reversal", "Measurement"],
           ["Where disputes arise", "Procurement, safeguards", "Whether a condition was met", "Whether a result is real"],
           ["Accountability question", "Who was displaced", "Who was consulted on the reform", "Who verified, and how"]]) +
    hbox("Results-based lending moves the contested ground to measurement, which is why an MEL practitioner "
         "is suddenly a party to a financing dispute. If the indicator is weak, the disbursement is wrong "
         "in one direction or the other.", "teal"))

sec("Instruments", "Concessionality, computed",
    p("The grant element of a loan is the difference between its face value and the present value of its "
      "future repayments, expressed as a percentage of face value. The discount rate chosen changes the "
      "answer, which is why the choice of discount rate is itself contested in the reporting standards.") +
    bullets(["A grant has a grant element of 100% by definition",
             "A loan at the discount rate has a grant element of zero",
             "Longer maturity and longer grace raise the grant element",
             "A higher discount rate raises the measured concessionality of any given loan",
             "Reporting standards that permit a generous discount rate therefore inflate reported concessional finance"]) +
    SRC % "Method as used in OECD DAC reporting; the Oxfam and CARE shadow reports contest the standard application.")

sec("Instruments", "Debt sustainability, briefly and carefully",
    p("Debt sustainability analysis asks whether a country can service its obligations without an "
      "implausible fiscal adjustment. It is a projection exercise, and its conclusions are sensitive to "
      "assumptions about growth, exchange rates and interest rates over long horizons.") +
    twocol("What it is good for",
           bullets(["Structuring a conversation about repayment capacity",
                    "Making assumptions explicit and testable",
                    "Comparing scenarios rather than asserting a single future"]),
           "What it is not",
           bullets(["A measurement of an observed quantity",
                    "Independent of the growth assumption, which drives the result",
                    "A neutral technical output &mdash; the assumptions are choices",
                    "A reason to treat contingent liabilities as absent because they are unquantified"])))

sec("Instruments", "Where the documents are",
    table(["Document", "What it tells you", "Usually available?"],
          [["Project appraisal document", "Rationale, design, expected results, risks", "Often published by MDBs"],
           ["Loan or financing agreement", "The binding terms and covenants", "Frequently published"],
           ["Environmental and social assessment", "Footprint, affected people, mitigation", "Usually published, sometimes late"],
           ["Procurement notices and awards", "Who is building it", "Often published"],
           ["Concession agreement (PPP)", "Risk allocation between state and concessionaire", "Variable; often the hardest to obtain"],
           ["Implementation and completion report", "What actually happened", "Published after close"]]) +
    hbox("The concession agreement is the row that matters most and is hardest to get. It is where risk "
         "allocation actually lives, and its schedules carry the obligations the main text only gestures at."))

sec("Instruments", "Module three summary",
    bullets(["The instrument determines who bears risk; the headline figure does not",
             "Six terms decide a loan's real burden, and currency is the quietest of them",
             "Guarantees are unpriced public risk with a delayed and correlated cost",
             "Results-based lending makes measurement quality a financing question",
             "Grant element depends on a chosen discount rate, so the standard is contestable",
             "Most of the documents you need exist; the concession agreement is the hard one"]) +
    p("If you retain one operational habit from this module, make it the currency question. Interest rates are negotiated in public and scrutinised; currency denomination is treated as a technical detail and settled quietly. A project earning rupees and servicing dollars has an unhedged exposure that no clause in the loan describes as a risk, and a movement of twenty per cent in the exchange rate can convert a comfortable debt service into an impossible one without a single term of the agreement changing. Ask what currency the revenue is in, ask what currency the debt is in, and if they differ, ask who absorbs the gap."))

# ============================================================ 04
divider(4, "Module Four", "From Lending to De-risking")

sec("The shift", "Billions to trillions",
    p("Ahead of the 2015 Addis Ababa conference on financing for development, the multilateral development "
      "banks and the IMF published a joint paper arguing that the sums implied by the Sustainable "
      "Development Goals were far beyond what aid budgets could supply, and that the gap should be closed "
      "by using public money to mobilise private capital at a multiple.") +
    hbox("The arithmetic of the argument is not in dispute: aid budgets are small relative to the estimated "
         "need. What is in dispute is whether the proposed mechanism delivers the multiple, and what it "
         "costs in policy terms to try.") +
    SRC % "From Billions to Trillions: Transforming Development Finance, joint MDB and IMF paper, Development Committee, 2015.")

sec("The shift", "The Cascade, as the Bank states it",
    flow(["Can the private sector finance it commercially?", "If not, what reform would make it so?", "Only then, public money"]) +
    p("The World Bank's Maximizing Finance for Development approach sets this as a decision sequence for "
      "project appraisal. Read as drafting, the significant feature is where the burden of proof sits: "
      "public financing is the residual, to be justified after the commercial and regulatory-reform options "
      "have been exhausted.") +
    p("Whether that is prudent stewardship of scarce public money or a structural bias against public "
      "provision is the argument. The sequence itself is not hidden; it is published policy."))

sec("The shift", "Gabor's account: the de-risking state",
    p("Daniela Gabor's argument is that Billions to Trillions, Maximizing Finance for Development and the "
      "G20's Infrastructure as an Asset Class agenda are one project: reorganising development around "
      "escorting institutional investors into a new asset class.") +
    twocol("The mechanism she describes",
           bullets(["The state absorbs demand risk, so revenue is predictable",
                    "The state absorbs political risk, including the risk of future policy change",
                    "Local financial systems are reshaped towards market-based finance",
                    "Development assets are standardised so portfolios can hold them"]),
           "The consequence she draws",
           p("A state that has guaranteed investor returns has contracted away part of its own policy "
             "space. Her specific concern is climate: a just transition may require exactly the kinds of "
             "policy change &mdash; tariff changes, retirement of assets, redistribution &mdash; that a "
             "de-risking contract is designed to protect investors against.")) +
    SRC % "Gabor, The Wall Street Consensus, Development and Change 52(3), 2021, pp. 429&ndash;459.")

sec("The shift", "Reading the critique fairly",
    twocol("What the argument establishes",
           bullets(["The policy documents say what Gabor says they say; they are public",
                    "De-risking instruments do transfer specified risks to the public",
                    "Contractual protection of investor returns does constrain later policy",
                    "The direction of travel is documented, not inferred"]),
           "What remains open",
           bullets(["Whether the alternative &mdash; less investment &mdash; would be better for the same populations",
                    "Whether mobilisation ratios are as poor as critics claim, which is measurable",
                    "Whether the policy-space loss is large in practice or mostly theoretical",
                    "Whether the framework applies equally to a large state like India and a small one"])) +
    hbox("Teaching a critique honestly means naming what would falsify it. Mobilisation data, covered next, "
         "is where much of that falsification would have to come from.", "teal"))

sec("Evidence", "Mobilisation: the testable claim",
    p("If public money is justified by the private capital it mobilises, then the ratio is the test. The "
      "OECD publishes an annual series on amounts mobilised from the private sector by official development "
      "finance interventions, broken down by instrument, sector and recipient income group.") +
    bullets(["Guarantees and syndicated loans account for a large share of reported mobilisation",
             "Instrument mix matters: some instruments mobilise far more per public dollar than others",
             "The distribution across income groups is the politically significant cut",
             "The attribution method &mdash; who gets credit for a given private dollar &mdash; is itself a standard, not a fact"]) +
    SRC % "OECD, Amounts Mobilised from the Private Sector by Official Development Finance Interventions, annual series.")

sec("Evidence", "The two questions to ask of any mobilisation figure",
    twocol("Additionality",
           p("Would the private investment have happened without the public intervention? If yes, the public "
             "money did not mobilise anything; it subsidised something that was going to occur anyway. "
             "Additionality is hard to establish because the counterfactual is unobserved. That difficulty "
             "is a reason to state the assumption openly, not a reason to stop asking."),
           "Attribution",
           p("When a guarantee, a concessional tranche and a policy reform all precede one private "
             "investment, which of them mobilised it? Reporting standards answer by convention, apportioning "
             "credit according to a rule. The rule is defensible and it is still a convention, so a "
             "mobilisation total is the output of an accounting decision as much as of an observation.")) +
    hbox("Establish which convention produced a number before comparing two mobilisation figures."))

sec("Evidence", "Where mobilisation lands",
    twocol("The pattern critics point to",
           bullets(["A larger share flows to middle-income than to low-income countries",
                    "Energy, banking and industry attract more than health or education",
                    "Instruments that work need a revenue stream, which social sectors often lack"]),
           "Why that pattern is not surprising",
           bullets(["Private capital requires a return; where there is no revenue there is no return",
                    "Risk-adjusted returns are worse in the poorest markets, which is why they are underserved",
                    "The mechanism is therefore best suited to precisely the places least in need of it",
                    "This is a structural feature, not an implementation failure"])) +
    hbox("If the mechanism works least well where need is greatest, the question is not how to improve it "
         "but what it should be expected to do at all."))

sec("The shift", "Blended finance and the additionality problem",
    p("Blended finance mixes concessional public money with commercial capital in a single structure, "
      "typically with the public tranche taking first-loss or subordinate position. The OECD DAC principles "
      "set standards: anchor to a development rationale, design to attract commercial finance, tailor to "
      "local context, manage for results, and monitor transparently.") +
    twocol("The design question",
           bullets(["How much concession is the minimum needed?",
                    "Who captures the upside if the project succeeds?",
                    "What happens to the public tranche in a downside?",
                    "Is the transaction replicable, or bespoke and unrepeatable?"]),
           "The disclosure question",
           bullets(["Are the terms of the concessional tranche public?",
                    "Is the mobilisation claim independently checkable?",
                    "Is the counterfactual stated, even if it cannot be proven?",
                    "Are failures reported alongside successes?"])))

sec("The shift", "Module four summary",
    bullets(["The shift from lending to mobilising is documented in the institutions' own published policy",
             "The Cascade places public financing last in the appraisal sequence",
             "De-risking transfers specified risks to the public and constrains later policy by contract",
             "Mobilisation ratios are the testable core of the agenda, and OECD publishes the data",
             "Additionality is the hardest and most important question, and is rarely answered",
             "The mechanism performs worst where need is greatest, which is structural"]) +
    p("The fair summary of this debate is that both sides are describing the same mechanism accurately and disagreeing about the counterfactual. Supporters are right that aid budgets cannot fund the estimated need and that private capital will not move without risk mitigation. Critics are right that the mitigation transfers real risk to the public and contracts away policy room. What would settle it is evidence on additionality, and that evidence is thin because the counterfactual is unobservable and nobody with a stake in the answer is well placed to produce it. Treat confident claims in either direction with the scepticism the evidence base deserves."))

# ============================================================ 05
divider(5, "Module Five", "How a Project Gets Financed")

sec("Project finance", "What makes project finance different",
    p("In corporate lending, a bank lends to a company and looks to that company's whole balance sheet for "
      "repayment. In project finance, a lender lends to a single project, usually housed in a special "
      "purpose vehicle, and looks primarily to that project's own cash flows.") +
    twocol("Consequences of non-recourse lending",
           bullets(["The lender's security is the project's revenue, not the sponsor's other assets",
                    "Every risk must be identified and allocated to someone by contract",
                    "Documentation is therefore enormous and highly specific",
                    "The sponsor's exposure is capped at its equity, by design"]),
           "Why that matters for accountability",
           bullets(["The entity that owes duties may be a thin SPV, not the well-known sponsor",
                    "A community's counterparty may have no assets beyond the project",
                    "Contract, not corporate reputation, determines who answers for harm",
                    "Identifying the right respondent is the first task in any complaint"])))

sec("Project finance", "The cast of a typical project",
    table(["Party", "Role", "What they want"],
          [["Sponsor", "Develops and part-owns the project", "Return on equity, limited exposure"],
           ["Special purpose vehicle", "The legal project entity", "To be bankable"],
           ["Lenders", "Senior debt, often a syndicate", "Predictable cash flow and security"],
           ["Government or authority", "Grants the concession, may fund a gap", "Service delivered, fiscal cost contained"],
           ["Offtaker", "Buys the output, e.g. a power distributor", "Supply at agreed price"],
           ["EPC contractor", "Builds it", "Paid on milestones, bounded liability"],
           ["O&M operator", "Runs it", "A workable operating regime"],
           ["Affected people", "Live on or near the site", "Compensation, livelihood, information"]]) +
    hbox("Only the last row has no contract. Everyone else's position is negotiated; theirs is set by "
         "statute and by whatever the safeguard regime requires."))

sec("Project finance", "Risk allocation is the whole document",
    table(["Risk", "Typically borne by", "How it is shifted"],
          [["Construction cost overrun", "EPC contractor", "Fixed-price turnkey contract"],
           ["Delay", "Contractor, then sponsor", "Liquidated damages"],
           ["Demand or volume", "Varies; often the state", "Take-or-pay, availability payment, minimum revenue guarantee"],
           ["Currency", "Borrower, unless hedged", "Hedging, or tariff indexation"],
           ["Interest rate", "Borrower, unless fixed", "Swap"],
           ["Political and regulatory change", "Often the state", "Change-in-law clause, stabilisation clause"],
           ["Force majeure", "Shared by formula", "Defined events and relief"]]) +
    p("The single most consequential row for public policy is the last but one. A change-in-law or "
      "stabilisation clause can require the state to compensate the concessionaire when it changes policy, "
      "which is the contractual form of the policy-space argument in module four."))

sec("Project finance", "Availability payments and take-or-pay",
    twocol("Availability payment",
           p("The state pays the concessionaire for keeping the asset available to a standard, regardless of "
             "how much it is used. Demand risk sits with the state. Common in roads and social "
             "infrastructure where usage is unpredictable or where tolling is politically difficult."),
           "Take-or-pay",
           p("The offtaker must pay for a contracted quantity whether or not it takes delivery. Common in "
             "power. It converts an uncertain revenue stream into a near-certain one, which is exactly what "
             "makes the project financeable and exactly what transfers the risk to the buyer.")) +
    hbox("Both are legitimate instruments and both do the same thing: move demand risk off the investor. "
         "The policy question is whether the price paid for that transfer is known and disclosed.", "teal"))


sec("Project finance", "The financial model, and why it is the real document",
    p("Every project has a financial model: a spreadsheet projecting capital cost, revenue, operating cost, "
      "debt service and equity return over the concession period. The negotiated terms are whatever makes "
      "that model produce an acceptable return.") +
    bullets(["The equity internal rate of return is the number the sponsor is solving for",
             "Tariff, concession length and guarantee structure are the levers that move it",
             "A small change in assumed demand can change the required tariff substantially",
             "The model's assumptions are therefore the substance of the public interest question"]) +
    hbox("Ask for the model's key assumptions, not the model. Demand forecast, discount rate, and assumed "
         "operating cost are usually enough to see whether the deal is generous."))

sec("Project finance", "Why demand forecasts are the recurring failure",
    p("Optimistic traffic and demand forecasts are the most documented pathology in infrastructure "
      "appraisal internationally. Forecasts made by parties with an interest in the project proceeding tend "
      "to be higher than outturn.") +
    twocol("What goes wrong",
           bullets(["The forecast is produced for the promoter",
                    "Optimism is rewarded at appraisal and not penalised later",
                    "Nobody re-checks the forecast against outturn after opening",
                    "Renegotiation absorbs the error, at public cost"]),
           "What a reviewer can do",
           bullets(["Ask who produced the forecast and who paid for it",
                    "Ask for the outturn of the same forecaster's last three projects",
                    "Check whether the contract penalises over-forecasting at all",
                    "Treat a single-point forecast without a range as incomplete"])))

sec("Project finance", "Renegotiation: the normal case, not the failure case",
    p("A large share of long-concession infrastructure contracts are renegotiated. Concessions run for "
      "decades; no party can foresee three decades of demand, policy and cost. The Kelkar Committee's "
      "central insight was that renegotiation should be designed for rather than treated as a scandal.") +
    bullets(["If renegotiation is unplanned, it happens under duress and asymmetric information",
             "The party threatening to walk away has leverage the public interest does not",
             "A pre-agreed renegotiation framework converts a crisis into a procedure",
             "Without one, the state's choice is between a bad deal and a stalled asset"]) +
    SRC % "Committee on Revisiting and Revitalising the PPP Model of Infrastructure Development (Kelkar, chair), 2015.")

sec("Project finance", "What to read, in what order, on a real project",
    flow(["Appraisal document", "Concession agreement", "Environmental and social assessment", "Procurement award", "Implementation report"]) +
    p("The appraisal document tells you what the project is for and what risks were identified. The "
      "concession agreement tells you who carries them. The environmental and social assessment tells you "
      "who lives there. The procurement award tells you who is building it and for how much. The "
      "implementation report, published years later, tells you what actually happened.") +
    hbox("Reading them in that order takes a day and answers most questions an advocacy organisation "
         "actually has."))

sec("Project finance", "Module five summary",
    bullets(["Project finance lends against a project's cash flows, so every risk is allocated by contract",
             "The legal counterparty may be a thin SPV rather than the recognised sponsor",
             "Availability payments and take-or-pay both move demand risk to the public side",
             "Change-in-law and stabilisation clauses are where policy space is contracted away",
             "The financial model's assumptions are the substance of the public interest question",
             "Renegotiation is normal, and is best handled by a framework agreed in advance"]) +
    p("The practical lesson of this module is that a concession is not a procurement with a longer timescale. A procurement buys a thing; a concession allocates an uncertain future between parties with different appetites for risk and very different information about it. That is why the document runs to hundreds of pages and why the schedules matter more than the recitals. When you are handed a summary of a concession, what you have been handed is the part the drafter was comfortable summarising. The risk allocation table is the document."))

# ============================================================ 06
divider(6, "Module Six", "India's Own Architecture")

sec("India", "The institutions in one table",
    table(["Institution or instrument", "Established", "What it does"],
          [["NaBFID", "Act assented 28 March 2021", "Development financial institution for long-term infrastructure lending"],
           ["National Monetisation Pipeline", "Announced Union Budget 2021-22", "Leases existing public assets to raise capital"],
           ["Viability gap funding", "Scheme, earlier origin", "Capital grant to make a marginal PPP project viable"],
           ["EXIM Bank, NABARD, NHB, SIDBI", "Various", "The four earlier All India Financial Institutions"],
           ["State PPP cells and authorities", "Various", "Procure and manage state-level concessions"]]) +
    p("NaBFID is the fifth All India Financial Institution, after EXIM Bank, NABARD, NHB and SIDBI.") +
    p("Read the table as a sequence rather than a list. India dismantled its development financial institutions in the 1990s and 2000s on the reasoning that banks and capital markets would supply long-term finance more efficiently. Banks then lent heavily to infrastructure, funded by short-term deposits, and a large share of that lending became stressed. NaBFID in 2021 is a reversal of the 1990s judgement, made in the light of what followed it. Whether the second attempt works depends on whether the bond market that the first attempt lacked now exists."))

sec("India", "NaBFID: the return of the DFI",
    p("India spent the 1990s and 2000s winding down the development financial institution model, on the "
      "view that term lending was better done by banks and markets. NaBFID reverses that judgement for "
      "infrastructure specifically.") +
    twocol("What the Act provides",
           bullets(["Authorised share capital of <strong>Rs 1,00,000 crore</strong>",
                    "Shares divided into 10,000 crore shares of Rs 10 each",
                    "Mandate covering long-term non-recourse infrastructure finance",
                    "An explicit remit to develop the bonds and derivatives markets that such lending needs"]),
           "Who may hold shares",
           bullets(["The Central Government",
                    "Multilateral institutions",
                    "Sovereign wealth funds",
                    "Pension funds and insurers",
                    "Banks and other financial institutions"])) +
    hbox("That shareholder list is the de-risking argument written into statute: the institution is "
         "designed from the outset to sit between public purpose and institutional investor capital.") +
    SRC % "The National Bank for Financing Infrastructure and Development Act, 2021.")

sec("India", "Why a DFI for infrastructure at all",
    twocol("The asset-liability problem",
           p("A commercial bank funds itself with short-term deposits. An infrastructure loan runs fifteen to "
             "twenty-five years. Funding long assets with short liabilities is the classic maturity "
             "mismatch, and it is a large part of why Indian bank lending to infrastructure ended in stressed "
             "assets in the 2010s."),
           "What a DFI is meant to fix",
           p("A dedicated institution can fund itself long, through bonds, and hold long assets without the "
             "mismatch. Whether it does so depends on whether a deep long-tenor bond market exists, which is "
             "why the Act gives NaBFID an explicit market-development mandate alongside its lending one.")) +
    p("Judge the institution on both mandates. Lending volume alone would miss half of what it was created to do."))

sec("India", "Asset monetisation: the logic",
    p("The National Monetisation Pipeline, developed by NITI Aayog on a Union Budget 2021-22 mandate, "
      "identified an aggregate monetisation potential of <strong>Rs 6 lakh crore</strong> across roads, "
      "railways, power, gas pipelines, telecom and civil aviation, over FY2021-22 to FY2024-25.") +
    bullets(["The framing is explicit: structured contractual partnership, not privatisation or slump sale",
             "Ownership is retained; the right to operate and collect revenue is transferred for a period",
             "The state receives capital up front, to recycle into new construction",
             "Government reporting put realised monetisation at about Rs 3.85 lakh crore over the first three years"]) +
    SRC % "NITI Aayog, National Monetisation Pipeline, Volumes I and II, August 2021; realisation figure from Government of India reporting.")

sec("India", "Asset monetisation: the questions to ask",
    twocol("The case for",
           bullets(["Brownfield assets carry no construction risk, so they attract capital cheaply",
                    "Capital released can fund new assets without new borrowing",
                    "Private operation may improve maintenance and service",
                    "Ownership is retained, so the asset returns at the end of the term"]),
           "The case to examine",
           bullets(["Is the up-front payment good value against the revenue forgone over the term?",
                    "Who sets tariffs during the concession, and under what constraint?",
                    "What happens to the workforce?",
                    "Is the discount rate used to value the future revenue stream disclosed?",
                    "What condition must the asset be returned in, and who verifies?"])) +
    hbox("The valuation question is the whole question. Monetisation is a trade of future revenue for "
         "present cash, and whether it is a good trade depends entirely on the rate at which the future "
         "was discounted."))

sec("India", "Viability gap funding",
    p("Viability gap funding is a capital grant to a PPP project that is economically desirable but not "
      "commercially viable at a tariff users can bear. The state contributes a share of capital cost so "
      "that the project clears the investor's return threshold.") +
    twocol("When it is defensible",
           bullets(["The social return exceeds the private return, which is the textbook case for subsidy",
                    "The gap is competitively bid, so the subsidy is minimised",
                    "The grant is capped and disclosed"]),
           "When it is not",
           bullets(["The gap is negotiated rather than bid",
                    "The demand forecast that establishes the gap is the promoter's own",
                    "Subsidy is layered on top of a demand guarantee, so the state pays twice",
                    "The project would have been viable without it"])))

sec("India", "The Kelkar diagnosis, and what to trace",
    p("The Kelkar Committee reported to the Finance Minister on 19 November 2015; the report was released "
      "publicly on 28 December 2015. Its diagnosis was that PPP contracts had been drafted around fiscal "
      "transfer rather than service delivery, and that disputes had nowhere sensible to go.") +
    bullets(["Recommended an Infrastructure PPP Project Review Committee",
             "Recommended an Infrastructure PPP Adjudication Tribunal, headed by a former Supreme Court or High Court judge",
             "Recommended model concession agreements be reviewed sector by sector",
             "Recommended a national PPP policy document from the Ministry of Finance",
             "Recommended an inbuilt renegotiation mechanism rather than ad hoc renegotiation"]) +
    hbox("A good exercise for a learner: take each recommendation and establish what was actually "
         "implemented. The gap between a well-reasoned official report and its implementation is itself "
         "the subject.", "teal"))

sec("India", "Where Indian project information lives",
    table(["Source", "What you get"],
          [["Ministry and authority websites", "Concession notices, model agreements, sector policy"],
           ["PRS Legislative Research", "Bill tracks, committee report summaries, legislative history"],
           ["CAG audit reports", "After-the-fact scrutiny of specific projects and schemes"],
           ["Parliamentary questions and standing committee reports", "Answers on specific projects, often the only public figure"],
           ["Environmental clearance portals", "EIA reports, public hearing minutes, clearance conditions"],
           ["Company filings", "Where the concessionaire is listed, the project's financials"]]) +
    p("Comparing a Bill as introduced with the Act as assented is the fastest way to see which safeguards "
      "survived committee, and PRS makes that comparison straightforward."))

sec("India", "A worked comparison",
    table(["", "Budget-funded public works", "PPP concession", "Monetised brownfield asset"],
          [["Who builds", "Government contractor", "Concessionaire", "Already built"],
           ["Who owns", "Government", "Government, after transfer", "Government throughout"],
           ["Who operates", "Government", "Concessionaire, for the term", "Operator, for the term"],
           ["Where the money comes from", "Budget", "Private capital, sometimes with VGF", "Up-front payment from operator"],
           ["Main public risk", "Cost overrun", "Demand guarantee, change in law", "Under-valuation of the stream sold"],
           ["Main public document", "Budget line and tender", "Concession agreement", "Transaction documents and valuation"]]) +
    hbox("Three routes to the same road. They differ less in what gets built than in who carries the "
         "downside and which document you have to read to find out."))

sec("India", "Module six summary",
    bullets(["NaBFID revives the DFI model for infrastructure, with Rs 1,00,000 crore authorised capital and a market-development mandate",
             "Its permitted shareholder list runs from the Central Government to pension funds and sovereign wealth funds",
             "The Monetisation Pipeline trades future revenue for present cash; the discount rate is the crux",
             "Viability gap funding is defensible when competitively bid and not stacked on other guarantees",
             "Kelkar's recommendations are a checklist to trace against actual implementation",
             "Indian project information is scattered but substantially public"]) +
    p("Two threads run through this module and both are worth stating plainly. The first is that India has now tried, at different times, most of the available models: budget-funded public works, PPP concessions with viability gap support, a dedicated development financial institution, and the sale of future revenue from assets already built. Each was adopted partly because the previous one disappointed, which should make anyone cautious about the current one's permanence. The second is that the disappointments were rarely about the model in the abstract; they were about forecasting, risk allocation and renegotiation, which are execution questions that follow whichever model is chosen."))

# ============================================================ 07
divider(7, "Module Seven", "Land, Environment and Consent")

sec("Law", "Where finance meets the people on the site",
    p("Every financed infrastructure project occupies land, and in India two statutes principally govern "
      "what it owes the people there: the Right to Fair Compensation and Transparency in Land Acquisition, "
      "Rehabilitation and Resettlement Act, 2013, and the Environment Impact Assessment Notification, 2006, "
      "issued under the Environment (Protection) Act, 1986.") +
    hbox("For a finance course these are not a digression. They generate the documents that constitute the "
         "public record of a project's social and environmental cost, and those documents are frequently "
         "the only description of the project available to anyone outside it.", "teal"))

sec("Law", "What the 2013 Act changed",
    twocol("The 1894 Act",
           bullets(["Colonial-era statute",
                    "Acquisition for a broadly defined public purpose",
                    "Compensation, with limited process",
                    "No general statutory resettlement entitlement",
                    "Urgency provisions widely used"]),
           "The 2013 Act",
           bullets(["Consent requirements for certain private and PPP acquisitions",
                    "Social impact assessment as a statutory step",
                    "Rehabilitation and resettlement entitlements in the statute itself",
                    "Defined timelines and published documents",
                    "Retained urgency provisions, narrower in scope"])) +
    p("The practical shift is procedural as much as substantive: the Act creates steps that must be "
      "documented, and documentation is what makes a process reviewable.") +
    p("One structural feature deserves emphasis because it is frequently missed. The 2013 Act extends entitlements beyond people who hold title to the land. Families whose livelihood depends on the area, including agricultural labourers, artisans and those dependent on common resources, fall within its definition of affected families. In practice this is the provision most often under-implemented, because identifying the landless requires survey work that acquiring authorities have an incentive to do narrowly, and because the people affected are least likely to have documentation of their own."))

sec("Law", "Social impact assessment as a document trail",
    flow(["Notification", "Social impact assessment", "Public hearing", "Expert appraisal", "Award and R&R"]) +
    bullets(["The assessment identifies affected families, not just landowners, which matters for the landless",
             "It is required to consider whether the acquisition is the minimum necessary",
             "The public hearing produces minutes, which are a record of objections",
             "Entitlements attach to categories defined in the Act's schedules"]) +
    hbox("For an organisation supporting affected people, the schedules are the operative part. They set "
         "the floor, and a project cannot contract below a statutory floor."))

sec("Law", "The EIA Notification 2006 in outline",
    table(["Stage", "What happens", "What it produces"],
          [["Screening", "Is the project in category A or B?", "Determines who appraises it"],
           ["Scoping", "What must the assessment examine?", "Terms of reference"],
           ["Public consultation", "Hearing plus written responses", "Minutes and objections on record"],
           ["Appraisal", "Expert committee review", "Recommendation"],
           ["Clearance", "Grant with conditions, or refusal", "Enforceable clearance conditions"]]) +
    p("Category A projects are appraised centrally; category B at state level. The screening decision "
      "therefore determines the forum, and the forum affects both scrutiny and the route for challenge.") +
    p("Two practical notes on obtaining these documents. Draft EIA reports are published before the public hearing precisely so that objections can be informed, which means the window to read and respond is narrow and known in advance rather than discretionary. And the minutes of the hearing are a formal record: objections made there are on file whether or not they are accepted, and a later challenge can point to the fact that a specific risk was raised at the time and how the appraisal dealt with it."))

sec("Law", "Clearance conditions are enforceable commitments",
    p("An environmental clearance is granted subject to conditions. Those conditions are not advisory. They "
      "are the terms on which the project was permitted, and compliance with them is reportable and "
      "challengeable.") +
    twocol("What to do with them",
           bullets(["Obtain the clearance letter and list the conditions",
                    "Identify which are measurable and on what schedule",
                    "Request the compliance reports the conditions require",
                    "Compare the reports against observable conditions on the ground"]),
           "Why this is often the strongest route",
           bullets(["It does not require challenging the project itself",
                    "It uses the promoter's own commitments as the standard",
                    "Non-compliance is a factual question, not a contested policy one",
                    "It has a forum: the regulator that granted the clearance"])))

sec("Law", "Consent, and what it does and does not mean",
    p("The 2013 Act's consent requirements apply to defined categories of acquisition and are expressed as "
      "thresholds of affected families. Consent in this statutory sense is a procedural requirement with a "
      "numerical threshold. It is not the same as the free, prior and informed consent standard used in "
      "international instruments and in some lenders' safeguard policies.") +
    hbox("Where a project is financed by an institution with its own consultation standard, two regimes "
         "apply at once, and they do not always align. Knowing which standard binds which party is the "
         "first question in a safeguards dispute."))

sec("Law", "The exemptions are where the litigation is",
    p("Both statutory regimes contain exemptions, exclusions and category boundaries, and in practice a "
      "large share of dispute concerns whether a project falls inside or outside them rather than whether "
      "its substantive obligations were met.") +
    bullets(["Whether an acquisition falls under a state-specific or sector-specific regime",
             "Whether a project is category A or category B under the EIA Notification",
             "Whether an expansion requires fresh appraisal or rides on an earlier clearance",
             "Whether urgency provisions were properly invoked",
             "Whether a project was split so that each part falls below a threshold"]) +
    hbox("Project splitting is the recurring one. If a single development is appraised as several smaller "
         "projects, each may avoid the threshold that the whole would cross."))

sec("Law", "What a finance practitioner should take from this module",
    bullets(["Two Indian statutes generate the public documents describing a project's social and environmental cost",
             "The 2013 Act's entitlements are a statutory floor a contract cannot go below",
             "The EIA process produces minutes, objections and enforceable clearance conditions",
             "Compliance with a promoter's own clearance conditions is usually the most tractable line of challenge",
             "Statutory consent and international free, prior and informed consent are different standards",
             "Category and threshold disputes, including project splitting, are where the action is"]) +
    hbox("None of this requires legal training to use. It requires knowing the documents exist and asking "
         "for them.", "teal") +
    p("It is worth being precise about why a finance course spends a module on two statutes. It is not "
      "because a finance practitioner needs to litigate. It is because these statutes are the only "
      "mechanism that compels a project to produce a public description of its own social and "
      "environmental cost, in a form that can be checked against what is happening on the ground. Without "
      "the social impact assessment and the environmental clearance, the public record of a large project "
      "consists of a press release and a contractor's board. With them there is a document trail that "
      "names affected people, sets entitlements, and records commitments the project made in order to be "
      "permitted at all."))

# ============================================================ 08
divider(8, "Module Eight", "Climate Finance and Its Accounting")

sec("Climate", "The headline and the argument, revisited",
    p("Module one opened with the gap between US$115.9 billion reported and US$28&ndash;35 billion assessed. "
      "This module explains how a gap that large is produced without anyone falsifying a number.") +
    table(["Accounting choice", "Effect on the headline"],
          [["Count loans at face value rather than grant equivalent", "Raises it substantially"],
           ["Use a generous discount rate for grant equivalence", "Raises measured concessionality"],
           ["Count the full value of a project with a partial climate component", "Raises it"],
           ["Count mobilised private finance alongside public", "Raises it"],
           ["Count finance that would have flowed anyway as climate finance", "Raises it"]]) +
    p("Every row is a defensible convention that someone argues for. Each one moves the total in the same "
      "direction, which is the pattern worth noticing.") +
    SRC % "Oxfam and CARE, Climate Finance Shadow Report 2025, reporting year 2022.")

sec("Climate", "Adequacy and direction are different questions",
    twocol("Adequacy",
           p("Is the total large enough against the estimated need? This is the question the US$100 billion "
             "commitment and its successors are assessed against, and it is the one most reporting covers."),
           "Direction",
           p("Where does the money go, and as what? Mitigation or adaptation, grant or loan, which countries, "
             "which sectors. A total can grow while the adaptation share falls, and for a practitioner "
             "working on adaptation in South Asia the second question is the material one.")) +
    hbox("A headline that answers adequacy tells you almost nothing about direction, and direction is where "
         "the distributional consequences are."))

sec("Climate", "Why adaptation is structurally underfunded",
    p("Mitigation projects frequently generate a revenue stream: a solar plant sells power. Adaptation "
      "frequently does not: a sea wall, an early warning system, a drought-resistant cropping programme "
      "produce avoided losses rather than income.") +
    bullets(["Private capital requires a return, and avoided loss is not a return to the investor",
             "So mitigation attracts blended and mobilised finance more readily",
             "Adaptation therefore depends disproportionately on grants and public budgets",
             "Which are precisely the sources under pressure",
             "The UNEP Adaptation Gap Report series quantifies the resulting shortfall"]) +
    hbox("This is not a failure of effort. It follows from the instrument: a mechanism built to mobilise "
         "private capital cannot fund things that generate no cash flow."))

sec("Climate", "Loss and damage, and why it is a separate category",
    twocol("The three categories",
           bullets(["<strong>Mitigation</strong> &mdash; reducing emissions",
                    "<strong>Adaptation</strong> &mdash; reducing harm from changes now unavoidable",
                    "<strong>Loss and damage</strong> &mdash; harm that has already occurred and cannot be adapted to"]),
           "Why the third is contested",
           p("Adaptation finance can be framed as investment. Loss and damage finance is closer to "
             "compensation, and compensation implies responsibility. That is why the category was resisted "
             "for years and why its institutional form, funding level and eligibility rules remain the "
             "sharpest part of the negotiation.")) +
    p("For a South Asian practitioner the category matters concretely rather than semantically. Slow-onset losses, such as land becoming saline or a glacier-fed river changing regime, sit awkwardly in every existing funding window: they are not a discrete disaster that triggers humanitarian finance, and they are not something adaptation spending can prevent. How eligibility is drawn will determine whether these losses are fundable at all, which is why the drafting of eligibility criteria deserves more attention than the headline pledge figures usually get."))

sec("Climate", "Who publishes what",
    table(["Source", "What it reports", "Read it for"],
          [["OECD", "Climate finance provided and mobilised by developed countries", "The official series the commitment is judged against"],
           ["UNFCCC Standing Committee on Finance", "Biennial Assessment of climate finance flows", "The treaty body's own totals and its candour on definitional uncertainty"],
           ["UNEP", "Adaptation Gap Report", "Estimated adaptation need against delivered finance"],
           ["Oxfam and CARE", "Climate Finance Shadow Report", "The grant-equivalent recalculation and methodological critique"]]) +
    p("Reading the OECD series and the shadow report side by side, on the same year, is the single best "
      "exercise in this module. The disagreement is transparent and the methods are published."))

sec("Climate", "Greenwashing, defined usefully",
    p("Used loosely the word means little. Used precisely it names specific, checkable practices.") +
    bullets(["<strong>Relabelling</strong>: existing development finance reported as climate finance without change in activity",
             "<strong>Over-attribution</strong>: counting a project's full value when only a component is climate-related",
             "<strong>Double counting</strong>: the same flow reported by more than one party",
             "<strong>Instrument inflation</strong>: reporting loans at face value as though they were grants",
             "<strong>Definitional drift</strong>: widening what qualifies, so totals rise without flows changing"]) +
    hbox("Each of these is testable against published methodology. An accusation of greenwashing that does "
         "not name which practice is alleged is not yet an argument."))

sec("Climate", "India's stated position",
    p("India's updated Nationally Determined Contribution and its Long-Term Low-Carbon Development Strategy, "
      "both submitted in 2022, set out the country's targets and its assessment of what the transition "
      "requires. For this course the financing paragraphs matter more than the targets.") +
    twocol("What to read them for",
           bullets(["The stated cost of the transition",
                    "How much is expected from domestic sources",
                    "What is asked of international climate finance",
                    "The conditionality attached to specific commitments"]),
           "The exercise",
           p("Set the stated international requirement against the delivered flows in the previous slides. "
             "That arithmetic, done honestly, structures every negotiating position India takes, and doing it "
             "yourself is more instructive than reading a summary of someone else's version.")))

sec("Climate", "A checklist for any climate finance claim",
    flow(["What year?", "Grant or loan?", "Whose money?", "Counted how?"]) +
    bullets(["<strong>Year</strong>: reporting lags two to three years, so a current-sounding figure is usually old",
             "<strong>Instrument</strong>: face value or grant equivalent changes the answer by a factor of three",
             "<strong>Source</strong>: public, mobilised private, or both added together",
             "<strong>Method</strong>: which attribution and qualification rules were applied"]) +
    hbox("Four questions. Most published climate finance claims fail at least one of them, and asking is "
         "not hostile: it is the minimum required to compare two numbers.", "teal"))

sec("Climate", "Module eight summary",
    bullets(["A large reported-versus-assessed gap is produced by conventions, not by falsification",
             "Every convention in common use moves the total in the same direction",
             "Adequacy and direction are separate questions, and direction carries the distributional consequences",
             "Adaptation is structurally underfunded because it generates no revenue stream",
             "Loss and damage is contested because it implies responsibility rather than investment",
             "Greenwashing is checkable once you name which specific practice is alleged"]) +
    p("A closing caution against the easy conclusion. The accounting problems documented here are real and they are not, by themselves, evidence that climate finance is a fiction or that the institutions reporting it are dishonest. Reporting conventions are genuinely difficult: reasonable people disagree about whether a loan at below-market rates delivers value equal to its face value, its grant equivalent, or something between. What is fair to say, and what the evidence supports, is that every convention in wide use happens to raise the reported total, that the bodies choosing the conventions are the bodies being assessed by them, and that the resulting numbers should therefore be read as negotiated figures rather than as measurements."))

# ============================================================ 09
divider(9, "Module Nine", "Accountability: Who Can Complain")

sec("Accountability", "The mechanism that started it",
    p("The World Bank's Inspection Panel was created by the Board in September 1993 and began operating on "
      "1 August 1994. It was the first independent accountability mechanism at any international financial "
      "institution, and its innovation has since been copied at more than twenty other development banks "
      "and bilateral institutions.") +
    bullets(["It provides a route for people who believe a Bank-financed operation may harm them",
             "It reports to the Board, not to management, which is the source of its independence",
             "It assesses compliance with the Bank's own policies and procedures",
             "It cannot award compensation; it can find non-compliance and trigger a response"]) +
    SRC % "World Bank Inspection Panel, institutional history and case registry.")

sec("Accountability", "What these mechanisms can and cannot do",
    twocol("Can",
           bullets(["Investigate whether the institution followed its own safeguard policies",
                    "Produce a public finding of non-compliance",
                    "Require management to prepare an action plan",
                    "In some mechanisms, offer dispute resolution between parties",
                    "Create a documented record that other forums can use"]),
           "Cannot",
           bullets(["Order compensation as a court would",
                    "Halt a project directly",
                    "Bind the borrower government, which is not the respondent",
                    "Act on harm unconnected to a policy the institution owes",
                    "Help where the financing came from an institution with no mechanism"])) +
    hbox("The central limit is the second column's third row. The respondent is the lender, not the state, "
         "so a finding tells you the lender breached its own rules. Whether anything changes on the ground "
         "depends on the action plan that follows."))

sec("Accountability", "The map of mechanisms",
    table(["Institution", "Mechanism", "Covers"],
          [["World Bank (IBRD/IDA)", "Inspection Panel", "Sovereign-lending operations"],
           ["IFC and MIGA", "Compliance Advisor Ombudsman", "Private-sector investments and guarantees"],
           ["Asian Development Bank", "Accountability Mechanism", "ADB-financed projects"],
           ["AIIB", "Its own project-affected people's mechanism", "AIIB-financed projects"],
           ["Other MDBs and bilaterals", "Various, modelled on the Panel", "Varies by institution"]]) +
    p("The first task in any complaint is identifying which institution financed the specific component "
      "causing harm, because that determines which mechanism has jurisdiction and which safeguard policy "
      "sets the standard."))

sec("Accountability", "The practical sequence",
    flow(["Identify the financier", "Find the policy breached", "Establish harm and link", "File", "Follow the action plan"]) +
    bullets(["<strong>Financier</strong>: from the appraisal document, procurement notices, or the project's own signage",
             "<strong>Policy</strong>: the safeguard framework in force when the project was approved, not today's",
             "<strong>Harm and link</strong>: the requirement is harm plausibly connected to the breach",
             "<strong>File</strong>: mechanisms have eligibility criteria and time limits; read them first",
             "<strong>Follow-up</strong>: the action plan and its monitoring is where outcomes are won or lost"]) +
    hbox("The second bullet catches people out. Safeguard frameworks are revised, and the version that "
         "binds a project is generally the one in force at approval."))

sec("Accountability", "Why most eligible complaints are never filed",
    twocol("The practical barriers",
           bullets(["Affected people do not know which institution financed the project",
                    "Documents are in English and online",
                    "Filing requires knowing that a mechanism exists at all",
                    "Time limits run while people are still negotiating locally",
                    "Fear of retaliation is a documented and serious constraint"]),
           "What an intermediary organisation can do",
           bullets(["Establish the financier early, before harm crystallises",
                    "Obtain and translate the safeguard summary",
                    "Document harm contemporaneously, with dates",
                    "Advise on time limits before they expire",
                    "Support, and where appropriate front, the filing"])) +
    p("The gap between a mechanism as designed and a mechanism as reached is the single most useful thing "
      "to understand about this architecture, and it is not primarily a legal gap."))

sec("Accountability", "Reading a case file",
    p("Every mechanism publishes its cases. Reading two or three end to end teaches more than any summary "
      "of the procedure, because a case file shows what the mechanism actually treats as sufficient.") +
    bullets(["What the requesters alleged, in their own framing",
             "Which policies the mechanism considered in scope",
             "What management said in response",
             "What the investigation found, and on what evidence",
             "What the action plan committed to, and what monitoring followed"]) +
    hbox("Pay particular attention to the last row. A finding of non-compliance with a weak action plan and "
         "no monitoring is a document, not a remedy.", "teal"))

sec("Accountability", "Domestic routes, and how they interact",
    twocol("Indian forums",
           bullets(["The regulator that granted environmental clearance, on condition compliance",
                    "The National Green Tribunal, on environmental matters",
                    "Writ jurisdiction of the High Courts and Supreme Court",
                    "Statutory authorities under the 2013 land Act",
                    "Information requests under the RTI Act"]),
           "How they compare",
           bullets(["Domestic forums can order remedies; MDB mechanisms cannot",
                    "MDB mechanisms can find fault by the lender; domestic forums usually cannot reach it",
                    "The two produce different records, and both are usable",
                    "Pursuing one does not always preclude the other, but check each mechanism's rules"])) +
    hbox("For most Indian projects the domestic route is the one with teeth. The lender mechanism is "
         "valuable for the record it creates and the leverage that record provides."))

sec("Accountability", "Module nine summary",
    bullets(["The Inspection Panel, from 1993, is the model for more than twenty later mechanisms",
             "They assess the lender's compliance with its own policies, not the state's conduct",
             "They cannot compensate or halt a project; they produce findings and action plans",
             "Jurisdiction follows the financier, so identifying it is the first task",
             "The binding safeguard version is generally the one in force at approval",
             "Most of the barrier is practical, not legal, and intermediaries are what close it",
             "In India the domestic forums carry the remedies; the mechanism carries the record"]) +
    p("The honest assessment of this architecture is mixed and should be taught as such. These mechanisms were a real innovation: before 1994 there was no route at all by which a person harmed by an internationally financed project could be heard by the financier. They have produced findings that changed project designs and, in some cases, stopped them. They are also slow, procedurally demanding, unable to compensate, and reachable in practice mainly by people who have an organised intermediary. Both halves of that are true at once, and a practitioner deciding whether to invest months in a filing needs both halves rather than either one."))

# ============================================================ 10
divider(10, "Module Ten", "Following the Money in Practice")

sec("Method", "The question, made answerable",
    p("&ldquo;Who is financing this project?&rdquo; is not one question. It is four, and they have different "
      "sources and different difficulty.") +
    table(["Question", "Best source", "Difficulty"],
          [["Who is lending?", "Appraisal document, project signage, press release", "Usually easy"],
           ["On what terms?", "Loan or financing agreement", "Moderate; often published"],
           ["Who is building and operating?", "Procurement award, company filings", "Usually easy"],
           ["Who carries the downside?", "Concession agreement and its schedules", "Hard; frequently withheld"]]) +
    hbox("Answering the first three takes an afternoon. The fourth is the one worth the effort, and the one "
         "most often skipped.") +
    p("It helps to know in advance which answers you are entitled to and which you are merely hoping for. Appraisal documents and environmental clearances are published as a matter of policy by most lenders and regulators, so failure to produce them is itself irregular. Concession agreements sit in a different category: commercial confidentiality is routinely claimed over them, sometimes legitimately and often more broadly than the exemption supports. Knowing which of the two you are asking for changes how the request should be framed and what refusal means."))

sec("Method", "A six-step trace",
    flow(["Name the project", "Find the approving authority", "Get the appraisal", "Get the agreements", "Map the parties", "Check compliance"]) +
    bullets(["<strong>Name it precisely</strong>: official project name and any phase or package number",
             "<strong>Approving authority</strong>: which ministry, state department or board signed off",
             "<strong>Appraisal</strong>: MDB project pages, ministry sites, clearance portals",
             "<strong>Agreements</strong>: concession agreement, loan agreement, power purchase agreement",
             "<strong>Parties</strong>: sponsor, SPV, lenders, contractor, offtaker, and their corporate parents",
             "<strong>Compliance</strong>: clearance conditions, safeguard reports, audit findings"]) +
    p("The order is not arbitrary. Each step supplies the identifiers the next one needs: the official project name unlocks the clearance portal, the approving authority tells you whose records to request, and the appraisal document names the parties whose filings you then search. Starting in the middle, which is the natural instinct when a project is already controversial, tends to produce a folder of documents about a project you cannot conclusively identify, which is the state in which most half-finished investigations are abandoned."))

sec("Method", "Where to look, in order of yield",
    table(["Source", "Yields", "Note"],
          [["MDB project pages", "Appraisal, safeguard documents, status", "Searchable by country and sector"],
           ["Environmental clearance portals", "EIA, hearing minutes, conditions", "Often the richest single source"],
           ["Procurement portals and tender notices", "Who won, at what price", "Award notices persist even when tenders expire"],
           ["Company filings and annual reports", "Project-level financials, related parties", "Where the concessionaire is listed"],
           ["CAG audit reports", "Independent scrutiny after the fact", "Slow, but authoritative and citable"],
           ["Parliamentary and assembly questions", "Specific figures on specific projects", "Sometimes the only public number"],
           ["RTI requests", "What none of the above disclosed", "Slowest; use when the gap is identified"]]) +
    p("Work top to bottom. An RTI request drafted after the first six sources are exhausted is far more "
      "precise, and far harder to deflect, than one drafted first."))

sec("Method", "Two habits that make the difference",
    twocol("Date everything",
           p("Frameworks, thresholds and institutional names change. A note that records what a document "
             "said and when you retrieved it stays useful; an undated assertion becomes unusable within a "
             "year and actively misleading within three."),
           "Keep the document, not the summary",
           p("Save the PDF. Government and institutional sites reorganise, and pages that were public are "
             "routinely moved or withdrawn. A citation to a URL that no longer resolves is worth "
             "considerably less than a saved copy with its retrieval date recorded.")) +
    hbox("Both habits cost minutes and both are the difference between research that survives scrutiny and "
         "research that does not.", "teal"))

sec("Method", "A worked exercise",
    p("Pick one infrastructure project near where you work. Something with a name, a site and a visible "
      "contractor board. Then answer, in writing, with a source for each:") +
    bullets(["What is the project's official name and sanctioned cost?",
             "Which authority approved it, and on what date?",
             "Is it budget-funded, a PPP, or a monetised asset?",
             "Who are the sponsor, the SPV and the lenders?",
             "Does it hold an environmental clearance, and what conditions attach?",
             "Was land acquired under the 2013 Act, and what R&amp;R was due?",
             "If demand disappoints, who absorbs the loss?"]) +
    hbox("The last question is the test. If you cannot answer it from public documents, that itself is the "
         "finding, and it is a reportable one."))

sec("Method", "Module ten summary",
    bullets(["Split the question: who lends, on what terms, who builds, who carries the downside",
             "Six steps, from naming the project precisely to checking compliance",
             "Work the sources in order of yield; RTI last and therefore sharper",
             "Date every retrieval and keep the document rather than the summary",
             "Inability to answer the risk-allocation question from public sources is itself a finding"]) +
    p("A final point about what this method is for. Tracing a project is not an end in itself, and a document collection is not an argument. The purpose is to be able to state, precisely and with sources, what a specific project commits the public to and what it owes the people affected by it. That statement is what a journalist can publish, a parliamentarian can ask about, a regulator has to answer, and a court can consider. Everything in this module is in service of producing one paragraph that can survive being checked."))

# ============================================================ 11
divider(11, "Module Eleven", "What to Check Before You Cite")

sec("Practice", "This deck will go out of date, in specific ways",
    table(["What changes", "How fast", "Check against"],
          [["Statutory thresholds and rules", "Years, occasionally faster", "The bare Act as amended, on the ministry site"],
           ["Institutional capital and mandates", "Years", "The institution's own annual report"],
           ["Climate finance totals", "Annually, with a two to three year lag", "OECD series, UNFCCC assessment, shadow reports"],
           ["Energy and data centre projections", "Annually, and revised sharply", "The current IEA edition, not a summary of an old one"],
           ["Safeguard frameworks", "Every several years", "The version in force when the project was approved"],
           ["Monetisation and pipeline figures", "Annually", "NITI Aayog and government reporting"]]) +
    hbox("The figures in this deck carry their source and year for exactly this reason. A number without "
         "its year is not a fact; it is a rumour with a decimal point."))

sec("Practice", "Five questions before you use any number here",
    flow(["What year?", "Who published?", "Counted how?", "Compared to what?", "Still current?"]) +
    bullets(["<strong>Year</strong>: reporting lags, and the lag is often longer than people assume",
             "<strong>Publisher</strong>: an institution reporting on itself is a source, not an independent one",
             "<strong>Method</strong>: face value or grant equivalent; public only or mobilised included",
             "<strong>Comparison</strong>: a total means nothing without the denominator or the counterfactual",
             "<strong>Currency</strong>: has the underlying series been revised since?"]) +
    p("These five questions are most of what separates a citable claim from a repeated one."))

sec("Practice", "Where to go next on ImpactMojo",
    twocol("Go deeper on the evidence",
           bullets(["<em>The Political Economy of Development Finance</em> Deep Dive &mdash; 26 annotated readings, including everything cited here",
                    "<em>Public Finance &amp; Budgeting 101</em> &mdash; the domestic side of the same system",
                    "<em>Political Economy 101</em> &mdash; institutions, rents and collective action"]),
           "Go practical",
           bullets(["<em>Budget &amp; Fiscal Analysis Studio</em> &mdash; trace funds Centre to beneficiary",
                    "<em>Union Budget Explorer</em> &mdash; eight years of actual Union spending head by head",
                    "<em>Energy Explorer</em> &mdash; state generation, potential and coal",
                    "<em>CSR &amp; ESG 101</em> &mdash; corporate money under Section 135"])) +
    p("The Deep Dive is the natural next step: this deck teaches the architecture, and the reading list "
      "gives you the primary documents and the arguments about them."))

sec("Practice", "The six things worth keeping",
    bullets(["A finance figure is a construct; establish what it counts before comparing it to anything",
             "Concessionality and instrument, not headline size, determine what money does to a country",
             "The system has moved from lending to states towards making projects investible, and that shift is documented in the institutions' own policy",
             "In a financed project, risk allocation lives in the contract, and the contract is the document to obtain",
             "Two Indian statutes generate the public record of a project's social and environmental cost",
             "Accountability mechanisms judge the lender against its own rules; domestic forums carry the remedies"]) +
    hbox("If you remember one thing: ask who carries the downside, and keep asking until someone shows you "
         "the clause."))

# ============================================================ extra coverage
divider(12, "Module Twelve", "Lenders and Cases the Map Leaves Out")

sec("Lenders", "Export credit agencies, the quiet channel",
    p("Export credit agencies are state-backed bodies that insure or finance their own country's exporters. "
      "They rarely appear in development finance discussions and they move very large sums into "
      "infrastructure in developing countries, because a power plant or a metro system is, from the "
      "exporting country's point of view, an export order.") +
    twocol("Why they matter here",
           bullets(["The financing is tied, formally or in effect, to buying from the lending country",
                    "Appraisal is organised around export promotion rather than development impact",
                    "Environmental and social standards vary widely between agencies",
                    "Their accountability mechanisms are weaker than the MDBs', where they exist at all",
                    "They frequently co-finance alongside MDBs, in the same project"]),
           "What to check",
           bullets(["Whether the agency is an OECD Arrangement participant, which sets some common terms",
                    "What the tying arrangement is, and what it does to procurement cost",
                    "Which standards the agency applies, and whether they bind the contractor",
                    "Whether a complaint route exists and who may use it"])) +
    hbox("If a project's equipment all comes from one country, look for an export credit agency behind it. "
         "The financing terms may be good and the procurement competition may be absent."))

sec("Lenders", "Bilateral lending beyond the traditional donors",
    p("A substantial share of infrastructure lending to developing countries now comes from bilateral "
      "lenders outside the traditional OECD donor group, with China the largest single source over the "
      "past two decades. The terms and the disclosure practices differ from MDB lending in ways that "
      "matter for anyone trying to trace a project.") +
    twocol("What tends to differ",
           bullets(["Loan agreements are less often published",
                    "Terms sit closer to commercial than to concessional",
                    "Collateral and revenue-assignment arrangements may be used",
                    "Safeguard frameworks and complaint mechanisms differ or are absent",
                    "Contracts may contain confidentiality clauses covering the terms themselves"]),
           "What to do about it",
           bullets(["Work from the borrower's side: budget documents, audit reports, parliamentary answers",
                    "Look for the project in the state's own debt reporting rather than the lender's",
                    "Treat absence of a published agreement as a finding to report, not a dead end",
                    "Be precise about what is unknown rather than inferring terms"])) +
    hbox("Analytical discipline matters most where disclosure is weakest. Say what the documents show and "
         "name what they do not, rather than filling the gap with assumption.", "teal"))

sec("Debt", "When the repayment stops working",
    p("Debt distress is not a binary. A country moves through rising debt service as a share of revenue, "
      "then difficulty rolling over maturing debt, then arrears, then restructuring. Each stage narrows "
      "the fiscal space available for everything else, which is why this is a development question and "
      "not only a finance one.") +
    table(["Stage", "What it looks like", "Effect on spending"],
          [["Rising service burden", "Interest consumes a growing share of revenue", "Crowds out discretionary spending"],
           ["Rollover difficulty", "New borrowing is costly or unavailable", "Capital spending is cut first"],
           ["Arrears", "Payments missed", "Access to new finance largely closes"],
           ["Restructuring", "Terms renegotiated with creditors", "Usually accompanied by fiscal conditions"]]) +
    p("The sequencing matters for a practitioner because capital budgets are cut before salaries and "
      "transfers, so the first visible effect of a debt problem is often a stalled construction site "
      "rather than an announced austerity programme."))

sec("Debt", "Why restructuring is harder than it used to be",
    twocol("The old creditor structure",
           bullets(["A small number of official bilateral creditors",
                    "Coordinated through the Paris Club",
                    "Broadly comparable terms and disclosure",
                    "Multilateral debt treated as senior and generally excluded"]),
           "The current structure",
           bullets(["Official bilateral creditors outside the traditional club",
                    "A large bondholder base, dispersed and hard to convene",
                    "Commercial and collateralised debt with varied terms",
                    "Disagreement about what comparability of treatment requires"])) +
    p("Coordination failure is the binding problem: each creditor class has reason to wait for the others "
      "to take losses first. The consequence falls on the debtor, which stays in limbo while the "
      "negotiation runs, and limbo is itself expensive."))

sec("India", "Municipal and sub-sovereign finance",
    p("Most Indian urban infrastructure is delivered by bodies with weak own-revenue and limited borrowing "
      "capacity. That constraint shapes what gets built more than any national policy does.") +
    twocol("The structural problem",
           bullets(["Property tax collection is well below potential in most cities",
                    "User charges frequently sit below operating cost",
                    "Transfers are substantial but often tied and unpredictable",
                    "A body with weak own-revenue cannot service debt, so it cannot borrow"]),
           "The instruments tried",
           bullets(["Municipal bonds, issued by a small number of larger cities",
                    "Pooled finance structures for smaller bodies",
                    "Centrally sponsored mission funding, tied to reform conditions",
                    "Land-based financing, including betterment levies and land monetisation"])) +
    hbox("Municipal bond issuance in India has remained concentrated in a handful of creditworthy cities. "
         "The reason is the first column: creditworthiness follows own-revenue, and own-revenue is a "
         "political question about property tax, not a financial one."))

sec("Instruments", "Guarantees, in their varieties",
    table(["Type", "Covers", "Typical issuer"],
          [["Partial credit guarantee", "A share of debt service, whatever the cause of default", "MDB, national guarantee fund"],
           ["Partial risk guarantee", "Default caused by specified government non-performance", "MDB"],
           ["Political risk insurance", "Expropriation, transfer restriction, war and civil disturbance", "MIGA, national agencies"],
           ["Sovereign counter-guarantee", "The state indemnifies the guarantor", "The borrowing state"]]) +
    p("The fourth row is the one to look for and the easiest to miss. Where an MDB issues a partial risk "
      "guarantee, the borrowing state commonly counter-guarantees it, which means the risk the guarantee "
      "appeared to move off the public balance sheet has travelled back onto it by a second document.") +
    hbox("A guarantee structure has to be read as a loop, not a line. Ask where the risk finally rests "
         "after every instrument in the chain."))

sec("Instruments", "Outcome-based instruments and their measurement problem",
    p("Development impact bonds and outcome funds pay on verified results rather than on activity. An "
      "investor funds delivery up front and an outcome payer repays with a return if agreed results are "
      "achieved and verified.") +
    twocol("The appeal",
           bullets(["Risk of non-delivery sits with the investor rather than the funder",
                    "Focus shifts from inputs to outcomes",
                    "Delivery organisations gain flexibility within the period",
                    "Verification creates an evidence record that would not otherwise exist"]),
           "The problems that recur",
           bullets(["Transaction costs are high relative to deal size",
                    "Outcome metrics are gameable, and gaming is rational for the investor",
                    "Measurable outcomes displace important unmeasurable ones",
                    "Attribution over a short window is genuinely hard",
                    "Very few have been independently evaluated against a counterfactual"])) +
    hbox("This is where an MEL practitioner becomes a financing party. If the indicator is weak, money "
         "moves wrongly, and the indicator was chosen at contract stage by people who will be paid on it.", "teal"))

sec("Context", "Aid is not the largest flow, and has not been for years",
    p("Development finance discussion focuses on official flows, which are the ones with policy attached. "
      "For many countries they are not the largest external flow, and keeping the relative magnitudes in "
      "view prevents a common category error.") +
    table(["Flow", "Who sends it", "What it responds to"],
          [["Remittances", "Migrant workers to households", "Family need; counter-cyclical in crises"],
           ["Foreign direct investment", "Firms", "Expected commercial return"],
           ["Portfolio investment", "Institutional investors", "Yield and risk appetite; highly reversible"],
           ["Official development assistance", "Donor governments", "Policy priorities and negotiated conditions"],
           ["Non-concessional official lending", "MDBs, bilateral lenders", "Project appraisal and creditworthiness"]]) +
    p("The rows behave differently in a crisis, which is the practically important point. Remittances have "
      "historically held up or risen when a receiving economy weakens; portfolio flows reverse fastest. A "
      "resilience plan built on the wrong row will fail at the moment it is needed."))

sec("Context", "Procurement is where the money actually goes",
    p("A financing decision allocates money; a procurement decision determines who receives it. For a "
      "project's local economic effect, and for most corruption risk, the second matters more.") +
    twocol("What the rules try to do",
           bullets(["Secure value for money through competition",
                    "Treat bidders equally and transparently",
                    "Create a reviewable record of the award decision",
                    "Provide a complaint route for losing bidders"]),
           "Where they are weakened in practice",
           bullets(["Specifications written so only one supplier qualifies",
                    "Qualification thresholds that exclude local firms",
                    "Single-source award justified by urgency",
                    "Splitting contracts to stay under a competitive threshold",
                    "Variations after award that change the deal's economics"])) +
    hbox("Award notices persist online long after tender documents are withdrawn, which makes them the "
         "most reliably obtainable document in the whole chain."))

sec("Practice", "A short glossary to keep",
    terms([("Concession agreement", "The contract granting a private party the right to build or operate an asset and collect revenue for a defined term, and allocating every risk between the parties."),
           ("Special purpose vehicle", "A company created to hold one project, so that its debts and risks are ring-fenced from its sponsor's other business."),
           ("Offtaker", "The party contractually obliged to buy the project's output, whose creditworthiness largely determines whether the project can be financed."),
           ("Availability payment", "Payment for keeping an asset available to standard, irrespective of usage, which places demand risk on the payer."),
           ("Change-in-law clause", "A contract term requiring compensation to the private party if a change in law affects its returns."),
           ("Grant element", "The share of a loan's face value that is effectively a gift, once future repayments are discounted to present value.")]))

sec("Practice", "Three things this deck deliberately does not settle",
    twocol("Open questions",
           bullets(["Whether de-risking produces more real investment than the alternatives, which is an empirical question with contested evidence",
                    "Whether the accountability mechanisms change outcomes or mainly produce records",
                    "Whether a development finance institution is the right vehicle for Indian infrastructure, which the 1990s answered one way and 2021 answered another"]),
           "Why leave them open",
           p("A foundational course that resolved live empirical disputes by assertion would be teaching a "
             "position rather than a subject. Each question above has a serious literature on both sides, "
             "and the Deep Dive that accompanies this deck points to it. Form your own view from the "
             "sources; the purpose here is to make you able to read them.")) +
    hbox("Knowing which questions are settled and which are not is itself part of knowing a field.") +
    p("The deck closes here rather than with a call to action, deliberately. Development finance attracts strong positions, and most of them are held by people who have not read a concession agreement. The purpose of a foundational course is to put you in a position to form a view that survives contact with the documents, and then to change it when the documents say something different. If you finish this deck more uncertain than you started, but better able to say precisely what you are uncertain about and which document would resolve it, the deck has done its work."))

slides.append(('end', None))

# ------------------------------------------------- TOC ranges, computed
mod_titles = [t for (_, _, t) in (pl for k, pl in slides if k == 'divider')]
bounds = [i for i, (k, _) in enumerate(slides) if k == 'divider'] + [len(slides) - 1]
ranges = []
for j in range(len(bounds) - 1):
    first = bounds[j] + 1              # 0-indexed slide after the divider
    last = bounds[j + 1]               # next divider (or end slide)
    ranges.append((mod_titles[j], '%d&ndash;%d' % (first + 1, last)))
slides[1] = ('toc', ranges)

db.build(
    course="Development Finance 101",
    out_name="development-finance.html",
    meta_desc=("Development Finance 101 - a free foundational course for practitioners in South Asia. "
               "Multilateral and bilateral lenders, project and infrastructure finance, the shift from "
               "lending to de-risking private capital, India's own architecture (NaBFID, asset "
               "monetisation, viability gap funding), land and environmental law, climate finance "
               "accounting, and the accountability mechanisms affected communities can use."),
    title_main_html="Development<br>Finance<br><span class='title-accent'>101</span>",
    title_sub_html=("The money that arrives from outside the budget &mdash; who lends, on what terms, "
                    "and who can complain"),
    title_tags=["Free Forever", "100 Slides", "11 Modules", "India-first"],
    toc=ranges,
    slides=slides,
    end_headline_html="Ask who carries the downside.<br>Keep asking until someone shows you the clause.",
    end_byline="Development Finance 101 &middot; ImpactMojo 101 Series",
)
print("slides:", len(slides))
for name, rng in ranges:
    print("  %-46s %s" % (name, rng.replace('&ndash;', '-')))
