"""Generate undergraduate medicine PDF study notes for the Telegram bot."""

from __future__ import annotations

from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

from content import PDF_CATALOG

PDF_DIR = Path(__file__).resolve().parent / "pdfs"

NOTES = {
    "anatomy": [
        "Upper limb: brachial plexus roots C5–T1; median nerve = C5–T1 (lateral + medial cords).",
        "Heart valves: aortic/pulmonic = 2nd ICS; tricuspid = lower left sternal; mitral = 5th ICS midclavicular.",
        "Portal triad in hepatoduodenal ligament: portal vein, proper hepatic artery, common bile duct.",
        "Femoral triangle: inguinal ligament, sartorius, adductor longus; NAVEL (lateral→medial).",
        "Cranial nerve exits: CN III/IV/VI via superior orbital fissure; CN VII via stylomastoid foramen.",
    ],
    "physiology": [
        "Cardiac output = HR × Stroke volume; MAP ≈ CO × SVR.",
        "Frank–Starling: ↑ venous return → ↑ EDV → ↑ stroke volume (within limits).",
        "ADH acts on V2 receptors in collecting duct → aquaporin-2 insertion → water reabsorption.",
        "Oxygen–hemoglobin dissociation: right shift (↑ unload) with ↑ CO2, ↑ H+, ↑ 2,3-BPG, ↑ temp.",
        "GFR is estimated clinically by creatinine clearance / eGFR equations.",
    ],
    "pathology": [
        "Inflammation cardinal signs: rubor, tumor, calor, dolor, functio laesa.",
        "Apoptosis: programmed cell death (caspases); necrosis: uncontrolled cell death with inflammation.",
        "Neoplasia hallmarks: sustained proliferation, evade growth suppressors, resist apoptosis, invade/metastasize.",
        "Atherosclerosis: endothelial injury → lipid accumulation → foam cells → fibrous plaque.",
        "Type I hypersensitivity: IgE-mediated (anaphylaxis, asthma); Type IV: T-cell mediated (TB skin test).",
    ],
    "pharmacology": [
        "Pharmacokinetics: Absorption, Distribution, Metabolism, Excretion (ADME).",
        "Zero-order elimination examples: phenytoin, ethanol, high-dose aspirin (capacity-limited).",
        "Beta-blockers: ↓ HR/contractility; caution in asthma (nonselective) and decompensated HF.",
        "ACE inhibitors: ↓ Ang II → vasodilation + ↓ aldosterone; side effects: cough, hyperkalemia, angioedema.",
        "Aminoglycosides: bactericidal, concentration-dependent; toxicity = ototoxicity + nephrotoxicity.",
    ],
    "clinical": [
        "ABCDE approach in emergencies: Airway, Breathing, Circulation, Disability, Exposure.",
        "Chest pain differentials: ACS, PE, aortic dissection, pneumothorax, pericarditis, GERD, MSK.",
        "Sepsis: infection + organ dysfunction; early cultures, antibiotics, fluids, source control.",
        "DKA: hyperglycemia + ketones + acidosis; treat with fluids, insulin, K+ monitoring.",
        "Postpartum hemorrhage 4 Ts: Tone, Trauma, Tissue, Thrombin.",
        "Always correlate history, exam, labs, and imaging — avoid isolated lab interpretation.",
    ],
}


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


def ensure_pdfs(pdf_dir: Path | None = None) -> list[Path]:
    """Create all catalog PDFs if missing; return their paths."""
    target = pdf_dir or PDF_DIR
    created: list[Path] = []
    for item in PDF_CATALOG:
        path = target / item["filename"]
        if not path.exists():
            write_pdf(path, item["title"], NOTES[item["key"]])
        created.append(path)
    return created


if __name__ == "__main__":
    paths = ensure_pdfs()
    for p in paths:
        print(p)
