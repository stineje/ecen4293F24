class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("We eat")

# Inherents features of methods of Animal class
class Mammal(Animal):
    def walk(self):
        print("We walk")

class Fish(Animal):
    def walk(self):
        print("We swim")

m = Mammal()
m.eat()
print(m.age)