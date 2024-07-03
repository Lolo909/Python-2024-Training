print("Insert letter of the alphabet:", end="")
letter = input()

while(len(letter) != 1 or not letter.isalpha()):
    print("You must insert only one letter")
    print("Insert letter of the alphabet:", end="")
    letter = input()

listWithVowelLetters = ["a", "e", "i", "o", "u"]

if letter in listWithVowelLetters:
    print("Letter is vowel.")
else:
    print("Letter is consonant.")

#Second way:
# match letter:
#     case "a":
#         print("Letter is vowel.")
#     case "e":
#         print("Letter is vowel.")
#     case "i":
#         print("Letter is vowel.")
#     case "o":
#         print("Letter is vowel.")
#     case "u":
#         print("Letter is vowel.")
#     case _:
#         print("Letter is consonant.")
        
        