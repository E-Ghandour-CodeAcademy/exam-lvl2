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
	pass

# Desired Outcome:
# v = Vehicle()
# v.make = "Toyota"
# v.model = "Corolla"
# v.year = 2005
# print(v.make, v.model, v.year)  # Expected: Toyota Corolla 2005
# v.year = 1800  # Should raise ValueError: Invalid year
