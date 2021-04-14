def main():
    """ask for inout and siplaye the colour codes."""
    COLOUR_DICT = {"ALICEBlUE":	"#f0f8ff", "ANTIQUEWHITE": "#faebd7", "BEIGE": "#f5f5dc", "AZURE": "#f0ffff", "AQUAMARINE": "#7fffd4",
                   "BLACK": "#000000", "BLUE": "#0000ff", "BROWN": "#a52a2a", "CADETBLUE": "#5f9ea0", "CORAL": "#ff7f50"}

    colour_name = str(input("Colour: "))
    colour_name = colour_name.upper()

    while colour_name.upper != "":
        if colour_name in COLOUR_DICT:
            print(COLOUR_DICT[colour_name])
        else:
            print("Invalid input")
        colour_name = input("Colour: ")
        colour_name = colour_name.upper()

    if colour_name == "":
        print()









main()