"""Ejercicio 1 — Fácil
Pide un número al usuario e imprime si es positivo, negativo o cero.
Ingresa un número: -5
El número es negativo.

Ingresa un número: 0
El número es cero."""
numero=int(input("Ingresa un numero: "))
if numero==0:
    print("El numero es cero.")
elif numero<0:
    print("es negativo.")
else:
    print("es positivo.")

"""Ejercicio 2 — Fácil
Imprime todos los números del 1 al 100 que sean divisibles entre 3 o entre 5. Al final imprime cuántos encontraste.
3, 5, 6, 9, 10, 12, 15 ...
Total encontrados: 47"""

contador=0
for i in range(1,10+1):
    if i%3==0 or i%5==0:
     print({i}, end=" ")
     contador+=1

print(f"Total de encontrados:", contador)

"""Ejercicio 3 — Fácil
Pide al usuario una palabra e imprime cada letra numerada.
Ingresa una palabra: Python
1 → P
2 → y
3 → t
4 → h
5 → o
6 → n"""

numletras=0
palabra=input("ingresa una palabra: ")
for letra in palabra:
   numletras+=1
   print(numletras,"->",letra)

"""Ejercicio 4 — Medio
Crea un programa que pida números al usuario en un while hasta que escriba 0. 
Al final imprime la suma, el promedio, el mayor y el menor.
Ingresa un número (0 para terminar): 4
Ingresa un número (0 para terminar): 8
Ingresa un número (0 para terminar): 2
Ingresa un número (0 para terminar): 0

Números ingresados: 3
Suma:     14
Promedio: 4.67
Mayor:    8
Menor:    2"""
contadorNum=0
suma=0
promedio=0
mayor=0
menor=0

numeroingresado=int(input("ingresa un numero: "))
while numeroingresado!=0:
   contadorNum+=1
   suma=suma+numeroingresado
   promedio=suma/contadorNum
   if numeroingresado>mayor:
      mayor=numeroingresado
   elif numeroingresado<menor:
      menor=numeroingresado 
   numeroingresado=int(input("ingresa un numero: "))

if numeroingresado==0:
   print(f"suma:{suma}")
   print(f"promedio:{promedio}")
   print(f"mayor:{mayor}")
   print(f"menor:{menor}")
   print(f"numeros ingresados:{contadorNum}")
"""OPTIMIZADO
numeros = []

numero = int(input("Ingresa un número (0 para terminar): "))
while numero != 0:
    numeros.append(numero)
    numero = int(input("Ingresa un número (0 para terminar): "))

if numeros:
    print(f"Números ingresados: {len(numeros)}")
    print(f"Suma:     {sum(numeros)}")
    print(f"Promedio: {sum(numeros) / len(numeros):.2f}")
    print(f"Mayor:    {max(numeros)}")
    print(f"Menor:    {min(numeros)}")
"""

"""Ejercicio 5 — Medio
Imprime el siguiente patrón usando bucles anidados. El tamaño lo decide el usuario.
Ingresa el tamaño: 5
*
* *
* * *
* * * *
* * * * *"""

patron=int(input("tamaño de patron: "))
for i in range(1,patron+1):
    print("")
    for j in range(1,i+1):
        print(end="*")
