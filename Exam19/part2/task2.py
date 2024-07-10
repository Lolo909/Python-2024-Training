# Task 2 - Even or Odd 
# Write a Python function that takes an integer as input and returns 'Even' if it's an even number and 'Odd' 
# if it's an odd number.

def Even_or_Odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
print(Even_or_Odd(4))
print(Even_or_Odd(7))