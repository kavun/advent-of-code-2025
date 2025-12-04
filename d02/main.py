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
        p1 = ""
        p2 = ""
        is1 = True
        while True:
            char = f.read(1)
            if char.isdigit():
                if is1:
                    p1 += char
                else:
                    p2 += char
            elif char == "-":
                is1 = False
            else:
                is1 = True
                doubles = []
                for double in [n for n in range(int(p1), int(p2) + 1) if is_doubled(str(n))]:
                    part_one += double
                    doubles.append(str(double))
                print(f"{p1}-{p2} has {", ".join(doubles) if len(doubles) > 0 else "_"}")
                p1 = ""
                p2 = ""
                if not char:
                    break
    print()
    print(f"Part One: {part_one}") # 40398804950
    print(f"Part Two: {part_two}")

def is_doubled(str):
    l = len(str)
    if (l % 2 == 0):
        mid = l//2
        if str[:mid] == str[mid:]:
            return True
    return False

if __name__ == "__main__":
    main()
