# silver_service_taxi.py
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi that inherits from Taxi."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialize a SilverServiceTaxi instance, based on the parent class Taxi."""
        super().__init__(name, fuel, price_per_km=Taxi.price_per_km * fanciness)
        self.fanciness = fanciness

    def get_fare(self):
        """Return the total price for the taxi trip, including flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string representation of the SilverServiceTaxi."""
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km plus flagfall of ${self.flagfall:.2f}"
