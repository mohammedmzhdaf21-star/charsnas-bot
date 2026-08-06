"""Generate Short MCQs via Perplexity API — strict JSON batch + validation."""

from __future__ import annotations

import json
import logging
import os
import re
from typing import Any

import httpx

log = logging.getLogger("charanas-input-bot.perplexity")

DEFAULT_API_URL = "https://api.perplexity.ai/chat/completions"
DEFAULT_MODEL = "sonar-pro"
DIFFICULTIES = ("easy", "medium", "hard", "extreme")

# Same advancement mixes as study bots
LEVEL_MIXES: dict[int, dict[str, float]] = {
    1: {"easy": 0.50, "medium": 0.20, "hard": 0.20, "extreme": 0.10},
    2: {"easy": 0.35, "medium": 0.35, "hard": 0.20, "extreme": 0.10},
    3: {"easy": 0.20, "medium": 0.30, "hard": 0.30, "extreme": 0.20},
    4: {"easy": 0.20, "medium": 0.20, "hard": 0.30, "extreme": 0.30},
    5: {"easy": 0.15, "medium": 0.15, "hard": 0.20, "extreme": 0.50},
}

BATCH_JSON_SCHEMA: dict[str, Any] = {
    "name": "charanas_mcq_batch",
    "schema": {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "department": {"type": "string"},
            "stage": {"type": "string"},
            "specialty": {"type": "string"},
            "topic": {"type": "string"},
            "difficulty_distribution": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "easy": {"type": "integer"},
                    "medium": {"type": "integer"},
                    "hard": {"type": "integer"},
                    "extreme": {"type": "integer"},
                },
                "required": ["easy", "medium", "hard", "extreme"],
            },
            "questions": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "difficulty": {
                            "type": "string",
                            "enum": ["easy", "medium", "hard", "extreme"],
                        },
                        "question": {"type": "string"},
                        "options": {
                            "type": "array",
                            "minItems": 4,
                            "maxItems": 4,
                            "items": {"type": "string"},
                        },
                        "answer_letter": {
                            "type": "string",
                            "enum": ["A", "B", "C", "D"],
                        },
                        "explanation": {"type": "string"},
                        "choice_explanations": {
                            "type": "object",
                            "additionalProperties": False,
                            "properties": {
                                "A": {"type": "string"},
                                "B": {"type": "string"},
                                "C": {"type": "string"},
                                "D": {"type": "string"},
                            },
                            "required": ["A", "B", "C", "D"],
                        },
                    },
                    "required": [
                        "difficulty",
                        "question",
                        "options",
                        "answer_letter",
                        "explanation",
                    ],
                },
            },
        },
        "required": [
            "department",
            "stage",
            "specialty",
            "topic",
            "difficulty_distribution",
            "questions",
        ],
    },
}

# Simpler schema used as fallback when the full schema is rejected by the API.
BATCH_JSON_SCHEMA_SIMPLE: dict[str, Any] = {
    "name": "charanas_mcq_batch_simple",
    "schema": {
        "type": "object",
        "additionalProperties": True,
        "properties": {
            "questions": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": True,
                    "properties": {
                        "difficulty": {"type": "string"},
                        "question": {"type": "string"},
                        "options": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "answer_letter": {"type": "string"},
                        "explanation": {"type": "string"},
                    },
                    "required": [
                        "difficulty",
                        "question",
                        "options",
                        "answer_letter",
                        "explanation",
                    ],
                },
            },
        },
        "required": ["questions"],
    },
}


class PerplexityError(RuntimeError):
    """Raised when Perplexity generation or validation fails."""


def api_key() -> str:
    return (
        os.getenv("PERPLEXITY_API_KEY")
        or os.getenv("PPLX_API_KEY")
        or ""
    ).strip()


def configured() -> bool:
    return bool(api_key())


def allocate_mix(count: int, level: int) -> dict[str, int]:
    """Largest-remainder allocation so counts sum exactly to `count`."""
    if level not in LEVEL_MIXES:
        raise PerplexityError(f"Invalid level: {level}")
    mix = LEVEL_MIXES[level]
    raw = {d: count * mix[d] for d in DIFFICULTIES}
    alloc = {d: int(raw[d]) for d in DIFFICULTIES}
    rem = count - sum(alloc.values())
    order = sorted(DIFFICULTIES, key=lambda d: (raw[d] - alloc[d], mix[d]), reverse=True)
    for i in range(rem):
        alloc[order[i % len(order)]] += 1
    return alloc


def single_distribution(count: int, difficulty: str) -> dict[str, int]:
    if difficulty not in DIFFICULTIES:
        raise PerplexityError(f"Invalid difficulty: {difficulty}")
    dist = {d: 0 for d in DIFFICULTIES}
    dist[difficulty] = count
    return dist


def mix_summary(dist: dict[str, int]) -> str:
    return " · ".join(f"{d.capitalize()} {dist.get(d, 0)}" for d in DIFFICULTIES)


def _strip_code_fence(text: str) -> str:
    t = text.strip()
    if t.startswith("```"):
        t = re.sub(r"^```(?:json)?\s*", "", t, count=1, flags=re.I)
        t = re.sub(r"\s*```$", "", t, count=1)
    return t.strip()


def _normalize_item(raw: dict[str, Any], fallback_difficulty: str = "medium") -> dict[str, Any] | None:
    question = str(raw.get("question") or "").strip()
    options = raw.get("options") or []
    if not isinstance(options, list):
        return None
    opts = [str(o).strip() for o in options]
    if len(opts) != 4 and isinstance(raw.get("options"), dict):
        od = raw["options"]
        opts = [str(od.get(L) or od.get(L.lower()) or "").strip() for L in "ABCD"]
    if not question or len(opts) != 4 or any(not o for o in opts):
        return None
    cleaned = []
    for i, o in enumerate(opts):
        cleaned.append(re.sub(rf"^{re.escape('ABCD'[i])}\)\s*", "", o, count=1, flags=re.I).strip())
    letter = str(raw.get("answer_letter") or raw.get("answer") or "").strip().upper()[:1]
    if letter not in "ABCD":
        ans = str(raw.get("answer") or "").strip()
        for i, o in enumerate(cleaned):
            if ans and (ans == o or ans.endswith(o) or o in ans):
                letter = "ABCD"[i]
                break
    if letter not in "ABCD":
        return None
    difficulty = str(raw.get("difficulty") or fallback_difficulty).strip().lower()
    if difficulty not in DIFFICULTIES:
        difficulty = fallback_difficulty
    explanation = str(raw.get("explanation") or "").strip()
    choice_explanations = _normalize_choice_explanations(
        raw.get("choice_explanations") or raw.get("option_explanations"),
        answer_letter=letter,
        explanation=explanation,
    )
    return {
        "difficulty": difficulty,
        "question": question,
        "options": cleaned,
        "answer_letter": letter,
        "explanation": explanation or "Generated by Perplexity.",
        "choice_explanations": choice_explanations,
    }


def _normalize_choice_explanations(
    raw: Any,
    *,
    answer_letter: str,
    explanation: str,
) -> dict[str, str]:
    """Normalize A–D choice rationales; fill gaps from the main explanation."""
    out: dict[str, str] = {}
    if isinstance(raw, dict):
        for L in "ABCD":
            val = raw.get(L) or raw.get(L.lower())
            if isinstance(val, dict):
                text = str(
                    val.get("why_not")
                    or val.get("why_wrong")
                    or val.get("why")
                    or val.get("reason")
                    or val.get("meaning")
                    or ""
                ).strip()
            else:
                text = str(val or "").strip()
            if text and text.lower() not in {
                "not the best answer for this item.",
                "not the best answer",
                "incorrect",
            }:
                out[L] = text
    # Correct choice should always have a rationale for reveal
    if answer_letter in "ABCD" and answer_letter not in out and explanation:
        out[answer_letter] = explanation
    return out


def _parse_raw_json(content: str) -> dict[str, Any]:
    text = _strip_code_fence(content)
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        m = re.search(r"(\{[\s\S]*\})", text)
        if not m:
            raise PerplexityError("Perplexity reply was not valid JSON.")
        data = json.loads(m.group(1))
    if not isinstance(data, dict):
        raise PerplexityError("Perplexity JSON must be an object.")
    return data


def validate_batch(
    data: dict[str, Any],
    *,
    expected_department: str,
    expected_specialty: str,
    expected_stage: str = "",
    expected_topic: str = "",
    expected_distribution: dict[str, int] | None = None,
    fallback_difficulty: str = "medium",
) -> dict[str, Any]:
    """Validate and normalize a Perplexity batch. Returns a clean batch dict."""
    questions_raw = data.get("questions") or data.get("items") or data.get("mcqs")
    if not isinstance(questions_raw, list) or not questions_raw:
        raise PerplexityError("JSON missing a non-empty questions array.")

    items: list[dict[str, Any]] = []
    for raw in questions_raw:
        if not isinstance(raw, dict):
            continue
        item = _normalize_item(raw, fallback_difficulty=fallback_difficulty)
        if item:
            items.append(item)
    if not items:
        raise PerplexityError("No valid Short MCQs after validation.")

    # Rebuild distribution from accepted items (source of truth after validation)
    dist = {d: 0 for d in DIFFICULTIES}
    for item in items:
        dist[item["difficulty"]] += 1

    if expected_distribution:
        expected_total = sum(expected_distribution.values())
        if len(items) > expected_total:
            items = items[:expected_total]
            dist = {d: 0 for d in DIFFICULTIES}
            for item in items:
                dist[item["difficulty"]] += 1

    stage = str(data.get("stage") or expected_stage or "").strip()
    topic = str(data.get("topic") or expected_topic or expected_specialty).strip()
    department = str(data.get("department") or expected_department).strip().lower()
    specialty = str(data.get("specialty") or expected_specialty).strip().lower()

    # Soft-check identity fields (form wins)
    if department and department.replace(" ", "_") not in {
        expected_department,
        expected_department.replace("_", " "),
    }:
        log.warning(
            "Perplexity department %r differs from form %r — keeping form value",
            department,
            expected_department,
        )
    if specialty and specialty.replace(" ", "_") not in {
        expected_specialty,
        expected_specialty.replace("_", " "),
    }:
        log.warning(
            "Perplexity specialty %r differs from form %r — keeping form value",
            specialty,
            expected_specialty,
        )

    return {
        "department": expected_department,
        "stage": expected_stage or stage,
        "specialty": expected_specialty,
        "topic": topic,
        "difficulty_distribution": dist,
        "questions": items,
    }


def _build_prompt(
    *,
    department_key: str,
    department_label: str,
    stage_key: str,
    stage_label: str,
    specialty_key: str,
    specialty_label: str,
    topic: str,
    distribution: dict[str, int],
    avoid_stems: list[str] | None = None,
) -> str:
    focus = topic.strip() if topic.strip() else specialty_label
    total = sum(distribution.values())
    dist_line = ", ".join(f"{distribution[d]} {d}" for d in DIFFICULTIES if distribution[d])
    avoid_block = ""
    if avoid_stems:
        lines = "\n".join(f"- {s}" for s in avoid_stems[:50])
        avoid_block = (
            "\n\nDo NOT write questions that are the same as, or mere rephrases of, "
            "these existing stems already in the bank:\n"
            f"{lines}\n"
            "Each new stem must test a different fact, decision, or clinical angle.\n"
        )
    return (
        "You are generating exam content for the CharaNas study system.\n"
        "Decide wording for each stem, but keep the routing fields exactly as given.\n\n"
        f"department: {department_key} ({department_label})\n"
        f"stage: {stage_key or 'n/a'} ({stage_label or 'n/a'})\n"
        f"specialty/curriculum: {specialty_key} ({specialty_label})\n"
        f"topic: {focus}\n"
        f"difficulty_distribution: {dist_line} (total {total})\n\n"
        "Generate exactly that many Short MCQ questions.\n"
        "Each question must include its own difficulty matching the distribution counts.\n\n"
        "Rules:\n"
        "- Clinically accurate and coherent; no fake crisis wording on mild topics.\n"
        "- Expand abbreviations to full words in stems and choices.\n"
        "- Exactly 4 options; one best answer (answer_letter A/B/C/D).\n"
        "- Plausible distractors only.\n"
        "- Do not prefix options with A)/B)/C)/D).\n"
        "- explanation: 3–5 teaching sentences at a slightly more advanced level than the stem. "
        "First justify the correct choice with mechanism/pathophysiology/clinical reasoning, "
        "then explicitly say why each incorrect choice is wrong (specific contrast for A/B/C/D, "
        "not generic 'not the best answer').\n"
        "- choice_explanations: object with keys A, B, C, D.\n"
        "  • Correct letter: slightly more advanced rationale for why that choice is correct "
        "(mechanism, landmark finding, or decision rule).\n"
        "  • Each incorrect letter: one clear sentence stating why that specific choice is "
        "incorrect for this stem (what it confuses or which criterion it fails).\n"
        "  • Never use placeholders like 'Not the best answer for this item.'\n"
        "- Questions in this batch must also be distinct from each other "
        "(no rephrased duplicates inside the batch).\n"
        "- Return strict JSON only matching the schema."
        f"{avoid_block}"
    )


def _post_perplexity(api_url: str, headers: dict[str, str], payload: dict[str, Any]):
    try:
        import httpx
    except ImportError as exc:  # pragma: no cover
        raise PerplexityError(
            "Python package httpx is not installed. Run: pip install httpx"
        ) from exc
    try:
        with httpx.Client(timeout=120.0) as client:
            return client.post(api_url, headers=headers, json=payload)
    except httpx.HTTPError as err:
        raise PerplexityError(f"Perplexity network error: {err}") from err


def generate_batch(
    *,
    department_key: str,
    department_label: str,
    specialty_key: str,
    specialty_label: str,
    distribution: dict[str, int],
    topic: str = "",
    stage_key: str = "",
    stage_label: str = "",
    avoid_stems: list[str] | None = None,
) -> dict[str, Any]:
    """Call Perplexity, validate JSON, return normalized batch.

    Retries with simpler schemas if the API rejects strict json_schema formatting.
    """
    key = api_key()
    if not key:
        raise PerplexityError(
            "Missing PERPLEXITY_API_KEY. Add it to question_input/.env and restart the input bot."
        )
    total = sum(distribution.values())
    if total < 1 or total > 20:
        raise PerplexityError("Count must be between 1 and 20 for Perplexity generation.")
    for d in DIFFICULTIES:
        distribution.setdefault(d, 0)

    api_url = (os.getenv("PERPLEXITY_API_URL") or DEFAULT_API_URL).strip()
    model = (os.getenv("PERPLEXITY_MODEL") or DEFAULT_MODEL).strip()
    prompt = _build_prompt(
        department_key=department_key,
        department_label=department_label,
        stage_key=stage_key,
        stage_label=stage_label,
        specialty_key=specialty_key,
        specialty_label=specialty_label,
        topic=topic,
        distribution=distribution,
        avoid_stems=avoid_stems,
    )
    fallback_diff = next((d for d in DIFFICULTIES if distribution.get(d)), "medium")

    system_msg = (
        "You are a medical/dental education exam writer for CharaNas. "
        "When revealing answers, always teach why the correct choice is right "
        "at a slightly more advanced level, and why each incorrect choice is wrong. "
        "Output strict JSON only. No markdown."
    )
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    attempts: list[dict[str, Any]] = [
        {
            "label": "json_schema_full",
            "payload": {
                "model": model,
                "temperature": 0.2,
                "messages": [
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": prompt},
                ],
                "response_format": {
                    "type": "json_schema",
                    "json_schema": BATCH_JSON_SCHEMA,
                },
            },
        },
        {
            "label": "json_schema_simple",
            "payload": {
                "model": model,
                "temperature": 0.2,
                "messages": [
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": prompt},
                ],
                "response_format": {
                    "type": "json_schema",
                    "json_schema": BATCH_JSON_SCHEMA_SIMPLE,
                },
            },
        },
        {
            "label": "json_object",
            "payload": {
                "model": model,
                "temperature": 0.2,
                "messages": [
                    {"role": "system", "content": system_msg},
                    {
                        "role": "user",
                        "content": prompt
                        + "\n\nRespond with a JSON object only containing a questions array.",
                    },
                ],
                "response_format": {"type": "json_object"},
            },
        },
        {
            "label": "plain_json",
            "payload": {
                "model": model,
                "temperature": 0.2,
                "messages": [
                    {"role": "system", "content": system_msg},
                    {
                        "role": "user",
                        "content": prompt
                        + "\n\nRespond with JSON only:\n"
                        '{"department":"...","stage":"...","specialty":"...","topic":"...",'
                        '"difficulty_distribution":{"easy":0,"medium":0,"hard":0,"extreme":0},'
                        '"questions":[{"difficulty":"medium","question":"...","options":'
                        '["...","...","...","..."],"answer_letter":"A","explanation":"...",'
                        '"choice_explanations":{"A":"why A","B":"why B","C":"why C","D":"why D"}}]}',
                    },
                ],
            },
        },
    ]

    log.info(
        "Calling Perplexity model=%s total=%s dept=%s specialty=%s topic=%r",
        model,
        total,
        department_key,
        specialty_key,
        topic,
    )

    last_error = "unknown error"
    content = ""
    for attempt in attempts:
        payload = attempt["payload"]
        if "sonar" in model.lower():
            payload = dict(payload)
            payload["disable_search"] = True
        resp = _post_perplexity(api_url, headers, payload)
        if resp.status_code >= 400:
            last_error = f"Perplexity API {resp.status_code}: {resp.text[:400]}"
            log.warning("Attempt %s failed: %s", attempt["label"], last_error)
            # Auth errors will not be fixed by schema retries
            if resp.status_code in {401, 403}:
                raise PerplexityError(
                    "Perplexity rejected the API key (401/403). "
                    "Check PERPLEXITY_API_KEY in question_input/.env and restart the input bot."
                )
            continue
        body = resp.json()
        try:
            content = body["choices"][0]["message"]["content"]
        except (KeyError, IndexError, TypeError):
            last_error = f"Unexpected Perplexity response: {str(body)[:500]}"
            log.warning("Attempt %s bad body: %s", attempt["label"], last_error)
            continue
        if isinstance(content, list):
            content = "".join(
                part.get("text", "") if isinstance(part, dict) else str(part) for part in content
            )
        try:
            raw = _parse_raw_json(str(content))
            return validate_batch(
                raw,
                expected_department=department_key,
                expected_specialty=specialty_key,
                expected_stage=stage_key,
                expected_topic=topic or specialty_label,
                expected_distribution=distribution,
                fallback_difficulty=fallback_diff,
            )
        except PerplexityError as exc:
            last_error = str(exc)
            log.warning("Attempt %s validate failed: %s", attempt["label"], last_error)
            continue

    raise PerplexityError(last_error)


# Back-compat helper used by older call sites / tests
def generate_short_mcqs(
    *,
    department_label: str,
    specialty_label: str,
    difficulty: str,
    count: int,
    topic: str = "",
) -> list[dict[str, Any]]:
    batch = generate_batch(
        department_key=department_label.lower().replace(" ", "_"),
        department_label=department_label,
        specialty_key=specialty_label.lower().replace(" ", "_"),
        specialty_label=specialty_label,
        distribution=single_distribution(count, difficulty),
        topic=topic,
    )
    return batch["questions"]
