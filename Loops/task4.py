# Task 4: Factorial Calculator
# Write a Python program that calculates the factorial of a given number using a for loop.
# 5! = 5 x 4 x 3 x 2 x 1 = 120

print("Insert number:",end="")
number = int(input());

result=1;
for i in range(1, number+1):
    result*=i;

print(result)