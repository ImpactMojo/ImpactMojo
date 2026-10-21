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
OLD_N, NEW_N = 30, 45
TODAY = "2026-10-21"

def _load_products():
    """The fifteen further templates: each t_*.py module carries its own PAGE."""
    import build_more

    out = []
    for m in build_more.load():
        d = dict(m.PAGE)
        d.setdefault("form_title", d["title"])
        out.append(d)
    return out


PRODUCTS = _load_products()


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
        if idx is None:
            last = max(i for i, ln in enumerate(lines) if re.search(r"<loc>https://www\.impactmojo\.in/products/(?!notes-101)[^<]+/</loc>", ln))
            idx = last + 1
        lines.insert(idx, new)
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
    s = s.replace("<s>₹6,970</s>", "<s>₹9,955</s>")
    s = s.replace("all 15 templates, all four workbooks, both trainer decks", "all 30 templates, all four workbooks, both trainer decks")
    s = s.replace("The six Excel templates each come with a Word companion guide", "The eleven Excel templates each come with a Word companion guide")
    marker = "The rest of the evaluator's desk is in the kit too"
    if marker not in s:
        s = s.replace(
            "Buy them as a set and you have the whole pipeline.",
            "Buy them as a set and you have the whole pipeline. " + marker + ": the clarification letter, three-option offer, engagement charter, invoice pack, kick-off workplan, RAID log, weekly status note, evidence strength rating, storyline, validation workshop plan, prioritisation, management response tracker, after-action review, client feedback survey and case study with consent.",
            1,
        )
    a = s.index("<h3 style=\"margin:.9rem 0 .3rem;font-size:1rem\">Templates")
    end = s.index("</ul>", a)
    items = ""
    for p in PRODUCTS:
        li = f"<li>{esc(p['title'])}</li>"
        if li not in s:
            items += li
    s = s[:end] + items + s[end:]
    path.write_text(s, encoding="utf-8")
    for f in (ROOT / "products").glob("*/index.html"):
        t = f.read_text(encoding="utf-8")
        if f"All {OLD_N} products (every template" in t:
            f.write_text(t.replace(f"All {OLD_N} products (every template", f"All {NEW_N} products (every template"), encoding="utf-8")
    rb = ROOT / "ops" / "money-flow-runbook.md"
    t = rb.read_text(encoding="utf-8")
    t = t.replace(f"| {OLD_N} one-time products", f"| {NEW_N} one-time products").replace(f"Evaluation Essentials Kit (all {OLD_N})", f"Evaluation Essentials Kit (all {NEW_N})").replace(f"(all {OLD_N} + bundle", f"(all {NEW_N} + bundle")
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
