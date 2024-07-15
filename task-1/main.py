import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function `{func.__name__}` took {elapsed_time:.3f} seconds")
        return result
    return wrapper

# Example usage:
@timer
def some_heavy_computation():
    time.sleep(2)

some_heavy_computation()
