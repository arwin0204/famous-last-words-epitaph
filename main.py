#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

Writes a single-line epitaph (famous last words) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic: the entry is hardcoded.

The program writes ONLY to $MAKEFUN_OUTPUT_DIR (fallback /output).
It never writes into the repository directory, because the grader
runs with a read-only repo.
"""

import os
from pathlib import Path

ENTRY = "Here lies Max. He bet he could hold his breath forever. He won."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    output_path = Path(output_dir) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
