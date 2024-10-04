# Base class (Parent)
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f"{self.name} makes a sound"

# Derived class (Child) inheriting from Anima
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class's constructor
        self.breed = breed

    # Overriding the sound method
    def sound(self):
        return f"{self.name} barks"

# Another derived class inheriting from Animal
class Cat(Animal):
    def sound(self):
        return f"{self.name} meows"

# Creating objects of the derived classes
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers")

# Accessing methods from the derived classes
print(dog.sound())  # Output: Buddy barks
print(cat.sound())  # Output: Whiskers meows
