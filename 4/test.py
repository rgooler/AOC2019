from main import challenge
import unittest

class ChallengeTest(unittest.TestCase):
    def test_part1(self):
        chall = challenge()
        chall.load([])
        self.assertEqual(chall.part1(), None)

    def test_part2(self):
        chall = challenge()
        chall.load([])
        self.assertEqual(chall.part2(), None)

if __name__ == '__main__':
    unittest.main()