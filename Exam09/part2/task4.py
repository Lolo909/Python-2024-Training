# Task 4: Write a Python program that takes a string input from the user and checks if it is a palindrome 
# (reads the same forwards and backwards). Print "Palindrome" or "Not a palindrome" accordingly.


word = list(input("Insert word to check if it is palindrom or not:"))

reversedWord = list(reversed(word))

print(reversedWord)
if word == reversedWord:
    print("This word is palindrom")
else:
    print("This word is not palindrom")