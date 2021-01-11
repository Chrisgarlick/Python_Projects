def intake():
    money = float(input("Please enter how much money you have: "))
    return money

def moneyout():
    cost = float(input("Please enter how much the item cost: "))
    return cost

def replay():
    replay = input("Would you like to calculate your change? Press 'q' to quit: ")
    if replay == 'q':
        return False
    else:
        return True

redo = replay()

while redo:
    money_in = intake()
    money_out = moneyout()
    money_left = money_in - money_out
    new_money = round(money_left, 2)
    print("Calculating...")
    print(f"You have £{new_money} left.")
    redo = replay()

    
