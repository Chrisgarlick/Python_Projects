import time

time = input("Please enter how long would you like to start a timer for in seconds: ")

def countdown(timer):
    while timer > 0:
        print(timer)
        timer -= 1
        time.sleep(1)
    print("You have run out of time!")
    
while not time.isdigit():
    print("Please enter a valid integer to countdown from: ")
    time = input("Please enter how long would you like to start a timer for in seconds: ")
timer = int(time)
    
    
countdown(timer)
