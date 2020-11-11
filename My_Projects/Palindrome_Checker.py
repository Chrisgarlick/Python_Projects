user = input("Please enter a word you would like to check: ")

if user.lower() == user.lower()[::-1]:
    print("That's a palindrome!")
else:
    print("That words not a palindrome!")
