
def main():
    lower = 10
    upper = 50
    number = get_number(lower, upper)

    while number < lower or number > upper:
        print("Only between 10 to 50!")
        number = get_number(lower, upper)
        print(chr(number), "\n", "...")


def get_number(lower, upper):
    error_check = True
    while error_check:
        try:
            number = int(input("Enter a number between 10 and 50: "))
            error_check = False

        except ValueError:
            print("Invalid input")
            error_check = True

    return number


main()
