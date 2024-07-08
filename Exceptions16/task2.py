# Task 2: Handling IndexError
# Write a Python script that does the following:
# Create a list of numbers.
# Prompt the user to input an index.
# Try to access the element at the specified index in the list.
# Handle the IndexError exception if the index is out of range.
# Print the value of the element if the index is valid or an error message if an index out of range occurs.

numbers = (1,2,3,4,5,6,7,8,9)

index = int(input("Insert index: "))

try:
    print(numbers[index])
except IndexError as e:
    print("Error:", e)