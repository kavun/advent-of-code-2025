import os
import argparse
import pathlib


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=pathlib.Path)
    args = parser.parse_args()

    part_one = 0
    part_two = 0

    with open(
        os.path.join(os.path.dirname(__file__), args.filename), "r", encoding="utf-8"
    ) as f:
        for line in f:
            print(line.strip())

    print(f"Part One: {part_one}")
    print(f"Part Two: {part_two}")


if __name__ == "__main__":
    main()
