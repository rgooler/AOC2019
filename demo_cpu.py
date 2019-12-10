#!/usr/bin/env python3

from aoc2019 import CPU
import logging

if __name__ == "__main__":
    #logging.basicConfig(level=logging.DEBUG)
    chall = CPU(True)
    code = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    chall.run(code.copy())
    print(chall.code)
    print(chall.e_output)