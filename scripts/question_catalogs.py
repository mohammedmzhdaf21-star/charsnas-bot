"""Merged specialty concept catalogs for bank generation."""

from __future__ import annotations

from catalogs_medicine import MEDICINE_CATALOG
from catalogs_dentistry import DENTISTRY_CATALOG
from catalogs_pharmacy import PHARMACY_CATALOG
from catalogs_mls import MLS_CATALOG
from catalogs_nursing import NURSING_CATALOG

CATALOGS = {
    "medicine": MEDICINE_CATALOG,
    "dentistry": DENTISTRY_CATALOG,
    "pharmacy": PHARMACY_CATALOG,
    "mls": MLS_CATALOG,
    "nursing": NURSING_CATALOG,
}

FIELD_DIRS = {
    "medicine": "question_banks",
    "dentistry": "dentistry/question_banks",
    "pharmacy": "pharmacy/question_banks",
    "mls": "mls/question_banks",
    "nursing": "nursing/question_banks",
}

for field, cat in CATALOGS.items():
    for spec, concepts in cat.items():
        if len(concepts) < 100:
            raise SystemExit(f"{field}/{spec} has only {len(concepts)} concepts")
