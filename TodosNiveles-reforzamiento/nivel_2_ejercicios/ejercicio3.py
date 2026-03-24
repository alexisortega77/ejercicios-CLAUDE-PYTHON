
# ------------------------------------------------------------
# EJERCICIO 3 — Fácil
# Pide un número N e imprime su tabla de multiplicar del 1 al 10.
# Marca con (!) los resultados mayores a 50.
# ------------------------------------------------------------
# Input: 6
# Output esperado:
# Tabla del 6:
# 6 x 1  = 6
# 6 x 2  = 12
# 6 x 3  = 18
# 6 x 4  = 24
# 6 x 5  = 30
# 6 x 6  = 36
# 6 x 7  = 42
# 6 x 8  = 48
# 6 x 9  = 54  (!)
# 6 x 10 = 60  (!)

num=int(input("ingresa un numero: "))
for i in range(1,11):
    result=num*i
    marc="(!)" if result>50 else ""
    print(f"{num} x {i} = {result} {marc}")
