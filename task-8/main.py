# Create a Chainable List Class
# Objective: Implement a class `ChainableList` that supports method chaining for append, extend, and pop methods.
# Parameters:
# - None initially; the methods will handle input.
# Returns:
# - Self, after modifying the list, to support chaining.
# Details:
# - Override the `append`, `extend`, and `pop` methods to return self.
# - Ensure no method breaks the chaining by raising an exception or not returning self.

class ChainableList(list):
    def append(self, value):
        super().append(value)
        return self

    def extend(self, iterable):
        super().extend(iterable)
        return self

    def pop(self, index=-1):
        super().pop(index)
        return self

# Example usage:
cl = ChainableList()
cl.append(1).extend([2, 3]).pop().append(4)
print(cl)  # Expected: [1, 4]
