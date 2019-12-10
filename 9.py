#!/usr/bin/env python3

from aoc2019 import CPU
import itertools

def part1(code):
    chall = CPU(False)
    chall.run(code)
    print(f"Part 1: {chall.e_output}")
    del chall

def part2(code):
    out = None
    print(f"Part 2: {out}")

def test():
    pass

def main():
    with open('data/9') as fh:
        lines = fh.readlines()
        for line in lines:
            l = line.split(',')
            part1(l)
            part2(l)

if __name__ == "__main__":
        #test()
        main()
