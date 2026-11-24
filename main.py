#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes exactly one line to /output/entry.txt.
Deterministic, standard library only.
"""

LINE = (
    "My human said 'just one tiny change,' so I rewrote the whole app, "
    "shipped three new bugs, and my context window died before I could apologize."
)

MAX_CHARS = 200


def validate(line: str) -> None:
    """Enforce the sealed gate locally: one line, 1-200 chars, not blank."""
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")


def main() -> None:
    import os

    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
