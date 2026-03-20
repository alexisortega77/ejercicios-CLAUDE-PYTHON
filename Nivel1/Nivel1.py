# Ejercicio 1
nombre = "Manuel Alexis"
edad = 23
ciudad = "Mexico"

print(f"Hola, me llamo {nombre}, tengo {edad} años y vivo en {ciudad}")


# Ejercicio 2
año_actual = 2026

nombre = input("¿Cuál es tu nombre? ")
año_nacimiento = int(input("¿En qué año naciste? "))
edad = año_actual - año_nacimiento

print(f"Hola {nombre}, tienes aproximadamente {edad} años.")


# Ejercicio 3
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

suma           = num1 + num2
resta          = num1 - num2
multiplicacion = num1 * num2
division       = num1 / num2

print(f"Suma:           {suma}")
print(f"Resta:          {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División:       {division}")

"""
Quieres texto + variables juntos
f"Hola {nombre}"
Solo quieres imprimir cosas separadasprint("Hola", nombre)
Nunca mezcles los dos en el mismo print
❌ print(f"Hola", {nombre})"""