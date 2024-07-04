# Task 6: Password Checker
# Create a simple password checker program using a while loop. Ask the user to enter a password, 
# and keep asking until they enter the correct password "python123."


theSecretPassword = "python123"

isPasswordCorrect = False;

while(not isPasswordCorrect):
    print("Guess password:", end="")
    guessPassword = input()

    if theSecretPassword == guessPassword:
        print("Correct!")
        isPasswordCorrect = True;
        break;
    else:
        print("Wrong password! Try again!")