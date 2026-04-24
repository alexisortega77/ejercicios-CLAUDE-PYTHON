"""
Ejercicio 5 — Medio
Crea un decorador cache que guarde los resultados de llamadas anteriores y los reutilice.
python@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

fibonacci(10)   → 55
fibonacci(35)   → 9227465  # instantáneo la segunda vez

💡 Guarda los resultados en un diccionario {args: resultado}.
"""