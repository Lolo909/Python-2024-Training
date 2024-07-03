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