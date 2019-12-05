from main import challenge
import unittest

class ChallengeTest(unittest.TestCase):
    def otest_part1_a(self):
        chall = challenge()
        chall.code = [1,0,0,0,99]
        chall.eval()
        self.assertEqual(chall.code, [2,0,0,0,99])
        
    def otest_part1_b(self):
        chall = challenge()
        chall.code = [2,3,0,3,99]
        chall.eval()
        self.assertEqual(chall.code, [2,3,0,6,99])

    def otest_part1_c(self):
        chall = challenge()
        chall.code = [2,4,4,5,99,0]
        chall.eval()
        self.assertEqual(chall.code, [2,4,4,5,99,9801])

    def otest_part1_d(self):
        chall = challenge()
        chall.code = [1,1,1,4,99,5,6,0,99]
        chall.eval()
        self.assertEqual(chall.code,[30,1,1,4,2,5,6,0,99])

    def test_part1_a(self):
        chall = challenge()
        chall.part1([3,0,4,0,99],55)
        self.assertEqual(chall.e_output, 55)
        
    def test_part1_b(self):
        chall = challenge()
        chall.part1([1002,4,3,4,33],55)
        print(chall.code)
        self.assertEqual(chall.code[4], 99)

if __name__ == '__main__':
    unittest.main()