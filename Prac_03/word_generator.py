import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
word_format = "%#*"
words = ""

letter_random = random.choice(word_format)


def main():
    print(is_valid_format(words))


def is_valid_format(words):
    for kind in letter_random.lower():
        if kind == "%" or "*":
            words += random.choice(CONSONANTS)
            return words
        elif kind == "#":
            words += random.choice(VOWELS)
            return words
        else:
            words += words
            return words


main()
