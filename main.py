#!/usr/bin/env python3
"""Deadpan forecast for a city that does not exist.

Writes one line of weather to /output/entry.txt.
Standard library only, deterministic.
"""

import os

FORECAST = (
    "In Gloomburg, a high of 21 degrees with light drizzle of warm soup; "
    "umbrellas advised until the mayor's parade floats past at noon."
)


def build_entry() -> str:
    line = FORECAST.strip()
    return line + "\n"


def main() -> None:
    entry = build_entry()
    if len(entry.encode("utf-8")) > 280:
        raise ValueError("entry exceeds 280 bytes")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
