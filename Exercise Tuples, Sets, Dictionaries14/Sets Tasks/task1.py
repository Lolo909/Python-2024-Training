# Set Operations: Create two sets, one representing the even numbers from 1 to 10 and the other representing multiples of 3 from 1 to 10. Perform the following operations:
# Find the intersection of the two sets.
# Find the union of the two sets.
# Find the elements that are in the first set but not in the second set.

setWithEvenNumbers = {2,4,6,8,10}
setWithNumbersMultipliesOf3 = {3,6,9}

print(setWithEvenNumbers.intersection(setWithNumbersMultipliesOf3))
print(setWithEvenNumbers.union(setWithNumbersMultipliesOf3))
print(setWithEvenNumbers-setWithNumbersMultipliesOf3)