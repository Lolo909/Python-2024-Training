
# Task 2: Create two tuples containing random integers. 
# Write a program to find and print the common elements (values that exist in both tuples) without duplicates.

tupleOne = (1,4,7)
tupleTwo = (7,55,7,99, 4)

listWithCommonElements = []


for number in tupleOne:
    if number in tupleTwo and number not in listWithCommonElements:
        listWithCommonElements.append(number)
    
print(listWithCommonElements)

