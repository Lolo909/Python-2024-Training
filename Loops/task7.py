# Task 7: Prime Number Checker
# Write a Python program to check if a given number is prime or not using a for loop.

# A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. 
# In other words, a prime number is a whole number that cannot be formed by multiplying two smaller
#  whole numbers other than 1 and itself.

isTheInputCorrect = False

number = ""

while(not isTheInputCorrect):
    number = input("Insert number:")

    if not number.lstrip("-").isnumeric():
        print("Enter valid input!")
        continue
    
    number = int(number)

    isTheInputCorrect = True

isNumberPrime = True

for i in range(2, number):
    if number % i == 0:
        isNumberPrime = False;

if isNumberPrime:
    print("Number is prime");
else:
    print("Number is not prime")
