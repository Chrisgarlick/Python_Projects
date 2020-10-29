import random
# Rock Paper Scissors, P < R, R < S, S < P
player = False

ready = input("Are you ready to play?: Yes or No: ")
if ready.lower() == 'y':
    player == False

# Scores
myscore = 0
opponent_score = 0

# Game play
while player == False:
    # Opponents choice
    opponent = ["R", "P", "S"]
    opponent_choice = random.choices(opponent)
    opponents_go = str(opponent_choice)[2]
    # Users guess
    player = input("Please choose a weapon:\nRock\nPaper\nScissors\n")
    if player.lower() == 'r' and opponents_go.lower() == 's':
        print("You have chosen Rock!")
        print("You have won this round!")
        myscore += 1
        print(f"{myscore}:{opponent_score} \n")
    elif player.lower() == 's' and opponents_go.lower() == 'p':
        print("You have chosen Scissors!")
        print("You have won this round!")
        myscore += 1
        print(f"{myscore}:{opponent_score} \n")
    elif player.lower() == 'p' and opponents_go.lower() == 'r':
        print("You have chosen Paper! ")
        print("You have won this round!")
        myscore += 1
        print(f"{myscore}:{opponent_score} \n")
    elif opponents_go.lower() == player.lower():
        print(f"You have chosen {user}")
        print("It's a tie!")
        print(f"{myscore}:{opponent_score} \n")
    else:
        print(f"You have chosen {user}")
        print("Opponent has won!")
        opponent_score += 1
        print(f"{myscore}:{opponent_score} \n")
    
    player = False
        
    if myscore == 3:
        print(f"You have won! {myscore}:{opponent_score} Congrats")
        break
    elif opponent_score == 3:
        print(f"You have lost... {myscore}:{opponent_score} Unlucky")
        break
        
