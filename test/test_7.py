import unittest
import logging
logging.basicConfig(level=logging.CRITICAL)
from aoc2019 import *

class Day7(unittest.TestCase):
    def test_part1(self):
        chall = CPU()
        data = []
        chall.load(data)
        err = chall.run()
        self.assertEqual(err, 0)