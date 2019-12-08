import unittest
import logging
logging.basicConfig(level=logging.CRITICAL)
from aoc2019 import Amplifier

class Day7(unittest.TestCase):
    def test_part1_a(self):
        phase_sequence = [4,3,2,1,0]
        code = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
        chall = Amplifier(code=code, enable_logs=False)
        r = chall.run(phase_sequence)
        self.assertEqual(r, 43210)
        del chall

    def test_part1_b(self):
        phase_sequence = [0,1,2,3,4]
        code = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
        chall = Amplifier(code=code, enable_logs=False)
        r = chall.run(phase_sequence)
        self.assertEqual(r, 54321)
        del chall

    def test_part1_c(self):
        phase_sequence = [1,0,4,3,2]
        code = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
        chall = Amplifier(code=code, enable_logs=False)
        r = chall.run(phase_sequence)
        self.assertEqual(r, 65210)
        del chall