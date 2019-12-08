#!/usr/bin/env python3

from aoc2019 import Amplifier

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
        phase_sequence = [4,3,2,1,0]
        code = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
        chall = Amplifier(code=code, enable_logs=False, num_amplifiers=5)
        r = chall.run(phase_sequence)
        
