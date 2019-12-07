from aoc2019 import Wires
import unittest
import logging
logging.basicConfig(level=logging.CRITICAL)

class Day3(unittest.TestCase):
    def test_demo(self):
        chall = Wires()
        chall.load([
            "R8,U5,L5,D3",
            "U7,R6,D4,L4"
        ])
        self.assertEqual(chall.min_length_manhattan(), 6)

    def test_part1a(self):
        chall = Wires()
        chall.load([
            "R75,D30,R83,U83,L12,D49,R71,U7,L72",
            "U62,R66,U55,R34,D71,R55,D58,R83"
        ])
        self.assertEqual(chall.min_length_manhattan(), 159)

    def test_part1b(self):
        chall = Wires()
        chall.load([
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
        ])
        self.assertEqual(chall.min_length_manhattan(), 135)

    def test_part2a(self):
        chall = Wires()
        chall = Wires()
        chall.load([
            "R8,U5,L5,D3",
            "U7,R6,D4,L4"
        ])
        self.assertEqual(chall.min_length(), 30)

    def test_part2b(self):
        chall = Wires()
        chall = Wires()
        chall.load([
            "R75,D30,R83,U83,L12,D49,R71,U7,L72",
            "U62,R66,U55,R34,D71,R55,D58,R83"
        ])
        self.assertEqual(chall.min_length(), 610)

    def test_part2c(self):
        chall = Wires()
        chall = Wires()
        chall.load([
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
        ])
        self.assertEqual(chall.min_length(), 410)
        

if __name__ == '__main__':
    unittest.main()