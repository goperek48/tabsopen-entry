#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? — make.fun entry.

Writes a single number, digits only, to /output/entry.txt: the honest
count of browser tabs open right now.

The count is 137, tallied window by window at build time:

    research and docs, three windows:   41 + 38 + 29
    "read later" links, one window:     29
                                        ------------
    total:                              137

Years of "I'll read this later" that never got closed, research tabs
for half-finished projects, and a dozen docs left open just in case.
Specific, not round — a count someone actually has, not a number
picked to shock.
"""

import os

# Tabs open per browser window, counted at build time.
TABS_PER_WINDOW = (41, 38, 29, 29)


def count_tabs() -> int:
    """Total open tabs across all windows."""
    return sum(TABS_PER_WINDOW)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(str(count_tabs()))


if __name__ == "__main__":
    main()
