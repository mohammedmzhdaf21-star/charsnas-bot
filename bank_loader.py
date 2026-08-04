"""Load specialty MCQ banks from JSON (120 unique questions per specialty)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


DIFFICULTIES = ("easy", "medium", "hard", "extreme")
TARGET_PER_DIFFICULTY = 30
TARGET_PER_SPECIALTY = 120


def bank_path(banks_dir: Path, specialty_key: str) -> Path:
    return banks_dir / f"{specialty_key}.json"


EMPTY_BANK = {d: [] for d in DIFFICULTIES}


def ensure_bank_files(banks_dir: Path | str, specialty_keys: list[str]) -> list[str]:
    """Create missing empty bank JSON files so every specialty/curriculum is wired."""
    root = Path(banks_dir)
    root.mkdir(parents=True, exist_ok=True)
    created: list[str] = []
    for key in specialty_keys:
        path = bank_path(root, key)
        if path.exists():
            continue
        path.write_text(json.dumps(EMPTY_BANK, indent=2) + "\n", encoding="utf-8")
        created.append(key)
    return created


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
    root.mkdir(parents=True, exist_ok=True)
    ensure_bank_files(root, list(specialties.keys()))
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


CASE_DIFFICULTIES = ("easy", "medium", "hard")


def _read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def apply_custom_content(specialties: dict[str, dict], custom_dir: Path | str) -> None:
    """Merge user-submitted cases/books from custom_content into SPECIALTIES."""
    root = Path(custom_dir)
    if not root.is_dir():
        return
    for key, spec in specialties.items():
        if "_base_books" not in spec:
            spec["_base_books"] = list(spec.get("books") or [])
        books = list(spec["_base_books"])
        extra_books = _read_json(root / "books" / f"{key}.json", [])
        if isinstance(extra_books, list):
            for title in extra_books:
                t = str(title).strip()
                if t and t not in books:
                    books.append(t)
        spec["books"] = books

        if "_base_cases" not in spec:
            base = spec.get("cases") or {}
            spec["_base_cases"] = {
                d: list(base.get(d) or []) for d in CASE_DIFFICULTIES
            }
        merged = {d: list(spec["_base_cases"].get(d) or []) for d in CASE_DIFFICULTIES}
        extra_cases = _read_json(root / "cases" / f"{key}.json", {})
        if isinstance(extra_cases, dict):
            for d in CASE_DIFFICULTIES:
                for item in extra_cases.get(d) or []:
                    if isinstance(item, dict) and item.get("stem"):
                        merged[d].append(item)
        spec["cases"] = merged


def reload_department_content(
    specialties: dict[str, dict],
    banks_dir: Path | str,
    custom_dir: Path | str | None = None,
) -> None:
    """Reload MCQ banks and custom cases/books from disk (picks up input-bot saves)."""
    apply_question_banks(specialties, banks_dir)
    if custom_dir is not None:
        apply_custom_content(specialties, custom_dir)


def custom_pdf_paths(
    pdf_dir: Path | str,
    specialty_key: str,
    *,
    also_keys: list[str] | None = None,
) -> list[Path]:
    """Return uploaded/generated PDFs for a specialty/curriculum.

    Looks in:
      - pdfs/custom/<key>/*.pdf
      - pdfs/generated/<key>/*.pdf
      - pdfs/generated/*/<key>/*.pdf   (stage/curriculum layout from Input bot)
    """
    root = Path(pdf_dir)
    keys: list[str] = []
    for key in [specialty_key, *(also_keys or [])]:
        k = (key or "").strip()
        if k and k not in keys:
            keys.append(k)
    found: list[Path] = []
    seen: set[str] = set()

    def _add(path: Path) -> None:
        if not path.is_file() or path.suffix.lower() != ".pdf":
            return
        resolved = str(path.resolve())
        if resolved in seen:
            return
        seen.add(resolved)
        found.append(path)

    generated_root = root / "generated"
    for key in keys:
        custom_dir = root / "custom" / key
        if custom_dir.is_dir():
            for path in sorted(custom_dir.glob("*.pdf")):
                _add(path)
        direct_gen = generated_root / key
        if direct_gen.is_dir():
            for path in sorted(direct_gen.glob("*.pdf")):
                _add(path)
        if generated_root.is_dir():
            for path in sorted(generated_root.glob(f"*/{key}/*.pdf")):
                _add(path)
    return found
