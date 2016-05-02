

import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

word_format = input("Enter the word format: ")
word = ""

for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
else:
    word += random.choice(VOWELS)
print(word)