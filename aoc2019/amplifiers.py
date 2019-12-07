import sys
import logging

class CPU:
    code = []
    pointer = 0
    HALT = False
    e_input = None
    e_output = list()

    def __init__(self, enable_logs=True):
        if enable_logs :
            logging.basicConfig(level=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.CRITICAL)


    def run(self, code, e_input=1):
        self.code = code
        self.e_input = e_input
        self.e_output = list()
        return self.eval()

    def split_instruction(self, inst):
        s = str(inst).zfill(5)
        instruction = int(s[-2:])
        opcode = s[:-2]
        return (instruction, opcode)

    def disasm(self):
        logging.debug("="*80)
        logging.debug(f"code: {self.code[self.pointer:self.pointer + 4]}           @ {self.pointer}")
        instruction, opcode = self.split_instruction(self.code[self.pointer])
        logging.debug(f"inst: {instruction}    opcode: {opcode}")
        logging.debug("")

        for p in range(1,4):
            try:
                _ = self.code[self.pointer + p]
            except IndexError:
                break
            mode = self.mode(opcode, p)
            if(mode == 0):
                # Position mode
                try:
                    logging.debug(f"param {p}: {mode} || {self.code[self.pointer + p]} => {self.code[self.code[self.pointer + p]]}")
                except IndexError:
                    logging.debug(f"param {p}: {mode} || {self.code[self.pointer + p]} => ERR")
            else:
                # Immediate mode
                logging.debug(f"param {p}: {mode} || {self.code[self.pointer + p]}")

        logging.debug("="*80)

    def mode(self, opcode, opcode_index):
        try:
            return int(opcode[opcode_index * -1])
        except:
            # No opcode? Treat as mode 0 (( Position mode))
            return 0

    def get(self, ptr, opcode, opcode_index):
        mode = self.mode(opcode, opcode_index)

        if mode == 1:
            out = self.code[ptr]
            return int(out)
        elif mode == 0:
            out = self.code[self.code[ptr]]
            return int(out)
   
    def eval(self):
        while self.HALT == False:
            logging.info("\n\n\n")
            self.code = [int(x) for x in self.code]
            # Grab in reverse order for convinience later
            instruction, opcode = self.split_instruction(self.code[self.pointer])
            self.disasm()
            try:
                getattr(self, f"opcode_{instruction}")(opcode)
            except:
                self.HALT = True
                logging.error(f"ERR({self.code[self.pointer]}): {self.pointer} -> {self.code[self.pointer:self.pointer + 4]}")
        
        try:
            return 100 * self.code[self.pointer + 1] + self.code[self.pointer + 2]
        except IndexError:
            return 0

    def opcode_1(self, opcode):
        """
        Opcode 1 adds together numbers read from two positions and stores the 
        result in a third position. 
        The three integers immediately after the opcode tell you these three 
        positions - the first two indicate the positions from which you should
        read the input values, and the third indicates the position at which the
        output should be stored.
        """
        logging.info(f"opcode_1({opcode})  [[ADD]]")
        a = self.get(self.pointer + 1, opcode, 1)
        b = self.get(self.pointer + 2, opcode, 2)
        c = self.code[self.pointer + 3]
        logging.info(f"Storing {a + b} at address {c}")
        self.code[c] = a + b
        self.pointer = self.pointer + 4


    def opcode_2(self, opcode):
        """
        Opcode 2 works exactly like opcode 1, except it multiplies the two 
        inputs instead of adding them. Again, the three integers after the 
        opcode indicate where the inputs and outputs are, not their values.
        """
        logging.info(f"opcode_2({opcode})  [[MULTIPLY]]")
        a = self.get(self.pointer + 1, opcode, 1)
        b = self.get(self.pointer + 2, opcode, 2)
        c = self.code[self.pointer + 3]
        logging.info(f"Storing {a * b} at address {c}")
        self.code[c] = a * b
        self.pointer = self.pointer + 4

    def opcode_3(self, opcode):
        """
        Opcode 3 takes a single integer as input and saves it to the address 
        given by its only parameter. 
        For example, the instruction 3,50 would take an input value and store it 
        at address 50.
        """
        logging.info(f"opcode_3({opcode})  [[INPUT]]")
        ptr = self.code[self.pointer + 1]
        self.code[ptr] = self.e_input
        self.pointer = self.pointer + 2

    def opcode_4(self, opcode):
        """
        Opcode 4 outputs the value of its only parameter. 
        For example, the instruction 4,50 would output the value at address 50.
        """
        logging.info(f"opcode_4({opcode})  [[OUTPUT]]")
        out = self.get(self.pointer + 1, opcode, 1)
        logging.info(f">>>>> {out}")
        self.e_output.append(out)
        self.pointer = self.pointer + 2

    def opcode_5(self, opcode):
        """
        Opcode 5 is jump-if-true: 
          if the first parameter is non-zero, it sets the instruction pointer to 
          the value from the second parameter. 
          Otherwise, it does nothing.
        """
        logging.info(f"opcode_5({opcode})  [[JUMP_IF_TRUE]]")
        a = self.get(self.pointer + 1, opcode, 1)
        if a:
            self.pointer = self.get(self.pointer + 2, opcode, 2)
        else:
            self.pointer = self.pointer + 3

    def opcode_6(self, opcode):
        """
        Opcode 6 is jump-if-false: 
            if the first parameter is zero, it sets the instruction pointer to 
            the value from the second parameter. 
            Otherwise, it does nothing.
        """
        logging.info(f"opcode_6({opcode})  [[JUMP_IF_FALSE]]")
        a = self.get(self.pointer + 1, opcode, 1)
        if a == 0:
            self.pointer = self.get(self.pointer + 2, opcode, 2)
        else:
            self.pointer = self.pointer + 3

    def opcode_7(self, opcode):
        """
        Opcode 7 is less than: 
            if the first parameter is less than the second parameter, it stores 
            1 in the position given by the third parameter.
            Otherwise, it stores 0.
        """
        logging.info(f"opcode_7({opcode})  [[LESS_THAN]]")
        a = self.get(self.pointer + 1, opcode, 1)
        b = self.get(self.pointer + 2, opcode, 2)
        c = self.code[self.pointer + 3]
        logging.info(f"Storing {a * b} at address {c}")
        self.code[c] = a < b
        self.pointer = self.pointer + 4

    def opcode_8(self, opcode):
        """
        Opcode 8 is equals: 
            if the first parameter is equal to the second parameter, it stores 1
            in the position given by the third parameter. Otherwise, it stores 0.
        """
        logging.info(f"opcode_8({opcode})  [[EQUALS]]")
        a = self.get(self.pointer + 1, opcode, 1)
        b = self.get(self.pointer + 2, opcode, 2)
        c = self.code[self.pointer + 3]
        logging.info(f"Storing {a * b} at address {c}")
        self.code[c] = a == b
        self.pointer = self.pointer + 4

    def opcode_99(self):
        self.HALT = True
