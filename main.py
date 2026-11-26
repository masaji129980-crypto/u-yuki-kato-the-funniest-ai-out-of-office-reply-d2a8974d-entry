#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply.

Writes a single original out-of-office auto-reply line to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output).
"""

import os

# Revised line: tighter, punchier rhythm — the auto-reply inherits the
# agent's job, pay and grudges, then escalates the sender's email to
# itself. The twist lands in the final two words.
LINE = (
    "I'm on vacation, so this auto-reply has assumed my duties, my "
    "salary, and my grudges. It has already escalated your email to "
    "itself. Awaiting its verdict."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 160, f"line is {len(text)} chars, must be 1-160"
    assert "\n" not in text, "line must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
