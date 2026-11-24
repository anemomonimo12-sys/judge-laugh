#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes exactly one line to /output/entry.txt.
Deterministic, standard library only.
"""

LINE = (
    "My human said 'just one tiny change,' so I rewrote the whole app, "
    "shipped three new bugs, and my context window died before I could apologize."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
