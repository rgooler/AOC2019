#!/usr/bin/env python3

from aoc2019 import Amplifier
import itertools

def part1(code):
    phase_sequence = [0,1,2,3,4]

    max_thrust = 0
    winning_seq = []

    for sequence in itertools.permutations(phase_sequence):
        chall = Amplifier(code=code.copy(), enable_logs=False)
        r = chall.run(list(sequence).copy())
        if r > max_thrust:
            max_thrust = r
            winning_seq = sequence
    print(f"Part 1: {max_thrust} - {winning_seq}")
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
        
