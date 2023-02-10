class Animal:
    def __init__(self, name, place):
        self.name = name
        self.place = place

    def food(self):
        pass

    def __repr__(self):
        return f"{self.name} lives in {self.place}"

class Cow(Animal):
    def food(self):
        return "Grass"

class Horse(Animal):
    def food(self):
        return "Grams"

class Dog(Animal):
    def food(self):
        return "Pedigree and bones"


# Create instances of each subclass
c = Cow("Dhenu", "Farm")
h = Horse("Chetak", "Stable")
d = Dog("Henry", "Home")

# Printing each instance
print(c)
print(h)
print(d)


# Printing the food for each instance
print("\n")
print(c.name,"eats",c.food())
print(h.name,"eats",h.food())
print(d.name,"eats",d.food())
