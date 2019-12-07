class Rocket:
    def calc_fuel_weight(self, weight):
        weight = int(weight)
        return int(weight / 3) - 2

    def calc_fuel_weight_recursive(self, weight):
        weight = int(weight)
        # This time with recursion for fuel weight
        total = self.calc_fuel_weight(weight)
        fuelweight = self.calc_fuel_weight(total)
        while fuelweight > 0:
            total = total + fuelweight
            fuelweight = self.calc_fuel_weight(fuelweight)
        return total
