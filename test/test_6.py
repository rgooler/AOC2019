import unittest
import logging
logging.basicConfig(level=logging.CRITICAL)
from aoc2019 import Map

class Day6(unittest.TestCase):
    def test_part1(self):
        chall = Map()
        data = ["COM)B","B)C","C)D","D)E","E)F","B)G","G)H","D)I","E)J","J)K","K)L"]
        chall.load(data)
        self.assertEqual(chall.part1(), 42)

    def test_part2(self):
        chall = Map()
        data = ["YOU)B","B)C","C)D","D)E","E)F","B)G","G)H","D)I","E)J","J)K","K)SAN"]
        chall.load(data)
        self.assertEqual(chall.part2(), 7)

if __name__ == '__main__':
    unittest.main()