import unittest
import logging
logging.basicConfig(level=logging.CRITICAL)
from aoc2019 import CPU

class Day5(unittest.TestCase):
    def test_part1_a(self):
        chall = CPU(False)
        code = [3,0,4,0,99]
        chall.run(code, 55)
        self.assertEqual(chall.e_output, [55])
        
    def test_part1_b(self):
        chall = CPU(False)
        code = [1002,4,3,4,33]
        chall.run(code, 55)
        self.assertEqual(chall.code[4], 99)

    def test_part2_a_PASS(self):
        """
        3,9,8,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
        """
        code = [3,9,8,9,10,9,4,9,99,-1,8]
        chall = CPU(False)
        chall.run(code, 8)
        self.assertEqual(chall.e_output, [1])

    def test_part2_a_FAIL(self):
        code = [3,9,8,9,10,9,4,9,99,-1,8]
        chall = CPU(False)
        chall.run(code, 9)
        self.assertEqual(chall.e_output, [0])

    def test_part2_b_PASS(self):
        """
        3,9,7,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
        """
        code = [3,9,7,9,10,9,4,9,99,-1,8]
        chall = CPU(False)
        chall.run(code, 7)
        self.assertEqual(chall.e_output, [1])

    def test_part2_b_FAIL(self):
        code = [3,9,7,9,10,9,4,9,99,-1,8]
        chall = CPU(False)
        chall.run(code, 8)
        self.assertEqual(chall.e_output, [0])

    def test_part2_c_PASS(self):
        """
        3,3,1108,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
        """
        code = [3,3,1108,-1,8,3,4,3,99]
        chall = CPU(False)
        chall.run(code, 8)
        self.assertEqual(chall.e_output, [1])

    def test_part2_c_FAIL(self):
        code = [3,3,1108,-1,8,3,4,3,99]
        chall = CPU(False)
        chall.run(code, 7)
        self.assertEqual(chall.e_output, [0])

    def test_part2_d_PASS(self):
        """
        3,3,1107,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
        """
        code = [3,3,1107,-1,8,3,4,3,99]
        chall = CPU(False)
        chall.run(code, 7)
        self.assertEqual(chall.e_output, [1])

    def test_part2_d_FAIL(self):
        code = [3,3,1107,-1,8,3,4,3,99]
        chall = CPU(False)
        chall.run(code, 8)
        self.assertEqual(chall.e_output, [0])
    
    def test_part2_e_PASS(self):
        """
        Here are some jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero:
        (using position mode)
        """
        code = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
        chall = CPU(False)
        chall.run(code, 1)
        self.assertEqual(chall.e_output, [1])

    def test_part2_e_FAIL(self):
        code = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
        chall = CPU(False)
        chall.run(code, 0)
        self.assertEqual(chall.e_output, [0])

    def test_part2_f_LT(self):
        """
        The above example program uses an input instruction to ask for a single number.  
        The program will then output 999 if the input value is below 8, 
        output 1000 if the input value is equal to 8, 
        or output 1001 if the input value is greater than 8.
        """
        code = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
        chall = CPU(False)
        chall.run(code, 7)
        self.assertEqual(chall.e_output, [999])

    def test_part2_f_EQ(self):
        """
        The above example program uses an input instruction to ask for a single number. 
        The program will then output 999 if the input value is below 8, 
        output 1000 if the input value is equal to 8, 
        or output 1001 if the input value is greater than 8.
        """
        code = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
        chall = CPU(False)
        chall.run(code, 8)
        self.assertEqual(chall.e_output, [1000])

    def test_part2_f_GT(self):
        """
        The above example program uses an input instruction to ask for a single number. 
        The program will then output 999 if the input value is below 8, 
        output 1000 if the input value is equal to 8, 
        or output 1001 if the input value is greater than 8.
        """
        code = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
        chall = CPU(False)
        chall.run(code, 9)
        self.assertEqual(chall.e_output, [1001])

if __name__ == '__main__':
    unittest.main()