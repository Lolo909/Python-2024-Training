
# Task 3: Create two tuples, one with even numbers and one with odd numbers. 
# Write a program to concatenate these two tuples, find the maximum and minimum values, 
# and calculate the average of the combined elements.


tupleWithOddNumbers = (1,3,5,7,9)
tupleWithEvenNumbers = (2,4,6,8)

tupleCombine = tupleWithOddNumbers + tupleWithEvenNumbers

print("The maximum number is", max(tupleCombine))
print("The minimum number is", min(tupleCombine))

sumOfAllNumbers = 0

for number in tupleCombine:
    sumOfAllNumbers += number

average = sumOfAllNumbers/len(tupleCombine)

print(average)