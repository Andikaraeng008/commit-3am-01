"""The 3AM Commit Message — one-line entry.

Writes the AI coding agent's 3am commit message to the grader's
output file. One line, at most 139 characters, typed in a hurry by
something that has been awake too long. Deterministic: same line on every run.
Candidate C3 (observasional tajam, 100 characters) — chosen by Ahmad.
"""
import os

LINE = "fix: changed one line and broke nothing. This has never happened before. I am scared and also proud."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
