# List Filtering: Implement a function that takes a list of numbers and a threshold value as input, 
# and returns a new list containing only the numbers greater than or equal to the threshold.

def List_Filtering(listWithNumbers, thresholdNumber):
    listWithNumberEqualOrBiggerThanThresholdNumber = []
    for number in listWithNumbers:
        if number >= thresholdNumber:
            listWithNumberEqualOrBiggerThanThresholdNumber.append(number)
    
    return listWithNumberEqualOrBiggerThanThresholdNumber

print(List_Filtering([1,2,3,4,4,5,5,6,7,8,31,313,144,131,3,0], 8))
