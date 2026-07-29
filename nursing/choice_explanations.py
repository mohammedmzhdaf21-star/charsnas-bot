"""Build long, detailed why-right / why-wrong breakdowns for every MCQ choice."""

from __future__ import annotations


def _letter(option: str) -> str:
    return option.strip()[0].upper()


def _option_body(option: str) -> str:
    text = option.strip()
    if len(text) > 2 and text[1] in ")." and text[0].isalpha():
        return text[2:].strip()
    return text


def _correct_letter(item: dict) -> str:
    return item["answer"].strip()[0].upper()


def explain_choice(
    *,
    letter: str,
    option: str,
    question: str,
    correct_letter: str,
    correct_answer: str,
    core_explanation: str,
    all_options: list[str],
) -> str:
    """Return a long teaching paragraph for one choice."""
    body = _option_body(option)
    correct_body = _option_body(correct_answer)
    other_wrong = [
        _option_body(o)
        for o in all_options
        if _letter(o) not in {letter, correct_letter}
    ]

    if letter == correct_letter:
        return (
            f"✅ Choice {letter} — CORRECT\n"
            f"Statement: {body}\n\n"
            f"Why this is the right answer (detailed):\n"
            f"1) It matches the core teaching point of the question. "
            f"The stem asks you to identify the single best concept; "
            f"“{correct_body}” is the option that stays faithful to that concept "
            f"without adding dangerous assumptions.\n"
            f"2) Core explanation from the bank: {core_explanation}\n"
            f"3) In clinical / exam reasoning, prefer the option that is always "
            f"(or most safely) true for the described scenario. This choice does that: "
            f"it aligns with standard undergraduate teaching, avoids rare-exceptions-first "
            f"thinking, and does not skip urgent safety steps.\n"
            f"4) Contrast with the distractors: the other options typically "
            f"over-simplify, over-generalize (“always/only/never”), name a related but "
            f"different entity, or jump to an unsafe action. Keeping {letter} protects "
            f"you from those traps.\n"
            f"5) How to remember it: restate the question in one line, then ask "
            f"“which option answers THAT exact question?” — {letter} does. "
            f"If two options feel close, pick the safer, more specific, guideline-aligned one; "
            f"here that is {letter}.\n"
            f"6) Study tip: after this item, write one sentence linking the stem → "
            f"mechanism/definition → why {letter} follows. That sentence is your flashcard."
        )

    # Wrong option — long detailed teardown
    traps = []
    low = body.lower()
    if any(w in low for w in ("always", "never", "only", "all ", "none", "forever", "exclusively")):
        traps.append(
            "it uses absolute language (always/never/only). Absolute words are classic "
            "MCQ traps unless the statement is a true universal rule; most clinical "
            "statements have exceptions, so absolutist distractors are usually wrong"
        )
    if any(w in low for w in ("ignore", "do nothing", "no need", "unnecessary", "skip")):
        traps.append(
            "it encourages inaction or skipping assessment/management. In safety-critical "
            "stems, passivity is almost never the best answer"
        )
    if any(w in low for w in ("only", "just ", "merely", "simply")):
        traps.append(
            "it under-treats complexity by pretending one tiny factor explains everything, "
            "while the correct answer captures the fuller mechanism or priority"
        )
    if not traps:
        traps.append(
            "it is a near-miss distractor: related vocabulary or a neighboring concept, "
            "but it does not correctly answer the precise question asked"
        )

    trap_text = "; ".join(traps)
    others = "; ".join(f"“{x}”" for x in other_wrong) if other_wrong else "the remaining distractors"

    return (
        f"❌ Choice {letter} — INCORRECT\n"
        f"Statement: {body}\n\n"
        f"Why this choice is wrong (detailed):\n"
        f"1) It conflicts with the correct teaching point. "
        f"The right answer is {correct_letter}) {correct_body}. "
        f"Choice {letter} does not establish that point and therefore cannot be best.\n"
        f"2) Main reason this distractor fails: {trap_text}.\n"
        f"3) Concept contrast: if you chose {letter}, you likely latched onto a familiar "
        f"word or a partially true idea. Partial truth is not enough — the option must be "
        f"the best complete answer to THIS stem. The bank’s key explanation is: "
        f"{core_explanation} That explanation supports {correct_letter}, not {letter}.\n"
        f"4) What would have to be true for {letter} to become correct? The stem would need "
        f"different facts (different diagnosis, different priority, different mechanism). "
        f"As written, those facts are not present, so {letter} is a mismatch.\n"
        f"5) Clinical / exam danger of believing {letter}: you may pick a less safe action, "
        f"miss the urgent priority, or memorize the wrong association for future questions. "
        f"Rejecting {letter} protects both exam score and real-world reasoning.\n"
        f"6) How to eliminate {letter} next time: (a) underline the exact ask in the stem; "
        f"(b) predict the answer before looking at options; (c) strike any option that is "
        f"too absolute, off-target, or unsafe; (d) compare survivors to the predicted answer. "
        f"Under that process, {letter} falls away and {correct_letter} remains.\n"
        f"7) Relation to other wrong options ({others}): they fail for neighboring reasons "
        f"(wrong entity, wrong priority, or overconfidence). Learning why {letter} fails "
        f"also trains you to spot that whole family of distractors.\n"
        f"8) Memory hook: “{body[:120]}{'…' if len(body) > 120 else ''}” → NOT the answer "
        f"because it does not match “{correct_body[:120]}{'…' if len(correct_body) > 120 else ''}”. "
        f"Drill that contrast out loud once."
    )


def format_all_choice_explanations(item: dict) -> str:
    """Build the full per-choice breakdown block for an MCQ item."""
    options = item.get("options") or []
    if not options:
        return ""

    # Prefer author-provided explanations when present
    provided = item.get("choice_explanations") or item.get("option_explanations") or {}

    correct = _correct_letter(item)
    question = item.get("question", "")
    correct_answer = item.get("answer", "")
    core = item.get("explanation", "")

    blocks = [
        "━━━━━━━━━━━━━━━━━━━━",
        "📚 DETAILED BREAKDOWN OF EVERY CHOICE",
        "Read each option carefully. Wrong answers include long explanations of why they fail.",
        "━━━━━━━━━━━━━━━━━━━━",
    ]

    for opt in options:
        letter = _letter(opt)
        if letter in provided and str(provided[letter]).strip():
            header = (
                f"✅ Choice {letter} — CORRECT\n"
                if letter == correct
                else f"❌ Choice {letter} — INCORRECT\n"
            )
            blocks.append(header + f"Statement: {_option_body(opt)}\n\n" + str(provided[letter]).strip())
        else:
            blocks.append(
                explain_choice(
                    letter=letter,
                    option=opt,
                    question=question,
                    correct_letter=correct,
                    correct_answer=correct_answer,
                    core_explanation=core,
                    all_options=options,
                )
            )
        blocks.append("--------------------")

    blocks.append(
        "📌 Final takeaway: lock in the correct choice, then actively rehearse why each "
        "distractor is wrong so you will not fall for the same trap on exam day."
    )
    return "\n\n".join(blocks)
