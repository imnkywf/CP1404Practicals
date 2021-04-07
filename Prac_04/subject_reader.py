"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)

    display_details(data)

def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []  # creat a list called data
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)  # add list to data

    input_file.close()
    return data


def display_details(data):
    """Display subject details"""
    for subject_details in data:
        print("{} is taught by {} and has {} students. ".format(*subject_details))


main()
