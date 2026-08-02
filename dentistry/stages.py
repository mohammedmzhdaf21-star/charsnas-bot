"""Dentistry stage levels and curricula (undergraduate).

Navigation: Stage → Curriculum → Short MCQ / PDF / Book source
Edit this file when the faculty curriculum list changes.

Every curriculum key MUST resolve to a question_banks/{stem}.json file.
`ensure_curriculum_banks()` creates missing empty banks on bot/input startup.
"""

from __future__ import annotations

import json
from pathlib import Path

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

# Remaps only — curricula not listed use their own key as the bank stem.
# Keep remaps when several curricula share one starter bank.
_BANK_REMAPS: dict[str, str] = {
    "head_neck_anatomy": "anatomy",
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
}

# Full map: every curriculum key → bank stem (identity + remaps). Built below.
BANK_FILE_MAP: dict[str, str] = {}

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
    "anatomy": "anatomy",
    "head_neck_anatomy": "anatomy",
}

DIFFICULTIES = ("easy", "medium", "hard", "extreme")
EMPTY_BANK = {d: [] for d in DIFFICULTIES}


def all_curricula() -> list[tuple[str, str]]:
    """Flat list of (key, label) in stage order."""
    out: list[tuple[str, str]] = []
    for stage_key in STAGE_ORDER:
        out.extend(STAGES[stage_key]["curricula"])
    return out


def _rebuild_bank_file_map() -> None:
    BANK_FILE_MAP.clear()
    for key, _label in all_curricula():
        BANK_FILE_MAP[key] = _BANK_REMAPS.get(key, key)


_rebuild_bank_file_map()


def bank_stem(curriculum_key: str) -> str:
    return BANK_FILE_MAP.get(curriculum_key, curriculum_key)


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


def stages_as_catalog() -> list[tuple[str, str, list[tuple[str, str]]]]:
    """Shape used by Question Input catalog: (stage_key, stage_label, curricula)."""
    return [
        (stage_key, STAGES[stage_key]["label"], list(STAGES[stage_key]["curricula"]))
        for stage_key in STAGE_ORDER
    ]


def ensure_curriculum_banks(banks_dir: Path | str) -> list[str]:
    """Create missing empty bank JSON files for every curriculum stem. Returns created stems."""
    root = Path(banks_dir)
    root.mkdir(parents=True, exist_ok=True)
    created: list[str] = []
    stems = {bank_stem(key) for key, _label in all_curricula()}
    for stem in sorted(stems):
        path = root / f"{stem}.json"
        if path.exists():
            continue
        path.write_text(json.dumps(EMPTY_BANK, indent=2) + "\n", encoding="utf-8")
        created.append(stem)
    return created


def assert_curricula_wired(banks_dir: Path | str, specialties: dict | None = None) -> None:
    """Raise if any curriculum lacks a bank file, or in-memory bank is empty while file has items."""
    root = Path(banks_dir)
    missing_files: list[str] = []
    unloadable: list[str] = []
    for key, label in all_curricula():
        stem = bank_stem(key)
        path = root / f"{stem}.json"
        if not path.exists():
            missing_files.append(f"{key} ({label}) → {stem}.json")
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        file_n = sum(len(data.get(d) or []) for d in DIFFICULTIES)
        if specialties is not None and key in specialties:
            mem = specialties[key].get("questions") or {}
            mem_n = sum(len(mem.get(d) or []) for d in DIFFICULTIES)
            if file_n > 0 and mem_n == 0:
                unloadable.append(f"{key} ({label}): file has {file_n} Q but memory is empty")
    if missing_files or unloadable:
        parts = []
        if missing_files:
            parts.append("Missing bank files:\n- " + "\n- ".join(missing_files))
        if unloadable:
            parts.append("Wiring bugs (file not loaded):\n- " + "\n- ".join(unloadable))
        raise RuntimeError("Dentistry curricula not fully wired.\n" + "\n".join(parts))
