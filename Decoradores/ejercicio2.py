"""
Ejercicio 2 — Fácil
Crea un decorador timer que imprima cuánto tardó en ejecutarse la función.
python
@timer
def slow_sum(n):
    return sum(range(n))

slow_sum(1000000)
# slow_sum took 0.0312 seconds
# → 499999500000

"""
import time
from functools import wraps
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start  = time.time()
        result = func(*args, **kwargs)
        end    = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

print(slow_sum(1000000))


        