from car import Car
import random

class Unreliable_car(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        percentage = random.randint(1, 100)
        if percentage < self.reliability:
            return super(Unreliable_car, self).drive(distance)
        else:
            distance = 0
            return super(Unreliable_car, self).drive(distance)




