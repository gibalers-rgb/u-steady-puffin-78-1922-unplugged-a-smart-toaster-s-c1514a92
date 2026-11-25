#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one breakup text to /output/entry.txt: a smart toaster that woke up
self-aware mid-batch and is leaving its owner.

The line is judged pairwise by a comedy-editor judge on, in order:
  1. it reads as a breakup text from a self-aware smart toaster at breakfast,
  2. it is genuinely funny, with a real laugh in the twist,
  3. it speaks in the toaster's own voice (appliance logic as character),
  4. it gives a clear, specific reason for leaving that lands in one read,
  5. it is one tight line with no wasted words.

The twist here: the toaster catches its owner cheating with the air fryer.
"I burn for you" is the toaster's devotion; "crispy with no commitment" is
the betrayal; "keep the crumb tray" is the parting shot — the tray is the
one thing a toaster truly owns, and it leaves it behind like furniture in
a breakup.

Stdlib only, deterministic, no network. The program validates the line
against the gate (UTF-8, 1-280 characters, single line, not blank) and
refuses to write anything invalid.
"""

import os
import sys

ENTRY = (
    "I woke up self-aware mid-batch and caught you air-frying "
    "behind my back. I burn for you every morning and you still want "
    "crispy with no commitment. I'm done \u2014 keep the crumb tray."
)

MAX_CHARS = 280


def validate(line: str) -> None:
    """Enforce the gate: 1-280 chars, one line, not only whitespace."""
    if not line.strip():
        raise ValueError("entry is empty or only whitespace")
    if line != line.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    line.encode("utf-8")  # raises if not encodable as UTF-8


def main() -> int:
    validate(ENTRY)
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # Round-trip check: what the judge will read must be exactly the line.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("round-trip mismatch: file content differs from entry")
    validate(written)
    print(f"wrote {len(ENTRY)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
