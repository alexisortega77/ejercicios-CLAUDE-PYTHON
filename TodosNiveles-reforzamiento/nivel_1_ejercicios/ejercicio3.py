# ------------------------------------------------------------
# EJERCICIO 3 — Fácil
# Pide nombre y apellido por separado, muéstralos unidos y en mayúsculas.
# ------------------------------------------------------------
# Input del usuario: ana / garcia
# Output esperado:
# Nombre completo: Ana Garcia
# En mayúsculas:   ANA GARCIA
# Iniciales:       A.G.
# Longitud del nombre completo: 9

nombre=input("Ingresa tu nombre: ")
apellido=input("Ingresa tu apellido: ")
nombre_completo=nombre+" "+apellido
mayusculas=nombre_completo.upper()
iniciales=nombre[0].upper()+"."+apellido[0].upper()
longitud=len(nombre_completo)

print(f"Nombre completo: {nombre_completo}")
print(f"En mayusculas: {mayusculas}")
print(f"Iniciales : {iniciales}")
print(f"Longitud del nombre completo completo: {longitud}")