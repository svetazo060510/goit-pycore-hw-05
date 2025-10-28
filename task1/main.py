from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    # Create empty dict cache.
    cache = {}

    def fibonacci(n: int) -> int:
        # Basic cases of the Fibonacci series
        if n <= 0:
            return 0
        if n == 1:
            return 1
        
        # Checking if a value is already in the cache
        if n in cache:
            return cache[n]  

        # If the value is not in the cache, we calculate it recursively
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# -- Usage example --
fib = caching_fibonacci()

# The first time fib(10) is called, it will calculate and cache
# fib(1) ... fib(10).
print(f"fib(10) = {fib(10)}")  # 55

# Calling fib(15), it will use the already stored values ​​from 1 to 10 and only calculate 
# fib(11) ... fib(15).
print(f"fib(15) = {fib(15)}")  # 610

# fib(10) is already in the cache
print(f"fib(10) = {fib(10)}")  # 55
