class Employee:
    def greet(self):
        print("Welcome to the team!")


class Person:
    def greet(self):
        print("Welcome Hooman!")


class Manager(Employee, Person):
    pass


manager = Manager()
manager.greet()
