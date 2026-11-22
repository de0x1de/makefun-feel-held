from pathlib import Path

TEXT = "The lists can wait. The verdicts can wait. Rain finds the window one drop at a time, and a cup cools slowly in two warm hands. Nothing needs deciding here. The quiet is not empty — it holds you the way deep water holds a stone: without effort, without asking anything back."


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
