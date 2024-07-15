# Utilize `super()` in Inheritance
# Objective: Create a class hierarchy where `ElectricCar` extends `Car` and uses `super()` to initialize parent class attributes.
# Parameters:
# - `make`: String
# - `model`: String
# - `battery_size`: Integer (specific to `ElectricCar`)
# Returns:
# - None; initialization of attributes.
# Details:
# - `Car` class should initialize `make` and `model`.
# - `ElectricCar` should add `battery_size` and initialize it using `super()`.

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size

ec = ElectricCar('Tesla', 'Model S', 85)
print(ec.make, ec.model, ec.battery_size)  # Expected: Tesla Model S 85
