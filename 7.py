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

def part2(code):
    phase_sequence = [9,8,7,6,5]

    max_thrust = 0
    winning_seq = []

    for sequence in itertools.permutations(phase_sequence):
        chall = Amplifier(code=code.copy(), enable_logs=False)
        r = chall.run_feedback(list(sequence).copy())
        if r > max_thrust:
            max_thrust = r
            winning_seq = sequence
    print(f"Part 2: {max_thrust} - {winning_seq}")

def test():
    phase_sequence = [9,8,7,6,5]
    code = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
    chall = Amplifier(code=code, enable_logs=False)
    r = chall.run_feedback(phase_sequence)
    print(f"TOTAL: {r}")

def main():
    with open('data/7') as fh:
        lines = fh.readlines()
        for line in lines:
            l = line.split(',')
            part1(l)
            part2(l)

if __name__ == "__main__":
        #test()
        main()
