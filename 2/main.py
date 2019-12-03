import sys

class challenge:
    code = []
    pointer = 0
    HALT = False
    opcodes = [1,2]

    def part1(self, code):
        return self.part2(code, 12, 2)

    def part2(self, code, a, b):
        self.code = [int(x) for x in code]
        self.code[1] = a
        self.code[2] = b
        return self.eval()

    def eval(self):
        while self.HALT == False:
            self.code = [int(x) for x in self.code]
            instruction = self.code[self.pointer]
            #print(f"instruction: {instruction}, {self.pointer}")
            if instruction in self.opcodes:
                #print("Found instruction")
                getattr(self, f"opcode_{instruction}")()
            elif instruction == 99:
                self.HALT = True
            else:
                self.HALT = True
                #if self.code[0] != 1:
                #    print(f"ERR({instruction}): {self.code[0]}")
        
        try:
            return 100 * self.code[self.pointer + 1] + self.code[self.pointer + 2]
        except IndexError:
            return 0

    def opcode_1(self):
        """
        Opcode 1 adds together numbers read from two positions and stores the 
        result in a third position. 
        The three integers immediately after the opcode tell you these three 
        positions - the first two indicate the positions from which you should
        read the input values, and the third indicates the position at which the
        output should be stored.
        """

        a = self.code[self.code[self.pointer + 1]]
        b = self.code[self.code[self.pointer + 2]]
        c = self.code[self.pointer + 3]
        #print(f"a: {a}\nb:{b}\nc:{c}")
        self.code[c] = a + b
        self.pointer = self.pointer + 4
        #print(f"pointer: {self.pointer} -- {self.code[self.pointer]}")


    def opcode_2(self):
        """
        Opcode 2 works exactly like opcode 1, except it multiplies the two 
        inputs instead of adding them. Again, the three integers after the 
        opcode indicate where the inputs and outputs are, not their values.
        """
        a = self.code[self.code[self.pointer + 1]]
        b = self.code[self.code[self.pointer + 2]]
        c = self.code[self.pointer + 3]
        #print(f"a: {a}\nb:{b}\nc:{c}")
        self.code[c] = a * b
        self.pointer = self.pointer + 4
        #print(f"pointer: {self.pointer} -- {self.code[self.pointer]}")

    def opcode_99(self):
        self.HALT = True

def main():
    chall = challenge()
    with open('input') as fh:
        lines = fh.readlines()
        for line in lines:
            l = line.split(',')
            chall.part1(l)
            print(f"Part 1: {chall.code}")
            for a in range(0, 99):
                for b in range(0, 99):
                    y = challenge()
                    y.part2(l.copy(), a, b)
                    x = y.code[0]
                    if x == 19690720:
                        val = 100 * a + b
                        print(f">> Part 2: {val} = {a},{b}")
                        sys.exit(0)


if __name__ == "__main__":
    chall = challenge()
    main()