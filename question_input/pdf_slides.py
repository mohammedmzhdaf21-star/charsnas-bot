"""Build 15–20 page topic slide PDFs with a centered CharaNas logo watermark."""

from __future__ import annotations

import io
import re
from pathlib import Path
from typing import Any

from PIL import Image as PILImage
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader
from reportlab.platypus import (
    Flowable,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)

ROOT = Path(__file__).resolve().parents[1]
# Exact brand mark — never redraw/recolor this file. Watermark only scales opacity.
LOGO_PATH = ROOT / "assets" / "charanas_logo.png"
NAVY = colors.HexColor("#0B2A4A")
SLATE = colors.HexColor("#334155")
MUTED = colors.HexColor("#64748b")
PAGE_SIZE = landscape(A4)
# Low opacity so the exact logo stays recognizable without blocking IMB text.
WATERMARK_OPACITY = 0.10


def _styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "cover_brand": ParagraphStyle(
            "CoverBrand",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=14,
            textColor=NAVY,
            alignment=TA_CENTER,
            spaceAfter=8,
        ),
        "cover_title": ParagraphStyle(
            "CoverTitle",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=26,
            leading=30,
            textColor=NAVY,
            alignment=TA_CENTER,
            spaceAfter=12,
        ),
        "cover_sub": ParagraphStyle(
            "CoverSub",
            parent=base["Normal"],
            fontSize=12,
            leading=16,
            textColor=SLATE,
            alignment=TA_CENTER,
            spaceAfter=6,
        ),
        "slide_title": ParagraphStyle(
            "SlideTitle",
            parent=base["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=18,
            leading=22,
            textColor=NAVY,
            spaceAfter=10,
        ),
        "body": ParagraphStyle(
            "SlideBody",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=11,
            leading=15,
            alignment=TA_JUSTIFY,
            textColor=colors.HexColor("#0f172a"),
            spaceAfter=7,
        ),
        "bullet": ParagraphStyle(
            "SlideBullet",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=11,
            leading=14.5,
            leftIndent=8,
            textColor=colors.HexColor("#0f172a"),
            spaceAfter=3,
        ),
        "pearl": ParagraphStyle(
            "Pearl",
            parent=base["BodyText"],
            fontName="Helvetica-Oblique",
            fontSize=10.5,
            leading=14,
            textColor=NAVY,
            spaceBefore=6,
            spaceAfter=4,
        ),
        "caption": ParagraphStyle(
            "FigCaption",
            parent=base["Normal"],
            fontName="Helvetica-Oblique",
            fontSize=9,
            leading=11,
            textColor=MUTED,
            alignment=TA_CENTER,
            spaceBefore=4,
            spaceAfter=6,
        ),
        "fig_label": ParagraphStyle(
            "FigLabel",
            parent=base["Normal"],
            fontSize=9.5,
            leading=12,
            textColor=SLATE,
            spaceAfter=2,
        ),
        "footer": ParagraphStyle(
            "Footer",
            parent=base["Normal"],
            fontSize=8,
            textColor=MUTED,
        ),
    }


def _escape(text: str) -> str:
    return (
        str(text or "")
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def _watermark_reader() -> ImageReader | None:
    """Load the brand logo unchanged except for watermark opacity.

    RGB channels are preserved exactly from assets/charanas_logo.png.
    Only the alpha channel is scaled so the mark does not distract from reading.
    """
    if not LOGO_PATH.exists():
        return None
    img = PILImage.open(LOGO_PATH).convert("RGBA")
    # Preserve every color pixel; only multiply alpha for soft watermarking.
    r, g, b, a = img.split()
    a = a.point(lambda p: int(p * WATERMARK_OPACITY))
    img = PILImage.merge("RGBA", (r, g, b, a))
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return ImageReader(buf)


_WATERMARK = None


def _get_watermark() -> ImageReader | None:
    global _WATERMARK
    if _WATERMARK is None:
        _WATERMARK = _watermark_reader()
    return _WATERMARK


def _draw_page_chrome(canvas, doc, *, brand_line: str) -> None:
    canvas.saveState()
    wm = _get_watermark()
    width, height = PAGE_SIZE
    if wm is not None:
        size = min(width, height) * 0.52
        x = (width - size) / 2
        y = (height - size) / 2
        canvas.drawImage(wm, x, y, width=size, height=size, mask="auto", preserveAspectRatio=True)
    canvas.setStrokeColor(colors.HexColor("#e2e8f0"))
    canvas.setLineWidth(0.6)
    canvas.rect(1.2 * cm, 1.1 * cm, width - 2.4 * cm, height - 2.2 * cm)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(MUTED)
    canvas.drawString(1.5 * cm, 0.7 * cm, brand_line[:90])
    canvas.drawRightString(width - 1.5 * cm, 0.7 * cm, f"Slide {doc.page}")
    canvas.restoreState()


class SchematicFigure(Flowable):
    """Textbook-style schematic sketch rendered from structured figure data."""

    def __init__(self, figure: dict[str, Any], width: float = 22 * cm, height: float = 7.2 * cm):
        super().__init__()
        self.figure = figure or {}
        self.width = width
        self.height = height

    def wrap(self, availWidth, availHeight):
        self.width = min(self.width, availWidth)
        return self.width, self.height

    def draw(self):
        kind = str(self.figure.get("kind") or "schematic").lower()
        c = self.canv
        c.setStrokeColor(NAVY)
        c.setFillColor(colors.HexColor("#f8fafc"))
        c.setLineWidth(1.2)
        c.roundRect(0, 0, self.width, self.height, 8, fill=1, stroke=1)

        title = str(self.figure.get("title") or self.figure.get("caption") or "Schematic")[:80]
        c.setFillColor(NAVY)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(10, self.height - 16, title)

        labels = [str(x).strip() for x in (self.figure.get("labels") or []) if str(x).strip()]
        notes = str(self.figure.get("sketch_notes") or self.figure.get("description") or "").strip()

        if kind in {"flowchart", "flow"}:
            self._draw_flow(c, labels)
        elif kind in {"table", "comparison"}:
            self._draw_comparison(c, labels)
        elif kind in {"anatomy", "anatomy_schematic", "labeled_anatomy"}:
            self._draw_anatomy(c, labels)
        else:
            self._draw_schematic(c, labels)

        if notes:
            c.setFillColor(MUTED)
            c.setFont("Helvetica-Oblique", 8)
            # wrap notes lightly
            line = notes[:140] + ("…" if len(notes) > 140 else "")
            c.drawString(10, 8, line)

    def _draw_flow(self, c, labels: list[str]):
        boxes = labels[:4] or ["Assessment", "Decision", "Action", "Review"]
        n = len(boxes)
        bw = min(4.2 * cm, (self.width - 40 - (n - 1) * 18) / n)
        bh = 1.5 * cm
        y = self.height / 2 - bh / 2
        xs = []
        gap = 18
        total = n * bw + (n - 1) * gap
        x0 = (self.width - total) / 2
        for i, lab in enumerate(boxes):
            x = x0 + i * (bw + gap)
            xs.append(x)
            c.setFillColor(colors.white)
            c.setStrokeColor(NAVY)
            c.roundRect(x, y, bw, bh, 6, fill=1, stroke=1)
            c.setFillColor(NAVY)
            c.setFont("Helvetica", 8)
            text = lab[:42]
            c.drawCentredString(x + bw / 2, y + bh / 2 - 3, text)
            if i < n - 1:
                c.setStrokeColor(NAVY)
                c.line(x + bw, y + bh / 2, x + bw + gap, y + bh / 2)
                c.line(x + bw + gap - 6, y + bh / 2 + 4, x + bw + gap, y + bh / 2)
                c.line(x + bw + gap - 6, y + bh / 2 - 4, x + bw + gap, y + bh / 2)

    def _draw_comparison(self, c, labels: list[str]):
        left = labels[0] if labels else "Feature A"
        right = labels[1] if len(labels) > 1 else "Feature B"
        extras = labels[2:6]
        mid = self.width / 2
        c.setFillColor(colors.white)
        c.roundRect(14, 28, mid - 28, self.height - 55, 6, fill=1, stroke=1)
        c.roundRect(mid + 8, 28, mid - 28, self.height - 55, 6, fill=1, stroke=1)
        c.setFillColor(NAVY)
        c.setFont("Helvetica-Bold", 9)
        c.drawCentredString(mid / 2 + 7, self.height - 40, left[:50])
        c.drawCentredString(mid + (mid / 2) - 7, self.height - 40, right[:50])
        c.setFont("Helvetica", 8)
        c.setFillColor(SLATE)
        for i, e in enumerate(extras[:4]):
            c.drawString(24, self.height - 58 - i * 14, f"• {e[:55]}")

    def _draw_anatomy(self, c, labels: list[str]):
        cx, cy, r = self.width / 2, self.height / 2 - 4, min(self.width, self.height) * 0.22
        c.setFillColor(colors.HexColor("#e2e8f0"))
        c.circle(cx, cy, r, fill=1, stroke=1)
        c.setFillColor(colors.white)
        c.circle(cx, cy, r * 0.45, fill=1, stroke=1)
        labs = labels[:6] or ["Landmark A", "Landmark B", "Landmark C", "Landmark D"]
        anchors = [
            (cx, cy + r + 10, cx, cy + r),
            (cx + r + 8, cy, cx + r, cy),
            (cx, cy - r - 10, cx, cy - r),
            (cx - r - 8, cy, cx - r, cy),
            (cx + r * 0.7, cy + r * 0.7, cx + r * 0.55, cy + r * 0.55),
            (cx - r * 0.7, cy - r * 0.7, cx - r * 0.55, cy - r * 0.55),
        ]
        c.setFont("Helvetica", 8)
        for i, lab in enumerate(labs):
            tx, ty, ax, ay = anchors[i]
            c.setStrokeColor(NAVY)
            c.line(ax, ay, tx, ty)
            c.setFillColor(NAVY)
            c.drawCentredString(tx, ty + (4 if ty >= cy else -10), lab[:40])

    def _draw_schematic(self, c, labels: list[str]):
        labs = labels[:5] or ["Key structure", "Related pathway", "Clinical cue", "Decision point"]
        box_h = 1.15 * cm
        y = self.height - 36 - box_h
        for i, lab in enumerate(labs):
            x = 16
            c.setFillColor(colors.white)
            c.setStrokeColor(NAVY)
            c.roundRect(x, y - i * (box_h + 6), self.width - 32, box_h, 5, fill=1, stroke=1)
            c.setFillColor(NAVY)
            c.setFont("Helvetica-Bold", 9)
            c.drawString(x + 10, y - i * (box_h + 6) + box_h / 2 - 3, f"{i + 1}. {lab[:90]}")


def _slide_flowables(slide: dict[str, Any], styles: dict[str, ParagraphStyle]) -> list:
    block: list = []
    title = _escape(slide.get("title") or "Untitled slide")
    num = slide.get("slide_number")
    prefix = f"Slide {num}: " if num else ""
    block.append(Paragraph(f"{prefix}{title}", styles["slide_title"]))

    for para in slide.get("body_paragraphs") or slide.get("paragraphs") or []:
        p = str(para).strip()
        if p:
            block.append(Paragraph(_escape(p), styles["body"]))

    bullets = [str(b).strip() for b in (slide.get("bullets") or []) if str(b).strip()]
    for b in bullets:
        block.append(Paragraph(f"• {_escape(b)}", styles["bullet"]))

    fig = slide.get("figure") or {}
    if isinstance(fig, dict) and str(fig.get("kind") or "none").lower() != "none":
        block.append(Spacer(1, 0.15 * cm))
        block.append(SchematicFigure(fig))
        cap = str(fig.get("caption") or fig.get("title") or "").strip()
        if cap:
            block.append(
                Paragraph(
                    f"Figure — {_escape(cap)} "
                    "(original CharaNas schematic for study; verify details in current textbooks/guidelines).",
                    styles["caption"],
                )
            )
        for lab in fig.get("labels") or []:
            if str(lab).strip():
                block.append(Paragraph(f"• {_escape(lab)}", styles["fig_label"]))

    pearl = str(slide.get("clinical_pearl") or slide.get("pearl") or "").strip()
    if pearl:
        block.append(Paragraph(f"<b>IMB clinical pearl:</b> {_escape(pearl)}", styles["pearl"]))

    return block


def build_topic_pdf(
    *,
    out_path: Path,
    department_label: str,
    stage_label: str,
    specialty_label: str,
    topic: str,
    slides: list[dict[str, Any]],
    sources: list[str] | None = None,
) -> Path:
    """Write a landscape slide PDF with centered logo watermark on every page."""
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    styles = _styles()
    brand = f"CharaNas · {department_label}"
    if stage_label:
        brand += f" · {stage_label}"
    brand += f" · {specialty_label}"

    def on_page(canvas, doc):
        _draw_page_chrome(canvas, doc, brand_line=brand)

    doc = SimpleDocTemplate(
        str(out_path),
        pagesize=PAGE_SIZE,
        leftMargin=1.6 * cm,
        rightMargin=1.6 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.4 * cm,
        title=f"CharaNas — {topic}",
        author="CharaNas",
    )

    story: list = []
    # Cover
    story.append(Spacer(1, 2.2 * cm))
    story.append(Paragraph("CharaNas Study Slides", styles["cover_brand"]))
    story.append(Paragraph(_escape(topic), styles["cover_title"]))
    path_line = department_label
    if stage_label:
        path_line += f" → {stage_label}"
    path_line += f" → {specialty_label}"
    story.append(Paragraph(_escape(path_line), styles["cover_sub"]))
    story.append(
        Paragraph(
            "Iraqi Medical Board (IMB)–style teaching notes with high-yield detail. "
            "Schematic figures are original study drawings inspired by standard textbook themes "
            "(not scanned copyrighted plates). Prefer the newest clinical guidelines for practice.",
            styles["cover_sub"],
        )
    )
    story.append(PageBreak())

    clean_slides = [s for s in slides if isinstance(s, dict)]
    for slide in clean_slides:
        story.extend(_slide_flowables(slide, styles))
        story.append(PageBreak())

    # Sources / closing slide
    story.append(Paragraph("Sources & revision reminder", styles["slide_title"]))
    story.append(
        Paragraph(
            "Use these slides for active recall alongside Short MCQs. "
            "Confirm drug doses, staging systems, and protocols against your college curriculum "
            "and the latest society guidelines.",
            styles["body"],
        )
    )
    for src in sources or []:
        if str(src).strip():
            story.append(Paragraph(f"• {_escape(src)}", styles["bullet"]))
    if not sources:
        story.append(
            Paragraph(
                "• Core undergraduate / IMB references for this specialty (latest editions)",
                styles["bullet"],
            )
        )
        story.append(
            Paragraph(
                "• Current national/international clinical practice guidelines where applicable",
                styles["bullet"],
            )
        )

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    return out_path


def safe_topic_filename(topic: str) -> str:
    stem = re.sub(r"[^\w.\-]+", "_", topic.strip()).strip("_") or "topic"
    return stem[:80]
