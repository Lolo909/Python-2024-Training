
# Task 2: Given a sentence, use a dictionary to count the frequency of each word in the sentence. Ignore punctuation and make the comparison case-insensitive. For example, for the input "The quick brown fox jumps over the lazy dog," the output should be a dictionary like this:
# {
#     "the": 2,
#     "quick": 1,
#     "brown": 1,
#     "fox": 1,
#     "jumps": 1,
#     "over": 1,
#     "lazy": 1,
#     "dog": 1
# }



import re

text = "The quick brown fox jumps over the lazy dog,"

text = text.lower()
onlyWordsFromText = re.findall(r'\w+', text)

words = {}

for word in onlyWordsFromText:
    if word in words:
        words [word] = words[word] + 1
    else:
        words [word] = 1

print(words)