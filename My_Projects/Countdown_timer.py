import time

t = int(input("Please enter how long would you like to start a timer for in seconds: "))

def countdown(t):
    while t > 0:
        print(t)
        t -= 1
        time.sleep(1)
    print("You have run out of time!")
    
countdown(t)
