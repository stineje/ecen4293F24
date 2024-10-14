class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


def make_animal_speak(animal):
    print(animal.speak())


# Using polymorphism
dog = Dog()
cat = Cat()
make_animal_speak(dog)  # Output: Woof!
make_animal_speak(cat)  # Output: Meow!
