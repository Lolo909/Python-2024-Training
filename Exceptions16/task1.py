# Task 1: Handling Division by Zero
# Write a Python script that does the following:
# Prompt the user to input two numbers.
# Try to divide the first number by the second number.
# Handle the ZeroDivisionError exception if the second number is zero.
# Print the result of the division if successful or an error message if division by zero occurs.

numberOne = int(input("Insert first number: "))

numberTwo = int(input("Insert second number: "))

try:
    result = numberOne/numberTwo
    print(str(numberOne) + "/" + str(numberTwo) + "=" + "{:.2f}".format(result))
except ZeroDivisionError as e:
    print("Error:", e)
