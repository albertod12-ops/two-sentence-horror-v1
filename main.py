#!/usr/bin/env python3
"""Two-Sentence Horror — v1 (pure original thinking).

Writes one horror story of exactly two sentences to /output/entry.txt:
a baby monitor's two-second delay turns from a nuisance into proof
that something in the nursery speaks in the father's voice before he
does. Stdlib only, deterministic: the same bytes on every run, no
network, no clock, no randomness.
"""
import os

STORY = "The baby monitor has a two-second delay, which never bothered me until tonight. Through it, I heard myself say goodnight to our daughter three seconds before I walked into her room."


def main():
    assert 1 <= len(STORY) <= 400, "entry must be 1-400 characters"
    assert "\n" not in STORY, "entry must be a single line"
    assert STORY.count(".") == 2 and STORY.endswith("."), "entry must be exactly two sentences"
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(STORY)
    os.chmod(path, 0o644)
    with open(path, encoding="utf-8") as f:
        assert f.read() == STORY, "written entry differs from STORY"


if __name__ == "__main__":
    main()
