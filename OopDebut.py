# Définition d'une classe
class Rectangle:
    def __init__(self,
                 length, width, color="red"):
        self.length = length
        self.width = width
        self.color = color

    def calculate_area(self):
        return self.length * self.width


class Cake:
    def __init__(self, flavor):
        self.flavor = flavor

    def cut_in_part(self):
        print('gâteau découpé en 4 parts !')


rect1 = Rectangle(4, 2)
rect2 = Rectangle(5, 3, color="blue")

cake = Cake('chocolate')
print(cake.flavor)
cake.cut_in_part()

cake = Cake('banana')
print(cake.flavor)


class Bird:
    # Attribut de classe
    names = ('mouette', 'pigeon', "moineau", "hirondelle")
    positions = {}

    def __init__(self, name):
        self.position = 1, 2
        self.name = name
        self.positions[self.position] = self.name

    # Methode de classe
    @classmethod
    def find_bird(cls, position):
        if position in cls.positions:
            return f"on a trouvé un {cls.positions[position]}"
        return "any bird found"

    # Methode statique
    @staticmethod
    def get_definition():
        return "Bird:\n" "Birds are a group of warm-blooded " \
               "vertebrates constituting the class Aves, " \
               "characterised by feathers, toothless beaked jaws, " \
               "the laying of hard-shelled eggs, a high metabolic rate, " \
               "a four-chambered heart, and a strong yet lightweight skeleton"


print(Bird.find_bird((1, 2)))
bird = Bird("mouette")
print(Bird.find_bird((1, 2)))
print(Bird.get_definition())
