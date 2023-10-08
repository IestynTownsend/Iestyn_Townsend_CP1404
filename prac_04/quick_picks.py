import random

# constants for program
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBER_OF_PICKS = 6


def generate_quick_pick():
    quick_pick = []

    while len(quick_pick) < NUMBER_OF_PICKS:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)

        if number not in quick_pick:
            quick_pick.append(number)

    quick_pick.sort()
    return quick_pick


def main():
    try:
        number_of_quick_picks = int(input("How many quick picks? "))
        if number_of_quick_picks <= 0:
            print("Please enter a positive number of quick picks.")
        else:
            for i in range(number_of_quick_picks):
                quick_pick = generate_quick_pick()
                print(quick_pick)
    except ValueError:
        print("Invalid input. Please inout a valid number of quick picks.")


main()
