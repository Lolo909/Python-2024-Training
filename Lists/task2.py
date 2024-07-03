numbers = [ 5, 10, 15, 20, 25];

print(numbers[2])

numbers[1] = 30
print(numbers)

numbers.append(35)
print(numbers)

numbers = numbers[1:len(numbers):1]
print(numbers)

subset = numbers[1:4:1]
print(subset)

more_numbers = [40,45,50]

more_numbers+=numbers;
print(more_numbers)

print(len(numbers))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)