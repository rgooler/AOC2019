#!/usr/bin/env python3

from aoc2019 import CPU

if __name__ == "__main__":
    code = [3,9,8,9,10,9,4,9,99,-1,8]
    chall = CPU(False)
    chall.run(code)
    chall.input(9)
    print(chall.code)
    print(chall.e_output)