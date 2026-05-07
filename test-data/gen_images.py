"""Generate test images with synthetic PHI for Redact testing."""
from PIL import Image, ImageDraw, ImageFont
import os

OUT = os.path.dirname(__file__)

def make_font(size):
    # Try common Windows fonts, fall back to default
    for name in ["arial.ttf", "calibri.ttf", "times.ttf", "cour.ttf"]:
        for path in [
            f"C:/Windows/Fonts/{name}",
            f"C:/Windows/Fonts/{name.upper()}",
        ]:
            if os.path.exists(path):
                try:
                    return ImageFont.truetype(path, size)
                except Exception:
                    pass
    return ImageFont.load_default()


# ── 1. Patient ID Card (PNG) ─────────────────────────────────────────────────
def make_patient_id_card():
    W, H = 900, 540
    img = Image.new("RGB", (W, H), color=(245, 248, 255))
    draw = ImageDraw.Draw(img)

    # Header bar
    draw.rectangle([(0, 0), (W, 90)], fill=(30, 70, 140))
    hdr = make_font(28)
    draw.text((30, 30), "MIDWEST REGIONAL MEDICAL CENTER", font=hdr, fill="white")

    # Subtitle
    sub = make_font(18)
    draw.text((30, 110), "PATIENT IDENTIFICATION CARD", font=sub, fill=(30, 70, 140))

    body = make_font(20)
    bold = make_font(20)

    fields = [
        ("Patient Name:",    "Kevin D. Ostrowski"),
        ("Date of Birth:",   "11/30/1969"),
        ("MRN:",             "MRMC-5509182"),
        ("SSN:",             "507-83-2241"),
        ("Insurance:",       "Aetna PPO — Member ID: AET-IL-30882917"),
        ("Group No:",        "GRP-77441"),
        ("Primary Care:",    "Dr. Fiona J. Brennan, MD  |  (847) 555-0217"),
        ("Address:",         "712 Elm Street, Evanston, IL 60201"),
        ("Phone:",           "(847) 555-0934"),
        ("Emergency:",       "Susan Ostrowski  (847) 555-1102"),
        ("Blood Type:",      "O+"),
        ("Allergies:",       "Penicillin, Sulfa drugs"),
    ]

    y = 155
    for label, value in fields:
        draw.text((50, y), label, font=bold, fill=(80, 80, 80))
        draw.text((260, y), value, font=body, fill=(20, 20, 20))
        y += 32

    # Footer
    draw.rectangle([(0, H - 50), (W, H)], fill=(30, 70, 140))
    foot = make_font(16)
    draw.text((30, H - 35), "Issue Date: 01/15/2025    Card No: CRD-20250115-8834", font=foot, fill="white")

    out = os.path.join(OUT, "patient_id_card.png")
    img.save(out, "PNG")
    print(f"Saved {out}")


# ── 2. Scanned referral letter (JPG) ─────────────────────────────────────────
def make_referral_letter_jpg():
    W, H = 850, 1100
    img = Image.new("RGB", (W, H), color=(252, 250, 245))
    draw = ImageDraw.Draw(img)

    font_h = make_font(22)
    font_b = make_font(18)
    font_n = make_font(17)

    lines = [
        ("h", "NORTHSHORE CARDIOLOGY ASSOCIATES"),
        ("h", "3000 N. Halsted St, Suite 400, Chicago, IL 60657"),
        ("h", "Tel: (773) 555-0540  |  Fax: (773) 555-0541"),
        ("",  ""),
        ("b", "REFERRAL / CONSULTATION REQUEST"),
        ("",  ""),
        ("n", "Date: April 20, 2026"),
        ("n", ""),
        ("n", "Referring Physician: Dr. Angela T. Kim, MD"),
        ("n", "NPI: 1122334455   Phone: (773) 555-2201"),
        ("n", "Practice: Wicker Park Family Medicine, 1600 N. Milwaukee Ave, Chicago IL 60647"),
        ("n", ""),
        ("b", "PATIENT INFORMATION"),
        ("n", "Name:          Robert S. Flanagan"),
        ("n", "Date of Birth: 05/08/1954   Age: 71"),
        ("n", "SSN:           388-21-7064"),
        ("n", "MRN:           WKFM-10034229"),
        ("n", "Phone:         (773) 555-8841"),
        ("n", "Email:         r.flanagan54@comcast.net"),
        ("n", "Address:       4411 W. Diversey Ave, Chicago, IL 60639"),
        ("n", "Insurance:     Medicare — HIC No. 1EG4-TE5-MK72"),
        ("n", ""),
        ("b", "REASON FOR REFERRAL"),
        ("n", "Mr. Flanagan is a 71-year-old male with a history of hypertension and"),
        ("n", "hyperlipidemia presenting with exertional dyspnea and atypical chest"),
        ("n", "discomfort x 6 weeks. Recent stress test (04/12/2026) showed 2mm ST"),
        ("n", "depression in leads V4-V6 at peak exercise. Please evaluate for possible"),
        ("n", "coronary artery disease."),
        ("n", ""),
        ("b", "CURRENT MEDICATIONS"),
        ("n", "Lisinopril 20mg daily, Atorvastatin 40mg QHS, Aspirin 81mg daily,"),
        ("n", "Metoprolol succinate 50mg daily"),
        ("n", ""),
        ("n", "Allergies: Contrast dye (hives, 2019)"),
        ("n", ""),
        ("n", "Please contact our office at (773) 555-2201 with any questions."),
        ("n", ""),
        ("n", "Sincerely,"),
        ("n", ""),
        ("n", "Dr. Angela T. Kim, MD"),
        ("n", "Wicker Park Family Medicine"),
        ("n", "License No.: IL-058-082241"),
    ]

    y = 40
    for kind, text in lines:
        f = font_h if kind == "h" else (font_b if kind == "b" else font_n)
        color = (30, 70, 140) if kind == "h" else (0, 0, 0)
        draw.text((50, y), text, font=f, fill=color)
        y += 28 if kind in ("h", "b") else 24

    out = os.path.join(OUT, "referral_letter.jpg")
    img.save(out, "JPEG", quality=88)
    print(f"Saved {out}")


# ── 3. Insurance card scan (TIFF) ─────────────────────────────────────────────
def make_insurance_card_tiff():
    W, H = 1010, 640
    img = Image.new("RGB", (W, H), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Card outline
    draw.rectangle([(10, 10), (W - 10, H - 10)], outline=(0, 0, 120), width=4)

    # Header
    draw.rectangle([(10, 10), (W - 10, 100)], fill=(0, 60, 160))
    hf = make_font(30)
    draw.text((30, 35), "UNITED HEALTHCARE — PPO GOLD PLAN", font=hf, fill="white")

    body = make_font(22)
    bold = make_font(22)

    left = [
        ("Member Name:",    "Denise M. Kowalski"),
        ("Member ID:",      "UHC-IL-88204471"),
        ("Group Number:",   "GRP-2204-HMO"),
        ("Plan Code:",      "IL-PPO-G-2025"),
        ("Effective Date:", "01/01/2025"),
        ("DOB:",            "03/27/1980"),
        ("SSN (last 4):",   "XXX-XX-4419"),
    ]
    right = [
        ("Subscriber:",       "Denise M. Kowalski"),
        ("Employer:",         "Chicago Public Schools"),
        ("PCP:",              "Dr. Marcus Webb, MD"),
        ("PCP Phone:",        "(312) 555-6621"),
        ("Copay (PCP):",      "$20"),
        ("Copay (Spec):",     "$45"),
        ("ER Copay:",         "$200"),
    ]

    y = 125
    for (ll, lv), (rl, rv) in zip(left, right):
        draw.text((30, y),   ll, font=bold, fill=(60, 60, 60))
        draw.text((230, y),  lv, font=body, fill=(0, 0, 0))
        draw.text((530, y),  rl, font=bold, fill=(60, 60, 60))
        draw.text((720, y),  rv, font=body, fill=(0, 0, 0))
        y += 60

    draw.rectangle([(10, H - 80), (W - 10, H - 10)], fill=(0, 60, 160))
    ff = make_font(17)
    draw.text((30, H - 60), "Claims: PO Box 30555, Salt Lake City UT 84130   |   Member Services: 1-800-555-0100", font=ff, fill="white")

    out = os.path.join(OUT, "insurance_card.tiff")
    img.save(out, "TIFF")
    print(f"Saved {out}")


if __name__ == "__main__":
    make_patient_id_card()
    make_referral_letter_jpg()
    make_insurance_card_tiff()
    print("Done.")
