# Palindrome Checker: Write a function that checks if a given string is a palindrome 
# (reads the same forwards and backwards) and returns True or False accordingly.

def isItPalindrom(text):   
    
    if text.lower() == text[::-1].lower():
        print("Yes, this is palindrom:", text)
    else:
        print("No, this is not palindrom:", text)
    

isItPalindrom("POP")
isItPalindrom("CAT")