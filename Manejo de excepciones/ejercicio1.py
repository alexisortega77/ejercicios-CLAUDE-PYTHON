"""
Ejercicio 1 — Fácil
Crea una función safe_divide(a, b) que maneje división entre cero y tipos incorrectos.
safe_divide(10, 2)      → 5.0
safe_divide(10, 0)      → "Error: cannot divide by zero"
safe_divide(10, "dos")  → "Error: invalid types"

"""
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: cannot divide by zero"
    except TypeError:
        return "Error: invalid types"
    else:
        return result   # solo devuelve si no hubo excepción

print(safe_divide(10, 2))       # 5.0
print(safe_divide(10, 0))       # Error: cannot divide by zero
print(safe_divide(10, "dos"))   # Error: invalid types