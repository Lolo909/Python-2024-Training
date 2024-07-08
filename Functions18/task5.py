# List Sum: Create a function that takes a list of numbers as input and returns the sum
# of all the numbers in the list.

def list_sum(listWithNumbers):
    result = 0;
    for number in listWithNumbers:
        result+=number
    
    return(result)

print(list_sum((1,2,3,4,5,6,7,7)))