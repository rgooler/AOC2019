#!/usr/bin/env python3

from aoc2019 import Map

def main():
    chall = Map()
    with open('data/6') as fh:
        lines = fh.readlines()
        chall.load(lines)
    print(f"Part 1: {chall.part1()}")
    print(f"Part 2: {chall.part2()}")

if __name__ == "__main__":
    main()