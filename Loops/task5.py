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