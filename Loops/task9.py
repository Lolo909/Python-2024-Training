
# Task 9: Reverse a String
# Write a Python program that takes a string as input and prints the reverse of that string using a for loop.
word = input("Insert word to reverse:")

lenghtWord = len(word)
for i in range(1,lenghtWord+1):
    print(word[lenghtWord-i],end="")
