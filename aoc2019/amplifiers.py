import sys
import logging
from .cpu import CPU

class Amplifier:
    code = []
    amplifiers = []

    def __init__(self, code=[], enable_logs=True, num_amplifiers=5):
        if enable_logs :
            logging.basicConfig(level=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.CRITICAL)
        self.amplifiers = []
        for a in range(num_amplifiers):
            self.code = code
            self.amplifiers.append(CPU(enable_logs))

    def run(self, phase_sequence=[], input_signal=0):
        for amp in self.amplifiers:
            ## print("*"*80)
            amp.run(self.code.copy())
            # Set phase
            phase = phase_sequence.pop(0)
            ## print(f"Setting phase to {phase}")
            amp.input(phase)
            # Previous result
            ## print(f"Setting input_signal to {input_signal}")
            amp.input(input_signal)
            input_signal = amp.e_output[-1]
            ## print(amp.code)
            ## print(input_signal)

        # The end result is the max thruster signal
        return input_signal