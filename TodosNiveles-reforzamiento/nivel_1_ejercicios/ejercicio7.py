# ------------------------------------------------------------
# EJERCICIO 7 — Desafío
# Pide año de nacimiento, mes actual y mes de cumpleaños.
# Calcula la edad exacta considerando si ya cumplió años este año.
# ------------------------------------------------------------
# Input: año=2000, mes_actual=3, mes_cumple=8
# Output esperado:
# Todavía no has cumplido años este año.
# Edad actual: 25 años
#
# Input: año=2000, mes_actual=10, mes_cumple=8
# Output esperado:
# Ya cumpliste años este año.
# Edad actual: 26 años

año_nacimiento=int(input("año nacimiento: "))
mes_actual=int(input("mes actual: "))
mes_nacimiento=int(input("mes nacimiento: "))

año_actual=2026
edad_actual=año_actual-año_nacimiento
if mes_actual>mes_nacimiento:
    print("Ya cumpliste años")
    print(f"Edad actual: {edad_actual}")
else:
     print("todavia no cumples años")
     print(f"Edad actual: {edad_actual-1}")


