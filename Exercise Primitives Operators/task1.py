num1 = 1;
num2 = 2;

def sumOfThenumbers(numberOne, numberTwo):
    return numberOne + numberTwo;

def differenceOfTheNumbers(numberOne, numberTwo):
    return numberOne - numberTwo;

def productOfTheNumbers(numberOne, numberTwo):
    return numberOne * numberTwo;

def quotientOfTheNumbers(numberOne, numberTwo):
    return numberOne*1.0 / numberTwo*1.0;


print("num1 + num2 = %d" % sumOfThenumbers(num1,num2));
print("num1 - num2 = %d" % differenceOfTheNumbers(num1,num2));
print("num1 * num2 = %d" % productOfTheNumbers(num1,num2));
print("num1 / num2 = %.1f" % quotientOfTheNumbers(num1,num2));

