#!/usr/bin/env python3
"""Generate original board-style Short MCQ banks (NOT copied from copyrighted QBanks).

Style targets (original content only):
  medicine  → USMLE / NBME vignette style
  dentistry → INBDE / NBDE vignette style
  pharmacy  → NAPLEX-style applied therapeutics
  mls       → BOC/ASCP-style laboratory reasoning
  nursing   → NCLEX-style clinical judgment

30 easy + 30 medium + 30 hard + 30 extreme = 120 unique stems per specialty.
All four choices are close near-misses from the same specialty catalog.
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
    r"incomplete data|competing explanations|closely related alternatives|"
    r"primary driver|unifies the|overall (picture|clinical picture)|after synthesizing|"
    r"pathophysiologic reasoning|high-acuity|presentation related to|"
    r"features linked to|diagnostic uncertainty|near-miss|near miss|"
    r"overlapping features of|high[- ]stakes|junior colleague|item\s*#|"
    r"single best answer|core concept of|short vignette|board-style|"
    r"which option is most|expected process|workup in .{0,40} is underway|"
    r"history suggestive of|"
    r"multiple comorbidities develops rapidly progressive|"
    r"true driver|dominant pathophysiology|several closely related explanations",
    re.I,
)

RULEOUTISH = re.compile(
    r"^(equals|always equals|never |only isolated|ignore |panic explains|"
    r"skin tags prove|watchful waiting|chest physiotherapy|antibiotics as lipid|"
    r"steroids as antiplatelet|means ecg always)",
    re.I,
)

TOPIC_FIXES = {
    "sl nitroglycerin angina": "sublingual nitroglycerin in angina",
    "acei post-mi hf": "ACE inhibitor therapy after MI with heart failure",
    "hfref beta-blocker": "beta-blocker therapy in HFrEF",
    "new lbbb equivalent": "new left bundle branch block with ischemic symptoms",
    "unstable angina def": "unstable angina",
    "nstemi def": "NSTEMI",
    "wct treat as vt": "regular wide-complex tachycardia",
    "pulseless vt/vf": "pulseless ventricular tachycardia or fibrillation",
    "as clinical triad": "severe symptomatic aortic stenosis",
    "mr murmur": "mitral regurgitation",
    "ms murmur": "mitral stenosis",
    "ar murmur": "aortic regurgitation",
    "hocm valsalva": "hypertrophic obstructive cardiomyopathy",
    "pe ecg": "pulmonary embolism",
    "af anticoagulation": "stroke prevention in atrial fibrillation",
    "af rate control": "rate control in atrial fibrillation",
    "hyperk ecg": "hyperkalemia",
    "hypok ecg": "hypokalemia",
    "rv infarction": "right ventricular infarction",
    "inferior stemi leads": "inferior STEMI",
    "anterior stemi": "anterior STEMI",
    "lateral stemi": "lateral STEMI",
    "primary pci": "primary PCI for STEMI",
    "dapt post stent": "dual antiplatelet therapy after coronary stenting",
    "ecg primary signal": "the surface ECG",
    "aspirin acs mechanism": "aspirin in acute coronary syndrome",
}


def clean(s: str) -> str:
    s = re.sub(r"\s+", " ", (s or "").strip())
    return s.strip(" :,-")


def phrase_topic(topic: str) -> str:
    raw = clean(topic)
    key = raw.lower()
    if key in TOPIC_FIXES:
        return TOPIC_FIXES[key]
    t = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", raw).replace("_", " ")
    t = re.sub(r"\bdef\b", "", t, flags=re.I)
    t = re.sub(r"\bmech(anism)?\b", "", t, flags=re.I)
    t = re.sub(r"\bsigns?\b", "", t, flags=re.I)
    t = re.sub(r"\bSL\b", "sublingual", t)
    t = re.sub(r"\s+", " ", t).strip(" -")
    if t and not t.isupper():
        t = t[0].lower() + t[1:]
    return t or raw.lower()


def _tokens(s: str) -> set[str]:
    stop = {
        "the", "and", "with", "from", "for", "that", "this", "into", "only",
        "most", "more", "than", "when", "after", "before", "over", "under",
        "a", "an", "of", "in", "to", "on", "or", "as", "by", "is", "are",
        "be", "not", "no", "all", "any", "may", "can", "if",
    }
    return {w for w in re.findall(r"[a-z0-9]+", (s or "").lower()) if len(w) > 2 and w not in stop}


def letters_options(texts: list[str]) -> tuple[list[str], dict[str, str]]:
    opts, mapping = [], {}
    for i, t in enumerate(texts):
        L = "ABCD"[i]
        opts.append(f"{L}) {t}")
        mapping[L] = t
    return opts, mapping


def pick_related(topics: list[dict], idx: int, rng: random.Random, k: int = 8) -> list[dict]:
    base = topics[idx]
    base_tok = _tokens(" ".join([base["topic"], base["correct"], base["near"], base.get("mechanism", "")]))
    scored = []
    for j, t in enumerate(topics):
        if j == idx:
            continue
        tok = _tokens(" ".join([t["topic"], t["correct"], t["near"]]))
        overlap = len(base_tok & tok)
        adj = 1.0 if min(abs(j - idx), len(topics) - abs(j - idx)) <= 4 else 0.0
        scored.append((overlap * 3.0 + adj + rng.random() * 0.15, t))
    scored.sort(key=lambda x: x[0], reverse=True)
    out, seen = [], set()
    for score, t in scored:
        if t["topic"] in seen:
            continue
        if score < 1.0 and len(out) >= 3:
            continue
        seen.add(t["topic"])
        out.append(t)
        if len(out) >= k:
            break
    return out


def build_options(topic: dict, related: list[dict], rng: random.Random):
    correct = clean(topic["correct"])
    near = clean(topic["near"])
    base_tok = _tokens(" ".join([topic["topic"], correct, near, topic.get("mechanism", "")]))
    pool = [near]
    for r in related:
        pool.append(clean(r["near"]))
    for r in related:
        pool.append(clean(r["correct"]))
    uniq, seen = [], {correct.lower()}

    def accept(p: str, need_overlap: bool) -> bool:
        if not p or p.lower() in seen:
            return False
        if RULEOUTISH.search(p):
            return False
        if need_overlap and base_tok and not (_tokens(p) & base_tok):
            return False
        return True

    for need in (True, False):
        for p in pool:
            if accept(p, need):
                seen.add(p.lower())
                uniq.append(p)
            if len(uniq) >= 3:
                break
        if len(uniq) >= 3:
            break
    while len(uniq) < 3:
        for p in pool:
            if p and p.lower() not in seen:
                uniq.append(p)
                seen.add(p.lower())
            if len(uniq) >= 3:
                break
        else:
            uniq.append(clean(related[len(uniq) % len(related)]["near"]) if related else near)
            break
    texts = [correct] + uniq[:3]
    rng.shuffle(texts)
    opts, mapping = letters_options(texts)
    answer = next(o for o in opts if o.split(") ", 1)[1] == correct)
    return correct, opts, mapping, answer


def _demo(age: int, sex: str) -> str:
    return f"A {age}-year-old {sex}"


def stem_easy(topic: dict, n: int, rng: random.Random) -> str:
    label = phrase_topic(topic["topic"])
    templates = [
        f"Which of the following best characterizes {label}?",
        f"Which finding is most consistent with {label}?",
        f"Which of the following statements about {label} is most accurate?",
        f"In patients with {label}, which of the following is most correct?",
        f"Which of the following is the hallmark feature of {label}?",
        f"Which description most accurately matches {label}?",
        f"Regarding {label}, which of the following is most accurate?",
        f"Which of the following mechanisms best explains {label}?",
    ]
    return templates[n % len(templates)]


def stem_medium(topic: dict, n: int, rng: random.Random, field: str) -> str:
    label = phrase_topic(topic["topic"])
    mech = clean(topic.get("mechanism", ""))
    age = 24 + (n * 7 + len(label) * 3) % 52
    sex = "woman" if (n + len(label)) % 2 == 0 else "man"
    who = _demo(age, sex)

    if field == "pharmacy":
        templates = [
            f"{who} is started on therapy relevant to {label}. Which of the following is the most accurate statement?",
            f"{who} with multiple medications is evaluated for an issue involving {label}. Which of the following is most appropriate?",
            f"A pharmacist reviews a regimen concerning {label}. Which of the following is most accurate?",
            f"{who} develops a clinical problem related to {label}. Which of the following best explains the findings?",
            f"{who} presents to clinic with a medication-related question about {label}. Which of the following is most correct?",
            f"During medication reconciliation, a concern about {label} is raised. Which of the following is most accurate?",
            f"{who} requires counseling about {label}. Which of the following statements is most appropriate?",
            f"{who} has laboratory changes attributed to {label}. Which of the following is most likely?",
        ]
    elif field == "mls":
        templates = [
            f"{who} has laboratory findings evaluated in the context of {label}. Which of the following is most accurate?",
            f"A laboratory workup for {label} is reviewed. Which of the following interpretations is most correct?",
            f"{who} undergoes testing relevant to {label}. Which of the following results is most consistent with the diagnosis?",
            f"Quality and method considerations for {label} are discussed. Which of the following is most accurate?",
            f"{who} has an abnormal panel suggesting {label}. Which of the following is the most likely explanation?",
            f"A technologist reviews results related to {label}. Which of the following is most appropriate?",
            f"{who} is being evaluated for {label}. Which of the following laboratory conclusions is most correct?",
            f"In the laboratory assessment of {label}, which of the following is most accurate?",
        ]
    elif field == "nursing":
        templates = [
            f"{who} is admitted with a condition involving {label}. Which of the following nursing actions is most appropriate?",
            f"{who} develops findings consistent with {label}. Which of the following is the priority assessment focus?",
            f"On the ward, a patient shows features of {label}. Which of the following is most accurate?",
            f"{who} requires care planning for {label}. Which of the following is most appropriate?",
            f"A nurse reviews a case centered on {label}. Which of the following is most correct?",
            f"{who} has vital-sign changes related to {label}. Which of the following is most likely?",
            f"During bedside evaluation for {label}, which of the following is most accurate?",
            f"{who} is monitored for complications of {label}. Which of the following is most appropriate?",
        ]
    elif field == "dentistry":
        templates = [
            f"{who} presents for dental evaluation with findings consistent with {label}. Which of the following is most likely?",
            f"{who} reports tooth-related symptoms. Examination suggests {label}. Which of the following is most accurate?",
            f"A dental examination raises concern for {label}. Which of the following is the most appropriate interpretation?",
            f"{who} is seen for pain and a lesion pattern associated with {label}. Which of the following is most likely?",
            f"Radiographs and clinical findings point toward {label}. Which of the following is most correct?",
            f"{who} undergoes endodontic/periodontal assessment for possible {label}. Which of the following is most accurate?",
            f"In clinic, a case of suspected {label} is reviewed. Which of the following is most likely?",
            f"{who} has oral findings related to {label}. Which of the following best fits the presentation?",
        ]
    else:  # medicine
        templates = [
            f"{who} presents with a history and examination consistent with {label}. Which of the following is most likely?",
            f"{who} is evaluated in clinic for symptoms pointing to {label}. Which of the following is the most accurate conclusion?",
            f"{who} with relevant risk factors develops a presentation of {label}. Which of the following is most likely?",
            f"{who} is admitted for workup of {label}. Which of the following statements is most accurate?",
            f"On examination and initial testing, findings support {label}. Which of the following is most correct?",
            f"{who} reports progressive symptoms. The constellation is classic for {label}. Which of the following is most likely?",
            f"{who} is seen in the emergency department with features of {label}. Which of the following is most accurate?",
            f"A clinical scenario centers on {label}. {mech} Which of the following is most likely?",
        ]
    stem = templates[n % len(templates)]
    # Avoid dumping raw mechanism if it makes stem too long/awkward
    if mech and mech.lower() in stem.lower() and len(stem) > 320:
        stem = templates[n % (len(templates) - 1)]
    return stem


def stem_hard(topic: dict, n: int, rng: random.Random, field: str) -> str:
    label = phrase_topic(topic["topic"])
    age = 35 + (n * 5 + len(label)) % 40
    sex = "woman" if (n + len(label)) % 2 else "man"
    who = _demo(age, sex)
    templates = [
        f"{who} presents with findings that could fit more than one process often confused with {label}. "
        f"Based on history, examination, and initial tests, which of the following is most likely?",
        f"{who} is hospitalized with evolving features of {label}. A common mimic remains possible. "
        f"Which of the following is most likely?",
        f"{who} with several comorbidities is evaluated for {label}. "
        f"Which of the following is favored after comparison with frequent look-alikes?",
        f"{who} is evaluated for suspected {label}. Initial findings do not yet separate common look-alikes. "
        f"Which of the following is most likely?",
        f"Findings thought to represent {label} can be misread. Which of the following is most correct?",
        f"{who} presents with {label}. Distinguishing this from frequent textbook mimics is required. "
        f"Which of the following is most likely?",
        f"A complex case of {label} is reviewed on rounds. Which of the following is most accurate?",
        f"{who} has progressive abnormalities attributed to {label}. "
        f"Which of the following is most consistent with the clinical process?",
    ]
    return templates[n % len(templates)]


def stem_extreme(topic: dict, n: int, rng: random.Random, field: str) -> str:
    label = phrase_topic(topic["topic"])
    age = 48 + (n * 3 + len(label)) % 30
    sex = "woman" if (n + len(label)) % 2 == 0 else "man"
    who = _demo(age, sex)
    templates = [
        f"{who} with diabetes, hypertension, and chronic kidney disease develops rapidly worsening features of {label}. "
        f"Vital signs are unstable. Which of the following is most likely?",
        f"In the emergency department, {who.lower()} is critically ill with a syndrome centered on {label}. "
        f"Which of the following is most likely?",
        f"{who} deteriorates overnight with {label}. Timing, risk factors, and early diagnostics favor one process. "
        f"Which of the following is most likely?",
        f"{who} develops life-threatening complications in the setting of {label}. "
        f"Which of the following is most consistent with the clinical process?",
        f"A rapidly progressive presentation of {label} is reviewed. "
        f"Which of the following is most likely?",
        f"{who} requires urgent decision-making for {label}. Incorrect attribution would change management substantially. "
        f"Which of the following is most likely?",
        f"{who} has refractory abnormalities due to {label}. Which of the following is the most accurate interpretation?",
        f"A critical-care presentation involving {label} is discussed. Which of the following is most likely?",
    ]
    return templates[n % len(templates)]


def explanations(topic: dict, correct: str, mapping: dict[str, str], answer_letter: str):
    mech = clean(topic.get("mechanism", ""))
    why_near = clean(topic.get("why_near", ""))
    near = clean(topic["near"])
    overall = (
        f"{mech} Therefore, the most accurate choice is: {correct}. "
        f"{why_near or 'Alternative choices share overlapping features but fit the presentation less well.'}"
    ).strip()
    ce = {}
    for L, text in mapping.items():
        if L == answer_letter:
            ce[L] = f"{mech} This matches the correct interpretation.".strip()
            if len(ce[L]) < 40:
                ce[L] += f" It correctly identifies: {correct}."
        elif text.lower() == near.lower():
            ce[L] = (
                f"{why_near or 'This is a frequent clinical look-alike.'} "
                "It is less consistent than the correct choice."
            ).strip()
        else:
            ce[L] = (
                "This alternative can appear on a thoughtful differential, "
                "but the discriminating findings align more closely with the correct choice."
            )
        if len(ce[L]) < 40:
            ce[L] += " Compare mechanism and clinical pattern carefully."
    return overall, ce


def build_specialty(field: str, specialty: str, topics: list[dict], out_path: Path) -> None:
    rng = random.Random(f"{SEED}:{field}:{specialty}")
    bank = {d: [] for d in DIFFICULTIES}
    used: set[str] = set()
    letter_counts = {L: 0 for L in "ABCD"}

    stem_fns = {
        "easy": lambda t, i: stem_easy(t, i, rng),
        "medium": lambda t, i: stem_medium(t, i, rng, field),
        "hard": lambda t, i: stem_hard(t, i, rng, field),
        "extreme": lambda t, i: stem_extreme(t, i, rng, field),
    }

    for difficulty in DIFFICULTIES:
        i = 0
        guard = 0
        while len(bank[difficulty]) < PER_DIFF and guard < PER_DIFF * 80:
            guard += 1
            idx = i % len(topics)
            topic = topics[idx]
            stem = clean(stem_fns[difficulty](topic, i))
            if not stem or BANNED.search(stem) or stem.lower() in used:
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
            qid = f"{specialty}:{difficulty}:{len(bank[difficulty])}"
            bank[difficulty].append(
                {
                    "id": qid,
                    "question": stem,
                    "options": opts,
                    "answer": answer,
                    "explanation": overall,
                    "choice_explanations": ce,
                }
            )
            used.add(stem.lower())
            letter_counts[answer_letter] += 1
            i += 1
        if len(bank[difficulty]) < PER_DIFF:
            raise RuntimeError(f"{field}/{specialty}/{difficulty}: {len(bank[difficulty])}")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(bank, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {out_path.relative_to(ROOT)} (120)")


def main() -> None:
    for field, specialties in CATALOGS.items():
        base = ROOT if field == "medicine" else ROOT / field
        for specialty, topics in specialties.items():
            if len(topics) < 30:
                raise RuntimeError(f"{field}/{specialty} catalog too small")
            build_specialty(field, specialty, topics, base / "question_banks" / f"{specialty}.json")
    print("Done.")


if __name__ == "__main__":
    main()
