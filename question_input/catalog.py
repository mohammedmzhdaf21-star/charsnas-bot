"""Departments and specialties available for content input."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# Single source of truth for dentistry stage → curriculum → bank stems
from dentistry.stages import (  # noqa: E402
    BANK_FILE_MAP as DENTISTRY_BANK_FILE_MAP,
    ensure_curriculum_banks as ensure_dentistry_banks,
    stages_as_catalog as dentistry_stages_as_catalog,
)

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
        "nav_mode": "stages",
        # Imported from dentistry/stages.py — do not duplicate lists here
        "stages": dentistry_stages_as_catalog(),
        "specialties": [],
        "bank_aliases": dict(DENTISTRY_BANK_FILE_MAP),
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
    ("perplexity_mcq", "Generate Short MCQs + PDF (auto)"),
    ("perplexity_pdf", "Generate topic PDF only"),
    ("short_mcq", "Type Short MCQs myself"),
    ("case_based", "Case-based questions"),
    ("pdf_files", "Upload PDF files"),
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


def ensure_all_department_banks() -> dict[str, list[str]]:
    """Ensure every specialty/curriculum has a bank JSON file. Returns created stems by dept."""
    from bank_loader import ensure_bank_files

    created: dict[str, list[str]] = {}
    # Dentistry: curriculum stems (including shared remaps)
    created["dentistry"] = ensure_dentistry_banks(DEPARTMENTS["dentistry"]["banks_dir"])
    for key, dep in DEPARTMENTS.items():
        if key == "dentistry":
            continue
        stems = [spec_key for spec_key, _label in dep["specialties"]]
        created[key] = ensure_bank_files(dep["banks_dir"], stems)
    return created


_fill_flat_specialties()
ensure_all_department_banks()


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
