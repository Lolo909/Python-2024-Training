# List Reversal: Write a function that reverses a list of elements 
# in place (without using Python's built-in reverse() method).

def reverse_list(listForReversing):
    i = len(listForReversing) - 1

    reversedList = []
    while i >= 0:
        reversedList.append(listForReversing[i])
        i-=1
    return reversedList

print(reverse_list([1,2,3,"dada",5]))