#!/usr/bin/env python3
"""Validate USMLE-style question banks."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANNED = re.compile(
    r"high[- ]stakes|junior colleague|junior doctor|a student analyzes|"
    r"item\s*#?\s*\d+|single best answer|beware of near-miss|"
    r"choose the most accurate option and beware|in clinical practice regarding|"
    r"which statement best matches the core concept|"
    r"which choice is the single best|key teaching point:",
    re.I,
)

DIRS = [
    ROOT / "question_banks",
    ROOT / "dentistry" / "question_banks",
    ROOT / "pharmacy" / "question_banks",
    ROOT / "mls" / "question_banks",
    ROOT / "nursing" / "question_banks",
]


def main() -> int:
    errors: list[str] = []
    files = 0
    for d in DIRS:
        if not d.is_dir():
            errors.append(f"missing dir {d}")
            continue
        for path in sorted(d.glob("*.json")):
            files += 1
            data = json.loads(path.read_text(encoding="utf-8"))
            stems: set[str] = set()
            for diff in ("easy", "medium", "hard", "extreme"):
                qs = data.get(diff) or []
                if len(qs) != 30:
                    errors.append(f"{path.name}/{diff}: {len(qs)} != 30")
                for i, q in enumerate(qs):
                    stem = str(q.get("question", "")).strip()
                    low = stem.lower()
                    if not stem:
                        errors.append(f"{path.name}/{diff}[{i}] empty")
                        continue
                    if low in stems:
                        errors.append(f"{path.name} duplicate: {stem[:80]}")
                    stems.add(low)
                    if BANNED.search(stem):
                        errors.append(f"{path.name}/{diff}[{i}] banned phrase: {stem[:100]}")
                    opts = q.get("options") or []
                    if len(opts) != 4 or q.get("answer") not in opts:
                        errors.append(f"{path.name}/{diff}[{i}] bad options/answer")
                    ce = q.get("choice_explanations") or {}
                    if not all(str(ce.get(L, "")).strip() for L in "ABCD"):
                        errors.append(f"{path.name}/{diff}[{i}] incomplete explanations")
            if len(stems) != 120:
                errors.append(f"{path.name}: unique stems {len(stems)} != 120")
    print(f"checked {files} bank files")
    if errors:
        print(f"ERRORS {len(errors)}")
        for e in errors[:40]:
            print(" -", e)
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
