from guitar import Guitar

def main():
    guitars_list = []
    print("My guitars!")
    name = input("Name:")

    while True:
        if name != "":
            year = input("Year:")
            cost = input("Cost:")
            add_guitars = Guitar(name, year, cost)
            guitars_list.append(add_guitars)

            print(name, year, cost, "added")

            name = input("Name:")
        else:
            for i in guitars_list:
                print(i)
            break

        guitars_list.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
        guitars_list.append(Guitar("Line 6 JTV-59", 2010, 1512.9))


main()
