# silver_service_taxi_test.py
from silver_service_taxi import SilverServiceTaxi


def main():
    # Create a new SilverServiceTaxi object, my_silver_taxi, with name "Hummer", 200 units of fuel, and fanciness of 4
    my_silver_taxi = SilverServiceTaxi("Hummer", 200, 4)

    # Drive the silver service taxi for an 18 km trip
    my_silver_taxi.drive(18)

    # Print the silver service taxi's details and the total fare
    print("Silver Service Taxi details:", my_silver_taxi)
    print("Total Fare:", my_silver_taxi.get_fare())


if __name__ == "__main__":
    main()
