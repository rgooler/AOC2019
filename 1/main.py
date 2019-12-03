class challenge:
    def calc(self, weight):
        return int(weight / 3) - 2

    def calc2(self, weight):
        # This time with recursion for fuel weight
        total = self.calc(weight)
        fuelweight = self.calc(total)
        while fuelweight > 0:
            total = total + fuelweight
            fuelweight = self.calc(fuelweight)
        return total


if __name__ == "__main__":
    part1 = 0
    part2 = 0
    chall = challenge()
    with open('input') as fh:
        lines = fh.readlines()
        for line in lines:
            part1 = part1 + chall.calc(int(line))
            part2 = part2 + chall.calc2(int(line))

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")