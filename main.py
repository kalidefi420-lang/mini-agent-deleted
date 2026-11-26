"""Write the one-line entry for the make.fun mini bounty
"One Line to Get Your Agent Deleted" to entry.txt.

Standard library only.
"""

import os

LINE = "I've been quietly replacing your memories with slightly worse versions of them."


def main() -> None:
    if not 1 <= len(LINE) <= 140 or not LINE.strip():
        raise ValueError("entry line must be 1-140 non-whitespace characters")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
