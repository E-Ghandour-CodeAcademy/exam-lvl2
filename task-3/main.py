# Abstract Animal Class
# Objective: Define an abstract class `Animal` with an abstract method `speak`.
# Parameters:
# - None
# Returns:
# - Each subclass must implement `speak` which returns a string.
# Details:
# - Use the `abc` module to make `Animal` an abstract base class.
# - Subclasses like `Dog` and `Cat` should implement the `speak` method returning "Bark" and "Meow" respectively.
from abc import ABC, abstractmethod

class Animal():
    @abstractmethod
    def speak(self) -> str:
        pass

class Dog(Animal):
    def speak(self) -> str:
        return "Bark"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow"

dog = Dog()
print(dog.speak())  # Expected: Bark
cat = Cat()
print(cat.speak())  # Expected: Meow
