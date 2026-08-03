"""Generate topic study-slide packs via Perplexity (15–20 slides, IMB-style detail)."""

from __future__ import annotations

import json
import logging
import os
import re
from typing import Any

import httpx

try:
    from perplexity_gen import (
        DEFAULT_API_URL,
        DEFAULT_MODEL,
        PerplexityError,
        _parse_raw_json,
        api_key,
    )
except ImportError:  # pragma: no cover
    from question_input.perplexity_gen import (
        DEFAULT_API_URL,
        DEFAULT_MODEL,
        PerplexityError,
        _parse_raw_json,
        api_key,
    )

log = logging.getLogger("charanas-input-bot.perplexity-pdf")

MIN_SLIDES = 15
MAX_SLIDES = 20

SLIDE_BATCH_SCHEMA: dict[str, Any] = {
    "name": "charanas_topic_slides",
    "schema": {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "department": {"type": "string"},
            "stage": {"type": "string"},
            "specialty": {"type": "string"},
            "topic": {"type": "string"},
            "sources": {
                "type": "array",
                "items": {"type": "string"},
            },
            "slides": {
                "type": "array",
                "minItems": MIN_SLIDES,
                "maxItems": MAX_SLIDES,
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "slide_number": {"type": "integer"},
                        "title": {"type": "string"},
                        "body_paragraphs": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "bullets": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "figure": {
                            "type": "object",
                            "additionalProperties": False,
                            "properties": {
                                "kind": {
                                    "type": "string",
                                    "enum": [
                                        "schematic",
                                        "anatomy_schematic",
                                        "flowchart",
                                        "comparison",
                                        "table",
                                        "none",
                                    ],
                                },
                                "title": {"type": "string"},
                                "caption": {"type": "string"},
                                "labels": {
                                    "type": "array",
                                    "items": {"type": "string"},
                                },
                                "sketch_notes": {"type": "string"},
                            },
                            "required": ["kind", "caption", "labels", "sketch_notes"],
                        },
                        "clinical_pearl": {"type": "string"},
                    },
                    "required": [
                        "slide_number",
                        "title",
                        "body_paragraphs",
                        "bullets",
                        "figure",
                        "clinical_pearl",
                    ],
                },
            },
        },
        "required": ["department", "stage", "specialty", "topic", "sources", "slides"],
    },
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
) -> str:
    return (
        "You are writing CharaNas study slides for Iraqi Medical Board (IMB)–style teaching.\n"
        "Produce ONE PDF slide deck as strict JSON for the topic below.\n\n"
        f"department: {department_key} ({department_label})\n"
        f"stage: {stage_key or 'n/a'} ({stage_label or 'n/a'})\n"
        f"specialty/curriculum: {specialty_key} ({specialty_label})\n"
        f"topic: {topic}\n\n"
        f"Create between {MIN_SLIDES} and {MAX_SLIDES} slides (inclusive).\n"
        "Each slide is one teaching page with detailed IMB-level prose (not bullet-only fluff).\n\n"
        "Content rules:\n"
        "- Cover the most important high-yield facts for this topic at undergraduate/IMB depth.\n"
        "- Prefer the newest widely accepted clinical information and guideline themes "
        "(state when criteria/staging systems are recent).\n"
        "- Expand abbreviations to full words on first use.\n"
        "- body_paragraphs: 2–4 detailed teaching paragraphs per slide "
        "(mechanism, clinical features, investigations, management, complications as relevant).\n"
        "- bullets: 3–6 high-yield points reinforcing the paragraphs.\n"
        "- clinical_pearl: one advanced exam-style pearl per slide.\n"
        "- figures: on at least 10 slides, set figure.kind to schematic / anatomy_schematic / "
        "flowchart / comparison / table (not none). Describe the BEST classic textbook-style "
        "sketch for that concept using labels + sketch_notes so our renderer can draw an "
        "original educational schematic. Do NOT claim to paste copyrighted textbook plates; "
        "describe the ideal teaching sketch instead.\n"
        "- sources: 4–8 modern textbook/guideline references (names + editions or societies).\n"
        "- Slide 1 should introduce/define the topic; later slides deepen diagnosis, differentials, "
        "workup, management, complications, and exam traps.\n"
        "- Return strict JSON only matching the schema."
    )


def _normalize_figure(raw: Any) -> dict[str, Any]:
    if not isinstance(raw, dict):
        return {
            "kind": "none",
            "title": "",
            "caption": "",
            "labels": [],
            "sketch_notes": "",
        }
    kind = str(raw.get("kind") or "none").strip().lower().replace(" ", "_")
    allowed = {
        "schematic",
        "anatomy_schematic",
        "flowchart",
        "comparison",
        "table",
        "none",
        "anatomy",
        "flow",
        "labeled_anatomy",
    }
    if kind not in allowed:
        kind = "schematic" if (raw.get("labels") or raw.get("sketch_notes")) else "none"
    if kind in {"anatomy", "labeled_anatomy"}:
        kind = "anatomy_schematic"
    if kind == "flow":
        kind = "flowchart"
    labels = raw.get("labels") or []
    if not isinstance(labels, list):
        labels = [str(labels)]
    return {
        "kind": kind,
        "title": str(raw.get("title") or "").strip(),
        "caption": str(raw.get("caption") or raw.get("title") or "").strip(),
        "labels": [str(x).strip() for x in labels if str(x).strip()][:8],
        "sketch_notes": str(raw.get("sketch_notes") or raw.get("description") or "").strip(),
    }


def _normalize_slide(raw: dict[str, Any], index: int) -> dict[str, Any] | None:
    title = str(raw.get("title") or "").strip()
    if not title:
        return None
    paras = raw.get("body_paragraphs") or raw.get("paragraphs") or raw.get("body") or []
    if isinstance(paras, str):
        paras = [paras]
    if not isinstance(paras, list):
        paras = []
    paras = [str(p).strip() for p in paras if str(p).strip()]
    bullets = raw.get("bullets") or raw.get("points") or []
    if isinstance(bullets, str):
        bullets = [bullets]
    if not isinstance(bullets, list):
        bullets = []
    bullets = [str(b).strip() for b in bullets if str(b).strip()]
    if not paras and not bullets:
        return None
    if not paras and bullets:
        paras = [" ".join(bullets[:2])]
    num = raw.get("slide_number")
    try:
        slide_number = int(num)
    except (TypeError, ValueError):
        slide_number = index
    return {
        "slide_number": slide_number,
        "title": title,
        "body_paragraphs": paras[:6],
        "bullets": bullets[:8],
        "figure": _normalize_figure(raw.get("figure")),
        "clinical_pearl": str(raw.get("clinical_pearl") or raw.get("pearl") or "").strip(),
    }


def validate_slide_deck(
    data: dict[str, Any],
    *,
    expected_topic: str,
) -> dict[str, Any]:
    slides_raw = data.get("slides") or data.get("pages") or data.get("deck")
    if not isinstance(slides_raw, list) or not slides_raw:
        raise PerplexityError("JSON missing a non-empty slides array.")
    slides: list[dict[str, Any]] = []
    for i, raw in enumerate(slides_raw, start=1):
        if not isinstance(raw, dict):
            continue
        item = _normalize_slide(raw, i)
        if item:
            slides.append(item)
    if len(slides) < MIN_SLIDES:
        raise PerplexityError(
            f"Need at least {MIN_SLIDES} slides; Perplexity returned {len(slides)} valid slides."
        )
    slides = slides[:MAX_SLIDES]
    for i, s in enumerate(slides, start=1):
        s["slide_number"] = i
    sources = data.get("sources") or []
    if not isinstance(sources, list):
        sources = [str(sources)]
    sources = [str(s).strip() for s in sources if str(s).strip()][:12]
    return {
        "topic": str(data.get("topic") or expected_topic).strip() or expected_topic,
        "sources": sources,
        "slides": slides,
    }


def generate_topic_slides(
    *,
    department_key: str,
    department_label: str,
    specialty_key: str,
    specialty_label: str,
    topic: str,
    stage_key: str = "",
    stage_label: str = "",
) -> dict[str, Any]:
    """Call Perplexity (with search) and return a normalized 15–20 slide deck."""
    key = api_key()
    if not key:
        raise PerplexityError(
            "Missing PERPLEXITY_API_KEY. Add it to question_input/.env and restart the input bot."
        )
    topic = topic.strip()
    if not topic:
        raise PerplexityError("Topic is required for PDF generation.")

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
    )

    payload: dict[str, Any] = {
        "model": model,
        "temperature": 0.2,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are an IMB (Iraqi Medical Board) medical/dental education writer for CharaNas. "
                    "Write detailed, up-to-date teaching slides as strict JSON only. No markdown."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        "response_format": {
            "type": "json_schema",
            "json_schema": SLIDE_BATCH_SCHEMA,
        },
    }
    # Keep web search ON so newest guideline themes can inform content.
    if "sonar" in model.lower() and os.getenv("PERPLEXITY_PDF_DISABLE_SEARCH", "").strip() in {
        "1",
        "true",
        "yes",
    }:
        payload["disable_search"] = True

    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    log.info(
        "Calling Perplexity for topic PDF slides topic=%r dept=%s specialty=%s",
        topic,
        department_key,
        specialty_key,
    )
    try:
        with httpx.Client(timeout=180.0) as client:
            resp = client.post(api_url, headers=headers, json=payload)
    except httpx.HTTPError as exc:
        raise PerplexityError(f"Perplexity network error: {exc}") from exc

    if resp.status_code >= 400:
        if resp.status_code in {400, 422} and "response_format" in payload:
            log.warning("Perplexity rejected slide response_format; retrying plain JSON prompt")
            payload.pop("response_format", None)
            payload["messages"][-1]["content"] += (
                "\n\nRespond with JSON only:\n"
                '{"department":"...","stage":"...","specialty":"...","topic":"...",'
                '"sources":["..."],"slides":[{"slide_number":1,"title":"...",'
                '"body_paragraphs":["..."],"bullets":["..."],'
                '"figure":{"kind":"schematic","title":"","caption":"...",'
                '"labels":["..."],"sketch_notes":"..."},"clinical_pearl":"..."}]}'
            )
            with httpx.Client(timeout=180.0) as client:
                resp = client.post(api_url, headers=headers, json=payload)
        if resp.status_code >= 400:
            raise PerplexityError(f"Perplexity API {resp.status_code}: {resp.text[:400]}")

    body = resp.json()
    try:
        content = body["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise PerplexityError(f"Unexpected Perplexity response: {str(body)[:500]}") from exc

    if isinstance(content, list):
        content = "".join(
            part.get("text", "") if isinstance(part, dict) else str(part) for part in content
        )

    raw = _parse_raw_json(str(content))
    deck = validate_slide_deck(raw, expected_topic=topic)
    return deck


def parse_topics(text: str) -> list[str]:
    """Split user message into one topic per PDF (newline / ; / | separated)."""
    parts = re.split(r"[\n;|]+", text or "")
    topics: list[str] = []
    for p in parts:
        t = " ".join(p.strip().split())
        if t and t.lower() not in {"skip", "/skip"}:
            topics.append(t[:160])
    # de-dupe preserving order
    seen: set[str] = set()
    out: list[str] = []
    for t in topics:
        key = t.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(t)
    return out[:10]
