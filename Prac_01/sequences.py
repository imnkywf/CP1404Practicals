
MENU = """(E)ven Numbers
(O)dd Numbers
(S)quares
(Q)uit"""
print(MENU)

choice = input(">>> ").upper()

odd_nums = []
even_nums = []

while choice != "Q":

    if choice == "E":
        num1 = int(input("Number 1:"))
        num2 = int(input("Number 2:"))

        for i in range(num1, num2):
            if i % 2 == 0:
                even_nums.append(i)
            else:
                odd_nums.append(i)
        print("Even numbers are:",even_nums)
        print(MENU)

        choice = input(">>> ").upper()

    elif choice == "O":
        num1 = int(input("Number 1:"))
        num2 = int(input("Number 2:"))

        for i in range(num1, num2):
            if i % 2 == 0:
                even_nums.append(i)
            else:
                odd_nums.append(i)
        print("Odd numbers are:",odd_nums)

        print(MENU)
        choice = input(">>> ").upper()

    elif choice == "S":
        num1 = int(input("Number 1:"))
        num2 = int(input("Number 2:"))

        for i in range(num1, num2):
            print(i ** 2,end=",")

        print(MENU)
        choice = input(">>> ").upper()

    else:
        print("Invalid choice.")

        print(MENU)
        choice = input(">>> ").upper()

while choice == "Q":
    print("Finished")
    break




