from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def display_taxis(taxis):
    """Display the available taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Choose a taxi from the list."""
    display_taxis(taxis)
    choice = input("Choose taxi: ")
    try:
        choice = int(choice)
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid option")


def drive_taxi(taxi):
    """Drive the chosen taxi."""
    if taxi is None:
        print("You need to choose a taxi before you can drive")
    else:
        distance = float(input("Drive how far? "))
        cost = taxi.drive(distance)
        print(f"Your {taxi.name} trip cost you ${cost:.2f}")
        return cost


def main():
    print("Let's drive!")
    current_taxi = None
    total_bill = 0.0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    while True:
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()

        if choice == 'q':
            print(f"Total trip cost: ${total_bill:.2f}")
            print("Taxis are now:")
            display_taxis(taxis)
            break
        elif choice == 'c':
            current_taxi = choose_taxi(taxis)
        elif choice == 'd':
            cost = drive_taxi(current_taxi)
            if cost is not None:
                total_bill += cost

        print(f"Bill to date: ${total_bill:.2f}")


if __name__ == "__main__":
    main()
