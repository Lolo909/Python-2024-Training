# Calculator Function: Create a function that takes two numbers 
# and an operator (+, -, *, /) as input and returns the result of applying the operator to the numbers.

def calculate(number1, number2, operater):
    
    match(operater):
        case "+":
            return number1 + number2
        case "-":
            return number1 - number2
        case "*":
            return number1 * number2
        case "/":
            return number1 / number2
        

print(calculate(1,2,"+"))
print(calculate(1,2,"-"))
print(calculate(1,2,"*"))
print(calculate(1,2,"/"))