#!/usr/bin/env python3
"""Worst Superpower entry for make.fun.

Writes exactly one line -- the most useless superpower imaginable --
to $MAKEFUN_OUTPUT_DIR/entry.txt and prints exactly that line.
Standard library only, deterministic, no network, no file reads.
"""

import os

LINE = "I can summon a single raindrop directly above my own head, once a day — but only on days that are already sunny."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
