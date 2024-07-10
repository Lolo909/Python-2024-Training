# Task 3 - Word Frequency Counter
# Write a Python function that reads a text file and counts the frequency of each word in the file. 
# Ignore punctuation and consider words with different letter cases as the same word (e.g., "Word" and "word" 
# should be counted together).

import re

try:
    file = open("Exam19\part2\\task3TextFile.txt", "r")
    content = file.read()

    
    text = content.lower()
    onlyWordsFromText = re.findall(r'\w+', text)

    words = {}

    for word in onlyWordsFromText:
        if word in words:
            words [word] = words[word] + 1
        else:
            words [word] = 1

    print(words)
   
    file.close()
except FileNotFoundError as e:
    print("Error:", e)