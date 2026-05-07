"""Generate a minimal DOCX (Word) file with synthetic PHI — no external deps."""
import zipfile, os, textwrap

OUT = os.path.join(os.path.dirname(__file__), "discharge_summary.docx")

CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml"  ContentType="application/xml"/>
  <Override PartName="/word/document.xml"
    ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>"""

RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1"
    Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument"
    Target="word/document.xml"/>
</Relationships>"""

WORD_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
</Relationships>"""

def para(text, bold=False, size=24):
    b_open  = "<w:b/><w:bCs/>" if bold else ""
    lines = text.split("\n")
    runs = ""
    for i, line in enumerate(lines):
        runs += f"""<w:r><w:rPr>{b_open}<w:sz w:val="{size}"/></w:rPr><w:t xml:space="preserve">{line}</w:t></w:r>"""
        if i < len(lines) - 1:
            runs += "<w:r><w:br/></w:r>"
    return f"<w:p>{runs}</w:p>"

def blank():
    return "<w:p><w:r><w:t></w:t></w:r></w:p>"

paragraphs = [
    para("HOSPITAL DISCHARGE SUMMARY", bold=True, size=28),
    para("St. Anthony Medical Center — Department of Cardiology", bold=True),
    blank(),
    para("PATIENT INFORMATION", bold=True),
    para("Name:              Eleanor J. Strickland\n"
         "Date of Birth:     09/14/1948\n"
         "Age:               77\n"
         "Sex:               Female\n"
         "MRN:               SAMC-7700341\n"
         "SSN:               601-29-8843\n"
         "Address:           88 Birchwood Lane, Joliet, IL 60432\n"
         "Phone:             (815) 555-0224\n"
         "Email:             eleanor.strickland48@yahoo.com"),
    blank(),
    para("ADMISSION / DISCHARGE", bold=True),
    para("Admitted:          04/14/2026\n"
         "Discharged:        04/20/2026\n"
         "LOS:               6 days\n"
         "Attending:         Dr. Harold B. Sinclair, MD  |  NPI: 3344556677\n"
         "Consulting:        Dr. Priya Mehta, MD (Cardiology)  |  (815) 555-0800"),
    blank(),
    para("ADMITTING DIAGNOSIS", bold=True),
    para("Non-ST-elevation myocardial infarction (NSTEMI), anterior wall."),
    blank(),
    para("DISCHARGE DIAGNOSIS", bold=True),
    para("1. NSTEMI, anterior wall — treated with PCI, drug-eluting stent x1 (LAD)\n"
         "2. Hypertension — controlled\n"
         "3. Hyperlipidemia\n"
         "4. Type 2 Diabetes Mellitus — HbA1c 7.8%"),
    blank(),
    para("HOSPITAL COURSE", bold=True),
    para("Ms. Strickland presented to the ED on 04/14/2026 with acute-onset chest pain\n"
         "and diaphoresis. EKG demonstrated ST depression in V1-V4. Troponin I peaked\n"
         "at 18.4 ng/mL. Cardiac catheterization on 04/15/2026 revealed 90% occlusion\n"
         "of the proximal LAD; PCI performed with placement of a 3.0 x 18mm\n"
         "Xience Alpine DES. Post-procedure course uncomplicated. Echocardiogram\n"
         "04/17/2026: EF 45%, mild anterior hypokinesis."),
    blank(),
    para("DISCHARGE MEDICATIONS", bold=True),
    para("1. Aspirin 81mg — daily (indefinite)\n"
         "2. Clopidogrel 75mg — daily x 12 months\n"
         "3. Atorvastatin 80mg — nightly\n"
         "4. Metoprolol succinate 50mg — daily\n"
         "5. Lisinopril 10mg — daily\n"
         "6. Metformin 1000mg — BID with meals\n"
         "7. Nitroglycerin SL 0.4mg — PRN chest pain"),
    blank(),
    para("FOLLOW-UP", bold=True),
    para("Cardiology (Dr. Mehta): 04/27/2026 at 9:00 AM — (815) 555-0800\n"
         "Primary Care (Dr. L. Torres): 04/29/2026 — (815) 555-1133\n"
         "Cardiac Rehab referral placed — patient verbalized understanding."),
    blank(),
    para("EMERGENCY CONTACT", bold=True),
    para("Gerald Strickland (Son)  |  (815) 555-7741  |  gstrickland@email.com"),
    blank(),
    para("INSURANCE", bold=True),
    para("Medicare Part A/B — HIC No. 2HJ9-WQ4-TL81\n"
         "Secondary: AARP Supplemental, Policy No. AARP-IL-3309882"),
    blank(),
    para("Electronically signed: Dr. Harold B. Sinclair, MD"),
    para("Date/Time: 04/20/2026 14:32"),
    para("License No.: IL-036-071188"),
]

body_xml = "\n".join(paragraphs)

DOCUMENT = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas"
  xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
{body_xml}
  </w:body>
</w:document>"""

with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("[Content_Types].xml", CONTENT_TYPES)
    z.writestr("_rels/.rels", RELS)
    z.writestr("word/_rels/document.xml.rels", WORD_RELS)
    z.writestr("word/document.xml", DOCUMENT)

print(f"Saved {OUT}")
