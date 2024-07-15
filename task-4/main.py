# Encapsulate Vehicle Class
# Objective: Create a class `Vehicle` with private attributes for `make`, `model`, and `year`, and implement getters and setters for each.
# Parameters:
# - make: String
# - model: String
# - year: Integer
# Returns:
# - None directly; use properties to get/set values.
# Details:
# - Use property decorators to create getters and setters.
# - Ensure invalid values (e.g., non-string for make/model, non-integer/year before 1886) raise ValueError.

class Vehicle:
    def __init__(self):
        self._make = None
        self._model = None
        self._year = None

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, value):
        if not isinstance(value, str):
            raise ValueError("Make must be a string")
        self._make = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if not isinstance(value, str):
            raise ValueError("Model must be a string")
        self._model = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise ValueError("Year must be an integer")
        if value < 1886:
            raise ValueError("Invalid year")
        self._year = value

v = Vehicle()
v.make = "Toyota"
v.model = "Corolla"
v.year = 2005
print(v.make, v.model, v.year)  # Expected: Toyota Corolla 2005
try:
    v.year = 1800  # Should raise ValueError: Invalid year
except ValueError as e:
    print(f"Error: {e}")
