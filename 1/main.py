class challenge:
    def calc(self, weight):
        return int(weight / 3) - 2

if __name__ == "__main__":
    total = 0
    chall = challenge()
    with open('input') as fh:
        lines = fh.readlines()
        for line in lines:
            total = total + chall.calc(int(line))

    print(total)