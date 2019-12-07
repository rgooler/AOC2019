
from aoc2019 import Crack
import unittest
import logging
logging.basicConfig(level=logging.CRITICAL)

class Day4(unittest.TestCase):
    def test_part1a(self):
        chall = Crack()
        self.assertEqual(chall.test('111111'), True)

    def test_part1b(self):
        chall = Crack()
        self.assertEqual(chall.test('223450'), False)

    def test_part1c(self):
        chall = Crack()
        self.assertEqual(chall.test('123789'), False)

    def test_part2a(self):
        chall = Crack()
        self.assertEqual(chall.test2('112233'), True)

    def test_part2b(self):
        chall = Crack()
        self.assertEqual(chall.test2('123444'), False)

    def test_part2c(self):
        chall = Crack()
        self.assertEqual(chall.test2('111122'), True)

if __name__ == '__main__':
    unittest.main()