class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

class ANewAnimalType(Animal):
    def sound(self):
        return "A new animal type"

# Polymorphic behavior
animals = [Dog(), Cat(), ANewAnimalType(),Animal()]
for animal in animals:
    print(animal.sound())
