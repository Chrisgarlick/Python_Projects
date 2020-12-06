import random 

def dice():
    '''
    Create two dice which randomize a number between 1 and 6
    '''
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2

two_dice = dice()

if two_dice == 12:
    print(f"DOUBLE 6!! You've just rolled a {two_dice}")
elif two_dice >= 10:
    print(f"High roller! You just rolled a {two_dice}")
elif two_dice >= 6:
    print(f"Big roll, you just rolled a {two_dice}")
else:
    print(f"Not amazing, but you rolled a {two_dice}")
