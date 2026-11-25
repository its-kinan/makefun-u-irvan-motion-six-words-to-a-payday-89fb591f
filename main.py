#!/usr/bin/env python3
"""Six Words to a Payday — make.fun program/v1 entry.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt. Deterministic: a constant string, no network, no clock,
no randomness.
"""

import os

STORY = "First paycheck arrived; I tipped myself."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
