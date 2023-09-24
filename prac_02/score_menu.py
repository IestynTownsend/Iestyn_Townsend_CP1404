

def main():
    score = int(input(f"Enter score: "))
    MENU = """G - Get Score
                P - Print Result
                S - Show Stars
                Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = int(input(f"Enter score: "))
        elif choice == "P":
            print(determine_grade(score))
            pass
        elif choice == "S":
            print_censored_password(score)
            pass
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def determine_grade(score):
    if score > 100 or score < 0:
        return "Invalid Score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_censored_password(score):
    for i in range(0, score, 1):
        print('*', end='')
    print()
    print()


main()