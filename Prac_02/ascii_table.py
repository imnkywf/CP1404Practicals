letter = str(input("Enter a letter: "))
print("{} ".format(letter), ord(letter), "\n", "...")

number = int(input("Enter a number between 33 and 127: "))
while number < 33 or number > 127:
    print("Only between 33 to 127!")
    number = int(input("Enter a number between 33 and 127: "))

print("{} ".format(number), chr(number),"\n", "...")
