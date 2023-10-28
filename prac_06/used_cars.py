"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    car1 = Car(100, "Limo")
    car2 = Car(100, "Sedan")
    car1.add_fuel(20)
    car2.add_fuel(50)
    print(f"{car1.name} has fuel: {car1.fuel}")
    print(f"{car2.name} has fuel: {car2.fuel}")
    car1.drive(115)
    car2.drive(70)
    print(car1)
    print(car2)


main()