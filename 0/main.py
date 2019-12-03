class challenge:
    data = []

    def load(self, data):
        self.data = data

    def part1(self):
        return None

    def part2(self):
        return None

def main():
    chall = challenge()
    with open('input') as fh:
        lines = fh.readlines()
        chall.load(lines)
    print(f"Part 1: {chall.part1()}")
    print(f"Part 1: {chall.part2()}")

if __name__ == "__main__":
    main()