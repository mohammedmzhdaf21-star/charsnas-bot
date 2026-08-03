#!/usr/bin/env python3
"""Remove duplicate / near-duplicate Short MCQs from department banks.

Usage:
  python3 scripts/dedupe_question_banks.py              # dry-run all depts
  python3 scripts/dedupe_question_banks.py --apply      # write changes
  python3 scripts/dedupe_question_banks.py --dept dentistry --apply
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "question_input"))

from dedupe import find_similar  # noqa: E402

DIFFICULTIES = ("easy", "medium", "hard", "extreme")


def bank_dirs(dept: str | None) -> list[tuple[str, Path]]:
    mapping = {
        "medicine": ROOT / "question_banks",
        "dentistry": ROOT / "dentistry" / "question_banks",
        "pharmacy": ROOT / "pharmacy" / "question_banks",
        "mls": ROOT / "mls" / "question_banks",
        "nursing": ROOT / "nursing" / "question_banks",
    }
    if dept:
        return [(dept, mapping[dept])]
    return list(mapping.items())


def dedupe_bank(path: Path, apply: bool) -> tuple[int, int]:
    data = json.loads(path.read_text(encoding="utf-8"))
    kept_all: dict[str, list[dict]] = {d: [] for d in DIFFICULTIES}
    pool: list[dict] = []
    removed = 0
    total = 0
    for diff in DIFFICULTIES:
        items = data.get(diff) or []
        if not isinstance(items, list):
            continue
        for item in items:
            if not isinstance(item, dict):
                continue
            total += 1
            q = str(item.get("question") or "")
            match, score = find_similar(q, pool, mode="cleanup")
            if match is not None:
                removed += 1
                continue
            kept_all[diff].append(item)
            pool.append(item)
    if apply and removed:
        path.write_text(json.dumps(kept_all, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return total, removed


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="Write cleaned banks")
    ap.add_argument("--dept", choices=["medicine", "dentistry", "pharmacy", "mls", "nursing"])
    args = ap.parse_args()

    grand_total = grand_removed = 0
    for dept, folder in bank_dirs(args.dept):
        if not folder.is_dir():
            continue
        print(f"\n=== {dept} ({folder}) ===")
        for path in sorted(folder.glob("*.json")):
            total, removed = dedupe_bank(path, apply=args.apply)
            grand_total += total
            grand_removed += removed
            flag = "UPDATED" if args.apply and removed else ("would remove" if removed else "clean")
            print(f"  {path.name}: {total} Q → remove {removed} ({flag})")

    mode = "APPLIED" if args.apply else "DRY-RUN"
    print(f"\n{mode}: scanned {grand_total} questions, duplicate/similar {grand_removed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
