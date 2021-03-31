def main():
    score = float(input("Enter score: "))
    print("Your result is:", result(score))


def result(score):
    if score < 0:
        score = "Invalid score"
        return score
    elif score > 100:
        score = "Invalid score"
        return score
    elif 90 <= score <= 100:
        score = "Excellent"
        return score
    elif 50 <= score < 90:
        score = "Passable"
        return score
    elif score < 50:
        score = "Bad"
        return score


main()


import random

def main():
    test = random.chocie(0 - 100)
    print("Your result is:", Result(test))

def Result(test):
    if 90 <= test <= 100:
        test = "Excellent"
        return test
    elif 50 <= test < 90:
        test = "Passable"
        return test
    elif test < 50:
        test = "Bad"
        return test