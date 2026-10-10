#!/usr/bin/env python3
"""Write the shop for the 101 Course Notes from the deck list.

    python3 scripts/course-notes/build-101-shop.py          # write
    python3 scripts/course-notes/build-101-shop.py --check  # CI: fail on drift

Every 101 deck has a printable notes PDF (render-101.mjs), sold at ₹149.
Eighty products are too many to keep in step by hand, so this writes all of
them from data/decks.json and data/course-notes-101.json (page counts from
the last render):

  products/notes-101/index.html           the catalogue, one row per deck
  products/notes-101/<slug>/index.html    one buy page per deck
  netlify/functions/submission-created.mjs  the FILES lines between the
                                          101-notes markers
  sitemap.xml and data/search-index.json  one entry per page
  101-courses/<slug>.html                 a buy link on the title slide and
                                          in the slide controls, between
                                          notes-101 markers

A deck added to decks.json without a render fails here, so nothing is put on
sale that the order handler cannot deliver.
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRICE = 149
QR = "/assets/images/upi/upi-notes-101-149.png"
TEMPLATE = ROOT / "products" / "notes-nothing-about-us" / "index.html"
HANDLER = ROOT / "netlify" / "functions" / "submission-created.mjs"
START, END = "  // 101-notes:start (written by build-101-shop.py)\n", "  // 101-notes:end\n"
E = html.escape

# What the builder adds to each deck. Everything sits between markers so a
# re-run replaces it rather than stacking a second copy.
DECK_CSS = ('<style id="notes-101">'
            '.title-tag.notes-buy{color:#fff;text-decoration:none;border-color:#38BDF8;background:rgba(14,165,233,0.22)}'
            '.title-tag.notes-buy:hover,.title-tag.notes-buy:focus-visible{background:rgba(14,165,233,0.4)}'
            '#nav .nav-notes{color:#fff;text-decoration:none;font-family:var(--font-mono);font-size:10px;letter-spacing:0.6px;'
            'text-transform:uppercase;padding:6px 10px;border-radius:14px;background:rgba(255,255,255,0.1);white-space:nowrap}'
            '#nav .nav-notes:hover,#nav .nav-notes:focus-visible{background:rgba(255,255,255,0.2)}'
            '@media print{.notes-buy{display:none !important}}'
            '</style>\n')
MARK = re.compile(r"<!--notes-101-->.*?<!--/notes-101-->", re.S)
CSS_MARK = re.compile(r'<style id="notes-101">.*?</style>\n')


def deck_with_link(text, slug, title):
    """The deck's HTML with its notes link, or None if it has nowhere to put it."""
    url = f"/products/notes-101/{slug}/"
    text = CSS_MARK.sub("", MARK.sub("", text))
    tags = '<div class="title-tags">'
    nav = text.find('<div id="nav"')
    if tags not in text or nav < 0 or "</head>" not in text:
        return None
    label = E(f"Buy the {title} course notes, a printable PDF, for ₹{PRICE}")
    text = text.replace(tags, tags + f'<!--notes-101--><a class="title-tag notes-buy" href="{url}" aria-label="{label}">Course Notes PDF &middot; ₹{PRICE}</a><!--/notes-101-->', 1)
    nav = text.find('<div id="nav"')
    close = text.find("</div>", nav)
    text = text[:close] + f'<!--notes-101--> <a class="nav-notes notes-buy" href="{url}" aria-label="{label}">Notes ₹{PRICE}</a>\n<!--/notes-101-->' + text[close:]
    return text.replace("</head>", DECK_CSS + "</head>", 1)


def title_of(d):
    return html.unescape(d["title"])


def page(d, n):
    """One buy page."""
    t, slug = title_of(d), d["slug"]
    desc = html.unescape(d.get("desc", ""))
    secs = [html.unescape(s) for s in d.get("sections", [])]
    product = f"{t}, Course Notes (₹{PRICE})"
    meta = f"{t} as printable course notes: all {d['slides']} slides, two to an A4 page with space for notes, {n} pages. ₹{PRICE} via UPI."
    items = "\n".join(f"      <li>{E(s)}</li>" for s in secs)
    return f'''<main class="wrap" id="main">
  <div class="crumb"><a href="/products.html">Products</a> › <a href="/products/notes-101/">101 Course Notes</a> › {E(t)}</div>
  <span class="eyebrow">Course Notes · PDF · {d['slides']} slides</span>
  <h1 class="title">{E(t)}: course notes</h1>
  <p class="lede">{E(desc)} This is the whole <a href="{E(d['url'])}">{E(t)}</a> deck as an A4 document: every slide, two to a page, with ruled space under each pair to write your own notes.</p>
  <div class="buybar">
    <span class="price">₹{PRICE}</span>
    <a class="btn buy" href="#buy">Buy now →</a>
    <a class="btn ghost" href="#inside">See what's inside</a>
  </div>
  <p class="note">PDF · {d['slides']} slides · {n} pages · delivered to your inbox within 24 hours of payment. The deck stays <a href="{E(d['url'])}">free to study online</a>; this is the copy to print and keep.</p>
  <div class="statgrid"><div class="s"><b>{d['slides']}</b> slides</div><div class="s"><b>{len(secs)}</b> sections</div><div class="s"><b>2</b> slides a page</div><div class="s">ruled <b>notes</b> space</div><div class="s"><b>Print-ready</b> A4</div></div>

  <section class="blk" id="inside">
    <h2>What's inside: {len(secs)} sections</h2>
    <ul class="checklist">
{items}
    </ul>
    <p style="margin-top:1rem">Diagrams and charts print as they appear in the deck, in colour, with text you can search and copy.</p>
  </section>

  <section class="blk" id="buy">
    <h2>Buy it: ₹{PRICE}</h2>
    <div class="pay">
      <div class="card">
        <h3 style="font-size:1.05rem;margin-bottom:.2rem">Pay by UPI</h3>
        <p class="note">Scan the code, or pay to the UPI ID below (amount ₹{PRICE}).</p>
        <div class="upi-id"><span id="upi">impactmojo@ibl</span><button onclick="copyUPI()">Copy</button></div>
        <img class="qr" src="{QR}" alt="UPI QR to pay ₹{PRICE} to impactmojo@ibl">
        <p class="note" style="margin-top:.5rem">Add your email in the payment note, or fill the form so we know where to send it.</p>
        <p style="margin-top:.6rem"><button class="btn ghost" id="waBtn" onclick="waOrder()" style="font-size:.85rem">Order on WhatsApp instead</button></p>
      </div>
      <div class="card">
        <h3 style="font-size:1.05rem;margin-bottom:.2rem">Confirm your order</h3>
        <p class="note">Paid? Tell us where to send the PDF. Delivered within 24 hours.</p>
        <form name="product-order" method="POST" data-netlify="true" netlify-honeypot="bot-field" onsubmit="return submitOrder(event)">
          <input type="hidden" name="form-name" value="product-order">
          <input type="hidden" name="product" value="{E(product)}">
          <p style="display:none"><label>Don't fill: <input name="bot-field"></label></p>
          <div class="field"><label for="nm">Name</label><input id="nm" name="name" required></div>
          <div class="field"><label for="em">Email (where we'll send the PDF)</label><input id="em" type="email" name="email" required></div>
          <div class="field"><label for="ref">UPI transaction / reference no.</label><input id="ref" name="upi_ref" placeholder="e.g. 4xxxxxxxxxxx" required></div>
          <button class="btn buy" type="submit" style="width:100%;justify-content:center">I've paid: send my notes</button>
          <div class="ok-msg" id="okMsg">✓ Order received. We'll verify the payment and email your PDF within 24 hours.</div>
        </form>
      </div>
    </div>
  </section>

  <section class="blk faq">
    <h2>FAQ</h2>
    <details><summary>What exactly do I get?</summary><p>One A4 PDF of {n} pages: a cover with the course outline, then all {d['slides']} slides of the deck, two to a page, with ruled space under each pair for your notes.</p></details>
    <details><summary>Isn't the deck free?</summary><p>Yes. <a href="{E(d['url'])}">Every slide is free online</a> and will stay free. The PDF is the version to print, annotate and keep offline.</p></details>
    <details><summary>How fast is delivery?</summary><p>Within 24 hours of confirming payment, usually sooner. We check the UPI reference, then email you a private download link.</p></details>
    <details><summary>Can I share it?</summary><p>It is for your own and your organisation's learning: print it and use it in training. The slides carry a CC BY-NC-ND 4.0 licence, so please don't resell or repost the file.</p></details>
  </section>
</main>''', meta, product


def wrap(tpl, title, meta, url, main, wa):
    s = tpl
    s = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{E(meta)}">', s)
    s = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{E(title)} | ImpactMojo">', s)
    s = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{E(meta)}">', s)
    s = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="https://www.impactmojo.in{url}">', s)
    s = re.sub(r"<title>[^<]*</title>", f"<title>{E(title)} | ImpactMojo</title>", s)
    s = re.sub(r'<main class="wrap" id="main">.*?</main>', lambda m: main, s, flags=re.S)
    s = re.sub(r'var msg=encodeURIComponent\("[^"]*"\);', lambda m: "var msg=encodeURIComponent(" + json.dumps(wa, ensure_ascii=False) + ");", s)
    return s


def index_page(rows, pages):
    trs = "\n".join(
        f'      <tr data-q="{E((title_of(d) + " " + " ".join(html.unescape(x) for x in d.get("sections", []))).lower())}"><td><a href="/products/notes-101/{d["slug"]}/">{E(title_of(d))}</a></td><td>{d["slides"]}</td><td>{pages[d["slug"]]}</td><td><a class="btn ghost sm" href="/products/notes-101/{d["slug"]}/#buy">Buy ₹{PRICE}</a></td></tr>'
        for d in rows)
    return f'''<main class="wrap" id="main">
  <div class="crumb"><a href="/products.html">Products</a> › 101 Course Notes</div>
  <span class="eyebrow">Course Notes · PDF · {len(rows)} courses</span>
  <h1 class="title">101 Course Notes</h1>
  <p class="lede">Every course in the ImpactMojo 101 series as a printable A4 document: all the slides, two to a page, with ruled space under each pair for your own notes. ₹{PRICE} each. The decks themselves stay <a href="/101-courses/">free online</a>.</p>
  <div class="field" style="max-width:420px"><label for="q">Find a course</label><input id="q" type="search" placeholder="e.g. regression, nutrition, caste" oninput="filt(this.value)"></div>
  <div class="tblwrap" tabindex="0" role="region" aria-label="101 Course Notes"><table class="n101">
    <thead><tr><th scope="col">Course</th><th scope="col">Slides</th><th scope="col">Pages</th><th scope="col"><span class="sr-only">Buy</span></th></tr></thead>
    <tbody>
{trs}
    </tbody>
  </table></div>
  <p class="note" id="none" hidden>No course matches that search.</p>
  <style>.n101{{width:100%;border-collapse:collapse;margin-top:1rem}}.n101 th,.n101 td{{text-align:left;padding:.55rem .6rem;border-bottom:1px solid var(--bd)}}.n101 th{{font-family:Inter;font-size:.8rem;text-transform:uppercase;letter-spacing:.06em;color:var(--mut)}}.n101 td:nth-child(2),.n101 td:nth-child(3){{font-family:'JetBrains Mono';font-size:.85rem;color:var(--tx2)}}.btn.sm{{padding:.35rem .8rem;font-size:.82rem}}.tblwrap{{overflow-x:auto}}.sr-only{{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}}#none[hidden]{{display:none}}</style>
  <script>function filt(v){{v=v.trim().toLowerCase();var n=0;document.querySelectorAll('.n101 tbody tr').forEach(function(r){{var s=!v||r.dataset.q.indexOf(v)>-1;r.hidden=!s;if(s)n++;}});document.getElementById('none').hidden=n>0;}}</script>
</main>'''


def link_deck(text, slug):
    """For scripts/deck-builder/build.py: the deck with its notes link, if it is on sale."""
    pages = json.loads((ROOT / "data/course-notes-101.json").read_text(encoding="utf-8"))
    decks = json.loads((ROOT / "data/decks.json").read_text(encoding="utf-8"))["decks"]
    d = next((d for d in decks if d["slug"] == slug), None)
    if d is None or slug not in pages:
        return text
    return deck_with_link(text, slug, title_of(d)) or text


def main():
    check = "--check" in sys.argv
    decks = json.loads((ROOT / "data/decks.json").read_text(encoding="utf-8"))["decks"]
    pages = json.loads((ROOT / "data/course-notes-101.json").read_text(encoding="utf-8"))
    missing = [d["slug"] for d in decks if d["slug"] not in pages]
    if missing:
        sys.exit("FAIL - no rendered notes for: " + ", ".join(missing))
    tpl = TEMPLATE.read_text(encoding="utf-8")
    want, files_lines, search, urls = {}, [], [], []
    rows = sorted(decks, key=lambda d: title_of(d).lower())
    for d in rows:
        n = pages[d["slug"]]["pages"]
        main_html, meta, product = page(d, n)
        url = f"/products/notes-101/{d['slug']}/"
        t = title_of(d)
        want[ROOT / url.strip("/") / "index.html"] = wrap(tpl, f"{t}: Course Notes (PDF)", meta, url, main_html,
                                                           f"Hi ImpactMojo, I'd like to buy the {t} Course Notes (₹{PRICE}). I've paid by UPI; here is my reference: ")
        files_lines.append(f'  {json.dumps(product[: -len(f" (₹{PRICE})")], ensure_ascii=False)}: "ImpactMojo-101-Notes-{d["slug"]}.pdf",\n')
        search.append({"id": f"N101-{d['slug']}", "title": f"{t}: Course Notes (PDF)", "description": meta, "type": "product",
                       "category": "101 Course Notes", "url": url, "tags": ["notes", "paid", f"₹{PRICE}", "101"]})
        urls.append(url)
    idx_meta = f"All {len(rows)} ImpactMojo 101 courses as printable A4 course notes, every slide two to a page with space for notes. ₹{PRICE} each."
    want[ROOT / "products/notes-101/index.html"] = wrap(tpl, "101 Course Notes (PDF)", idx_meta, "/products/notes-101/", index_page(rows, {k: v["pages"] for k, v in pages.items()}), "Hi ImpactMojo, I'd like to buy 101 Course Notes. I've paid by UPI; here is my reference: ")
    search.insert(0, {"id": "N101-index", "title": "101 Course Notes (PDF)", "description": idx_meta, "type": "product",
                      "category": "101 Course Notes", "url": "/products/notes-101/", "tags": ["notes", "paid", f"₹{PRICE}", "101"]})
    urls.insert(0, "/products/notes-101/")

    # the decks themselves
    nowhere = []
    for d in rows:
        dp = ROOT / d["url"].lstrip("/")
        new = deck_with_link(dp.read_text(encoding="utf-8"), d["slug"], title_of(d))
        if new is None:
            nowhere.append(d["slug"])
        else:
            want[dp] = new
    if nowhere:
        sys.exit("FAIL - no title tags or slide controls to carry the notes link in: " + ", ".join(nowhere))

    # handler FILES block
    h = HANDLER.read_text(encoding="utf-8")
    i, j = h.find(START), h.find(END)
    if i < 0 or j < 0:
        sys.exit("FAIL - 101-notes markers missing from FILES in " + HANDLER.name)
    new_h = h[: i + len(START)] + "".join(files_lines) + h[j:]
    want[HANDLER] = new_h

    # search index: replace every N101- row
    si_path = ROOT / "data/search-index.json"
    si = json.loads(si_path.read_text(encoding="utf-8"))
    kept = [e for e in si if not str(e.get("id", "")).startswith("N101-")]
    at = max((k for k, e in enumerate(kept) if str(e.get("url", "")).startswith("/products/notes-")), default=len(kept) - 1) + 1
    want[si_path] = json.dumps(kept[:at] + search + kept[at:], ensure_ascii=False, indent=2) + "\n"

    # sitemap
    sm_path = ROOT / "sitemap.xml"
    sm = re.sub(r"  <url><loc>https://www\.impactmojo\.in/products/notes-101/[^<]*</loc>[^\n]*\n", "", sm_path.read_text(encoding="utf-8"))
    # After the last flagship notes entry, not at the end: build-theories.py
    # owns the block before </urlset>, and two builders appending there undo
    # each other.
    last = [m.end() for m in re.finditer(r"  <url><loc>https://www\.impactmojo\.in/products/notes-[^<]*</loc>[^\n]*\n", sm)]
    k = last[-1] if last else sm.rindex("</urlset>")
    want[sm_path] = sm[:k] + "".join(f"  <url><loc>https://www.impactmojo.in{u}</loc><lastmod>2026-10-10</lastmod></url>\n" for u in urls) + sm[k:]

    stale = []
    for p, text in want.items():
        cur = p.read_text(encoding="utf-8") if p.exists() else None
        if cur != text:
            stale.append(p.relative_to(ROOT).as_posix())
            if not check:
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(text, encoding="utf-8")
    on_disk = {p for p in (ROOT / "products/notes-101").glob("*/index.html")}
    extra = sorted(p.relative_to(ROOT).as_posix() for p in on_disk if p not in want)
    if check:
        if stale or extra:
            print("FAIL - 101 Course Notes shop is out of step with data/decks.json")
            for s in stale:
                print("  stale: " + s)
            for s in extra:
                print("  page for a deck that no longer exists: " + s)
            sys.exit(1)
        print("PASS - %d 101 Course Notes pages, handler and listings in step" % len(rows))
    else:
        print("wrote %d files (%d products)" % (len(stale), len(rows)))


if __name__ == "__main__":
    main()
