"""
Ejercicio 1 — Fácil
Crea un decorador uppercase que convierta a mayúsculas el string que devuelve una función.
python
@uppercase
def greet(name):
    return f"hello, {name}!"

greet("manuel")   → "HELLO, MANUEL!"
"""
from functools import wraps

def uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper
@uppercase
def greet(name):
    return f"hello, {name}!"

print(greet("manuel"))