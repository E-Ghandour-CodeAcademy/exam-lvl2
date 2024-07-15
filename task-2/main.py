# Data Analysis with Aggregation
# Objective: Write a class `DataAnalyzer` that can load a list of numbers and perform aggregation operations like average, sum, and median.
# Parameters:
# - data: List of numbers.
# Returns:
# - Calculated aggregated values based on the method called.
# Details:
# - Implement methods for `average`, `total`, and `median` which compute respective statistical measures.
# - Ensure the data list is not empty before performing calculations; raise ValueError if it is.

class DataAnalyzer:
    def __init__(self, data):
        if not data:
            raise ValueError("Data list cannot be empty")
        self.data = data

    def average(self):
        return sum(self.data) / len(self.data)

    def total(self):
        return sum(self.data)

    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        if n % 2 == 0:
            mid1 = sorted_data[n // 2 - 1]
            mid2 = sorted_data[n // 2]
            return (mid1 + mid2) / 2
        else:
            return sorted_data[n // 2]

da = DataAnalyzer([1, 3, 5, 7])
print(da.average())  # Expected: 4.0
print(da.total())    # Expected: 16
print(da.median())   # Expected: 4.0