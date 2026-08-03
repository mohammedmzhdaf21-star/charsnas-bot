#!/usr/bin/env python3
"""Fail if any department specialty/curriculum is missing a bank file or fails to load.

Usage:
  python3 scripts/check_curriculum_banks.py
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "question_input"))


def main() -> int:
    errors: list[str] = []

    # Dentistry — stages source of truth
    from dentistry.stages import (
        assert_curricula_wired,
        ensure_curriculum_banks,
        all_curricula,
        bank_stem,
    )

    dent_banks = ROOT / "dentistry" / "question_banks"
    created = ensure_curriculum_banks(dent_banks)
    if created:
        print("Created dentistry banks:", ", ".join(created))
    try:
        import os
        import runpy

        prev = os.getcwd()
        os.chdir(ROOT / "dentistry")
        try:
            dent_content = runpy.run_path(str(ROOT / "dentistry" / "content.py"))
        finally:
            os.chdir(prev)

        specs = dent_content["SPECIALTIES"]
        assert_curricula_wired(dent_banks, specs)
        print(f"Dentistry OK: {len(all_curricula())} curricula wired")
        for key, label in all_curricula():
            stem = bank_stem(key)
            q = specs[key]["questions"]
            n = sum(len(q[d]) for d in ("easy", "medium", "hard", "extreme"))
            print(f"  {key:32} → {stem}.json  ({n} Q)  {label}")
    except Exception as exc:
        errors.append(f"dentistry: {exc}")

    # Other departments via question_input catalog
    from catalog import DEPARTMENTS, ensure_all_department_banks
    from bank_loader import load_specialty_questions

    created_all = ensure_all_department_banks()
    for dept, stems in created_all.items():
        if stems:
            print(f"Created {dept} banks:", ", ".join(stems))

    for dept_key, dep in DEPARTMENTS.items():
        if dept_key == "dentistry":
            continue
        banks_dir = Path(dep["banks_dir"])
        for key, label in dep["specialties"]:
            path = banks_dir / f"{key}.json"
            if not path.exists():
                errors.append(f"{dept_key}/{key}: missing {path.name}")
                continue
            loaded = load_specialty_questions(banks_dir, key)
            if loaded is None:
                errors.append(f"{dept_key}/{key}: failed to load {path.name}")
            else:
                n = sum(len(loaded[d]) for d in ("easy", "medium", "hard", "extreme"))
                print(f"{dept_key:10} {key:28} ({n} Q)  {label}")

    if errors:
        print("\nFAILED:", file=sys.stderr)
        for e in errors:
            print(" -", e, file=sys.stderr)
        return 1
    print("\nAll department curricula/specialties are wired to bank files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
