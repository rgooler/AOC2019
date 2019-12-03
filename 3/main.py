class challenge:
    data = []

    def load(self, data):
        self.data = [a.split(',') for a in data]
    
    def part1(self):
        l1 = self.draw_line(0)
        l2 = self.draw_line(1)
        s = self.find_intersections(l1, l2)
        length, coords = self.find_min_manhattan(s)
        return length

    def part2(self):
        return None

    def find_min_manhattan(self, s):
        length = 0xffffffff
        coords = (0,0)

        for item in s:
            x, y = item
            if abs(x) + abs(y) < length:
                length = abs(x) + abs(y)
                coords = item

        return (length, coords)

    def draw_line(self, line):
        out = []
        x = 0
        y = 0
        #print(self.data[line])
        for item in self.data[line]:
            #print(f">> {item}")
            aim = item[0]
            steps = int(item[1:])
            if aim == 'U':
                for i in range(steps):
                    x = x + 1
                    out.append((x, y))
            elif item[0] == 'L':
                for i in range(steps):
                    y = y - 1
                    out.append((x, y))
            elif item[0] == 'D':
                for i in range(steps):
                    x = x - 1
                    out.append((x, y))
            elif item[0] == 'R':
                for i in range(steps):
                    y = y + 1
                    out.append((x, y))
        return out


    def find_intersections(self, l1, l2):
        s1 = set(l1)
        s2 = set(l2)
        return s1 & s2

def main():
    chall = challenge()
    with open('input') as fh:
        lines = fh.readlines()
        chall.load(lines)
    print(f"Part 1: {chall.part1()}")
    

if __name__ == "__main__":
    main()
