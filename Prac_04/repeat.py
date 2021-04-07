def main():
    str_list = []
    new_list = []

    strings = str(input("Enter your string:"))
    str_list.append(strings)
    print(str_list)
    for i in str_list:
        if i not in new_list:
            new_list.append(i)
        else:
            print(i, end=" ")


main()