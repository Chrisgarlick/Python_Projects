import random
from IPython.display import clear_output

# Random num generated, guess count and While True conditional
correct = False
number = random.randint(1, 100)
guess_count = 0

# While condition, user guesses, guess_count added to, output cleared
while not correct:
    guess = input("Please choose a number between 1-100: ")

    guess_count += 1
    
    clear_output()

# if correct - print how many guesses it took
    if int(guess) == number:
        print(f"You are successful, this took {guess_count} number of guesses!")
        break
# else if higher than number, say too high
    elif int(guess)> number:
        print("Your guess is too big!")
# else if lower than number, say too low
    elif int(guess) < number:
        print("Your guess is too small!")
