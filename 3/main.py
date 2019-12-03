class challenge:
    data = []

    def load(self, data):
        self.data = data
    
    def part1(self):
        return None

    def part2(self):
        return None

if __name__ == "__main__":
    chall = challenge()
    with open('input') as fh:
        lines = fh.readlines()
        for line in lines:
            part1 = part1 + chall.part1()
            part2 = part2 + chall.part2()

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")