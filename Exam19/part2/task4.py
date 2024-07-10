
# Task 4 - List Intersection:
# Write a Python function that takes two lists as input and returns a new list 
# containing the elements that are common to both input lists (intersection). 
# For example, if the input lists are [1, 2, 3, 4] and [3, 4, 5, 6], the function should return [3, 4].

def List_Intersection(list1, list2):
    commonSet = set()

    for number in list1:
        if number in list2:
            commonSet.add(number)
        
    return list(commonSet)

print(List_Intersection([1,2,3], [2,3,4]))

    
