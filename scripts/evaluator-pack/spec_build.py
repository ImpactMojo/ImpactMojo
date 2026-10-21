"""Build a house-format Word pack from a data spec.

A spec is a dict:

    file        output file name
    cover       (title, subtitle, line3)
    inside      list of "WHAT IS INSIDE THIS PACK" lines
    intro       the grey instruction paragraph under the box
    parts       [(label, title, [block, ...]), ...]

A block is a tuple whose first item is the kind:

    ("h", text)  ("sub", text)  ("purpose", text)  ("guide", text)  ("body", text)
    ("bullets", [..])  ("numbered", [..])  ("lines", n)
    ("table", header, rows, widths_cm)
    ("good", text)  ("mistakes", text)  ("legal", text)  ("figures", text)
    ("box", label, [paragraphs])  ("pagebreak",)

Text may carry **bold** runs, which Pack._rich renders.
"""
from lib import Pack


def build_doc(spec, path):
    k = Pack()
    k.cover(*spec["cover"])
    k.version(spec.get("version", "Version 1.0   ·   October 2026   ·   Part of the Evaluation Essentials Kit"))
    k.box("WHAT IS INSIDE THIS PACK", spec["inside"])
    k.guide(spec["intro"])
    for label, title, blocks in spec["parts"]:
        k.part(label, title)
        for b in blocks:
            kind = b[0]
            if kind == "table":
                k.table(b[1], b[2], b[3])
            elif kind == "lines":
                k.lines(b[1])
            elif kind == "box":
                k.box(b[1], b[2])
            elif kind == "pagebreak":
                k.page_break()
            else:
                getattr(k, {
                    "h": "h", "sub": "sub", "purpose": "purpose", "guide": "guide", "body": "body",
                    "bullets": "bullets", "numbered": "numbered", "good": "good", "mistakes": "mistakes",
                    "legal": "legal", "figures": "figures",
                }[kind])(b[1])
    if spec.get("sources"):
        k.part("SOURCES", "Where the rules and figures come from")
        k.bullets(spec["sources"], 9.5)
    k.save(path)
