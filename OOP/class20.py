class Animal:
    def eat(self):
        print("We eat")


class Bird(Animal):
    def fly(self):
        print("We fly")


class Chicken(Bird):
    pass


m = Chicken()
