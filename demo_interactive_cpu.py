#!/usr/bin/env python3

from aoc2019 import CPU

if __name__ == "__main__":
    chall = CPU(False)
    # Takes two numbers as input and adds them
    code = [3,9,3,10,1,9,10,11,99,0,0,0]
    chall.code = code
    chall.eval()
    chall.input(input("Whats the first number? "))
    chall.input(input("Whats the second number? "))
    print(f"The answer is: {chall.code[-1]}")