"""Detect duplicate / near-duplicate Short MCQ stems (rephrases).

Intentional difficulty variants that teach the same topic with different stems
should usually remain. We only reject near-copies / paraphrases.
"""

from __future__ import annotations

import os
import re
from difflib import SequenceMatcher
from typing import Any, Iterable

# Tuned for paraphrase detection without wiping board-style variants
DEFAULT_SEQ_THRESHOLD = float(os.getenv("MCQ_SIMILARITY_SEQ", "0.88"))
DEFAULT_JACCARD_THRESHOLD = float(os.getenv("MCQ_SIMILARITY_JACCARD", "0.82"))
DEFAULT_CONTAINMENT_THRESHOLD = float(os.getenv("MCQ_SIMILARITY_CONTAINMENT", "0.92"))
# Cleanup of existing banks uses a stricter near-exact bar
CLEANUP_SEQ_THRESHOLD = float(os.getenv("MCQ_CLEANUP_SEQ", "0.93"))

_STOP = {
    "a", "an", "the", "of", "in", "on", "at", "to", "for", "and", "or", "is", "are",
    "was", "were", "be", "been", "being", "with", "by", "from", "as", "that", "this",
    "these", "those", "which", "what", "when", "where", "who", "whom", "whose", "how",
    "why", "most", "best", "likely", "following", "regarding", "about", "into", "than",
    "then", "also", "only", "not", "no", "yes", "patient", "patients", "year", "years",
    "old", "presents", "presented", "presenting", "statement", "true", "correct",
    "accurate", "among", "below", "above", "after", "before", "during", "while",
    "their", "there", "they", "them", "his", "her", "its", "have", "has", "had",
    "does", "did", "do", "can", "may", "might", "should", "would", "could", "will",
}


class DuplicateQuestionError(ValueError):
    """Raised when a new stem is duplicate/similar to an existing bank item."""

    def __init__(
        self,
        message: str,
        *,
        matched_id: str | None = None,
        matched_question: str | None = None,
        score: float = 0.0,
    ) -> None:
        super().__init__(message)
        self.matched_id = matched_id
        self.matched_question = matched_question
        self.score = score


def normalize_stem(text: str) -> str:
    t = (text or "").lower().strip()
    t = re.sub(r"^[a-d]\)\s*", "", t)
    t = re.sub(r"[^\w\s]", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def _light_stem(word: str) -> str:
    w = word
    if len(w) > 5 and w.endswith("ies"):
        return w[:-3] + "y"
    if len(w) > 5 and w.endswith("ing"):
        return w[:-3]
    if len(w) > 4 and w.endswith("ed"):
        return w[:-2]
    # Plural: tissues->tissue, forms->form (avoid chopping "es" into "tissu")
    if len(w) > 3 and w.endswith("s") and not w.endswith(("ss", "us", "is")):
        return w[:-1]
    return w


def stem_tokens(text: str) -> set[str]:
    toks = []
    for w in normalize_stem(text).split():
        if len(w) < 3 or w in _STOP or w.isdigit():
            continue
        toks.append(_light_stem(w))
    return set(toks)


def similarity_score(a: str, b: str) -> float:
    na, nb = normalize_stem(a), normalize_stem(b)
    if not na or not nb:
        return 0.0
    if na == nb:
        return 1.0
    seq = SequenceMatcher(None, na, nb).ratio()
    ta, tb = stem_tokens(a), stem_tokens(b)
    if not ta or not tb:
        return seq
    inter = len(ta & tb)
    jacc = inter / (len(ta | tb) or 1)
    contain = inter / min(len(ta), len(tb))
    # Sequence dominates; token overlap only boosts when already fairly close
    return max(seq, 0.35 * seq + 0.35 * jacc + 0.30 * contain)


def is_similar(
    a: str,
    b: str,
    *,
    seq_threshold: float = DEFAULT_SEQ_THRESHOLD,
    jaccard_threshold: float = DEFAULT_JACCARD_THRESHOLD,
    containment_threshold: float = DEFAULT_CONTAINMENT_THRESHOLD,
    mode: str = "reject",
) -> tuple[bool, float]:
    """Return (is_duplicate_or_rephrase, score).

    mode='reject' — used when saving new questions (paraphrase-aware)
    mode='cleanup' — only near-exact duplicates in existing banks
    """
    na, nb = normalize_stem(a), normalize_stem(b)
    if not na or not nb:
        return False, 0.0
    if na == nb:
        return True, 1.0

    seq = SequenceMatcher(None, na, nb).ratio()
    ta, tb = stem_tokens(a), stem_tokens(b)
    jacc = contain = 0.0
    if ta and tb:
        inter = len(ta & tb)
        jacc = inter / (len(ta | tb) or 1)
        contain = inter / min(len(ta), len(tb))
    score = similarity_score(a, b)

    if mode == "cleanup":
        # Keep educational variants; only drop near-copies
        hit = seq >= CLEANUP_SEQ_THRESHOLD or na == nb
        return hit, score

    # Paraphrase: high sequence, or almost-same content tokens (reworded stem)
    inter = len(ta & tb) if ta and tb else 0
    symdiff = len(ta ^ tb) if ta and tb else 99
    hit = (
        seq >= seq_threshold
        or (jacc >= jaccard_threshold and seq >= 0.72)
        or (contain >= containment_threshold and jacc >= 0.75 and seq >= 0.70)
        # Same core facts, only 1–2 content words swapped (typical LLM rephrase)
        or (inter >= 3 and symdiff <= 2)
        or (inter >= 4 and symdiff <= 3 and contain >= 0.75)
    )
    return hit, score


def iter_bank_questions(bank: dict[str, list[dict[str, Any]]]) -> Iterable[dict[str, Any]]:
    for diff in ("easy", "medium", "hard", "extreme"):
        for item in bank.get(diff) or []:
            if isinstance(item, dict) and item.get("question"):
                yield item


def find_similar(
    question: str,
    candidates: Iterable[dict[str, Any] | str],
    *,
    seq_threshold: float = DEFAULT_SEQ_THRESHOLD,
    jaccard_threshold: float = DEFAULT_JACCARD_THRESHOLD,
    containment_threshold: float = DEFAULT_CONTAINMENT_THRESHOLD,
    mode: str = "reject",
) -> tuple[dict[str, Any] | None, float]:
    best: dict[str, Any] | None = None
    best_score = 0.0
    best_hit = False
    for raw in candidates:
        item = {"question": raw} if isinstance(raw, str) else raw
        other = str(item.get("question") or "")
        hit, score = is_similar(
            question,
            other,
            seq_threshold=seq_threshold,
            jaccard_threshold=jaccard_threshold,
            containment_threshold=containment_threshold,
            mode=mode,
        )
        if score > best_score:
            best_score = score
        if hit and (best is None or score >= best_score):
            best = item
            best_score = score
            best_hit = True
    return (best if best_hit else None), best_score


def filter_unique_batch(
    items: list[dict[str, Any]],
    existing: Iterable[dict[str, Any] | str],
    *,
    question_key: str = "question",
    mode: str = "reject",
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    kept: list[dict[str, Any]] = []
    dropped: list[dict[str, Any]] = []
    pool: list[dict[str, Any] | str] = list(existing)
    for item in items:
        q = str(item.get(question_key) or "")
        match, score = find_similar(q, pool, mode=mode)
        if match is not None:
            dropped.append(
                {
                    **item,
                    "_duplicate_of": match.get("id") or match.get("question"),
                    "_score": score,
                }
            )
            continue
        kept.append(item)
        pool.append(item)
    return kept, dropped


def existing_stem_samples(bank: dict[str, list[dict[str, Any]]], limit: int = 40) -> list[str]:
    out: list[str] = []
    for item in iter_bank_questions(bank):
        q = str(item.get("question") or "").strip()
        if not q:
            continue
        if len(q) > 160:
            q = q[:157] + "..."
        out.append(q)
        if len(out) >= limit:
            break
    return out
