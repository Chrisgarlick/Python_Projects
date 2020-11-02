num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))
operator = int(input("Please choose a math operator:\n1) Add\n2) Subtract\n3) Multiply\n4) Divide\n"))

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

if operator == 1:
    result = add(num1, num2)
    print(f"Congrats, your answer is {result}")
elif operator == 2:
    result = subtract(num1, num2)
    print(f"Congrats, your answer is {result}")
elif operator == 3:
    result = multiply(num1, num2)
    print(f"Congrats, your answer is {result}")
elif operator == 4:
    result = divide(num1, num2)
    print(f"Congrats, your answer is {result}")
else:
    print("Please ensure you have inputted the correct numbers or operators")
