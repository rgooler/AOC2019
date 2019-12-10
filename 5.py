#!/usr/bin/env python3

from aoc2019 import CPU

def part1(code):
    chall = CPU(False)
    chall.run(code)
    chall.input(1)
    print(f"Part 1: {chall.e_output[-1]}")
    del chall

def part2(code):
    chall = CPU(False)
    chall.run(code)
    chall.input(5)
    print(f"Part 2: {chall.e_output[-1]}")
    del chall

def main():
    with open('data/5') as fh:
        lines = fh.readlines()
        for line in lines:
            l = line.split(',')
        
        part1(l.copy())
        part2(l.copy())


if __name__ == "__main__":
    main()
