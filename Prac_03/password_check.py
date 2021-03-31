#CONSTANTS
minimum_length = 6

def main():
    password = get_password(minimum_length)
    while not len(password) >= minimum_length:
        password = get_password(minimum_length)
    asterisks(password)


def asterisks(password):
    print('*' * len(password))


def get_password(minimum):
    password = input('Please enter a password of at least {} characters: '.format(minimum))
    return password


main()