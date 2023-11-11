# Define the constant for the current year
CURRENT_YEAR = 2023


class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= 50

    def __lt__(self, other):
        return self.year < other.year


# Function to read and process the data from the CSV file
def read_guitars_from_file(file_name):
    guitars = []

    with open(file_name, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            name, year, cost = parts[0], int(parts[1]), float(parts[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)

    return guitars


# Read guitars from the CSV file
file_name = 'guitars.csv'
guitars = read_guitars_from_file(file_name)

# Display the guitars
print("All Guitars:")
for guitar in guitars:
    print(guitar)

# Sort the list of guitars by year (oldest to newest)
guitars.sort()

# Display the sorted list of guitars
print("\nSorted Guitars (oldest to newest):")
for guitar in guitars:
    print(guitar)
