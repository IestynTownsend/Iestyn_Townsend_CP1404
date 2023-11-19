class Taxi:
    """Specialised version of a Car that includes fare costs."""

    price_per_km = 1.23

    def __init__(self, name, fuel):
        """Initialise a Taxi instance, based on parent class Car."""
        self.name = name
        self.fuel = fuel
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{self.name}, fuel={self.fuel}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = min(distance, self.fuel)
        self.fuel -= distance_driven
        self.current_fare_distance += distance_driven
        return distance_driven


def main():
    # Create a new taxi object, my_taxi, with name "Prius 1", 100 units of fuel, and a price of $1.23
    my_taxi = Taxi("Prius 1", 100)

    # Drive the taxi 40 km
    my_taxi.drive(40)

    # Print the taxi's details and the current fare
    print("Taxi details:", my_taxi)
    print("Current Fare:", my_taxi.get_fare())

    # Restart the meter (start a new fare) and then drive the car 100 km
    my_taxi.start_fare()
    my_taxi.drive(100)

    # Print the details and the current fare
    print("\nTaxi details after restarting the fare:", my_taxi)
    print("Current Fare:", my_taxi.get_fare())


if __name__ == "__main__":
    main()
