print("Insert 3 numbers with space between them:",end="")

numbers = input().split()

numbers = sorted(numbers)
numbers.reverse()

biggestNumber = numbers[0];
print(biggestNumber);
