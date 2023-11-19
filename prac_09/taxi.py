# taxi.py
from prac_09.car import Car


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""

    def __init__(self, name, fuel, price_per_km=1.23):
        """Initialize a Taxi instance, based on the parent class Car."""
        super().__init__(fuel)
        self.name = name
        self.price_per_km = price_per_km
        self.current_fare_distance = 0

    def get_fare(self):
        """Return the price for the taxi trip, rounded to the nearest 10 cents."""
        fare = self.price_per_km * self.current_fare_distance
        rounded_fare = round(fare, 1)  # Round to the nearest 10 cents
        return rounded_fare

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven
