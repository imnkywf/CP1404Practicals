import random

def main():
    score = random.randint(0, 100)
    print("Your score is {}".format(score))
    print("Your result is:", result(score))


def result(score):
    if 90 <= score <= 100:
        score = "Excellent"
        return score
    elif 50 <= score < 90:
        score = "Passable"
        return score
    elif score < 50:
        score = "Bad"
        return score


main()
