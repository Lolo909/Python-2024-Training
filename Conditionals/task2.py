
isTheInputCorrect = False

age = ""

while(not isTheInputCorrect):
    print("Insert your age:")
    age = input()

    if not age.isdigit():
        print("Enter valid input!")
        continue
    
    age = int(age)

    if age<0:
        print("Age can't be negative")
        continue
 
    isTheInputCorrect = True
    

if age <= 12:
    print("You are a child")
elif age <=18:
    print("You are teenager")
else:
    print("You are adult")