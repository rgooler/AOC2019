#!/usr/bin/env python3

from aoc2019 import CPU

def main():
    with open('data/2') as fh:
        lines = fh.readlines()
        for line in lines:
            code = line.split(',')
            cpu = CPU(False)
            cpu.run(code.copy())
            print(f"Part 1: {cpu.code[0]}")

            for a in range(0, 99):
                for b in range(0, 99):
                    c = code.copy()
                    c[1] = a
                    c[2] = b
                    cpu.run(c)
                    x = cpu.code[0]
                    if x == 19690720:
                        val = 100 * a + b
                        print(f"Part 2: {val} = {a},{b}")
                        return

if __name__ == "__main__":
    main()
