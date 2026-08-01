"""Generate specialty-specific undergraduate medicine PDF notes (5+ pages each)."""

from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

from content import SPECIALTIES, SPECIALTY_ORDER
from pdf_content import PDF_SECTIONS

try:
    from stages import PDF_FILE_MAP
except ImportError:  # pragma: no cover
    PDF_FILE_MAP = {}

PDF_DIR = Path(__file__).resolve().parent / "pdfs"


def pdf_filename(specialty_key: str) -> str:
    stem = PDF_FILE_MAP.get(specialty_key, specialty_key)
    return f"UG_Dentistry_{stem.title().replace(' ', '_')}_Notes.pdf"


def _styles():
    base = getSampleStyleSheet()
    return {
        "cover": ParagraphStyle(
            "Cover",
            parent=base["Title"],
            fontSize=22,
            leading=26,
            alignment=TA_CENTER,
            spaceAfter=18,
            textColor=colors.HexColor("#0f172a"),
        ),
        "subtitle": ParagraphStyle(
            "Subtitle",
            parent=base["Normal"],
            fontSize=12,
            alignment=TA_CENTER,
            spaceAfter=8,
            textColor=colors.HexColor("#334155"),
        ),
        "note": ParagraphStyle(
            "Note",
            parent=base["Normal"],
            fontSize=9,
            leading=12,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#64748b"),
            spaceAfter=16,
        ),
        "h1": ParagraphStyle(
            "H1",
            parent=base["Heading1"],
            fontSize=14,
            leading=18,
            spaceBefore=6,
            spaceAfter=10,
            textColor=colors.HexColor("#0f172a"),
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["BodyText"],
            fontSize=10.5,
            leading=15,
            alignment=TA_JUSTIFY,
            spaceAfter=9,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=base["BodyText"],
            fontSize=10.5,
            leading=14,
            leftIndent=12,
            spaceAfter=5,
        ),
        "caption": ParagraphStyle(
            "Caption",
            parent=base["Normal"],
            fontSize=8.5,
            leading=11,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#64748b"),
            spaceBefore=4,
            spaceAfter=12,
        ),
        "footer": ParagraphStyle(
            "Footer",
            parent=base["Normal"],
            fontSize=8,
            textColor=colors.HexColor("#94a3b8"),
        ),
    }


def _header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#94a3b8"))
    canvas.drawString(2 * cm, 1.2 * cm, "CharaNas UG Dentistry — study aid (not a textbook scan)")
    canvas.drawRightString(A4[0] - 2 * cm, 1.2 * cm, f"Page {doc.page}")
    canvas.restoreState()


def build_story(specialty_key: str) -> list:
    data = SPECIALTIES[specialty_key]
    styles = _styles()
    sections = PDF_SECTIONS[specialty_key]
    story: list = []

    # Cover
    story.append(Spacer(1, 2.5 * cm))
    story.append(Paragraph(f"Undergraduate Dentistry", styles["subtitle"]))
    story.append(Paragraph(f"{data['label']} Study Pack", styles["cover"]))
    story.append(Paragraph("CharaNas Dentistry — Specialty Notes", styles["subtitle"]))
    story.append(
        Paragraph(
            "Expanded notes with original schematic figures for revision. "
            "These are educational drawings inspired by standard undergraduate teaching themes, "
            "not copied textbook plates. Always follow your faculty curriculum and latest guidelines.",
            styles["note"],
        )
    )

    # Contents table
    rows = [["Section", "Focus"]]
    for i, section in enumerate(sections, start=1):
        rows.append([str(i), section["title"].split(". ", 1)[-1]])
    rows.append([str(len(sections) + 1), "Quick pearls from these notes"])
    rows.append([str(len(sections) + 2), "Recommended book sources"])
    table = Table(rows, colWidths=[2.2 * cm, 13 * cm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0f172a")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 10),
                ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#f8fafc")),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#cbd5e1")),
                ("PADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    story.append(table)
    story.append(PageBreak())

    # Main sections (aim: one major section per page where possible)
    for section in sections:
        block = [Paragraph(section["title"], styles["h1"])]
        for para in section["paras"]:
            block.append(Paragraph(para, styles["body"]))
        fig = section.get("figure")
        if fig is None and section.get("figure_name"):
            import pdf_content as _pc
            fig = getattr(_pc, section["figure_name"], None)
        if callable(fig):
            drawing = fig()
            block.append(Spacer(1, 0.2 * cm))
            block.append(drawing)
            block.append(
                Paragraph(
                    "Schematic figure for learning — verify details in your recommended textbooks.",
                    styles["caption"],
                )
            )
        # Extra revision bullets to thicken pages
        block.append(Paragraph("<b>Revision prompts</b>", styles["body"]))
        prompts = [
            f"Explain this section aloud in 60 seconds as if teaching a junior student about {data['label'].lower()}.",
            "List 3 red flags that would make you escalate care urgently.",
            "Name 2 investigations and 2 initial management steps you would consider first.",
        ]
        for p in prompts:
            block.append(Paragraph(f"• {p}", styles["bullet"]))
        story.append(KeepTogether(block))
        story.append(PageBreak())

    # Pearls page from content.pdf_notes
    story.append(Paragraph(f"{len(sections) + 1}. Quick pearls", styles["h1"]))
    story.append(
        Paragraph(
            "High-yield reminders packaged with this specialty in CharaNas:",
            styles["body"],
        )
    )
    for i, pearl in enumerate(data["pdf_notes"], start=1):
        story.append(Paragraph(f"<b>{i}.</b> {pearl}", styles["body"]))
    for extra in [
        "Link symptoms → anatomy/physiology → investigation → first management step.",
        "Write one OSCE-style explanation for a common presentation in this specialty.",
        "After reading, do the Short MCQ and Case-based Question for active recall.",
    ]:
        story.append(Paragraph(f"• {extra}", styles["bullet"]))
    story.append(PageBreak())

    # Books page
    story.append(Paragraph(f"{len(sections) + 2}. Recommended book sources", styles["h1"]))
    story.append(
        Paragraph(
            "Standard undergraduate references commonly used internationally. "
            "Use the edition your college recommends. Figures in commercial textbooks are copyrighted; "
            "use library/licensed access for full plates and photographs.",
            styles["body"],
        )
    )
    book_rows = [["#", "Reference"]]
    for i, book in enumerate(data["books"], start=1):
        book_rows.append([str(i), book])
    book_table = Table(book_rows, colWidths=[1.5 * cm, 14 * cm])
    book_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0f172a")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#cbd5e1")),
                ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#f8fafc")),
                ("PADDING", (0, 0), (-1, -1), 8),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    story.append(book_table)
    story.append(Spacer(1, 0.6 * cm))
    story.append(
        Paragraph(
            "How to study with this PDF: read one section → sketch the figure from memory → "
            "answer the MCQs/cases → review mistakes → revisit the matching section.",
            styles["body"],
        )
    )
    story.append(
        Paragraph(
            "Disclaimer: educational aid only; not a substitute for clinical guidelines, "
            "faculty teaching, or licensed textbooks.",
            styles["note"],
        )
    )
    return story


def write_specialty_pdf(path: Path, specialty_key: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=1.8 * cm,
        rightMargin=1.8 * cm,
        topMargin=1.8 * cm,
        bottomMargin=2 * cm,
        title=f"UG Medicine — {SPECIALTIES[specialty_key]['label']}",
        author="CharaNas Dentistry",
    )
    doc.build(build_story(specialty_key), onFirstPage=_header_footer, onLaterPages=_header_footer)


def ensure_pdfs(pdf_dir: Path | None = None, force: bool = False) -> dict[str, Path]:
    """Create PDFs only for curricula that have section content or an existing file."""
    target = pdf_dir or PDF_DIR
    paths: dict[str, Path] = {}
    for key in SPECIALTY_ORDER:
        path = target / pdf_filename(key)
        section_key = PDF_FILE_MAP.get(key, key)
        can_build = section_key in PDF_SECTIONS or key in PDF_SECTIONS
        if path.exists() and not force:
            paths[key] = path
            continue
        if can_build and (force or not path.exists()):
            build_key = key if key in PDF_SECTIONS else section_key
            # Prefer writing under curriculum filename using mapped content
            if build_key != key and build_key in PDF_SECTIONS:
                # Temporarily build from mapped specialty sections
                if key not in PDF_SECTIONS:
                    PDF_SECTIONS[key] = PDF_SECTIONS[build_key]
            write_specialty_pdf(path, key)
            paths[key] = path
        elif path.exists():
            paths[key] = path
    return paths


def pdf_for_specialty(specialty_key: str, pdf_dir: Path | None = None) -> Path | None:
    """Return an existing notes PDF for this curriculum, or None if not available yet."""
    target = pdf_dir or PDF_DIR
    path = target / pdf_filename(specialty_key)
    if path.exists():
        return path
    # Fall back to mapped legacy stem filename if present
    stem = PDF_FILE_MAP.get(specialty_key)
    if stem:
        legacy = target / f"UG_Dentistry_{stem.title().replace(' ', '_')}_Notes.pdf"
        if legacy.exists():
            return legacy
    return None


if __name__ == "__main__":
    for key, path in ensure_pdfs(force=True).items():
        from pypdf import PdfReader

        pages = len(PdfReader(str(path)).pages)
        print(f"{key}: {path.name} ({pages} pages)")
