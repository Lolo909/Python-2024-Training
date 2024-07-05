# Unique Words: Given a list of words, 
# print all the unique words (ignoring case and punctuation).
# Test it with a sentence or paragraph of text.

import re

text = '''The polar bear (Ursus maritimus) is a large bear native to the Arctic and nearby areas. 
It is closely related to the brown bear, and the two species can interbreed. The polar bear is 
the largest extant species of bear and land carnivore, with adult males weighing 300–800 kg '''


text = text.lower()
onlyWordsFromText = re.findall(r'\w+', text)

setWithUniqueWords = set()

for word in onlyWordsFromText:
    setWithUniqueWords.add(word)

print(setWithUniqueWords)