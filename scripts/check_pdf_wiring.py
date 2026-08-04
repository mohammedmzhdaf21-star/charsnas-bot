#!/usr/bin/env python3
"""Fail if generated topic PDFs are not discoverable by study-bot lookup.

Also mirrors generated → custom so older custom-only scanners keep working.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from pdf_discovery import (  # noqa: E402
    assert_generated_pdfs_discoverable,
    find_specialty_pdfs,
    sync_generated_into_custom,
)

DEPARTMENT_PDF_DIRS = {
    "medicine": ROOT / "pdfs",
    "dentistry": ROOT / "dentistry" / "pdfs",
    "pharmacy": ROOT / "pharmacy" / "pdfs",
    "mls": ROOT / "mls" / "pdfs",
    "nursing": ROOT / "nursing" / "pdfs",
}


def _dentistry_alias_map() -> dict[str, str]:
    try:
        from dentistry.stages import PDF_FILE_MAP, BANK_FILE_MAP

        out = dict(BANK_FILE_MAP)
        out.update(PDF_FILE_MAP)
        return out
    except Exception:
        return {}


def main() -> int:
    alias_maps = {
        "dentistry": _dentistry_alias_map(),
    }
    any_pdfs = False
    for dept, pdf_dir in DEPARTMENT_PDF_DIRS.items():
        if not pdf_dir.exists():
            print(f"{dept}: pdf dir missing ({pdf_dir}) — skip")
            continue
        copied = sync_generated_into_custom(pdf_dir)
        if copied:
            print(f"{dept}: mirrored {len(copied)} generated PDF(s) into custom/")
        counts = assert_generated_pdfs_discoverable(
            pdf_dir,
            also_key_map=alias_maps.get(dept),
        )
        if not counts:
            print(f"{dept}: no generated topic PDFs yet (ok)")
            continue
        any_pdfs = True
        for specialty, n in sorted(counts.items()):
            # Smoke: custom-only path also non-empty after sync
            custom_only = list((pdf_dir / "custom" / specialty).glob("*.pdf")) if (pdf_dir / "custom" / specialty).is_dir() else []
            found = find_specialty_pdfs(pdf_dir, specialty)
            print(f"{dept:10} {specialty:28} discoverable={n} custom_mirror={len(custom_only)} total_found={len(found)}")
            if n == 0:
                raise SystemExit(f"{dept}/{specialty}: discoverable count is 0")
    print("PDF wiring OK" + (" (with generated decks)" if any_pdfs else " (no generated decks yet)"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
