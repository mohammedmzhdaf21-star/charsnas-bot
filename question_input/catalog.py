"""Departments and specialties available for content input."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DEPARTMENTS = {
    "medicine": {
        "label": "Medicine",
        "banks_dir": ROOT / "question_banks",
        "custom_dir": ROOT / "custom_content",
        "pdf_dir": ROOT / "pdfs",
        "specialties": [
            ("cardiology", "Cardiology"),
            ("ophthalmology", "Ophthalmology"),
            ("urology", "Urology"),
            ("neurology", "Neurology"),
            ("pulmonology", "Pulmonology"),
            ("gastroenterology", "Gastroenterology"),
            ("endocrinology", "Endocrinology"),
            ("nephrology", "Nephrology"),
            ("orthopedics", "Orthopedics"),
            ("dermatology", "Dermatology"),
            ("obgyn", "Obstetrics & Gynecology"),
            ("pediatrics", "Pediatrics"),
        ],
    },
    "dentistry": {
        "label": "Dentistry",
        "banks_dir": ROOT / "dentistry" / "question_banks",
        "custom_dir": ROOT / "dentistry" / "custom_content",
        "pdf_dir": ROOT / "dentistry" / "pdfs",
        "specialties": [
            ("oral_surgery", "Oral Surgery"),
            ("orthodontics", "Orthodontics"),
            ("periodontics", "Periodontics"),
            ("endodontics", "Endodontics"),
            ("prosthodontics", "Prosthodontics"),
            ("pediatric_dentistry", "Pediatric Dentistry"),
            ("oral_medicine", "Oral Medicine & Pathology"),
            ("restorative", "Restorative Dentistry"),
            ("oral_radiology", "Oral Radiology"),
            ("dental_anatomy", "Dental Anatomy"),
        ],
    },
    "pharmacy": {
        "label": "Pharmacy",
        "banks_dir": ROOT / "pharmacy" / "question_banks",
        "custom_dir": ROOT / "pharmacy" / "custom_content",
        "pdf_dir": ROOT / "pharmacy" / "pdfs",
        "specialties": [
            ("pharmacology", "Pharmacology"),
            ("clinical_pharmacy", "Clinical Pharmacy"),
            ("pharmaceutics", "Pharmaceutics"),
            ("pharmacokinetics", "Pharmacokinetics"),
            ("medicinal_chemistry", "Medicinal Chemistry"),
            ("pharmacognosy", "Pharmacognosy"),
            ("pharmacy_practice", "Pharmacy Practice"),
            ("hospital_pharmacy", "Hospital Pharmacy"),
            ("toxicology", "Toxicology"),
            ("pharm_microbiology", "Pharmaceutical Microbiology"),
        ],
    },
    "mls": {
        "label": "MLS (Lab Science)",
        "banks_dir": ROOT / "mls" / "question_banks",
        "custom_dir": ROOT / "mls" / "custom_content",
        "pdf_dir": ROOT / "mls" / "pdfs",
        "specialties": [
            ("hematology", "Hematology"),
            ("clinical_chemistry", "Clinical Chemistry"),
            ("medical_microbiology", "Medical Microbiology"),
            ("immunology", "Immunology & Serology"),
            ("blood_bank", "Blood Bank / Transfusion"),
            ("histopathology", "Histopathology"),
            ("parasitology", "Parasitology"),
            ("molecular_diagnostics", "Molecular Diagnostics"),
            ("lab_qa", "Lab QA & Safety"),
            ("urinalysis", "Urinalysis & Body Fluids"),
        ],
    },
    "nursing": {
        "label": "Nursing",
        "banks_dir": ROOT / "nursing" / "question_banks",
        "custom_dir": ROOT / "nursing" / "custom_content",
        "pdf_dir": ROOT / "nursing" / "pdfs",
        "specialties": [
            ("fundamentals", "Fundamentals of Nursing"),
            ("med_surg", "Medical-Surgical Nursing"),
            ("pediatrics", "Pediatric Nursing"),
            ("maternity", "Maternity / OB Nursing"),
            ("psychiatric", "Psychiatric Nursing"),
            ("community", "Community / Public Health"),
            ("critical_care", "Critical Care Nursing"),
            ("pharm_nursing", "Pharmacology for Nurses"),
            ("ethics_leadership", "Ethics & Leadership"),
            ("geriatrics", "Geriatric Nursing"),
        ],
    },
}

CONTENT_TYPES = [
    ("short_mcq", "Short MCQ questions"),
    ("case_based", "Case-based questions"),
    ("pdf_files", "PDF files"),
    ("book_source", "Book sources"),
]

DIFFICULTIES = [
    ("easy", "Easy"),
    ("medium", "Medium"),
    ("hard", "Hard"),
    ("extreme", "Extreme"),
]

CASE_DIFFICULTIES = [
    ("easy", "Easy"),
    ("medium", "Medium"),
    ("hard", "Hard"),
]
