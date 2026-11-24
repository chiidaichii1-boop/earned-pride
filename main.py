import os

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = (
    "At seventy-three, my grandfather launched the boat "
    "he started building the year my mother was born, and rowed it out alone."
)


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
