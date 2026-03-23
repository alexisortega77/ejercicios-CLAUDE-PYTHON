# ------------------------------------------------------------
# EJERCICIO 2 — Fácil
# Pide al usuario dos números y muestra todas las operaciones básicas.
# ------------------------------------------------------------
# Input del usuario: 15 y 4
# Output esperado:
# Suma:             19
# Resta:            11
# Multiplicación:   60
# División:         3.75
# División entera:  3
# Módulo:           3
# Potencia:         50625

num1=int(input("Ingresa un numero"))
num2=int(input("Ingresa un numero"))
print(f"Suma: {num1+num2}")
print(f"Resta: {num1-num2}")
print(f"Multiplicacion: {num1*num2}")
print(f"Division: {num1/num2}")
print(f"Division entera: {num1//num2}")
print(f"Modulo: {num1%num2}")
print(f"Potencia: {num1**num2}")
