# Task 2: Write a Python program that calculates the sum of all even numbers from 1 to 50 using a for loop.

result = 0

for i in range(1,51):
    if i % 2 == 0:
        result+=i

print(result)