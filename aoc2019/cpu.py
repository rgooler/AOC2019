import sys
import logging

class CPU:
    code = None
    pointer = 0
    BLOCKED = False
    HALT = False
    e_input = []
    e_output = []
    exit_code = 0
    relative_base = 0

    def __init__(self, enable_logs=True):
        if enable_logs :
            logging.basicConfig(level=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.CRITICAL)
        e_input = []
        e_output = []

    def run(self, code):
        self.code = code
        self.e_input = []
        self.e_output = []
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
        logging.debug(f"inst: {instruction}    opcode: {opcode}     rel: {self.relative_base}")
        logging.debug("")

        for p in range(1,4):
            try:
                _ = self.code[self.pointer + p]
            except IndexError:
                break
            mode = self.mode(opcode, p)
            if mode == 0:
                # Position mode
                try:
                    target = self.get_mode(self.pointer + p, mode, True)
                    logging.debug(f"|| param {p}: {mode} || {target} => {self.code[target]}")
                except IndexError:
                    logging.debug(f"|| param {p}: {mode} || {self.code[self.pointer + p]} => ERR")
            elif mode == 1:
                # Immediate mode
                logging.debug(f"|| param {p}: {mode} || {self.code[self.pointer + p]}")
            elif mode == 2:
                # Relative mode
                try:
                    target = self.get_mode(self.pointer + p, mode, True)
                    logging.info(f"target: {target}")
                    logging.debug(f"|| param {p}: {mode} || {self.code[self.pointer + p]} ({self.relative_base + self.code[self.pointer + p]}) ~> {target}")
                except IndexError:
                    logging.debug(f"|| param {p}: {mode} || {self.code[self.pointer + p]} ({self.relative_base + self.code[self.pointer + p]}) ~> ERR")
            else:
                print(f"ERR: Unknown mode {mode}")

        logging.debug("="*80)

    def mode(self, opcode, opcode_index):
        logging.info(f"mode(self, {opcode}, {opcode_index})")
        try:
            return int(opcode[opcode_index * -1])
        except:
            # No opcode? Treat as mode 0 (( Position mode))
            return 0

    def get_mode(self, ptr, mode, diag=False):
        ptr = int(ptr)
        logging.info(f"get_mode(self, {ptr}, {mode})")
        if ptr < 0:
            self.HALT = True
            print("Get from negative index")
            return None
        if mode == 0:
            # Position Mode
            logging.info("~ Position Mode [0] ~")
            rptr = int(self.code[ptr])
            logging.info(f"{rptr} > {len(self.code)} = {rptr > len(self.code)}")
            if rptr >= len(self.code) and diag == False:
                howmany = rptr - len(self.code)
                logging.info(f">> howmany:{howmany}")
                self.code.extend(['0'] * howmany )
                logging.info(f"Extended code: {self.code}")
            else:
                logging.info("Not extending")
            try:
                return int(self.code[rptr])
            except IndexError:
                return 0
        elif mode == 1:
            # Intermediate Mode
            logging.info("~ Immediate Mode [1] ~")
            return int(self.code[ptr])
        elif mode == 2:
            # Relative mode
            logging.info("~ Relative Mode [2] ~")
            rptr = self.relative_base + self.code[ptr]
            logging.info(f"rptr: {rptr}")
            if rptr >= len(self.code) and diag == False:
                howmany = rptr - len(self.code)
                self.code.extend(['0'] * howmany )
                logging.info(f"Extended code: {self.code}")
            try:
                return int(self.code[rptr])
            except IndexError:
                return 0

    def put_mode(self, ptr, mode, value):
        logging.info(f"put_mode(self, {ptr}, {mode}, {value}):")
        if mode == 0:
            logging.info("+ Position Mode [0] +")
            rptr = self.code[ptr]
            logging.info(f"rptr: {rptr}/{len(self.code)}")
            if rptr >= len(self.code):
                logging.info(">> extending...")
                howmany = rptr - len(self.code) + 1
                self.code.extend(['0'] * howmany)
                logging.info(f"~~~ {howmany}, {len(self.code)} -=- {rptr}")
            self.code[rptr] = value
        elif mode == 1:
            logging.info("+ Immediate Mode [1] +")
            self.code[ptr] = value
        elif mode == 2:
            logging.info("+ Relative Mode [2] +")
            rptr = self.relative_base + ptr
            if rptr >= len(self.code):
                howmany = rptr - len(self.code)
                self.code.extend(['0'] * howmany)
            self.code[rptr] = value

    def get(self, ptr, opcode, opcode_index):
        logging.info(f"get(self, {ptr}, {opcode}, {opcode_index})")
        if ptr > len(self.code):
            howmany = ptr - len(self.code)
            logging.info("extending by {howmany}")
            self.code.extend(['0'] * howmany)

        mode = self.mode(opcode, opcode_index)
        return self.get_mode(ptr, mode)

    def put(self, ptr, opcode, opcode_index, value):
        logging.info(f"put(self, {ptr}, {opcode}, {opcode_index}, {value})")
        if ptr > len(self.code):
            self.code.extend(['0'] * ptr - len(self.code))

        mode = self.mode(opcode, opcode_index)
        self.put_mode(ptr, mode, value)

    def eval(self):
        while self.HALT == False:
            self.tick()
            if self.BLOCKED == True:
                # Pause CPU if blocked
                return
        try:
            self.exit_code = 100 * int(self.code[self.pointer + 1]) + int(self.code[self.pointer + 2])
        except IndexError:
            pass
        return self.exit_code

    def clean(self):
        while self.code[-1] == 0 or self.code[-1] == '0':
            self.code.pop()

    def tick(self):
        logging.info("\n\n\nTICK\n")
        self.code = [int(x) for x in self.code]
        # Grab in reverse order for convinience later
        instruction, opcode = self.split_instruction(self.code[self.pointer])
        self.disasm()
        try:
            getattr(self, f"opcode_{instruction}")(opcode)
        except AttributeError:
            self.HALT = True
            logging.error(f"TICK ERROR RUNNING opcode_{instruction} WITH {opcode}")
            logging.error(f"ERR({self.code[self.pointer]}): {self.pointer} -> {self.code[self.pointer:self.pointer + 4]}")

    def input(self, data):
        self.e_input.append(data)
        if self.BLOCKED == True:
            self.BLOCKED = False
            self.eval()

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
        logging.info(f"a: {a}")
        b = self.get(self.pointer + 2, opcode, 2)
        logging.info(f"Storing {a + b} ")
        self.put(self.pointer + 3, opcode, 3, a + b)
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
        logging.info(f"Storing {a * b} ")
        self.put(self.pointer + 3, opcode, 3, a * b)
        self.pointer = self.pointer + 4

    def opcode_3(self, opcode):
        """
        Opcode 3 takes a single integer as input and saves it to the address 
        given by its only parameter. 
        For example, the instruction 3,50 would take an input value and store it 
        at address 50.
        """
        logging.info(f"opcode_3({opcode})  [[INPUT]]")
        if self.e_input == []:
            self.BLOCKED = True
            return
        self.put(self.pointer + 1, opcode, 1, int(self.e_input.pop(0)))
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
        logging.info(f"Storing {a < b} ")
        self.put(self.pointer + 3, opcode, 3, a < b)
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
        logging.info(f"Storing {a == b} ")
        self.put(self.pointer + 3, opcode, 3, a == b)
        self.pointer = self.pointer + 4

    def opcode_9(self, opcode):
        """
        Opcode 9 adjusts the relative base by the value of its only parameter. 
        The relative base increases (or decreases, if the value is negative) by the value of the parameter.
        """
        logging.info(f"opcode_9({opcode})  [[RELATIVE_BASE_OFFSET]]")
        self.relative_base = self.relative_base + self.get(self.pointer + 1, opcode, 1)
        logging.info(f">>>>> {self.relative_base}")
        self.pointer = self.pointer + 2

    def opcode_99(self, opcode):
        self.HALT = True
