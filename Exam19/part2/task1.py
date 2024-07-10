# Task 1 - Temperature Converter
# Write a Python function that converts a temperature in Celsius to Fahrenheit. 
# The formula is: Fahrenheit = (Celsius * 9/5) + 32.


def Temperature_Converter(numberCelsius):
    return (numberCelsius * 9/5) + 32.

print("{:.2f}".format(Temperature_Converter(39)))