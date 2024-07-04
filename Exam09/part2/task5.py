# Task 5: Write a Python program that calculates the factorial of a given positive integer and prints the result.

isTheInputCorrect = False

number = ""

while(not isTheInputCorrect):
    number = input("Insert number:")

    if not number.lstrip("-").isnumeric():
        print("Enter valid input!")
        continue
    
    number = int(number)

    isTheInputCorrect = True

result = 1;
for i in range(1,number+1):
    result *= i

print(result)