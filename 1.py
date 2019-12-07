#!/usr/bin/env python3

from aoc2019 import Rocket

def main():
    chall = Rocket()
    with open('data/1') as fh:
        lines = fh.readlines()
        weight = 0
        totalweight = 0
        for line in lines:
            # Part 1
            weight = weight + chall.calc_fuel_weight(line)
            # Part 2            
            totalweight = totalweight + chall.calc_fuel_weight_recursive(line)
        
        print(f"Part 1: {weight}")
        print(f"Part 2: {totalweight}")

if __name__ == "__main__":
    main()
