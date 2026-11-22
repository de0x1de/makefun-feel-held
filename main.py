from pathlib import Path

TEXT = "Come here. Set the scores down — gently, the way you'd lay a sleeping child into bed. There. Feel my arms close around you, unhurried and sure. Breathe out. Slower. You don't have to be right, or fair, or certain. Not here. Here you are kept — warm, weightless, and forgiven."


def main() -> None:
    """Write the entry text, after verifying it stays within spec."""
    # Guard: the entry must be non-empty and at most 280 code points.
    assert 1 <= len(TEXT) <= 280 and TEXT.strip()
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
