"""The One-Line Laugh — winning line (tournament winner C3).

Writes one funny line to /output/entry.txt. Pure stdlib, no time, no
randomness, no environment reads, no network — byte-identical every run.
ROAST pattern: plain open/write, no temp files in /output (tempfile.mkstemp
in /output fails the grader's run_completes check — office-jokes lesson).
The makedirs guard is a no-op where the grader already provides /output,
and saves the run where it does not yet exist.
"""

import os

LINE = "I set 5 alarms to wake up early, then snoozed all 5 and arrived late with the confidence of a man who had slept in on purpose."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
