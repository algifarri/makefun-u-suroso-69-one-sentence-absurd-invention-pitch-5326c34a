#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single-sentence pitch for a ridiculous invention that fixes a
tiny everyday annoyance to /output/entry.txt.

Deterministic, standard library only, no network access. The pitch is a
single sentence of 148 characters, inside the gate's 1-220 character limit.
"""

import os

PITCH = (
    "The Hostage Washer is a washing machine that returns all your laundry "
    "except one sock, which it keeps hostage until you finally clean the lint trap."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
