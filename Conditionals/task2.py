print("Insert your age:")
age = int(input())

while (age<0):
    print("Age can't be negative")
    print("Insert your age:")
    age = int(input())-1

if age <= 12:
    print("You are a child")
elif age <=18:
    print("You are teenager")
else:
    print("You are adult")