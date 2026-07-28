"""Generate specialty-specific undergraduate medicine PDF notes."""

from __future__ import annotations

from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

from content import SPECIALTIES, SPECIALTY_ORDER

PDF_DIR = Path(__file__).resolve().parent / "pdfs"


def pdf_filename(specialty_key: str) -> str:
    return f"UG_Medicine_{specialty_key.title().replace(' ', '_')}_Notes.pdf"


def _styles():
    styles = getSampleStyleSheet()
    title = ParagraphStyle(
        "TitleLocal",
        parent=styles["Heading1"],
        fontSize=16,
        spaceAfter=12,
    )
    body = ParagraphStyle(
        "BodyLocal",
        parent=styles["BodyText"],
        fontSize=11,
        leading=15,
        spaceAfter=8,
    )
    note = ParagraphStyle(
        "NoteLocal",
        parent=styles["BodyText"],
        fontSize=9,
        leading=12,
        textColor="grey",
    )
    return title, body, note


def write_pdf(path: Path, title: str, bullets: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
    )
    title_style, body_style, note_style = _styles()
    story = [
        Paragraph(title, title_style),
        Paragraph("CharaNas — Undergraduate Medicine Department", body_style),
        Paragraph(
            "Study aid only. Confirm with your faculty curriculum and recommended textbooks.",
            note_style,
        ),
        Spacer(1, 0.4 * cm),
    ]
    for i, line in enumerate(bullets, start=1):
        story.append(Paragraph(f"<b>{i}.</b> {line}", body_style))
    doc.build(story)


def ensure_pdfs(pdf_dir: Path | None = None) -> dict[str, Path]:
    """Create specialty PDFs if missing; return map specialty_key → path."""
    target = pdf_dir or PDF_DIR
    paths: dict[str, Path] = {}
    for key in SPECIALTY_ORDER:
        data = SPECIALTIES[key]
        path = target / pdf_filename(key)
        if not path.exists():
            write_pdf(
                path,
                f"Undergraduate Medicine — {data['label']} Notes",
                data["pdf_notes"],
            )
        paths[key] = path
    return paths


def pdf_for_specialty(specialty_key: str, pdf_dir: Path | None = None) -> Path:
    paths = ensure_pdfs(pdf_dir)
    return paths[specialty_key]


if __name__ == "__main__":
    for key, path in ensure_pdfs().items():
        print(key, path)
