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
