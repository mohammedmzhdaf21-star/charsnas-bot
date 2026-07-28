"""Undergraduate medicine study content organized by specialty."""

from __future__ import annotations

import random

SPECIALTIES: dict[str, dict] = {
    "cardiology": {
        "label": "Cardiology",
        "questions": [
            {
                "question": "Which coronary artery most often supplies the SA node?",
                "options": [
                    "A) Left anterior descending",
                    "B) Right coronary artery",
                    "C) Circumflex artery",
                    "D) Posterior descending artery",
                ],
                "answer": "B) Right coronary artery",
                "explanation": "In most people the RCA supplies the SA node.",
            },
            {
                "question": "First-line acute treatment for stable angina symptom relief?",
                "options": [
                    "A) Digoxin",
                    "B) Sublingual nitroglycerin",
                    "C) Amiodarone",
                    "D) Spironolactone",
                ],
                "answer": "B) Sublingual nitroglycerin",
                "explanation": "Nitrates reduce preload and relieve anginal pain.",
            },
            {
                "question": "ECG finding most specific for STEMI localization to the inferior wall?",
                "options": [
                    "A) ST elevation in V1–V4",
                    "B) ST elevation in II, III, aVF",
                    "C) ST elevation in I, aVL, V5–V6",
                    "D) Diffuse ST elevation with PR depression",
                ],
                "answer": "B) ST elevation in II, III, aVF",
                "explanation": "Inferior STEMI shows STE in II, III, and aVF.",
            },
            {
                "question": "Which murmur is holosystolic and radiates to the axilla?",
                "options": [
                    "A) Aortic stenosis",
                    "B) Mitral regurgitation",
                    "C) Mitral stenosis",
                    "D) Aortic regurgitation",
                ],
                "answer": "B) Mitral regurgitation",
                "explanation": "MR is a holosystolic murmur radiating to the axilla.",
            },
        ],
        "cases": [
            {
                "title": "Crushing Chest Pain",
                "stem": (
                    "A 58-year-old man with diabetes has crushing retrosternal pain for 40 minutes, "
                    "diaphoresis, and nausea. ECG: ST elevation in V2–V4."
                ),
                "question": "Most likely diagnosis and immediate reperfusion strategy?",
                "answer": "Anterior STEMI. Urgent PCI (or fibrinolysis if PCI unavailable timely).",
                "discussion": "Anterior STEMI is usually LAD territory. Time-critical reperfusion saves myocardium.",
                "book_hint": "Braunwald's Heart Disease — Acute Coronary Syndromes",
            },
            {
                "title": "Dyspnea and Ankle Edema",
                "stem": (
                    "A 70-year-old with prior MI has orthopnea, bilateral crackles, and pitting edema. "
                    "BNP is elevated; echo EF 30%."
                ),
                "question": "Diagnosis and cornerstone drug classes?",
                "answer": "HFrEF. ACEi/ARB/ARNI, evidence-based beta-blocker, MRA, SGLT2i ± loop diuretic.",
                "discussion": "Guideline-directed medical therapy improves survival in HFrEF.",
                "book_hint": "Harrison's — Heart Failure",
            },
        ],
        "books": [
            "Braunwald's Heart Disease",
            "Harrison's Principles of Internal Medicine — Cardiology",
            "ECG Made Easy — John Hampton",
        ],
        "pdf_notes": [
            "ACS spectrum: unstable angina, NSTEMI, STEMI — treat as time-critical.",
            "STEMI: ST elevation in contiguous leads ± new LBBB; urgent reperfusion.",
            "HF signs: orthopnea, raised JVP, crackles, edema; confirm with BNP/echo.",
            "MR = holosystolic to axilla; AS = crescendo-decrescendo to carotids.",
            "Secondary prevention after MI: antiplatelet, statin, beta-blocker, ACEi as indicated.",
        ],
    },
    "ophthalmology": {
        "label": "Ophthalmology",
        "questions": [
            {
                "question": "Painful red eye with mid-dilated fixed pupil suggests?",
                "options": [
                    "A) Open-angle glaucoma",
                    "B) Acute angle-closure glaucoma",
                    "C) Conjunctivitis",
                    "D) Cataract",
                ],
                "answer": "B) Acute angle-closure glaucoma",
                "explanation": "Acute angle closure: painful red eye, halos, mid-dilated nonreactive pupil.",
            },
            {
                "question": "Relative afferent pupillary defect (RAPD) is tested with?",
                "options": [
                    "A) Cover-uncover test",
                    "B) Swinging flashlight test",
                    "C) Schirmer test",
                    "D) Tonometry alone",
                ],
                "answer": "B) Swinging flashlight test",
                "explanation": "RAPD is detected by the swinging flashlight test.",
            },
            {
                "question": "Most common cause of irreversible blindness in the elderly in many regions?",
                "options": [
                    "A) Cataract",
                    "B) Age-related macular degeneration",
                    "C) Pterygium",
                    "D) Hordeolum",
                ],
                "answer": "B) Age-related macular degeneration",
                "explanation": "AMD is a leading cause of irreversible central vision loss in older adults; cataract is reversible with surgery.",
            },
            {
                "question": "Which cranial nerve palsy causes impaired abduction of the eye?",
                "options": ["A) CN II", "B) CN III", "C) CN IV", "D) CN VI"],
                "answer": "D) CN VI",
                "explanation": "CN VI (abducens) innervates lateral rectus → abduction.",
            },
        ],
        "cases": [
            {
                "title": "Sudden Painful Red Eye",
                "stem": (
                    "A 55-year-old hyperopic woman develops sudden severe eye pain, headache, "
                    "halos around lights, nausea, and a mid-dilated poorly reactive pupil."
                ),
                "question": "Most likely diagnosis and urgency?",
                "answer": "Acute angle-closure glaucoma — ophthalmic emergency.",
                "discussion": "Lower IOP urgently (meds ± laser/surgery). Avoid dilating drops.",
                "book_hint": "Kanski's Clinical Ophthalmology — Glaucoma",
            },
            {
                "title": "Painless Vision Loss in a Diabetic",
                "stem": (
                    "A 62-year-old with long-standing diabetes notes gradual blurred vision. "
                    "Fundoscopy shows microaneurysms, dot-blot hemorrhages, and hard exudates."
                ),
                "question": "Diagnosis?",
                "answer": "Diabetic retinopathy (non-proliferative features described).",
                "discussion": "Screen diabetics regularly; control glucose/BP; refer for macular edema or proliferative disease.",
                "book_hint": "Kanski — Retinal Vascular Disease",
            },
        ],
        "books": [
            "Kanski's Clinical Ophthalmology",
            "Vaughan & Asbury's General Ophthalmology",
            "Clinical Ophthalmology — Parsons' ",
        ],
        "pdf_notes": [
            "Red eye emergencies: angle-closure glaucoma, keratitis, uveitis, endophthalmitis.",
            "RAPD: swinging flashlight test — optic nerve / severe retinal disease.",
            "Diabetic retinopathy: microaneurysms, hemorrhages, exudates ± neovascularization.",
            "CN III palsy: eye 'down and out'; CN VI: failed abduction.",
            "Cataract: reversible surgically; AMD: irreversible central loss if advanced.",
        ],
    },
    "urology": {
        "label": "Urology",
        "questions": [
            {
                "question": "Most common composition of renal stones in adults?",
                "options": [
                    "A) Uric acid",
                    "B) Calcium oxalate",
                    "C) Struvite",
                    "D) Cystine",
                ],
                "answer": "B) Calcium oxalate",
                "explanation": "Calcium oxalate stones are the most common.",
            },
            {
                "question": "Flank pain radiating to the groin with hematuria is classic for?",
                "options": [
                    "A) Acute prostatitis",
                    "B) Ureteric colic",
                    "C) Epididymitis",
                    "D) Bladder cancer only",
                ],
                "answer": "B) Ureteric colic",
                "explanation": "Ureteric stone colic radiates loin to groin ± hematuria.",
            },
            {
                "question": "First imaging choice for suspected ureteric stone in non-pregnant adults?",
                "options": [
                    "A) IVP only",
                    "B) Non-contrast CT KUB",
                    "C) MRI abdomen first",
                    "D) PET scan",
                ],
                "answer": "B) Non-contrast CT KUB",
                "explanation": "Non-contrast CT is the standard for stone detection.",
            },
            {
                "question": "Painless gross hematuria in an older smoker most concerning for?",
                "options": [
                    "A) Simple UTI always",
                    "B) Bladder cancer",
                    "C) Stress incontinence",
                    "D) Hydrocele",
                ],
                "answer": "B) Bladder cancer",
                "explanation": "Painless hematuria in smokers raises concern for urothelial carcinoma.",
            },
        ],
        "cases": [
            {
                "title": "Loin-to-Groin Pain",
                "stem": (
                    "A 35-year-old man has sudden severe left flank pain radiating to the groin, "
                    "restlessness, and microscopic hematuria. Afebrile."
                ),
                "question": "Most likely diagnosis and preferred imaging?",
                "answer": "Ureteric colic (stone). Non-contrast CT KUB.",
                "discussion": "Analgesia, hydration as appropriate, urology referral if obstruction/infection/large stone.",
                "book_hint": "Campbell-Walsh-Wein Urology — Urinary Lithiasis",
            },
            {
                "title": "Fever and Flank Pain",
                "stem": (
                    "A 28-year-old woman has fever, flank tenderness, dysuria, and vomiting. "
                    "Urinalysis: nitrites and many WBC."
                ),
                "question": "Diagnosis and initial management idea?",
                "answer": "Acute pyelonephritis. Culture + empiric antibiotics; image if not improving or complicated.",
                "discussion": "Differentiate from simple cystitis; watch for sepsis and obstruction.",
                "book_hint": "Harrison's — Urinary Tract Infections",
            },
        ],
        "books": [
            "Campbell-Walsh-Wein Urology",
            "Smith's General Urology",
            "Bailey & Love — Urology chapters",
        ],
        "pdf_notes": [
            "Stone types: calcium oxalate most common; struvite with urease organisms; uric acid radiolucent.",
            "Loin→groin pain + hematuria = ureteric colic until proven otherwise.",
            "Painless hematuria: rule out malignancy (esp. smokers).",
            "Pyelonephritis: fever + flank pain + UTI signs → antibiotics ± imaging.",
            "BPH: storage/voiding symptoms in older men; assess PSA/exam judiciously.",
        ],
    },
    "neurology": {
        "label": "Neurology",
        "questions": [
            {
                "question": "Sudden unilateral weakness with aphasia most suggests?",
                "options": [
                    "A) Bell's palsy",
                    "B) Acute ischemic stroke",
                    "C) Myasthenia gravis",
                    "D) Absence seizure",
                ],
                "answer": "B) Acute ischemic stroke",
                "explanation": "Focal deficit of sudden onset is stroke until proven otherwise.",
            },
            {
                "question": "Upper motor neuron signs include?",
                "options": [
                    "A) Fasciculations and hyporeflexia",
                    "B) Spasticity and Babinski sign",
                    "C) Flaccid paralysis only",
                    "D) Distal sensory loss only",
                ],
                "answer": "B) Spasticity and Babinski sign",
                "explanation": "UMN: spasticity, hyperreflexia, Babinski.",
            },
            {
                "question": "First-line abortive therapy for mild–moderate migraine often includes?",
                "options": [
                    "A) Triptans / NSAIDs as appropriate",
                    "B) IV phenytoin always",
                    "C) High-dose steroids first-line for all",
                    "D) Antibiotics",
                ],
                "answer": "A) Triptans / NSAIDs as appropriate",
                "explanation": "NSAIDs or triptans are common abortive options depending on severity/contraindications.",
            },
            {
                "question": "Kernig and Brudzinski signs are associated with?",
                "options": [
                    "A) Meningeal irritation",
                    "B) Cerebellar stroke only",
                    "C) Carpal tunnel",
                    "D) Migraine aura only",
                ],
                "answer": "A) Meningeal irritation",
                "explanation": "They suggest meningeal irritation (e.g., meningitis).",
            },
        ],
        "cases": [
            {
                "title": "Thunderclap Headache",
                "stem": (
                    "A 45-year-old has the worst headache of life peaking within seconds, with neck stiffness. "
                    "CT head non-contrast is the first test."
                ),
                "question": "What diagnosis must be excluded urgently?",
                "answer": "Subarachnoid hemorrhage.",
                "discussion": "If CT early is negative but suspicion high, consider LP. SAH is a neurosurgical emergency.",
                "book_hint": "Adams and Victor's Principles of Neurology — Stroke/SAH",
            },
            {
                "title": "Fever and Neck Stiffness",
                "stem": (
                    "A 21-year-old student has fever, photophobia, nuchal rigidity, and confusion."
                ),
                "question": "Immediate priorities?",
                "answer": "ABCs, blood cultures, empiric IV antibiotics (± steroids per protocol), LP if safe.",
                "discussion": "Do not delay antibiotics for CT/LP if bacterial meningitis is likely.",
                "book_hint": "Harrison's — Meningitis",
            },
        ],
        "books": [
            "Adams and Victor's Principles of Neurology",
            "Harrison's — Neurology",
            "Clinical Neurology — Simon R. / Brazis",
        ],
        "pdf_notes": [
            "Stroke = sudden focal deficit — time is brain; use FAST/NIHSS pathways.",
            "UMN vs LMN: spasticity/hyperreflexia vs flaccid/hyporeflexia/fasciculations.",
            "SAH: thunderclap headache — urgent non-contrast CT ± LP.",
            "Meningitis: fever, neck stiffness, altered mentation — early antibiotics.",
            "Migraine: unilateral throbbing ± nausea/photo-phonophobia; rule out red flags.",
        ],
    },
    "pulmonology": {
        "label": "Pulmonology",
        "questions": [
            {
                "question": "Most common organism in community-acquired pneumonia?",
                "options": [
                    "A) Staphylococcus aureus",
                    "B) Streptococcus pneumoniae",
                    "C) Pseudomonas aeruginosa",
                    "D) Mycobacterium tuberculosis",
                ],
                "answer": "B) Streptococcus pneumoniae",
                "explanation": "S. pneumoniae is the leading cause of CAP.",
            },
            {
                "question": "Asthma is characterized by?",
                "options": [
                    "A) Fixed irreversible obstruction only",
                    "B) Reversible airway obstruction and hyperresponsiveness",
                    "C) Always normal spirometry",
                    "D) Digoxin deficiency",
                ],
                "answer": "B) Reversible airway obstruction and hyperresponsiveness",
                "explanation": "Asthma features reversible obstruction and airway hyperresponsiveness.",
            },
            {
                "question": "CURB-65 is used to assess severity of?",
                "options": [
                    "A) Asthma only",
                    "B) Community-acquired pneumonia",
                    "C) Pulmonary embolism only",
                    "D) Lung cancer staging",
                ],
                "answer": "B) Community-acquired pneumonia",
                "explanation": "CURB-65 helps risk-stratify CAP.",
            },
            {
                "question": "Wells score helps estimate probability of?",
                "options": [
                    "A) Appendicitis",
                    "B) Pulmonary embolism",
                    "C) Migraine",
                    "D) Cataract",
                ],
                "answer": "B) Pulmonary embolism",
                "explanation": "Wells criteria stratify PE probability.",
            },
        ],
        "cases": [
            {
                "title": "Fever and Productive Cough",
                "stem": (
                    "A 64-year-old smoker has fever, rusty sputum, tachypnea, and bronchial breath sounds "
                    "at the right base. CXR shows lobar consolidation."
                ),
                "question": "Most likely diagnosis?",
                "answer": "Community-acquired lobar pneumonia (classically pneumococcal).",
                "discussion": "Assess severity (CURB-65), cultures as indicated, timely antibiotics, oxygen if hypoxic.",
                "book_hint": "Harrison's — Pneumonia",
            },
            {
                "title": "Sudden Dyspnea after Long Flight",
                "stem": (
                    "A 40-year-old woman after a long flight has sudden dyspnea, pleuritic pain, and tachycardia. "
                    "SpO2 90% on air."
                ),
                "question": "Top diagnosis to exclude?",
                "answer": "Pulmonary embolism.",
                "discussion": "Use Wells/PERC appropriately; D-dimer or CT PA per pathway; start anticoagulation if PE confirmed and no contraindication.",
                "book_hint": "Harrison's — Venous Thromboembolism",
            },
        ],
        "books": [
            "West's Respiratory Physiology",
            "Harrison's — Respiratory Medicine",
            "Crofton and Douglas's Respiratory Diseases",
        ],
        "pdf_notes": [
            "CAP: S. pneumoniae most common; assess CURB-65 severity.",
            "Asthma: reversible obstruction; COPD: largely irreversible.",
            "PE: sudden dyspnea/pleuritic pain post-risk — Wells + CT PA pathway.",
            "Tension pneumothorax: shock + tracheal deviation — immediate decompression.",
            "TB: chronic cough, night sweats, weight loss — AFB/GeneXpert as available.",
        ],
    },
    "gastroenterology": {
        "label": "Gastroenterology",
        "questions": [
            {
                "question": "H. pylori is most strongly associated with?",
                "options": [
                    "A) Diverticulitis only",
                    "B) Peptic ulcer disease",
                    "C) Gallstones only",
                    "D) Appendicitis",
                ],
                "answer": "B) Peptic ulcer disease",
                "explanation": "H. pylori is a major cause of peptic ulcer disease.",
            },
            {
                "question": "Charcot triad indicates?",
                "options": [
                    "A) Acute appendicitis",
                    "B) Ascending cholangitis",
                    "C) Pancreatic cancer only",
                    "D) IBS",
                ],
                "answer": "B) Ascending cholangitis",
                "explanation": "RUQ pain + fever + jaundice = Charcot triad.",
            },
            {
                "question": "Most common cause of cirrhosis worldwide historically related to?",
                "options": [
                    "A) Alcohol and chronic viral hepatitis (major causes)",
                    "B) Vitamin C deficiency alone",
                    "C) Migraine",
                    "D) Otitis media",
                ],
                "answer": "A) Alcohol and chronic viral hepatitis (major causes)",
                "explanation": "Alcohol and chronic HBV/HCV are major cirrhosis causes (NAFLD also rising).",
            },
            {
                "question": "McBurney's point tenderness suggests?",
                "options": [
                    "A) Cholecystitis",
                    "B) Appendicitis",
                    "C) Pyelonephritis",
                    "D) Pancreatitis",
                ],
                "answer": "B) Appendicitis",
                "explanation": "McBurney's point tenderness is classic for appendicitis.",
            },
        ],
        "cases": [
            {
                "title": "RUQ Pain and Jaundice",
                "stem": (
                    "A 45-year-old woman with obesity has RUQ pain, fever, and jaundice. "
                    "Labs: ↑ ALP, ↑ bilirubin, ↑ WBC."
                ),
                "question": "Most likely diagnosis?",
                "answer": "Ascending cholangitis.",
                "discussion": "Needs antibiotics and biliary decompression (often ERCP).",
                "book_hint": "Sleisenger and Fordtran's — Biliary Disease",
            },
            {
                "title": "Epigastric Pain Radiating to Back",
                "stem": (
                    "A 40-year-old with heavy alcohol use has severe epigastric pain radiating to the back, "
                    "vomiting, and elevated lipase."
                ),
                "question": "Diagnosis and initial care focus?",
                "answer": "Acute pancreatitis. Supportive care: fluids, analgesia, monitor complications.",
                "discussion": "Gallstones and alcohol are common causes. Score severity; avoid early routine antibiotics.",
                "book_hint": "Harrison's — Pancreatitis",
            },
        ],
        "books": [
            "Sleisenger and Fordtran's Gastrointestinal and Liver Disease",
            "Harrison's — Gastroenterology",
            "Bailey & Love — Abdominal surgery chapters",
        ],
        "pdf_notes": [
            "Charcot triad = cholangitis; Reynolds pentad adds hypotension + confusion.",
            "H. pylori → PUD; test-and-treat in appropriate settings.",
            "Pancreatitis: epigastric pain to back + ↑ lipase; fluids and support.",
            "Appendicitis: periumbilical→RLQ pain, McBurney's tenderness.",
            "Cirrhosis complications: varices, ascites, encephalopathy, HCC surveillance.",
        ],
    },
    "endocrinology": {
        "label": "Endocrinology",
        "questions": [
            {
                "question": "DKA laboratory triad includes?",
                "options": [
                    "A) Hypoglycemia + alkalosis + low ketones",
                    "B) Hyperglycemia + ketosis + metabolic acidosis",
                    "C) Hyponatremia alone",
                    "D) Isolated hypercalcemia",
                ],
                "answer": "B) Hyperglycemia + ketosis + metabolic acidosis",
                "explanation": "DKA = hyperglycemia, ketones, anion-gap metabolic acidosis.",
            },
            {
                "question": "Most common cause of primary hypothyroidism in iodine-sufficient areas?",
                "options": [
                    "A) Hashimoto thyroiditis",
                    "B) Graves disease",
                    "C) Thyroid storm",
                    "D) Pheochromocytoma",
                ],
                "answer": "A) Hashimoto thyroiditis",
                "explanation": "Hashimoto's is the leading cause of hypothyroidism in iodine-sufficient regions.",
            },
            {
                "question": "First-line drug for most patients with type 2 diabetes (if tolerated)?",
                "options": [
                    "A) Metformin",
                    "B) Regular insulin only always",
                    "C) Propylthiouracil",
                    "D) Desmopressin",
                ],
                "answer": "A) Metformin",
                "explanation": "Metformin is usual first-line pharmacotherapy for T2DM if no contraindication.",
            },
            {
                "question": "Chvostek and Trousseau signs suggest?",
                "options": [
                    "A) Hyperkalemia",
                    "B) Hypocalcemia",
                    "C) Hypernatremia",
                    "D) Hypoglycemia only",
                ],
                "answer": "B) Hypocalcemia",
                "explanation": "These signs indicate neuromuscular irritability from hypocalcemia.",
            },
        ],
        "cases": [
            {
                "title": "Polyuria and Kussmaul Breathing",
                "stem": (
                    "A 16-year-old has weight loss, polyuria, polydipsia, Kussmaul breathing. "
                    "Glucose 420 mg/dL, pH 7.18, bicarbonate 10, urine ketones positive."
                ),
                "question": "Diagnosis and priority?",
                "answer": "DKA. IV fluids, insulin, careful K+ replacement.",
                "discussion": "Never start insulin with severe untreated hypokalemia.",
                "book_hint": "Williams Textbook of Endocrinology — Diabetes",
            },
            {
                "title": "Heat Intolerance and Weight Loss",
                "stem": (
                    "A 30-year-old woman has heat intolerance, weight loss, tremor, and a diffuse goiter. "
                    "TSH low, free T4 high."
                ),
                "question": "Most likely diagnosis category?",
                "answer": "Thyrotoxicosis (e.g., Graves disease common in this picture).",
                "discussion": "Confirm etiology (TRAb, uptake if needed); treat with antithyroid drugs/beta-blocker ± definitive therapy.",
                "book_hint": "Harrison's — Thyroid Disease",
            },
        ],
        "books": [
            "Williams Textbook of Endocrinology",
            "Harrison's — Endocrinology",
            "Greenspan's Basic & Clinical Endocrinology",
        ],
        "pdf_notes": [
            "DKA: hyperglycemia + ketones + acidosis; fluids, insulin, K+.",
            "Hashimoto → hypothyroidism; Graves → hyperthyroidism.",
            "Metformin first-line for many T2DM patients if eGFR allows.",
            "Hypocalcemia: Chvostek/Trousseau; check Mg and PTH.",
            "Adrenal crisis: shock + hyponatremia/hyperkalemia — give steroids/fluids urgently.",
        ],
    },
    "nephrology": {
        "label": "Nephrology",
        "questions": [
            {
                "question": "Best overall index of kidney function in practice is often?",
                "options": [
                    "A) Serum amylase",
                    "B) eGFR / creatinine-based estimate",
                    "C) AST alone",
                    "D) Hemoglobin A1c alone",
                ],
                "answer": "B) eGFR / creatinine-based estimate",
                "explanation": "eGFR estimated from creatinine is widely used to assess kidney function.",
            },
            {
                "question": "Nephritic syndrome typically features?",
                "options": [
                    "A) Heavy proteinuria >3.5 g/day alone without hematuria",
                    "B) Hematuria, hypertension, oliguria, mild–moderate proteinuria",
                    "C) Only hyperlipidemia",
                    "D) Only hypocalcemia",
                ],
                "answer": "B) Hematuria, hypertension, oliguria, mild–moderate proteinuria",
                "explanation": "Nephritic = active urinary sediment, HTN, impaired GFR.",
            },
            {
                "question": "Preferred antihypertensives in diabetic albuminuria?",
                "options": [
                    "A) ACE inhibitor or ARB",
                    "B) Alpha blocker only",
                    "C) Hydralazine only",
                    "D) Short-acting nifedipine only",
                ],
                "answer": "A) ACE inhibitor or ARB",
                "explanation": "ACEI/ARB reduce proteinuria and protect kidneys in diabetic nephropathy.",
            },
            {
                "question": "Pre-renal AKI is suggested by?",
                "options": [
                    "A) Muddy brown casts always",
                    "B) Low FENa and history of volume depletion",
                    "C) RBC casts only",
                    "D) Always normal BUN:creatinine",
                ],
                "answer": "B) Low FENa and history of volume depletion",
                "explanation": "Pre-renal: hypoperfusion, low FENa (if not on diuretics), improved with volume.",
            },
        ],
        "cases": [
            {
                "title": "Oliguria after Diarrhea",
                "stem": (
                    "A 70-year-old with gastroenteritis has oliguria, dry mucosa, creatinine rise from 1.0 to 2.2. "
                    "Urine Na low; improves with IV fluids."
                ),
                "question": "AKI type?",
                "answer": "Pre-renal AKI.",
                "discussion": "Restore volume; avoid nephrotoxins; reassess if not improving (ATN possible).",
                "book_hint": "Brenner & Rector's The Kidney — AKI",
            },
            {
                "title": "Edema and Heavy Proteinuria",
                "stem": (
                    "A 22-year-old has periorbital edema, hypoalbuminemia, proteinuria 4.5 g/day, and hyperlipidemia."
                ),
                "question": "Syndrome name?",
                "answer": "Nephrotic syndrome.",
                "discussion": "Find cause (MCD, FSGS, membranous, diabetic, etc.); treat edema, ACEI/ARB, anticoagulation risk assessment.",
                "book_hint": "Harrison's — Glomerular Diseases",
            },
        ],
        "books": [
            "Brenner & Rector's The Kidney",
            "Harrison's — Nephrology",
            "Comprehensive Clinical Nephrology — Feehally",
        ],
        "pdf_notes": [
            "AKI types: pre-renal, intrinsic (ATN/AIN/GN), post-renal.",
            "Nephritic vs nephrotic: active sediment/HTN vs heavy protein/edema.",
            "Diabetic kidney disease: ACEI/ARB cornerstone with glycemic/BP control.",
            "eGFR guides drug dosing and CKD staging.",
            "Hyperkalemia emergencies: ECG changes → calcium, shift, remove K+.",
        ],
    },
    "orthopedics": {
        "label": "Orthopedics",
        "questions": [
            {
                "question": "Fat embolism classic triad after long-bone fracture includes?",
                "options": [
                    "A) Jaundice, ascites, spider nevi",
                    "B) Respiratory distress, neurologic change, petechial rash",
                    "C) Only ankle swelling",
                    "D) Only fever without hypoxia",
                ],
                "answer": "B) Respiratory distress, neurologic change, petechial rash",
                "explanation": "Fat embolism: hypoxia, neuro changes, petechiae after fracture.",
            },
            {
                "question": "Ottawa ankle rules help decide need for?",
                "options": [
                    "A) MRI always",
                    "B) Ankle/foot X-ray after sprain injury",
                    "C) Immediate ORIF for all sprains",
                    "D) Antibiotics",
                ],
                "answer": "B) Ankle/foot X-ray after sprain injury",
                "explanation": "Ottawa rules reduce unnecessary radiographs.",
            },
            {
                "question": "Colles fracture typically involves?",
                "options": [
                    "A) Distal radius with dorsal angulation",
                    "B) Clavicle midshaft only",
                    "C) Femoral neck only",
                    "D) Scaphoid waist always without fall",
                ],
                "answer": "A) Distal radius with dorsal angulation",
                "explanation": "Colles = distal radius fracture with dorsal angulation (FOOSH).",
            },
            {
                "question": "Compartment syndrome key clinical feature?",
                "options": [
                    "A) Pain out of proportion, pain on passive stretch",
                    "B) Only itching",
                    "C) Painless swelling always safe",
                    "D) Normal pulses exclude it always",
                ],
                "answer": "A) Pain out of proportion, pain on passive stretch",
                "explanation": "Pain out of proportion/passive stretch is the earliest key sign; pulses may remain.",
            },
        ],
        "cases": [
            {
                "title": "Pain after Cast Application",
                "stem": (
                    "A 25-year-old with tibial fracture has severe pain in cast, pain on passive toe stretch, "
                    "and tense compartments. Pulses present."
                ),
                "question": "Diagnosis and action?",
                "answer": "Acute compartment syndrome — urgent fasciotomy (after confirming clinically/pressure).",
                "discussion": "Do not wait for pulselessness. Remove constricting casts; emergent ortho review.",
                "book_hint": "Apley's System of Orthopaedics — Compartment Syndrome",
            },
            {
                "title": "Hip Pain in Elderly After Fall",
                "stem": (
                    "An 82-year-old falls; shortened externally rotated leg and cannot bear weight."
                ),
                "question": "Most likely injury?",
                "answer": "Hip fracture (e.g., femoral neck / intertrochanteric).",
                "discussion": "X-ray pelvis/hip; early ortho, VTE prophylaxis, surgery as indicated.",
                "book_hint": "Apley's — Fractures around the hip",
            },
        ],
        "books": [
            "Apley's System of Orthopaedics and Fractures",
            "Campbell's Operative Orthopaedics",
            "Bailey & Love — Orthopaedics chapters",
        ],
        "pdf_notes": [
            "Compartment syndrome: pain out of proportion — emergency fasciotomy pathway.",
            "Colles fracture: FOOSH → distal radius dorsal angulation.",
            "Ottawa ankle rules guide X-ray after sprain.",
            "Hip fracture: shortened externally rotated limb in elderly fall.",
            "Fat embolism after long-bone fracture: hypoxia, neuro, petechiae.",
        ],
    },
    "dermatology": {
        "label": "Dermatology",
        "questions": [
            {
                "question": "ABCDE criteria screen for?",
                "options": [
                    "A) Psoriasis",
                    "B) Melanoma",
                    "C) Impetigo",
                    "D) Acne only",
                ],
                "answer": "B) Melanoma",
                "explanation": "Asymmetry, Border, Color, Diameter, Evolving — melanoma warning signs.",
            },
            {
                "question": "Honey-colored crusted lesions on a child's face suggest?",
                "options": [
                    "A) Impetigo",
                    "B) Melanoma",
                    "C) Vitiligo",
                    "D) Tinea capitis only",
                ],
                "answer": "A) Impetigo",
                "explanation": "Impetigo classically shows honey-colored crusts.",
            },
            {
                "question": "Auspitz sign is associated with?",
                "options": [
                    "A) Psoriasis",
                    "B) Scabies only",
                    "C) Cellulitis",
                    "D) Urticaria",
                ],
                "answer": "A) Psoriasis",
                "explanation": "Pinpoint bleeding on scale removal = Auspitz sign in psoriasis.",
            },
            {
                "question": "Night itch worse in finger webs commonly suggests?",
                "options": [
                    "A) Scabies",
                    "B) Melanoma",
                    "C) Basal cell carcinoma",
                    "D) Alopecia areata",
                ],
                "answer": "A) Scabies",
                "explanation": "Scabies: intense nocturnal itch, burrows in web spaces.",
            },
        ],
        "cases": [
            {
                "title": "Changing Mole",
                "stem": (
                    "A 48-year-old notices a pigmented lesion with irregular border, multiple colors, "
                    "and recent growth."
                ),
                "question": "Concern and next step?",
                "answer": "Suspect melanoma — urgent dermatology for excision biopsy.",
                "discussion": "Do not shave destructive biopsy of suspected melanoma; full-thickness excision preferred.",
                "book_hint": "Rook's Textbook of Dermatology — Melanoma",
            },
            {
                "title": "Honey Crusts in a Child",
                "stem": (
                    "A 6-year-old has facial erosions with honey-colored crusts after a minor scratch. Afebrile."
                ),
                "question": "Likely diagnosis?",
                "answer": "Impetigo.",
                "discussion": "Often S. aureus or S. pyogenes; topical/systemic antibiotics per extent; hygiene counseling.",
                "book_hint": "Harrison's — Skin and Soft Tissue Infections",
            },
        ],
        "books": [
            "Rook's Textbook of Dermatology",
            "Fitzpatrick's Dermatology",
            "Habif's Clinical Dermatology",
        ],
        "pdf_notes": [
            "ABCDE for melanoma; urgent specialist referral for suspicious lesions.",
            "Impetigo: honey-colored crusts — contagious.",
            "Psoriasis: silvery scale, Auspitz, extensor surfaces common.",
            "Scabies: nocturnal itch, finger webs — treat patient + contacts.",
            "Cellulitis vs abscess: antibiotics ± drainage if collection.",
        ],
    },
    "obgyn": {
        "label": "Obstetrics & Gynecology",
        "questions": [
            {
                "question": "Most common cause of postpartum hemorrhage?",
                "options": [
                    "A) Uterine atony",
                    "B) Amniotic fluid embolism always",
                    "C) Placenta previa only",
                    "D) Cervical cancer",
                ],
                "answer": "A) Uterine atony",
                "explanation": "Atony is the leading cause of PPH (4 Ts: Tone, Trauma, Tissue, Thrombin).",
            },
            {
                "question": "Ectopic pregnancy classic risk setting includes?",
                "options": [
                    "A) Prior PID / tubal damage",
                    "B) Only multiparity without other risk",
                    "C) Vitamin D excess",
                    "D) Migraine alone",
                ],
                "answer": "A) Prior PID / tubal damage",
                "explanation": "Tubal damage (e.g., PID) increases ectopic risk.",
            },
            {
                "question": "Fetal heart usually first heard by Doppler around?",
                "options": [
                    "A) 6 weeks",
                    "B) 10–12 weeks",
                    "C) 28 weeks only",
                    "D) 40 weeks",
                ],
                "answer": "B) 10–12 weeks",
                "explanation": "Doppler heart tones commonly from 10–12 weeks.",
            },
            {
                "question": "Pre-eclampsia is defined with hypertension after 20 weeks plus?",
                "options": [
                    "A) Proteinuria or end-organ dysfunction features",
                    "B) Only ankle edema always",
                    "C) Only backache",
                    "D) Only constipation",
                ],
                "answer": "A) Proteinuria or end-organ dysfunction features",
                "explanation": "Pre-eclampsia: new HTN ≥20 weeks with proteinuria or maternal organ dysfunction.",
            },
        ],
        "cases": [
            {
                "title": "Postpartum Bleeding",
                "stem": (
                    "Thirty minutes after vaginal delivery, heavy bleeding, boggy uterus, hypotension."
                ),
                "question": "Most likely cause and first steps?",
                "answer": "Uterine atony — uterine massage + oxytocin; escalate uterotonics/PPH protocol.",
                "discussion": "Recall 4 Ts; early recognition prevents maternal death.",
                "book_hint": "Williams Obstetrics — PPH",
            },
            {
                "title": "Positive Pregnancy Test and Unilateral Pain",
                "stem": (
                    "A 28-year-old with positive β-hCG has unilateral pelvic pain and spotting. "
                    "Ultrasound: empty uterus, adnexal mass."
                ),
                "question": "Diagnosis?",
                "answer": "Ectopic pregnancy until proven otherwise.",
                "discussion": "Hemodynamic stability guides medical vs surgical management; rupture is emergency.",
                "book_hint": "Williams Obstetrics — Ectopic Pregnancy",
            },
        ],
        "books": [
            "Williams Obstetrics",
            "Beckmann and Ling's Obstetrics and Gynecology",
            "DC Dutta's Textbook of Obstetrics",
        ],
        "pdf_notes": [
            "PPH 4 Ts: Tone (atony most common), Trauma, Tissue, Thrombin.",
            "Ectopic: positive hCG + empty uterus + pain/spotting — emergency awareness.",
            "Pre-eclampsia after 20 weeks: HTN + proteinuria/organ dysfunction.",
            "Antenatal care milestones: dating, anomaly scan, Rh, vaccines as indicated.",
            "Doppler FHR typically ~10–12 weeks.",
        ],
    },
    "pediatrics": {
        "label": "Pediatrics",
        "questions": [
            {
                "question": "Which vaccine is live attenuated?",
                "options": [
                    "A) Hepatitis B",
                    "B) Tetanus toxoid",
                    "C) MMR",
                    "D) Inactivated polio (IPV)",
                ],
                "answer": "C) MMR",
                "explanation": "MMR is live attenuated.",
            },
            {
                "question": "First-line oral rehydration for most childhood diarrhea?",
                "options": [
                    "A) ORS",
                    "B) Immediate IV antibiotics always",
                    "C) Soft drinks only",
                    "D) High-dose aspirin",
                ],
                "answer": "A) ORS",
                "explanation": "ORS is cornerstone therapy for most dehydrating diarrheas.",
            },
            {
                "question": "Kawasaki disease concerning complication?",
                "options": [
                    "A) Coronary artery aneurysms",
                    "B) Only otitis externa",
                    "C) Only constipation",
                    "D) Cataract",
                ],
                "answer": "A) Coronary artery aneurysms",
                "explanation": "Kawasaki can cause coronary aneurysms; treat with IVIG/aspirin per protocol.",
            },
            {
                "question": "APGAR assesses newborn status at?",
                "options": [
                    "A) 1 and 5 minutes (commonly)",
                    "B) Only at 1 hour",
                    "C) Only at discharge",
                    "D) Only prenatally",
                ],
                "answer": "A) 1 and 5 minutes (commonly)",
                "explanation": "APGAR is routinely at 1 and 5 minutes.",
            },
        ],
        "cases": [
            {
                "title": "Fever and Strawberry Tongue",
                "stem": (
                    "A 3-year-old has ≥5 days fever, bilateral conjunctivitis, strawberry tongue, "
                    "cervical lymphadenopathy, and rash."
                ),
                "question": "Likely diagnosis?",
                "answer": "Kawasaki disease.",
                "discussion": "Needs prompt IVIG to reduce coronary complications; echo follow-up.",
                "book_hint": "Nelson Textbook of Pediatrics — Kawasaki",
            },
            {
                "title": "Dehydration after Diarrhea",
                "stem": (
                    "An 18-month-old with watery diarrhea has sunken eyes and reduced urine but is still drinking."
                ),
                "question": "Initial therapy preference?",
                "answer": "Oral rehydration solution (ORS) if able to drink and not in shock.",
                "discussion": "IV fluids if severe dehydration/shock; zinc may be used per guidelines; avoid antimotility drugs in young children.",
                "book_hint": "Nelson — Diarrheal Diseases",
            },
        ],
        "books": [
            "Nelson Textbook of Pediatrics",
            "Illustrated Textbook of Paediatrics — Lissauer",
            "Forfar and Arneil's Textbook of Pediatrics",
        ],
        "pdf_notes": [
            "ORS first-line for most pediatric dehydration from diarrhea.",
            "MMR is live; know live vs inactivated vaccines.",
            "Kawasaki: prolonged fever + mucocutaneous signs → coronary risk.",
            "APGAR at 1 and 5 minutes guides immediate newborn status.",
            "Always calculate pediatric doses by weight; watch fluid rates.",
        ],
    },
}

# Ordered list for stable menu layout
SPECIALTY_ORDER = [
    "cardiology",
    "ophthalmology",
    "urology",
    "neurology",
    "pulmonology",
    "gastroenterology",
    "endocrinology",
    "nephrology",
    "orthopedics",
    "dermatology",
    "obgyn",
    "pediatrics",
]


def specialty_label(key: str) -> str:
    return SPECIALTIES[key]["label"]


def label_to_key(label: str) -> str | None:
    for key, data in SPECIALTIES.items():
        if data["label"] == label:
            return key
    return None


def get_specialty(key: str) -> dict:
    return SPECIALTIES[key]


def next_unique(items: list[dict], remaining: list[int] | None) -> tuple[int, dict, list[int]]:
    """Pick the next unused item; reshuffle only after the full set is exhausted."""
    pool = list(remaining) if remaining else []
    if not pool:
        pool = list(range(len(items)))
        random.shuffle(pool)
    idx = pool.pop()
    return idx, items[idx], pool


def pick_question(specialty_key: str, remaining: list[int] | None = None) -> tuple[int, dict, list[int]]:
    items = SPECIALTIES[specialty_key]["questions"]
    return next_unique(items, remaining)


def pick_case(specialty_key: str, remaining: list[int] | None = None) -> tuple[int, dict, list[int]]:
    items = SPECIALTIES[specialty_key]["cases"]
    return next_unique(items, remaining)


def correct_letter(item: dict) -> str:
    return item["answer"].strip()[0].upper()


def option_letter(option: str) -> str:
    return option.strip()[0].upper()


def format_question_prompt(item: dict, specialty_label_text: str) -> str:
    return (
        f"📘 *Short MCQ — {specialty_label_text}*\n\n"
        f"{item['question']}\n\n"
        f"_Tap an answer button below._"
    )


def format_question_result(item: dict, chosen: str, specialty_label_text: str) -> str:
    correct = correct_letter(item)
    chosen = chosen.upper()
    verdict = "✅ *Correct!*" if chosen == correct else f"❌ *Incorrect.* You chose *{chosen}*."
    options = "\n".join(item["options"])
    return (
        f"📘 *Short MCQ — {specialty_label_text}*\n\n"
        f"{item['question']}\n\n"
        f"{options}\n\n"
        f"{verdict}\n"
        f"✅ *Answer:* {item['answer']}\n"
        f"💡 {item['explanation']}"
    )


def format_case_prompt(item: dict, specialty_label_text: str) -> str:
    return (
        f"🏥 *Case-based Question — {specialty_label_text}*\n"
        f"*{item['title']}*\n\n"
        f"{item['stem']}\n\n"
        f"❓ *Question:* {item['question']}\n\n"
        f"_Tap the button below to reveal the answer._"
    )


def format_case_result(item: dict, specialty_label_text: str) -> str:
    return (
        f"🏥 *Case-based Question — {specialty_label_text}*\n"
        f"*{item['title']}*\n\n"
        f"{item['stem']}\n\n"
        f"❓ *Question:* {item['question']}\n\n"
        f"✅ *Answer:* {item['answer']}\n\n"
        f"📝 *Discussion:* {item['discussion']}\n\n"
        f"📚 *Book source:* {item['book_hint']}"
    )


def format_book_sources(specialty_key: str) -> str:
    data = SPECIALTIES[specialty_key]
    books = "\n".join(f"• {b}" for b in data["books"])
    return (
        f"📚 *Book sources — {data['label']}*\n\n"
        f"{books}\n\n"
        f"_Use the edition recommended by your faculty._"
    )


def specialty_menu_text() -> str:
    return (
        "🩺 *CharaNas Medicine Bot*\n"
        "Undergraduate Medicine Department\n\n"
        "Choose a *specialty* first:\n"
        "Then you can open Short MCQ, Case-based Question, PDF files, or Book source "
        "for that specialty.\n\n"
        "Use *Change specialty* anytime to switch topics."
    )


def feature_menu_text(specialty_key: str) -> str:
    label = specialty_label(specialty_key)
    return (
        f"📍 Specialty: *{label}*\n\n"
        "Choose a feature:\n"
        "• Short MCQ\n"
        "• Case-based Question\n"
        "• PDF files\n"
        "• Book source\n\n"
        "Or tap *Change specialty* to go back."
    )
