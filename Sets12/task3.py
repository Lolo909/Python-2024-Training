
# Task 3: Given a list of sets, find and print the intersection of all sets.

sets = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}, {3, 5, 6}]

setUniqueElements = sets[0]

i = 1
while i < len(sets):
    setTemp = sets[i]
    setUniqueElements = setUniqueElements.intersection(setTemp)
    i+=1


print(setUniqueElements)

