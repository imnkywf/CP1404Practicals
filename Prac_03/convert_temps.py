def main():
    out_file = open("temps_output.txt", "w")
    in_file = open("temps_input.txt", "r")

    for lines in in_file:
        fahrenheit = float(lines)
        print("Degrees in celsius is:",fahrenheit_to_celsius(fahrenheit), file=out_file)

    in_file.close()


def fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
