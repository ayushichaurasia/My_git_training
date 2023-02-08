# Ques 1:Create animal base class with attribute and related methods then create sub concrete subclass using animal eg
# of subclass: cow, horse, dog

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self, food):
        print(self.name, "eats", food)


class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, species="Cow")

    def eat(self):
        super().eat("grass")


class Horse(Animal):
    def __init__(self, name):
        super().__init__(name, species="Horse")

    def eat(self):
        super().eat("grams")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, species="Dog")

    def eat(self):
        super().eat("Pedigree")


cow = Cow("Dhenu", )
cow.eat()

horse = Horse("Chetak", )
horse.eat()

dog = Dog("Henry", )
dog.eat()
