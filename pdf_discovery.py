"""Single source of truth for locating uploaded + generated study PDFs.

Study bots must discover Input-bot topic PDFs saved under:
  pdfs/generated/<specialty>/
  pdfs/generated/<stage>/<specialty>/

and uploads under:
  pdfs/custom/<specialty>/

`sync_generated_into_custom` mirrors generated files into custom/ so lookups
cannot silently break again if a caller only checks the custom folder.
"""

from __future__ import annotations

import logging
import shutil
from pathlib import Path

log = logging.getLogger("charanas.pdf_discovery")


def specialty_pdf_keys(specialty_key: str, also_keys: list[str] | None = None) -> list[str]:
    keys: list[str] = []
    for key in [specialty_key, *(also_keys or [])]:
        k = (key or "").strip()
        if k and k not in keys:
            keys.append(k)
    return keys


def find_specialty_pdfs(
    pdf_dir: Path | str,
    specialty_key: str,
    *,
    also_keys: list[str] | None = None,
) -> list[Path]:
    """Return all PDFs for a specialty/curriculum (custom + generated).

    Deduplicates by filename so a mirrored custom/ copy of the same generated
    topic deck is not returned twice.
    """
    root = Path(pdf_dir)
    keys = specialty_pdf_keys(specialty_key, also_keys)
    found: list[Path] = []
    seen_names: set[str] = set()
    seen_resolved: set[str] = set()

    def _add(path: Path) -> None:
        if not path.is_file() or path.suffix.lower() != ".pdf":
            return
        resolved = str(path.resolve())
        if resolved in seen_resolved:
            return
        name_key = path.name.lower()
        if name_key in seen_names:
            return
        seen_resolved.add(resolved)
        seen_names.add(name_key)
        found.append(path)

    generated_root = root / "generated"
    for key in keys:
        # Prefer custom/ first (includes mirrored generated decks).
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


def iter_generated_pdfs(pdf_dir: Path | str) -> list[tuple[str, Path]]:
    """Yield (specialty_key, path) for every PDF under pdfs/generated/."""
    root = Path(pdf_dir) / "generated"
    if not root.is_dir():
        return []
    out: list[tuple[str, Path]] = []
    for path in sorted(root.rglob("*.pdf")):
        if not path.is_file():
            continue
        # generated/<specialty>/file.pdf  OR  generated/<stage>/<specialty>/file.pdf
        rel = path.relative_to(root)
        parts = rel.parts
        if len(parts) == 2:
            specialty = parts[0]
        elif len(parts) >= 3:
            specialty = parts[1]
        else:
            continue
        out.append((specialty, path))
    return out


def sync_generated_into_custom(pdf_dir: Path | str) -> list[Path]:
    """Copy generated topic PDFs into pdfs/custom/<specialty>/ (idempotent).

    Returns list of newly copied destinations. Existing same-name files are left
    alone; if content differs, a timestamped copy is not created — we only fill
    gaps so study bots that only scan custom/ still work.
    """
    root = Path(pdf_dir)
    copied: list[Path] = []
    for specialty, src in iter_generated_pdfs(root):
        dest_dir = root / "custom" / specialty
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / src.name
        if dest.exists():
            continue
        shutil.copy2(src, dest)
        copied.append(dest)
        log.info("Mirrored generated PDF into custom/: %s", dest)
    return copied


def assert_generated_pdfs_discoverable(
    pdf_dir: Path | str,
    *,
    also_key_map: dict[str, str] | None = None,
) -> dict[str, int]:
    """Raise if any generated PDF is not returned by find_specialty_pdfs.

    also_key_map: optional specialty -> alias stem (e.g. head_neck_anatomy -> anatomy)
    Returns {specialty: count} for discoverable generated specialties.
    """
    root = Path(pdf_dir)
    by_spec: dict[str, list[Path]] = {}
    for specialty, path in iter_generated_pdfs(root):
        by_spec.setdefault(specialty, []).append(path)

    missing: list[str] = []
    counts: dict[str, int] = {}
    for specialty, paths in sorted(by_spec.items()):
        also = []
        if also_key_map:
            mapped = also_key_map.get(specialty)
            if mapped and mapped != specialty:
                also.append(mapped)
        found = find_specialty_pdfs(root, specialty, also_keys=also)
        found_names = {p.name.lower() for p in found}
        for path in paths:
            custom_copy = root / "custom" / specialty / path.name
            if path.name.lower() in found_names or custom_copy.exists():
                continue
            missing.append(str(path))
        counts[specialty] = len(found)

    if missing:
        raise RuntimeError(
            "Generated PDFs are not discoverable by study-bot lookup:\n  - "
            + "\n  - ".join(missing[:20])
            + ("\n  ..." if len(missing) > 20 else "")
        )
    return counts
