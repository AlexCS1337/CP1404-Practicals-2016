import random

class Car:
    def __init__(self, name="", fuel=0):
        """ initialise a Car instance """
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        return "{}, fuel={}, odo={}".format(self.name, self.fuel, self.odometer)

    def add_fuel(self, amount):
        """ add amount to the car's fuel"""
        self.fuel += amount

    def drive(self, distance):
        """ drive the car a given distance if it has enough fuel or drive until fuel runs out
        return the distance actually driven """

        if distance > self.fuel:
            distance_driven = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
            distance_driven = distance
        self.odometer += distance_driven
        return distance_driven

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability=0):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = random.randint(0, 100)
        if self.reliability > random_number:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            return 0

test = UnreliableCar('test', 1000, 50)
for i in range(1000):
    test.drive(1)
    print(test)