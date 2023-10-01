# Task 1

user_name = input("Enter your name: ")
with open("name.txt", "w") as name_file:
    name_file.write(user_name)

# Task 2

with open("name.txt", "r") as name_file:
    name = name_file.read()
    print(f"Your name is {name}")

# Task 3

with open("numbers.txt", "r") as numbers_file:
    lines = numbers_file.readlines()

    line_1 = int(lines[0].strip())
    line_2= int(lines[1].strip())

    sum_both_lines = line_1 + line_2
    print(f"The sum of the first two lines is {sum_both_lines}")

# Task 4

with open("numbers.txt", "r") as numbers_file:
    lines = numbers_file.readlines()
    total = 0
    for line in lines:
        number = int(line.strip())
        total = total + number
print(f"Total is {total}")
