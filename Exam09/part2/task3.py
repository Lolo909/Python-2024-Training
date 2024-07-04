
# Task 3: Write a Python program that checks if a given number is positive, 
# negative, or zero, and prints an appropriate message.

isTheInputCorrect = False

number = ""

while(not isTheInputCorrect):
    number = input("Insert number:")

    if not number.lstrip("-").isnumeric():
        print("Enter valid input!")
        continue
    
    number = int(number)

    isTheInputCorrect = True

if number > 0:
    print("This number is positive");
elif number < 0:
    print("This number is negative")
else:
    print("This number is ZERO")