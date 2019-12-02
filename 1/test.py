from main import challenge
import unittest

class ChallengeTest(unittest.TestCase):
    def test_mass_12(self):
        chall = challenge()
        self.assertEqual(chall.calc(12), 2)

    def test_mass_14(self):
        chall = challenge()
        self.assertEqual(chall.calc(14), 2)

    def test_mass_1969(self):
        chall = challenge()
        self.assertEqual(chall.calc(1969), 654)

    def test_mass_100756(self):
        chall = challenge()
        self.assertEqual(chall.calc(100756), 33583)

if __name__ == '__main__':
    unittest.main()