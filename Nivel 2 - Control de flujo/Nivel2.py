# Ejercicio 1
numero_dia = int(input("¿que numero de dia es?"))
if numero_dia==1:
    print("es Lunes")
elif numero_dia==2:
    print("es martes")
elif numero_dia==3:
    print("es miercoles")
elif numero_dia==4:
    print("es jueves")
elif numero_dia==5:
    print("es viernes")
elif numero_dia==6:
    print("es sabado")
elif numero_dia==7:
    print("es domingo")
else:
    print("Numero invalido.")

#Ejercicio 2
for i in range(1,11):
    i=int(input("de que numero desea la tabla de multiplicar"))
    for j in range(1,11):
        multiplicacion=j*i
        print((i), f"x {j}= ",(multiplicacion))

#Ejercicio 3
numero_mayor=0
contador=0
numero=int(input("ingresa un numero"))
while numero!=0:
    contador+=1
    if numero>numero_mayor:
        numero_mayor=numero
    numero = int(input("Ingresa un número (0 para terminar): "))   
print(f"ingresaste {contador} numeros y el numero mas mayor fue: {numero_mayor}")

# Ejercicio 1al 3 optimizado
numero_dia = int(input("¿Qué número de día es? "))

dias = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}

if numero_dia in dias:
    print(f"El día {numero_dia} es: {dias[numero_dia]}")
else:
    print("Número inválido. Ingresa un número del 1 al 7.")


# solucion comun ejercicio 2
numero = int(input("¿De qué número quieres la tabla? "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# solucion optima ejercicio 2
numero = int(input("¿De qué número quieres la tabla? "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")


#solucion comun ejercicio 3
numero_mayor = None
contador = 0

numero = int(input("Ingresa un número (0 para terminar): "))

while numero != 0:
    contador += 1
    if numero_mayor is None or numero > numero_mayor:
        numero_mayor = numero
    numero = int(input("Ingresa un número (0 para terminar): "))

print(f"Ingresaste {contador} números. El mayor fue: {numero_mayor}")

# Solucion optimizada ejercicio 3 con 
numeros = []
numero = int(input("Ingresa un número (0 para terminar): "))

while numero != 0:
    numeros.append(numero)
    numero = int(input("Ingresa un número (0 para terminar): "))

if numeros:
    print(f"Ingresaste {len(numeros)} números. El mayor fue: {max(numeros)}")


"""Ejercicio 4 — Medio
Pide al usuario un número entero positivo e imprime todos sus divisores. Al final indica si el número es primo.
Ingresa un número: 12
Divisores de 12: 1, 2, 3, 4, 6, 12
12 no es primo.

Ingresa un número: 7
Divisores de 7: 1, 7
7 es primo.

💡 Tip: un número n es divisor si numero % n == 0."""
# Solucion EJERCICIO 4
numero = int(input("Ingresa un número: "))
divisores = []

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(i)

print(f"Divisores de {numero}: {', '.join(str(d) for d in divisores)}")

if len(divisores) == 2:
    print(f"{numero} es primo.")
else:
    print(f"{numero} no es primo.")



"""Ejercicio 5 — Desafío
Crea un juego de adivinar el número. El programa "piensa" en el número 42. El usuario tiene 5 intentos para adivinarlo. 
En cada intento le dices si el número secreto es mayor o menor. Si lo adivina, felicítalo y di en cuántos intentos lo logró. 
Si se acaban los intentos, revela el número.
Adivina el número (tienes 5 intentos)
Intento 1: 50
Demasiado alto.
Intento 2: 30
Demasiado bajo.
Intento 3: 42
¡Correcto! Lo adivinaste en 3 intentos.

💡 Tip: necesitas un for para los intentos y un if dentro para comparar. Usa break cuando adivine."""

#Solucion EJERCICIO 5
numero_secreto = 42

print("Adivina el número (tienes 5 intentos)")

for intento in range(1, 6):
    guess = int(input(f"Intento {intento}: "))

    if guess == numero_secreto:
        print(f"¡Correcto! Lo adivinaste en {intento} intentos.")
        break
    elif guess > numero_secreto:
        print("Demasiado alto.")
    else:
        print("Demasiado bajo.")
else:
    print(f"Se acabaron los intentos. El número era {numero_secreto}.")