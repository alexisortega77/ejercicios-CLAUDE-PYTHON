"""
Ejercicio 4 — Medio
Crea un decorador validate_types que verifique que los 
argumentos sean del tipo correcto usando las anotaciones de la función.
python
@validate_types
def add(a: int, b: int) -> int:
    return a + b

add(3, 4)        → 7
add(3, "four")   → TypeError: Argument 'b' must be int, got str

💡 Usa func.__annotations__ para acceder a los tipos declarados.
"""
from functools import wraps
import inspect
def validate_types(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        params      = [p for p in func.__code__.co_varnames if p in annotations]

        for name, value in zip(params, args):
            expected = annotations[name]
            if not isinstance(value, expected):
                raise TypeError(
                    f"Argument '{name}' must be {expected.__name__}, got {type(value).__name__}"
                )
        return func(*args, **kwargs)
    return wrapper

@validate_types
def add(a:int, b:int):
    return a + b

try:
    add(3, "four")
except TypeError as e:
    print(f"TypeError: {e}")             
    
    