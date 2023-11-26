# car.py
class Car:
    """Represent a Car object."""

    price_per_km = 1.23  # Class variable shared by all instances of Car

    def __init__(self, fuel=0.0):
        """Initialize a Car instance."""
        self.fuel = float(fuel)  # Convert fuel to float
        self._odometer = 0

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance."""
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0.0  # Ensure fuel is set to a float value
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance

    def __str__(self):
        return f"Car, fuel={self.fuel}, odometer={self._odometer}"
