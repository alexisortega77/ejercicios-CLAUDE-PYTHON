

# ------------------------------------------------------------
# EJERCICIO 6 — Medio
# Pide una palabra y cuenta sin usar count() ni funciones de listas:
# vocales, consonantes, espacios y su longitud total.
# ------------------------------------------------------------
# Input: murcielago
# Output esperado:
# Palabra: murcielago
# Longitud:     10
# Vocales:      5
# Consonantes:  5
# Espacios:     0
vocales="aeiou"
espacios=" "
consonantes="qwrtyplkjhgfdsmnbvcxz"
contador_vocales=0
contador_consonantes=0
contador_espacios=0

word=input("ingresa una palabra: ")
for i in word:
    if i in vocales:
        contador_vocales+=1
    elif i in consonantes:
        contador_consonantes+=1
    elif i in espacios:
        contador_espacios+=1

longitud=len(word)
print(f"palabra: {word}")
print(f"longitud: {longitud}")
print(f"vocales: {contador_vocales}")
print(f"consonantes: {contador_consonantes}")
print(f"espacios: {contador_espacios}")