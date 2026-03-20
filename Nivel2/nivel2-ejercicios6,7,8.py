"""Ejercicio 6 — Medio
Crea una calculadora con menú. El programa muestra las opciones, 
el usuario elige una operación, ingresa dos números y ve el resultado. 
Después pregunta si quiere hacer otra operación.
--- Calculadora ---
1. Suma
2. Resta
3. Multiplicación
4. División
5. Salir

Elige una opción: 1
Primer número: 10
Segundo número: 5
Resultado: 15

¿Deseas otra operación? (s/n): s"""
suma=0
resta=0
multiplicacion=0
division=0
print("1. Suma: ")
print("2. Resta: ")
print("3. Multiplicacion: ")
print("4. Division: ")    
print("5. Salir: ")
opcion=int(input("ingresa el numero de operacion que quieras realizar:"))

while opcion!=5:
   
    num1=int(input("ingresa el primer numero: "))
    num2=int(input("ingresa el primer numero: "))

    if opcion==1:
        suma=num1+num2
        print(f"resultado: {suma}")    
    elif opcion==2:
        resta=num1-num2
        print(f"resultado: {resta}")
    elif opcion==3:
        multiplicacion=num1*num2
        print(f"resultado: {multiplicacion}")
    elif opcion==4:
        division=num1/num2
        print(f"resultado: {division}")
    continuar=input("deseas hacer otra operacion: s/n:").lower()
    if continuar == "s":
     print("1. Suma: ")
     print("2. Resta: ")
     print("3. Multiplicacion: ")
     print("4. Division: ")    
     print("5. Salir: ")
     opcion=int(input("ingresa el numero de operacion que quieras realizar:"))
    else: 
        break


"""Ejercicio 7 — Desafío
Crea un programa que le pida al usuario una frase y cuente cuántas vocales, 
cuántas consonantes y cuántos espacios tiene. Ignora mayúsculas/minúsculas.
Ingresa una frase: Hola Mundo
Vocales:     4
Consonantes: 6
Espacios:    1

💡 Tip: recorre la frase letra por letra con for. 
Convierte todo a minúsculas con .lower() antes de checar. 
Las vocales son "aeiou", puedes checar con if letra in "aeiou"."""

contadorVocales=0
ContadorEspacios=0
contadorConsonantes=0
frase=input("Ingresa una frase: ").lower()
print(frase)

for letra in frase:
    if letra==" ":
     ContadorEspacios+=1
    elif letra in "aeiou":
     contadorVocales+=1
    elif letra.isalpha():     
     contadorConsonantes+=1
print("Vocales: ",contadorVocales)
print("Consonantes: ",contadorConsonantes)
print("Espacios: ",ContadorEspacios)

"""Ejercicio 8 — Desafío
Genera la secuencia de Fibonacci hasta un límite que el usuario defina. 
La secuencia empieza con 0 y 1, y 
cada número siguiente es la suma de los dos anteriores.
¿Hasta qué número quieres la secuencia? 100
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

💡 Tip: necesitas dos variables, a = 0 y b = 1. 
En cada vuelta imprimes a, luego actualizas: a, b = b, a + b. 
Esto es un swap simultáneo, una característica única de Python."""

a=0
b=1
limite=int(input("Ingrese el limite: "))
while limite>a:
   print(a, end=" ")
   c=a+b
   a=b
   b=c


#SOLUCION MAS COMUN
limite1=int(input("Ingrese el limite: "))
while a<=limite1:
   print(a, end=", ")
   a, b=b,a+b
    