def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']

    numbers = []
    name = str(input("What is your name: "))
    if name in usernames:
        print("Access granted")
    else:
        print("Access denied.")

    for number in range(1,6):
        number_1 = int(input("Number {} :".format(number)))
        while number_1 < 0:
            number_1 = int(input("Number {} :".format(number)))

    numbers.append(number_1)

    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is {}".format(sum(numbers)/5))








main()