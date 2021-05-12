import os

category = []
os.chdir("FilesToSort")

path = "."
files = os.listdir(path)

for filename in files:
    extension = filename.split('.')[-1]
    print("{} file".format(extension))

    if extension not in category:
        new_dir = input("What category would you like to sort {} files into? ".format(extension))

        try:
            os.mkdir(new_dir)
        except FileExistsError:
            pass



