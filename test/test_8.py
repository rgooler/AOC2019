from aoc2019 import *
import unittest

class Day8(unittest.TestCase):
    def test_Day8_part_1(self):
        dsn = DigitalSendingNetwork()
        dsn.load("123456789012")
        dsn.split_into_layers(3, 2)
        l = dsn.least_zeros()
        self.assertEqual(l.data, ['123', '456'])
        del dsn

    def test_Day8_part_2(self):
        dsn = DigitalSendingNetwork()
        dsn.load("0222112222120000")
        dsn.split_into_layers(2, 2)
        res = dsn.render()
        self.assertEqual(res.data, ['01', '10'])
        del dsn

    def test_Day8_part_2a(self):
        dsn = DigitalSendingNetwork()
        dsn.load("0222112222120000")
        dsn.split_into_layers(4, 1)
        res = dsn.render()
        self.assertEqual(res.data, ['0110'])
        del dsn

if __name__ == '__main__':
    unittest.main()
