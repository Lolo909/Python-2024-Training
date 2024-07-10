# Task 5 - Unique Characters in String
# Write a Python function that takes a string as input and returns True 
# if all the characters in the string are unique (no character is repeated), and False otherwise.

text = input("Insert text to check if it is unique:")

def Unique_Characters_in_String(text):

    listWithCharacters = []

    for character in text:
        if character in listWithCharacters:
            return False
        else:
            listWithCharacters.append(character)

    return True

print(Unique_Characters_in_String(text))


