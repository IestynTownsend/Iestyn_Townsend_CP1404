
total_number_of_items = int(input("Total number of items: "))
total_cost = 0

# Checking if there is an invalid amount of items
if total_number_of_items <= 0:
    print("Please enter an amount of items larger than 0")
    total_number_of_items = int(input("Total number of items: "))

# getting the cost of each item and adding it to the total cost
for i in range(total_number_of_items):
    price = float(input(f"What is the price of item number {i + 1}? $"))
    total_cost = total_cost + price

# applying a 10% discount if cost is over 100
if total_cost > 100:
    total_cost = total_cost * 0.9

# displaying the total price
print(f"Total price for {total_number_of_items} items is ${total_cost:.2f}")
