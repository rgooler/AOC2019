from main import challenge
import unittest

class ChallengeTest(unittest.TestCase):
    def test_demo(self):
        chall = challenge()
        chall.load([
            "R8,U5,L5,D3",
            "U7,R6,D4,L4"
        ])
        self.assertEqual(chall.part1(), 6)

    def test_part1a(self):
        chall = challenge()
        chall.load([
            "R75,D30,R83,U83,L12,D49,R71,U7,L72",
            "U62,R66,U55,R34,D71,R55,D58,R83"
        ])
        self.assertEqual(chall.part1(), 159)

    def test_part1b(self):
        chall = challenge()
        chall.load([
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
        ])
        self.assertEqual(chall.part1(), 135)

    def test_part2(self):
        chall = challenge()
        self.assertEqual(chall.part2(), None)

if __name__ == '__main__':
    unittest.main()