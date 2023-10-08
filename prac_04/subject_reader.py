"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_subject_information(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []  # Initialise an empty list to store the data
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        data.append(parts)  # Append the parts to the data list
    input_file.close()
    return data


def display_subject_information(data):
    for subject in data:
        # unsure why "= subject" needs to be at the back, but it does not work otherwise.
        subject_code, lecturer, number_of_students = subject
        print(f"{subject_code} is taught by {lecturer} and has {number_of_students} enrolled.")


main()
