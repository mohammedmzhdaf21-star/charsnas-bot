#!/usr/bin/env python3
"""Generate standardized-exam Short MCQ banks (USMLE/INBDE/NAPLEX/NCLEX/MLS style).

30 easy + 30 medium + 30 hard + 30 extreme = 120 unique questions per specialty.
All four options are clinical near-misses from the same specialty catalog.
Never uses wrong1/wrong2 (easy rule-outs). No meta exam wording in stems.
"""

from __future__ import annotations

import json
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from question_catalogs import CATALOGS  # noqa: E402

DIFFICULTIES = ("easy", "medium", "hard", "extreme")
PER_DIFF = 30
SEED = 20260731

BANNED = re.compile(
    r"high[- ]stakes|junior colleague|junior doctor|a student analyzes|"
    r"item\s*#?\s*\d+|single best answer|beware of near-miss|"
    r"core concept of|best choice answer|which statement best matches|"
    r"in clinical practice regarding|key teaching point|teaching point|"
    r"which choice is the single best|student (did|does|analyzes)|"
    r"for a student|board-style|short vignette|flashcard",
    re.I,
)

TOPIC_FIXES = {
    "sl nitroglycerin angina": "sublingual nitroglycerin in angina",
    "acei post-mi hf": "ACE inhibitor use after MI with heart failure",
    "hfref beta-blocker": "evidence-based beta-blockade in HFrEF",
    "new lbbb equivalent": "new LBBB as a STEMI equivalent",
    "type a dissection caution": "type A aortic dissection caution in ACS pathways",
    "unstable angina def": "unstable angina",
    "nstemi def": "NSTEMI",
    "wct treat as vt": "regular wide-complex tachycardia",
    "pulseless vt/vf": "pulseless VT or VF",
    "chb pacing": "pacing readiness in high-grade AV block",
    "as clinical triad": "symptomatic severe aortic stenosis",
    "ms murmur": "the murmur of mitral stenosis",
    "hocm valsalva": "the HOCM murmur response to Valsalva",
    "pe ecg": "ECG findings in pulmonary embolism",
    "abi <0.9": "an ABI below 0.9",
    "af anticoagulation": "anticoagulation decisions in atrial fibrillation",
    "af rate control": "rate control in stable atrial fibrillation",
    "hyperk ecg": "ECG changes of hyperkalemia",
    "hypok ecg": "ECG changes of hypokalemia",
    "rv infarction": "right ventricular infarction",
    "inferior stemi leads": "inferior STEMI localization",
    "anterior stemi": "anterior STEMI localization",
    "lateral stemi": "lateral STEMI localization",
    "primary pci": "primary PCI for STEMI",
    "dapt post stent": "DAPT after coronary stenting",
    "acute apical abscess": "acute apical abscess",
    "pulp necrosis signs": "pulp necrosis",
}

RULEOUTISH = re.compile(
    r"^(equals|always equals|never |only isolated|ignore |panic explains|"
    r"skin tags prove|watchful waiting|oral digoxin bolus|routine iv steroids|"
    r"chest physiotherapy|fluid restriction alone|antibiotics as lipid|"
    r"nitrates lower ldl|steroids as antiplatelet)",
    re.I,
)


def clean(s: str) -> str:
    s = re.sub(r"\s+", " ", (s or "").strip())
    s = BANNED.sub("", s)
    return s.strip(" :,-")


def phrase_topic(topic: str) -> str:
    raw = clean(topic)
    key = raw.lower().strip()
    if key in TOPIC_FIXES:
        return TOPIC_FIXES[key]
    t = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", raw)
    t = t.replace("_", " ")
    replacements = [
        (r"\bdef\b", ""),
        (r"\bmech(anism)?\b", "mechanism"),
        (r"\bsigns?\b", ""),
        (r"\bcaution\b", ""),
        (r"\bRx\b", "treatment"),
        (r"\bdx\b", "diagnosis"),
        (r"\bSL\b", "sublingual"),
    ]
    for pat, rep in replacements:
        t = re.sub(pat, rep, t, flags=re.I)
    phrase = re.sub(r"\s+", " ", t).strip(" -")
    # Prefer sentence-friendly casing
    if phrase and not phrase.isupper():
        phrase = phrase[0].lower() + phrase[1:]
    return phrase or raw.lower()


def letters_options(texts: list[str]) -> tuple[list[str], dict[str, str]]:
    opts = []
    mapping = {}
    for i, t in enumerate(texts):
        L = "ABCD"[i]
        opts.append(f"{L}) {t}")
        mapping[L] = t
    return opts, mapping


def _tokens(s: str) -> set[str]:
    stop = {
        "the", "and", "with", "from", "for", "that", "this", "into", "only",
        "most", "more", "than", "when", "after", "before", "over", "under",
        "a", "an", "of", "in", "to", "on", "or", "as", "by", "is", "are",
        "be", "not", "no", "all", "any", "may", "can", "if", "vs",
    }
    words = re.findall(r"[a-z0-9]+", (s or "").lower())
    return {w for w in words if len(w) > 2 and w not in stop}


def pick_related(topics: list[dict], idx: int, rng: random.Random, k: int = 8) -> list[dict]:
    """Prefer catalog neighbors that share clinical tokens with the stem topic."""
    base = topics[idx]
    base_tok = _tokens(
        " ".join([base["topic"], base["correct"], base["near"], base.get("mechanism", "")])
    )
    scored: list[tuple[float, int, dict]] = []
    for j, t in enumerate(topics):
        if j == idx:
            continue
        tok = _tokens(" ".join([t["topic"], t["correct"], t["near"]]))
        overlap = len(base_tok & tok)
        # Small bonus for catalog adjacency (same organ-system cluster)
        adj = 1.0 if min(abs(j - idx), len(topics) - abs(j - idx)) <= 4 else 0.0
        score = overlap * 3.0 + adj + rng.random() * 0.2
        scored.append((score, j, t))
    scored.sort(key=lambda x: x[0], reverse=True)
    out = []
    seen = set()
    for score, j, t in scored:
        if t["topic"] in seen:
            continue
        # Require some overlap when possible
        if score < 1.0 and len(out) >= 3:
            continue
        seen.add(t["topic"])
        out.append(t)
        if len(out) >= k:
            break
    return out


def similar_length(correct: str, candidate: str) -> bool:
    if not candidate:
        return False
    if abs(len(candidate) - len(correct)) > 50 and len(candidate) > 65:
        return False
    return True


def build_options(
    topic: dict, related: list[dict], rng: random.Random
) -> tuple[str, list[str], dict[str, str], str]:
    correct = clean(topic["correct"])
    near = clean(topic["near"])
    base_tok = _tokens(" ".join([topic["topic"], correct, near, topic.get("mechanism", "")]))

    # Prefer near-misses first (topic near + related nears), then related corrects
    pool_priority: list[str] = [near]
    for r in related:
        pool_priority.append(clean(r["near"]))
    for r in related:
        pool_priority.append(clean(r["correct"]))

    uniq: list[str] = []
    seen = {correct.lower()}

    def accept(p: str, require_overlap: bool, strict_len: bool) -> bool:
        if not p or p.lower() in seen:
            return False
        if RULEOUTISH.search(p):
            return False
        if strict_len and not similar_length(correct, p):
            return False
        if require_overlap and base_tok and not (_tokens(p) & base_tok):
            return False
        return True

    for require_overlap, strict_len in (
        (True, True),
        (True, False),
        (False, True),
        (False, False),
    ):
        for p in pool_priority:
            if accept(p, require_overlap=require_overlap, strict_len=strict_len):
                seen.add(p.lower())
                uniq.append(p)
            if len(uniq) >= 3:
                break
        if len(uniq) >= 3:
            break

    if len(uniq) < 3:
        for p in pool_priority:
            if p and p.lower() not in seen:
                uniq.append(p)
                seen.add(p.lower())
            if len(uniq) >= 3:
                break
    while len(uniq) < 3:
        uniq.append(
            f"Closely related alternative interpretation involving {phrase_topic(topic['topic'])}"
        )
    distractors = uniq[:3]
    texts = [correct] + distractors
    rng.shuffle(texts)
    opts, mapping = letters_options(texts)
    answer = next(o for o in opts if o.split(") ", 1)[1] == correct)
    return correct, opts, mapping, answer


def stem_for(difficulty: str, topic: dict, n: int, rng: random.Random) -> str:
    label = phrase_topic(topic["topic"])
    mech = clean(topic.get("mechanism", ""))
    age = 24 + (n * 7 + len(label) * 3) % 52
    sex = "woman" if (n + len(label)) % 2 == 0 else "man"
    setting = [
        "clinic",
        "the emergency department",
        "the ward",
        "urgent care",
        "outpatient follow-up",
    ][n % 5]

    if difficulty == "easy":
        templates = [
            f"Which statement about {label} is most accurate?",
            f"Which finding is most consistent with {label}?",
            f"Which option best characterizes {label}?",
            f"In {label}, which description is most correct?",
            f"Which interpretation of {label} is most appropriate?",
            f"Which option most accurately describes {label}?",
            f"Regarding {label}, which statement is most correct?",
            f"Which feature most reliably supports {label}?",
        ]
        if n % 9 == 3 and mech:
            return f"Which physiologic or pharmacologic explanation best accounts for {label}?"
        return templates[n % len(templates)]

    if difficulty == "medium":
        templates = [
            f"A {age}-year-old {sex} is evaluated in {setting} for a presentation related to {label}. Which option is most likely?",
            f"A {age}-year-old {sex} has symptoms and findings pointing toward {label}. Which option best unifies the data?",
            f"During assessment for possible {label}, which option is the most accurate conclusion?",
            f"A {age}-year-old {sex} with relevant risk factors develops features of {label}. Which option is most appropriate?",
            f"Workup in {setting} for {label} is underway. Which option is most consistent with the expected process?",
            f"A {age}-year-old {sex} reports a history suggestive of {label}. Which option is most accurate?",
            f"In a patient with suspected {label}, which option is the most likely explanation?",
            f"A {age}-year-old {sex} undergoes evaluation for {label}. Which option should guide clinical reasoning?",
        ]
        return templates[n % len(templates)]

    if difficulty == "hard":
        templates = [
            f"A {age}-year-old {sex} presents with overlapping features of {label}. Closely related alternatives remain on the differential. After integrating history, examination, and initial tests, which option is most likely?",
            f"A hospitalized {age}-year-old {sex} develops evolving findings related to {label}. Early data are incomplete. Which option best fits the overall picture?",
            f"A {age}-year-old {sex} with comorbidities is evaluated for {label}. Near-miss alternatives share several features. Which option is favored?",
            f"Diagnostic uncertainty surrounds {label}. Common textbook mimics are considered. Which option is the most likely primary process?",
            f"A {age}-year-old {sex} has incomplete data for {label}. Which option is most consistent once close differentials are weighed?",
            f"Findings attributed to {label} can be misinterpreted. Which option is most correct?",
            f"A {age}-year-old {sex} presents with {label}. Pathophysiologic reasoning is required to separate the true process from nearby alternatives. Which option is most likely?",
            f"For a presentation dominated by {label}, which option is most accurate?",
        ]
        return templates[n % len(templates)]

    templates = [
        f"A {age}-year-old {sex} with multiple comorbidities develops rapidly progressive features of {label}. Initial assessment is compatible with more than one process. After synthesizing vital signs, examination, and key investigations, which option is most likely?",
        f"In the emergency setting, a critically ill {age}-year-old {sex} shows a syndrome centered on {label}. Competing explanations remain active. Which option best accounts for the presentation?",
        f"A deteriorating {age}-year-old {sex} has findings of {label} with incomplete data. Near-miss alternatives cannot be excluded on the first pass. Which option is the most likely primary driver?",
        f"Overnight, a {age}-year-old {sex} worsens with {label}. Timing, risk factors, and early diagnostics favor one process over close mimics. Which option is most likely?",
        f"A complex presentation involving {label} requires distinguishing the true driver from closely related alternatives. Which option is most likely?",
        f"A {age}-year-old {sex} develops life-threatening features linked to {label}. Which option is most consistent with the dominant pathophysiology?",
        f"When several closely related explanations for {label} compete, which option is most likely?",
        f"A high-acuity presentation involving {label} is reviewed with incomplete data. Which option is most likely?",
    ]
    return templates[n % len(templates)]


def explanations(
    topic: dict,
    correct: str,
    mapping: dict[str, str],
    answer_letter: str,
) -> tuple[str, dict[str, str]]:
    mech = clean(topic.get("mechanism", ""))
    why_near = clean(topic.get("why_near", ""))
    near = clean(topic["near"])
    overall = (
        f"{mech} Therefore, {correct} is the most coherent choice. "
        f"{why_near or 'Nearby alternatives share overlapping features but fit less well overall.'}"
    ).strip()
    ce = {}
    for L, text in mapping.items():
        if L == answer_letter:
            ce[L] = f"{mech} This option matches the dominant process.".strip()
            if len(ce[L]) < 40:
                ce[L] = f"{ce[L]} It correctly identifies: {correct}."
        elif text.lower() == near.lower():
            ce[L] = (
                f"{why_near or 'This is a frequent near-miss with overlapping features.'} "
                f"It remains less consistent than the correct option."
            ).strip()
        else:
            ce[L] = (
                "This alternative can appear on a thoughtful differential for related presentations, "
                "but the discriminating findings align more closely with the correct option."
            )
        if len(ce[L]) < 40:
            ce[L] += " Careful comparison of mechanism and clinical pattern separates it."
    return overall, ce


def build_specialty(field: str, specialty: str, topics: list[dict], out_path: Path) -> None:
    rng = random.Random(f"{SEED}:{field}:{specialty}")
    bank: dict[str, list] = {d: [] for d in DIFFICULTIES}
    used_stems: set[str] = set()
    letter_counts = {L: 0 for L in "ABCD"}

    for difficulty in DIFFICULTIES:
        i = 0
        guard = 0
        while len(bank[difficulty]) < PER_DIFF and guard < PER_DIFF * 60:
            guard += 1
            idx = i % len(topics)
            topic = topics[idx]
            stem = clean(stem_for(difficulty, topic, i, rng))
            if not stem or BANNED.search(stem) or stem.lower() in used_stems:
                i += 1
                continue

            related = pick_related(topics, idx, rng)
            correct, opts, mapping, answer = build_options(topic, related, rng)
            answer_letter = answer[0]
            if letter_counts[answer_letter] > (sum(letter_counts.values()) / 4.0) + 4:
                texts = [mapping[L] for L in "ABCD"]
                rng.shuffle(texts)
                opts, mapping = letters_options(texts)
                answer = next(o for o in opts if o.split(") ", 1)[1] == correct)
                answer_letter = answer[0]

            overall, ce = explanations(topic, correct, mapping, answer_letter)
            if BANNED.search(overall):
                overall = BANNED.sub("", overall).strip()

            bank[difficulty].append(
                {
                    "question": stem,
                    "options": opts,
                    "answer": answer,
                    "explanation": overall,
                    "choice_explanations": ce,
                }
            )
            used_stems.add(stem.lower())
            letter_counts[answer_letter] += 1
            i += 1

        if len(bank[difficulty]) < PER_DIFF:
            raise RuntimeError(
                f"{field}/{specialty}/{difficulty}: only {len(bank[difficulty])} questions"
            )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(bank, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {out_path.relative_to(ROOT)} (120 Qs)")


def main() -> None:
    for field, specialties in CATALOGS.items():
        base = ROOT if field == "medicine" else ROOT / field
        for specialty, topics in specialties.items():
            if len(topics) < 30:
                raise RuntimeError(f"{field}/{specialty}: catalog too small ({len(topics)})")
            build_specialty(field, specialty, topics, base / "question_banks" / f"{specialty}.json")
    print("Done.")


if __name__ == "__main__":
    main()
