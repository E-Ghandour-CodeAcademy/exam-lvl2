# Implement a Timer Decorator
# Objective: Write a decorator `timer` that measures the execution time of any function it decorates.
# Parameters:
# - None directly; it decorates functions.
# Returns:
# - Wrapper function that prints the execution time.
# Details:
# - Use the `time` module to calculate the execution time.
# - Print the time in seconds.

def timer(func):
	pass

# Desired Outcome:
# @timer
# def some_heavy_computation():
#     # Arbitrary computation that takes time, e.g., a loop or sleep
#     time.sleep(2)
# some_heavy_computation()  # Expected to print: Function `some_heavy_computation` took X.XXX seconds
