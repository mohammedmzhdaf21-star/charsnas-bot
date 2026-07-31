"""Rich multi-page specialty PDF content and schematic figure builders."""

from __future__ import annotations

from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.graphics.shapes import Drawing, Rect, String, Line, Circle, Ellipse
from reportlab.graphics.charts.barcharts import VerticalBarChart


def _box(d: Drawing, x, y, w, h, label, fill=colors.Color(0.9, 0.93, 0.98)):
    d.add(Rect(x, y, w, h, fillColor=fill, strokeColor=colors.HexColor("#334155"), strokeWidth=1))
    d.add(String(x + w / 2, y + h / 2 - 4, label, fontSize=8, textAnchor="middle", fillColor=colors.HexColor("#0f172a")))


def fig_heart_flow() -> Drawing:
    d = Drawing(400, 180)
    d.add(String(200, 165, "Figure: Simplified cardiac blood-flow pathway", fontSize=10, textAnchor="middle"))
    _box(d, 20, 100, 70, 35, "Body veins")
    _box(d, 110, 100, 70, 35, "RA")
    _box(d, 200, 100, 70, 35, "RV")
    _box(d, 290, 100, 90, 35, "Lungs")
    _box(d, 110, 30, 70, 35, "LA")
    _box(d, 200, 30, 70, 35, "LV")
    _box(d, 290, 30, 90, 35, "Aorta/body")
    for x1, y1, x2, y2 in [
        (90, 117, 110, 117),
        (180, 117, 200, 117),
        (270, 117, 290, 117),
        (335, 100, 335, 65),
        (290, 47, 270, 47),
        (180, 47, 200, 47),
        (145, 100, 145, 65),
    ]:
        d.add(Line(x1, y1, x2, y2, strokeColor=colors.HexColor("#dc2626"), strokeWidth=1.5))
    d.add(String(200, 8, "Deoxygenated path above → lungs; oxygenated path below → systemic circulation", fontSize=7, textAnchor="middle", fillColor=colors.grey))
    return d


def fig_ecg_stemi() -> Drawing:
    d = Drawing(400, 150)
    d.add(String(200, 135, "Figure: Schematic STEMI vs normal ST segment", fontSize=10, textAnchor="middle"))
    # baseline
    d.add(Line(30, 40, 370, 40, strokeColor=colors.grey, strokeWidth=0.5))
    d.add(String(40, 110, "Normal", fontSize=8))
    points = [(40, 70), (55, 70), (60, 95), (65, 55), (80, 70), (110, 70), (125, 85), (140, 70), (180, 70)]
    for (x1, y1), (x2, y2) in zip(points, points[1:]):
        d.add(Line(x1, y1, x2, y2, strokeColor=colors.HexColor("#2563eb"), strokeWidth=1.5))
    d.add(String(220, 110, "STEMI (schematic STE)", fontSize=8))
    points2 = [(220, 70), (235, 70), (240, 95), (245, 50), (255, 100), (300, 100), (315, 70), (350, 70)]
    for (x1, y1), (x2, y2) in zip(points2, points2[1:]):
        d.add(Line(x1, y1, x2, y2, strokeColor=colors.HexColor("#dc2626"), strokeWidth=1.5))
    d.add(String(200, 10, "Educational schematic only — interpret real ECGs with clinical context", fontSize=7, textAnchor="middle", fillColor=colors.grey))
    return d


def fig_eye() -> Drawing:
    d = Drawing(400, 170)
    d.add(String(200, 155, "Figure: Simplified ocular cross-section", fontSize=10, textAnchor="middle"))
    d.add(Circle(200, 75, 55, strokeColor=colors.HexColor("#334155"), fillColor=colors.Color(0.93, 0.96, 1)))
    d.add(Circle(200, 75, 18, strokeColor=colors.HexColor("#1d4ed8"), fillColor=colors.Color(0.8, 0.88, 1)))
    d.add(Circle(200, 75, 7, fillColor=colors.HexColor("#0f172a"), strokeColor=colors.HexColor("#0f172a")))
    d.add(Ellipse(145, 75, 8, 18, strokeColor=colors.HexColor("#0ea5e9"), fillColor=colors.Color(0.85, 0.95, 1)))
    d.add(String(120, 75, "Cornea", fontSize=7, textAnchor="end"))
    d.add(String(200, 100, "Lens", fontSize=7, textAnchor="middle"))
    d.add(String(255, 75, "Retina", fontSize=7))
    d.add(Line(255, 75, 300, 75, strokeColor=colors.HexColor("#334155"), strokeWidth=2))
    d.add(String(305, 72, "Optic nerve", fontSize=7))
    d.add(String(200, 8, "Angle-closure risk rises when iris blocks aqueous outflow near the angle", fontSize=7, textAnchor="middle", fillColor=colors.grey))
    return d


def fig_nephron() -> Drawing:
    d = Drawing(400, 170)
    d.add(String(200, 155, "Figure: Nephron overview (schematic)", fontSize=10, textAnchor="middle"))
    d.add(Circle(70, 100, 22, fillColor=colors.Color(0.96, 0.9, 0.9), strokeColor=colors.HexColor("#b91c1c")))
    d.add(String(70, 96, "Glomerulus", fontSize=7, textAnchor="middle"))
    d.add(Line(92, 100, 130, 100, strokeColor=colors.HexColor("#334155"), strokeWidth=2))
    _box(d, 130, 85, 70, 30, "PCT", fill=colors.Color(0.9, 0.95, 0.9))
    d.add(Line(200, 100, 230, 100, strokeColor=colors.HexColor("#334155"), strokeWidth=2))
    d.add(Line(230, 100, 230, 40, strokeColor=colors.HexColor("#334155"), strokeWidth=2))
    d.add(Line(230, 40, 280, 40, strokeColor=colors.HexColor("#334155"), strokeWidth=2))
    d.add(Line(280, 40, 280, 100, strokeColor=colors.HexColor("#334155"), strokeWidth=2))
    d.add(String(255, 55, "Loop of Henle", fontSize=7, textAnchor="middle"))
    _box(d, 290, 85, 70, 30, "DCT", fill=colors.Color(0.9, 0.93, 0.98))
    d.add(Line(360, 100, 385, 100, strokeColor=colors.HexColor("#334155"), strokeWidth=2))
    d.add(String(200, 12, "Filtration → reabsorption/secretion → collecting system → urine", fontSize=7, textAnchor="middle", fillColor=colors.grey))
    return d


def fig_lung_zones() -> Drawing:
    d = Drawing(400, 160)
    d.add(String(200, 145, "Figure: Lung fields & lobar idea (schematic)", fontSize=10, textAnchor="middle"))
    d.add(Ellipse(130, 70, 55, 50, strokeColor=colors.HexColor("#0369a1"), fillColor=colors.Color(0.88, 0.94, 0.98)))
    d.add(Ellipse(270, 70, 55, 50, strokeColor=colors.HexColor("#0369a1"), fillColor=colors.Color(0.88, 0.94, 0.98)))
    d.add(Line(130, 95, 130, 45, strokeColor=colors.HexColor("#0f172a"), strokeWidth=0.8))
    d.add(Line(270, 100, 270, 40, strokeColor=colors.HexColor("#0f172a"), strokeWidth=0.8))
    d.add(Line(270, 70, 310, 70, strokeColor=colors.HexColor("#0f172a"), strokeWidth=0.8))
    d.add(String(130, 70, "L lung", fontSize=8, textAnchor="middle"))
    d.add(String(270, 78, "R lung", fontSize=8, textAnchor="middle"))
    d.add(String(200, 10, "Lobar pneumonia consolidates a lobe; listen and correlate with CXR", fontSize=7, textAnchor="middle", fillColor=colors.grey))
    return d


def fig_biliary() -> Drawing:
    d = Drawing(400, 160)
    d.add(String(200, 145, "Figure: Biliary tree pathway (schematic)", fontSize=10, textAnchor="middle"))
    _box(d, 30, 90, 80, 30, "Liver / bile")
    _box(d, 140, 90, 70, 30, "CHD")
    _box(d, 240, 90, 70, 30, "CBD")
    _box(d, 140, 30, 70, 30, "Gallbladder")
    _box(d, 320, 90, 60, 30, "Duodenum")
    d.add(Line(110, 105, 140, 105, strokeColor=colors.HexColor("#ca8a04"), strokeWidth=2))
    d.add(Line(210, 105, 240, 105, strokeColor=colors.HexColor("#ca8a04"), strokeWidth=2))
    d.add(Line(310, 105, 320, 105, strokeColor=colors.HexColor("#ca8a04"), strokeWidth=2))
    d.add(Line(175, 90, 175, 60, strokeColor=colors.HexColor("#ca8a04"), strokeWidth=2))
    d.add(String(200, 8, "Obstruction + infection → ascending cholangitis (Charcot triad)", fontSize=7, textAnchor="middle", fillColor=colors.grey))
    return d


def fig_hpa() -> Drawing:
    d = Drawing(400, 160)
    d.add(String(200, 145, "Figure: Hypothalamic–pituitary–thyroid axis", fontSize=10, textAnchor="middle"))
    _box(d, 150, 110, 100, 28, "Hypothalamus")
    _box(d, 150, 65, 100, 28, "Pituitary")
    _box(d, 150, 20, 100, 28, "Thyroid")
    d.add(Line(200, 110, 200, 93, strokeColor=colors.HexColor("#7c3aed"), strokeWidth=1.5))
    d.add(Line(200, 65, 200, 48, strokeColor=colors.HexColor("#7c3aed"), strokeWidth=1.5))
    d.add(String(270, 95, "TRH", fontSize=8))
    d.add(String(270, 50, "TSH", fontSize=8))
    d.add(String(270, 28, "T4/T3", fontSize=8))
    d.add(String(200, 5, "Feedback loops regulate TSH; interpret TFT patterns clinically", fontSize=7, textAnchor="middle", fillColor=colors.grey))
    return d


def fig_joint() -> Drawing:
    d = Drawing(400, 150)
    d.add(String(200, 135, "Figure: Fracture & compartment idea (schematic)", fontSize=10, textAnchor="middle"))
    d.add(Rect(80, 50, 30, 70, fillColor=colors.Color(0.92, 0.92, 0.92), strokeColor=colors.HexColor("#334155")))
    d.add(Rect(110, 50, 30, 70, fillColor=colors.Color(0.92, 0.92, 0.92), strokeColor=colors.HexColor("#334155")))
    d.add(Line(95, 85, 125, 75, strokeColor=colors.HexColor("#dc2626"), strokeWidth=2))
    d.add(String(100, 30, "Bone", fontSize=8, textAnchor="middle"))
    d.add(Ellipse(250, 85, 50, 35, strokeColor=colors.HexColor("#b45309"), fillColor=colors.Color(1, 0.95, 0.9)))
    d.add(String(250, 82, "Swollen\ncompartment", fontSize=7, textAnchor="middle"))
    d.add(String(200, 8, "Rising pressure → ischemia; pain out of proportion is a red flag", fontSize=7, textAnchor="middle", fillColor=colors.grey))
    return d


def fig_skin_layers() -> Drawing:
    d = Drawing(400, 150)
    d.add(String(200, 135, "Figure: Skin layers (schematic)", fontSize=10, textAnchor="middle"))
    d.add(Rect(60, 90, 280, 25, fillColor=colors.Color(1, 0.92, 0.85), strokeColor=colors.HexColor("#334155")))
    d.add(Rect(60, 55, 280, 35, fillColor=colors.Color(1, 0.85, 0.75), strokeColor=colors.HexColor("#334155")))
    d.add(Rect(60, 25, 280, 30, fillColor=colors.Color(0.95, 0.9, 0.85), strokeColor=colors.HexColor("#334155")))
    d.add(String(200, 98, "Epidermis", fontSize=9, textAnchor="middle"))
    d.add(String(200, 68, "Dermis", fontSize=9, textAnchor="middle"))
    d.add(String(200, 35, "Subcutis", fontSize=9, textAnchor="middle"))
    d.add(String(200, 5, "Depth matters: impetigo (epidermis) vs cellulitis (deeper soft tissue)", fontSize=7, textAnchor="middle", fillColor=colors.grey))
    return d


def fig_pregnancy() -> Drawing:
    d = Drawing(400, 150)
    d.add(String(200, 135, "Figure: Uterine atony concept after delivery", fontSize=10, textAnchor="middle"))
    d.add(Ellipse(140, 70, 40, 45, strokeColor=colors.HexColor("#be185d"), fillColor=colors.Color(1, 0.9, 0.94)))
    d.add(String(140, 67, "Firm\nuterus", fontSize=7, textAnchor="middle"))
    d.add(Ellipse(280, 70, 55, 45, strokeColor=colors.HexColor("#be185d"), fillColor=colors.Color(1, 0.85, 0.9)))
    d.add(String(280, 67, "Boggy\natonic uterus", fontSize=7, textAnchor="middle"))
    d.add(String(200, 8, "Atony → failure to contract → postpartum hemorrhage (most common PPH cause)", fontSize=7, textAnchor="middle", fillColor=colors.grey))
    return d


def fig_growth() -> Drawing:
    d = Drawing(400, 160)
    d.add(String(200, 145, "Figure: Example weight-for-age idea (schematic chart)", fontSize=10, textAnchor="middle"))
    chart = VerticalBarChart()
    chart.x = 50
    chart.y = 25
    chart.height = 90
    chart.width = 300
    chart.data = [[3, 5, 7, 9, 11]]
    chart.categoryAxis.categoryNames = ["0m", "3m", "6m", "9m", "12m"]
    chart.bars[0].fillColor = colors.HexColor("#0284c7")
    d.add(chart)
    d.add(String(200, 5, "Plot growth; falling off centiles needs evaluation", fontSize=7, textAnchor="middle", fillColor=colors.grey))
    return d


def fig_neuron() -> Drawing:
    d = Drawing(400, 150)
    d.add(String(200, 135, "Figure: UMN vs LMN lesion idea", fontSize=10, textAnchor="middle"))
    _box(d, 40, 80, 90, 30, "Cortex (UMN)", fill=colors.Color(0.9, 0.9, 1))
    d.add(Line(130, 95, 180, 95, strokeColor=colors.HexColor("#334155"), strokeWidth=2))
    _box(d, 180, 80, 90, 30, "Spinal LMN", fill=colors.Color(0.9, 1, 0.9))
    d.add(Line(270, 95, 320, 95, strokeColor=colors.HexColor("#334155"), strokeWidth=2))
    _box(d, 320, 80, 60, 30, "Muscle", fill=colors.Color(1, 0.95, 0.9))
    d.add(String(85, 50, "Spastic / ↑reflex", fontSize=7, textAnchor="middle"))
    d.add(String(225, 50, "Flaccid / ↓reflex", fontSize=7, textAnchor="middle"))
    d.add(String(200, 10, "Localize the lesion before naming the disease", fontSize=7, textAnchor="middle", fillColor=colors.grey))
    return d


def fig_gu() -> Drawing:
    d = Drawing(400, 150)
    d.add(String(200, 135, "Figure: Urinary tract overview", fontSize=10, textAnchor="middle"))
    d.add(Ellipse(120, 100, 35, 22, fillColor=colors.Color(0.9, 0.95, 1), strokeColor=colors.HexColor("#0369a1")))
    d.add(Ellipse(220, 100, 35, 22, fillColor=colors.Color(0.9, 0.95, 1), strokeColor=colors.HexColor("#0369a1")))
    d.add(String(120, 96, "Kidney", fontSize=7, textAnchor="middle"))
    d.add(String(220, 96, "Kidney", fontSize=7, textAnchor="middle"))
    d.add(Line(120, 78, 170, 45, strokeColor=colors.HexColor("#0369a1"), strokeWidth=2))
    d.add(Line(220, 78, 170, 45, strokeColor=colors.HexColor("#0369a1"), strokeWidth=2))
    _box(d, 140, 20, 60, 25, "Bladder", fill=colors.Color(0.88, 0.94, 1))
    d.add(String(200, 5, "Stone in ureter → loin-to-groin colic; obstruction + infection is an emergency", fontSize=7, textAnchor="middle", fillColor=colors.grey))
    return d


# Specialty → list of (section_title, paragraphs[], optional figure builder name)

def fig_tooth() -> Drawing:
    d = Drawing(400, 160)
    d.add(String(200, 145, "Figure: Simplified tooth zones", fontSize=10, textAnchor="middle"))
    d.add(Ellipse(200, 110, 35, 25, strokeColor=colors.HexColor("#334155"), fillColor=colors.Color(0.95, 0.95, 0.98)))
    d.add(String(200, 107, "Crown/enamel", fontSize=7, textAnchor="middle"))
    d.add(Rect(185, 55, 30, 40, strokeColor=colors.HexColor("#334155"), fillColor=colors.Color(0.98, 0.93, 0.9)))
    d.add(String(200, 72, "Root", fontSize=7, textAnchor="middle"))
    d.add(Line(200, 55, 200, 30, strokeColor=colors.HexColor("#b91c1c"), strokeWidth=2))
    d.add(String(210, 35, "Apex", fontSize=7))
    d.add(String(200, 8, "Pulp chamber → canals → apex; endodontic anatomy drives access design", fontSize=7, textAnchor="middle", fillColor=colors.grey))
    return d


def fig_periodontium() -> Drawing:
    d = Drawing(400, 150)
    d.add(String(200, 135, "Figure: Periodontium schematic", fontSize=10, textAnchor="middle"))
    d.add(Rect(150, 70, 40, 45, fillColor=colors.Color(0.95, 0.95, 1), strokeColor=colors.HexColor("#334155")))
    d.add(String(170, 90, "Tooth", fontSize=7, textAnchor="middle"))
    d.add(Rect(120, 55, 100, 15, fillColor=colors.Color(1, 0.9, 0.9), strokeColor=colors.HexColor("#b91c1c")))
    d.add(String(170, 58, "Gingiva / attachment", fontSize=7, textAnchor="middle"))
    d.add(Rect(120, 30, 100, 20, fillColor=colors.Color(0.93, 0.93, 0.93), strokeColor=colors.HexColor("#334155")))
    d.add(String(170, 36, "Alveolar bone", fontSize=7, textAnchor="middle"))
    d.add(String(200, 8, "Periodontitis = inflammation + clinical attachment/bone loss", fontSize=7, textAnchor="middle", fillColor=colors.grey))
    return d


def fig_radiograph() -> Drawing:
    d = Drawing(400, 140)
    d.add(String(200, 125, "Figure: Imaging choice idea", fontSize=10, textAnchor="middle"))
    _box(d, 30, 50, 90, 40, "Bitewing", fill=colors.Color(0.9, 0.95, 1))
    _box(d, 150, 50, 90, 40, "Periapical", fill=colors.Color(0.9, 1, 0.93))
    _box(d, 270, 50, 100, 40, "CBCT (justify)", fill=colors.Color(1, 0.95, 0.9))
    d.add(String(200, 15, "ALARA: start with lowest dose that answers the clinical question", fontSize=7, textAnchor="middle", fillColor=colors.grey))
    return d



def fig_dose_response() -> Drawing:
    d = Drawing(400, 150)
    d.add(String(200, 135, "Figure: Dose–response idea (schematic)", fontSize=10, textAnchor="middle"))
    d.add(Line(40, 30, 360, 30, strokeColor=colors.grey, strokeWidth=1))
    d.add(Line(40, 30, 40, 120, strokeColor=colors.grey, strokeWidth=1))
    pts = [(50, 40), (100, 55), (160, 90), (220, 110), (300, 118), (350, 120)]
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        d.add(Line(x1, y1, x2, y2, strokeColor=colors.HexColor("#2563eb"), strokeWidth=2))
    d.add(String(200, 8, "More dose is not always more effect — watch toxicity and receptors", fontSize=7, textAnchor="middle", fillColor=colors.grey))
    return d

PDF_SECTIONS: dict[str, list[dict]] = {'pharmacology': [{'title': '1. Core concepts in Pharmacology',
                   'paras': ['High-yield undergraduate themes in pharmacology for exams and '
                             'practice.',
                             'Connect mechanism → clinical effect → monitoring → counseling.',
                             'Safety, legality, and evidence-based use are central to pharmacy.'],
                   'figure_name': 'fig_dose_response'},
                  {'title': '2. Clinical / practice patterns',
                   'paras': ['Recognize common presentations and risk situations in pharmacology.',
                             'Identify high-alert medicines and interaction red flags early.',
                             'Document interventions and communicate clearly with the care team.']},
                  {'title': '3. Calculations, quality and decision-making',
                   'paras': ['Dose calculations, renal/hepatic adjustment, and TDM timing save '
                             'lives.',
                             'Formulation choice (IR vs MR, sterile vs nonsterile) changes '
                             'outcomes.',
                             'Use reliable references; do not rely on memory for critical doses.'],
                   'figure_name': 'fig_dose_response'},
                  {'title': '4. Errors, ADRs and systems safety',
                   'paras': ['Prevent look-alike/sound-alike errors and crush/MR mistakes.',
                             'Report ADRs and near misses; improve systems, not only individuals.',
                             'Know when to refer urgently (toxicology, sepsis, airway, bleed).']},
                  {'title': '5. Checklist and book anchors',
                   'paras': ['Checklist: indication, dose, interactions, allergies, organ '
                             'function, counseling, follow-up.',
                             'Prevention and stewardship (antimicrobials, opioids) are daily '
                             'responsibilities.',
                             "Primary references: Rang and Dale's Pharmacology; Katzung Basic & "
                             "Clinical Pharmacology; Goodman & Gilman's."]}],
 'clinical_pharmacy': [{'title': '1. Core concepts in Clinical Pharmacy',
                        'paras': ['High-yield undergraduate themes in clinical pharmacy for exams '
                                  'and practice.',
                                  'Connect mechanism → clinical effect → monitoring → counseling.',
                                  'Safety, legality, and evidence-based use are central to '
                                  'pharmacy.'],
                        'figure_name': 'fig_dose_response'},
                       {'title': '2. Clinical / practice patterns',
                        'paras': ['Recognize common presentations and risk situations in clinical '
                                  'pharmacy.',
                                  'Identify high-alert medicines and interaction red flags early.',
                                  'Document interventions and communicate clearly with the care '
                                  'team.']},
                       {'title': '3. Calculations, quality and decision-making',
                        'paras': ['Dose calculations, renal/hepatic adjustment, and TDM timing '
                                  'save lives.',
                                  'Formulation choice (IR vs MR, sterile vs nonsterile) changes '
                                  'outcomes.',
                                  'Use reliable references; do not rely on memory for critical '
                                  'doses.'],
                        'figure_name': 'fig_dose_response'},
                       {'title': '4. Errors, ADRs and systems safety',
                        'paras': ['Prevent look-alike/sound-alike errors and crush/MR mistakes.',
                                  'Report ADRs and near misses; improve systems, not only '
                                  'individuals.',
                                  'Know when to refer urgently (toxicology, sepsis, airway, '
                                  'bleed).']},
                       {'title': '5. Checklist and book anchors',
                        'paras': ['Checklist: indication, dose, interactions, allergies, organ '
                                  'function, counseling, follow-up.',
                                  'Prevention and stewardship (antimicrobials, opioids) are daily '
                                  'responsibilities.',
                                  'Primary references: Clinical Pharmacy and Therapeutics — '
                                  'Walker; Applied Therapeutics; Pharmacotherapy — DiPiro.']}],
 'pharmaceutics': [{'title': '1. Core concepts in Pharmaceutics',
                    'paras': ['High-yield undergraduate themes in pharmaceutics for exams and '
                              'practice.',
                              'Connect mechanism → clinical effect → monitoring → counseling.',
                              'Safety, legality, and evidence-based use are central to pharmacy.'],
                    'figure_name': 'fig_tooth'},
                   {'title': '2. Clinical / practice patterns',
                    'paras': ['Recognize common presentations and risk situations in '
                              'pharmaceutics.',
                              'Identify high-alert medicines and interaction red flags early.',
                              'Document interventions and communicate clearly with the care '
                              'team.']},
                   {'title': '3. Calculations, quality and decision-making',
                    'paras': ['Dose calculations, renal/hepatic adjustment, and TDM timing save '
                              'lives.',
                              'Formulation choice (IR vs MR, sterile vs nonsterile) changes '
                              'outcomes.',
                              'Use reliable references; do not rely on memory for critical doses.'],
                    'figure_name': 'fig_dose_response'},
                   {'title': '4. Errors, ADRs and systems safety',
                    'paras': ['Prevent look-alike/sound-alike errors and crush/MR mistakes.',
                              'Report ADRs and near misses; improve systems, not only individuals.',
                              'Know when to refer urgently (toxicology, sepsis, airway, bleed).']},
                   {'title': '5. Checklist and book anchors',
                    'paras': ['Checklist: indication, dose, interactions, allergies, organ '
                              'function, counseling, follow-up.',
                              'Prevention and stewardship (antimicrobials, opioids) are daily '
                              'responsibilities.',
                              "Primary references: Aulton's Pharmaceutics; Ansel's Pharmaceutical "
                              'Dosage Forms; Remington.']}],
 'pharmacokinetics': [{'title': '1. Core concepts in Pharmacokinetics',
                       'paras': ['High-yield undergraduate themes in pharmacokinetics for exams '
                                 'and practice.',
                                 'Connect mechanism → clinical effect → monitoring → counseling.',
                                 'Safety, legality, and evidence-based use are central to '
                                 'pharmacy.'],
                       'figure_name': 'fig_dose_response'},
                      {'title': '2. Clinical / practice patterns',
                       'paras': ['Recognize common presentations and risk situations in '
                                 'pharmacokinetics.',
                                 'Identify high-alert medicines and interaction red flags early.',
                                 'Document interventions and communicate clearly with the care '
                                 'team.']},
                      {'title': '3. Calculations, quality and decision-making',
                       'paras': ['Dose calculations, renal/hepatic adjustment, and TDM timing save '
                                 'lives.',
                                 'Formulation choice (IR vs MR, sterile vs nonsterile) changes '
                                 'outcomes.',
                                 'Use reliable references; do not rely on memory for critical '
                                 'doses.'],
                       'figure_name': 'fig_dose_response'},
                      {'title': '4. Errors, ADRs and systems safety',
                       'paras': ['Prevent look-alike/sound-alike errors and crush/MR mistakes.',
                                 'Report ADRs and near misses; improve systems, not only '
                                 'individuals.',
                                 'Know when to refer urgently (toxicology, sepsis, airway, '
                                 'bleed).']},
                      {'title': '5. Checklist and book anchors',
                       'paras': ['Checklist: indication, dose, interactions, allergies, organ '
                                 'function, counseling, follow-up.',
                                 'Prevention and stewardship (antimicrobials, opioids) are daily '
                                 'responsibilities.',
                                 'Primary references: Applied Biopharmaceutics & Pharmacokinetics '
                                 '— Shargel; Rowland and Tozer; Clinical Pharmacokinetics concepts '
                                 'texts.']}],
 'medicinal_chemistry': [{'title': '1. Core concepts in Medicinal Chemistry',
                          'paras': ['High-yield undergraduate themes in medicinal chemistry for '
                                    'exams and practice.',
                                    'Connect mechanism → clinical effect → monitoring → '
                                    'counseling.',
                                    'Safety, legality, and evidence-based use are central to '
                                    'pharmacy.'],
                          'figure_name': 'fig_dose_response'},
                         {'title': '2. Clinical / practice patterns',
                          'paras': ['Recognize common presentations and risk situations in '
                                    'medicinal chemistry.',
                                    'Identify high-alert medicines and interaction red flags '
                                    'early.',
                                    'Document interventions and communicate clearly with the care '
                                    'team.']},
                         {'title': '3. Calculations, quality and decision-making',
                          'paras': ['Dose calculations, renal/hepatic adjustment, and TDM timing '
                                    'save lives.',
                                    'Formulation choice (IR vs MR, sterile vs nonsterile) changes '
                                    'outcomes.',
                                    'Use reliable references; do not rely on memory for critical '
                                    'doses.'],
                          'figure_name': 'fig_dose_response'},
                         {'title': '4. Errors, ADRs and systems safety',
                          'paras': ['Prevent look-alike/sound-alike errors and crush/MR mistakes.',
                                    'Report ADRs and near misses; improve systems, not only '
                                    'individuals.',
                                    'Know when to refer urgently (toxicology, sepsis, airway, '
                                    'bleed).']},
                         {'title': '5. Checklist and book anchors',
                          'paras': ['Checklist: indication, dose, interactions, allergies, organ '
                                    'function, counseling, follow-up.',
                                    'Prevention and stewardship (antimicrobials, opioids) are '
                                    'daily responsibilities.',
                                    "Primary references: Foye's Principles of Medicinal Chemistry; "
                                    'Wilson and Gisvold; The Organic Chemistry of Drug Design.']}],
 'pharmacognosy': [{'title': '1. Core concepts in Pharmacognosy',
                    'paras': ['High-yield undergraduate themes in pharmacognosy for exams and '
                              'practice.',
                              'Connect mechanism → clinical effect → monitoring → counseling.',
                              'Safety, legality, and evidence-based use are central to pharmacy.'],
                    'figure_name': 'fig_growth'},
                   {'title': '2. Clinical / practice patterns',
                    'paras': ['Recognize common presentations and risk situations in '
                              'pharmacognosy.',
                              'Identify high-alert medicines and interaction red flags early.',
                              'Document interventions and communicate clearly with the care '
                              'team.']},
                   {'title': '3. Calculations, quality and decision-making',
                    'paras': ['Dose calculations, renal/hepatic adjustment, and TDM timing save '
                              'lives.',
                              'Formulation choice (IR vs MR, sterile vs nonsterile) changes '
                              'outcomes.',
                              'Use reliable references; do not rely on memory for critical doses.'],
                    'figure_name': 'fig_dose_response'},
                   {'title': '4. Errors, ADRs and systems safety',
                    'paras': ['Prevent look-alike/sound-alike errors and crush/MR mistakes.',
                              'Report ADRs and near misses; improve systems, not only individuals.',
                              'Know when to refer urgently (toxicology, sepsis, airway, bleed).']},
                   {'title': '5. Checklist and book anchors',
                    'paras': ['Checklist: indication, dose, interactions, allergies, organ '
                              'function, counseling, follow-up.',
                              'Prevention and stewardship (antimicrobials, opioids) are daily '
                              'responsibilities.',
                              'Primary references: Trease and Evans Pharmacognosy; Pharmacognosy '
                              'texts; WHO quality control herbal themes.']}],
 'pharmacy_practice': [{'title': '1. Core concepts in Pharmacy Practice',
                        'paras': ['High-yield undergraduate themes in pharmacy practice for exams '
                                  'and practice.',
                                  'Connect mechanism → clinical effect → monitoring → counseling.',
                                  'Safety, legality, and evidence-based use are central to '
                                  'pharmacy.'],
                        'figure_name': 'fig_radiograph'},
                       {'title': '2. Clinical / practice patterns',
                        'paras': ['Recognize common presentations and risk situations in pharmacy '
                                  'practice.',
                                  'Identify high-alert medicines and interaction red flags early.',
                                  'Document interventions and communicate clearly with the care '
                                  'team.']},
                       {'title': '3. Calculations, quality and decision-making',
                        'paras': ['Dose calculations, renal/hepatic adjustment, and TDM timing '
                                  'save lives.',
                                  'Formulation choice (IR vs MR, sterile vs nonsterile) changes '
                                  'outcomes.',
                                  'Use reliable references; do not rely on memory for critical '
                                  'doses.'],
                        'figure_name': 'fig_dose_response'},
                       {'title': '4. Errors, ADRs and systems safety',
                        'paras': ['Prevent look-alike/sound-alike errors and crush/MR mistakes.',
                                  'Report ADRs and near misses; improve systems, not only '
                                  'individuals.',
                                  'Know when to refer urgently (toxicology, sepsis, airway, '
                                  'bleed).']},
                       {'title': '5. Checklist and book anchors',
                        'paras': ['Checklist: indication, dose, interactions, allergies, organ '
                                  'function, counseling, follow-up.',
                                  'Prevention and stewardship (antimicrobials, opioids) are daily '
                                  'responsibilities.',
                                  'Primary references: Community Pharmacy — Rutter; Pharmacy '
                                  'Practice texts; Local professional standards/guidance.']}],
 'hospital_pharmacy': [{'title': '1. Core concepts in Hospital Pharmacy',
                        'paras': ['High-yield undergraduate themes in hospital pharmacy for exams '
                                  'and practice.',
                                  'Connect mechanism → clinical effect → monitoring → counseling.',
                                  'Safety, legality, and evidence-based use are central to '
                                  'pharmacy.'],
                        'figure_name': 'fig_radiograph'},
                       {'title': '2. Clinical / practice patterns',
                        'paras': ['Recognize common presentations and risk situations in hospital '
                                  'pharmacy.',
                                  'Identify high-alert medicines and interaction red flags early.',
                                  'Document interventions and communicate clearly with the care '
                                  'team.']},
                       {'title': '3. Calculations, quality and decision-making',
                        'paras': ['Dose calculations, renal/hepatic adjustment, and TDM timing '
                                  'save lives.',
                                  'Formulation choice (IR vs MR, sterile vs nonsterile) changes '
                                  'outcomes.',
                                  'Use reliable references; do not rely on memory for critical '
                                  'doses.'],
                        'figure_name': 'fig_dose_response'},
                       {'title': '4. Errors, ADRs and systems safety',
                        'paras': ['Prevent look-alike/sound-alike errors and crush/MR mistakes.',
                                  'Report ADRs and near misses; improve systems, not only '
                                  'individuals.',
                                  'Know when to refer urgently (toxicology, sepsis, airway, '
                                  'bleed).']},
                       {'title': '5. Checklist and book anchors',
                        'paras': ['Checklist: indication, dose, interactions, allergies, organ '
                                  'function, counseling, follow-up.',
                                  'Prevention and stewardship (antimicrobials, opioids) are daily '
                                  'responsibilities.',
                                  'Primary references: Hospital Pharmacy practice handbooks; ASHP '
                                  'guidelines themes; Injectable Drug Information references.']}],
 'toxicology': [{'title': '1. Core concepts in Toxicology',
                 'paras': ['High-yield undergraduate themes in toxicology for exams and practice.',
                           'Connect mechanism → clinical effect → monitoring → counseling.',
                           'Safety, legality, and evidence-based use are central to pharmacy.'],
                 'figure_name': 'fig_dose_response'},
                {'title': '2. Clinical / practice patterns',
                 'paras': ['Recognize common presentations and risk situations in toxicology.',
                           'Identify high-alert medicines and interaction red flags early.',
                           'Document interventions and communicate clearly with the care team.']},
                {'title': '3. Calculations, quality and decision-making',
                 'paras': ['Dose calculations, renal/hepatic adjustment, and TDM timing save '
                           'lives.',
                           'Formulation choice (IR vs MR, sterile vs nonsterile) changes outcomes.',
                           'Use reliable references; do not rely on memory for critical doses.'],
                 'figure_name': 'fig_dose_response'},
                {'title': '4. Errors, ADRs and systems safety',
                 'paras': ['Prevent look-alike/sound-alike errors and crush/MR mistakes.',
                           'Report ADRs and near misses; improve systems, not only individuals.',
                           'Know when to refer urgently (toxicology, sepsis, airway, bleed).']},
                {'title': '5. Checklist and book anchors',
                 'paras': ['Checklist: indication, dose, interactions, allergies, organ function, '
                           'counseling, follow-up.',
                           'Prevention and stewardship (antimicrobials, opioids) are daily '
                           'responsibilities.',
                           "Primary references: Goldfrank's Toxicologic Emergencies; Casarett & "
                           "Doull's Toxicology; Local poison center protocols."]}],
 'pharm_microbiology': [{'title': '1. Core concepts in Pharmaceutical Microbiology',
                         'paras': ['High-yield undergraduate themes in pharmaceutical microbiology '
                                   'for exams and practice.',
                                   'Connect mechanism → clinical effect → monitoring → counseling.',
                                   'Safety, legality, and evidence-based use are central to '
                                   'pharmacy.'],
                         'figure_name': 'fig_periodontium'},
                        {'title': '2. Clinical / practice patterns',
                         'paras': ['Recognize common presentations and risk situations in '
                                   'pharmaceutical microbiology.',
                                   'Identify high-alert medicines and interaction red flags early.',
                                   'Document interventions and communicate clearly with the care '
                                   'team.']},
                        {'title': '3. Calculations, quality and decision-making',
                         'paras': ['Dose calculations, renal/hepatic adjustment, and TDM timing '
                                   'save lives.',
                                   'Formulation choice (IR vs MR, sterile vs nonsterile) changes '
                                   'outcomes.',
                                   'Use reliable references; do not rely on memory for critical '
                                   'doses.'],
                         'figure_name': 'fig_dose_response'},
                        {'title': '4. Errors, ADRs and systems safety',
                         'paras': ['Prevent look-alike/sound-alike errors and crush/MR mistakes.',
                                   'Report ADRs and near misses; improve systems, not only '
                                   'individuals.',
                                   'Know when to refer urgently (toxicology, sepsis, airway, '
                                   'bleed).']},
                        {'title': '5. Checklist and book anchors',
                         'paras': ['Checklist: indication, dose, interactions, allergies, organ '
                                   'function, counseling, follow-up.',
                                   'Prevention and stewardship (antimicrobials, opioids) are daily '
                                   'responsibilities.',
                                   "Primary references: Hugo and Russell's Pharmaceutical "
                                   'Microbiology; Pharmaceutical Microbiology texts; GMP '
                                   'microbiology guidance.']}]}
