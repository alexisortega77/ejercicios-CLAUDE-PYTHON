"""
Ejercicio 3 — Fácil
Crea una función read_age() que pida la edad al usuario y siga pidiendo hasta obtener un número entero válido entre 0 y 120.
Ingresa tu edad: hola
Error: debe ser un número entero.
Ingresa tu edad: -5
Error: la edad debe estar entre 0 y 120.
Ingresa tu edad: 25
Edad válida: 25
"""
def is_valid_age(age):
    return 0 <= age <= 120

def read_age():
    while True:
        try:
            age = int(input("Ingresa tu edad: "))
            if is_valid_age(age):
                print(f"Edad válida: {age}")
                return age
            print("Error: la edad debe estar entre 0 y 120.")
        except ValueError:
            print("Error: debe ser un número entero.")

read_age()