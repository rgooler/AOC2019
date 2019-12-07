import re

class Crack:
    data = []

    def load(self, data):
        self.data = [a.split(',') for a in data]

    def part1(self, start=108457, end=562041):
        counter = 0
        for i in range(start, end):
            if self.test(i):
                counter = counter + 1
        return counter

    def part2(self, start=108457, end=562041):
        counter = 0
        for i in range(start, end):
            if self.test(i) and self.test2(i):
                counter = counter + 1
        return counter

    def test(self, i):
        i = str(i)
        # Contains double
        if not any(map(i.__contains__, ['11','22','33','44','55','66','77','88','99','00'])):
            return False
        # Increasing order
        if i != ''.join(sorted(i)):
            return False
        return True

    def test2(self, i):
        # No odd matching sets
        s = str(i)
        groups = [m.group(0) for m in re.finditer(r"(\d)\1*", s)]
        for item in groups:
            if len(item) == 2:
                if item in ['11','22','33','44','55','66','77','88','99','00']:
                    return True
        
        return False


def main():
    chall = challenge()
    with open('input') as fh:
        lines = fh.readlines()
        chall.load(lines)
    print(f"Part 1: {chall.part1()}")
    print(f"Part 1: {chall.part2()}")

if __name__ == "__main__":
    main()
