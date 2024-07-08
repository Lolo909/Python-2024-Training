# Greeting Function: Write a Python function that takes a person's name as 
# an argument and returns a greeting message using that name.

def greeting(name = "Anonymous"):
    print("Hello, " + name + "!")


greeting(input("Insert your name:"))
#or
greeting()