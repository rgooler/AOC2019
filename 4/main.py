class challenge:
    data = []

    def load(self, data):
        self.data = [a.split(',') for a in data]

    def part1(self, start=108457, end=562041):
        counter = 0
        for i in range(start, end):
            if self.test(i):
                counter = counter + 1
        return counter

    def part2(self):
        return None

    def test(self, i):
        i = str(i)
        # Contains double
        if not any(map(i.__contains__, ['11','22','33','44','55','66','77','88','99','00'])):
            return False
        # Increasing order
        if int(i[1]) < int(i[0]):
            return False
        if int(i[2]) < int(i[1]):
            return False
        if int(i[3]) < int(i[2]):
            return False
        if int(i[4]) < int(i[3]):
            return False
        if int(i[5]) < int(i[4]):
            return False
        return True

def main():
    chall = challenge()
    with open('input') as fh:
        lines = fh.readlines()
        chall.load(lines)
    print(f"Part 1: {chall.part1()}")
    print(f"Part 1: {chall.part2()}")

if __name__ == "__main__":
    main()