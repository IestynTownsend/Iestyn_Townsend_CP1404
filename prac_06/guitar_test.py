"""
Expected: 10 minutes
Actual: 25 minutes
Reason: could not figure out why my output was different to example. example used 2022 as current year.
"""

from prac_06.guitar import Guitar

def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 800.00)

    current_year = 2023

    print(f"{gibson.name} get_age() - Expected 101. Got {gibson.get_age(current_year)}")
    print(f"{another_guitar.name} get_age() - Expected 10. Got {another_guitar.get_age(current_year)}")

    # Test is_vintage() method
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage(current_year)}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage(current_year)}")


main()