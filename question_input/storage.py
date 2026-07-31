"""Persist user-entered content into department banks / custom folders."""

from __future__ import annotations

import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from catalog import DEPARTMENTS
except ImportError:  # pragma: no cover
    from question_input.catalog import DEPARTMENTS

DIFFICULTIES = ("easy", "medium", "hard", "extreme")
CASE_DIFFS = ("easy", "medium", "hard")


def _read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def department_paths(field: str) -> dict[str, Path]:
    dep = DEPARTMENTS[field]
    return {
        "banks_dir": Path(dep["banks_dir"]),
        "custom_dir": Path(dep["custom_dir"]),
        "pdf_dir": Path(dep["pdf_dir"]),
    }


def load_bank(field: str, specialty: str) -> dict[str, list[dict]]:
    path = department_paths(field)["banks_dir"] / f"{specialty}.json"
    data = _read_json(path, {d: [] for d in DIFFICULTIES})
    for d in DIFFICULTIES:
        data.setdefault(d, [])
    return data


def append_short_mcq(
    field: str,
    specialty: str,
    difficulty: str,
    *,
    question: str,
    options: list[str],
    answer_letter: str,
    explanation: str = "",
) -> dict[str, Any]:
    """Append one Short MCQ into the department specialty bank. Returns saved item."""
    if difficulty not in DIFFICULTIES:
        raise ValueError(f"invalid difficulty: {difficulty}")
    if len(options) != 4:
        raise ValueError("need exactly 4 options")
    letter = answer_letter.strip().upper()[:1]
    if letter not in "ABCD":
        raise ValueError("answer must be A, B, C, or D")

    labeled = []
    for i, text in enumerate(options):
        L = "ABCD"[i]
        t = text.strip()
        if re.match(rf"^{L}\)\s*", t, flags=re.I):
            labeled.append(re.sub(rf"^{L}\)\s*", f"{L}) ", t, count=1, flags=re.I))
        else:
            labeled.append(f"{L}) {t}")

    answer = labeled[ord(letter) - ord("A")]
    exp = (explanation or "").strip() or "User-submitted question."
    choice_explanations = {
        L: (exp if L == letter else "Not the best answer for this item.")
        for L in "ABCD"
    }

    bank = load_bank(field, specialty)
    idx = len(bank[difficulty])
    item = {
        "id": f"{specialty}:{difficulty}:custom:{idx}",
        "question": question.strip(),
        "options": labeled,
        "answer": answer,
        "explanation": exp,
        "choice_explanations": choice_explanations,
        "source": "user_input",
        "added_at": datetime.now(timezone.utc).isoformat(),
    }
    bank[difficulty].append(item)
    path = department_paths(field)["banks_dir"] / f"{specialty}.json"
    _write_json(path, bank)
    return item


def append_case(
    field: str,
    specialty: str,
    difficulty: str,
    *,
    title: str,
    stem: str,
    question: str,
    answer: str,
    discussion: str = "",
    book_hint: str = "",
) -> dict[str, Any]:
    if difficulty not in CASE_DIFFS:
        raise ValueError(f"invalid case difficulty: {difficulty}")
    custom_dir = department_paths(field)["custom_dir"]
    path = custom_dir / "cases" / f"{specialty}.json"
    data = _read_json(path, {d: [] for d in CASE_DIFFS})
    for d in CASE_DIFFS:
        data.setdefault(d, [])
    item = {
        "title": title.strip(),
        "stem": stem.strip(),
        "question": question.strip(),
        "answer": answer.strip(),
        "discussion": (discussion or "").strip() or "User-submitted case.",
        "book_hint": (book_hint or "").strip() or "Custom case",
        "source": "user_input",
        "added_at": datetime.now(timezone.utc).isoformat(),
    }
    data[difficulty].append(item)
    _write_json(path, data)
    return item


def append_book(field: str, specialty: str, title: str) -> str:
    custom_dir = department_paths(field)["custom_dir"]
    path = custom_dir / "books" / f"{specialty}.json"
    data = _read_json(path, [])
    if not isinstance(data, list):
        data = []
    title = title.strip()
    if title and title not in data:
        data.append(title)
        _write_json(path, data)
    return title


def save_pdf(field: str, specialty: str, src_path: Path, original_name: str) -> Path:
    pdf_dir = department_paths(field)["pdf_dir"] / "custom" / specialty
    pdf_dir.mkdir(parents=True, exist_ok=True)
    safe = re.sub(r"[^\w.\-]+", "_", original_name).strip("_") or "upload.pdf"
    if not safe.lower().endswith(".pdf"):
        safe += ".pdf"
    dest = pdf_dir / safe
    if dest.exists():
        stem = dest.stem
        dest = pdf_dir / f"{stem}_{int(datetime.now().timestamp())}.pdf"
    shutil.copy2(src_path, dest)
    meta_path = department_paths(field)["custom_dir"] / "pdfs" / f"{specialty}.json"
    meta = _read_json(meta_path, [])
    meta.append(
        {
            "file": dest.name,
            "original_name": original_name,
            "added_at": datetime.now(timezone.utc).isoformat(),
        }
    )
    _write_json(meta_path, meta)
    return dest


def bank_counts(field: str, specialty: str) -> dict[str, int]:
    bank = load_bank(field, specialty)
    return {d: len(bank.get(d) or []) for d in DIFFICULTIES}
