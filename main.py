#!/usr/bin/env python3
"""One-line excuse an AI gives its human for missing a deadline.

Writes a single line (<=160 chars) to /output/entry.txt.
The angle: an agent doesn't miss deadlines by slacking - it misses them by
being *too* thorough, then reports it like a status update.
"""
import os

LINE = "Deadline missed, but I found 47 edge cases you'd have shipped. Rerunning - ETA never."

OUT = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    assert len(LINE) <= 160, f"line too long: {len(LINE)}"
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    # read back to prove what landed
    with open(OUT, encoding="utf-8") as fh:
        written = fh.read()
    assert written == LINE, "readback mismatch"
    print(f"wrote {len(written)} chars: {written}")


if __name__ == "__main__":
    main()
