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
PDF_SECTIONS: dict[str, list[dict]] = {
    "cardiology": [
        {
            "title": "1. Core physiology & anatomy",
            "paras": [
                "Cardiac output (CO) = heart rate × stroke volume. Mean arterial pressure approximates CO × systemic vascular resistance. The Frank–Starling mechanism links increased venous return to increased stroke volume within physiologic limits.",
                "Coronary perfusion of the left ventricle occurs mainly in diastole. The right coronary artery usually supplies the SA node. Know the territories: LAD → anterior wall; RCA → inferior wall; circumflex → lateral wall.",
                "Valves: mitral and tricuspid are atrioventricular; aortic and pulmonic are semilunar. Auscultation points and radiation patterns are high-yield for undergraduate exams and wards.",
            ],
            "figure": fig_heart_flow,
        },
        {
            "title": "2. Ischemic heart disease & ECG ideas",
            "paras": [
                "Chronic coronary disease presents with exertional angina; acute coronary syndromes include unstable angina, NSTEMI, and STEMI. Time-critical reperfusion saves myocardium in STEMI.",
                "STEMI: ST elevation in contiguous leads (e.g., II/III/aVF inferior; V2–V4 anterior). NSTEMI: troponin rise without STEMI criteria. Always combine ECG with history, exam, and risk factors.",
                "Immediate priorities in ACS: ABCs, ECG within minutes, aspirin (if no contraindication), anticoagulation/antiplatelet strategy per protocol, and urgent reperfusion for STEMI.",
            ],
            "figure": fig_ecg_stemi,
        },
        {
            "title": "3. Heart failure & murmurs",
            "paras": [
                "Heart failure symptoms: dyspnea, orthopnea, PND, edema. Signs: raised JVP, crackles, S3, peripheral edema. BNP/NT-proBNP and echocardiography help confirm and classify HFrEF vs HFpEF.",
                "HFrEF cornerstone therapy commonly includes ACEi/ARB/ARNI, evidence-based beta-blocker, mineralocorticoid receptor antagonist, and SGLT2 inhibitor, with loop diuretics for congestion.",
                "Mitral regurgitation: holosystolic murmur to axilla. Aortic stenosis: crescendo–decrescendo systolic murmur to carotids, slow-rising pulse. Aortic regurgitation: early diastolic decrescendo. Mitral stenosis: diastolic rumble (± opening snap).",
            ],
        },
        {
            "title": "4. Arrhythmias & emergencies",
            "paras": [
                "AF: irregularly irregular pulse; risk-stratify stroke risk (e.g., CHA2DS2-VASc) and bleeding risk when considering anticoagulation. Rate vs rhythm control depends on context.",
                "Unstable tachycardia/bradycardia: follow ACLS-style pathways — if unstable with serious signs, prepare for synchronized cardioversion or pacing as indicated.",
                "Pericarditis: positional/pleuritic pain, diffuse STE with PR depression. Tamponade: Beck triad (hypotension, raised JVP, muffled sounds) — urgent echo and drainage.",
            ],
        },
        {
            "title": "5. Ward checklist & book anchors",
            "paras": [
                "Ward checklist: vitals + SpO2, focused CV exam, ECG, troponin if ACS suspected, CXR if HF/infection, echo when structural disease/HF suspected, medication review (beta-blockers, ACEi, diuretics, anticoagulants).",
                "Secondary prevention after MI: lifestyle, high-intensity statin when appropriate, antiplatelet therapy, BP/glucose control, cardiac rehab.",
                "Book anchors: Braunwald's Heart Disease; Harrison's cardiology sections; ECG Made Easy (Hampton). Prefer faculty-recommended editions.",
            ],
        },
    ],
    "ophthalmology": [
        {
            "title": "1. Globe anatomy essentials",
            "paras": [
                "Light path: cornea → anterior chamber → pupil → lens → vitreous → retina. The optic nerve carries visual signals; papilledema suggests raised ICP until proven otherwise.",
                "Extraocular muscles: LR6 (CN VI), SO4 (CN IV), all others CN III. CN III palsy: eye 'down and out' ± ptosis/pupil involvement. CN VI: failed abduction.",
                "Aqueous humor is produced by ciliary body and drains via trabecular meshwork/angle — critical for glaucoma pathophysiology.",
            ],
            "figure": fig_eye,
        },
        {
            "title": "2. Red eye & emergencies",
            "paras": [
                "Dangerous red eyes: acute angle-closure glaucoma, keratitis, uveitis, endophthalmitis, scleritis, orbital cellulitis. Conjunctivitis is common but should not show severe pain, vision loss, or fixed mid-dilated pupil.",
                "Acute angle closure: severe pain, halos, nausea, mid-dilated poorly reactive pupil, rock-hard eye — ophthalmic emergency. Avoid dilating drops.",
                "Chemical burns: immediate copious irrigation before detailed exam. Traumatic globe injury: shield, NPO, urgent specialty care — do not pressure the eye.",
            ],
        },
        {
            "title": "3. Visual loss patterns",
            "paras": [
                "Sudden painless vision loss differentials include retinal vascular occlusion, vitreous hemorrhage, retinal detachment (flashes/floaters/curtain), and optic neuropathies.",
                "Gradual loss: refractive error, cataract (reversible with surgery), glaucoma (field loss), macular degeneration (central loss), diabetic retinopathy.",
                "RAPD (swinging flashlight test) suggests optic nerve disease or extensive retinal disease on the affected side.",
            ],
        },
        {
            "title": "4. Diabetic & hypertensive eye disease",
            "paras": [
                "Diabetic retinopathy: microaneurysms, hemorrhages, hard exudates, cotton-wool spots; proliferative disease adds neovascularization and vitreous hemorrhage risk.",
                "Screening intervals matter — early laser/anti-VEGF/surgery pathways prevent blindness. Control glucose, blood pressure, and lipids.",
                "Hypertensive retinopathy grades include arteriolar narrowing, AV nicking, hemorrhages/exudates, and papilledema in malignant hypertension.",
            ],
        },
        {
            "title": "5. Study checklist & books",
            "paras": [
                "Exam checklist: visual acuity first, pupils (including RAPD), confrontational fields, motility, fluorescein stain when corneal disease suspected, fundoscopy, intraocular pressure when indicated.",
                "Never dismiss sudden vision loss or painful red eye with reduced acuity — escalate early.",
                "Books: Kanski's Clinical Ophthalmology; Vaughan & Asbury; faculty lecture notes for local protocols.",
            ],
        },
    ],
    "urology": [
        {
            "title": "1. Anatomy & stone disease",
            "paras": [
                "Kidneys → ureters → bladder → urethra. Loin-to-groin pain suggests ureteric colic. Microscopic or gross hematuria often accompanies stones.",
                "Stone types: calcium oxalate (most common), calcium phosphate, uric acid (often radiolucent on plain film), struvite (infection/urease organisms), cystine (genetic).",
                "Non-contrast CT KUB is the usual definitive imaging in non-pregnant adults. Ultrasound is preferred first-line in pregnancy.",
            ],
            "figure": fig_gu,
        },
        {
            "title": "2. Infection spectrum",
            "paras": [
                "Cystitis: dysuria, frequency, urgency, suprapubic discomfort — usually afebrile. Pyelonephritis: fever, flank pain, nausea — systemic illness.",
                "Complicated UTI: male sex, obstruction, stones, catheters, immunosuppression, pregnancy, anatomic abnormality — needs careful culture and follow-up.",
                "Obstruction + infection can rapidly progress to sepsis — urgent decompression may be required.",
            ],
        },
        {
            "title": "3. Hematuria & malignancy warnings",
            "paras": [
                "Painless gross hematuria in older adults (especially smokers) raises concern for urothelial carcinoma of the bladder — needs urologic workup.",
                "Renal cell carcinoma may present with hematuria, flank mass, or paraneoplastic features; many are incidental on imaging.",
                "Always ask about anticoagulation, trauma, infection, stones, and constitutional symptoms.",
            ],
        },
        {
            "title": "4. BPH, retention & scrotal emergencies",
            "paras": [
                "BPH causes storage and voiding LUTS in older men. Assess severity, infection, retention, creatinine, and medication effects.",
                "Acute urinary retention: painful inability to void — catheterize and investigate cause. Post-obstructive diuresis can follow relief of chronic obstruction.",
                "Testicular torsion: sudden severe pain in adolescent/young man — time-critical surgical emergency. Do not delay for imaging if high clinical suspicion.",
            ],
        },
        {
            "title": "5. Checklist & books",
            "paras": [
                "Checklist: vitals, abdominal/flank/genital exam, UA ± culture, pregnancy test when relevant, imaging tailored to suspicion, analgesia for colic, sepsis pathway if shocked.",
                "Books: Campbell-Walsh-Wein Urology; Smith's General Urology; Bailey & Love urology chapters.",
            ],
        },
    ],
    "neurology": [
        {
            "title": "1. Localization first",
            "paras": [
                "Neurology begins with localization: cortex, subcortex, brainstem, spinal cord, root, plexus, peripheral nerve, neuromuscular junction, muscle.",
                "UMN signs: spasticity, hyperreflexia, Babinski. LMN signs: flaccid weakness, hyporeflexia, fasciculations, atrophy.",
                "Time course matters: hyperacute (stroke/SAH), acute (infection/inflammation), subacute, chronic progressive, relapsing–remitting.",
            ],
            "figure": fig_neuron,
        },
        {
            "title": "2. Stroke & thunderclap headache",
            "paras": [
                "Stroke: sudden focal deficit — face/arm/speech pathways (FAST). Time is brain for thrombolysis/thrombectomy eligibility.",
                "Differentiate ischemic vs hemorrhagic with urgent non-contrast CT. Glucose check is mandatory (hypoglycemia mimics stroke).",
                "Thunderclap headache: peak intensity in seconds — exclude SAH with CT ± LP. Sentinel bleeds can precede catastrophic SAH.",
            ],
        },
        {
            "title": "3. Seizures, meningitis, raised ICP",
            "paras": [
                "First seizure workup: history (witness), glucose/electrolytes, consider CT/MRI and EEG as indicated. Status epilepticus is an emergency.",
                "Meningitis: fever, neck stiffness, altered mentation — early antibiotics after cultures when bacterial disease suspected; do not delay for imaging if unsafe delay.",
                "Raised ICP clues: headache worse lying down, vomiting, papilledema, focal signs — cautious LP only after risk assessment.",
            ],
        },
        {
            "title": "4. Common outpatient syndromes",
            "paras": [
                "Migraine: unilateral throbbing headache ± nausea, photo/phonophobia; red flags need exclusion (thunderclap, fever, focal neuro, cancer/immunosuppression, age >50 with new headache).",
                "Neuropathy patterns: length-dependent sensory loss in diabetes; entrapment neuropathies (carpal tunnel) are common.",
                "Parkinsonism: bradykinesia plus rest tremor/rigidity/postural instability — medication review for drug-induced causes.",
            ],
        },
        {
            "title": "5. Checklist & books",
            "paras": [
                "Checklist: ABCs, glucose, focused neuro exam (mental status, cranial nerves, motor, sensory, reflexes, coordination, gait), imaging/LP as indicated.",
                "Books: Adams and Victor; Harrison's neurology; local stroke pathway documents.",
            ],
        },
    ],
    "pulmonology": [
        {
            "title": "1. Respiratory physiology basics",
            "paras": [
                "Gas exchange requires ventilation, perfusion, and diffusion. Hypoxemia mechanisms: hypoventilation, V/Q mismatch, shunt, diffusion limitation, low inspired O2.",
                "Obstructive diseases reduce airflow (asthma, COPD); restrictive patterns reduce volumes (ILD, neuromuscular, kyphoscoliosis).",
                "ABG interpretation: look at pH, PaCO2, HCO3, PaO2 — decide acidosis/alkalosis and respiratory vs metabolic primary process.",
            ],
            "figure": fig_lung_zones,
        },
        {
            "title": "2. Pneumonia & severity",
            "paras": [
                "CAP classic organism: Streptococcus pneumoniae. Assess severity with tools such as CURB-65 and clinical judgment.",
                "Investigations: CXR, O2 sats, bloods, cultures when septic/hospitalized. Antibiotics according to local guidelines and risk for resistant organisms.",
                "Complications: parapneumonic effusion, empyema, abscess, respiratory failure, sepsis.",
            ],
        },
        {
            "title": "3. Asthma & COPD",
            "paras": [
                "Asthma: reversible obstruction and hyperresponsiveness; wheeze, dyspnea, cough; peak flow variability. Acute severe asthma is life-threatening — escalate early.",
                "COPD: progressive largely irreversible obstruction, usually smoking-related; exacerbations with infection/irritants. Oxygen targets are often controlled (e.g., 88–92%) in CO2 retainers — follow local protocol.",
                "Inhaler technique teaching is as important as the prescription.",
            ],
        },
        {
            "title": "4. PE, pneumothorax, TB",
            "paras": [
                "PE: sudden dyspnea/pleuritic pain with risk factors — Wells score guides D-dimer vs CT PA pathway.",
                "Tension pneumothorax: shock, tracheal deviation, absent breath sounds — immediate decompression, do not delay for CXR.",
                "TB: chronic cough, night sweats, weight loss, hemoptysis — infection control + microbiologic testing (AFB/NAAT) as available.",
            ],
        },
        {
            "title": "5. Checklist & books",
            "paras": [
                "Checklist: RR, SpO2, work of breathing, auscultation, CXR, ABG if tiring/hypercapnia risk, VTE risk, smoking history.",
                "Books: West's Respiratory Physiology; Harrison's respiratory chapters; Crofton & Douglas.",
            ],
        },
    ],
    "gastroenterology": [
        {
            "title": "1. Approach to abdominal pain",
            "paras": [
                "Characterize pain: onset, site, radiation, character, severity, relation to meals/defecation, associated vomiting/bleeding/fever/jaundice.",
                "Surgical abdomen red flags: peritonitis (guarding/rigidity), intractable vomiting, hemodynamic instability, suspected obstruction/perforation.",
                "Common UG diagnoses: appendicitis, cholecystitis, pancreatitis, PUD, diverticulitis, gastroenteritis, biliary colic, mesenteric ischemia (older/AF).",
            ],
            "figure": fig_biliary,
        },
        {
            "title": "2. Upper GI & H. pylori",
            "paras": [
                "Dyspepsia and peptic ulcer disease often link to H. pylori and NSAIDs. Alarm features (weight loss, anemia, dysphagia, bleeding, age thresholds) warrant endoscopy pathways.",
                "Upper GI bleed: resuscitation first, PPI per protocol, risk scores, endoscopy timing. Think varices in liver disease — airway and volume care.",
                "GERD is common; persistent symptoms or alarm features need further evaluation.",
            ],
        },
        {
            "title": "3. Hepatobiliary disease",
            "paras": [
                "Charcot triad (RUQ pain, fever, jaundice) = ascending cholangitis until proven otherwise. Reynolds pentad adds hypotension and confusion.",
                "Cholangitis needs antibiotics and biliary drainage (often ERCP). Obstructive LFTs show predominant ALP/GGT and bilirubin rise.",
                "Cirrhosis complications: variceal bleed, ascites, SBP, encephalopathy, hepatorenal syndrome, HCC surveillance.",
            ],
        },
        {
            "title": "4. Pancreas & bowel",
            "paras": [
                "Acute pancreatitis: epigastric pain to back + elevated lipase. Gallstones and alcohol are leading causes. Early care is supportive fluids/analgesia; severity scoring guides monitoring.",
                "Appendicitis: periumbilical pain migrating to RLQ, anorexia, McBurney's tenderness. Imaging when atypical.",
                "IBD vs IBS: alarm features, nocturnal diarrhea, bleeding, weight loss, anemia point away from simple IBS.",
            ],
        },
        {
            "title": "5. Checklist & books",
            "paras": [
                "Checklist: vitals, abdominal exam (including hernial orifices), pregnancy test, FBC/LFTs/lipase, AXR/US/CT as indicated, sepsis care if needed.",
                "Books: Sleisenger & Fordtran; Harrison's GI; Bailey & Love abdominal chapters.",
            ],
        },
    ],
    "endocrinology": [
        {
            "title": "1. Hormonal axes overview",
            "paras": [
                "Endocrine diagnosis uses clinical features plus paired hormone levels (e.g., TSH with free T4). Feedback loops explain many patterns.",
                "Diabetes mellitus: type 1 (insulin deficiency, DKA risk) vs type 2 (insulin resistance ± deficiency). Diagnose with fasting glucose, HbA1c, or OGTT per criteria.",
                "Always interpret labs with drugs, illness, and assay caveats in mind.",
            ],
            "figure": fig_hpa,
        },
        {
            "title": "2. Diabetes emergencies",
            "paras": [
                "DKA: hyperglycemia + ketosis + metabolic acidosis. Priorities: IV fluids, insulin, potassium monitoring/replacement. Do not start insulin if severe hypokalemia is uncorrected.",
                "HHS: marked hyperglycemia/hyperosmolarity, usually older T2DM, milder ketosis — careful fluid/electrolyte correction.",
                "Hypoglycemia: Whipple triad idea — low glucose, symptoms, resolution with glucose. Give fast carbohydrate or IV/IM glucagon pathways as needed.",
            ],
        },
        {
            "title": "3. Thyroid disease",
            "paras": [
                "Hypothyroidism (often Hashimoto in iodine-sufficient areas): fatigue, weight gain, cold intolerance, bradycardia — high TSH, low free T4 in primary disease.",
                "Hyperthyroidism/Graves: heat intolerance, weight loss, tremor, tachycardia, goiter ± orbitopathy — low TSH, high free T4/T3.",
                "Thyroid storm and myxedema coma are ICU-level emergencies.",
            ],
        },
        {
            "title": "4. Adrenal, calcium, pituitary",
            "paras": [
                "Adrenal insufficiency crisis: shock, hyponatremia, hyperkalemia — give stress-dose steroids and fluids urgently while investigating.",
                "Hypercalcemia: 'stones, bones, groans, psychiatric overtones'; ECG QT changes; treat severe cases urgently. Hypocalcemia: tetany, Chvostek/Trousseau.",
                "Pituitary masses may present with headache/visual field defects (bitemporal hemianopia) and hormone excess/deficiency.",
            ],
        },
        {
            "title": "5. Checklist & books",
            "paras": [
                "Checklist: glucose/ketones, TFTs, electrolytes/calcium, medication list (steroids, amiodarone, lithium), sick-day rules teaching for adrenal/diabetes patients.",
                "Books: Williams Textbook of Endocrinology; Greenspan; Harrison's endocrine chapters.",
            ],
        },
    ],
    "nephrology": [
        {
            "title": "1. Kidney function & AKI framework",
            "paras": [
                "eGFR estimated from creatinine is the everyday index of kidney function, but acute changes, low muscle mass, and drugs affect interpretation.",
                "AKI: rise in creatinine or drop in urine output. Classify pre-renal, intrinsic, post-renal. History of volume loss, nephrotoxins, obstruction is essential.",
                "Muddy brown casts suggest ATN; RBC casts suggest glomerulonephritis; sterile pyuria may suggest AIN/TB depending on context.",
            ],
            "figure": fig_nephron,
        },
        {
            "title": "2. Nephritic vs nephrotic",
            "paras": [
                "Nephritic: hematuria, hypertension, oliguria, mild–moderate proteinuria, rising creatinine.",
                "Nephrotic: heavy proteinuria (>3.5 g/day), hypoalbuminemia, edema, hyperlipidemia; complications include thrombosis and infection.",
                "Causes differ by age: MCD common in children; membranous/FSGS/diabetic kidney disease important in adults.",
            ],
        },
        {
            "title": "3. CKD & diabetic kidney disease",
            "paras": [
                "CKD staging uses GFR categories and albuminuria. Slow progression with BP control, ACEI/ARB in albuminuric disease, SGLT2i in many diabetic/CKD pathways, diabetes control, avoid nephrotoxins.",
                "Complications: anemia, bone mineral disorder, acidosis, hyperkalemia, volume overload, CVD risk.",
                "Refer early when GFR declines rapidly, complications are hard to manage, or transplant/dialysis planning is needed.",
            ],
        },
        {
            "title": "4. Electrolytes emergencies",
            "paras": [
                "Hyperkalemia with ECG changes is an emergency: stabilize membrane (calcium), shift K inward, remove K, address cause.",
                "Hyponatremia: assess volume status and tonicity; correct carefully to avoid osmotic demyelination. Hypernatremia usually means water deficit.",
                "Acid–base paired with electrolytes unlocks many diagnoses (e.g., RTA vs diarrhea, anion-gap metabolic acidosis list).",
            ],
        },
        {
            "title": "5. Checklist & books",
            "paras": [
                "Checklist: volume status, daily weights, urine dipstick ± microscopy, creatinine/eGFR/electrolytes, bladder scan/US for obstruction, drug review (NSAIDs, ACEi, gentamicin, contrast).",
                "Books: Brenner & Rector; Comprehensive Clinical Nephrology; Harrison's nephrology.",
            ],
        },
    ],
    "orthopedics": [
        {
            "title": "1. Fracture principles",
            "paras": [
                "Describe fractures: bone, open vs closed, location, pattern (transverse/oblique/spiral/comminuted), displacement/angulation, joint involvement.",
                "ATLS first for major trauma. Open fractures need antibiotics, tetanus status, and urgent ortho. Immobilize and assess neurovascular status before and after reduction/splinting.",
                "Colles fracture: FOOSH → distal radius dorsal angulation. Hip fracture in elderly: shortened externally rotated limb.",
            ],
            "figure": fig_joint,
        },
        {
            "title": "2. Compartment syndrome & emergencies",
            "paras": [
                "Compartment syndrome: pain out of proportion, pain on passive stretch, tense compartments — pulses may still be present. Urgent fasciotomy pathway.",
                "Fat embolism after long-bone fracture: respiratory distress, neurologic change, petechial rash.",
                "Septic arthritis: hot swollen joint, inability to bear weight/fever — urgent aspiration and antibiotics after cultures; joint emergency.",
            ],
        },
        {
            "title": "3. Soft tissue & Ottawa rules",
            "paras": [
                "Ottawa ankle/knee rules reduce unnecessary radiographs after sprain mechanisms while catching clinically important fractures.",
                "Sprain grades and RICE/PEACE & LOVE style early care are common teaching frameworks; unstable injuries need specialty review.",
                "Back pain red flags: trauma, cancer history, infection signs, saddle anesthesia, bowel/bladder change, progressive neurology — consider cauda equina.",
            ],
        },
        {
            "title": "4. Pediatric & elective themes",
            "paras": [
                "Children: greenstick fractures, growth plate (Salter–Harris) injuries — growth disturbance risk. Non-accidental injury must be considered when history/injury mismatch.",
                "Osteoarthritis vs inflammatory arthritis patterns differ in morning stiffness duration, systemic features, and erosions.",
                "Pre-op optimization: VTE risk, infection risk, bone health, and rehab planning matter as much as the operation.",
            ],
        },
        {
            "title": "5. Checklist & books",
            "paras": [
                "Checklist: look/feel/move, neurovascular exam, joint above and below, appropriate X-rays (two views), analgesia, immobilize, escalate emergencies early.",
                "Books: Apley's System of Orthopaedics; Campbell's; Bailey & Love ortho chapters.",
            ],
        },
    ],
    "dermatology": [
        {
            "title": "1. Skin structure & lesion language",
            "paras": [
                "Learn lesion morphology: macule, papule, plaque, vesicle, bulla, pustule, nodule, ulcer. Distribution and arrangement (dermatomal, flexural, extensor) are diagnostic clues.",
                "Epidermis vs dermis vs subcutis depth helps distinguish superficial infections from deeper soft-tissue infection.",
                "Always ask about drugs, atopy, occupation, travel, contacts, immunosuppression, and systemic symptoms.",
            ],
            "figure": fig_skin_layers,
        },
        {
            "title": "2. Infection & infestation",
            "paras": [
                "Impetigo: honey-colored crusts, common in children, contagious. Cellulitis: spreading erythema, warmth, tenderness — mark borders and treat per guidelines.",
                "Abscess usually needs drainage. Necrotizing infection: pain out of proportion, rapid progression, systemic toxicity — surgical emergency.",
                "Scabies: intense nocturnal itch, finger webs/flexures; treat index case and close contacts; wash linens.",
            ],
        },
        {
            "title": "3. Inflammatory dermatoses",
            "paras": [
                "Eczema/atopic dermatitis: itchy flexural inflammation; emollients are foundation therapy. Psoriasis: well-demarcated plaques with silvery scale, extensor surfaces, Auspitz sign.",
                "Urticaria vs anaphylaxis: look for airway/breathing/circulation involvement — anaphylaxis is emergency adrenaline territory.",
                "Drug eruptions range from simple exanthem to SJS/TEN — stop culprit drug early and escalate severe reactions.",
            ],
        },
        {
            "title": "4. Skin cancer vigilance",
            "paras": [
                "ABCDE for melanoma: Asymmetry, Border irregularity, Color variation, Diameter, Evolving. Suspicious lesions need urgent specialist excision pathways.",
                "Basal cell carcinoma: pearly nodule with telangiectasia common. Squamous cell carcinoma: scaly/ulcerated nodule; higher metastasis risk than BCC.",
                "Sun protection counseling is preventive medicine.",
            ],
        },
        {
            "title": "5. Checklist & books",
            "paras": [
                "Checklist: full skin exam when relevant, lymph nodes for suspicious lesions, photograph/monitor, biopsy appropriately, infection control for contagious rashes.",
                "Books: Rook; Fitzpatrick; Habif Clinical Dermatology.",
            ],
        },
    ],
    "obgyn": [
        {
            "title": "1. Pregnancy basics",
            "paras": [
                "Confirm pregnancy with β-hCG; date by LMP and early ultrasound. Routine antenatal care screens for anemia, blood group/Rh, infections, and fetal anomalies per schedule.",
                "Physiologic changes: increased blood volume, hypercoagulability, reduced residual volume, delayed gastric emptying — important for drugs and anesthesia risk.",
                "Fetal heart often audible by Doppler around 10–12 weeks.",
            ],
            "figure": fig_pregnancy,
        },
        {
            "title": "2. Obstetric emergencies",
            "paras": [
                "Postpartum hemorrhage: 4 Ts — Tone (atony most common), Trauma, Tissue (retained placenta), Thrombin (coagulopathy). Uterine massage + oxytocin are first steps for atony.",
                "Eclampsia/pre-eclampsia: HTN after 20 weeks with proteinuria or organ dysfunction; severe features need urgent care; magnesium for seizure prevention/treatment per protocol.",
                "Shoulder dystocia, cord prolapse, and maternal collapse have drill-based responses — know your local obstetric emergency algorithms.",
            ],
        },
        {
            "title": "3. Early pregnancy problems",
            "paras": [
                "Ectopic pregnancy: positive hCG, pain/bleeding, empty uterus — can rupture. Prior PID/tubal surgery increases risk. Unstable patients need urgent surgery pathways.",
                "Miscarriage spectrum: threatened, inevitable, incomplete, complete, septic — assess bleeding, pain, hemodynamics, and products of conception.",
                "Molar pregnancy may present with exaggerated symptoms and characteristic ultrasound appearances.",
            ],
        },
        {
            "title": "4. Gynecology essentials",
            "paras": [
                "Abnormal uterine bleeding: structure vs non-structure framework (PALM-COEIN). Exclude pregnancy first in reproductive-age patients.",
                "PID: pelvic pain, cervical motion tenderness, fever — treat early to reduce infertility/ectopic risk; consider TOA if severe.",
                "Contraception counseling should cover efficacy, contraindications (e.g., estrogen and migraine with aura/thrombosis risk), and emergency contraception options.",
            ],
        },
        {
            "title": "5. Checklist & books",
            "paras": [
                "Checklist: pregnancy test, vitals, abdominal/pelvic exam as appropriate, fetal heart when viable pregnancy, ultrasound, bloods (FBC, group & save in bleeding), escalate PPH/eclampsia early.",
                "Books: Williams Obstetrics; Beckmann & Ling; Dutta Obstetrics.",
            ],
        },
    ],
    "pediatrics": [
        {
            "title": "1. Development & assessment",
            "paras": [
                "Assess children by age: airway anatomy, fluid requirements, drug doses (usually mg/kg), and developmental milestones. Always calculate weight-based doses carefully.",
                "Growth charts detect failure to thrive and chronic disease. Parental concern matters — listen carefully.",
                "APGAR at 1 and 5 minutes summarizes early newborn transition, not long-term outcome alone.",
            ],
            "figure": fig_growth,
        },
        {
            "title": "2. Fluid, fever & infection",
            "paras": [
                "ORS is first-line for most dehydrating diarrheas if the child can drink and is not in shock. IV fluids for severe dehydration/shock.",
                "Fever in neonates is serious until proven otherwise. Immunization history changes differential and urgency.",
                "Kawasaki disease: prolonged fever plus mucocutaneous signs — coronary aneurysm risk; early IVIG matters.",
            ],
        },
        {
            "title": "3. Respiratory & cardiac clues",
            "paras": [
                "Respiratory distress: count RR, look for recessions, grunting, nasal flaring, SpO2. Bronchiolitis, croup, pneumonia, and asthma mimics are common.",
                "Congenital heart disease may present with murmur, cyanosis, poor feeding, or shock in the ductal-dependent period — prostaglandin pathways in neonates are specialty-led emergencies.",
                "Avoid over-oxygenation pitfalls in some congenital lesions — follow specialty guidance.",
            ],
        },
        {
            "title": "4. Safeguarding & common wards topics",
            "paras": [
                "Safeguarding: injury inconsistent with history, delayed presentation, patterned bruises — escalate via local child-protection pathways.",
                "Vaccines: know live vaccines (e.g., MMR) vs inactivated; counsel parents on schedule and contraindications.",
                "Common wards: bronchiolitis supportive care, asthma action plans, gastroenteritis hydration, neonatal jaundice assessment.",
            ],
        },
        {
            "title": "5. Checklist & books",
            "paras": [
                "Checklist: age-specific normals, weight, hydration, work of breathing, rash, meningism, immunization status, safeguarding screen, caregiver understanding.",
                "Books: Nelson Textbook of Pediatrics; Lissauer Illustrated Paediatrics; local IMCI/hospital protocols.",
            ],
        },
    ],
}


FIGURES = {
    "fig_heart_flow": fig_heart_flow,
    "fig_ecg_stemi": fig_ecg_stemi,
    "fig_eye": fig_eye,
    "fig_nephron": fig_nephron,
    "fig_lung_zones": fig_lung_zones,
    "fig_biliary": fig_biliary,
    "fig_hpa": fig_hpa,
    "fig_joint": fig_joint,
    "fig_skin_layers": fig_skin_layers,
    "fig_pregnancy": fig_pregnancy,
    "fig_growth": fig_growth,
    "fig_neuron": fig_neuron,
    "fig_gu": fig_gu,
}
