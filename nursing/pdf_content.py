"""Rich multi-page specialty PDF content and schematic figure builders for Nursing."""

from __future__ import annotations

from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing, Rect, String, Line, Circle


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


def fig_abc() -> Drawing:
    d = Drawing(400, 150)
    d.add(String(200, 135, "Figure: Priority framework (schematic)", fontSize=10, textAnchor="middle"))
    _box(d, 30, 70, 100, 40, "Airway", fill=colors.Color(1, 0.9, 0.9))
    _box(d, 150, 70, 100, 40, "Breathing", fill=colors.Color(1, 0.95, 0.9))
    _box(d, 270, 70, 100, 40, "Circulation", fill=colors.Color(0.9, 0.95, 1))
    for x in (130, 250):
        d.add(Line(x, 90, x + 20, 90, strokeColor=colors.HexColor("#334155"), strokeWidth=1.5))
    d.add(
        String(
            200,
            30,
            "Then disability/exposure, safety, and routine tasks",
            fontSize=8,
            textAnchor="middle",
        )
    )
    d.add(
        String(
            200,
            10,
            "Unstable patients outrank charting and non-urgent requests",
            fontSize=7,
            textAnchor="middle",
            fillColor=colors.grey,
        )
    )
    return d


def fig_med_rights() -> Drawing:
    d = Drawing(400, 160)
    d.add(String(200, 145, "Figure: Medication safety rights", fontSize=10, textAnchor="middle"))
    rights = ["Patient", "Drug", "Dose", "Route", "Time"]
    for i, r in enumerate(rights):
        _box(d, 15 + i * 78, 80, 70, 35, r, fill=colors.Color(0.93, 0.96, 1))
    d.add(String(200, 40, "+ Documentation / reason / response / education", fontSize=8, textAnchor="middle"))
    d.add(
        String(
            200,
            15,
            "Two identifiers — every time — before administration",
            fontSize=7,
            textAnchor="middle",
            fillColor=colors.grey,
        )
    )
    return d


def fig_sepsis() -> Drawing:
    d = Drawing(400, 160)
    d.add(String(200, 145, "Figure: Sepsis recognition → action", fontSize=10, textAnchor="middle"))
    _box(d, 20, 80, 110, 40, "Suspect infection", fill=colors.Color(1, 0.95, 0.9))
    _box(d, 150, 80, 110, 40, "Organ stress signs", fill=colors.Color(1, 0.9, 0.9))
    _box(d, 280, 80, 100, 40, "Escalate / bundle", fill=colors.Color(0.9, 0.97, 0.9))
    d.add(Line(130, 100, 150, 100, strokeColor=colors.HexColor("#dc2626"), strokeWidth=1.5))
    d.add(Line(260, 100, 280, 100, strokeColor=colors.HexColor("#dc2626"), strokeWidth=1.5))
    d.add(
        String(
            200,
            35,
            "Tachypnea, altered mentation, hypotension — do not wait",
            fontSize=8,
            textAnchor="middle",
        )
    )
    d.add(
        String(
            200,
            12,
            "Cultures → antibiotics/fluids per protocol without harmful delay",
            fontSize=7,
            textAnchor="middle",
            fillColor=colors.grey,
        )
    )
    return d


def fig_family() -> Drawing:
    d = Drawing(400, 150)
    d.add(String(200, 135, "Figure: Family-centered pediatric care", fontSize=10, textAnchor="middle"))
    d.add(Circle(200, 70, 35, fillColor=colors.Color(0.9, 0.95, 1), strokeColor=colors.HexColor("#334155")))
    d.add(String(200, 66, "Child", fontSize=9, textAnchor="middle"))
    _box(d, 40, 55, 80, 30, "Parents/caregivers", fill=colors.Color(0.95, 0.97, 0.92))
    _box(d, 280, 55, 80, 30, "Care team", fill=colors.Color(0.95, 0.97, 0.92))
    d.add(Line(120, 70, 165, 70, strokeColor=colors.HexColor("#334155"), strokeWidth=1.2))
    d.add(Line(235, 70, 280, 70, strokeColor=colors.HexColor("#334155"), strokeWidth=1.2))
    d.add(
        String(
            200,
            15,
            "Developmentally appropriate communication + safety",
            fontSize=7,
            textAnchor="middle",
            fillColor=colors.grey,
        )
    )
    return d


def fig_pph() -> Drawing:
    d = Drawing(400, 160)
    d.add(String(200, 145, "Figure: Postpartum hemorrhage first steps", fontSize=10, textAnchor="middle"))
    _box(d, 20, 80, 85, 40, "Call help", fill=colors.Color(1, 0.9, 0.9))
    _box(d, 115, 80, 85, 40, "Massage fundus", fill=colors.Color(1, 0.95, 0.9))
    _box(d, 210, 80, 85, 40, "ABC / access", fill=colors.Color(0.9, 0.95, 1))
    _box(d, 305, 80, 75, 40, "Protocol", fill=colors.Color(0.9, 0.97, 0.9))
    d.add(
        String(
            200,
            35,
            "Boggy uterus → massage; empty bladder; uterotonics as ordered",
            fontSize=8,
            textAnchor="middle",
        )
    )
    d.add(
        String(
            200,
            12,
            "Quantify blood loss and escalate early",
            fontSize=7,
            textAnchor="middle",
            fillColor=colors.grey,
        )
    )
    return d


def fig_safety_psych() -> Drawing:
    d = Drawing(400, 150)
    d.add(String(200, 135, "Figure: Psychiatric safety ladder", fontSize=10, textAnchor="middle"))
    _box(d, 30, 70, 100, 40, "Assess risk", fill=colors.Color(0.95, 0.95, 1))
    _box(d, 150, 70, 100, 40, "Remove means", fill=colors.Color(1, 0.95, 0.9))
    _box(d, 270, 70, 100, 40, "Observe / notify", fill=colors.Color(0.9, 0.97, 0.9))
    d.add(
        String(
            200,
            30,
            "Ask directly about ideation, plan, intent, and means",
            fontSize=8,
            textAnchor="middle",
        )
    )
    d.add(
        String(
            200,
            10,
            "De-escalation before restraint whenever safe",
            fontSize=7,
            textAnchor="middle",
            fillColor=colors.grey,
        )
    )
    return d


def fig_prevention() -> Drawing:
    d = Drawing(400, 160)
    d.add(String(200, 145, "Figure: Levels of prevention", fontSize=10, textAnchor="middle"))
    _box(d, 25, 80, 110, 40, "Primary", fill=colors.Color(0.9, 0.97, 0.9))
    _box(d, 145, 80, 110, 40, "Secondary", fill=colors.Color(0.9, 0.95, 1))
    _box(d, 265, 80, 110, 40, "Tertiary", fill=colors.Color(1, 0.95, 0.9))
    d.add(String(80, 45, "Vaccines / education", fontSize=7, textAnchor="middle"))
    d.add(String(200, 45, "Screening", fontSize=7, textAnchor="middle"))
    d.add(String(320, 45, "Rehab / limit disability", fontSize=7, textAnchor="middle"))
    d.add(
        String(
            200,
            12,
            "Public health nursing works across all three levels",
            fontSize=7,
            textAnchor="middle",
            fillColor=colors.grey,
        )
    )
    return d


def fig_shock() -> Drawing:
    d = Drawing(400, 160)
    d.add(String(200, 145, "Figure: Shock nursing priorities", fontSize=10, textAnchor="middle"))
    _box(d, 20, 85, 80, 35, "ABC")
    _box(d, 115, 85, 80, 35, "Access")
    _box(d, 210, 85, 80, 35, "Oxygen")
    _box(d, 305, 85, 75, 35, "Protocol")
    d.add(String(200, 45, "Identify type (hypovolemic / distributive / cardiogenic / obstructive)", fontSize=7, textAnchor="middle"))
    d.add(
        String(
            200,
            15,
            "Trend MAP, mentation, urine output, lactate as available",
            fontSize=7,
            textAnchor="middle",
            fillColor=colors.grey,
        )
    )
    return d


def fig_ethics() -> Drawing:
    d = Drawing(400, 150)
    d.add(String(200, 135, "Figure: Core ethics principles", fontSize=10, textAnchor="middle"))
    _box(d, 20, 70, 85, 40, "Autonomy", fill=colors.Color(0.93, 0.96, 1))
    _box(d, 115, 70, 85, 40, "Beneficence", fill=colors.Color(0.9, 0.97, 0.9))
    _box(d, 210, 70, 85, 40, "Nonmaleficence", fill=colors.Color(1, 0.95, 0.9))
    _box(d, 305, 70, 75, 40, "Justice", fill=colors.Color(0.95, 0.93, 1))
    d.add(
        String(
            200,
            30,
            "Advocacy + confidentiality uphold professional nursing",
            fontSize=8,
            textAnchor="middle",
        )
    )
    d.add(
        String(
            200,
            10,
            "Use chain of command when safety and ethics collide",
            fontSize=7,
            textAnchor="middle",
            fillColor=colors.grey,
        )
    )
    return d


def fig_delirium() -> Drawing:
    d = Drawing(400, 160)
    d.add(String(200, 145, "Figure: Acute confusion workup mindset", fontSize=10, textAnchor="middle"))
    causes = ["O2", "Infection", "Meds", "Electrolytes", "Pain", "Stroke?"]
    for i, c in enumerate(causes):
        x = 20 + (i % 3) * 125
        y = 85 if i < 3 else 40
        _box(d, x, y, 110, 30, c, fill=colors.Color(0.95, 0.96, 1))
    d.add(
        String(
            200,
            12,
            "Delirium is a symptom — seek reversible causes while protecting safety",
            fontSize=7,
            textAnchor="middle",
            fillColor=colors.grey,
        )
    )
    return d


def _section(label: str, figure_name: str, books: str) -> list[dict]:
    return [
        {
            "title": f"1. Core concepts in {label}",
            "paras": [
                f"High-yield undergraduate themes in {label.lower()} for exams and clinical practice.",
                "Connect assessment → priority → intervention → reassessment.",
                "Patient safety, communication, and ethics are woven into every specialty.",
            ],
            "figure_name": figure_name,
        },
        {
            "title": "2. Assessment and early warning",
            "paras": [
                f"Recognize red-flag presentations early in {label.lower()}.",
                "Use systematic ABC/safety frameworks before task lists.",
                "Know when to call rapid response or escalate up the chain of command.",
            ],
        },
        {
            "title": "3. Interventions and evaluation",
            "paras": [
                "Nursing actions should be evidence-informed and protocol-aligned.",
                "Reassess after medications, oxygen, fluids, and teaching.",
                "Document clearly; hand off risks using structured tools (SBAR themes).",
            ],
            "figure_name": figure_name,
        },
        {
            "title": "4. Safety, teaching and teamwork",
            "paras": [
                "Infection control, medication safety, and fall prevention are daily work.",
                "Teach patients/families in plain language and verify understanding.",
                "Collaborate with the interprofessional team; advocate when plans are unsafe.",
            ],
        },
        {
            "title": "5. Checklist and book anchors",
            "paras": [
                "Checklist: ABC/safety → focused assessment → intervene → reassess → communicate.",
                "After reading, practice with the MCQs and cases for active recall.",
                f"Primary references: {books}.",
            ],
        },
    ]


PDF_SECTIONS: dict[str, list[dict]] = {
    "fundamentals": _section(
        "Fundamentals of Nursing",
        "fig_abc",
        "Potter & Perry; Kozier & Erb",
    ),
    "med_surg": _section(
        "Medical-Surgical Nursing",
        "fig_sepsis",
        "Lewis; Ignatavicius",
    ),
    "pediatrics": _section(
        "Pediatric Nursing",
        "fig_family",
        "Wong's Essentials of Pediatric Nursing",
    ),
    "maternity": _section(
        "Maternity / OB Nursing",
        "fig_pph",
        "Lowdermilk; maternal-newborn texts",
    ),
    "psychiatric": _section(
        "Psychiatric Nursing",
        "fig_safety_psych",
        "Videbeck; Townsend",
    ),
    "community": _section(
        "Community / Public Health",
        "fig_prevention",
        "Stanhope & Lancaster",
    ),
    "critical_care": _section(
        "Critical Care Nursing",
        "fig_shock",
        "Urden; AACN essentials",
    ),
    "pharm_nursing": _section(
        "Pharmacology for Nurses",
        "fig_med_rights",
        "Lehne; nursing pharmacology texts",
    ),
    "ethics_leadership": _section(
        "Ethics & Leadership",
        "fig_ethics",
        "Nursing ethics and professional practice texts",
    ),
    "geriatrics": _section(
        "Geriatric Nursing",
        "fig_delirium",
        "Touhy & Jett; Eliopoulos; Beers Criteria",
    ),
}
