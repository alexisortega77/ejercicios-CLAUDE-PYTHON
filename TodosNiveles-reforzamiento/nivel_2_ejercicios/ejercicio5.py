
# ------------------------------------------------------------
# EJERCICIO 5 — Medio
# Imprime los primeros N números de la secuencia de Fibonacci.
# (no hasta un límite, sino exactamente N números)
# ------------------------------------------------------------
# Input: 8
# Output esperado:
# Fibonacci (8 números):
# 0, 1, 1, 2, 3, 5, 8, 13

num=int(input("ingresa un numero: "))
a=0
b=1
for i in range(1,num+1):
    print(a, end=" ")
    c=a+b
    b=a
    a=c