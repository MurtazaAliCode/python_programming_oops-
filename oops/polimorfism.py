# make an example of polymorphism using the same example of inharitance.py

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

kity = Dog("haski")
haski = Cat("kity")

print(kity.speak())
print(haski.speak())

#* Polymorphism is a way to make the same method behave differently based on the input.
#* in this example, the speak method behaves differently based on the input.