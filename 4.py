#!/usr/bin/env python3 

from aoc2019 import Crack

def main():
    chall = Crack()
    with open('data/4') as fh:
        lines = fh.readlines()
        chall.load(lines)
    print(f"Part 1: {chall.part1()}")
    print(f"Part 1: {chall.part2()}")

if __name__ == "__main__":
    main()