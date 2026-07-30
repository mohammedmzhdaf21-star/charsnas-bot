"""Precise scientific per-choice explanations for MCQ answers."""

from __future__ import annotations

import re
from typing import Any


def _clean(text: Any) -> str:
    text = " ".join(str(text or "").split())
    # Strip awkward template tails left by some generated banks.
    text = re.split(
        r"\s*It fails this stem,? which requires[^:]*:\s*",
        text,
        maxsplit=1,
        flags=re.I,
    )[0].strip()
    text = re.split(
        r"\s*This fails the stem.*?$",
        text,
        maxsplit=1,
        flags=re.I,
    )[0].strip()
    return text


def _trim(text: str, limit: int = 420) -> str:
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


def _first_sentences(text: str, n: int = 2) -> str:
    text = _clean(text)
    if not text:
        return ""
    parts = re.split(r"(?<=[.!?])\s+", text)
    return " ".join(parts[:n]).strip()


def _authored_map(item: dict[str, Any]) -> dict[str, str]:
    raw = item.get("choice_explanations") or item.get("option_explanations") or {}
    if not isinstance(raw, dict):
        return {}
    out: dict[str, str] = {}
    for k, v in raw.items():
        letter = str(k).strip().upper()[:1]
        if letter not in "ABCD":
            continue
        if isinstance(v, dict):
            text = _clean(
                v.get("why_not")
                or v.get("why_wrong")
                or v.get("why")
                or v.get("reason")
                or v.get("meaning")
                or ""
            )
        else:
            text = _clean(v)
        if text:
            out[letter] = text
    return out


def _scientific_correct(choice: str, explanation: str, question: str) -> str:
    core = _first_sentences(explanation, 2)
    if core:
        return core
    return (
        f"{choice} is the scientifically correct answer to the stem because it matches "
        f"the accepted definition or mechanism being tested."
    )


def _scientific_wrong(
    choice: str,
    correct_choice: str,
    explanation: str,
    question: str,
) -> str:
    """
    Build a precise contrast: what this option refers to vs what the stem actually requires.
    Prefers mechanism language from the bank explanation.
    """
    core = _first_sentences(explanation, 1)
    qlow = question.lower()
    clow = choice.lower()

    # Diagnosis-style stems
    if any(w in qlow for w in ("diagnosis", "suggests", "most likely", "suspect", "presents")):
        lead = (
            f"{choice} names a different clinical entity/mechanism than the one produced "
            f"by the findings in the stem."
        )
    elif any(w in qlow for w in ("treatment", "management", "next", "therapy", "drug", "given")):
        lead = (
            f"{choice} is not the intervention that correctly targets the pathophysiology "
            f"asked here."
        )
    elif any(w in qlow for w in ("record", "means", "definition", "refers", "primarily", "is?")):
        lead = (
            f"{choice} refers to a different physiologic signal, structure, or definition "
            f"than the one asked."
        )
    else:
        lead = f"{choice} does not correctly state the mechanism or definition required by the stem."

    if core:
        return (
            f"{lead} Scientifically, {correct_choice} fits because {core} "
            f"That does not describe {choice}."
        )
    return (
        f"{lead} The correct concept is {correct_choice}, which matches the stem’s "
        f"physiology/pathology; {choice} does not."
    )


def generate_choice_explanations(item: dict[str, Any]) -> dict[str, str]:
    options = options_as_dict(item)
    if not options:
        return {}
    correct = correct_letter(item, options)
    explanation = _clean(item.get("explanation"))
    question = _clean(item.get("question"))
    correct_choice = options.get(correct, "the correct answer")
    authored = _authored_map(item)

    out: dict[str, str] = {}
    for letter, choice in options.items():
        if letter in authored:
            out[letter] = authored[letter]
        elif letter == correct:
            out[letter] = _scientific_correct(choice, explanation, question)
        else:
            out[letter] = _scientific_wrong(
                choice, correct_choice, explanation, question
            )
    return out


def _trim_wrong_restatement(text: str, correct_choice: str, correct_expl: str) -> str:
    """Keep the scientific contrast for a distractor; drop a trailing restatement of the right answer."""
    text = _clean(text)
    if not text:
        return text
    sentences = re.split(r"(?<=[.!?])\s+", text)
    if len(sentences) <= 1:
        return text
    correct_tokens = {
        w for w in re.findall(r"[a-zA-Z]{5,}", (correct_choice + " " + correct_expl).lower())
    }
    kept = [sentences[0]]
    for sent in sentences[1:]:
        words = set(re.findall(r"[a-zA-Z]{5,}", sent.lower()))
        if correct_tokens and len(words & correct_tokens) >= 4:
            # Later sentence is mostly restating the correct concept — stop.
            break
        kept.append(sent)
    return " ".join(kept).strip()


def format_all_choice_explanations(item: dict[str, Any]) -> str:
    """Format a precise scientific breakdown for every option."""
    options = options_as_dict(item)
    if not options:
        return ""

    correct = correct_letter(item, options)
    generated = generate_choice_explanations(item)
    correct_choice = options.get(correct, "")
    correct_expl = generated.get(correct, _clean(item.get("explanation")))

    lines = [
        "Scientific reason for each choice",
        "",
    ]

    for letter in ("A", "B", "C", "D"):
        if letter not in options:
            continue
        choice = options[letter]
        is_correct = letter == correct
        tag = "Correct" if is_correct else "Incorrect"
        text = generated.get(letter, "")
        if not is_correct:
            text = _trim_wrong_restatement(text, correct_choice, correct_expl)
        text = _trim(text, 450)
        lines.append(f"{letter}) {choice}")
        lines.append(f"→ {tag}: {text}")
        lines.append("")

    return "\n".join(lines).rstrip()
