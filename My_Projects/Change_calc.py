# How much money does user have?
money = float(input("Please enter how much money you have: "))

# Total amount of money subtracted
cost = float(input("Please enter how much you are being charged: "))
money_left = money - cost
new_money = round(money_left, 2)

# User's money - total = change
print("Calculating...")
print(f"You have £{new_money} left over!")
