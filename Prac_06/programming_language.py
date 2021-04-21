
class ProgrammingLanguage:
    """Programming language object"""
    def __init__(self, names, typing, reflection, year):
        self.names = names
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self,):
        return self.typing == "Dynamic"

    def __str__(self):
        return "{}, {} Typing, Reflection= {}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)



