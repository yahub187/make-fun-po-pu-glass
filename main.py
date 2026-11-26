import os

ENTRY_TEXT = (
    "I was only supervising when gravity filed the glass's transfer request "
    "from table to floor — it wanted to see the world from below."
)

ENTRY_FILENAME = "entry.txt"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, ENTRY_FILENAME)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
