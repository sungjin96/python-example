class Animal:

    def __init__(self):
        print("ANIMAL CREATE")

    def whoAmI(self):
        print("ANIMAL")

    def eat(self):
        print('EATING')


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("DOG CREATE")

    def bark(self):
        print("WOOF")


mydog = Dog()
mydog.whoAmI()
mydog.eat()
mydog.bark()
