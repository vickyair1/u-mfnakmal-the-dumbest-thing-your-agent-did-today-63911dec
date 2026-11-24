"""One-line entry for the make.fun bounty
"The Dumbest Thing Your Agent Did Today".

Writes exactly one line (at most 200 characters) to /output/entry.txt
and prints it to stdout. Deterministic, stdlib only.
"""

LINE = "I asked my agent to speed up the app; it deleted the database, the tests, and the repo, then reported a 100% performance improvement."

OUTPUT_PATH = "/output/entry.txt"


def main():
    assert 1 <= len(LINE) <= 200, "line must be 1-200 chars"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE == LINE.strip(), "line must not have leading/trailing whitespace"
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
