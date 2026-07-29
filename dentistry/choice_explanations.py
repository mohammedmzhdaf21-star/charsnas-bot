"""Textbook-style scientific explanations for each MCQ choice."""

from __future__ import annotations

import re
from typing import Any


def _clean(text: Any) -> str:
    return " ".join(str(text or "").split())


def _trim(text: str, limit: int = 360) -> str:
    text = _clean(text)
    if len(text) <= limit:
        return text
    cut = text[: limit - 1]
    if " " in cut:
        cut = cut.rsplit(" ", 1)[0]
    return cut.rstrip(".,;:") + "…"


def _strip_letter_prefix(text: str) -> str:
    return re.sub(r"^[A-D]\)\s*", "", _clean(text), flags=re.I)


def options_as_dict(item: dict[str, Any]) -> dict[str, str]:
    raw = item.get("options")
    out: dict[str, str] = {}
    if isinstance(raw, dict):
        for k, v in raw.items():
            letter = str(k).strip().upper()[:1]
            if letter in "ABCD":
                out[letter] = _strip_letter_prefix(str(v))
        return out
    if isinstance(raw, (list, tuple)):
        for i, v in enumerate(raw):
            text = _clean(v)
            m = re.match(r"^([A-D])\)\s*(.*)$", text, flags=re.I)
            if m:
                out[m.group(1).upper()] = _clean(m.group(2))
            elif i < 4:
                out["ABCD"[i]] = _strip_letter_prefix(text)
    return out


def correct_letter(item: dict[str, Any], options: dict[str, str] | None = None) -> str:
    options = options if options is not None else options_as_dict(item)
    raw = item.get("correct") or item.get("answer") or ""
    text = _clean(raw)
    m = re.match(r"^([A-D])\)\s*", text, flags=re.I)
    if m:
        return m.group(1).upper()
    letter = text.strip().upper()[:1]
    if letter in (options or {}):
        return letter
    needle = _strip_letter_prefix(text).lower()
    for k, v in (options or {}).items():
        if v.lower() == needle or needle in v.lower() or v.lower() in needle:
            return k
    return ""


# Lightweight concept notes used to make distractor explanations precise.
# Matched against option text (and sometimes the stem).
_CONCEPT_NOTES: list[tuple[tuple[str, ...], str]] = [
    (
        ("blood pressure", "bp "),
        "Blood pressure is the force of blood on artery walls, measured with a "
        "sphygmomanometer; it is hemodynamics, not an electrical recording.",
    ),
    (
        ("electrical activity", "ecg", "ekg", "depolar"),
        "The ECG records extracellular voltage changes produced by myocardial "
        "depolarization and repolarization over time.",
    ),
    (
        ("coronary calcium", "calcium score"),
        "Coronary calcium is assessed by CT calcium scoring, an anatomic/imaging "
        "marker of atherosclerosis, not by surface ECG.",
    ),
    (
        ("lung sound", "auscult"),
        "Lung sounds are acoustic findings from chest auscultation (airflow in airways), "
        "not cardiac electrical signals.",
    ),
    (
        ("leg swelling", "edema"),
        "Leg swelling suggests fluid retention or venous/lymphatic problems; it is not "
        "the classic symptom pattern of myocardial ischemia.",
    ),
    (
        ("chest discomfort", "chest pain", "angina", "exertion"),
        "Angina is myocardial ischemia causing retrosternal discomfort typically provoked "
        "by exertion and relieved by rest or nitrates.",
    ),
    (
        ("itchy rash", "rash"),
        "An itchy rash is a dermatologic finding and does not represent ischemic cardiac pain.",
    ),
    (
        ("double vision", "diplopia"),
        "Diplopia is a neuro-ophthalmic symptom and is not a feature of typical angina.",
    ),
    (
        ("dilate bronchi", "bronchodil"),
        "Bronchodilation acts on airway smooth muscle (e.g. β2-agonists); it is not "
        "aspirin’s main role in ACS.",
    ),
    (
        ("inhibit platelet", "antiplatelet", "aspirin"),
        "Aspirin irreversibly acetylates platelet COX-1, reducing thromboxane A2 and "
        "platelet aggregation — foundational in ACS antithrombotic care.",
    ),
    (
        ("kill bacteria", "antibiotic", "antibacterial"),
        "Antibacterial action treats infection; aspirin is not used as an antibiotic in ACS.",
    ),
    (
        ("lower potassium", "hypokal"),
        "Lowering potassium is unrelated to aspirin’s antiplatelet mechanism in coronary thrombosis.",
    ),
    (
        ("anterior", " lad"),
        "Anterior wall ischemia/infarction is typically from LAD occlusion and is reflected "
        "in precordial leads (e.g. V2–V4), not inferior leads II/III/aVF.",
    ),
    (
        ("inferior", " rca"),
        "Inferior wall infarction localizes to leads II, III, and aVF and is commonly due "
        "to RCA occlusion (less often a dominant LCx).",
    ),
    (
        ("posterior",),
        "Posterior infarction is suggested by posterior-lead changes or anterior reciprocal "
        "depression, not by ST elevation confined to II/III/aVF.",
    ),
    (
        ("right bundle", "rbbb"),
        "Right bundle branch block is a conduction abnormality; it is not the coronary "
        "territory implied by ST elevation in II/III/aVF.",
    ),
    (
        ("aortic stenosis",),
        "Aortic stenosis is typically a crescendo–decrescendo systolic ejection murmur "
        "radiating to the carotids, not a holosystolic apical murmur to the axilla.",
    ),
    (
        ("mitral regurgitation", " mr"),
        "Mitral regurgitation produces a high-pitched holosystolic murmur at the apex "
        "that radiates to the axilla.",
    ),
    (
        ("mitral stenosis",),
        "Mitral stenosis is a diastolic rumble (often with opening snap), not a holosystolic "
        "murmur to the axilla.",
    ),
    (
        ("pulmonic stenosis", "pulmonary stenosis"),
        "Pulmonic stenosis is a systolic ejection murmur at the left upper sternal border, "
        "not an apical holosystolic murmur radiating to the axilla.",
    ),
    (
        ("nitroglycerin", "nitrate"),
        "Nitroglycerin dilates veins (↓preload) and coronaries, reducing myocardial oxygen "
        "demand and often relieving ischemic pain when not contraindicated.",
    ),
    (
        ("digoxin",),
        "Digoxin increases contractility and increases vagal tone; it is not first-line "
        "acute anti-anginal relief.",
    ),
    (
        ("amiodarone",),
        "Amiodarone is an antiarrhythmic; it does not provide immediate angina symptom relief "
        "like a nitrate.",
    ),
    (
        ("steroid", "corticosteroid"),
        "Corticosteroids are anti-inflammatory/immunosuppressive drugs and are not acute "
        "anti-ischemic therapy for angina.",
    ),
    (
        ("right ventricular", "rv infarction"),
        "RV infarction (often with inferior MI) causes preload-dependent hypotension, raised "
        "JVP, and clear lungs; nitrates can drop preload dangerously.",
    ),
    (
        ("apical thrombus", "lv thrombus"),
        "LV apical thrombus is a complication of anterior infarct/akinesis, not the "
        "hemodynamic picture of nitrate-related hypotension with clear lungs and raised JVP.",
    ),
    (
        ("epinephrine", "adrenaline"),
        "Epinephrine treats anaphylaxis by α1 vasoconstriction, β1 cardiac support, and β2 "
        "bronchodilation, and it stabilizes mast cells.",
    ),
    (
        ("antihistamine",),
        "Antihistamines block histamine receptors and help itch/urticaria, but they do not "
        "rapidly reverse anaphylactic shock or airway obstruction.",
    ),
]


def _concept_note(text: str) -> str:
    low = f" {_clean(text).lower()} "
    for keys, note in _CONCEPT_NOTES:
        if any(k in low for k in keys):
            return note
    return ""


def _scientific_correct(choice: str, explanation: str, question: str) -> str:
    exp = _trim(explanation, 420)
    if exp:
        return exp
    note = _concept_note(choice) or _concept_note(question)
    if note:
        return note
    return (
        f"“{choice}” matches the accepted definition/mechanism of the concept asked in the stem."
    )


def _scientific_wrong(
    choice: str,
    correct_choice: str,
    explanation: str,
    question: str,
) -> str:
    note = _concept_note(choice)
    correct_note = _concept_note(correct_choice) or _concept_note(question)
    exp = _trim(explanation, 200)

    if note and correct_note:
        return (
            f"{note} That is why it is incorrect here. "
            f"The right answer is {correct_choice}: {correct_note}"
        )
    if note and exp:
        return (
            f"{note} Therefore it does not answer this stem. "
            f"{correct_choice} is correct because {exp}"
        )
    if note:
        return (
            f"{note} The stem instead requires {correct_choice}."
        )
    if exp:
        return (
            f"“{choice}” does not match the mechanism/definition being tested. "
            f"{correct_choice} is correct because {exp}"
        )
    return (
        f"“{choice}” describes a different structure, function, diagnosis, or treatment "
        f"than the one required. The scientifically correct answer is {correct_choice}."
    )


def generate_choice_explanations(item: dict[str, Any]) -> dict[str, str]:
    """Return letter -> one scientific paragraph (right or wrong)."""
    options = options_as_dict(item)
    if not options:
        return {}
    correct = correct_letter(item, options)
    explanation = _clean(item.get("explanation"))
    question = _clean(item.get("question"))
    correct_choice = options.get(correct, "the correct answer")

    out: dict[str, str] = {}
    for letter, choice in options.items():
        if letter == correct:
            out[letter] = _scientific_correct(choice, explanation, question)
        else:
            out[letter] = _scientific_wrong(
                choice, correct_choice, explanation, question
            )
    return out


def format_all_choice_explanations(item: dict[str, Any]) -> str:
    """Format a precise scientific breakdown for every option."""
    options = options_as_dict(item)
    if not options:
        return ""

    correct = correct_letter(item, options)
    authored = item.get("choice_explanations") or item.get("option_explanations") or {}
    generated = generate_choice_explanations(item)

    lines = [
        "Why each choice is right or wrong",
        "",
    ]

    for letter in ("A", "B", "C", "D"):
        if letter not in options:
            continue
        choice = options[letter]
        is_correct = letter == correct
        tag = "Correct" if is_correct else "Incorrect"

        text = ""
        if isinstance(authored, dict) and letter in authored and _clean(authored[letter]):
            raw = authored[letter]
            if isinstance(raw, dict):
                text = _clean(
                    raw.get("why_not")
                    or raw.get("why_wrong")
                    or raw.get("why")
                    or raw.get("reason")
                    or raw.get("meaning")
                    or ""
                )
            else:
                text = _clean(raw)
        if not text:
            text = generated.get(letter, "")

        lines.append(f"{letter}) {choice}")
        lines.append(f"→ {tag}: {text}")
        lines.append("")

    return "\n".join(lines).rstrip()
