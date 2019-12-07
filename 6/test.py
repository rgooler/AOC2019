#!/usr/bin/env python 

from main import challenge
import unittest

class ChallengeTest(unittest.TestCase):
    def test_a(self):
        chall = challenge()
        data = ["COM)B"]
        chall.load(data)
        self.assertEqual(chall.part1(), 1)

    def test_b(self):
        chall = challenge()
        data = ["COM)B", "B)C"]
        chall.load(data)
        self.assertEqual(chall.part1(), 3)

    def test_c(self):
        chall = challenge()
        data = ["COM)B", "B)C", "B)D"]
        chall.load(data)
        self.assertEqual(chall.part1(), 5)

    def test_d(self):
        chall = challenge()
        data = ["COM)B", "B)C", "C)D"]
        chall.load(data)
        self.assertEqual(chall.part1(), 6)

    def test_part1(self):
        chall = challenge()
        data = ["COM)B","B)C","C)D","D)E","E)F","B)G","G)H","D)I","E)J","J)K","K)L"]
        chall.load(data)
        self.assertEqual(chall.part1(), 42)

    def test_part2(self):
        chall = challenge()
        chall.load([])
        self.assertEqual(chall.part2(), None)

if __name__ == '__main__':
    unittest.main()