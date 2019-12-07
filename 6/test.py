from main import challenge
import unittest

class ChallengeTest(unittest.TestCase):
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