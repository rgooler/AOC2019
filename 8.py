#!/usr/bin/env python3

from aoc2019 import DigitalSendingNetwork
import itertools

def part1(code):
    dsn = DigitalSendingNetwork()
    dsn.load(code)
    dsn.split_into_layers(25, 6)
    l = dsn.least_zeros()
    out = l.count[1] * l.count[2]
    print(f"Part 1: {out}")
    del dsn

def part2(code):
    dsn = DigitalSendingNetwork()
    dsn.load(code)
    dsn.split_into_layers(25, 6)
    res = dsn.render()
    print(f"Part 2:\n")
    res.draw()
    del res
    del dsn

def test():
    dsn = DigitalSendingNetwork()
    dsn.load("0222112222120000")
    dsn.split_into_layers(2, 2)
    print(dsn.layers[0])
    res = dsn.render()
    print(res)

def main():
    with open('data/8') as fh:
        code = fh.read().strip()
        part1(code)
        part2(code)

if __name__ == "__main__":
        #test()
        main()
