# Task 4: Create a tuple containing the first five prime numbers (2, 3, 5, 7, 11). Perform the following operations:
# Add the number 13 to the tuple.
# Find the length of the modified tuple.
# Create a new tuple by repeating the modified tuple three times.
# Write Python code to perform these operations and print the results.

tuple = (2,3,5,7,11)
tuple2 = (13,)

modifiedTuple = tuple + tuple2
print(modifiedTuple)

print(len(modifiedTuple))

newTuple = modifiedTuple * 3
print(newTuple)