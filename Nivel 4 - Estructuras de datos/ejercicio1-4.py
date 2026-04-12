"""
**Ejercicio 1 — Fácil**
Crea una lista con 5 frutas. Luego imprime la primera, la última, y las del medio. 
Después agrega una fruta al final, elimina la primera y muestra la lista final.
```
Lista original: ['manzana', 'pera', 'uva', 'mango', 'kiwi']
Primera: manzana
Última: kiwi
Del medio: ['pera', 'uva', 'mango']
Lista final: ['pera', 'uva', 'mango', 'kiwi', 'fresa']
```
"""
frutas=["manzana", "pera","uva", "mango", "kiwi"]

print("Lista Original: ", frutas)
print("Primera: ", frutas[0])
print("Ultima: ", frutas[-1])
#frutas[1:-1] siempre excluye el primero y el último sin importar el tamaño.
print("Del medio:", frutas[1:-1]) 

# remove() — elimina por VALOR, busca el elemento
frutas.remove("manzana")   # busca "manzana" y lo elimina
                           # error si "manzana" no existe

# pop(0) — elimina por POSICIÓN, siempre el índice 0
frutas.pop(0)              # elimina el primero sin importar qué valor tiene
                           # más seguro cuando sabes la posición, no el valor
frutas.pop(0)
frutas.append("fresa")
print("Lista Final: ", frutas)


"""
---

**Ejercicio 2 — Fácil**
Pide 5 números al usuario, guárdalos en una lista e imprime la suma, el promedio, el mayor y el menor. Sin usar funciones del Nivel 3.
```
Ingresa el número 1: 4
Ingresa el número 2: 8
...
Suma: 30
Promedio: 6.0
Mayor: 10
Menor: 2

"""
"""
# ❌ Tu versión — recalcula promedio, mayor y menor en cada vuelta
for i in range(1, 5+1):
    numero = int(input(f"Ingresa el numero {i}: "))
    numeros.append(numero)
    promedio = sum(numeros) / 5      # ← se recalcula 5 veces
    num_mayor = max(numeros)         # ← se recalcula 5 veces
    num_menor = min(numeros)         # ← se recalcula 5 veces
"""
numeros=[]
for i in range(1,5+1):
    numero=int(input(f"Ingresa el numero {i}: "))
    numeros.append(numero)
    promedio=sum(numeros)/5
    num_mayor=max(numeros)
    num_menor=min(numeros)
print("Suma: ", sum(numeros))
print(f"Promedio: {promedio}")
print(f"Mayor: {num_mayor}")
print(f"Menor: {num_menor}")
print(numeros)

"""
numeros = []

for i in range(1, 6):
    numero = int(input(f"Ingresa el número {i}: "))
    numeros.append(numero)

total = sum(numeros)
promedio = total / len(numeros)

print(f"Suma:     {total}")
print(f"Promedio: {promedio:.1f}")
print(f"Mayor:    {max(numeros)}")
print(f"Menor:    {min(numeros)}")
"""

"""

**Ejercicio 3 — Fácil**
Crea un diccionario con información de una persona (nombre, edad, ciudad, profesión). Imprime cada campo con su etiqueta. 
Luego actualiza la ciudad y agrega un campo nuevo.
```
Nombre:    Manuel
Edad:      23
Ciudad:    México
Profesión: Ingeniero
---
Ciudad actualizada: Guadalajara
Nuevo campo - Email: manuel@mail.com
```
"""
persona={
    "nombre":"Manuel",
    "edad": 23,
    "ciudad": "Mexico",
    "profesion": "ingeniero"
}
print("Nombre: ",persona["nombre"])
print("Edad: ",persona["edad"])
print("Ciudad: ",persona["ciudad"])
print("Profesion: ",persona["profesion"])
persona["ciudad"]="BCS"
print("Ciudad actualizada: ", persona["ciudad"])
persona["Email"]="Manuel@gmail.com"
print("Nuevo campo - Email: ", persona["Email"])


#SOLUCION MAS COMUN
persona = {
    "nombre": "Manuel",
    "edad": 23,
    "ciudad": "México",
    "profesion": "Ingeniero"
}

for clave, valor in persona.items():
    print(f"{clave.capitalize()}: {valor}")

print("---")
persona["ciudad"] = "Guadalajara"
print("Ciudad actualizada:", persona["ciudad"])

persona["email"] = "manuel@mail.com"
print("Nuevo campo - Email:", persona.get("email"))

"""

**Ejercicio 4 — Medio**
Crea una lista de 10 números con valores repetidos. Usando sets encuentra cuántos números únicos hay y cuáles son.
 Luego imprime los números que aparecen más de una vez.
```
Lista: [1, 2, 2, 3, 4, 4, 4, 5, 1, 3]
Únicos: {1, 2, 3, 4, 5}
Total únicos: 5
Repetidos: [1, 2, 3, 4]
```
> 💡 Tip: un número está repetido si `lista.count(numero) > 1`.
"""
lista_num = []
for i in range(1, 11):
    numero = int(input("Ingresa el numero: "))
    lista_num.append(numero)

repetidos = []
for num in lista_num:
    if lista_num.count(num) > 1 and num not in repetidos:
        repetidos.append(num)

print("Lista:", lista_num)
sin_duplicados = set(lista_num)
print("Unicos:", sin_duplicados)
print("Total unicos:", len(sin_duplicados))
print("Repetidos:", repetidos)

"""
lista_num = [1, 2, 2, 3, 4, 4, 4, 5, 1, 3]

sin_duplicados = set(lista_num)

repetidos = []
for num in lista_num:
    if lista_num.count(num) > 1 and num not in repetidos:
        repetidos.append(num)

print("Lista:        ", lista_num)
print("Únicos:       ", sin_duplicados)
print("Total únicos: ", len(sin_duplicados))
print("Repetidos:    ", sorted(repetidos))   # sorted() para mostrarlos ordenados
"""
#SOLUCION OPTIMA USANDO LIST COMPRESION
lista_num = [1, 2, 2, 3, 4, 4, 4, 5, 1, 3]

sin_duplicados = set(lista_num)
repetidos = list(set(num for num in lista_num if lista_num.count(num) > 1))
# Explicación paso a paso:
# 1. "for num in lista_num"        → recorre cada número
# 2. "if lista_num.count(num) > 1" → filtra solo los que aparecen más de una vez
# 3. "set(...)"                    → elimina duplicados de los repetidos
# 4. "list(...)"                   → convierte el set a lista

print("Lista:        ", lista_num)
print("Únicos:       ", sin_duplicados)
print("Total únicos: ", len(sin_duplicados))
print("Repetidos:    ", sorted(repetidos))