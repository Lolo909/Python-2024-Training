# Task 10: Palindrome Checker
# Create a program that checks if a given word or phrase is a palindrome (reads the same forwards and backwards) using a for loop.

# A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization, in most cases). 
# Here are some examples of palindromes:
# Word Palindromes:
# "racecar" 
# "deified"
# "level"
# "rotor"
# "civic"
# Phrase Palindromes:
# "A man, a plan, a canal, Panama!"
# "Madam, in Eden, I'm Adam."
# "Never odd or even."
# Number Palindromes:
# 121
# 1331
# 12321
# 9009


inputFromUser = input("Insert text to check if it is palindrom or not:")

clearedInputFromUser = []
for i in inputFromUser:

    if i.isnumeric():
        clearedInputFromUser.append(i)
    elif i.isalpha():
        clearedInputFromUser.append(i)

lenghtOfInputFromUser = len(clearedInputFromUser)
reversedInputFromUser = []

for i in range(1,lenghtOfInputFromUser+1):
    reversedInputFromUser.append(clearedInputFromUser[lenghtOfInputFromUser-i])

if clearedInputFromUser == reversedInputFromUser:
    print("Yes this is palindrom")
else:
    print("No this is not palindrom")
