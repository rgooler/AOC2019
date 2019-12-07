from aoc2019 import *
import unittest

class Day1(unittest.TestCase):
    def test_mass_12(self):
        chall = Rocket()
        self.assertEqual(chall.calc_fuel_weight(12), 2)

    def test_mass_14(self):
        chall = Rocket()
        self.assertEqual(chall.calc_fuel_weight(14), 2)

    def test_mass_1969(self):
        chall = Rocket()
        self.assertEqual(chall.calc_fuel_weight(1969), 654)

    def test_mass_100756(self):
        chall = Rocket()
        self.assertEqual(chall.calc_fuel_weight(100756), 33583)

    def test_mass2_12(self):
        chall = Rocket()
        self.assertEqual(chall.calc_fuel_weight_recursive(12), 2)

    def test_mass2_1969(self):
        chall = Rocket()
        self.assertEqual(chall.calc_fuel_weight_recursive(1969), 966)

    def test_mass2_100756(self):
        chall = Rocket()
        self.assertEqual(chall.calc_fuel_weight_recursive(100756), 50346)

if __name__ == '__main__':
    unittest.main()