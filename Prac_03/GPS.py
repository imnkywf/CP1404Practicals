import random

BORN_LOWER = 0.01
BORN_UPPER = 0.02
DIE_LOWER = 0.05
DIE_UPPER = 0.25
starting_population = 1000


def main():
    print("Welcome to the Gopher Population Simulator!", "\n"
          "Starting population: 1000", "\n"
          "Year 1""\n")

    born_rate = random.uniform(BORN_LOWER, BORN_UPPER)
    die_rate = random.uniform(DIE_LOWER, DIE_UPPER)

    population_2 = starting_population + round(starting_population * born_rate) - round(starting_population * die_rate)
    born_num_2 = round(starting_population * born_rate)
    die_num_2 = round(starting_population * die_rate)

    population_3 = population_2 + round(population_2 * born_rate) - round(population_2 * die_rate)
    born_num_3 = round(population_2 * born_rate)
    die_num_3 = round(population_2 * die_rate)

    population_4 = population_3 + round(population_3 * born_rate) - round(population_3* die_rate)
    born_num_4 = round(population_3 * born_rate)
    die_num_4 = round(population_3 * die_rate)

    population_5 = population_4 + round(population_4 * born_rate) - round(population_4 * die_rate)
    born_num_5 = round(population_4 * born_rate)
    die_num_5 = round(population_4 * die_rate)

    population_6 = population_5 + round(population_5 * born_rate) - round(population_5 * die_rate)
    born_num_6 = round(population_5 * born_rate)
    die_num_6 = round(population_5 * die_rate)

    population_7 = population_6 + round(population_6 * born_rate) - round(population_6 * die_rate)
    born_num_7 = round(population_6 * born_rate)
    die_num_7 = round(population_6 * die_rate)

    population_8 = population_7 + round(population_7 * born_rate) - round(population_7 * die_rate)
    born_num_8 = round(population_7 * born_rate)
    die_num_8 = round(population_7 * die_rate)

    population_9 = population_8 + round(population_8 * born_rate) - round(population_8 * die_rate)
    born_num_9 = round(population_8 * born_rate)
    die_num_9 = round(population_8 * die_rate)

    population_10 = population_9 + round(population_9 * born_rate) - round(population_9 * die_rate)
    born_num_10 = round(population_9 * born_rate)
    die_num_10 = round(population_9 * die_rate)

    print(born_num_2, "gophers were born.", die_num_2, "died.""\n"
          "Population:", population_2, "\n"
          "Year 2""\n")

    print(born_num_3, "gophers were born.", die_num_3, "died.""\n"
          "Population:", population_3, "\n"
          "Year 3""\n")
    print(born_num_4, "gophers were born.", die_num_4, "died.""\n"
          "Population:", population_4, "\n"
          "Year 4""\n")
    print(born_num_5, "gophers were born.", die_num_5, "died.""\n"
          "Population:", population_5, "\n"
          "Year 5""\n")
    print(born_num_6, "gophers were born.", die_num_6, "died.""\n"
          "Population:", population_6, "\n"
          "Year 6""\n")
    print(born_num_7, "gophers were born.", die_num_7, "died.""\n"
          "Population:", population_7, "\n"
          "Year 7""\n")
    print(born_num_8, "gophers were born.", die_num_8, "died.""\n"
          "Population:", population_8, "\n"
          "Year 8""\n")
    print(born_num_9, "gophers were born.", die_num_9, "died.""\n"
          "Population:", population_9, "\n"
          "Year 9""\n")
    print(born_num_10, "gophers were born.", die_num_10, "died.""\n"
          "Population:", population_10, "\n"
          "Year 10""\n")



main()
