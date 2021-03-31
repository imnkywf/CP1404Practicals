"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random


VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
word_format = "%#*"

word = ""

letter_random = random.choice(word_format)

for kind in letter_random.lower():
    if kind == "%" or "*":
        word += random.choice(CONSONANTS)
    elif kind == "#":
        word += random.choice(VOWELS)
    else:
        word = word

print(word)