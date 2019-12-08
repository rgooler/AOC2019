from aoc2019 import Wires


def main():
    chall = Wires()
    with open('data/3') as fh:
        lines = fh.readlines()
        chall.load(lines)
    print(f"Part 1: {chall.min_length_manhattan()}")
    print(f"Part 1: {chall.min_length()}")

if __name__ == "__main__":
    main()
