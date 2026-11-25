#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph — one tombstone line of at most
150 characters. Writes the epitaph verbatim to entry.txt.

A judge model reads entries two at a time and keeps the funnier line, so the
line is built to land on its own: a man who finally escapes the group chat,
takes the Wi-Fi password to his grave, and leaves three hundred messages on
read — with a "do not disturb" he finally means. The joke stacks three small
betrayals (exit, theft, silence) and ends on the one boundary he never kept
while alive.

Deterministic, stdlib only, no network, no randomness.
"""

import os
from pathlib import Path

EPITAPH = "Here lies Sam. He finally left the group chat, took the Wi-Fi password to his grave, and left 300 messages on read. Do not disturb \u2014 he means it."

MAX_CHARS = 150


def main() -> None:
    assert 1 <= len(EPITAPH) <= MAX_CHARS, f"line is {len(EPITAPH)} chars (max {MAX_CHARS})"
    assert "\n" not in EPITAPH, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(EPITAPH, encoding="utf-8")
    print(f"wrote {len(EPITAPH)} characters to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
