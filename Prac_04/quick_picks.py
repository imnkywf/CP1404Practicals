import random


def main():

    row = int(input("How many quick picks?"))
    for i in range(row):
        CONSTANTS = []
        for a in range(6):
            random_num = random.randint(1, 45)
            CONSTANTS.append(random_num)
            CONSTANTS.sort()

        print(" ".join("{}".format(number) for number in CONSTANTS))


main()
