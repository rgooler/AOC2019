import sys
import logging
from .cpu import CPU

class Amplifier:
    code = []
    amplifiers = list()

    def __init__(self, code=[], enable_logs=True, num_amplifiers=5):
        if enable_logs :
            logging.basicConfig(level=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.CRITICAL)
        for a in range(num_amplifiers):
            c = CPU(enable_logs)
            CPU.code = code.copy()
            self.amplifiers.append(c)

    def run(self, phase_sequence=[], input_signal=0):
        for amp in self.amplifiers:
            amp.eval()
            # Set phase
            phase = phase_sequence.pop(0)
            amp.input(phase)
            # Previous result
            amp.input(input_signal)
            input_signal = amp.code[-1]

        # The end result is the max thruster signal
        return input_signal