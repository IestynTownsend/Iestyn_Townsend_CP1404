"""
Expected: 30 minutes
Actual: 20 minutes
"""


class Guitar:
    current_year = 2023

    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self, current_year):
        return current_year - self.year

    def is_vintage(self, current_year):
        return self.get_age(current_year) >= 50
