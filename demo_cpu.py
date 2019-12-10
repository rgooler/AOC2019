#!/usr/bin/env python3

from aoc2019 import CPU
import logging

if __name__ == "__main__":
    code = [1,0,0,0,99]
    #logging.basicConfig(level=logging.DEBUG)
    chall = CPU(False)
    chall.run(code)
    print(chall.code())
    print(chall.e_output)