"""
Ejercicio 4 — Medio
Crea un decorador validate_types que verifique que los argumentos sean del tipo correcto usando las anotaciones de la función.
python@validate_types
def add(a: int, b: int) -> int:
    return a + b

add(3, 4)        → 7
add(3, "four")   → TypeError: Argument 'b' must be int, got str

💡 Usa func.__annotations__ para acceder a los tipos declarados.
"""