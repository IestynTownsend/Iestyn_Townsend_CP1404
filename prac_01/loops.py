"""
Base code that is provided
it outputs every second number from 1 to 20
"""
for i in range(1, 21, 2):
    print(i, end=' ')
print()

"""
Count in 10s from 0 to 100
"""
for i in range(0, 101, 10):
    print(i, end=' ')
print()

"""
Count backwards from 20 to 1
"""
for i in range(20, 0, -1):
    print(i, end=' ')
print()

"""
Ask the user for a number and then print that many *'s
"""
number_of_stars = int(input("Number of stars: "))
for i in range(0, number_of_stars, 1):
    print('*', end='')
print()
print()  # double print just so that there is a gap between the end of this one and the start of the next

"""
print n lines of increasing stars
e.g. if 5 is input print;
*
**
***
****
*****
"""
number_of_stars = int(input("Number of stars: "))
for i in range(0, number_of_stars + 1, 1):
    for j in range(i):
        print('*', end='')
    print()

x = 10
while x > 4:
    print(x, end=" ")
    x = x - 2
