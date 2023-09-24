def main():
    score = float(input("Enter score: "))
    print(determine_grade(score))


def determine_grade(score):
    if score > 100 or score < 0:
        return "Invalid Score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
