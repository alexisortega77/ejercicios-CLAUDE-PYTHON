# ------------------------------------------------------------
# EJERCICIO 1 — Fácil
# Pide un número y clasifícalo: positivo/negativo/cero Y par/impar.
# ------------------------------------------------------------
# Input: -4
# Output esperado:
# -4 es negativo y par.
#
# Input: 7
# Output esperado:
# 7 es positivo e impar.
#
# Input: 0
# Output esperado:
# 0 es cero.

numero=int(input("Ingresa un numero: "))

if numero==0:
    print(f"{numero} es cero.")
else:
    if numero>0:
        tipo="positivo"
    else:
        tipo="negativo"
    if numero%2==0:
     print(f"{numero} es {tipo} y par")
    else:
     print(f"{numero} es {tipo} e impar")

