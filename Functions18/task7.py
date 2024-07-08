# Fibonacci Sequence: Implement a function that generates the first n numbers of the Fibonacci 
# sequence and returns them as a list.


def Fibonacci_Sequence(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return Fibonacci_Sequence(number-1) + Fibonacci_Sequence(number-2)
    
def Fibonacci_Sequence_List(number):

    fibonacciSequenceNumbers = []
    
    while number >= 0:
        num = Fibonacci_Sequence(number)
        fibonacciSequenceNumbers.append(num)
        number-=1
    
    return list(reversed(fibonacciSequenceNumbers))

print(Fibonacci_Sequence_List(9))