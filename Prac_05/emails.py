
def find_names(email):
    acc_name = email.split('@',)[0]
    acc_name_split = acc_name.split('.')
    names = ''.join(acc_name_split).title()
    return names

def main():
    my_dict = {}
    email = input("Email: ")
    while email != "":
        names = find_names(email)
        name = str(input("Is your name {} (y/n)".format(names)))
        if name == "y":
            print()
            email = input("Email: ")
        elif name == "n":
            name = str(input("Enter your name: "))
            EMAIL_DICT = {name.title(): email}
main()






