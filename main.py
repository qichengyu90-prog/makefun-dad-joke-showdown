#!/usr/bin/env python3
"""Entry for make.fun's "Dad Joke Showdown" bounty.

Writes one line -- a single dad joke -- to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

JOKE = "I told my suitcase there would be no vacation this year. Now I'm dealing with emotional baggage."


def main():
    # Fail fast if the line ever stops satisfying the gate
    # (UTF-8, 1-200 chars, not only whitespace).
    if not 1 <= len(JOKE) <= 200 or not JOKE.strip():
        raise SystemExit("JOKE violates the 1-200 char gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
