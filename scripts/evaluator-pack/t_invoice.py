"""Invoice Pack with GST and TDS (Excel workbook and Word guide, zipped)."""
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill

from xl_pack import BORDER, IN_FILL, NAVY, SOFT, TEAL, box, dropdown, head, package, readme, title

BASE = "ImpactMojo-Invoice-GST-TDS-Pack"
FILE = BASE + ".zip"

NAT = ["Professional services (10%)", "Technical services (2%)", "No deduction expected"]


def invoice_sheet(ws, ex=None):
    ex = ex or {}
    title(ws, "Tax invoice with GST and TDS", "Fill the yellow cells. The tax, the deduction and the amount you will receive calculate for you.")
    for col, w in zip("ABCDEFG", (34, 34, 12, 14, 16, 16, 4)):
        ws.column_dimensions[col].width = w

    def label(r, a, b, val):
        ws.cell(row=r, column=1, value=a).font = Font(name="Calibri", size=10, bold=True)
        c = ws.cell(row=r, column=2, value=val)
        box(c, IN_FILL)
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=6)

    ws["A4"] = "Supplier (you)"
    ws["A4"].font = Font(name="Calibri", size=11, bold=True, color=TEAL)
    s = ex.get("supplier", {})
    label(5, "Legal name", "", s.get("name", ""))
    label(6, "Address", "", s.get("addr", ""))
    label(7, "GSTIN", "", s.get("gstin", ""))
    label(8, "State and state code (two digits)", "", s.get("state", ""))
    label(9, "State code only (for the tax calculation)", "", s.get("code", ""))
    label(10, "PAN", "", s.get("pan", ""))

    ws["A12"] = "Recipient (client)"
    ws["A12"].font = Font(name="Calibri", size=11, bold=True, color=TEAL)
    c = ex.get("client", {})
    label(13, "Legal name", "", c.get("name", ""))
    label(14, "Address", "", c.get("addr", ""))
    label(15, "GSTIN (if registered)", "", c.get("gstin", ""))
    label(16, "Place of supply: state code (the recipient's location for B2B services)", "", c.get("pos", ""))
    label(17, "Client PAN", "", c.get("pan", ""))

    ws["A19"] = "Invoice details"
    ws["A19"].font = Font(name="Calibri", size=11, bold=True, color=TEAL)
    m = ex.get("meta", {})
    label(20, "Invoice number (up to 16 characters: letters, numbers, / and -)", "", m.get("no", ""))
    label(21, "Invoice date", "", m.get("date", ""))
    label(22, "Contract or purchase order reference", "", m.get("po", ""))
    label(23, "Payment due (days from date)", "", m.get("due", ""))
    label(24, "Tax payable on reverse charge?", "", "No")
    dropdown(ws, "B24", ["No", "Yes"])

    ws["A26"] = "Services"
    ws["A26"].font = Font(name="Calibri", size=11, bold=True, color=TEAL)
    head(ws, 27, ["Description of service", "SAC", "Qty", "Rate (₹)", "Amount (₹)"], 1)
    # description takes A, SAC B... keep columns A..E
    lines = ex.get("lines", [("", "", None, None)] * 6)
    for i in range(6):
        r = 28 + i
        d, sac, q, rt = lines[i] if i < len(lines) else ("", "", None, None)
        for j, v in enumerate([d, sac, q, rt], 1):
            cc = ws.cell(row=r, column=j, value=v)
            box(cc, IN_FILL, align="center" if j in (2, 3) else "top")
        cc = ws.cell(row=r, column=5, value=f'=IF(OR(C{r}="",D{r}=""),"",C{r}*D{r})')
        box(cc, None, align="top")
        cc.number_format = "#,##0.00"
        ws.cell(row=r, column=4).number_format = "#,##0.00"
    ws["A35"] = "Use SAC 9983 (other professional, technical and business services) or 9981 (research and experimental development) to match the work."
    ws["A35"].font = Font(name="Calibri", size=9, italic=True, color="5B6776")

    ws["A37"] = "Tax"
    ws["A37"].font = Font(name="Calibri", size=11, bold=True, color=TEAL)
    rows = [
        (38, "Taxable value (₹)", '=SUM(E28:E33)', "#,##0.00"),
        (39, "GST rate", ex.get("rate", 0.18), "0%"),
        (40, "Type of supply", '=IF(OR(B9="",B16=""),"Enter both state codes",IF(B9=B16,"Intra-state: CGST and SGST","Inter-state: IGST"))', "@"),
        (41, "CGST (₹)", '=IF(B40="Intra-state: CGST and SGST",ROUND(B38*B39/2,2),0)', "#,##0.00"),
        (42, "SGST or UTGST (₹)", '=IF(B40="Intra-state: CGST and SGST",ROUND(B38*B39/2,2),0)', "#,##0.00"),
        (43, "IGST (₹)", '=IF(B40="Inter-state: IGST",ROUND(B38*B39,2),0)', "#,##0.00"),
        (44, "Invoice total (₹)", '=B38+B41+B42+B43', "#,##0.00"),
    ]
    for r, lab, v, fmt in rows:
        ws.cell(row=r, column=1, value=lab).font = Font(name="Calibri", size=10, bold=(r in (38, 44)))
        cc = ws.cell(row=r, column=2, value=v)
        box(cc, IN_FILL if r == 39 else SOFT, align="center", bold=(r in (38, 44)))
        cc.number_format = fmt
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)

    ws["A46"] = "Tax the client may deduct at source (section 393 of the Income-tax Act, 2025)"
    ws["A46"].font = Font(name="Calibri", size=11, bold=True, color=TEAL)
    t = ex.get("tds", {})
    rows2 = [
        (47, "How the client treats your fee", t.get("nature", NAT[0]), "@", True),
        (48, "Payments from this client earlier this financial year (₹, excluding GST)", t.get("prev", 0), "#,##0.00", True),
        (49, "Annual threshold (₹)", 50000, "#,##0", True),
        (50, "Deduction rate", '=IF(B47="Professional services (10%)",0.1,IF(B47="Technical services (2%)",0.02,0))', "0%", False),
        (51, "Tax expected to be deducted from this invoice (₹)", '=IF(B50=0,0,IF(B48+B38>B49,ROUND(B38*B50,2),0))', "#,##0.00", False),
        (52, "Amount you should receive (₹)", '=B44-B51', "#,##0.00", False),
    ]
    for r, lab, v, fmt, inp in rows2:
        ws.cell(row=r, column=1, value=lab).font = Font(name="Calibri", size=10, bold=(r == 52))
        ws.cell(row=r, column=1).alignment = Alignment(wrap_text=True, vertical="top")
        cc = ws.cell(row=r, column=2, value=v)
        box(cc, IN_FILL if inp else SOFT, align="center", bold=(r == 52))
        cc.number_format = fmt
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
        ws.row_dimensions[r].height = 28 if r == 48 else 18
    dropdown(ws, "B47", NAT)
    ws["A54"] = ("Tax is deducted on the fee without the GST when the GST is shown separately on the invoice. Where an earlier payment has already taken the total past the threshold, "
                 "the client deducts on this invoice in full. Ask the client's accounts team how they classify your fee, and match their deduction certificate to your tax statement.")
    ws["A54"].font = Font(name="Calibri", size=9, italic=True, color="5B6776")
    ws["A54"].alignment = Alignment(wrap_text=True, vertical="top")
    ws.merge_cells("A54:F54")
    ws.row_dimensions[54].height = 40

    ws["A56"] = "E-invoice check"
    ws["A56"].font = Font(name="Calibri", size=11, bold=True, color=TEAL)
    ws["A57"] = "Did your aggregate turnover exceed ₹5 crore in any year since 2017-18?"
    ws["B57"] = ex.get("einv", "No")
    box(ws["B57"], IN_FILL, align="center")
    dropdown(ws, "B57", ["No", "Yes"])
    ws["A58"] = "What follows"
    ws["B58"] = '=IF(B57="Yes","Generate an e-invoice (IRN) for this B2B invoice","An e-invoice is not required; issue this tax invoice within 30 days of the supply")'
    ws.merge_cells("B58:F58")
    ws["B58"].font = Font(name="Calibri", size=10, bold=True)
    ws["A59"] = "Signature of the supplier or authorised representative: ____________________"
    ws["A59"].font = Font(name="Calibri", size=10)
    ws.sheet_view.showGridLines = False
    ws.freeze_panes = "A4"


def receipt_sheet(ws):
    title(ws, "Receipt voucher for an advance", "Issue one when a client pays before you invoice. GST on services is due on receipt of the advance.")
    for col, w in zip("AB", (52, 40)):
        ws.column_dimensions[col].width = w
    rows = [
        (4, "Supplier legal name, address and GSTIN", ""),
        (5, "Serial number (unique in the financial year: letters, numbers, / and -)", ""),
        (6, "Date", ""),
        (7, "Recipient name, address and GSTIN (if registered)", ""),
        (8, "Description of the service the advance is for", ""),
        (9, "Advance received (₹)", None),
        (10, "Does the amount received already include GST?", "Yes"),
        (11, "GST rate", 0.18),
    ]
    for r, lab, v in rows:
        ws.cell(row=r, column=1, value=lab).font = Font(name="Calibri", size=10, bold=True)
        ws.cell(row=r, column=1).alignment = Alignment(wrap_text=True, vertical="top")
        cc = ws.cell(row=r, column=2, value=v)
        box(cc, IN_FILL)
    ws["B9"].number_format = "#,##0.00"
    ws["B11"].number_format = "0%"
    dropdown(ws, "B10", ["Yes", "No"])
    calc = [
        (13, "Value of the service for which the advance is taken (₹)", '=IF(B9="","",IF(B10="Yes",ROUND(B9/(1+B11),2),B9))'),
        (14, "GST on the advance (₹)", '=IF(B9="","",IF(B10="Yes",B9-B13,ROUND(B9*B11,2)))'),
        (15, "Total received (₹)", '=IF(B9="","",B13+B14)'),
    ]
    for r, lab, f in calc:
        ws.cell(row=r, column=1, value=lab).font = Font(name="Calibri", size=10, bold=True)
        cc = ws.cell(row=r, column=2, value=f)
        box(cc, SOFT, align="center", bold=True)
        cc.number_format = "#,##0.00"
    ws["A17"] = ("Show the place of supply with the state and its code if the supply is inter-state, and say whether tax is payable on reverse charge. "
                 "When you issue the tax invoice later, show the advance and the tax already paid, and charge only the balance.")
    ws["A17"].font = Font(name="Calibri", size=9, italic=True, color="5B6776")
    ws["A17"].alignment = Alignment(wrap_text=True, vertical="top")
    ws.merge_cells("A17:B17")
    ws.row_dimensions[17].height = 42
    ws.sheet_view.showGridLines = False


def log_sheet(ws, ex=None):
    title(ws, "Invoice log", "One row per invoice. The log shows what you are owed, the deductions you expect and the gaps to chase.")
    labels = ["Invoice no.", "Date", "Client", "Taxable value (₹)", "GST (₹)", "Total (₹)", "Tax to be deducted (₹)", "Deducted per client's certificate (₹)",
              "Certificate received?", "Date paid", "Amount received (₹)", "Difference (₹)", "Action"]
    head(ws, 4, labels)
    ws.row_dimensions[4].height = 44
    rows = ex or [[None] * 11] * 3
    for i in range(20):
        r = 5 + i
        data = rows[i] if i < len(rows) else [None] * 11
        # data: no, date, client, taxable, gst, total, tds, tds_cert, cert?, paid, received
        for j in range(11):
            v = data[j] if j < len(data) else None
            cc = ws.cell(row=r, column=j + 1, value=v)
            box(cc, IN_FILL if j not in (5,) else SOFT, align="center" if j in (0, 1, 8, 9) else "top")
            if j in (3, 4, 5, 6, 7, 10):
                cc.number_format = "#,##0.00"
        ws.cell(row=r, column=6, value=f'=IF(D{r}="","",D{r}+E{r})')
        box(ws.cell(row=r, column=6), SOFT)
        ws.cell(row=r, column=6).number_format = "#,##0.00"
        cc = ws.cell(row=r, column=12, value=f'=IF(K{r}="","",F{r}-G{r}-K{r})')
        box(cc, SOFT)
        cc.number_format = "#,##0.00"
        cc = ws.cell(row=r, column=13, value=f'=IF(F{r}="","",IF(K{r}="","Chase payment",IF(ABS(L{r})>1,"Reconcile the difference",IF(AND(G{r}>0,I{r}<>"Yes"),"Ask for the deduction certificate","Closed"))))')
        box(cc, SOFT)
    ws["A26"] = "Totals"
    ws["A26"].font = Font(name="Calibri", size=10, bold=True)
    for col in "DEFGHK":
        ws[f"{col}26"] = f"=SUM({col}5:{col}24)"
        box(ws[f"{col}26"], SOFT, bold=True)
        ws[f"{col}26"].number_format = "#,##0.00"
    dropdown(ws, "I5:I24", ["Yes", "No"])
    for col, w in zip("ABCDEFGHIJKLM", (12, 12, 26, 15, 13, 15, 16, 18, 13, 12, 16, 14, 30)):
        ws.column_dimensions[col].width = w
    ws.sheet_view.showGridLines = False
    ws.freeze_panes = "A5"


def build(out):
    wb = Workbook()
    ws = wb.active
    ws.title = "Read me"
    readme(ws, "Invoice pack: GST and TDS", "A tax invoice, an advance receipt voucher and an invoice log for evaluators and consultants in India.", [
        ("What is in the workbook", True),
        ("Invoice: a tax invoice with the supplier and recipient blocks, six service lines, GST that switches between CGST and SGST or IGST by the state codes, the tax the client may deduct at source, the amount you should receive and an e-invoice check.", False),
        ("Advance receipt: the voucher you issue when a client pays before you invoice, with the GST on the advance worked out.", False),
        ("Invoice log: one row per invoice, with the deductions you expect, the certificate you must collect and the difference to chase.", False),
        ("Worked example: a filled invoice for the second milestone of a maternal and newborn health evaluation.", False),
        ("How to use it", True),
        ("Yellow cells are yours to fill. Grey cells calculate. Copy the Invoice sheet for each new invoice, or save a PDF of it.", False),
        ("The rates, the section number and the threshold were checked on 21 October 2026 against the CBIC and Income Tax Department sources named in the Word guide. Rates and thresholds change, so check the date before you rely on them. This is a drafting aid and not tax advice: have your accountant confirm your own position.", False),
    ])
    ws2 = wb.create_sheet("Invoice")
    invoice_sheet(ws2)
    ws3 = wb.create_sheet("Advance receipt")
    receipt_sheet(ws3)
    ws4 = wb.create_sheet("Invoice log")
    log_sheet(ws4)
    ws5 = wb.create_sheet("Worked example")
    invoice_sheet(ws5, dict(
        supplier=dict(name="[Evaluator LLP]", addr="[Address, Hyderabad]", gstin="[36AAAAA0000A1Z5]", state="Telangana", code="36", pan="[AAAAA0000A]"),
        client=dict(name="[State Health Mission, Telangana]", addr="[Address, Hyderabad]", gstin="[36BBBBB0000B1Z5]", pos="36", pan="[BBBBB0000B]"),
        meta=dict(no="EV/26-27/002", date="2026-12-05", po="[Contract SM-2026-14, milestone 2]", due="15"),
        lines=[("Inception report and evaluation matrix, milestone 2 of 4", "998399", 1, 1000000)],
        tds=dict(nature=NAT[0], prev=990000),
        einv="No",
    ))
    ws5.title = "Worked example"
    files = package(out, BASE, wb, GUIDE)
    return files


GUIDE = dict(
    file=BASE + "-GUIDE.docx",
    cover=("Invoice Pack: GST and TDS", "How to raise a correct tax invoice, handle an advance, understand the deduction at source and keep a log that catches the gaps", "Guide to the Excel workbook · ₹199"),
    inside=[
        "**Part A.** Why invoices fail, and the four mistakes that cost an evaluator money.",
        "**Part B.** The workbook sheet by sheet: the invoice, the advance receipt voucher, the invoice log and what each calculated cell does.",
        "**Part C.** Reference assets: the contents of a tax invoice, the timing rules, the deduction at source in plain words, a month-end routine and a glossary.",
        "**Part D.** A worked example: the second invoice for a maternal and newborn health evaluation.",
    ],
    intro="This guide goes with the Excel workbook. It is a drafting aid and not tax advice. Rates, thresholds and section numbers are as checked on 21 October 2026, and each blue box names its source. Have your accountant confirm your own position before you rely on it.",
    parts=[
        ("PART A", "Why invoices fail", [
            ("body", "An evaluator's invoice is simple in principle: a fee for a deliverable, plus GST, less tax deducted at source. In practice four mistakes cost money. The tax is charged under the wrong head, so the client's system rejects the invoice. The invoice is issued late. The tax deducted at source is never matched to the client's certificate, so credit is lost. And an advance arrives and no receipt voucher is issued, so GST falls due without anyone noticing."),
            ("body", "The workbook removes the arithmetic from each of them. It picks CGST and SGST or IGST from the two state codes, shows the deduction you should expect and the money you should receive, calculates the GST on an advance and keeps a log that flags every invoice that is unpaid, short-paid or missing a deduction certificate."),
            ("body", "Four habits make it work:"),
            ("bullets", [
                "Issue the invoice as soon as the deliverable is accepted, and never later than 30 days from the supply.",
                "Put the client's state code, and not the programme's, as the place of supply for a B2B service.",
                "Ask the client how it classifies your fee before you sign, and record the answer.",
                "Fill the log the day you invoice and the day you are paid.",
            ]),
        ]),
        ("PART B", "The workbook sheet by sheet", [
            ("h", "1.  Invoice"),
            ("purpose", "Produce a tax invoice with the particulars the GST rules require, and see the tax and the net receipt."),
            ("guide", "Fill the supplier and recipient blocks, then the invoice details, then the service lines. The type of supply, the CGST, SGST and IGST, the invoice total, the deduction at source and the amount you should receive calculate. Save the sheet as a PDF to send it."),
            ("table", ["Cell or block", "What it does"], [
                ["State codes (supplier B9, recipient B16)", "If they match, the invoice charges CGST and SGST in equal halves. If they differ, it charges IGST."],
                ["GST rate", "Set to 18% for evaluation and research services. Change it only if the rate changes."],
                ["How the client treats your fee", "Professional services take 10%. Technical services that are not professional take 2%. Choose the third option if the client has told you it will not deduct."],
                ["Payments earlier this financial year", "Enter the total of earlier fees from this client, excluding GST. The deduction applies when the total passes the annual threshold."],
                ["Amount you should receive", "The invoice total less the tax expected to be deducted. Compare it with the bank credit."],
                ["E-invoice check", "Answer the turnover question once for your organisation. A Yes tells you to generate an e-invoice."],
            ], [5.9, 10.0]),
            ("good", "The invoice carries every particular the rule asks for, and the sums match the bank credit within a rupee."),
            ("mistakes", "Using the programme's state code as the place of supply because the fieldwork was there. For a B2B service the place of supply is the recipient's location."),
            ("legal", "A tax invoice for services must carry, among other particulars, the supplier's name, address and GSTIN, a serial number of up to 16 characters that is unique in the financial year, the date, the recipient's name, address and GSTIN if registered, the description and SAC of the service, the value, the rate and amount of CGST and SGST or IGST, the place of supply with the state name and code for an inter-state supply, whether tax is payable on reverse charge and the supplier's signature (section 31 of the CGST Act, 2017 and Rule 46 of the CGST Rules, 2017). For services the invoice must be issued within 30 days of the supply (Rule 47). E-invoicing is mandatory for registered businesses whose aggregate turnover exceeded ₹5 crore in any financial year since 2017-18, for B2B supplies (CBIC Notification 10/2023-Central Tax, effective 1 August 2023); the test applies across all GSTINs under one PAN. Have your accountant confirm the current text."),
            ("h", "2.  Advance receipt"),
            ("purpose", "Record an advance correctly and calculate the GST on it."),
            ("guide", "Fill the voucher when money arrives before an invoice. Say whether the amount received already includes GST. The sheet splits it into the value of the service and the tax. When you raise the tax invoice later, show the advance and the tax already paid and charge only the balance."),
            ("legal", "A registered person who receives an advance for a supply must issue a receipt voucher with the supplier's name, address and GSTIN, a consecutive serial number, the date, the recipient, a description of the service, the amount of the advance, the rate and amount of tax, the place of supply for inter-state supplies, whether tax is payable on reverse charge, and a signature (section 31 of the CGST Act and Rule 50 of the CGST Rules). GST on an advance is payable on receipt for services. If the rate is not clear at the time of receipt, the Rules allow tax at 18%. Have your accountant confirm the current text."),
            ("good", "Every advance has a voucher with a serial number, and the later invoice shows the advance as paid."),
            ("mistakes", "Treating the advance as a loan or a deposit and waiting for the invoice to pay the GST."),
            ("h", "3.  Invoice log"),
            ("purpose", "Catch the invoices that are unpaid, short-paid or missing a deduction certificate."),
            ("guide", "Enter one row per invoice: number, date, client, taxable value and GST. The total and the tax to be deducted come from the invoice. When the client pays, enter the amount received, the amount deducted per the client's certificate and whether you have the certificate. The 'Action' column tells you what to do next: chase payment, reconcile a difference, ask for a certificate or close the row."),
            ("good", "No row stays open for more than 45 days, and every deduction has a certificate behind it."),
            ("mistakes", "Reading the bank credit as final. A short payment may be an unrecorded deduction, a late-fee or an error."),
            ("legal", "Tax deducted at source on fees for professional services is set by section 393(1), table serial 6(iii), of the Income-tax Act, 2025 (formerly section 194J): 10 per cent on fees for professional services and 2 per cent on fees for technical services that are not professional services, with a threshold of ₹50,000 a year. If you give the payer no valid PAN, section 397 requires deduction at a higher rate, and an inoperative PAN can have the same effect. Where GST is shown separately on the invoice, tax is deducted on the fee without the GST (CBDT Circular 23/2017). Government departments must also deduct GST at source at 2 per cent under section 51 of the CGST Act where the taxable value of a contract exceeds ₹2.5 lakh. Have your accountant confirm the current text."),
        ]),
        ("PART C", "Reference assets", [
            ("h", "C1.  A month-end routine"),
            ("numbered", [
                "List the deliverables accepted this month, and invoice each one.",
                "Check every state code and the SAC against the contract.",
                "Update the log with every payment received.",
                "For each deduction, confirm that the client has issued a certificate, and match it to your tax statement.",
                "Chase every invoice open for more than 30 days.",
                "Check the log total against your accounts.",
            ]),
            ("h", "C2.  Questions to ask the client's accounts team"),
            ("bullets", [
                "Under which section and at what rate will you deduct tax from our fee?",
                "Do you hold our PAN, and is it operative?",
                "To which address and GSTIN should the invoice go?",
                "How long does a payment take from the date of the invoice?",
                "Do you require an e-invoice or a purchase order number on the invoice?",
            ]),
            ("h", "C3.  Glossary"),
            ("table", ["Term", "Meaning"], [
                ["SAC", "Services Accounting Code: the code that classifies a service for GST."],
                ["Place of supply", "The state in which a supply is treated as made, which decides CGST and SGST or IGST."],
                ["Intra-state supply", "A supply where the supplier's location and the place of supply are in the same state."],
                ["TDS", "Tax deducted at source: tax the payer holds back from your fee and pays to the government in your name."],
                ["Receipt voucher", "The document that records an advance before the invoice is raised."],
                ["IRN", "Invoice Reference Number, issued by the government portal for an e-invoice."],
            ], [3.6, 12.3]),
        ]),
        ("PART D", "Worked example: second invoice, maternal and newborn health evaluation", [
            ("body", "The evaluator is in Hyderabad, state code 36, and the client is a state health mission in Hyderabad, so the place of supply is also 36. The fee for milestone 2, the inception report, is ₹10,00,000 before tax. The client has told the evaluator that it treats the fee as professional services. The client has already paid ₹9,90,000 this financial year, so the threshold has been passed."),
            ("table", ["Line", "Amount (₹)"], [
                ["Taxable value", "10,00,000.00"],
                ["Type of supply", "Intra-state: CGST and SGST"],
                ["CGST at 9%", "90,000.00"],
                ["SGST at 9%", "90,000.00"],
                ["Invoice total", "11,80,000.00"],
                ["Tax expected to be deducted (10% of 10,00,000)", "1,00,000.00"],
                ["Amount the evaluator should receive", "10,80,000.00"],
            ], [10.6, 5.3]),
            ("body", "When the payment arrives for ₹10,80,000, the log row closes only after the client's certificate for ₹1,00,000 has been received and matched. If the evaluator's turnover has never exceeded ₹5 crore, no e-invoice is needed and the invoice goes out within 30 days of the acceptance of the report."),
            ("figures", "The names, codes and amounts are illustrative. Replace them with your own."),
        ]),
    ],
    sources=[
        "CGST Act, 2017, sections 31 and 51; CGST Rules, 2017, Rules 46, 47 and 50, as published by CBIC and the GST Council.",
        "CBIC Notification 10/2023-Central Tax (e-invoicing threshold, 1 August 2023).",
        "Income-tax Act, 2025, sections 393 and 397, as published on incometaxindia.gov.in; CBDT Circular 23/2017.",
    ],
)

PAGE = dict(
    slug="invoice-gst-tds-pack",
    title="Invoice Pack: GST and TDS",
    file=FILE,
    ext="XLSX",
    eyebrow="Template · XLSX",
    crumb="Template",
    meta="An Excel invoice pack for evaluators in India: a tax invoice that picks CGST and SGST or IGST, shows the deduction at source and the amount you should receive, an advance receipt voucher and an invoice log, with a Word guide. ₹199.",
    og="A GST tax invoice, an advance receipt voucher and an invoice log for evaluators. ₹199.",
    lede="Raise a correct tax invoice, handle an advance, see the tax deducted at source before it arrives and keep a log that catches short payments.",
    note="Editable XLSX workbook + a Word guide · delivered to your inbox within 24 hours of payment.",
    letter_h="Take the arithmetic out of invoicing",
    letter=[
        "An evaluator's invoice is simple in principle: a fee, plus GST, less tax deducted at source. In practice the tax is charged under the wrong head, the invoice is issued late, the deduction is never matched to the client's certificate, or an advance arrives with no receipt voucher.",
        "This workbook picks CGST and SGST or IGST from the two state codes, shows the tax you should expect to have deducted and the money you should receive, splits an advance into value and GST and keeps a log that flags every invoice that is unpaid, short-paid or missing a certificate. The Word guide holds the rules, with boxes of law checked on 21 October 2026 and their sources.",
        'It follows the <a href="/products/sow-change-request-template/">Statement of Work &amp; Change Request Template</a>, whose payment milestones become the invoices here. The <a href="/products/evaluation-costing-calculator/">Evaluation Costing Calculator</a> builds the fee that goes onto them.',
    ],
    inside=[
        "A tax invoice that switches between CGST and SGST and IGST by state code",
        "The deduction at source and the amount you should receive, calculated before the money arrives",
        "An advance receipt voucher that splits the advance into value and GST",
        "An invoice log that tells you whether to chase, reconcile, ask for a certificate or close",
        "A Word guide with the rules, a month-end routine and questions for the client's accounts team",
        "A worked example: the second invoice of a maternal and newborn health evaluation",
    ],
    sample=[
        ("Invoice", "CGST and SGST or IGST, by state code"),
        ("Tax deducted at source", "10% or 2%, with the annual threshold"),
        ("Advance receipt", "GST on an advance, split from the value"),
        ("Invoice log", "chase, reconcile, ask for a certificate or close"),
    ],
    sample_file=None,
    faq=[
        ("What format is it?", "An Excel workbook (.xlsx) with live formulas, plus a Word guide. It also opens in Google Sheets and LibreOffice."),
        ("Is it tax advice?", "No. It is a drafting aid. The Word guide states the rules and their sources as read on 21 October 2026. Have your accountant confirm your own position."),
        ("Does it make e-invoices?", "No. It tells you whether an e-invoice is required. If it is, generate it through the GST e-invoice portal or your accounting software."),
        ("How fast is delivery?", "Within 24 hours of confirming payment, usually much sooner."),
    ],
    search_desc="An Excel invoice pack for evaluators in India with a GST tax invoice, the deduction at source, an advance receipt voucher and an invoice log, and a Word guide. Buy for ₹199 via UPI.",
    search_tags=["template", "invoice", "GST", "TDS", "tax", "consulting", "evaluation", "Excel", "premium", "paid", "₹199"],
    search_id="PROD-INVOICE-GST",
    card="Invoice Pack: GST and TDS",
    card_p="A tax invoice, an advance receipt and a log.",
    before="Stakeholder Map",
)
