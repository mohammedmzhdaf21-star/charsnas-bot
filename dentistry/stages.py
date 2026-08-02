"""Dentistry stage levels and curricula (undergraduate).

Navigation: Stage → Curriculum → Short MCQ / PDF / Book source
Edit this file when the faculty curriculum list changes.
"""

from __future__ import annotations

STAGE_ORDER = [
    "basic_foundation",
    "basic_dental_sciences",
    "preclinical",
    "clinical",
]

STAGES: dict[str, dict] = {
    "basic_foundation": {
        "label": "Basic Foundation",
        "curricula": [
            ("anatomy", "Anatomy / Human Anatomy"),
            ("physiology", "Physiology / Human Physiology"),
            ("biochemistry", "Biochemistry"),
            ("general_histology", "General Histology"),
            ("oral_histology", "Oral Histology / Embryology and Oral Histology"),
            ("oral_biology", "Oral Biology / Tooth Morphology"),
            ("dental_terminology", "Dental Terminology / Dental Anatomy terminology"),
        ],
    },
    "basic_dental_sciences": {
        "label": "Basic Dental Sciences",
        "curricula": [
            ("dental_anatomy", "Dental Anatomy"),
            ("dental_materials", "Dental Materials"),
            ("general_pathology", "General Pathology"),
            ("general_pharmacology", "General Pharmacology"),
            ("drugs_in_dentistry", "Drugs in Dentistry"),
            ("oral_physiology", "Oral Physiology"),
            ("head_neck_anatomy", "Head and Neck Anatomy"),
        ],
    },
    "preclinical": {
        "label": "Pre-clinical Dentistry",
        "curricula": [
            ("preclinical_operative", "Pre-clinical Operative Dentistry"),
            ("preclinical_prosthodontics", "Pre-clinical Prosthodontics"),
            ("preclinical_oral_surgery", "Pre-clinical Oral Surgery"),
            ("oral_medicine_radiology", "Oral Medicine / Oral Diagnosis / Oral Radiology"),
            ("community_dentistry", "Community Dentistry"),
            ("periodontology", "Periodontology"),
            ("oral_pathology", "Oral Pathology / Oral and Maxillofacial Pathology"),
        ],
    },
    "clinical": {
        "label": "Clinical Dentistry",
        "curricula": [
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
    },
}

# Map curriculum key → existing question_banks/{stem}.json (when available)
BANK_FILE_MAP: dict[str, str] = {
    "anatomy": "anatomy",
    "head_neck_anatomy": "anatomy",  # closest starter until a dedicated bank exists
    "dental_anatomy": "dental_anatomy",
    "oral_histology": "dental_anatomy",  # closest starter bank until dedicated content arrives
    "oral_biology": "dental_anatomy",
    "dental_terminology": "dental_anatomy",
    "preclinical_operative": "restorative",
    "preclinical_prosthodontics": "prosthodontics",
    "preclinical_oral_surgery": "oral_surgery",
    "oral_medicine_radiology": "oral_radiology",
    "periodontology": "periodontics",
    "oral_pathology": "oral_medicine",
    "conservative_dentistry": "restorative",
    "prosthodontics": "prosthodontics",
    "endodontics": "endodontics",
    "orthodontics": "orthodontics",
    "pediatric_dentistry": "pediatric_dentistry",
    "oral_maxillofacial_surgery": "oral_surgery",
}

# Optional PDF stem overrides (default: UG_Dentistry_{Key}_Notes.pdf via generate_pdfs)
PDF_FILE_MAP: dict[str, str] = {
    "conservative_dentistry": "restorative",
    "periodontology": "periodontics",
    "oral_maxillofacial_surgery": "oral_surgery",
    "oral_medicine_radiology": "oral_radiology",
    "oral_pathology": "oral_medicine",
    "preclinical_operative": "restorative",
    "preclinical_prosthodontics": "prosthodontics",
    "preclinical_oral_surgery": "oral_surgery",
    "dental_anatomy": "dental_anatomy",
}


def all_curricula() -> list[tuple[str, str]]:
    """Flat list of (key, label) in stage order."""
    out: list[tuple[str, str]] = []
    for stage_key in STAGE_ORDER:
        out.extend(STAGES[stage_key]["curricula"])
    return out


def stage_label(stage_key: str) -> str:
    return STAGES[stage_key]["label"]


def curriculum_stage(curriculum_key: str) -> str | None:
    for stage_key, stage in STAGES.items():
        for key, _label in stage["curricula"]:
            if key == curriculum_key:
                return stage_key
    return None


def label_to_stage(label: str) -> str | None:
    for key, stage in STAGES.items():
        if stage["label"] == label:
            return key
    return None


def label_to_curriculum(label: str) -> str | None:
    for key, lab in all_curricula():
        if lab == label:
            return key
    return None
