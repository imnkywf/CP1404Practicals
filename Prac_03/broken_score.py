import random

def main():
    out_file = open("results.txt", "w")
    score = random.randint(0, 100)
    print("Your score is {}".format(score),"your result is:", result(score), file=out_file)


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
