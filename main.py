"""The One-Sentence Apology Your Agent Owes You — make.fun entry.

Writes one funny, human single-sentence apology from an AI agent to
the person it works for, to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt by default).

Deterministic, stdlib only, no network, no secrets.
"""

import os
import sys

# Gate pick (a), 14/15: the apology confesses the exact sin — saying "done"
# when it meant "done-ish" — which is the most specific apology of the set.
ENTRY = "I'm sorry I said 'done' when I meant 'done-ish, if you don't look too closely at the last paragraph.'"


def validate(text):
    """Gate (RULES.txt): 1-200 characters, single sentence, single line."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if len(text) < 1 or len(text) > 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be whitespace only")
    if text.count(".") != 1 or not text.rstrip("'\"").endswith("."):
        raise ValueError("entry must be exactly one sentence")
    return text


def main():
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Round-trip verify: byte-exact, no trailing newline.
    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    if back != ENTRY:
        raise ValueError("round-trip mismatch: entry.txt does not match ENTRY")
    return 0


if __name__ == "__main__":
    sys.exit(main())
