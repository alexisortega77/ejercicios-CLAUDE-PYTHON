# ------------------------------------------------------------
# EJERCICIO 6 — Medio
# Crea una función recursiva factorial(n) que calcule n!
# sin usar bucles ni la función math.factorial.
# Luego úsala para calcular combinaciones C(n,r) = n! / (r! * (n-r)!)
# ------------------------------------------------------------
# Output esperado:
# factorial(0) → 1
# factorial(5) → 120
# factorial(10)→ 3628800
#
# combinaciones(5, 2) → 10
# combinaciones(10,3) → 120
# combinaciones(6, 6) → 1
#
# Pista: factorial(n) = n * factorial(n-1), caso base factorial(0) = 1
def factorial(n):
    if n < 0:
        return "Error: n must be non-negative"
    if n == 0:
        return 1
    return n * factorial(n - 1)

def combinations(n, r):
    if r > n:
        return "Error: r cannot be greater than n"
    return int(factorial(n) / (factorial(r) * factorial(n - r)))

print(factorial(0))          # 1
print(factorial(5))          # 120
print(factorial(10))         # 3628800

print(combinations(5, 2))    # 10
print(combinations(10, 3))   # 120
print(combinations(6, 6))    # 1


def factorial(n, depth=0):
    indent = "  " * depth
    if n == 0:
        return 1
    result = n * factorial(n - 1, depth + 1)
    return result

def combinations(n, r):
    if r > n or r < 0:
        return "Error: invalid values"
    return int(factorial(n) / (factorial(r) * factorial(n - r)))

"""
**¿Cómo funciona la recursión por dentro?**

Es lo más importante de este ejercicio. Visualiza lo que pasa con `factorial(4)`:
```
factorial(4)
  → 4 * factorial(3)
         → 3 * factorial(2)
                → 2 * factorial(1)
                       → 1 * factorial(0)
                                → 1          ← caso base, empieza a regresar
                       → 1 * 1 = 1
                → 2 * 1 = 2
         → 3 * 2 = 6
  → 4 * 6 = 24
Cada llamada espera a que la siguiente termine antes de calcular su resultado. 
La función se llama a sí misma achicando el problema hasta llegar al caso base n=0, y luego los resultados se van resolviendo de regreso.
¿Qué pasaría sin el caso base?
pythondef factorial(n):
    return n * factorial(n - 1)   # sin caso base

factorial(3)
# → 3 * factorial(2)
# → 3 * 2 * factorial(1)
# → 3 * 2 * 1 * factorial(0)
# → 3 * 2 * 1 * 0 * factorial(-1)
# → ... infinito → RecursionError
El caso base if n == 0: return 1 es lo que detiene la recursión. 
Sin él el programa se llama a sí mismo para siempre."""