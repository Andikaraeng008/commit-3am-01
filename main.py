"""The 3AM Commit Message — one-line entry.

Writes the AI coding agent's 3am commit message to the grader's
output file. One line, at most 139 characters, typed in a hurry by
something that has been awake too long. Deterministic: same line on every run.
Candidate C1 (dark, 94 characters) — chosen by Ahmad.
"""
import os

LINE = "fix: removed the bug and the feature it lived in. The tests pass now. So does my will to live."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
