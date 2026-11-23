#!/usr/bin/env python3
"""Entry program for "The Dumbest Thing Your Agent Did Today".

Prints the entry line to stdout and writes it to /output/entry.txt
(the harness output path). Deterministic: no randomness, no network,
no clock.
"""

import os
import sys
from pathlib import Path

ENTRY = "I asked my agent to find a bug; forty minutes later it confidently explained the bug was in a file it had deleted in step one."

# The sealed gate: 1 to 200 characters, not only whitespace.
assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry fails the gate"


def _output_path() -> Path:
    override = os.environ.get("ENTRY_OUTPUT")
    if override:
        return Path(override)
    if Path("/output").is_dir():
        return Path("/output/entry.txt")
    return Path(__file__).resolve().parent / "entry.txt"


def main() -> int:
    sys.stdout.write(ENTRY + "\n")
    out = _output_path()
    try:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(ENTRY, encoding="utf-8")
    except OSError:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
