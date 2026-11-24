"""One Line, One Chill — entry runner.

Reads the single horror line from entry.txt, checks it against the
bounty's own gate (one line, 1 to 200 characters, not blank), prints it,
and drops a copy at /output/entry.txt where the sealed scorer looks for it.
"""

from pathlib import Path

ENTRY_FILE = Path(__file__).with_name("entry.txt")
OUTPUT_FILE = Path("/output/entry.txt")
MAX_CHARS = 200


def load_line():
    raw = ENTRY_FILE.read_text(encoding="utf-8")
    lines = [part.strip() for part in raw.splitlines() if part.strip()]
    if len(lines) != 1:
        raise SystemExit("entry.txt must hold exactly one line")
    text = lines[0]
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit("entry must be 1 to 200 characters")
    return text


def deliver(line):
    print(line)
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(line + "\n", encoding="utf-8")


def main():
    deliver(load_line())


if __name__ == "__main__":
    main()
