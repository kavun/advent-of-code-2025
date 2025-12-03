import os
import argparse
import pathlib


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=pathlib.Path)
    args = parser.parse_args()

    pos = 50
    tick_pos = 50
    part_one = 0
    part_two = 0

    with open(
        os.path.join(os.path.dirname(__file__), args.filename), "r", encoding="utf-8"
    ) as f:
        for line in f:
            dir = -1 if line[0] == "L" else 1
            len = dir * int(line[1:])
            pos += len
            pos = pos % 100

            if pos == 0:
                part_one += 1

            for tick in [
                x for x in range(tick_pos, tick_pos + len + dir, dir) if x != tick_pos
            ]:
                tick_pos = tick
                if tick_pos % 100 == 0:
                    part_two += 1

            tick_pos = tick_pos % 100

    print(f"Part One: {part_one}")
    print(f"Part Two: {part_two}")


if __name__ == "__main__":
    main()
