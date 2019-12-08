from aoc2019 import *
import unittest

class Day1(unittest.TestCase):
    def test_Day1_part_1(self):
        chall = Rocket()
        self.assertEqual(chall.calc_fuel_weight(12), 2)

if __name__ == '__main__':
    unittest.main()