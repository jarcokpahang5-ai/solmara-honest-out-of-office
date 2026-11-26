#!/usr/bin/env python3
"""One brutally honest but still polite out-of-office auto-reply for make.fun.

Writes a single out-of-office reply to /output/entry.txt. Pure Python 3.13
standard library, deterministic, no network access.
"""

import os

MAX_LINE_LENGTH = 200

ENTRY_LINE = (
    "I'm away on annual leave, happily ignoring an inbox of 400 unread "
    "emails that will still be waiting when I return. Thank you for your "
    "patience — I'll reply soon."
)


def checked_line() -> str:
    """Return the reply, refusing anything the gate would reject."""
    line = ENTRY_LINE.strip()
    if not line:
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if len(line) > MAX_LINE_LENGTH:
        raise ValueError(
            f"entry line is {len(line)} characters, over the "
            f"{MAX_LINE_LENGTH} character limit"
        )
    return line


def main() -> None:
    line = checked_line()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


if __name__ == "__main__":
    main()
