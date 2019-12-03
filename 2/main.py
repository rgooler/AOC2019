class challenge:
    code = []
    pointer = 0
    HALT = False
    opcodes = [1,2,99]

    def part1(self, code):
        self.code = [int(x) for x in code]
        self.eval()
        return self.code

    def part2(self, code):
        return None

    def eval(self):
        while self.HALT == False:
            instruction = self.code[self.pointer]
            print(f"instruction: {instruction}")
            if instruction in self.opcodes:
                print("Found instruction")
                getattr(self, f"opcode_{instruction}")()
            else:
                self.HALT = True

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
        target = self.code[self.pointer + 3]
        print(f"a: {a}\nb:{b}\nc:{target}")
        self.code[target] = a + b
        self.pointer = self.pointer + 4
        print(f"pointer: {self.pointer} -- {self.code[self.pointer]}")


    def opcode_2(self):
        """
        Opcode 2 works exactly like opcode 1, except it multiplies the two 
        inputs instead of adding them. Again, the three integers after the 
        opcode indicate where the inputs and outputs are, not their values.
        """
        a = self.code[self.code[self.pointer + 1]]
        b = self.code[self.code[self.pointer + 2]]
        target = self.code[self.pointer + 3]
        print(f"a: {a}\nb:{b}\nc:{target}")
        self.code[target] = a * b
        self.pointer = self.pointer + 4
        print(f"pointer: {self.pointer} -- {self.code[self.pointer]}")

    def opcode_99(self):
        self.HALT = True

def main():
    chall = challenge()
    with open('input') as fh:
        lines = fh.readlines()
        for line in lines:
            a = line.split(',')
            a[1] = '12'
            a[2] = '2'
            chall.part1(a)
            #part2 = part2 + chall.part2(line.split(','))

    print(f"Part 1: {chall.code}")
    #print(f"Part 2: {part2}")

if __name__ == "__main__":
    chall = challenge()
    main()