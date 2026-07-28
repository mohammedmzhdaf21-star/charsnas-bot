"""Undergraduate medicine study content for CharaNas Medicine bot."""

from __future__ import annotations

import random

QUESTIONS = [
    {
        "subject": "Anatomy",
        "question": (
            "Which cranial nerve exits the skull through the stylomastoid foramen?"
        ),
        "options": ["A) CN VII", "B) CN IX", "C) CN X", "D) CN XII"],
        "answer": "A) CN VII (Facial nerve)",
        "explanation": "The facial nerve exits via the stylomastoid foramen.",
    },
    {
        "subject": "Physiology",
        "question": "What is the resting membrane potential of a typical neuron?",
        "options": ["A) +30 mV", "B) 0 mV", "C) −70 mV", "D) −90 mV"],
        "answer": "C) −70 mV",
        "explanation": "Neurons typically rest near −70 mV due to K+ leak and Na+/K+ ATPase.",
    },
    {
        "subject": "Biochemistry",
        "question": "Which enzyme is deficient in phenylketonuria (PKU)?",
        "options": [
            "A) Tyrosinase",
            "B) Phenylalanine hydroxylase",
            "C) Homogentisate oxidase",
            "D) Branched-chain ketoacid dehydrogenase",
        ],
        "answer": "B) Phenylalanine hydroxylase",
        "explanation": "PKU is caused by PAH deficiency → ↑ phenylalanine.",
    },
    {
        "subject": "Pathology",
        "question": "Reed–Sternberg cells are characteristic of which lymphoma?",
        "options": [
            "A) Burkitt lymphoma",
            "B) Follicular lymphoma",
            "C) Hodgkin lymphoma",
            "D) Mantle cell lymphoma",
        ],
        "answer": "C) Hodgkin lymphoma",
        "explanation": "Classic Hodgkin lymphoma shows CD15+/CD30+ Reed–Sternberg cells.",
    },
    {
        "subject": "Pharmacology",
        "question": "Which drug is a selective COX-2 inhibitor?",
        "options": ["A) Aspirin", "B) Ibuprofen", "C) Celecoxib", "D) Indomethacin"],
        "answer": "C) Celecoxib",
        "explanation": "Celecoxib selectively inhibits COX-2.",
    },
    {
        "subject": "Microbiology",
        "question": "Which organism is the most common cause of community-acquired pneumonia?",
        "options": [
            "A) Staphylococcus aureus",
            "B) Streptococcus pneumoniae",
            "C) Klebsiella pneumoniae",
            "D) Pseudomonas aeruginosa",
        ],
        "answer": "B) Streptococcus pneumoniae",
        "explanation": "S. pneumoniae is the leading cause of CAP.",
    },
    {
        "subject": "Internal Medicine",
        "question": "First-line drug class for hypertension with diabetes and albuminuria?",
        "options": ["A) Beta blockers", "B) ACE inhibitors", "C) Thiazides", "D) Alpha blockers"],
        "answer": "B) ACE inhibitors",
        "explanation": "ACEIs (or ARBs) are preferred for diabetic nephropathy.",
    },
    {
        "subject": "Surgery",
        "question": "Most common cause of small bowel obstruction in adults with prior surgery?",
        "options": ["A) Hernia", "B) Adhesions", "C) Volvulus", "D) Intussusception"],
        "answer": "B) Adhesions",
        "explanation": "Postoperative adhesions are the most common cause of SBO.",
    },
    {
        "subject": "Pediatrics",
        "question": "Which vaccine is live attenuated?",
        "options": ["A) Hepatitis B", "B) Tetanus toxoid", "C) MMR", "D) Inactivated polio (IPV)"],
        "answer": "C) MMR",
        "explanation": "MMR is a live attenuated vaccine.",
    },
    {
        "subject": "Obstetrics & Gynecology",
        "question": "At what gestational age is the fetal heart usually first heard by Doppler?",
        "options": ["A) 6 weeks", "B) 10–12 weeks", "C) 16 weeks", "D) 20 weeks"],
        "answer": "B) 10–12 weeks",
        "explanation": "Fetal heart tones are typically detected by Doppler around 10–12 weeks.",
    },
]

CASES = [
    {
        "title": "Chest Pain in a Young Adult",
        "stem": (
            "A 28-year-old medical student presents with sharp left-sided chest pain "
            "that worsens with deep inspiration and improves when leaning forward. "
            "ECG shows diffuse ST elevation and PR depression."
        ),
        "question": "What is the most likely diagnosis?",
        "answer": "Acute pericarditis",
        "discussion": (
            "Positional/pleuritic pain + diffuse ST elevation with PR depression "
            "points to pericarditis. Treat with NSAIDs ± colchicine; evaluate for cause."
        ),
        "book_hint": "Harrison's Principles of Internal Medicine — Pericardial Disease",
    },
    {
        "title": "Abdominal Pain and Jaundice",
        "stem": (
            "A 45-year-old woman with obesity and multiparity presents with RUQ pain "
            "radiating to the scapula, fever, and jaundice. Labs: ↑ ALP, ↑ bilirubin, ↑ WBC."
        ),
        "question": "What is the most likely diagnosis and next imaging step?",
        "answer": "Ascending cholangitis (Charcot triad). Next: RUQ ultrasound, then ERCP if indicated.",
        "discussion": (
            "Charcot triad = RUQ pain + fever + jaundice. Reynolds pentad adds hypotension "
            "and altered mentation. Urgent biliary decompression may be required."
        ),
        "book_hint": "Bailey & Love's Short Practice of Surgery — Biliary Tract",
    },
    {
        "title": "Polyuria and Polydipsia",
        "stem": (
            "A 16-year-old presents with weight loss, polyuria, polydipsia, and Kussmaul "
            "breathing. Glucose 420 mg/dL, arterial pH 7.18, bicarbonate 10 mEq/L, "
            "urine ketones positive."
        ),
        "question": "What is the diagnosis and initial management priority?",
        "answer": "Diabetic ketoacidosis (DKA). Priority: IV fluids, then insulin, electrolyte repletion (especially K+).",
        "discussion": (
            "DKA = hyperglycemia + ketosis + metabolic acidosis. Never start insulin if "
            "severe hypokalemia is present; replace K+ carefully."
        ),
        "book_hint": "Nelson Textbook of Pediatrics — Diabetes Mellitus",
    },
    {
        "title": "Postpartum Bleeding",
        "stem": (
            "A 32-year-old woman delivers a term infant vaginally. Thirty minutes later "
            "she has heavy vaginal bleeding, a boggy uterus, and hypotension."
        ),
        "question": "Most likely cause and first-line management?",
        "answer": "Uterine atony. First-line: uterine massage + oxytocin; escalate uterotonics as needed.",
        "discussion": (
            "Atony is the most common cause of postpartum hemorrhage. Follow the 4 Ts: "
            "Tone, Trauma, Tissue, Thrombin."
        ),
        "book_hint": "Williams Obstetrics — Postpartum Hemorrhage",
    },
    {
        "title": "Fever and Neck Stiffness",
        "stem": (
            "A 21-year-old student has fever, severe headache, photophobia, and nuchal "
            "rigidity. Kernig and Brudzinski signs are positive. No rash."
        ),
        "question": "What is the immediate next step after ABCs and blood cultures?",
        "answer": "Start empiric IV antibiotics promptly; perform LP if no contraindication to imaging delay.",
        "discussion": (
            "Do not delay antibiotics for CT/LP if bacterial meningitis is strongly suspected. "
            "Common undergrad organisms: N. meningitidis, S. pneumoniae."
        ),
        "book_hint": "Harrison's — Meningitis and CNS Infections",
    },
    {
        "title": "Shortness of Breath and Leg Swelling",
        "stem": (
            "A 68-year-old man with prior MI has progressive dyspnea, orthopnea, "
            "bilateral basal crackles, and pitting ankle edema. BNP is elevated."
        ),
        "question": "Most likely diagnosis and cornerstone outpatient therapy classes?",
        "answer": "Congestive heart failure (HFrEF likely). Cornerstones: ACEi/ARB/ARNI, beta-blocker, MRA, SGLT2i ± diuretic.",
        "discussion": (
            "Clinical volume overload + cardiac history + ↑ BNP supports HF. Confirm EF with echo "
            "and treat according to HFrEF/HFpEF pathway."
        ),
        "book_hint": "Braunwald's Heart Disease — Heart Failure",
    },
]

BOOK_SOURCES = [
    {
        "subject": "Anatomy",
        "books": [
            "Gray's Anatomy for Students",
            "Clinically Oriented Anatomy — Moore",
            "Snell's Clinical Anatomy",
        ],
    },
    {
        "subject": "Physiology",
        "books": [
            "Guyton and Hall Textbook of Medical Physiology",
            "Ganong's Review of Medical Physiology",
            "Costanzo Physiology",
        ],
    },
    {
        "subject": "Biochemistry",
        "books": [
            "Harper's Illustrated Biochemistry",
            "Lippincott Illustrated Reviews: Biochemistry",
            "Marks' Basic Medical Biochemistry",
        ],
    },
    {
        "subject": "Pathology",
        "books": [
            "Robbins Basic Pathology",
            "Robbins and Cotran Pathologic Basis of Disease",
            "Harsh Mohan Textbook of Pathology",
        ],
    },
    {
        "subject": "Pharmacology",
        "books": [
            "Katzung Basic & Clinical Pharmacology",
            "Rang and Dale's Pharmacology",
            "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        ],
    },
    {
        "subject": "Internal Medicine",
        "books": [
            "Harrison's Principles of Internal Medicine",
            "Davidson's Principles and Practice of Medicine",
            "Kumar & Clark's Clinical Medicine",
        ],
    },
    {
        "subject": "Surgery",
        "books": [
            "Bailey & Love's Short Practice of Surgery",
            "Schwartz's Principles of Surgery",
            "Sabiston Textbook of Surgery",
        ],
    },
    {
        "subject": "Pediatrics",
        "books": [
            "Nelson Textbook of Pediatrics",
            "Illustrated Textbook of Paediatrics — Lissauer",
        ],
    },
    {
        "subject": "Obstetrics & Gynecology",
        "books": [
            "Williams Obstetrics",
            "Beckmann and Ling's Obstetrics and Gynecology",
            "DC Dutta's Textbook of Obstetrics",
        ],
    },
    {
        "subject": "Exam Review",
        "books": [
            "First Aid for the USMLE Step 1",
            "Oxford Handbook of Clinical Medicine",
            "Bates' Guide to Physical Examination",
        ],
    },
]

PDF_CATALOG = [
    {
        "key": "anatomy",
        "filename": "UG_Medicine_Anatomy_Notes.pdf",
        "title": "Undergraduate Medicine — Anatomy Quick Notes",
    },
    {
        "key": "physiology",
        "filename": "UG_Medicine_Physiology_Notes.pdf",
        "title": "Undergraduate Medicine — Physiology Quick Notes",
    },
    {
        "key": "pathology",
        "filename": "UG_Medicine_Pathology_Notes.pdf",
        "title": "Undergraduate Medicine — Pathology Quick Notes",
    },
    {
        "key": "pharmacology",
        "filename": "UG_Medicine_Pharmacology_Notes.pdf",
        "title": "Undergraduate Medicine — Pharmacology Quick Notes",
    },
    {
        "key": "clinical",
        "filename": "UG_Medicine_Clinical_Pearls.pdf",
        "title": "Undergraduate Medicine — Clinical Pearls",
    },
]


def correct_letter(item: dict) -> str:
    """Return A/B/C/D from the answer string (e.g. 'B) ACE inhibitors')."""
    return item["answer"].strip()[0].upper()


def option_letter(option: str) -> str:
    return option.strip()[0].upper()


def pick_question() -> tuple[int, dict]:
    idx = random.randrange(len(QUESTIONS))
    return idx, QUESTIONS[idx]


def pick_case() -> tuple[int, dict]:
    idx = random.randrange(len(CASES))
    return idx, CASES[idx]


def format_question_prompt(item: dict) -> str:
    return (
        f"📘 *Undergraduate Medicine Question*\n"
        f"Subject: *{item['subject']}*\n\n"
        f"{item['question']}\n\n"
        f"_Tap an answer button below._"
    )


def format_question_result(item: dict, chosen: str) -> str:
    correct = correct_letter(item)
    chosen = chosen.upper()
    if chosen == correct:
        verdict = "✅ *Correct!*"
    else:
        verdict = f"❌ *Incorrect.* You chose *{chosen}*."
    options = "\n".join(item["options"])
    return (
        f"📘 *Undergraduate Medicine Question*\n"
        f"Subject: *{item['subject']}*\n\n"
        f"{item['question']}\n\n"
        f"{options}\n\n"
        f"{verdict}\n"
        f"✅ *Answer:* {item['answer']}\n"
        f"💡 {item['explanation']}"
    )


def format_case_prompt(item: dict) -> str:
    return (
        f"🏥 *Case-Based Question (UG Medicine)*\n"
        f"*{item['title']}*\n\n"
        f"{item['stem']}\n\n"
        f"❓ *Question:* {item['question']}\n\n"
        f"_Tap the button below to reveal the answer._"
    )


def format_case_result(item: dict) -> str:
    return (
        f"🏥 *Case-Based Question (UG Medicine)*\n"
        f"*{item['title']}*\n\n"
        f"{item['stem']}\n\n"
        f"❓ *Question:* {item['question']}\n\n"
        f"✅ *Answer:* {item['answer']}\n\n"
        f"📝 *Discussion:* {item['discussion']}\n\n"
        f"📚 *Book source:* {item['book_hint']}"
    )


def format_book_sources() -> str:
    lines = ["📚 *Undergraduate Medicine Book Sources*\n"]
    for entry in BOOK_SOURCES:
        books = "\n".join(f"  • {b}" for b in entry["books"])
        lines.append(f"*{entry['subject']}*\n{books}\n")
    lines.append(
        "_These are standard undergraduate medicine references. "
        "Prefer the edition recommended by your faculty._"
    )
    return "\n".join(lines)


def help_text() -> str:
    return (
        "🩺 *CharaNas Medicine Bot*\n"
        "Undergraduate Medicine Department only.\n\n"
        "Choose a feature from the buttons below:\n"
        "• *Short MCQ*\n"
        "• *Case-based Question*\n"
        "• *PDF files*\n"
        "• *Book source*\n\n"
        "For MCQs, tap an answer button to reveal the correct answer."
    )
