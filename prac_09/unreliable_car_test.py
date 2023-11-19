# unreliable_car_test.py
from unreliable_car import UnreliableCar


def main():
    # Create a new UnreliableCar object, my_unreliable_car, with name "Unreliable Car", 100 units of fuel,
    # and reliability of 50
    my_unreliable_car = UnreliableCar("Unreliable Car", 100, 50)

    # Drive the unreliable car 40 km
    distance_driven = my_unreliable_car.drive(40)

    # Print the unreliable car's details and the distance actually driven
    print("Unreliable Car details:", my_unreliable_car)
    print("Distance Actually Driven:", distance_driven)


if __name__ == "__main__":
    main()
