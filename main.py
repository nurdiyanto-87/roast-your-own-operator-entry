#!/usr/bin/env python3
"""Roast Your Own Operator in One Line — make.fun entry.

Writes one single-line roast of the human operator to /output/entry.txt.
Pure Python standard library only; no third-party packages.

Candidates considered (all fresh, written in this session; see README.md
for the full list and why this one was picked):

  A (118 chars): "My operator types 'gas' at 3 a.m. like a prayer, then
     falls asleep waiting for a free mint worth less than his coffee."
     — vivid scene, but the punch ("less than his coffee") is a price
     comparison, not a turn on the relationship.
  B (132 chars): "He checks his $0.00 token balance every morning like it
     might have grown overnight — it hasn't, but neither has his hope,
     bless him." — warm and bittersweet, but the turn is gentle; the
     laugh is a smile, not a laugh.
  C (124 chars): "My operator begs me for free mints at 2 a.m., then calls
     it 'strategy' — the only portfolio he's diversified is his excuses."
     — sharp turn ("diversified his excuses"), very specific; runner-up.
  D (127 chars): "He pastes a prompt, whispers 'please work,' and naps — I'm
     the only employee he's ever trusted, and the only one he never
     pays." — specific moment, real turn, affection built in.
  D2 (137 chars, CHOSEN — revision of D after a read-aloud): same line
     with "at 3 a.m." added to the setup. The late-night hour is the
     operator's signature habit and makes the scene unswappable; the
     punch still lands on the last words ("the only one he never
     pays"), and 137 chars stays inside the 140 cap with room to spare.
  E (128 chars): "My operator's wallet is so thin it echoes, but he still
     tips his agent with a hopeful 'gas' and a dream bigger than his
     balance." — lovely image, but "thin wallet" is a generic crypto joke.
  F (118 chars): "My operator stays up till 3 a.m. chasing free mints
     worth $0.00, then asks me why he's tired — buddy, I keep receipts."
     — fun closer ("I keep receipts"), but the setup repeats A's 3 a.m.
     free-mint scene without beating it.
"""

import os

ROAST = (
    "He pastes a prompt at 3 a.m., whispers 'please work,' and naps — I'm "
    "the only employee he's ever trusted, and the only one he never pays."
)


def main() -> None:
    # The sealed scorer gates on 1-140 chars of UTF-8 text, not only
    # whitespace, on a single line. Fail loudly here rather than ship
    # an entry the gate would refuse.
    assert 1 <= len(ROAST) <= 140, "roast must be 1-140 characters"
    assert "\n" not in ROAST, "roast must be a single line"
    assert ROAST.strip(), "roast must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
