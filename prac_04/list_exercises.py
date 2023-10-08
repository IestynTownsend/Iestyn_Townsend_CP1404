# creates an empty list to store the numbers in
numbers = []

# prompt for the user to enter 5 numbers
for i in range(5):
    number = float(input("Number: "))
    numbers.append(number)

# output the required information about the numbers
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
average = sum(numbers) / len(numbers)
print(f"The average of the numbers is {average:.1f}")
# unsure if having a ".0" at the end of the first 4 of ok, if not a ":.0f" should be appended.
