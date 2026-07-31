"""Short MCQ session helpers: question counts, advancement levels, daily limits."""

from __future__ import annotations

import json
import random
import threading
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DAILY_LIMIT = 20
COUNT_OPTIONS = (5, 10, 15, 20)

# Advancement level → difficulty mix (must sum to 1.0)
LEVEL_MIXES: dict[int, dict[str, float]] = {
    1: {"easy": 0.50, "medium": 0.20, "hard": 0.20, "extreme": 0.10},
    2: {"easy": 0.35, "medium": 0.35, "hard": 0.20, "extreme": 0.10},
    3: {"easy": 0.20, "medium": 0.30, "hard": 0.30, "extreme": 0.20},
    4: {"easy": 0.20, "medium": 0.20, "hard": 0.30, "extreme": 0.30},
    5: {"easy": 0.15, "medium": 0.15, "hard": 0.20, "extreme": 0.50},
}

LEVEL_LABELS = {
    1: "Level 1",
    2: "Level 2",
    3: "Level 3",
    4: "Level 4",
    5: "Level 5",
}

COUNT_BUTTONS = {f"{n} questions": n for n in COUNT_OPTIONS}
COUNT_BUTTONS.update({str(n): n for n in COUNT_OPTIONS})

LEVEL_BUTTONS = {f"Level {n}": n for n in range(1, 6)}
LEVEL_BUTTONS.update({str(n): n for n in range(1, 6)})

_DIFF_ORDER = ("easy", "medium", "hard", "extreme")
_LOCK = threading.Lock()


def utc_today() -> str:
    return datetime.now(timezone.utc).date().isoformat()


def allocate_mix(count: int, level: int) -> dict[str, int]:
    """Largest-remainder allocation so counts sum exactly to `count`."""
    mix = LEVEL_MIXES[level]
    raw = {d: count * mix[d] for d in _DIFF_ORDER}
    alloc = {d: int(raw[d]) for d in _DIFF_ORDER}
    rem = count - sum(alloc.values())
    order = sorted(_DIFF_ORDER, key=lambda d: (raw[d] - alloc[d], mix[d]), reverse=True)
    for i in range(rem):
        alloc[order[i % len(order)]] += 1
    return alloc


def build_difficulty_queue(count: int, level: int, rng: random.Random | None = None) -> list[str]:
    alloc = allocate_mix(count, level)
    queue: list[str] = []
    for diff, n in alloc.items():
        queue.extend([diff] * n)
    (rng or random.Random()).shuffle(queue)
    return queue


def mix_summary(level: int) -> str:
    m = LEVEL_MIXES[level]
    return (
        f"Easy {int(m['easy']*100)}% · "
        f"Medium {int(m['medium']*100)}% · "
        f"Hard {int(m['hard']*100)}% · "
        f"Extreme {int(m['extreme']*100)}%"
    )


def count_menu_text(specialty_label: str, remaining: int) -> str:
    return (
        f"📍 *{specialty_label}* — Short MCQ\n\n"
        f"How many questions do you want to solve?\n"
        f"• 5 · 10 · 15 · 20\n\n"
        f"Today’s remaining for this specialty: *{remaining}/{DAILY_LIMIT}*\n"
        f"_Limit resets tomorrow (UTC)._\n\n"
        f"Tap *Back to features* to return."
    )


def level_menu_text(specialty_label: str, count: int, remaining: int) -> str:
    lines = [
        f"📍 *{specialty_label}* — Short MCQ",
        f"Set size: *{count}* questions (remaining today: *{remaining}*)",
        "",
        "Choose advancement level:",
    ]
    for n in range(1, 6):
        lines.append(f"• *Level {n}* — {mix_summary(n)}")
    lines.extend(["", "Tap *Back to features* to return."])
    return "\n".join(lines)


def session_complete_text(specialty_label: str, session: dict[str, Any], remaining: int) -> str:
    total = int(session.get("count") or 0)
    correct = int(session.get("correct") or 0)
    level = int(session.get("level") or 0)
    pct = int(round(100 * correct / total)) if total else 0
    return (
        f"🏁 *Session complete — {specialty_label}*\n"
        f"Level *{level}* · Score *{correct}/{total}* ({pct}%)\n\n"
        f"Today’s remaining for this specialty: *{remaining}/{DAILY_LIMIT}*\n"
        f"Open *Short MCQ* again for another set, or *Back to features*."
    )


def daily_limit_text(specialty_label: str) -> str:
    return (
        f"⛔ You’ve reached today’s Short MCQ limit for *{specialty_label}* "
        f"(*{DAILY_LIMIT}* questions).\n"
        f"Come back tomorrow for another *{DAILY_LIMIT}*."
    )


class DailyUsageStore:
    """Persisted per-user, per-specialty daily Short MCQ counters."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def _load(self) -> dict:
        if not self.path.exists():
            return {}
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
            return data if isinstance(data, dict) else {}
        except (OSError, json.JSONDecodeError):
            return {}

    def _save(self, data: dict) -> None:
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        tmp.replace(self.path)

    def used(self, user_id: int, specialty_key: str, day: str | None = None) -> int:
        day = day or utc_today()
        with _LOCK:
            data = self._load()
            return int(((data.get(day) or {}).get(str(user_id)) or {}).get(specialty_key) or 0)

    def remaining(self, user_id: int, specialty_key: str, day: str | None = None) -> int:
        return max(0, DAILY_LIMIT - self.used(user_id, specialty_key, day))

    def increment(self, user_id: int, specialty_key: str, amount: int = 1, day: str | None = None) -> int:
        """Increment usage; returns new used count. Caps at DAILY_LIMIT."""
        if amount <= 0:
            return self.used(user_id, specialty_key, day)
        day = day or utc_today()
        with _LOCK:
            data = self._load()
            day_map = data.setdefault(day, {})
            user_map = day_map.setdefault(str(user_id), {})
            current = int(user_map.get(specialty_key) or 0)
            current = min(DAILY_LIMIT, current + amount)
            user_map[specialty_key] = current
            days_sorted = sorted(data.keys())
            for old in days_sorted[:-3]:
                data.pop(old, None)
            self._save(data)
            return current


def allowed_counts(remaining: int) -> list[int]:
    opts = [n for n in COUNT_OPTIONS if n <= remaining]
    if remaining > 0 and remaining not in opts and remaining < min(COUNT_OPTIONS):
        opts = [remaining]
    return opts


def parse_count(text: str) -> int | None:
    t = (text or "").strip().lower()
    if t in COUNT_BUTTONS:
        return COUNT_BUTTONS[t]
    # "5 questions" already in map; also allow "5 question"
    t = t.replace("question", "questions").replace("questionss", "questions")
    return COUNT_BUTTONS.get(t)


def parse_level(text: str) -> int | None:
    t = (text or "").strip()
    if t in LEVEL_BUTTONS:
        return LEVEL_BUTTONS[t]
    return None
