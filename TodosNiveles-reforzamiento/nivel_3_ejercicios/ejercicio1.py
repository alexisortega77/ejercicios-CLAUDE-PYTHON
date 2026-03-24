# ------------------------------------------------------------
# EJERCICIO 1 — Fácil
# Crea una función que reciba un número y devuelva
# si es par, impar, positivo, negativo o cero.
# ------------------------------------------------------------
# Output esperado:
# clasificar(4)   → "positivo y par"
# clasificar(-3)  → "negativo e impar"
# clasificar(0)   → "cero"
# clasificar(-8)  → "negativo y par"

def clasificar(num):
    if num==0:
        return "cero"
    else:

     if num>0:
         tipo="positivo"
     else:
         tipo="negativo"
     if num%2==0:
         return f"es {tipo} y par"
     else:
         return f"es {tipo} e impar"
print(clasificar(0))
         