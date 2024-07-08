# Prime Number Checker: Create a function that checks if a given number is prime and returns True or False accordingly.

def Prime_Number_Cheker(number):
    i = number - 1
    while i > 1:
        if number % i == 0:
            return False
        i-=1
    else:
        return True
    
print(Prime_Number_Cheker(12))