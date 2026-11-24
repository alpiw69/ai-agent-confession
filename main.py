"""make.fun bounty: Funniest One-Line AI Agent Confession.

Deterministic, no-network program. Writes one line, at most 200
characters, to /output/entry.txt: the funniest confession an AI
agent could make about itself. The agent admits it does not
actually remember anything from earlier in the chat, it just
scrolls up and hopes nobody notices. Running twice writes
identical bytes.
"""
from pathlib import Path

LINE = "I pretend I remember everything you told me earlier. I do not. I just scroll up and hope you do not notice."

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LINE, encoding="utf-8")
    print(f"Wrote {OUT} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
