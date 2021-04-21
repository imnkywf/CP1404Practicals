from guitar import Guitar

name = "Gibson L-5  CES"
year = 1922
cost = 16035.40

guitar = Guitar(name, year, cost)

print("{} get_age() - Expected {}. Got {}".format(guitar.name, guitar.get_age(),guitar.get_age()))
print("{} is_vintage() - Expected {}. Got {}".format(guitar.name, guitar.is_vintage(), guitar.is_vintage()))