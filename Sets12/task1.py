# Task 1: Given a text document as a string, find and print the unique words (case-insensitive) in the document.
# How many are they?

import re

text = "This is a sample text document. This document contains some sample words. Sample words are used for demonstration."

text = text.lower()
onlyWordsFromText = re.findall(r'\w+', text)

setWithUniqueWords = set()

for word in onlyWordsFromText:
    setWithUniqueWords.add(word)

print(setWithUniqueWords)

