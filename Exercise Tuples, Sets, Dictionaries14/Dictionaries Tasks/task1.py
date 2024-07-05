# Word Frequency: Given a sentence, print a dictionary where the keys are words, and the values are 
# the frequency of each word in the sentence (case-insensitive). Test it with a longer sentence or multiple sentences.

import re

text = "In earlier versions of Access, we used the Memo data type to store large amounts of text, and the Text data type to store shorter strings (up to 255 characters). In Access 2016, these two data types have been renamed “Long Text” and “Short Text” respectively, and they have different properties and size limits depending on whether you’re using a desktop database or an Access web app. Here are the details:"

text = text.lower()
onlyWordsFromText = re.findall(r'\w+', text)

words = {}

for word in onlyWordsFromText:
    if word in words:
        words [word] = words[word] + 1
    else:
        words [word] = 1

print(words)