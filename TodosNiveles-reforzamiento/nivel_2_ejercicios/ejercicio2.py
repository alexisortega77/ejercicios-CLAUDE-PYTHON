
# ------------------------------------------------------------
# EJERCICIO 2 — Fácil
# Imprime los múltiplos de 7 entre 1 y 100.
# Al final muestra cuántos encontraste.
# ------------------------------------------------------------
# Output esperado:
# 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98
# Total de múltiplos de 7 entre 1 y 100: 14
contador=0
for i in range(1,101):
    if i % 7==0:
        print(i, end=" ")
        contador+=1


print("\ntotal de multiplos de 7: ",contador)