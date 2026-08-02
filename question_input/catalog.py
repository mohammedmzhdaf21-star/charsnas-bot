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
        # Stage → curriculum navigation (matches dentistry bot)
        "nav_mode": "stages",
        "stages": [
            (
                "basic_foundation",
                "Basic Foundation",
                [
                    ("anatomy", "Anatomy / Human Anatomy"),
                    ("physiology", "Physiology / Human Physiology"),
                    ("biochemistry", "Biochemistry"),
                    ("general_histology", "General Histology"),
                    ("oral_histology", "Oral Histology / Embryology and Oral Histology"),
                    ("oral_biology", "Oral Biology / Tooth Morphology"),
                    ("dental_terminology", "Dental Terminology / Dental Anatomy terminology"),
                ],
            ),
            (
                "basic_dental_sciences",
                "Basic Dental Sciences",
                [
                    ("dental_anatomy", "Dental Anatomy"),
                    ("dental_materials", "Dental Materials"),
                    ("general_pathology", "General Pathology"),
                    ("general_pharmacology", "General Pharmacology"),
                    ("drugs_in_dentistry", "Drugs in Dentistry"),
                    ("oral_physiology", "Oral Physiology"),
                    ("head_neck_anatomy", "Head and Neck Anatomy"),
                ],
            ),
            (
                "preclinical",
                "Pre-clinical Dentistry",
                [
                    ("preclinical_operative", "Pre-clinical Operative Dentistry"),
                    ("preclinical_prosthodontics", "Pre-clinical Prosthodontics"),
                    ("preclinical_oral_surgery", "Pre-clinical Oral Surgery"),
                    ("oral_medicine_radiology", "Oral Medicine / Oral Diagnosis / Oral Radiology"),
                    ("community_dentistry", "Community Dentistry"),
                    ("periodontology", "Periodontology"),
                    ("oral_pathology", "Oral Pathology / Oral and Maxillofacial Pathology"),
                ],
            ),
            (
                "clinical",
                "Clinical Dentistry",
                [
                    ("conservative_dentistry", "Conservative Dentistry"),
                    ("prosthodontics", "Prosthodontics"),
                    ("endodontics", "Endodontics"),
                    ("orthodontics", "Orthodontics"),
                    ("pediatric_dentistry", "Pediatric Dentistry"),
                    ("oral_maxillofacial_surgery", "Oral and Maxillofacial Surgery"),
                    ("implantology", "Implantology"),
                    ("medically_compromised", "Management of Medically Compromised Patients"),
                    ("dental_ethics", "Medical Ethics / Ethics in Dentistry"),
                    ("comprehensive_care", "Comprehensive Dental Care"),
                    ("evidence_based_dentistry", "Evidence-Based Dentistry"),
                    ("medical_emergency", "Medical Emergency in Dentistry"),
                ],
            ),
        ],
        # Flat list used for label lookups (filled below)
        "specialties": [],
        "bank_aliases": {
            "oral_histology": "dental_anatomy",
            "oral_biology": "dental_anatomy",
            "dental_terminology": "dental_anatomy",
            "preclinical_operative": "restorative",
            "preclinical_prosthodontics": "prosthodontics",
            "preclinical_oral_surgery": "oral_surgery",
            "oral_medicine_radiology": "oral_radiology",
            "periodontology": "periodontics",
            "oral_pathology": "oral_medicine",
            "conservative_dentistry": "restorative",
            "oral_maxillofacial_surgery": "oral_surgery",
        },
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
    ("perplexity_mcq", "Generate Short MCQs (auto-save)"),
    ("short_mcq", "Type Short MCQs myself"),
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


def _fill_flat_specialties() -> None:
    """Build flat specialties list from stages for departments that use stage nav."""
    for dep in DEPARTMENTS.values():
        if dep.get("nav_mode") != "stages":
            continue
        flat: list[tuple[str, str]] = []
        for _stage_key, _stage_label, curricula in dep.get("stages") or []:
            flat.extend(curricula)
        dep["specialties"] = flat


_fill_flat_specialties()


def uses_stages(department: str) -> bool:
    return DEPARTMENTS.get(department, {}).get("nav_mode") == "stages"


def department_stages(department: str) -> list[tuple[str, str, list[tuple[str, str]]]]:
    return list(DEPARTMENTS.get(department, {}).get("stages") or [])


def stage_curricula(department: str, stage_key: str) -> list[tuple[str, str]]:
    for key, _label, curricula in department_stages(department):
        if key == stage_key:
            return list(curricula)
    return []


def stage_label(department: str, stage_key: str) -> str:
    for key, label, _curricula in department_stages(department):
        if key == stage_key:
            return label
    return stage_key


def specialty_label(department: str, specialty_key: str) -> str:
    dep = DEPARTMENTS.get(department) or {}
    return dict(dep.get("specialties") or {}).get(specialty_key, specialty_key)
