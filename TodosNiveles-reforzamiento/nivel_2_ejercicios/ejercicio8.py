
# ------------------------------------------------------------
# EJERCICIO 8 — Desafío
# Genera un triángulo de números. El usuario elige el tamaño.
# Cada fila muestra el número de fila repetido N veces.
# ------------------------------------------------------------
# Input: 5
# Output esperado:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
numero=int(input("ingresa numero: "))
for i in range(1,numero+1):
    for j in range(1,i+1):
      print(i,end=" ")
    print()