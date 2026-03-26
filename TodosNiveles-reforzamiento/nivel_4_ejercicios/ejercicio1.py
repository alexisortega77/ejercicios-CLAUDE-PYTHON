# ------------------------------------------------------------
# EJERCICIO 1 — Fácil
# Dada una lista de números, crea con list comprehension:
# - Solo los impares
# - Los que son divisibles entre 3
# - Cada número multiplicado por su índice
# ------------------------------------------------------------
numeros = [4, 7, 12, 3, 18, 5, 21, 8, 9, 15]

# Output esperado:
# Original:          [4, 7, 12, 3, 18, 5, 21, 8, 9, 15]
# Impares:           [7, 3, 5, 21, 9, 15]
# Divisibles entre 3:[12, 3, 18, 21, 9, 15]
# Por su índice:     [0, 7, 24, 9, 72, 25, 126, 56, 72, 135]


impares=[p for p in numeros if not p%2==0]
entre_tres=[p for p in numeros if p%3==0]
indice=[p*i for p,i in enumerate(numeros)]

print(f"Original: {numeros}")
print(f"impares: {impares}")
print(f"Divisibles entre 3: {entre_tres}")
print(f"Por su indice: {indice}")