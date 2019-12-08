import unittest
import logging
logging.basicConfig(level=logging.CRITICAL)
from aoc2019 import Amplifier

class Day7(unittest.TestCase):
    def test_part1_a(self):
        phase_sequence = [4,3,2,1,0]
        code = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
        chall = Amplifier(code=code, enable_logs=False, num_amplifiers=5)
        r = chall.run(phase_sequence)
        self.assertEqual(r, 43210)