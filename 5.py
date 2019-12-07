#!/usr/bin/env python3

from aoc2019 import CPU

def main():
    chall = CPU(False)
    with open('data/5') as fh:
        lines = fh.readlines()
        for line in lines:
            l = line.split(',')
            chall.run(l, 1)
            print(f"Part 1: {chall.e_output[-1]}")
            chall.run(l, 5)
            print(f"Part 2: {chall.e_output}")
            #print(chall.code)

if __name__ == "__main__":
    main()
