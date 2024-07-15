# Implement a Custom Iterator for Prime Numbers
# Objective: Design a class `PrimeIterator` that generates an infinite sequence of prime numbers.
# Parameters:
# - None, but the iterator should handle internal state for generating primes.
# Returns:
# - Prime numbers, one at a time, indefinitely.
# Details:
# - Implement the iterator protocol methods `__iter__()` and `__next__()`.
# - Use a sophisticated method to check for primes to ensure efficiency as numbers grow large.

class PrimeIterator:
    def __init__(self):
        self.primes = [2]  # Initialize with the first prime number (2)
        self.current = 2  # Initialize the current prime number

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            self.current += 1
            for prime in self.primes:
                if self.current % prime == 0:
                    break
            else:
                # If no divisor found, it's a prime number
                self.primes.append(self.current)
                return self.current

# Example usage:
primes = PrimeIterator()
for _ in range(10):
    print(next(primes))  # Prints the first 10 prime numbers

