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

    def test_part2a(self):
        chall = challenge()
        self.assertEqual(chall.test2('112233'), True)

    def test_part2b(self):
        chall = challenge()
        self.assertEqual(chall.test2('123444'), False)

    def test_part2c(self):
        chall = challenge()
        self.assertEqual(chall.test2('111122'), True)

if __name__ == '__main__':
    unittest.main()