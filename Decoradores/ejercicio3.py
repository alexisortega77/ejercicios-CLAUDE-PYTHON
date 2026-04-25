"""
Ejercicio 3 — Fácil
Crea un decorador logger que registre cada llamada con sus argumentos y resultado.
python
@logger
def multiply(a, b):
    return a * b

multiply(3, 4)
# [LOG] multiply(3, 4) → 12

"""
from functools import wraps
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_str   = ", ".join(repr(a) for a in args)
        kwargs_str = ", ".join(f"{k}={repr(v)}" for k, v in kwargs.items())
        all_args   = ", ".join(filter(None, [args_str, kwargs_str]))
        result     = func(*args, **kwargs)
        print(f"[LOG] {func.__name__}({all_args}) -> {result}")
        return result
    return wrapper
@logger
def multiply(a, b):
    return a*b

print(multiply(3,4))

        