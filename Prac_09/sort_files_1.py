import os

os.chdir("FilesToSort")

path = "."
s = os.listdir(path)

for filename in s:
    extension = filename.split('.')[-1]
    print(extension)

    try:
        os.mkdir(extension)
    except FileExistsError:
        pass

    os.rename(filename, "{}/{}".format(extension, filename))

    print()