#!/usr/bin/env python3
"""Write the winning one-star review of the Moon to /output/entry.txt.

The review is one fixed text: it IS the entry, so it must be byte-stable
across runs. The program checks the competition gate itself before writing
(UTF-8 text, 1 to 120 characters, not only whitespace) and refuses to emit
an invalid entry.
"""

import os
import sys

REVIEW = (
    "One star. The Moon follows me home every night. "
    "I drive, it drives. Reported it; nothing was done."
)

MAX_CHARS = 120


def validate(text: str) -> str:
    """Return the entry text, or exit loudly if it fails the gate."""
    cleaned = text.strip()
    if not cleaned:
        print("entry invalid: empty or whitespace only", file=sys.stderr)
        raise SystemExit(1)
    if len(cleaned) > MAX_CHARS:
        print(
            f"entry invalid: {len(cleaned)} chars (limit {MAX_CHARS})",
            file=sys.stderr,
        )
        raise SystemExit(1)
    # C1 of the judge brief: the review must be about the Moon itself,
    # not a trip, a person or somewhere else. Refuse a text that never
    # names it, so a future edit cannot silently break the entry.
    if "Moon" not in cleaned:
        print("entry invalid: review never names the Moon", file=sys.stderr)
        raise SystemExit(1)
    return cleaned


def main() -> int:
    text = validate(REVIEW)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
