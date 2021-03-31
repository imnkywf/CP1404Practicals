# 1
out_file = "names.txt"
out_file = open("names.txt", 'w')
name = str(input("Please enter your name:"))
print("your name is:", name, file=out_file)

out_file.close()

# 2
in_file = open("numbers.txt", "r")
number_1 = int(in_file.readline())
number_2 = int(in_file.readline())
result = number_1 + number_2
print(result)

in_file.close()

# 3
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
print(total)

in_file.close()
