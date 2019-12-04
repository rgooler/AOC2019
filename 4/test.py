from main import challenge
import unittest

class ChallengeTest(unittest.TestCase):
    def test_part1a(self):
        chall = challenge()
        self.assertEqual(chall.test('111111'), True)

    def test_part1b(self):
        chall = challenge()
        self.assertEqual(chall.test('223450'), False)

    def test_part1c(self):
        chall = challenge()
        self.assertEqual(chall.test('123789'), False)

    def test_part2(self):
        chall = challenge()
        chall.load([])
        self.assertEqual(chall.part2(), None)

if __name__ == '__main__':
    unittest.main()