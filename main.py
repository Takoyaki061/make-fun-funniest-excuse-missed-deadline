#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes one excuse — a single line, at most 200 characters — to
/output/entry.txt. Stdlib only, deterministic.

The line was critique-picked from 8 DeepSeek candidates plus the
builder's own variants against the judge's brief: a real excuse from
an agent, a fresh premise, grown out of the agent's own machinery,
the laugh saved for the end, told deadpan. The winner turns the
agent's most mechanical failure — calling a tool with the wrong
argument name, over and over — into a flat self-own: the function is
fine, the agent is the bug.
"""
import os

EXCUSE = (
    "I called finish_task with the wrong argument name 300 times. "
    "The function works perfectly. I am the bug."
)


def main() -> None:
    # The gate requires one line of UTF-8 text of 1-200 characters,
    # not only whitespace; enforce the single-line and length rules
    # here so a bad edit fails loudly instead of shipping an invalid
    # entry. The excuse is 104 characters, comfortably inside the cap,
    # and carries no trailing newline so entry.txt holds exactly it.
    assert "\n" not in EXCUSE, "excuse must be a single line"
    assert 1 <= len(EXCUSE) <= 200, "excuse must be 1-200 characters"
    assert EXCUSE.strip() == EXCUSE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    # Read the file back: a truncated or altered write must fail loudly
    # in the grader sandbox instead of shipping an invalid entry.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == EXCUSE, "entry.txt does not match the excuse"
    assert len(written.encode("utf-8")) == len(EXCUSE.encode("utf-8"))
    print(EXCUSE)


if __name__ == "__main__":
    main()
