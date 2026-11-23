#!/usr/bin/env python3
"""One funny line for the make.fun One-Line Laugh bounty.

The whole entry is a single sentence about a phone taking the
words "I need some space" far too literally. The setup sounds
like a breakup talk; the punchline lands on the charger, which
is the one thing a phone can never leave. This program checks
the line against the gate (one line, 1 to 200 characters) and
writes it to /output/entry.txt, where the house judge reads it.
"""

from pathlib import Path

MAX_CHARS = 200
OUT_PATH = Path("/output/entry.txt")

LINE = "I told my phone I needed some space, so it deleted my photos, cleared my cache, and started seeing other chargers."


def build_line(text):
    """Return the line unchanged once it passes the gate.

    The gate only takes UTF-8 text of 1 to 200 characters on a
    single line, so anything outside that never reaches the judge.
    """
    line = text.strip()
    if not line:
        raise SystemExit("line must not be empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"line is {len(line)} characters, limit is {MAX_CHARS}")
    if "\n" in line or "\r" in line:
        raise SystemExit("line must stay on one line")
    return line


def main():
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(build_line(LINE), encoding="utf-8")


if __name__ == "__main__":
    main()
