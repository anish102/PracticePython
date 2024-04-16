class Vehicle:
    def __init__(self, model, brand, buyYear, manuPrice, todaysPrice):
        self.model = model
        self.brand = brand
        self.buyYear = buyYear
        self.manuPrice = manuPrice
        self.todaysPrice = todaysPrice

    def profitCalculator(self):
        if (self.manuPrice > self.todaysPrice):
            print(
                f'You bought a car {self.model} of {self.brand} with a profit of {self.manuPrice-self.todaysPrice}')
        elif (self.manuPrice < self.todaysPrice):
            print(
                f'You bought a car {self.model} of {self.brand} with a loss of {self.todaysPrice-self.manuPrice}')
        else:
            print('You don\'t have any profit or loss.')


class Bus(Vehicle):
    def profitCalculator(self):
        if (self.manuPrice > self.todaysPrice):
            print(
                f'You bought a bus {self.model} of {self.brand} with a profit of {self.manuPrice-self.todaysPrice}')
        elif (self.manuPrice < self.todaysPrice):
            print(
                f'You bought a bus {self.model} of {self.brand} with a loss of {self.todaysPrice-self.manuPrice}')
        else:
            print('You don\'t have any profit or loss.')


car1 = Vehicle("santro", "tata", 2007, 1500000, 1200000)
car1.profitCalculator()

bus1 = Bus("ac suspension", "volvo", 2015, 10500000, 12000000)
bus1.profitCalculator()
print(Bus.mro())
