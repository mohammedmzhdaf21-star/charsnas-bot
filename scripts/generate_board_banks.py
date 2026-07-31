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
    r"history suggestive of|constellation is classic|relevant risk factors develops|"
    r"common mimic|alternatives|textbook mimics|Initial findings do not yet separate|"
    r"Incorrect attribution|syndrome centered on|rapidly progressive presentation|"
    r"rapidly worsening features of|critical-care presentation|refractory abnormalities|"
    r"progressive abnormalities attributed|clinical scenario centers|pediatric scenario|"
    r"therapy relevant to|medication-related question|case centered on|"
    r"condition involving|lesion pattern associated|best fits the presentation|"
    r"hallmark feature of|description most accurately matches|"
    r"findings consistent with|points toward .{0,40}\. Which|"
    r"Vital signs are unstable\. Which|life-threatening complications in the setting|"
    r"Timing, risk factors, and early diagnostics favor|"
    r"favored after comparison|Distinguishing this from frequent|"
    r"true driver|dominant pathophysiology|several closely related explanations|"
    r"On the ward,|A nurse reviews|A pharmacist reviews a regimen concerning|"
    r"Quality and method considerations for|laboratory conclusions is most correct",
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
    "aspirin acs mechanism": "aspirin in ACS",
    "copd definition": "COPD",
    "copd exacerbation": "COPD exacerbation",
    "asthma reversible obstruction": "asthma",
    "asthma exacerbation treatment": "acute asthma exacerbation",
    "emphysema path": "emphysema",
    "chronic bronchitis clinical": "chronic bronchitis",
    "community pneumonia": "community-acquired pneumonia",
    "ipf pattern": "idiopathic pulmonary fibrosis",
    "cf lung": "cystic fibrosis lung disease",
}


def clean(s: str) -> str:
    s = re.sub(r"\s+", " ", (s or "").strip())
    return s.strip(" :,-")


def phrase_topic(topic: str) -> str:
    raw = clean(topic)
    key = raw.lower().strip()
    if key in TOPIC_FIXES:
        return TOPIC_FIXES[key]
    t = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", raw).replace("_", " ")
    t = re.sub(
        r"\b(def|definition|mech|mechanism|signs?|path|clinical|pattern|rx|dx)\b",
        "",
        t,
        flags=re.I,
    )
    t = re.sub(r"\bSL\b", "sublingual", t)
    t = re.sub(r"\bc\s*opd\b", "COPD", t, flags=re.I)
    t = re.sub(r"\bcopd\b", "COPD", t, flags=re.I)
    t = re.sub(r"\bacs\b", "ACS", t, flags=re.I)
    t = re.sub(r"\bnstemi\b", "NSTEMI", t, flags=re.I)
    t = re.sub(r"\bstemi\b", "STEMI", t, flags=re.I)
    t = re.sub(r"\bhfref\b", "HFrEF", t, flags=re.I)
    t = re.sub(r"\bhocm\b", "HOCM", t, flags=re.I)
    t = re.sub(r"\s+", " ", t).strip(" -")
    if t and not t.isupper() and not re.match(r"^[A-Z]{2,}\b", t):
        t = t[0].lower() + t[1:]
    return t or raw.lower()


def condition_name(topic: str) -> str:
    label = phrase_topic(topic)
    label = re.sub(r"\binterpretation\b", "", label, flags=re.I)
    label = re.sub(r"\s+", " ", label).strip(" -")
    return label or phrase_topic(topic)

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


def _blob(topic: dict) -> str:
    return " ".join(
        [
            str(topic.get("topic", "")),
            str(topic.get("correct", "")),
            str(topic.get("near", "")),
            str(topic.get("mechanism", "")),
        ]
    ).lower()


def _has_kw(blob: str, keywords: tuple[str, ...]) -> bool:
    """Match keywords with word-boundary awareness for short tokens."""
    for k in keywords:
        k = k.strip().lower()
        if not k:
            continue
        if len(k) <= 4 or k.endswith(" "):
            if re.search(rf"\b{re.escape(k.strip())}\b", blob):
                return True
        else:
            if k in blob:
                return True
    return False


def patient_demo(
    field: str,
    specialty: str,
    topic: dict,
    n: int,
    difficulty: str,
) -> dict:
    """Return clinically plausible age/sex phrasing for this specialty + topic."""
    label = phrase_topic(topic["topic"])
    blob = _blob(topic) + " " + specialty.lower() + " " + label.lower()
    seed = n + len(label) * 3 + hash(specialty) % 97

    def pick(lo: int, hi: int) -> int:
        if hi < lo:
            lo, hi = hi, lo
        return lo + (seed * 7) % (hi - lo + 1)

    def sex_alt(default_female: bool = False) -> str:
        if default_female:
            return "woman"
        return "woman" if seed % 2 == 0 else "man"

    pregnancy_kw = (
        "pregnan", "abortion", "abort ", "ectopic", "previa", "abruption", "preeclamp", "eclamp",
        "intrapartum", "postpartum", "placenta", "molar pregnancy", "hydatidiform",
        "gestational", "obstetric", "vbac", "tocodynam", "neonatal resuscitation",
        "tocolysis", "oxytocin", "hellp", "shoulder dystocia", "lochia", "breastfeed",
        "mastitis", "endometritis", "chorioamnionitis", "gdm", "rhogam", "prenatal",
        "antepartum", "bishop score", "cesarean", "forceps delivery", "vacuum extraction",
        "pprom", "oligohydramnios", "polyhydramnios", "iugr", "stillbirth",
        "hyperemesis", "puppp", "vasa previa", "incomplete abortion", "inevitable abortion",
        "septic abortion", "choriocarcinoma", "quickening",
    )
    pediatric_kw = (
        "neonat", "newborn", "infant", "toddler", "milestones", "apgar", "bronchiolitis",
        "croup", "intussusception", "pyloric", "kawasaki", "congenital", "nicu",
        "fontanelle", "failure to thrive", "febrile seizure", "epiglottitis",
        "primary tooth", "early childhood caries", "eruption primary",
        "fluoride varnish", "pediatric", "pulpotomy primary", "space maintainer",
        "tell-show-do", "frankl", "knee-to-knee",
    )
    male_gu_kw = (
        "bph", "benign prostatic", "prostate", "prostatitis", "testicular",
        "varicocele", "hydrocele", "phimosis", "priapism", "epididym",
        "erectile", "turp",
    )
    menopause_kw = (
        "menopause", "postmenopausal", "endometrial cancer", "atrophic vaginitis",
        "hot flush", "hot flash",
    )
    young_cardiac_kw = ("hocm", "hypertrophic obstructive", "wpw", "marfan", "athlete syncope")
    elderly_kw = (
        "geriatr", "delirium", "fall multifactorial", "prescribing cascade",
        "polypharmacy", "frailty", "beers", "pressure injur", "skin tear",
    )

    is_preg = _has_kw(blob, pregnancy_kw)
    is_ped_topic = _has_kw(blob, pediatric_kw)
    is_male_gu = _has_kw(blob, male_gu_kw)
    is_meno = _has_kw(blob, menopause_kw)
    is_young_card = _has_kw(blob, young_cardiac_kw)
    is_geri = specialty == "geriatrics" or _has_kw(blob, elderly_kw)

    # 1) Specialty-first rules (prevent keyword collisions)
    if specialty in {"obgyn", "maternity"}:
        if is_meno:
            age = pick(50, 68)
            comorbidities = ""
        else:
            age = pick(19, 39) if difficulty != "extreme" else pick(22, 38)
            comorbidities = (
                "with gestational diabetes and chronic hypertension"
                if difficulty == "extreme"
                else ""
            )
        return {
            "who": _demo(age, "woman"),
            "age": age,
            "sex": "woman",
            "comorbidities": comorbidities,
            "is_child": False,
        }

    if specialty in {"pediatrics", "pediatric_dentistry"} or (
        field == "nursing" and specialty == "pediatrics"
    ):
        if any(k in blob for k in ("neonat", "newborn", "apgar", "rds", "ttn", "meconium")):
            days = 1 + (seed % 14)
            who = f"A {days}-day-old newborn"
            age = 0
        elif any(k in blob for k in ("infant", "bronchiolitis", "pyloric", "6mo", "12mo", "knee-to-knee")):
            months = 2 + (seed % 16)
            who = f"A {months}-month-old infant"
            age = 0
        elif any(k in blob for k in ("toddler", "croup", "2yr", "3yr")):
            age = pick(1, 4)
            who = f"A {age}-year-old toddler"
        elif specialty == "pediatric_dentistry":
            age = pick(3, 12)
            who = f"A {age}-year-old child"
        else:
            age = pick(2, 15)
            who = f"A {age}-year-old child"
        return {
            "who": who,
            "age": age,
            "sex": "child",
            "comorbidities": "",
            "is_child": True,
        }

    if specialty == "geriatrics" or (is_geri and specialty not in {"pediatrics", "obgyn", "maternity"}):
        age = pick(68, 88)
        sex = sex_alt()
        comorbidities = (
            "with frailty, polypharmacy, and prior falls"
            if difficulty == "extreme"
            else "with multiple chronic conditions"
        )
        return {
            "who": _demo(age, sex),
            "age": age,
            "sex": sex,
            "comorbidities": comorbidities,
            "is_child": False,
        }

    # 2) Topic keyword rules for other specialties
    if is_preg and specialty not in {"urology", "cardiology"}:
        age = pick(19, 39)
        return {
            "who": _demo(age, "woman"),
            "age": age,
            "sex": "woman",
            "comorbidities": "",
            "is_child": False,
        }

    if is_ped_topic:
        age = pick(2, 14)
        return {
            "who": f"A {age}-year-old child",
            "age": age,
            "sex": "child",
            "comorbidities": "",
            "is_child": True,
        }

    if is_male_gu or (specialty == "urology" and any(k in blob for k in ("prostate", "bph", "psa", "turp"))):
        if any(k in blob for k in ("testicular", "varicocele", "torsion")):
            age = pick(16, 35)
        else:
            age = pick(55, 78)
        return {
            "who": _demo(age, "man"),
            "age": age,
            "sex": "man",
            "comorbidities": "with hypertension and type 2 diabetes" if difficulty == "extreme" else "",
            "is_child": False,
        }

    if specialty == "cardiology":
        if is_young_card:
            age = pick(16, 34)
            sex = sex_alt()
            comorbidities = ""
        elif any(k in blob for k in ("stemi", "nstemi", "acs", "cabg", "hfref", "aortic stenosis")):
            age = pick(52, 78)
            sex = sex_alt()
            comorbidities = (
                "with diabetes, hypertension, and chronic kidney disease"
                if difficulty == "extreme"
                else "with hypertension"
            )
        else:
            age = pick(40, 72)
            sex = sex_alt()
            comorbidities = "with hypertension" if difficulty == "extreme" else ""
        return {
            "who": _demo(age, sex),
            "age": age,
            "sex": sex,
            "comorbidities": comorbidities,
            "is_child": False,
        }

    if specialty == "orthopedics":
        if any(k in blob for k in ("scoliosis", "slipped capital", "osgood", "developmental dysplasia", "salter")):
            age = pick(8, 16)
            return {
                "who": f"A {age}-year-old adolescent",
                "age": age,
                "sex": "adolescent",
                "comorbidities": "",
                "is_child": True,
            }
        if any(k in blob for k in ("osteopor", "fragility", "hip fracture", "colles")):
            age = pick(65, 85)
            sex = "woman" if seed % 3 != 0 else "man"
            return {
                "who": _demo(age, sex),
                "age": age,
                "sex": sex,
                "comorbidities": "with osteoporosis",
                "is_child": False,
            }
        age = pick(22, 60)
        sex = sex_alt()
        return {"who": _demo(age, sex), "age": age, "sex": sex, "comorbidities": "", "is_child": False}

    if specialty == "ophthalmology":
        if any(k in blob for k in ("retinopathy of prematurity", "amblyopia", "congenital cataract")):
            age = pick(1, 8)
            return {
                "who": f"A {age}-year-old child",
                "age": age,
                "sex": "child",
                "comorbidities": "",
                "is_child": True,
            }
        if any(k in blob for k in ("amd", "macular degeneration", "cataract", "glaucoma")):
            age = pick(60, 82)
        else:
            age = pick(25, 70)
        sex = sex_alt()
        return {"who": _demo(age, sex), "age": age, "sex": sex, "comorbidities": "", "is_child": False}

    if specialty == "dermatology":
        if "acne" in blob:
            age = pick(14, 24)
        elif any(k in blob for k in ("varicella", "measles", "roseola", "impetigo", "fifth disease")):
            age = pick(1, 12)
            return {
                "who": f"A {age}-year-old child",
                "age": age,
                "sex": "child",
                "comorbidities": "",
                "is_child": True,
            }
        elif any(k in blob for k in ("bullous pemphigoid", "actinic", "basal cell", "squamous cell")):
            age = pick(58, 80)
        else:
            age = pick(18, 65)
        sex = sex_alt()
        return {"who": _demo(age, sex), "age": age, "sex": sex, "comorbidities": "", "is_child": False}

    if specialty == "neurology":
        if any(k in blob for k in ("febrile seizure", "duchenne", "breath holding")):
            age = pick(1, 10)
            return {
                "who": f"A {age}-year-old child",
                "age": age,
                "sex": "child",
                "comorbidities": "",
                "is_child": True,
            }
        if any(k in blob for k in ("alzheimer", "parkinson", "lewy", "normal pressure")):
            age = pick(62, 84)
        elif any(k in blob for k in ("migraine", "multiple sclerosis", "myasthenia")):
            age = pick(22, 45)
        elif "stroke" in blob:
            age = pick(58, 82)
        else:
            age = pick(30, 75)
        sex = sex_alt(default_female=("migraine" in blob or "multiple sclerosis" in blob))
        comorbidities = "with atrial fibrillation and hypertension" if "stroke" in blob else ""
        return {
            "who": _demo(age, sex),
            "age": age,
            "sex": sex,
            "comorbidities": comorbidities,
            "is_child": False,
        }

    if specialty in {"pulmonology", "gastroenterology", "endocrinology", "nephrology"}:
        if specialty == "pulmonology" and any(k in blob for k in ("cystic fibrosis", "bronchiolitis")):
            if "bronchiolitis" in blob:
                return {
                    "who": "A 8-month-old infant",
                    "age": 0,
                    "sex": "child",
                    "comorbidities": "",
                    "is_child": True,
                }
            age = pick(8, 22)
        elif specialty == "endocrinology" and any(k in blob for k in ("type 1", "dka", "precocious")):
            age = pick(8, 24)
        elif specialty == "nephrology" and "psgn" in blob:
            age = pick(5, 12)
            return {
                "who": f"A {age}-year-old child",
                "age": age,
                "sex": "child",
                "comorbidities": "",
                "is_child": True,
            }
        else:
            age = pick(28, 72)
        sex = sex_alt()
        comorbidities = ""
        if difficulty == "extreme" and age >= 40:
            comorbidities = "with diabetes, hypertension, and chronic kidney disease"
        return {
            "who": _demo(age, sex),
            "age": age,
            "sex": sex,
            "comorbidities": comorbidities,
            "is_child": False,
        }

    if field == "dentistry":
        if specialty == "oral_surgery" and any(k in blob for k in ("third molar", "wisdom", "impacted")):
            age = pick(17, 28)
        elif specialty in {"periodontics", "prosthodontics"}:
            age = pick(40, 75)
        else:
            age = pick(20, 65)
        sex = sex_alt()
        return {
            "who": _demo(age, sex),
            "age": age,
            "sex": sex,
            "comorbidities": "with poorly controlled diabetes"
            if specialty == "periodontics" and difficulty == "extreme"
            else "",
            "is_child": False,
        }

    if field == "pharmacy":
        if any(k in blob for k in ("pediatric", "otitis media", "amoxicillin child")):
            age = pick(2, 10)
            return {
                "who": f"A {age}-year-old child",
                "age": age,
                "sex": "child",
                "comorbidities": "",
                "is_child": True,
            }
        if any(k in blob for k in ("geriatr", "beers", "elder")):
            age = pick(70, 88)
        else:
            age = pick(30, 70)
        sex = sex_alt()
        return {
            "who": _demo(age, sex),
            "age": age,
            "sex": sex,
            "comorbidities": "with reduced renal function" if difficulty == "extreme" and age >= 50 else "",
            "is_child": False,
        }

    # Generic adult
    age = pick(25, 70)
    sex = sex_alt()
    comorbidities = "with diabetes and hypertension" if difficulty == "extreme" and age >= 50 else ""
    return {
        "who": _demo(age, sex),
        "age": age,
        "sex": sex,
        "comorbidities": comorbidities,
        "is_child": False,
    }


def _with_comorbidities(who: str, comorbidities: str) -> str:
    if not comorbidities:
        return who
    # "A 60-year-old woman" + "with diabetes..." -> "A 60-year-old woman with diabetes..."
    return f"{who} {comorbidities}"



def topic_kind(topic: dict) -> str:
    blob = _blob(topic)
    if any(
        k in blob
        for k in (
            "efficacy", "potency", "agonist", "antagonist", "receptor", "pharmacokin",
            "half-life", "bioavailability", "first pass", "volume of distribution",
            "clearance", "therapeutic index", "partial agonist", "competitive",
        )
    ):
        return "concept"
    if any(
        k in blob
        for k in (
            "testing", "interpretation", "murmur", "ecg", "signal", "definition",
            "lead", "auscult", "radiograph", "assay", "method", "quality",
            "cold testing", "percussion", "primary signal",
        )
    ):
        return "finding"
    if any(
        k in blob
        for k in (
            "treatment", "therapy", "dose", "management", "pci", "dapt", "anticoagul",
            "rate control", "counseling", "vaccine", "rhogam", "varnish", "sealant",
        )
    ):
        return "management"
    return "disease"


def stem_easy(topic: dict, n: int, rng: random.Random) -> str:
    label = condition_name(topic["topic"])
    kind = topic_kind(topic)
    if kind == "concept":
        templates = [
            f"Which of the following best defines {label}?",
            f"Which statement about {label} is correct?",
            f"In basic pharmacology, which of the following is true of {label}?",
            f"Which of the following correctly describes {label}?",
            f"Select the correct statement regarding {label}.",
            f"Which of the following applies to {label}?",
            f"Which explanation of {label} is correct?",
            f"Which of the following is true for {label}?",
        ]
    elif kind == "finding":
        templates = [
            f"Which of the following is true about {label}?",
            f"Which finding matches {label}?",
            f"Which statement regarding {label} is correct?",
            f"In clinical examination related to {label}, which of the following is correct?",
            f"Which of the following best describes {label}?",
            f"Select the correct interpretation for {label}.",
            f"Which of the following applies to {label}?",
            f"Which statement about {label} is accurate?",
        ]
    else:
        templates = [
            f"Which of the following is true of {label}?",
            f"Which finding is expected in {label}?",
            f"Which of the following statements about {label} is correct?",
            f"In {label}, which of the following is correct?",
            f"Which of the following best describes {label}?",
            f"Select the correct statement about {label}.",
            f"Which mechanism accounts for {label}?",
            f"Which of the following applies to {label}?",
        ]
    return templates[n % len(templates)]


def stem_medium(topic: dict, n: int, rng: random.Random, field: str, specialty: str) -> str:
    label = condition_name(topic["topic"])
    kind = topic_kind(topic)
    demo = patient_demo(field, specialty, topic, n, "medium")
    who = demo["who"]

    if kind == "concept":
        templates = [
            f"Which of the following correctly describes {label} in clinical use?",
            f"During a pharmacology discussion of {label}, which statement is correct?",
            f"Which of the following correctly describes {label}?",
            f"In comparing drug properties, which statement about {label} is correct?",
            f"Regarding {label}, which of the following is correct?",
            f"Which explanation of {label} is most accurate?",
            f"Which of the following applies to {label} in standard therapeutics?",
            f"Which statement best defines {label}?",
        ]
        return templates[n % len(templates)]

    if kind == "finding":
        templates = [
            f"{who} is examined, and {label} is reviewed. Which of the following is correct?",
            f"While evaluating {who.lower()}, attention turns to {label}. Which of the following is most accurate?",
            f"{who} has findings requiring interpretation of {label}. Which of the following is correct?",
            f"In {who.lower()}, which statement about {label} is correct?",
            f"Clinical testing related to {label} is performed. Which of the following is correct?",
            f"{who} undergoes assessment involving {label}. Which of the following is most accurate?",
            f"Exam findings raise a question about {label}. Which of the following is correct?",
            f"Which interpretation of {label} is correct?",
        ]
        return templates[n % len(templates)]

    if demo["is_child"]:
        templates = [
            f"{who} is brought to clinic because of concerns related to {label}. Which of the following is correct?",
            f"{who} is evaluated for possible {label}. Which of the following is most accurate?",
            f"{who} presents with signs of {label}. Which of the following is correct?",
            f"{who} is admitted with suspected {label}. Which of the following statements is correct?",
            f"During evaluation of {who.lower()}, {label} is considered. Which of the following is most accurate?",
            f"{who} has findings that raise concern for {label}. Which of the following is correct?",
            f"{who} arrives in the emergency department with features of {label}. Which of the following is most accurate?",
            f"In {who.lower()}, which statement about {label} is correct?",
        ]
        return templates[n % len(templates)]

    if field == "pharmacy":
        templates = [
            f"{who} is started on treatment related to {label}. Which of the following is correct?",
            f"{who} takes several medicines and is assessed regarding {label}. Which of the following is most appropriate?",
            f"Medication review raises a question about {label}. Which of the following is correct?",
            f"{who} develops an adverse effect related to {label}. Which of the following best explains it?",
            f"{who} needs counseling about {label}. Which of the following is most appropriate?",
            f"During medication reconciliation, {label} is discussed. Which of the following is correct?",
            f"{who} needs dose adjustment related to {label}. Which of the following is most accurate?",
            f"{who} has lab changes linked to {label}. Which of the following is correct?",
        ]
    elif field == "mls":
        templates = [
            f"{who} has lab results reviewed for {label}. Which of the following is correct?",
            f"A specimen workup for {label} is interpreted. Which of the following is most accurate?",
            f"{who} undergoes testing for {label}. Which result pattern is most consistent?",
            f"Method selection for {label} is discussed. Which of the following is correct?",
            f"{who} has an abnormal panel. Which statement about {label} is most accurate?",
            f"Results related to {label} are verified before release. Which of the following is appropriate?",
            f"{who} is evaluated with assays used in {label}. Which of the following is correct?",
            f"In laboratory assessment of {label}, which of the following is correct?",
        ]
    elif field == "nursing":
        templates = [
            f"{who} is admitted with {label}. Which nursing action is most appropriate?",
            f"{who} develops findings of {label}. What is the priority assessment?",
            f"{who} shows signs of {label} on the unit. Which of the following is correct?",
            f"{who} needs a care plan for {label}. Which of the following is most appropriate?",
            f"Bedside assessment suggests {label}. Which of the following is correct?",
            f"{who} has vital-sign changes due to {label}. Which of the following is most accurate?",
            f"While caring for {who.lower()}, {label} is suspected. Which of the following is correct?",
            f"{who} is monitored for complications of {label}. Which of the following is most appropriate?",
        ]
    elif field == "dentistry":
        templates = [
            f"{who} presents for dental care with findings of {label}. Which of the following is correct?",
            f"{who} reports dental pain. Exam suggests {label}. Which of the following is most accurate?",
            f"Clinical and radiographic findings suggest {label}. Which interpretation is correct?",
            f"{who} is examined for {label}. Which of the following is most likely?",
            f"A dental exam raises concern for {label}. Which of the following is correct?",
            f"{who} is assessed for {label}. Which of the following is most accurate?",
            f"In the dental clinic, {label} is suspected. Which of the following is correct?",
            f"{who} has oral findings of {label}. Which of the following is most accurate?",
        ]
    else:
        templates = [
            f"{who} presents with a clinical picture of {label}. Which of the following is most accurate?",
            f"{who} is seen in clinic for suspected {label}. Which of the following is correct?",
            f"{who} develops symptoms of {label}. Which of the following is most accurate?",
            f"{who} is admitted with suspected {label}. Which statement is correct?",
            f"{who} has examination findings of {label}. Which of the following is most accurate?",
            f"{who} reports symptoms typical of {label}. Which of the following is correct?",
            f"{who} is evaluated in the emergency department for {label}. Which of the following is most accurate?",
            f"{who} is assessed for {label}. Which of the following statements is correct?",
        ]
    return templates[n % len(templates)]


def stem_hard(topic: dict, n: int, rng: random.Random, field: str, specialty: str) -> str:
    label = condition_name(topic["topic"])
    kind = topic_kind(topic)
    demo = patient_demo(field, specialty, topic, n, "hard")
    who = (
        _with_comorbidities(demo["who"], demo["comorbidities"])
        if demo["comorbidities"] and not demo["is_child"]
        else demo["who"]
    )
    if kind in {"concept", "finding", "management"}:
        templates = [
            f"Careful review of {label} is required. Which of the following is most accurate?",
            f"Two similar explanations for {label} are compared. Which of the following is correct?",
            f"In a detailed discussion of {label}, which of the following is most accurate?",
            f"Which of the following correctly distinguishes key points about {label}?",
            f"Careful interpretation of {label} is required. Which of the following is correct?",
            f"Which statement about {label} is most accurate?",
            f"Among close alternatives regarding {label}, which of the following is correct?",
            f"Which of the following is the best statement about {label}?",
        ]
        return templates[n % len(templates)]
    if demo["is_child"]:
        templates = [
            f"{who} is brought in with overlapping findings that include {label}. Which of the following is most accurate after history and examination?",
            f"{who} is hospitalized for evolving {label}. Which of the following is most accurate?",
            f"{who} is evaluated for {label}. Which of the following is the best interpretation?",
            f"{who} has suspected {label}, and similar diagnoses are also considered. Which of the following is most accurate?",
            f"Exam findings in {who.lower()} were first read as {label}. Which of the following is correct?",
            f"{who} presents with {label}. Which of the following best separates it from similar conditions?",
            f"On pediatric rounds, a difficult case of {label} is reviewed. Which of the following is correct?",
            f"{who} has progressive findings of {label}. Which of the following is most accurate?",
        ]
        return templates[n % len(templates)]
    templates = [
        f"{who} presents with findings that overlap several diagnoses, including {label}. Which of the following is most accurate?",
        f"{who} is hospitalized with evolving {label}. Which of the following is most accurate?",
        f"{who} is evaluated for {label}. Which of the following is the best interpretation?",
        f"{who} has suspected {label}, and similar diagnoses remain possible. Which of the following is most accurate?",
        f"Initial reading of the case suggested {label}. Which of the following is correct?",
        f"{who} presents with {label}. Which of the following best separates it from similar conditions?",
        f"A difficult case of {label} in {who.lower()} is reviewed. Which of the following is correct?",
        f"{who} has progressive findings of {label}. Which of the following is most accurate?",
    ]
    return templates[n % len(templates)]


def stem_extreme(topic: dict, n: int, rng: random.Random, field: str, specialty: str) -> str:
    label = condition_name(topic["topic"])
    kind = topic_kind(topic)
    demo = patient_demo(field, specialty, topic, n, "extreme")
    who = demo["who"]
    who_c = who if demo["is_child"] else (
        _with_comorbidities(who, demo["comorbidities"]) if demo["comorbidities"] else who
    )
    if kind in {"concept", "finding"}:
        templates = [
            f"Careful reasoning about {label} is required. Which of the following is most accurate?",
            f"Small differences in wording about {label} matter. Which of the following is correct?",
            f"Which of the following is the most precise statement about {label}?",
            f"In advanced review of {label}, which of the following is most accurate?",
            f"Which interpretation of {label} is most accurate?",
            f"Which closely related statement about {label} is correct?",
            f"Which of the following is the central point about {label}?",
            f"Which statement about {label} is most accurate?",
        ]
        return templates[n % len(templates)]
    if kind == "management":
        templates = [
            f"{who_c} requires urgent decisions about {label}. Which of the following is most accurate?",
            f"Management of {label} is reviewed for {who.lower()}. Which of the following is most accurate?",
            f"{who} needs immediate action related to {label}. Which of the following is correct?",
            f"In {who.lower()}, treatment choices for {label} are debated. Which of the following is most accurate?",
            f"{who_c} is treated for complications related to {label}. Which of the following is correct?",
            f"Safety concerns around {label} arise in {who.lower()}. Which of the following is most accurate?",
            f"{who} has a complicated course involving {label}. Which of the following is correct?",
            f"Which statement about managing {label} in {who.lower()} is most accurate?",
        ]
        return templates[n % len(templates)]
    if demo["is_child"]:
        templates = [
            f"{who} becomes acutely unstable with {label}. Which of the following is most accurate?",
            f"In the emergency department, {who.lower()} is critically ill with {label}. Which of the following is most accurate?",
            f"{who} worsens overnight with {label}. Which of the following is most accurate?",
            f"{who} develops dangerous complications of {label}. Which of the following is correct?",
            f"{who} has a rapidly worsening course of {label}. Which of the following is most accurate?",
            f"Urgent management of {label} is required in {who.lower()}. Which of the following is most accurate?",
            f"{who} has refractory {label}. Which of the following is correct?",
            f"In intensive care, {who.lower()} is treated for {label}. Which of the following is most accurate?",
        ]
        return templates[n % len(templates)]
    templates = [
        f"{who_c} becomes acutely unstable with {label}. Which of the following is most accurate?",
        f"In the emergency department, {who.lower()} is critically ill with {label}. Which of the following is most accurate?",
        f"{who} worsens overnight with {label}. Which of the following is most accurate?",
        f"{who_c} develops dangerous complications of {label}. Which of the following is correct?",
        f"{who} has a rapidly worsening course of {label}. Which of the following is most accurate?",
        f"Urgent management decisions for {label} are required in {who.lower()}. Which of the following is most accurate?",
        f"{who} has refractory {label}. Which of the following is correct?",
        f"In intensive care, {who.lower()} is treated for {label}. Which of the following is most accurate?",
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
                f"{why_near or 'This is a frequent clinical alternative.'} "
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
        "medium": lambda t, i: stem_medium(t, i, rng, field, specialty),
        "hard": lambda t, i: stem_hard(t, i, rng, field, specialty),
        "extreme": lambda t, i: stem_extreme(t, i, rng, field, specialty),
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
