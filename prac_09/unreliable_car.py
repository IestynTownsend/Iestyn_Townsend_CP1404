# unreliable_car.py
from random import randint
from car import Car  # Assuming car.py file is in the same directory


class UnreliableCar(Car):
    """Represent an UnreliableCar object that inherits from Car."""

    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar instance, based on parent class Car."""
        super().__init__(fuel, name)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car with a chance based on reliability."""
        random_number = randint(0, 100)
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            return 0  # Car didn't drive due to low reliability
