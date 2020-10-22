import random 

def dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    both_dice = dice1 + dice2

    if both_dice >= 6:
        print(f"Big roll!! You rolled a {both_dice}")
    else:
        print(f"Small roll!! You rolled a {both_dice}")
