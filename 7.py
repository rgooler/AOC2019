#!/usr/bin/env python3

from aoc2019 import CPU

def part1(code):
    chall = CPU(False)
    chall.run(l, 1)
    print(f"Part 1: {chall.e_output}")
    pass

def part2(code):
    pass

def main():
    with open('data/7') as fh:
        lines = fh.readlines()
        for line in lines:
            l = line.split(',')
            part1(l)
            part2(l)

if __name__ == "__main__":
    main()
