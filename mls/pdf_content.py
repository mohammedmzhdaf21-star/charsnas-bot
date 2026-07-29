"""Rich multi-page specialty PDF content and schematic figure builders for MLS."""

from __future__ import annotations

from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing, Rect, String, Line, Circle, Ellipse


def _box(d: Drawing, x, y, w, h, label, fill=colors.Color(0.9, 0.93, 0.98)):
    d.add(Rect(x, y, w, h, fillColor=fill, strokeColor=colors.HexColor("#334155"), strokeWidth=1))
    d.add(
        String(
            x + w / 2,
            y + h / 2 - 4,
            label,
            fontSize=8,
            textAnchor="middle",
            fillColor=colors.HexColor("#0f172a"),
        )
    )


def fig_lab_phases() -> Drawing:
    d = Drawing(400, 160)
    d.add(String(200, 145, "Figure: Total testing process (schematic)", fontSize=10, textAnchor="middle"))
    _box(d, 20, 70, 100, 40, "Preanalytic", fill=colors.Color(1, 0.95, 0.9))
    _box(d, 150, 70, 100, 40, "Analytic", fill=colors.Color(0.9, 0.95, 1))
    _box(d, 280, 70, 100, 40, "Postanalytic", fill=colors.Color(0.9, 0.97, 0.9))
    d.add(Line(120, 90, 150, 90, strokeColor=colors.HexColor("#334155"), strokeWidth=1.5))
    d.add(Line(250, 90, 280, 90, strokeColor=colors.HexColor("#334155"), strokeWidth=1.5))
    d.add(String(70, 40, "Order, ID, draw,\ntransport, prep", fontSize=7, textAnchor="middle"))
    d.add(String(200, 40, "Method, QC,\nmeasurement", fontSize=7, textAnchor="middle"))
    d.add(String(330, 40, "Verify, report,\ncritical call", fontSize=7, textAnchor="middle"))
    d.add(
        String(
            200,
            8,
            "Most laboratory errors originate in the preanalytic phase",
            fontSize=7,
            textAnchor="middle",
            fillColor=colors.grey,
        )
    )
    return d


def fig_cbc_indices() -> Drawing:
    d = Drawing(400, 160)
    d.add(String(200, 145, "Figure: CBC morphology clues (schematic)", fontSize=10, textAnchor="middle"))
    _box(d, 20, 80, 110, 40, "Low MCV", fill=colors.Color(0.95, 0.9, 0.9))
    _box(d, 145, 80, 110, 40, "High MCV", fill=colors.Color(0.9, 0.93, 1))
    _box(d, 270, 80, 110, 40, "Normal MCV", fill=colors.Color(0.92, 0.97, 0.92))
    d.add(String(75, 50, "Iron def / thal", fontSize=7, textAnchor="middle"))
    d.add(String(200, 50, "B12 / folate / etc.", fontSize=7, textAnchor="middle"))
    d.add(String(325, 50, "Many causes — smear!", fontSize=7, textAnchor="middle"))
    d.add(
        String(
            200,
            15,
            "Indices guide differentials; smear + clinical context confirm",
            fontSize=7,
            textAnchor="middle",
            fillColor=colors.grey,
        )
    )
    return d


def fig_chem_panel() -> Drawing:
    d = Drawing(400, 160)
    d.add(String(200, 145, "Figure: Chemistry pattern thinking", fontSize=10, textAnchor="middle"))
    _box(d, 30, 90, 80, 35, "Electrolytes")
    _box(d, 130, 90, 80, 35, "Renal")
    _box(d, 230, 90, 80, 35, "Liver")
    _box(d, 330, 90, 50, 35, "CK")
    d.add(Line(70, 90, 70, 55, strokeColor=colors.HexColor("#dc2626"), strokeWidth=1.5))
    d.add(String(70, 40, "Hemolysis↑K+", fontSize=7, textAnchor="middle", fillColor=colors.HexColor("#b91c1c")))
    d.add(
        String(
            200,
            12,
            "Ask: true patient change vs artifact vs interference?",
            fontSize=7,
            textAnchor="middle",
            fillColor=colors.grey,
        )
    )
    return d


def fig_gram_workflow() -> Drawing:
    d = Drawing(400, 170)
    d.add(String(200, 155, "Figure: Culture workup pathway (schematic)", fontSize=10, textAnchor="middle"))
    _box(d, 20, 100, 80, 35, "Specimen")
    _box(d, 120, 100, 80, 35, "Gram stain")
    _box(d, 220, 100, 80, 35, "Culture")
    _box(d, 320, 100, 60, 35, "AST")
    for x in (100, 200, 300):
        d.add(Line(x, 117, x + 20, 117, strokeColor=colors.HexColor("#334155"), strokeWidth=1.5))
    d.add(String(200, 55, "Report ID + susceptibility with stewardship notes", fontSize=8, textAnchor="middle"))
    d.add(
        String(
            200,
            20,
            "Biosafety and critical alerts (e.g., CRE) are part of the result",
            fontSize=7,
            textAnchor="middle",
            fillColor=colors.grey,
        )
    )
    return d


def fig_sero_algorithm() -> Drawing:
    d = Drawing(400, 170)
    d.add(String(200, 155, "Figure: Serology algorithm idea", fontSize=10, textAnchor="middle"))
    _box(d, 140, 110, 120, 35, "Screen assay", fill=colors.Color(0.95, 0.95, 1))
    d.add(Line(200, 110, 200, 85, strokeColor=colors.HexColor("#334155"), strokeWidth=1.5))
    _box(d, 40, 40, 120, 35, "Nonreactive → stop", fill=colors.Color(0.92, 0.97, 0.92))
    _box(d, 240, 40, 140, 35, "Reactive → confirm", fill=colors.Color(1, 0.93, 0.9))
    d.add(Line(200, 85, 100, 75, strokeColor=colors.HexColor("#334155"), strokeWidth=1.2))
    d.add(Line(200, 85, 310, 75, strokeColor=colors.HexColor("#334155"), strokeWidth=1.2))
    d.add(
        String(
            200,
            10,
            "Follow published algorithms (HIV, syphilis, etc.) — not a single test alone",
            fontSize=7,
            textAnchor="middle",
            fillColor=colors.grey,
        )
    )
    return d


def fig_abo() -> Drawing:
    d = Drawing(400, 170)
    d.add(String(200, 155, "Figure: ABO forward typing idea", fontSize=10, textAnchor="middle"))
    _box(d, 30, 90, 70, 40, "Anti-A")
    _box(d, 120, 90, 70, 40, "Anti-B")
    _box(d, 210, 90, 70, 40, "Anti-D")
    _box(d, 300, 90, 80, 40, "Interpret")
    d.add(String(200, 50, "Forward + reverse must agree; resolve discrepancies", fontSize=8, textAnchor="middle"))
    d.add(
        String(
            200,
            15,
            "Educational schematic — follow blood bank SOP exactly",
            fontSize=7,
            textAnchor="middle",
            fillColor=colors.grey,
        )
    )
    return d


def fig_tissue_flow() -> Drawing:
    d = Drawing(400, 170)
    d.add(String(200, 155, "Figure: Histology processing chain", fontSize=10, textAnchor="middle"))
    steps = ["Fix", "Process", "Embed", "Section", "Stain"]
    for i, s in enumerate(steps):
        x = 25 + i * 75
        _box(d, x, 80, 65, 35, s, fill=colors.Color(0.93, 0.95, 0.99))
        if i < len(steps) - 1:
            d.add(Line(x + 65, 97, x + 75, 97, strokeColor=colors.HexColor("#334155"), strokeWidth=1.5))
    d.add(
        String(
            200,
            35,
            "Poor fixation ruins morphology and many IHC results",
            fontSize=8,
            textAnchor="middle",
        )
    )
    d.add(
        String(
            200,
            12,
            "Labeling and orientation prevent wrong-patient / wrong-site errors",
            fontSize=7,
            textAnchor="middle",
            fillColor=colors.grey,
        )
    )
    return d


def fig_parasite() -> Drawing:
    d = Drawing(400, 160)
    d.add(String(200, 145, "Figure: Malaria smear roles", fontSize=10, textAnchor="middle"))
    d.add(Circle(120, 75, 40, strokeColor=colors.HexColor("#334155"), fillColor=colors.Color(0.95, 0.9, 0.9)))
    d.add(String(120, 72, "Thick", fontSize=9, textAnchor="middle"))
    d.add(Ellipse(280, 75, 55, 35, strokeColor=colors.HexColor("#1d4ed8"), fillColor=colors.Color(0.9, 0.94, 1)))
    d.add(String(280, 72, "Thin", fontSize=9, textAnchor="middle"))
    d.add(String(120, 25, "Sensitivity / screen", fontSize=7, textAnchor="middle"))
    d.add(String(280, 25, "Species morphology", fontSize=7, textAnchor="middle"))
    return d


def fig_pcr_workflow() -> Drawing:
    d = Drawing(400, 170)
    d.add(String(200, 155, "Figure: Molecular workflow (schematic)", fontSize=10, textAnchor="middle"))
    _box(d, 15, 90, 85, 40, "Extract", fill=colors.Color(0.95, 0.95, 1))
    _box(d, 115, 90, 85, 40, "Amplify", fill=colors.Color(0.9, 0.95, 1))
    _box(d, 215, 90, 85, 40, "Detect", fill=colors.Color(0.9, 0.97, 0.92))
    _box(d, 315, 90, 70, 40, "Report", fill=colors.Color(1, 0.95, 0.9))
    for x in (100, 200, 300):
        d.add(Line(x, 110, x + 15, 110, strokeColor=colors.HexColor("#334155"), strokeWidth=1.5))
    d.add(
        String(
            200,
            45,
            "Unidirectional workflow + controls reduce false positives/negatives",
            fontSize=8,
            textAnchor="middle",
        )
    )
    d.add(
        String(
            200,
            15,
            "Internal control: was the reaction valid?",
            fontSize=7,
            textAnchor="middle",
            fillColor=colors.grey,
        )
    )
    return d


def fig_qc_chart() -> Drawing:
    d = Drawing(400, 170)
    d.add(String(200, 155, "Figure: QC mean ± limits (schematic)", fontSize=10, textAnchor="middle"))
    d.add(Line(40, 90, 360, 90, strokeColor=colors.HexColor("#2563eb"), strokeWidth=1.5))
    d.add(Line(40, 120, 360, 120, strokeColor=colors.HexColor("#94a3b8"), strokeWidth=0.8))
    d.add(Line(40, 60, 360, 60, strokeColor=colors.HexColor("#94a3b8"), strokeWidth=0.8))
    d.add(String(370, 86, "mean", fontSize=7))
    d.add(String(370, 116, "+2SD", fontSize=7))
    d.add(String(370, 56, "-2SD", fontSize=7))
    pts = [(50, 95), (90, 88), (130, 100), (170, 85), (210, 92), (250, 70), (290, 55), (330, 50)]
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        d.add(Line(x1, y1, x2, y2, strokeColor=colors.HexColor("#dc2626"), strokeWidth=1.5))
    d.add(
        String(
            200,
            20,
            "Out-of-control QC → stop, investigate, correct, verify — then release",
            fontSize=7,
            textAnchor="middle",
            fillColor=colors.grey,
        )
    )
    return d


def fig_ua_cast() -> Drawing:
    d = Drawing(400, 160)
    d.add(String(200, 145, "Figure: Urine formed elements (schematic)", fontSize=10, textAnchor="middle"))
    _box(d, 30, 70, 100, 40, "RBCs / WBCs", fill=colors.Color(1, 0.93, 0.93))
    _box(d, 150, 70, 100, 40, "Casts", fill=colors.Color(0.93, 0.95, 1))
    _box(d, 270, 70, 100, 40, "Crystals", fill=colors.Color(0.93, 0.98, 0.93))
    d.add(String(200, 35, "Dipstick + microscopy together; know when to escalate", fontSize=8, textAnchor="middle"))
    d.add(
        String(
            200,
            12,
            "RBC casts → glomerular themes; crystals need polarization skill",
            fontSize=7,
            textAnchor="middle",
            fillColor=colors.grey,
        )
    )
    return d


def _section(title_prefix: str, label: str, figure_name: str, books: str) -> list[dict]:
    return [
        {
            "title": f"1. Core concepts in {label}",
            "paras": [
                f"High-yield undergraduate themes in {label.lower()} for exams and lab practice.",
                "Connect specimen quality → method → result → clinical action.",
                "Patient safety, biosafety, and quality systems are inseparable from MLS work.",
            ],
            "figure_name": figure_name,
        },
        {
            "title": "2. Preanalytic and specimen issues",
            "paras": [
                f"Recognize common preanalytic traps that distort {label.lower()} results.",
                "Correct patient ID, collection, timing, and transport prevent false crises.",
                "Know when to reject, redraw, or add a comment instead of releasing numbers.",
            ],
        },
        {
            "title": "3. Analytic methods and interpretation",
            "paras": [
                "Method principles, limitations, and interferences matter as much as the value.",
                "Use reference ranges and critical values appropriate to your analyzer and population.",
                "Pattern recognition beats memorizing isolated cutoffs.",
            ],
            "figure_name": figure_name,
        },
        {
            "title": "4. Quality, safety and communication",
            "paras": [
                "QC failures, critical calls, and biosafety events need clear SOPs.",
                "Document corrective actions; verify before returning to patient testing.",
                "Communicate urgent and unexpected findings promptly and clearly.",
            ],
        },
        {
            "title": "5. Checklist and book anchors",
            "paras": [
                "Checklist: ID → specimen integrity → method/QC → interpret → report/escalate.",
                "After reading, practice with bot MCQs and cases for active recall.",
                f"Primary references: {books}.",
            ],
        },
    ]


PDF_SECTIONS: dict[str, list[dict]] = {
    "hematology": _section(
        "1",
        "Hematology",
        "fig_cbc_indices",
        "Clinical Hematology — Rodak; Hoffbrand; CLSI hematology docs",
    ),
    "clinical_chemistry": _section(
        "1",
        "Clinical Chemistry",
        "fig_chem_panel",
        "Tietz Fundamentals; Bishop; CLSI chemistry docs",
    ),
    "medical_microbiology": _section(
        "1",
        "Medical Microbiology",
        "fig_gram_workflow",
        "Bailey & Scott; CLSI M100; Murray",
    ),
    "immunology": _section(
        "1",
        "Immunology & Serology",
        "fig_sero_algorithm",
        "Clinical immunology texts; Henry's; assay IFUs",
    ),
    "blood_bank": _section(
        "1",
        "Blood Bank / Transfusion",
        "fig_abo",
        "AABB Technical Manual; transfusion texts; local SOPs",
    ),
    "histopathology": _section(
        "1",
        "Histopathology",
        "fig_tissue_flow",
        "Bancroft; histotechnology manuals; CAP checklists",
    ),
    "parasitology": _section(
        "1",
        "Parasitology",
        "fig_parasite",
        "CDC DPDx; clinical parasitology texts; WHO guides",
    ),
    "molecular_diagnostics": _section(
        "1",
        "Molecular Diagnostics",
        "fig_pcr_workflow",
        "Molecular diagnostics texts; CAP molecular checklists; IFUs",
    ),
    "lab_qa": _section(
        "1",
        "Lab QA & Safety",
        "fig_qc_chart",
        "ISO 15189 overviews; CLSI quality docs; BMBL",
    ),
    "urinalysis": _section(
        "1",
        "Urinalysis & Body Fluids",
        "fig_ua_cast",
        "Strasinger; clinical microscopy manuals; CLSI body fluid docs",
    ),
}

# Shared figure used on cover-style reminder pages via generate_pdfs revision prompts
# Ensure lab phases is available for any specialty that wants it
FIGURES = {
    "fig_lab_phases": fig_lab_phases,
    "fig_cbc_indices": fig_cbc_indices,
    "fig_chem_panel": fig_chem_panel,
    "fig_gram_workflow": fig_gram_workflow,
    "fig_sero_algorithm": fig_sero_algorithm,
    "fig_abo": fig_abo,
    "fig_tissue_flow": fig_tissue_flow,
    "fig_parasite": fig_parasite,
    "fig_pcr_workflow": fig_pcr_workflow,
    "fig_qc_chart": fig_qc_chart,
    "fig_ua_cast": fig_ua_cast,
}
