# Task 5: Guess the Number
# Generate a random number between 1 and 10. Ask the user to guess the number using a while loop. 
# Provide feedback (too high or too low) until they guess correctly.

import random

numbers = []
for i in range(1,10):
    numbers.append(i);

chosenNumber = random.choice(numbers)

isUserGuessedRight = False;

while(not isUserGuessedRight):
    print("What is the number? Your guess: ",end="");
    guessNumber = int(input())
    if guessNumber > chosenNumber:
        print("Too high!")
        continue;
    elif guessNumber < chosenNumber:
        print("Too low!")
        continue;
    else:
        print("Correct the number is",chosenNumber)
        isUserGuessedRight = True;