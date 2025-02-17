# example of inharitance about cat and dog class

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return self.name + " says Woof!"

class Cat(Animal):

    def speak(self):
        return self.name + " says Meow!"

kity = Dog("kity")
haski = Cat("haski")

print(kity.speak())
print(haski.speak())

# A inharitance is a way to form new classes using classes that have already been defined.
# in this example, Dog and Cat are called subclasses, and Animal is called the superclass.

