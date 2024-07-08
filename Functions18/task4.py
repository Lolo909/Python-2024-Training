# Factorial Function: Implement a function that calculates the factorial of a non-negative integer n using recursion or a loop.

def factorial(number):
    result = 1;
    while number >= 1:
        result *= number
        number-=1

    return result

factorialNumber = factorial(5)
print(factorialNumber)