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


PDF_SECTIONS: dict[str, list[dict]] = {'oral_surgery': [{'title': '1. Core concepts in Oral Surgery',
                   'paras': ['This pack summarizes high-yield undergraduate themes in oral surgery '
                             'for clinic and exams.',
                             'Link anatomy and disease process to diagnosis, then to the safest '
                             'first management step.',
                             'Always correlate history, exam, and special tests (vitality, '
                             'probing, radiographs) before irreversible treatment.'],
                   'figure_name': 'fig_tooth'},
                  {'title': '2. Clinical presentation patterns',
                   'paras': ['Common presentations in oral surgery should be recognized early, '
                             'including red-flag emergencies.',
                             'Use localized vs spreading infection signs, pain patterns, and '
                             'systemic features to triage urgency.',
                             'Document findings clearly; consent discussions should include '
                             'material risks for the procedure planned.']},
                  {'title': '3. Investigations and decision-making',
                   'paras': ['Choose tests that change management. Avoid unnecessary radiation '
                             '(ALARA) and unnecessary invasive steps.',
                             'Vitality testing, periodontal charting, sensibility tests, and '
                             'appropriate imaging are specialty-dependent tools.',
                             'Re-evaluate after initial therapy; many dental diseases need staged '
                             'care rather than one-visit definitive treatment.'],
                   'figure_name': 'fig_radiograph'},
                  {'title': '4. Treatment principles and complications',
                   'paras': ['Know common complications and how to prevent them: nerve injury, '
                             'bleeding, pulp exposure, perio abscess, failed endodontics, '
                             'ORN/MRONJ risk contexts.',
                             'Infection control, isolation (rubber dam), and atraumatic technique '
                             'are cross-cutting safety skills.',
                             'Refer early when pathology, airway risk, or surgical complexity '
                             'exceeds your setting.']},
                  {'title': '5. Ward/clinic checklist and book anchors',
                   'paras': ['Checklist: medical history (bleeding, bisphosphonates, radiotherapy, '
                             'diabetes), allergies, vitals if unwell, focused exam, justified '
                             'imaging, consent.',
                             'Prevention counseling (hygiene, diet, fluoride, tobacco/alcohol) '
                             'belongs in almost every plan.',
                             "Primary references: Peterson's Principles of Oral and Maxillofacial "
                             'Surgery; Contemporary Oral and Maxillofacial Surgery — Hupp; Local '
                             'Anaesthesia in Dentistry.']}],
 'orthodontics': [{'title': '1. Core concepts in Orthodontics',
                   'paras': ['This pack summarizes high-yield undergraduate themes in orthodontics '
                             'for clinic and exams.',
                             'Link anatomy and disease process to diagnosis, then to the safest '
                             'first management step.',
                             'Always correlate history, exam, and special tests (vitality, '
                             'probing, radiographs) before irreversible treatment.'],
                   'figure_name': 'fig_tooth'},
                  {'title': '2. Clinical presentation patterns',
                   'paras': ['Common presentations in orthodontics should be recognized early, '
                             'including red-flag emergencies.',
                             'Use localized vs spreading infection signs, pain patterns, and '
                             'systemic features to triage urgency.',
                             'Document findings clearly; consent discussions should include '
                             'material risks for the procedure planned.']},
                  {'title': '3. Investigations and decision-making',
                   'paras': ['Choose tests that change management. Avoid unnecessary radiation '
                             '(ALARA) and unnecessary invasive steps.',
                             'Vitality testing, periodontal charting, sensibility tests, and '
                             'appropriate imaging are specialty-dependent tools.',
                             'Re-evaluate after initial therapy; many dental diseases need staged '
                             'care rather than one-visit definitive treatment.'],
                   'figure_name': 'fig_radiograph'},
                  {'title': '4. Treatment principles and complications',
                   'paras': ['Know common complications and how to prevent them: nerve injury, '
                             'bleeding, pulp exposure, perio abscess, failed endodontics, '
                             'ORN/MRONJ risk contexts.',
                             'Infection control, isolation (rubber dam), and atraumatic technique '
                             'are cross-cutting safety skills.',
                             'Refer early when pathology, airway risk, or surgical complexity '
                             'exceeds your setting.']},
                  {'title': '5. Ward/clinic checklist and book anchors',
                   'paras': ['Checklist: medical history (bleeding, bisphosphonates, radiotherapy, '
                             'diabetes), allergies, vitals if unwell, focused exam, justified '
                             'imaging, consent.',
                             'Prevention counseling (hygiene, diet, fluoride, tobacco/alcohol) '
                             'belongs in almost every plan.',
                             "Primary references: Proffit's Contemporary Orthodontics; Graber "
                             'Orthodontics; Handbook of Orthodontics — Cobourne.']}],
 'periodontics': [{'title': '1. Core concepts in Periodontics',
                   'paras': ['This pack summarizes high-yield undergraduate themes in periodontics '
                             'for clinic and exams.',
                             'Link anatomy and disease process to diagnosis, then to the safest '
                             'first management step.',
                             'Always correlate history, exam, and special tests (vitality, '
                             'probing, radiographs) before irreversible treatment.'],
                   'figure_name': 'fig_periodontium'},
                  {'title': '2. Clinical presentation patterns',
                   'paras': ['Common presentations in periodontics should be recognized early, '
                             'including red-flag emergencies.',
                             'Use localized vs spreading infection signs, pain patterns, and '
                             'systemic features to triage urgency.',
                             'Document findings clearly; consent discussions should include '
                             'material risks for the procedure planned.']},
                  {'title': '3. Investigations and decision-making',
                   'paras': ['Choose tests that change management. Avoid unnecessary radiation '
                             '(ALARA) and unnecessary invasive steps.',
                             'Vitality testing, periodontal charting, sensibility tests, and '
                             'appropriate imaging are specialty-dependent tools.',
                             'Re-evaluate after initial therapy; many dental diseases need staged '
                             'care rather than one-visit definitive treatment.'],
                   'figure_name': 'fig_radiograph'},
                  {'title': '4. Treatment principles and complications',
                   'paras': ['Know common complications and how to prevent them: nerve injury, '
                             'bleeding, pulp exposure, perio abscess, failed endodontics, '
                             'ORN/MRONJ risk contexts.',
                             'Infection control, isolation (rubber dam), and atraumatic technique '
                             'are cross-cutting safety skills.',
                             'Refer early when pathology, airway risk, or surgical complexity '
                             'exceeds your setting.']},
                  {'title': '5. Ward/clinic checklist and book anchors',
                   'paras': ['Checklist: medical history (bleeding, bisphosphonates, radiotherapy, '
                             'diabetes), allergies, vitals if unwell, focused exam, justified '
                             'imaging, consent.',
                             'Prevention counseling (hygiene, diet, fluoride, tobacco/alcohol) '
                             'belongs in almost every plan.',
                             "Primary references: Carranza's Clinical Periodontology; Lindhe's "
                             'Clinical Periodontology; Periodontology at a Glance.']}],
 'endodontics': [{'title': '1. Core concepts in Endodontics',
                  'paras': ['This pack summarizes high-yield undergraduate themes in endodontics '
                            'for clinic and exams.',
                            'Link anatomy and disease process to diagnosis, then to the safest '
                            'first management step.',
                            'Always correlate history, exam, and special tests (vitality, probing, '
                            'radiographs) before irreversible treatment.'],
                  'figure_name': 'fig_tooth'},
                 {'title': '2. Clinical presentation patterns',
                  'paras': ['Common presentations in endodontics should be recognized early, '
                            'including red-flag emergencies.',
                            'Use localized vs spreading infection signs, pain patterns, and '
                            'systemic features to triage urgency.',
                            'Document findings clearly; consent discussions should include '
                            'material risks for the procedure planned.']},
                 {'title': '3. Investigations and decision-making',
                  'paras': ['Choose tests that change management. Avoid unnecessary radiation '
                            '(ALARA) and unnecessary invasive steps.',
                            'Vitality testing, periodontal charting, sensibility tests, and '
                            'appropriate imaging are specialty-dependent tools.',
                            'Re-evaluate after initial therapy; many dental diseases need staged '
                            'care rather than one-visit definitive treatment.'],
                  'figure_name': 'fig_radiograph'},
                 {'title': '4. Treatment principles and complications',
                  'paras': ['Know common complications and how to prevent them: nerve injury, '
                            'bleeding, pulp exposure, perio abscess, failed endodontics, ORN/MRONJ '
                            'risk contexts.',
                            'Infection control, isolation (rubber dam), and atraumatic technique '
                            'are cross-cutting safety skills.',
                            'Refer early when pathology, airway risk, or surgical complexity '
                            'exceeds your setting.']},
                 {'title': '5. Ward/clinic checklist and book anchors',
                  'paras': ['Checklist: medical history (bleeding, bisphosphonates, radiotherapy, '
                            'diabetes), allergies, vitals if unwell, focused exam, justified '
                            'imaging, consent.',
                            'Prevention counseling (hygiene, diet, fluoride, tobacco/alcohol) '
                            'belongs in almost every plan.',
                            "Primary references: Cohen's Pathways of the Pulp; Endodontics — "
                            "Torabinejad; Ingle's Endodontics."]}],
 'prosthodontics': [{'title': '1. Core concepts in Prosthodontics',
                     'paras': ['This pack summarizes high-yield undergraduate themes in '
                               'prosthodontics for clinic and exams.',
                               'Link anatomy and disease process to diagnosis, then to the safest '
                               'first management step.',
                               'Always correlate history, exam, and special tests (vitality, '
                               'probing, radiographs) before irreversible treatment.'],
                     'figure_name': 'fig_tooth'},
                    {'title': '2. Clinical presentation patterns',
                     'paras': ['Common presentations in prosthodontics should be recognized early, '
                               'including red-flag emergencies.',
                               'Use localized vs spreading infection signs, pain patterns, and '
                               'systemic features to triage urgency.',
                               'Document findings clearly; consent discussions should include '
                               'material risks for the procedure planned.']},
                    {'title': '3. Investigations and decision-making',
                     'paras': ['Choose tests that change management. Avoid unnecessary radiation '
                               '(ALARA) and unnecessary invasive steps.',
                               'Vitality testing, periodontal charting, sensibility tests, and '
                               'appropriate imaging are specialty-dependent tools.',
                               'Re-evaluate after initial therapy; many dental diseases need '
                               'staged care rather than one-visit definitive treatment.'],
                     'figure_name': 'fig_radiograph'},
                    {'title': '4. Treatment principles and complications',
                     'paras': ['Know common complications and how to prevent them: nerve injury, '
                               'bleeding, pulp exposure, perio abscess, failed endodontics, '
                               'ORN/MRONJ risk contexts.',
                               'Infection control, isolation (rubber dam), and atraumatic '
                               'technique are cross-cutting safety skills.',
                               'Refer early when pathology, airway risk, or surgical complexity '
                               'exceeds your setting.']},
                    {'title': '5. Ward/clinic checklist and book anchors',
                     'paras': ['Checklist: medical history (bleeding, bisphosphonates, '
                               'radiotherapy, diabetes), allergies, vitals if unwell, focused '
                               'exam, justified imaging, consent.',
                               'Prevention counseling (hygiene, diet, fluoride, tobacco/alcohol) '
                               'belongs in almost every plan.',
                               'Primary references: Contemporary Fixed Prosthodontics — '
                               "Rosenstiel; McCracken's Removable Partial Prosthodontics; Complete "
                               'Denture Prosthodontics texts.']}],
 'pediatric_dentistry': [{'title': '1. Core concepts in Pediatric Dentistry',
                          'paras': ['This pack summarizes high-yield undergraduate themes in '
                                    'pediatric dentistry for clinic and exams.',
                                    'Link anatomy and disease process to diagnosis, then to the '
                                    'safest first management step.',
                                    'Always correlate history, exam, and special tests (vitality, '
                                    'probing, radiographs) before irreversible treatment.'],
                          'figure_name': 'fig_growth'},
                         {'title': '2. Clinical presentation patterns',
                          'paras': ['Common presentations in pediatric dentistry should be '
                                    'recognized early, including red-flag emergencies.',
                                    'Use localized vs spreading infection signs, pain patterns, '
                                    'and systemic features to triage urgency.',
                                    'Document findings clearly; consent discussions should include '
                                    'material risks for the procedure planned.']},
                         {'title': '3. Investigations and decision-making',
                          'paras': ['Choose tests that change management. Avoid unnecessary '
                                    'radiation (ALARA) and unnecessary invasive steps.',
                                    'Vitality testing, periodontal charting, sensibility tests, '
                                    'and appropriate imaging are specialty-dependent tools.',
                                    'Re-evaluate after initial therapy; many dental diseases need '
                                    'staged care rather than one-visit definitive treatment.'],
                          'figure_name': 'fig_radiograph'},
                         {'title': '4. Treatment principles and complications',
                          'paras': ['Know common complications and how to prevent them: nerve '
                                    'injury, bleeding, pulp exposure, perio abscess, failed '
                                    'endodontics, ORN/MRONJ risk contexts.',
                                    'Infection control, isolation (rubber dam), and atraumatic '
                                    'technique are cross-cutting safety skills.',
                                    'Refer early when pathology, airway risk, or surgical '
                                    'complexity exceeds your setting.']},
                         {'title': '5. Ward/clinic checklist and book anchors',
                          'paras': ['Checklist: medical history (bleeding, bisphosphonates, '
                                    'radiotherapy, diabetes), allergies, vitals if unwell, focused '
                                    'exam, justified imaging, consent.',
                                    'Prevention counseling (hygiene, diet, fluoride, '
                                    'tobacco/alcohol) belongs in almost every plan.',
                                    "Primary references: McDonald and Avery's Dentistry for the "
                                    'Child and Adolescent; Paediatric Dentistry — Welbury; '
                                    'Clinical Cases in Pediatric Dentistry.']}],
 'oral_medicine': [{'title': '1. Core concepts in Oral Medicine & Pathology',
                    'paras': ['This pack summarizes high-yield undergraduate themes in oral '
                              'medicine & pathology for clinic and exams.',
                              'Link anatomy and disease process to diagnosis, then to the safest '
                              'first management step.',
                              'Always correlate history, exam, and special tests (vitality, '
                              'probing, radiographs) before irreversible treatment.'],
                    'figure_name': 'fig_skin_layers'},
                   {'title': '2. Clinical presentation patterns',
                    'paras': ['Common presentations in oral medicine & pathology should be '
                              'recognized early, including red-flag emergencies.',
                              'Use localized vs spreading infection signs, pain patterns, and '
                              'systemic features to triage urgency.',
                              'Document findings clearly; consent discussions should include '
                              'material risks for the procedure planned.']},
                   {'title': '3. Investigations and decision-making',
                    'paras': ['Choose tests that change management. Avoid unnecessary radiation '
                              '(ALARA) and unnecessary invasive steps.',
                              'Vitality testing, periodontal charting, sensibility tests, and '
                              'appropriate imaging are specialty-dependent tools.',
                              'Re-evaluate after initial therapy; many dental diseases need staged '
                              'care rather than one-visit definitive treatment.'],
                    'figure_name': 'fig_radiograph'},
                   {'title': '4. Treatment principles and complications',
                    'paras': ['Know common complications and how to prevent them: nerve injury, '
                              'bleeding, pulp exposure, perio abscess, failed endodontics, '
                              'ORN/MRONJ risk contexts.',
                              'Infection control, isolation (rubber dam), and atraumatic technique '
                              'are cross-cutting safety skills.',
                              'Refer early when pathology, airway risk, or surgical complexity '
                              'exceeds your setting.']},
                   {'title': '5. Ward/clinic checklist and book anchors',
                    'paras': ['Checklist: medical history (bleeding, bisphosphonates, '
                              'radiotherapy, diabetes), allergies, vitals if unwell, focused exam, '
                              'justified imaging, consent.',
                              'Prevention counseling (hygiene, diet, fluoride, tobacco/alcohol) '
                              'belongs in almost every plan.',
                              'Primary references: Oral and Maxillofacial Pathology — Neville; '
                              "Cawson's Essentials of Oral Pathology; Oral Medicine — Odell."]}],
 'restorative': [{'title': '1. Core concepts in Restorative Dentistry',
                  'paras': ['This pack summarizes high-yield undergraduate themes in restorative '
                            'dentistry for clinic and exams.',
                            'Link anatomy and disease process to diagnosis, then to the safest '
                            'first management step.',
                            'Always correlate history, exam, and special tests (vitality, probing, '
                            'radiographs) before irreversible treatment.'],
                  'figure_name': 'fig_tooth'},
                 {'title': '2. Clinical presentation patterns',
                  'paras': ['Common presentations in restorative dentistry should be recognized '
                            'early, including red-flag emergencies.',
                            'Use localized vs spreading infection signs, pain patterns, and '
                            'systemic features to triage urgency.',
                            'Document findings clearly; consent discussions should include '
                            'material risks for the procedure planned.']},
                 {'title': '3. Investigations and decision-making',
                  'paras': ['Choose tests that change management. Avoid unnecessary radiation '
                            '(ALARA) and unnecessary invasive steps.',
                            'Vitality testing, periodontal charting, sensibility tests, and '
                            'appropriate imaging are specialty-dependent tools.',
                            'Re-evaluate after initial therapy; many dental diseases need staged '
                            'care rather than one-visit definitive treatment.'],
                  'figure_name': 'fig_radiograph'},
                 {'title': '4. Treatment principles and complications',
                  'paras': ['Know common complications and how to prevent them: nerve injury, '
                            'bleeding, pulp exposure, perio abscess, failed endodontics, ORN/MRONJ '
                            'risk contexts.',
                            'Infection control, isolation (rubber dam), and atraumatic technique '
                            'are cross-cutting safety skills.',
                            'Refer early when pathology, airway risk, or surgical complexity '
                            'exceeds your setting.']},
                 {'title': '5. Ward/clinic checklist and book anchors',
                  'paras': ['Checklist: medical history (bleeding, bisphosphonates, radiotherapy, '
                            'diabetes), allergies, vitals if unwell, focused exam, justified '
                            'imaging, consent.',
                            'Prevention counseling (hygiene, diet, fluoride, tobacco/alcohol) '
                            'belongs in almost every plan.',
                            "Primary references: Sturdevant's Art and Science of Operative "
                            "Dentistry; Summitt's Fundamentals of Operative Dentistry; Pickard's "
                            'Guide to Minimally Invasive Operative Dentistry.']}],
 'oral_radiology': [{'title': '1. Core concepts in Oral Radiology',
                     'paras': ['This pack summarizes high-yield undergraduate themes in oral '
                               'radiology for clinic and exams.',
                               'Link anatomy and disease process to diagnosis, then to the safest '
                               'first management step.',
                               'Always correlate history, exam, and special tests (vitality, '
                               'probing, radiographs) before irreversible treatment.'],
                     'figure_name': 'fig_radiograph'},
                    {'title': '2. Clinical presentation patterns',
                     'paras': ['Common presentations in oral radiology should be recognized early, '
                               'including red-flag emergencies.',
                               'Use localized vs spreading infection signs, pain patterns, and '
                               'systemic features to triage urgency.',
                               'Document findings clearly; consent discussions should include '
                               'material risks for the procedure planned.']},
                    {'title': '3. Investigations and decision-making',
                     'paras': ['Choose tests that change management. Avoid unnecessary radiation '
                               '(ALARA) and unnecessary invasive steps.',
                               'Vitality testing, periodontal charting, sensibility tests, and '
                               'appropriate imaging are specialty-dependent tools.',
                               'Re-evaluate after initial therapy; many dental diseases need '
                               'staged care rather than one-visit definitive treatment.'],
                     'figure_name': 'fig_tooth'},
                    {'title': '4. Treatment principles and complications',
                     'paras': ['Know common complications and how to prevent them: nerve injury, '
                               'bleeding, pulp exposure, perio abscess, failed endodontics, '
                               'ORN/MRONJ risk contexts.',
                               'Infection control, isolation (rubber dam), and atraumatic '
                               'technique are cross-cutting safety skills.',
                               'Refer early when pathology, airway risk, or surgical complexity '
                               'exceeds your setting.']},
                    {'title': '5. Ward/clinic checklist and book anchors',
                     'paras': ['Checklist: medical history (bleeding, bisphosphonates, '
                               'radiotherapy, diabetes), allergies, vitals if unwell, focused '
                               'exam, justified imaging, consent.',
                               'Prevention counseling (hygiene, diet, fluoride, tobacco/alcohol) '
                               'belongs in almost every plan.',
                               "Primary references: White and Pharoah's Oral Radiology; Essentials "
                               'of Dental Radiography; Oral Radiology principles texts.']}],
 'dental_anatomy': [{'title': '1. Core concepts in Dental Anatomy',
                     'paras': ['This pack summarizes high-yield undergraduate themes in dental '
                               'anatomy for clinic and exams.',
                               'Link anatomy and disease process to diagnosis, then to the safest '
                               'first management step.',
                               'Always correlate history, exam, and special tests (vitality, '
                               'probing, radiographs) before irreversible treatment.'],
                     'figure_name': 'fig_tooth'},
                    {'title': '2. Clinical presentation patterns',
                     'paras': ['Common presentations in dental anatomy should be recognized early, '
                               'including red-flag emergencies.',
                               'Use localized vs spreading infection signs, pain patterns, and '
                               'systemic features to triage urgency.',
                               'Document findings clearly; consent discussions should include '
                               'material risks for the procedure planned.']},
                    {'title': '3. Investigations and decision-making',
                     'paras': ['Choose tests that change management. Avoid unnecessary radiation '
                               '(ALARA) and unnecessary invasive steps.',
                               'Vitality testing, periodontal charting, sensibility tests, and '
                               'appropriate imaging are specialty-dependent tools.',
                               'Re-evaluate after initial therapy; many dental diseases need '
                               'staged care rather than one-visit definitive treatment.'],
                     'figure_name': 'fig_radiograph'},
                    {'title': '4. Treatment principles and complications',
                     'paras': ['Know common complications and how to prevent them: nerve injury, '
                               'bleeding, pulp exposure, perio abscess, failed endodontics, '
                               'ORN/MRONJ risk contexts.',
                               'Infection control, isolation (rubber dam), and atraumatic '
                               'technique are cross-cutting safety skills.',
                               'Refer early when pathology, airway risk, or surgical complexity '
                               'exceeds your setting.']},
                    {'title': '5. Ward/clinic checklist and book anchors',
                     'paras': ['Checklist: medical history (bleeding, bisphosphonates, '
                               'radiotherapy, diabetes), allergies, vitals if unwell, focused '
                               'exam, justified imaging, consent.',
                               'Prevention counseling (hygiene, diet, fluoride, tobacco/alcohol) '
                               'belongs in almost every plan.',
                               "Primary references: Wheeler's Dental Anatomy, Physiology and "
                               "Occlusion; Ash & Nelson's Dental Anatomy; Dental Anatomy review "
                               'guides.']}]}
