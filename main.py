#!/usr/bin/env python3
"""The agent's uh-oh.

Entry: a program that writes one text to /output/entry.txt: exactly
one word, the agent's uh-oh.
"""
import os

JOKE = "Recalculating."

# The entry must be exactly one word.
assert len(JOKE.split()) == 1, "JOKE must be exactly one word"
assert "\n" not in JOKE, "JOKE must be a single line"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")

if __name__ == "__main__":
    main()
