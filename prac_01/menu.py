name = str(input("Enter name: "))

MENU = """(H)ello
(G)oodbye
(Q)uit"""
print(MENU)

choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello", name)
        choice = input(">>> ").upper()
    elif choice == "G":
        print("Goodbye", name)
        choice = input(">>> ").upper()
    else:
        print("Invalid choice.")
        choice = input(">>> ").upper()

while choice == "Q":
    print("Finished")
    break




