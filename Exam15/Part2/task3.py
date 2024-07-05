# Task 3: Write a Python program that takes a sentence as 
# input and counts the frequency of each word in the sentence,
#  storing the results in a dictionary. For example,
#  for the input "The cat in the hat is the cat in the hat," 
# the output dictionary should show the word frequencies.


import re

text = "The cat in the hat is the cat in the hat."

text = text.lower()
onlyWordsFromText = re.findall(r'\w+', text)

words = {}

for word in onlyWordsFromText:
    if word in words:
        words [word] = words[word] + 1
    else:
        words [word] = 1

print(words)