
sales = float(input("Enter Sales Amount: $"))
while sales >= 0:
    if sales < 1000:
        sales_bonus = sales * 0.1
        total = sales + sales_bonus
    else:
        sales_bonus = sales * 0.15
        total = sales + sales_bonus
    print("Bonus is: $", sales_bonus,)
    sales = float(input("Enter Sales Amount: $"))
