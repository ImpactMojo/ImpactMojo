"""Management Response Tracker (Excel workbook and Word guide)."""
from openpyxl import Workbook
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import PatternFill

from xl_pack import grid_sheet, package, readme

BASE = "ImpactMojo-Management-Response-Tracker"
FILE = BASE + ".zip"
RESP = ["Accepted", "Partly accepted", "Not accepted"]
STAT = ["Not started", "In progress", "Done", "Dropped"]

FLAG = lambda r: f'=IF(OR(F{r}="",I{r}="Done",I{r}="Dropped"),"",IF(H{r}="","No due date",IF(H{r}<TODAY(),"Overdue","On time")))'
NEED = lambda r: f'=IF(OR(E{r}="Partly accepted",E{r}="Not accepted"),IF(F{r}="","Reason needed",""),"")'


def build(out):
    wb = Workbook()
    ws = wb.active
    ws.title = "Read me"
    readme(ws, "Management response tracker", "A table that follows every recommendation from the report to a decision, an owner, a date and a result.", [
        ("What is in the workbook", True),
        ("Tracker: one row per recommendation, with the client's response (Accepted, Partly accepted or Not accepted), the reason, the action, the owner, the due date and the status. A flag shows overdue actions and rows where a reason is missing.", False),
        ("Summary: counts of responses and statuses, and the share of accepted actions that are done.", False),
        ("Worked example: five recommendations from a maternal and newborn health evaluation.", False),
        ("How to use it", True),
        ("Yellow cells are yours to fill. Grey cells calculate. The client fills the response columns. The evaluator keeps the sheet and asks for a review every quarter.", False),
        ("An evaluation has not finished its work until the client has responded to every recommendation, even if the response is no.", False),
    ])
    cols = [("No.", 6), ("Recommendation (from the report)", 44), ("Priority group", 12), ("Responsible unit", 18), ("Response", 15), ("Reason, if not fully accepted", 36), ("Action the client will take", 40), ("Due date", 12), ("Status", 13), ("Update and evidence", 38), ("Flag", 14), ("Reason check", 14)]
    calc = {10: FLAG, 11: NEED}
    # the Flag formula looks at F (reason) for blank; use G (action) instead for blank check
    calc[10] = lambda r: f'=IF(OR(B{r}="",I{r}="Done",I{r}="Dropped",E{r}="Not accepted"),"",IF(H{r}="","No due date",IF(H{r}<TODAY(),"Overdue","On time")))'
    t = wb.create_sheet("Tracker")
    grid_sheet(t, "Tracker", "One row per recommendation. Fill in the response and the action; the flags calculate.", cols, 30, calc=calc, drops={2: ["Do first", "Plan it", "Quick win", "Park"], 4: RESP, 8: STAT}, fmts={7: "dd mmm yyyy"})
    t.conditional_formatting.add("K5:K34", FormulaRule(formula=['K5="Overdue"'], fill=PatternFill("solid", bgColor="F8D7D3")))
    s = wb.create_sheet("Summary")
    from xl_pack import title, box, SOFT
    from openpyxl.styles import Font
    title(s, "Summary", "Counts from the Tracker sheet.")
    s.column_dimensions["A"].width = 44
    s.column_dimensions["B"].width = 14
    rows = [
        ("Recommendations", '=COUNTA(Tracker!B5:B34)'),
        ("Accepted", '=COUNTIF(Tracker!E5:E34,"Accepted")'),
        ("Partly accepted", '=COUNTIF(Tracker!E5:E34,"Partly accepted")'),
        ("Not accepted", '=COUNTIF(Tracker!E5:E34,"Not accepted")'),
        ("No response yet", '=B4-B5-B6-B7'),
        ("Actions done", '=COUNTIF(Tracker!I5:I34,"Done")'),
        ("Actions overdue", '=COUNTIF(Tracker!K5:K34,"Overdue")'),
        ("Share of accepted and partly accepted that are done", '=IF(B5+B6=0,"",COUNTIFS(Tracker!E5:E34,"<>Not accepted",Tracker!E5:E34,"<>",Tracker!I5:I34,"Done")/(B5+B6))'),
    ]
    for i, (lab, f) in enumerate(rows):
        r = 4 + i
        s.cell(row=r, column=1, value=lab).font = Font(name="Calibri", size=10, bold=(i in (0, 7)))
        cc = s.cell(row=r, column=2, value=f)
        box(cc, SOFT, align="center")
        if i == 7:
            cc.number_format = "0%"
    s.sheet_view.showGridLines = False
    ex = [
        [1, "Give every health worker the new birth-asphyxia protocol", "Do first", "State training cell", "Accepted", None, "Train all 4,200 workers by September 2027", "2027-09-30", "In progress", "1,350 trained by 31 March"],
        [2, "Stock oxytocin at every sub-centre", "Plan it", "Supply chain", "Accepted", None, "Add cold-chain units to the next tender", "2027-06-30", "Not started", None],
        [3, "Post staff rosters at each facility", "Quick win", "Block medical officers", "Accepted", None, "Circular issued; rosters displayed", "2027-01-31", "Done", "Circular 14/2027; 28 of 30 sub-centres photographed"],
        [4, "Pay incentive on the day of delivery", "Plan it", "Finance", "Partly accepted", "Finance order needed; paid within 7 days of delivery instead", "Move payment to 7 days", "2027-08-31", "In progress", None],
        [5, "Replace delivery tables", "Park", "Procurement", "Not accepted", "Tables are within their useful life", None, None, "Dropped", None],
    ]
    x = wb.create_sheet("Worked example")
    grid_sheet(x, "Worked example: five recommendations", "From the Surakshit Maa evaluation. The flags calculate from the due dates.", cols, 5, rows=ex, calc=calc, drops={2: ["Do first", "Plan it", "Quick win", "Park"], 4: RESP, 8: STAT}, fmts={7: "dd mmm yyyy"})
    x.title = "Worked example"
    return package(out, BASE, wb, GUIDE)


GUIDE = dict(
    file=BASE + "-GUIDE.docx",
    cover=("Management Response Tracker", "A table that follows every recommendation from the report to a decision, an owner, a date and a result", "Guide to the Excel workbook · ₹199"),
    inside=[
        "**Part A.** Why a recommendation without a response is a wish.",
        "**Part B.** The method in five steps: transfer, ask, record, review and report.",
        "**Part C.** Reference assets: a covering email, wording for a response and a quarterly review routine.",
        "**Part D.** A worked example: five recommendations from a maternal and newborn health evaluation.",
    ],
    intro="This guide goes with the Excel workbook. Offer it at the end of the assignment. The client owns the responses, and the evaluator keeps the sheet current only if the contract says so.",
    parts=[
        ("PART A", "Why track the response", [
            ("body", "A report ends with recommendations. What happens next depends on whether anyone is asked to respond. A management response is the client's written answer to each recommendation: accept it, accept it in part or decline it, with a reason and, for what is accepted, an action, an owner and a date."),
            ("body", "Many evaluation policies require the response. Even where they do not, a tracker gives the evaluator an honest account of use. In the follow-up a year later, the question 'was the evaluation used?' has an answer in a table."),
            ("body", "Three rules apply:"),
            ("bullets", [
                "Every recommendation gets a response, including a no.",
                "A partial or negative response comes with a reason, so the evaluator can see whether the finding was misunderstood.",
                "Every accepted action has one owner and one date.",
            ]),
        ]),
        ("PART B", "The method", [
            ("h", "1.  Transfer"),
            ("purpose", "Move the recommendations from the report into the table."),
            ("guide", "Copy each recommendation into the Tracker as written in the report. Add the priority group from the prioritisation workbook, if you used it."),
            ("good", "The wording matches the report."),
            ("mistakes", "Rewriting the recommendations so that they are easier to accept."),
            ("h", "2.  Ask"),
            ("purpose", "Get a response for each row."),
            ("guide", "Send the table to the client with the covering email in Part C. Give a date, which should be 30 days after the final report. Offer a call to go through the rows."),
            ("good", "The client fills the response column on its own terms."),
            ("mistakes", "Filling the response for the client."),
            ("h", "3.  Record"),
            ("purpose", "Capture the response, the reason, the action, the owner and the date."),
            ("table", ["Response", "What the row needs"], [
                ["Accepted", "An action, a responsible unit, a due date."],
                ["Partly accepted", "The reason, the part accepted, an action, a due date."],
                ["Not accepted", "The reason."],
            ], [3.4, 12.5]),
            ("good", "The reason for a decline is specific, such as 'tables are within their useful life', and not 'not feasible'."),
            ("mistakes", "Allowing 'noted' as a response. It is not one."),
            ("h", "4.  Review"),
            ("purpose", "Keep the table alive."),
            ("guide", "Ask the client for an update each quarter. The Flag column shows an action that is past its date and not done. Record the evidence for each Done."),
            ("good", "Every Done has a line of evidence, such as a circular or a photograph."),
            ("mistakes", "Marking an item Done because a meeting happened."),
            ("h", "5.  Report"),
            ("purpose", "Show what was used."),
            ("guide", "The Summary sheet counts responses and statuses. Use it in the follow-up with the client after twelve months and in your own case study."),
            ("good", "You can say how many accepted actions are done and how many are late."),
            ("mistakes", "Reporting the share accepted without the share done."),
        ]),
        ("PART C", "Reference assets", [
            ("h", "C1.  Covering email"),
            ("body", "Subject: Management response to the evaluation of [programme]. Dear [name], the final report was accepted on [date]. The attached table lists each recommendation. We would be grateful if your team could fill in the response, the reason where you do not fully accept, the action, the responsible unit and the due date, by [date 30 days later]. A call of 30 minutes can go through the rows if that helps. [Name]"),
            ("h", "C2.  Wording that helps"),
            ("bullets", [
                "Accepted: 'We will [action] by [date]. [Unit] is responsible.'",
                "Partly accepted: 'We accept [part] because [reason]. We will [action] by [date]. We do not accept [part] because [reason].'",
                "Not accepted: 'We do not accept this because [reason].'",
            ]),
            ("h", "C3.  Quarterly review routine"),
            ("numbered", [
                "Send the table with last quarter's answers visible.",
                "Ask for status and evidence on every row not Done.",
                "Update the Flag and the Summary.",
                "Send a one-paragraph note to the client's sponsor with the numbers.",
            ]),
            ("h", "C4.  Glossary"),
            ("table", ["Term", "Meaning"], [
                ["Management response", "The client's written answer to each recommendation."],
                ["Responsible unit", "The part of the client organisation that will carry out the action."],
                ["Evidence of completion", "A document, photograph or record that shows the action was done."],
            ], [4.2, 11.7]),
        ]),
        ("PART D", "Worked example: maternal and newborn health evaluation", [
            ("table", ["No.", "Recommendation", "Response", "Status"], [
                ["1", "New birth-asphyxia protocol for every health worker", "Accepted", "In progress"],
                ["2", "Stock oxytocin at every sub-centre", "Accepted", "Not started"],
                ["3", "Post staff rosters at each facility", "Accepted", "Done"],
                ["4", "Pay incentive on the day of delivery", "Partly accepted", "In progress"],
                ["5", "Replace delivery tables", "Not accepted", "Dropped"],
            ], [1.0, 8.4, 3.4, 3.1]),
            ("body", "Five rows: three accepted, one partly accepted, one not accepted. Of the four accepted or partly accepted, one is done, which is 25 per cent. The reason for the partial response in row 4 is that the finance order allows payment within seven days of delivery and not on the day."),
            ("figures", "The responses are illustrative. Replace them with your own."),
        ]),
    ],
)

PAGE = dict(
    slug="management-response-tracker",
    title="Management Response Tracker",
    file=FILE,
    ext="XLSX",
    eyebrow="Template · XLSX",
    crumb="Template",
    meta="An Excel tracker that follows each evaluation recommendation to a response, a reason, an action, an owner and a date, with a summary, a Word guide and a worked example. ₹199.",
    og="Track every recommendation from the report to a response, an owner, a date and a result. ₹199.",
    lede="A table that follows every recommendation from the report to a decision, an owner, a date and a result.",
    note="Editable XLSX workbook + a Word guide · delivered to your inbox within 24 hours of payment.",
    letter_h="Find out whether the evaluation was used",
    letter=[
        "A report ends with recommendations. What happens next depends on whether anyone is asked to respond. A management response is the client's written answer to each recommendation, with a reason where it is not accepted and an action, an owner and a date where it is.",
        "This workbook gives you a tracker with dropdowns for the response and the status, a flag for overdue actions and missing reasons, and a summary that counts responses and the share of accepted actions that are done. A Word guide adds a covering email, wording for responses and a quarterly review routine.",
        'It takes the ranked list from the <a href="/products/impact-ease-prioritisation/">Impact and Ease Prioritisation</a> workbook and gives you the evidence for the three-month follow-up in the <a href="/products/client-feedback-template/">Client Feedback Survey &amp; Debrief</a>.',
    ],
    inside=[
        "A tracker for 30 recommendations with response, reason, action, owner, due date and status",
        "A flag for overdue actions and a check for missing reasons",
        "A summary of responses, statuses and the share of accepted actions that are done",
        "A Word guide with a covering email, response wording and a quarterly review routine",
        "A worked example: five recommendations from a maternal and newborn health evaluation",
    ],
    sample=[
        ("Tracker", "response, reason, action, owner, date"),
        ("Flags", "overdue actions and missing reasons"),
        ("Summary", "share of accepted actions that are done"),
        ("Covering email", "ask for the response in 30 days"),
    ],
    sample_file=None,
    faq=[
        ("What format is it?", "An Excel workbook (.xlsx) with live formulas and dropdowns, plus a Word guide. It also opens in Google Sheets and LibreOffice."),
        ("Who fills it in?", "The client fills the response columns. The evaluator keeps the sheet if the contract says so."),
        ("Does it send reminders?", "No. The flag shows overdue rows when you open the file. Send the reminders yourself."),
        ("How fast is delivery?", "Within 24 hours of confirming payment, usually much sooner."),
    ],
    search_desc="An Excel management response tracker for evaluations with response, reason, action, owner, due date and status, a summary, a Word guide and a worked example. Buy for ₹199 via UPI.",
    search_tags=["template", "management response", "tracker", "recommendations", "consulting", "evaluation", "Excel", "premium", "paid", "₹199"],
    search_id="PROD-MGMT-RESPONSE",
    card="Management Response Tracker",
    card_p="From recommendation to response, owner and date.",
    before="Stakeholder Map",
)
