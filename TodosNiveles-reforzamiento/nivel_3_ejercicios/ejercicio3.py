# ------------------------------------------------------------
# EJERCICIO 3 — Fácil
# Crea una función que reciba un texto y devuelva
# un diccionario con sus estadísticas básicas.
# ------------------------------------------------------------
# Output esperado:
# analizar("Hola Mundo Python")
# → {
#     "palabras": 3,
#     "caracteres": 18,
#     "vocales": 5,
#     "mayusculas": 3
#   }
def analizar(frase):
    palabras=len(frase.split())
    caracteres=len(frase)

    vocales=0
    mayusculas=0


    for letra in frase:
        if letra.lower() in "aeiou":
            vocales+=1
        if letra.isupper():
            mayusculas+=1

    return {"palabras": palabras, 
            "caracteres":caracteres,
            "vocales":vocales,
            "mayusculas":mayusculas
            }

print(analizar("HABIA una vez "))
print(analizar("Hola Mundo Python"))