"""Generate topic study-slide packs via Perplexity (15–20 slides, IMB-style detail)."""

from __future__ import annotations

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
# Generate in small chunks so one broad topic (e.g. Hypertension) cannot
# stall a single 15–20 slide API call until it times out.
CHUNK_SIZE = 8
TARGET_SLIDES = 16


def _build_prompt(
    *,
    department_key: str,
    department_label: str,
    stage_key: str,
    stage_label: str,
    specialty_key: str,
    specialty_label: str,
    topic: str,
    slide_count: int = TARGET_SLIDES,
    chunk_index: int = 1,
    chunk_total: int = 1,
    focus: str = "",
    avoid_titles: list[str] | None = None,
) -> str:
    avoid_block = ""
    if avoid_titles:
        lines = "\n".join(f"- {t}" for t in avoid_titles[:40])
        avoid_block = (
            "\nDo NOT repeat these slide titles already written in earlier chunks:\n"
            f"{lines}\n"
        )
    focus_line = f"Chunk focus: {focus}\n" if focus else ""
    return (
        "You are writing CharaNas study slides for Iraqi Medical Board (IMB)–style teaching.\n"
        "Produce ONE JSON slide chunk for the topic below.\n\n"
        f"department: {department_key} ({department_label})\n"
        f"stage: {stage_key or 'n/a'} ({stage_label or 'n/a'})\n"
        f"specialty/curriculum: {specialty_key} ({specialty_label})\n"
        f"topic: {topic}\n"
        f"chunk: {chunk_index}/{chunk_total}\n"
        f"{focus_line}"
        f"Create exactly {slide_count} slides for this chunk.\n"
        "Each slide is one teaching page with detailed IMB-level prose (not bullet-only fluff).\n\n"
        "Content rules:\n"
        "- Cover the most important high-yield facts for this topic at undergraduate/IMB depth.\n"
        "- Prefer the newest widely accepted clinical information and guideline themes "
        "(state when criteria/staging systems are recent).\n"
        "- Expand abbreviations to full words on first use.\n"
        "- body_paragraphs: 2–3 detailed teaching paragraphs per slide "
        "(mechanism, clinical features, investigations, management, complications as relevant).\n"
        "- bullets: 3–5 high-yield points reinforcing the paragraphs.\n"
        "- clinical_pearl: one advanced exam-style pearl per slide.\n"
        "- figures: on most slides in this chunk, set figure.kind to schematic / anatomy_schematic / "
        "flowchart / comparison / table (not none). Describe the BEST classic textbook-style "
        "sketch for that concept using labels + sketch_notes so our renderer can draw an "
        "original educational schematic. Do NOT claim to paste copyrighted textbook plates; "
        "describe the ideal teaching sketch instead.\n"
        "- sources: 3–6 modern textbook/guideline references (names + editions or societies).\n"
        f"{avoid_block}"
        "- Return strict JSON only matching the schema."
    )


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
                "minItems": 6,
                "maxItems": 10,
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
    min_slides: int = MIN_SLIDES,
    max_slides: int = MAX_SLIDES,
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
    if len(slides) < min_slides:
        raise PerplexityError(
            f"Need at least {min_slides} slides; Perplexity returned {len(slides)} valid slides."
        )
    slides = slides[:max_slides]
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


def _pdf_timeout() -> "httpx.Timeout":
    # Per-chunk timeout (chunks are ~8 slides). Override with PERPLEXITY_PDF_TIMEOUT.
    read_s = float(os.getenv("PERPLEXITY_PDF_TIMEOUT", "240") or "240")
    return httpx.Timeout(connect=30.0, read=read_s, write=60.0, pool=30.0)


def _post_pdf(api_url: str, headers: dict[str, str], payload: dict[str, Any]):
    try:
        with httpx.Client(timeout=_pdf_timeout()) as client:
            return client.post(api_url, headers=headers, json=payload)
    except httpx.TimeoutException as exc:
        raise PerplexityError(
            "Perplexity timed out while writing a slide chunk. Retrying…"
        ) from exc
    except httpx.HTTPError as exc:
        raise PerplexityError(f"Perplexity network error: {exc}") from exc


def _fetch_slide_chunk(
    *,
    api_url: str,
    headers: dict[str, str],
    model: str,
    prompt: str,
    expected_topic: str,
    min_slides: int,
    max_slides: int,
    enable_search: bool = False,
) -> dict[str, Any]:
    system_msg = (
        "You are an IMB (Iraqi Medical Board) medical/dental education writer for CharaNas. "
        "Write detailed, up-to-date teaching slides as strict JSON only. No markdown."
    )

    def _payload(user_prompt: str, response_format: dict[str, Any] | None) -> dict[str, Any]:
        data: dict[str, Any] = {
            "model": model,
            "temperature": 0.2,
            "messages": [
                {"role": "system", "content": system_msg},
                {"role": "user", "content": user_prompt},
            ],
        }
        if response_format is not None:
            data["response_format"] = response_format
        # Default: disable search for speed/reliability. Opt in with PERPLEXITY_PDF_ENABLE_SEARCH=1
        # or enable_search=True for the sources-oriented first chunk.
        force_search = os.getenv("PERPLEXITY_PDF_ENABLE_SEARCH", "").strip().lower() in {
            "1",
            "true",
            "yes",
        }
        if "sonar" in model.lower() and not (force_search or enable_search):
            data["disable_search"] = True
        return data

    plain_suffix = (
        "\n\nRespond with JSON only:\n"
        '{"topic":"...","sources":["..."],"slides":[{"slide_number":1,"title":"...",'
        '"body_paragraphs":["..."],"bullets":["..."],'
        '"figure":{"kind":"schematic","title":"","caption":"...",'
        '"labels":["..."],"sketch_notes":"..."},"clinical_pearl":"..."}]}'
    )
    attempts: list[tuple[str, dict[str, Any]]] = [
        (
            "json_schema",
            _payload(prompt, {"type": "json_schema", "json_schema": SLIDE_BATCH_SCHEMA}),
        ),
        (
            "json_object",
            _payload(
                prompt + "\n\nRespond with a JSON object containing a slides array.",
                {"type": "json_object"},
            ),
        ),
        ("plain_json", _payload(prompt + plain_suffix, None)),
    ]

    last_error = "unknown error"
    for label, payload in attempts:
        for round_i in range(1, 3):
            try:
                resp = _post_pdf(api_url, headers, payload)
            except PerplexityError as exc:
                last_error = str(exc)
                log.warning("PDF chunk %s round %s: %s", label, round_i, last_error)
                continue
            if resp.status_code >= 400:
                last_error = f"Perplexity API {resp.status_code}: {resp.text[:400]}"
                log.warning("PDF chunk %s HTTP error: %s", label, last_error)
                if resp.status_code in {401, 403}:
                    raise PerplexityError(
                        "Perplexity rejected the API key (401/403). "
                        "Check PERPLEXITY_API_KEY in question_input/.env and restart the input bot."
                    )
                break
            body = resp.json()
            try:
                content = body["choices"][0]["message"]["content"]
            except (KeyError, IndexError, TypeError):
                last_error = f"Unexpected Perplexity response: {str(body)[:500]}"
                break
            if isinstance(content, list):
                content = "".join(
                    part.get("text", "") if isinstance(part, dict) else str(part)
                    for part in content
                )
            try:
                raw = _parse_raw_json(str(content))
                return validate_slide_deck(
                    raw,
                    expected_topic=expected_topic,
                    min_slides=min_slides,
                    max_slides=max_slides,
                )
            except PerplexityError as exc:
                last_error = str(exc)
                log.warning("PDF chunk %s validate failed: %s", label, last_error)
                break
    raise PerplexityError(last_error)


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
    """Build a 15–20 slide deck via small Perplexity chunks (avoids full-deck timeouts)."""
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
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    # Two chunks of 8 => 16 slides (within 15–20). Broad topics no longer use one huge call.
    chunk_plan = [
        {
            "count": CHUNK_SIZE,
            "focus": (
                "definition, epidemiology, pathophysiology, classification/staging, "
                "clinical features, red flags"
            ),
            "enable_search": True,
        },
        {
            "count": CHUNK_SIZE,
            "focus": (
                "investigations, differentials, acute and chronic management, "
                "complications, guidelines, IMB exam traps"
            ),
            "enable_search": False,
        },
    ]

    log.info(
        "Calling Perplexity PDF in %s chunks topic=%r dept=%s specialty=%s",
        len(chunk_plan),
        topic,
        department_key,
        specialty_key,
    )

    all_slides: list[dict[str, Any]] = []
    all_sources: list[str] = []
    seen_titles: set[str] = set()

    for idx, plan in enumerate(chunk_plan, start=1):
        prompt = _build_prompt(
            department_key=department_key,
            department_label=department_label,
            stage_key=stage_key,
            stage_label=stage_label,
            specialty_key=specialty_key,
            specialty_label=specialty_label,
            topic=topic,
            slide_count=int(plan["count"]),
            chunk_index=idx,
            chunk_total=len(chunk_plan),
            focus=str(plan["focus"]),
            avoid_titles=sorted(seen_titles),
        )
        chunk = _fetch_slide_chunk(
            api_url=api_url,
            headers=headers,
            model=model,
            prompt=prompt,
            expected_topic=topic,
            min_slides=max(6, int(plan["count"]) - 2),
            max_slides=int(plan["count"]),
            enable_search=bool(plan.get("enable_search")),
        )
        for slide in chunk.get("slides") or []:
            title = str(slide.get("title") or "").strip()
            key_title = title.lower()
            if key_title and key_title in seen_titles:
                continue
            if key_title:
                seen_titles.add(key_title)
            all_slides.append(slide)
        for src in chunk.get("sources") or []:
            s = str(src).strip()
            if s and s not in all_sources:
                all_sources.append(s)

    if len(all_slides) < MIN_SLIDES:
        raise PerplexityError(
            f"Need at least {MIN_SLIDES} slides after chunking; got {len(all_slides)}."
        )

    all_slides = all_slides[:MAX_SLIDES]
    for i, slide in enumerate(all_slides, start=1):
        slide["slide_number"] = i
    return {
        "topic": topic,
        "sources": all_sources[:12],
        "slides": all_slides,
    }


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
