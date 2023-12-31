"""
CP1404/CP5632 Practical
Debugging exercise: almost-working version of a CSV scores file program.
The scores.csv file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.
"""


def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    scores_file.close()

    subjects = scores_data[0].strip().split(",")
    score_by_subject = [[] for _ in subjects]

    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        for i, score in enumerate(score_numbers):
            score_by_subject[i].append(score)

    print_scores(subjects, score_by_subject)


def print_scores(subjects, scores_by_subject):
    print("{:<10}".format("Subject"), end="")
    for i in range(1, 11):
        print("{:<4}".format(f"Student {i}   "), end="")
    print("Max    Min    Avg")

    for i in range(len(subjects)):
        print("{:<10}   ".format(subjects[i]), end="")
        for score in scores_by_subject[i]:
            print("{:<4}        ".format(score), end="")
        print("{:<5} ".format(max(scores_by_subject[i])), end="")
        print("{:<5}  ".format(min(scores_by_subject[i])), end="")
        average = sum(scores_by_subject[i]) / len(scores_by_subject[i])
        print("{:.2f}  ".format(average))


main()
