#!/usr/bin/env python3
"""Register the Evaluator's Desk products on the site, idempotently.

    python3 scripts/evaluator-pack/register.py BUILD_DIR

BUILD_DIR is the output of build.py (it holds the Word files the samples are cut from).

What it writes, per product: the buy page under products/<slug>/, the UPI QR image,
a watermarked sample (Word products), a card on products.html, a row in
data/search-index.json, a URL in sitemap.xml and a line in the order handler's FILES.
It also lifts the Evaluation Essentials Kit from 27 products to 30 everywhere the
number is written. It never uploads a file: the paid files go to the private
`products` bucket only after the [LEGAL CHECK] notes in them are cleared.
"""
import copy
import re
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

TEMPLATE = ROOT / "products" / "mel-plan" / "index.html"
OLD_N, NEW_N = 27, 30
TODAY = "2026-10-21"

PRODUCTS = [
    dict(
        slug="bid-no-bid-scorecard",
        title="Bid or No-Bid Scorecard",
        form_title="Bid or No-Bid Scorecard",
        file="ImpactMojo-Bid-No-Bid-Scorecard.zip",
        ext="XLSX",
        eyebrow="Template · XLSX",
        crumb="Template",
        meta="An Excel scorecard that tells you whether to bid on a terms of reference: eight weighted criteria, four knockout checks, clarification questions and a cost-of-bidding test, with a Word guide. ₹199.",
        og="Decide whether to bid on a ToR before you spend days on the proposal. Excel scorecard and Word guide. ₹199.",
        lede="Score a terms of reference before you spend days on a proposal. Eight weighted criteria, four knockout checks, the questions to send the client, and a test of whether the bid pays for itself.",
        note="Editable XLSX workbook + a Word guide · delivered to your inbox within 24 hours of payment.",
        letter_h="Why this matters",
        letter=[
            "A serious proposal takes days of unpaid work. Most of the assignments that cost an evaluator money were visible in the ToR: a question set nobody could answer, a budget half the size of the work, a payment clause that left the fieldwork unfunded.",
            "This workbook turns that early warning into a number. You score eight criteria from 1 to 5, answer four knockout checks, and read a decision: go, go with conditions or no-bid. Every low score becomes a clarification question you can send to the client before the deadline. A second sheet tests whether the expected return on a bid covers its cost, and a log records every decision so that after ten bids you can see your own pattern.",
            'It is written for the evaluator or consultant who receives the ToR. If you are the one writing a ToR, the <a href="/products/tor-template/">ToR Template</a> and the <a href="/products/proposal-scoring/">Proposal Scoring Rubric</a> are the other side of this table.',
        ],
        inside=[
            "A scorecard with eight weighted criteria, live formulas and a decision cell",
            "Four knockout checks that end the discussion whatever the score",
            "Clarification questions that write themselves for every criterion scored 1 or 2",
            "A cost-of-bidding sheet: expected value, and the win chance you need to break even",
            "A bid log that tracks your win rate and your no-bids",
            "A Word guide: what a 1, a 3 and a 5 look like, eleven red-flag ToR clauses with the question to ask for each, and a worked example",
        ],
        sample=[
            ("Criteria and weights", "eight criteria, weights that add to 100"),
            ("Knockout checks", "any Yes means no-bid"),
            ("Decision", "GO, GO WITH CONDITIONS or NO-BID, calculated for you"),
            ("Cost of bidding", "expected value and the win chance you need"),
        ],
        sample_file=None,
        faq=[
            ("What format is it?", "An Excel workbook (.xlsx) with live formulas, plus a Word guide. It also opens in Google Sheets and LibreOffice."),
            ("Can I change the weights and thresholds?", "Yes. The weights and the two thresholds are yellow cells you can edit. Set them before you score, so the number cannot be bent to fit a decision you have already made."),
            ("Does it work for public tenders?", "It works for any terms of reference. For a public tender, read the eligibility, earnest money and performance security rules in the tender document before you score."),
            ("How fast is delivery?", "Within 24 hours of confirming payment, usually much sooner."),
        ],
        search_desc="An Excel scorecard that decides whether to bid on a ToR: eight weighted criteria, four knockout checks, clarification questions, a cost-of-bidding test and a bid log. Ships with a Word guide and a worked example. Buy for ₹199 via UPI.",
        search_tags=["template", "bid", "no-bid", "tor", "tender", "consulting", "evaluation", "Excel", "premium", "paid", "₹199"],
        search_id="PROD-BID-NO-BID",
        card="Bid or No-Bid Scorecard",
        card_p="Score a ToR before you write the proposal.",
        before="Stakeholder Map",
    ),
    dict(
        slug="sow-change-request-template",
        title="Statement of Work & Change Request Template",
        form_title="Statement of Work & Change Request Template",
        file="ImpactMojo-SOW-Change-Request-Template.docx",
        ext="DOCX",
        eyebrow="Template · DOCX",
        crumb="Template",
        meta="An annotated statement of work for evaluators, with a change request form, a clause bank and a worked example. Settle scope, review rounds, payment and change control before the work starts. ₹199.",
        og="An annotated statement of work and change request form for evaluators. ₹199.",
        lede="Settle scope, review rounds, payment and change control before the work starts. An annotated statement of work, a one-page change request form, a clause bank and a worked example.",
        note="Editable DOCX file · delivered to your inbox within 24 hours of payment.",
        letter_h="Why the contract is where scope is won or lost",
        letter=[
            "Most disputes in an evaluation assignment are about one of four things: what was included, how many rounds of comments there would be, when the money was due, and who had the last word on the findings. Each can be settled in an afternoon before signing. After signing, each takes weeks and costs goodwill.",
            "This pack is the evaluator's side of the contract. It gives you a thirteen-section statement of work with guidance under every section, a change request form that turns extra work into a priced decision, and plain-language clauses to adapt for acceptance, independence, late payment, data handling and the use of AI tools.",
            'It pairs with the <a href="/products/bid-no-bid-scorecard/">Bid or No-Bid Scorecard</a> before you bid and the <a href="/products/inception-report-template/">Inception Report &amp; Evaluation Matrix Template</a> after you sign. The <a href="/products/tor-template/">ToR Template</a> is the commissioner\'s side of the same table.',
        ],
        inside=[
            "A thirteen-section annotated statement of work, each section with guidance, what good looks like and the mistakes to avoid",
            "A one-page change request form, so every extra task has days, a fee and a signature",
            "A clause bank in plain language: change control, acceptance, independence, late client inputs, late payment, early termination, data handling and AI use",
            "A payment-milestone chooser with a cash test",
            "Ten questions to ask when the client sends its own contract",
            "A worked example from the maternal and newborn health case, with a priced change request",
        ],
        sample=[
            ("3. Scope: in and out", "write down what sits outside the work"),
            ("4. Deliverables and schedule", "length, format, review rounds and due date"),
            ("8. Fees and payment milestones", "payments tied to submission"),
            ("10. Change control", "extra work becomes a priced decision"),
        ],
        sample_file="ImpactMojo-SOW-Change-Request-Template-SAMPLE.docx",
        faq=[
            ("What format is it?", "An editable DOCX file that opens in Microsoft Office, Google, LibreOffice and Pages."),
            ("Is it legal advice?", "It is a drafting aid. Where a statute, a tax rule or your client's own contract changes the answer, the file says so and tells you what to confirm. Have a lawyer read the final contract."),
            ("Can I use it if the client sends its own contract?", "Yes. Use the thirteen sections as a checklist and the ten questions in Part C as a list to raise before you sign."),
            ("How fast is delivery?", "Within 24 hours of confirming payment, usually much sooner."),
        ],
        search_desc="An annotated statement of work for evaluators with a change request form, a clause bank, a payment-milestone chooser and a worked example. Settle scope, review rounds, payment and change control before the work starts. Buy for ₹199 via UPI.",
        search_tags=["template", "statement of work", "SOW", "change request", "contract", "consulting", "evaluation", "premium", "paid", "₹199"],
        search_id="PROD-SOW-CHANGE",
        card="Statement of Work &amp; Change Request",
        card_p="Scope, review rounds, payment and change control.",
        before="Survey Instrument",
    ),
    dict(
        slug="inception-report-template",
        title="Inception Report & Evaluation Matrix Template",
        form_title="Inception Report & Evaluation Matrix Template",
        file="ImpactMojo-Inception-Report-Template.docx",
        ext="DOCX",
        eyebrow="Template · DOCX",
        crumb="Template",
        meta="An annotated inception report for evaluators, with an evaluation matrix guide, a sample-size method, a client sign-off checklist and a worked example. Turn a bid into a plan before any data is collected. ₹199.",
        og="An annotated inception report with an evaluation matrix guide and a sample-size method. ₹199.",
        lede="Turn a bid into a plan before any data is collected. An annotated inception report, an evaluation matrix guide, a sample-size method you can reproduce, a sign-off checklist for the client and a worked example.",
        note="Editable DOCX file · delivered to your inbox within 24 hours of payment.",
        letter_h="What the inception report settles",
        letter=[
            "The inception report is where an evaluation is won or lost quietly. It confirms the questions, shows how each will be answered, and gives the client a chance to correct a misunderstanding while the correction costs a conversation. After fieldwork the same correction costs a second round of surveys.",
            "This pack walks you through thirteen sections, from the changes since your bid to an outline of the final report written as headlines to test. The evaluation matrix has its own guide, with a weak entry and a stronger entry for every column. The sample-size section shows the arithmetic in steps, with a lookup table, so the client can check every number.",
            'It follows the <a href="/products/sow-change-request-template/">Statement of Work &amp; Change Request Template</a> and works with the <a href="/products/survey-instrument/">Survey Instrument Template</a>, the <a href="/products/fgd-guide/">FGD Facilitator\'s Guide</a> and the <a href="/products/data-consent/">Data Management &amp; Consent Pack</a>, which hold the tools it refers to.',
        ],
        inside=[
            "A thirteen-section annotated inception report, from changes since the bid to the outline of the final report",
            "An evaluation matrix guide, column by column, with weak and stronger entries",
            "A sample-size method for comparing two proportions, with every step shown and a lookup table",
            "An evidence-strength scale: strong, moderate and limited, with the wording to use in the report",
            "A ten-question checklist the client can use to approve the report",
            "A worked example from the maternal and newborn health case: matrix, sample, risks and report headlines",
        ],
        sample=[
            ("4. Evaluation matrix", "question, criterion, indicator, source, method, analysis"),
            ("6. Sampling and sample size", "every assumption stated and sourced"),
            ("12. Limitations", "tell the client now what the evaluation cannot say"),
            ("13. Outline of the final report", "headlines to test, not conclusions"),
        ],
        sample_file="ImpactMojo-Inception-Report-Template-SAMPLE.docx",
        faq=[
            ("What format is it?", "An editable DOCX file that opens in Microsoft Office, Google, LibreOffice and Pages."),
            ("Does it help with sample size?", "Yes. Part C gives a step-by-step method for comparing two proportions, with a lookup table, and Part D works one example from start to finish. It gives a planning figure. Take the final design to a statistician."),
            ("Which designs does it suit?", "Mixed-methods and outcome evaluations of programmes, with or without a comparison group. The worked example combines difference-in-differences on monitoring data with a household survey."),
            ("How fast is delivery?", "Within 24 hours of confirming payment, usually much sooner."),
        ],
        search_desc="An annotated inception report for evaluators with an evaluation matrix guide, a step-by-step sample-size method, an evidence-strength scale, a client sign-off checklist and a worked example. Buy for ₹199 via UPI.",
        search_tags=["template", "inception report", "evaluation matrix", "sample size", "consulting", "evaluation", "premium", "paid", "₹199"],
        search_id="PROD-INCEPTION",
        card="Inception Report &amp; Evaluation Matrix",
        card_p="Turn a bid into a plan before fieldwork.",
        before="Stakeholder Map",
    ),
]


def esc(t):
    return t.replace("&", "&amp;")


def title_attr(p):
    return esc(p["title"])


def page(p):
    t = TEMPLATE.read_text(encoding="utf-8")
    head, rest = t.split('<main class="wrap" id="main">', 1)
    tail = rest[rest.index("</main>"):]

    name = title_attr(p)
    # head: title, then the share block (build-social-tags.py redraws the card and image tags)
    head = re.sub(r"<title>.*?</title>", f"<title>{name}: ₹199 | ImpactMojo</title>", head, flags=re.S)
    url = f"https://www.impactmojo.in/products/{p['slug']}/"
    share = (
        "<!-- share:start -->\n"
        f'<link rel="canonical" href="{url}">\n'
        f'<meta name="description" content="{esc(p["meta"])}">\n'
        '<meta property="og:type" content="product">\n'
        '<meta property="og:site_name" content="ImpactMojo">\n'
        f'<meta property="og:title" content="{name} | ImpactMojo">\n'
        f'<meta property="og:description" content="{esc(p["og"])}">\n'
        f'<meta property="og:url" content="{url}">\n'
        '<meta name="twitter:card" content="summary_large_image">\n'
        f'<meta name="twitter:title" content="{name} | ImpactMojo">\n'
        f'<meta name="twitter:description" content="{esc(p["og"])}">\n'
        "<!-- share:end -->"
    )
    head = re.sub(r"<!-- share:start -->.*?<!-- share:end -->", lambda m: share, head, flags=re.S)

    paras = "".join(f"<p>{x}</p>" for x in p["letter"] if "<a " not in x)
    pairs = "".join(f'<p class="note" style="margin-top:.6rem">{x}</p>' for x in p["letter"] if "<a " in x)
    inside = "".join(f"<li>{esc(x)}</li>" for x in p["inside"])
    sample = "".join(
        f'<h3>{esc(h)}</h3><div class="g">➤ {esc(g)}</div><div class="ln"></div><div class="ln"></div>' for h, g in p["sample"]
    )
    if p["sample_file"]:
        fade = f'<div class="fade"><a class="btn ghost" href="/downloads/samples/{p["sample_file"]}" download>Download watermarked sample</a></div>'
    else:
        fade = '<div class="fade"><span class="note">Full preview above: clean editable file sent after purchase.</span></div>'
    faq = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in p["faq"])
    qr = f"upi-{p['slug']}-199.png"

    main = f"""<main class="wrap" id="main">
<div class="crumb"><a href="/products.html">Products</a> › {p['crumb']} › {name}</div>
<span class="eyebrow">{p['eyebrow']}</span>
<h1 class="title">{name}</h1>
<p class="lede">{esc(p['lede'])}</p>
<div class="buybar"><span class="price">₹199</span><a class="btn buy" href="#buy">Buy now →</a><a class="btn ghost" href="#sample">See sample</a></div>
<p class="note im-prod-sep" style="margin:.3rem 0 .8rem">Products are sold separately and are not included in Membership. <a href="/premium.html">See what Membership covers</a>.</p>
<p class="note">{p['note']}</p>
<section class="blk letter"><h2>{esc(p['letter_h'])}</h2>{paras}{pairs}</section>
<section class="blk"><h2>What's inside</h2><ul class="checklist">{inside}</ul></section>
<section class="blk" id="sample"><h2>Sample</h2><p class="note" style="margin-bottom:.7rem">The real file, watermarked. What you receive after payment is clean and fully editable.</p>
<div class="sample"><div class="pg"><div style="font-family:Inter;font-weight:700;color:#0369A1">ImpactMojo</div>
<div style="font-family:Inter;font-weight:800;font-size:1.3rem;margin:.2rem 0">{name}</div>{sample}</div>
{fade}</div></section>
<section class="blk" id="buy"><h2>Buy it: ₹199</h2><div class="pay">
<div class="card"><h3 style="font-size:1.05rem;margin-bottom:.2rem">Pay by UPI</h3><p class="note">Scan the code, or pay to the UPI ID below (₹199).</p>
<div class="upi-id"><span id="upi">impactmojo@ibl</span><button onclick="copyUPI()">Copy</button></div>
<img class="qr" src="/assets/images/upi/{qr}" alt="UPI QR to pay ₹199 to impactmojo@ibl">
<p style="margin-top:.6rem"><button class="btn ghost" onclick="waOrder()" style="font-size:.85rem">Order on WhatsApp instead</button></p></div>
<div class="card"><h3 style="font-size:1.05rem;margin-bottom:.2rem">Confirm your order</h3><p class="note">Paid? Tell us where to send the file. Delivered within 24 hours.</p>
<form name="product-order" method="POST" data-netlify="true" netlify-honeypot="bot-field" onsubmit="return submitOrder(event)">
<input type="hidden" name="form-name" value="product-order"><input type="hidden" name="product" value="{name} (₹199)">
<p style="display:none"><label>Don't fill: <input name="bot-field"></label></p>
<div class="field"><label for="nm">Name</label><input id="nm" name="name" required></div>
<div class="field"><label for="em">Email (where we'll send the file)</label><input id="em" type="email" name="email" required></div>
<div class="field"><label for="ref">UPI transaction / reference no.</label><input id="ref" name="upi_ref" required></div>
<button class="btn buy" type="submit" style="width:100%;justify-content:center">I've paid: send my file</button>
<div class="ok-msg" id="okMsg">✓ Order received. We'll verify the payment and email your file within 24 hours.</div></form></div></div></section>
<section class="blk"><h2>How delivery works</h2><ol class="steps">
<li>Pay ₹199 by UPI (scan the QR or use <span class="mono">impactmojo@ibl</span>), or order on WhatsApp.</li>
<li>Fill the short form with your email and the UPI reference.</li>
<li>We confirm payment and email your clean, editable file: within 24 hours.</li></ol>
<p class="note">Questions? <a href="/contact.html">Contact us</a>. Refunds per our <a href="/refund-policy.html">refund policy</a>.</p></section>
<section class="blk"><div class="upsell"><div style="flex:1;min-width:240px"><div class="eyebrow" style="margin-bottom:.3rem">Part of the kit</div>
<h3 style="font-size:1.15rem">Get the whole Evaluation Essentials Kit</h3><p class="note">This file is also in the Evaluation Essentials Kit, which holds all {NEW_N} ImpactMojo products for ₹2,499.</p></div>
<a class="btn buy" href="/products/evaluation-essentials-kit/">See the kit →</a></div></section>
<section class="blk faq"><h2>FAQ</h2>
{faq}</section>
"""
    tail = tail.replace("I'd like to buy: MEL Plan Template (₹199)", f"I'd like to buy: {p['title']} (₹199)")
    return head + main + tail


def qr(p):
    import qrcode

    tn = quote("ImpactMojo " + p["title"], safe="")
    data = f"upi://pay?pa=impactmojo@ibl&pn=ImpactMojo&am=199&cu=INR&tn={tn}"
    img = qrcode.make(data, box_size=8, border=4).convert("1")
    out = ROOT / "assets" / "images" / "upi" / f"upi-{p['slug']}-199.png"
    img.save(out)
    return data


def sample(p, build_dir):
    """Cut the first blocks of the built Word file and wrap them in a preview notice."""
    if not p["sample_file"]:
        return
    from docx import Document
    from docx.shared import Pt, RGBColor

    d = Document(str(Path(build_dir) / p["file"]))
    body = d.element.body
    kids = [k for k in body.iterchildren() if not k.tag.endswith("sectPr")]
    keep = 34
    for k in kids[keep:]:
        body.remove(k)
    first = d.paragraphs[0] if d.paragraphs else None
    note = d.add_paragraph()
    r = note.add_run(f"SAMPLE: preview only. This is the opening of the full pack, from impactmojo.in/products/{p['slug']}/")
    r.bold = True
    r.font.size = Pt(9)
    r.font.color.rgb = RGBColor(0xB4, 0x23, 0x18)
    end = d.add_paragraph()
    r = end.add_run("Sample ends here. The full pack and its worked example arrive clean and fully editable after purchase.")
    r.italic = True
    r.font.size = Pt(9)
    sect = body.find("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}sectPr")
    # move the notice to the top, the closing line to the end (before sectPr)
    body.remove(note._p)
    body.insert(0, note._p)
    body.remove(end._p)
    if sect is not None:
        sect.addprevious(end._p)
    d.save(str(ROOT / "downloads" / "samples" / p["sample_file"]))


def replace_once(path, old, new, count=1):
    s = path.read_text(encoding="utf-8")
    if old not in s:
        raise SystemExit(f"{path}: expected text not found: {old[:70]!r}")
    path.write_text(s.replace(old, new, count), encoding="utf-8")


def products_html():
    path = ROOT / "products.html"
    s = path.read_text(encoding="utf-8")
    a = s.index('<h2 class="anchor">Templates</h2>')
    grid_start = s.index('<div class="dl-grid">', a)
    grid_end = s.index("</div>\n        </div>", grid_start) if "</div>\n        </div>" in s[grid_start:] else None
    # cards are one per line
    lines = s[grid_start:].split("\n")
    out, i = [], 0
    new_cards = {}
    for p in PRODUCTS:
        if f'href="/products/{p["slug"]}/"' in s:
            continue
        ext = p["ext"]
        new_cards[p["before"]] = new_cards.get(p["before"], []) + [
            f'            <div class="dl"><span class="ext {ext.lower()}">{ext}</span><h3>{p["card"]}</h3><p>{esc(p["card_p"])}</p><div class="dlmeta">{ext} · ₹199</div>'
            f'<a class="dlbtn" href="/products/{p["slug"]}/">{{SVG}}View product</a></div>'
        ]
    # take the SVG markup from an existing card
    m = re.search(r'<a class="dlbtn" href="/products/tor-template/">(<svg.*?</svg>)View product</a>', s, flags=re.S)
    svg = m.group(1)
    for key in list(new_cards):
        new_cards[key] = [c.replace("{SVG}", svg) for c in new_cards[key]]
    done = set()
    res = []
    inside = False
    for ln in s.split("\n"):
        if "<h2 class=\"anchor\">Templates</h2>" in ln:
            inside = True
        elif inside and "<h2 class=\"anchor\">Workbooks</h2>" in ln:
            inside = False
        if inside:
            m2 = re.search(r'<div class="dl">.*?<h3>(.*?)</h3>', ln)
            if m2:
                for key, cards in new_cards.items():
                    if key == m2.group(1) and key not in done:
                        res.extend(cards)
                        done.add(key)
        res.append(ln)
    if len(done) != len(new_cards) and new_cards:
        raise SystemExit("products.html: could not place all cards: " + ", ".join(set(new_cards) - done))
    s = "\n".join(res)
    s = s.replace(f"All {OLD_N} products", f"All {NEW_N} products")
    path.write_text(s, encoding="utf-8")


def search_index():
    path = ROOT / "data" / "search-index.json"
    s = path.read_text(encoding="utf-8")
    m = re.search(r'(\n  \{\n    "id": "PROD-TOR-TEMPLATE".*?\n  \},?)', s, flags=re.S)
    ex = m.group(1)
    indent_probe = re.search(r'\n( +)"id"', ex).group(1)
    import json

    def block(p):
        d = {
            "id": p["search_id"],
            "title": p["title"],
            "description": p["search_desc"],
            "type": "product",
            "category": "Templates",
            "url": f"/products/{p['slug']}/",
            "tags": p["search_tags"],
            "price": "₹199",
        }
        body = json.dumps(d, ensure_ascii=False, indent=2)
        return "\n".join("  " + ln for ln in body.split("\n"))

    add = "".join(",\n" + block(p) for p in PRODUCTS if p["search_id"] not in s)
    if add:
        end = m.end()
        # the matched block may or may not end with a comma; insert after its closing brace
        close = s.index("}", m.start(1) + ex.rindex("}"))
        s = s[: close + 1] + add + s[close + 1:]
    s = s.replace(f"All {OLD_N} ImpactMojo products", f"All {NEW_N} ImpactMojo products")
    path.write_text(s, encoding="utf-8")
    json.loads(s)  # must stay valid


def sitemap():
    path = ROOT / "sitemap.xml"
    lines = path.read_text(encoding="utf-8").split("\n")
    for p in PRODUCTS:
        loc = f"https://www.impactmojo.in/products/{p['slug']}/"
        if any(loc in ln for ln in lines):
            continue
        new = f"  <url><loc>{loc}</loc><lastmod>{TODAY}</lastmod></url>"
        idx = None
        for i, ln in enumerate(lines):
            m = re.search(r"<loc>https://www\.impactmojo\.in/products/([^<]+)/</loc>", ln)
            if m and m.group(1) > p["slug"] and "notes-101" not in m.group(1):
                idx = i
                break
        lines.insert(idx if idx is not None else len(lines) - 1, new)
    path.write_text("\n".join(lines), encoding="utf-8")


def handler():
    path = ROOT / "netlify" / "functions" / "submission-created.mjs"
    s = path.read_text(encoding="utf-8")
    anchor = '  "Evaluation Essentials Kit": "ImpactMojo-Evaluation-Essentials-Kit.zip",\n'
    add = ""
    for p in PRODUCTS:
        key = p["form_title"]
        if f'"{key}"' not in s:
            add += f'  "{key}": "{p["file"]}",\n'
    if add:
        s = s.replace(anchor, anchor + add, 1)
    path.write_text(s, encoding="utf-8")


def kit_page():
    path = ROOT / "products" / "evaluation-essentials-kit" / "index.html"
    s = path.read_text(encoding="utf-8")
    s = s.replace(f"all {OLD_N} ImpactMojo products", f"all {NEW_N} ImpactMojo products")
    s = s.replace(f"Bundle · {OLD_N} products", f"Bundle · {NEW_N} products")
    s = s.replace(f"What's inside: all {OLD_N} products", f"What's inside: all {NEW_N} products")
    s = s.replace("<s>₹6,373</s>", "<s>₹6,970</s>")
    s = s.replace("all 12 templates, all four workbooks, both trainer decks", "all 15 templates, all four workbooks, both trainer decks")
    if "evaluator's side is in the kit too" not in s:
      s = s.replace(
        "Buy them as a set and you have the whole pipeline.</p>",
        "Buy them as a set and you have the whole pipeline. The evaluator's side is in the kit too: the <strong>bid or no-bid scorecard</strong> decides whether to bid, the <strong>statement of work</strong> fixes scope and payment, and the <strong>inception report</strong> turns the bid into a plan.</p>",
        1,
    )
    s = s.replace("The five Excel templates each come with a Word companion guide", "The six Excel templates each come with a Word companion guide")
    for item in ("Bid or No-Bid Scorecard", "Statement of Work & Change Request Template", "Inception Report & Evaluation Matrix Template"):
        if f"<li>{item}</li>" not in s and f"<li>{esc(item)}</li>" not in s:
            s = s.replace("<li>Data Management & Consent Pack</li></ul>", f"<li>Data Management & Consent Pack</li><li>{esc(item)}</li></ul>", 1) if "<li>Data Management & Consent Pack</li></ul>" in s else s.replace("<li>Data Management &amp; Consent Pack</li></ul>", f"<li>Data Management &amp; Consent Pack</li><li>{esc(item)}</li></ul>", 1)
    path.write_text(s, encoding="utf-8")
    # the other pages that offer the kit, and the runbook
    for f in (ROOT / "products").glob("*/index.html"):
        t = f.read_text(encoding="utf-8")
        if f"All {OLD_N} products (every template" in t:
            f.write_text(t.replace(f"All {OLD_N} products (every template", f"All {NEW_N} products (every template"), encoding="utf-8")
    rb = ROOT / "ops" / "money-flow-runbook.md"
    t = rb.read_text(encoding="utf-8")
    t = t.replace("| 27 one-time products", f"| {NEW_N} one-time products").replace("Evaluation Essentials Kit (all 27)", f"Evaluation Essentials Kit (all {NEW_N})").replace("(all 27 + bundle", f"(all {NEW_N} + bundle")
    rb.write_text(t, encoding="utf-8")


def main(build_dir):
    for p in PRODUCTS:
        d = ROOT / "products" / p["slug"]
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(page(p), encoding="utf-8")
        print("page   ", p["slug"], "|", qr(p))
        sample(p, build_dir)
    products_html()
    search_index()
    sitemap()
    handler()
    kit_page()
    print("done: now run build-social-tags.py, render-social-cards.mjs and the checks")


if __name__ == "__main__":
    main(sys.argv[1])
