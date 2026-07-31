"""Load specialty MCQ banks from JSON (100 unique questions per specialty)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


DIFFICULTIES = ("easy", "medium", "hard", "extreme")
TARGET_PER_DIFFICULTY = 25
TARGET_PER_SPECIALTY = 100


def bank_path(banks_dir: Path, specialty_key: str) -> Path:
    return banks_dir / f"{specialty_key}.json"


def load_specialty_questions(banks_dir: Path, specialty_key: str) -> dict[str, list[dict[str, Any]]] | None:
    path = bank_path(banks_dir, specialty_key)
    if not path.exists():
        return None
    data = json.loads(path.read_text(encoding="utf-8"))
    out: dict[str, list[dict[str, Any]]] = {}
    for diff in DIFFICULTIES:
        items = data.get(diff) or []
        if not isinstance(items, list):
            raise ValueError(f"{path}: {diff} must be a list")
        out[diff] = items
    return out


def apply_question_banks(specialties: dict[str, dict], banks_dir: Path | str) -> None:
    """Replace SPECIALTIES[*]['questions'] from JSON banks when present."""
    root = Path(banks_dir)
    if not root.is_dir():
        return
    for key, spec in specialties.items():
        loaded = load_specialty_questions(root, key)
        if loaded is None:
            continue
        spec["questions"] = loaded


def validate_specialty_bank(questions: dict[str, list[dict[str, Any]]], specialty_key: str) -> list[str]:
    errors: list[str] = []
    stems: set[str] = set()
    total = 0
    for diff in DIFFICULTIES:
        items = questions.get(diff) or []
        total += len(items)
        if len(items) < TARGET_PER_DIFFICULTY:
            errors.append(f"{specialty_key}/{diff}: {len(items)} < {TARGET_PER_DIFFICULTY}")
        for i, q in enumerate(items):
            stem = str(q.get("question", "")).strip().lower()
            if not stem:
                errors.append(f"{specialty_key}/{diff}[{i}]: empty question")
                continue
            if stem in stems:
                errors.append(f"{specialty_key}: duplicate stem: {stem[:80]}")
            stems.add(stem)
            opts = q.get("options") or []
            ans = q.get("answer")
            if len(opts) != 4:
                errors.append(f"{specialty_key}/{diff}[{i}]: need 4 options")
            if ans not in opts:
                errors.append(f"{specialty_key}/{diff}[{i}]: answer not in options")
            ce = q.get("choice_explanations") or {}
            if not all(L in ce and str(ce[L]).strip() for L in "ABCD"):
                errors.append(f"{specialty_key}/{diff}[{i}]: incomplete choice_explanations")
    if total < TARGET_PER_SPECIALTY:
        errors.append(f"{specialty_key}: total {total} < {TARGET_PER_SPECIALTY}")
    return errors
