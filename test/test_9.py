from aoc2019 import CPU
import unittest

class Day9(unittest.TestCase):
    def test_Day9_part_1a(self):
        chall = CPU(False)
        code = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
        chall.run(code.copy())
        self.assertEqual(chall.e_output, code)
        del chall

    def test_Day9_part_1b(self):
        chall = CPU(False)
        code = [1102,34915192,34915192,7,4,7,99,0]
        chall.run(code.copy())
        self.assertEqual(chall.e_output, [1219070632396864])
        del chall

    def test_Day9_part_1c(self):
        chall = CPU(False)
        code = [104,1125899906842624,99]
        chall.run(code.copy())
        self.assertEqual(chall.e_output, [1125899906842624])
        del chall

if __name__ == '__main__':
    unittest.main()
