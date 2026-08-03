Write ONE JSON bank file for undergraduate Short MCQs.

OUTPUT PATH: {OUT_PATH}
SPECIALTY: {SPECIALTY_LABEL} ({SPECIALTY_KEY})
FIELD/EXAM STYLE: {EXAM_STYLE}

Erase any old content. Create a new JSON object:
{
  "easy": [30 questions],
  "medium": [30 questions],
  "hard": [30 questions],
  "extreme": [30 questions]
}

Each question object MUST be:
{
  "question": "...",
  "options": ["A) ...", "B) ...", "C) ...", "D) ..."],
  "answer": "B) ...",  // exact match to one option
  "explanation": "2-4 scientific textbook sentences",
  "choice_explanations": {
    "A": "1-2 scientific sentences",
    "B": "1-2 scientific sentences",
    "C": "1-2 scientific sentences",
    "D": "1-2 scientific sentences"
  }
}

QUESTION STYLE (mandatory):
- Write like a clinician writing for {EXAM_STYLE} (standardized licensing exam).
- Intense, tricky, educational. Clinical vignettes preferred (especially medium/hard/extreme).
- Easy may be shorter stems but still exam-style, not flashcard meta prompts.
- FORBIDDEN phrases/patterns anywhere in stems:
  - "high-stakes", "junior colleague", "a student analyzes", "item #", "item 1"
  - "single best answer", "beware of near-miss", "core concept of"
  - "in clinical practice regarding", "key teaching point", "which statement best matches"
  - "which choice is the single best", "teaching point"
- Ask naturally: most likely diagnosis, most appropriate next step, most likely mechanism, expected finding, etc.

OPTIONS (mandatory):
- ALL FOUR options must be close, textbook-level near-misses in the same domain (Davidson / standard specialty textbooks style).
- Do NOT include obviously unrelated joke options that are easy to rule out.
- Exactly one correct answer; the other three should create real doubt.
- Balance correct letters roughly evenly across A/B/C/D within the file.

DIFFICULTY:
- easy: foundational but non-trivial exam items
- medium: applied clinical reasoning, short vignette
- hard: multi-cue vignette, close differentials
- extreme: dense high-difficulty vignette (priorities, contraindications, dangerous mimics) — still NO "high-stakes" wording

UNIQUENESS: all 120 stems must be unique.

After writing the file, run:
python3 - <<'PY'
import json
from pathlib import Path
p=Path("{OUT_PATH}")
data=json.loads(p.read_text())
assert all(len(data[d])==30 for d in ["easy","medium","hard","extreme"])
stems=[q["question"].strip().lower() for d in data for q in data[d]]
assert len(stems)==120 and len(set(stems))==120
for d in data:
  for q in data[d]:
    assert q["answer"] in q["options"] and len(q["options"])==4
    assert all(len(str(q["choice_explanations"][L]))>30 for L in "ABCD")
print("OK", p)
PY

Return OK and one hard example stem + options.
