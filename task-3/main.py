# Abstract Animal Class
# Objective: Define an abstract class `Animal` with an abstract method `speak`.
# Parameters:
# - None
# Returns:
# - Each subclass must implement `speak` which returns a string.
# Details:
# - Use the `abc` module to make `Animal` an abstract base class.
# - Subclasses like `Dog` and `Cat` should implement the `speak` method returning "Bark" and "Meow" respectively.

class Animal():
    pass

class Dog(Animal):
	pass

class Cat(Animal):
	pass

# Desired Outcome:
# dog = Dog()
# print(dog.speak())  # Expected: Bark
# cat = Cat()
# print(cat.speak())  # Expected: Meow
