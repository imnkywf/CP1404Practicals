
class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        years_old = 2020 - self.year
        return years_old

    def is_vintage(self):
        return self.get_age() > 50


