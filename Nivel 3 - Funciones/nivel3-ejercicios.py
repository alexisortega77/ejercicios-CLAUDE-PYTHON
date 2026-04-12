"""**Ejercicio 1 — Fácil**
Crea una función llamada `saludar` que reciba un nombre y devuelva un saludo. 
Luego llámala 3 veces con nombres diferentes.
```
Buenos días, Manuel!
Buenos días, Ana!
Buenos días, Carlos!
```

---
"""
def saludar(nombre):
    return f"Buenos días, {nombre}!"

print(saludar("Alexis"))    # imprimes desde afuera
print(saludar("Manuel"))
print(saludar("Megan"))

""""
**Ejercicio 2 — Fácil**
Crea una función `es_par` que reciba un número y devuelva 
`True` si es par y `False` si es impar. 
Luego úsala en un bucle para imprimir cuáles son pares del 1 al 10.
```
1 → impar
2 → par
3 → impar
...
```"""
def es_par(numero):
    return numero % 2 == 0   # devuelve True o False directamente



for i in range(1, 11):
    tipo = "par" if es_par(i) else "impar"
    print(f"{i} → {tipo}")
"""
**Ejercicio 3 — Fácil**
Crea una función `calcular_area` que reciba base y altura y devuelva el área de un triángulo 
(`base * altura / 2`). Llámala con 3 triángulos diferentes e imprime los resultados.
```
Triángulo 1: área = 15.0
Triángulo 2: área = 24.0
Triángulo 3: área = 6.5
```
"""

def calcular_area(base, altura):
    """Devuelve el área de un triángulo dada su base y altura."""
    return base * altura / 2

triangulos = [(10, 3), (8, 6), (5, 2.6),(6,3)]

for i, (base, altura) in enumerate(triangulos, start=1):
    print(f"Triángulo {i}: área = {calcular_area(base, altura)}")

"""**Ejercicio 4 — Medio**
Crea una función `mayor_de_tres` que reciba tres números y devuelva el mayor. Sin usar `max()`.
```
mayor_de_tres(3, 7, 2)  →  7
mayor_de_tres(10, 5, 8) →  10
```

"""
def mayor_de_tres(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= c:
        return b
    return c
    
print(mayor_de_tres(6,6,3))
print(mayor_de_tres(10,11,3))
print(mayor_de_tres(10,6,12))


"""
**Ejercicio 5 — Medio**
Crea una función `contar_vocales` que reciba una palabra y devuelva cuántas vocales tiene. 
Luego pide una frase al usuario, sepárala en palabras y muestra el conteo de vocales de cada una.
```
Ingresa una frase: Hola mundo Python
Hola    → 2 vocales
mundo   → 2 vocales
Python  → 1 vocal
```
> 💡 Tip: puedes separar una frase en palabras con `frase.split()`. Eso devuelve una lista que puedes recorrer con `for`.

---"""

def contar_vocales(palabra):
    contador = 0
    for letra in palabra.lower():
        if letra in "aeiou":
            contador += 1
    return contador

frase = input("Ingresa una frase: ")

for palabra in frase.split():
    total = contar_vocales(palabra)
    texto = "vocal" if total == 1 else "vocales"
    print(f"{palabra} → {total} {texto}")
"""

**Ejercicio 6 — Medio**
Crea una función `calculadora` que reciba dos números y una operación como string (`"suma"`, `"resta"`, `"multiplicacion"`, `"division"`),
 y devuelva el resultado. Si la operación no existe, devuelve un mensaje de error.
```
calculadora(10, 5, "suma")          →  15
calculadora(10, 5, "division")      →  2.0
calculadora(10, 0, "division")      →  "Error: división entre cero"
calculadora(10, 5, "potencia")      →  "Operación no reconocida"
```
"""
def calculadora(num1, num2, operacion):
    if operacion == "suma":
        return num1 + num2
    elif operacion == "resta":
        return num1 - num2
    elif operacion == "multiplicacion":
        return num1 * num2
    elif operacion == "division":
        if num2 == 0:
            return "Error: división entre cero"
        return num1 / num2
    else:
        return "Operación no reconocida"

print(calculadora(3,0,"division"))
#Solución óptima — con diccionario de operaciones:python
def calculadora(num1, num2, operacion):
    operaciones = {
        "suma":           lambda a, b: a + b,
        "resta":          lambda a, b: a - b,
        "multiplicacion": lambda a, b: a * b,
    }

    if operacion == "division":
        if num2 == 0:
            return "Error: división entre cero"
        return num1 / num2

    if operacion not in operaciones:
        return "Operación no reconocida"

    return operaciones[operacion](num1, num2)

"""
**Ejercicio 7 — Desafío**
Crea un sistema de calificaciones con tres funciones:
- `promedio(calificaciones)` — recibe una lista de números y devuelve el promedio
- `letra(promedio)` — recibe el promedio y devuelve la letra (A, B, C, D, F)
- `reporte(nombre, calificaciones)` — llama a las dos anteriores e imprime el reporte completo
```
reporte("Manuel", [85, 90, 78, 92, 88])

Estudiante: Manuel
Calificaciones: 85, 90, 78, 92, 88
Promedio: 86.60
Letra: B

💡 Escala: A=90+, B=80+, C=70+, D=60+, F=menos de 60
"""
def promedio(calificaciones):
    contador_calif=0
    suma=0
    for calificacion in calificaciones:
     contador_calif+=1
     suma=suma+calificacion
    return suma/contador_calif

def letra(promedio):
    if promedio>=90:
        return "A"
    elif promedio>=80:
        return "B"
    elif promedio>=70:
        return "C"
    elif promedio>=60:
        return "D"
    else:
     return "F"

def reporte(nombre, calificaciones):
    print(f"Estudiante: {nombre}")
    calif=promedio(calificaciones)
    asignacion=letra(promedio(calificaciones))
    print("Calificaciones:",",".join(str(n)for n in calificaciones))
    print(f"Promedio: {calif}")
    print(f"Letra: {asignacion}")


  #  return calif, asignacion

print(promedio([85,90,0,62,0]))
print(letra(promedio([85,90,0,62,0])))

reporte("Manuel", [85,90,78,92,88])

# SOLUCION COMUN Y SIMPLIFICADA
def promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)

def letra(promedio):
    if promedio >= 90:
        return "A"
    elif promedio >= 80:
        return "B"
    elif promedio >= 70:
        return "C"
    elif promedio >= 60:
        return "D"
    else:
        return "F"

def reporte(nombre, calificaciones):
    prom = promedio(calificaciones)
    asignacion = letra(prom)

    print(f"Estudiante: {nombre}")
    print(f"Calificaciones: {', '.join(str(n) for n in calificaciones)}")
    print(f"Promedio: {prom:.2f}")
    print(f"Letra: {asignacion}")

reporte("Manuel", [85, 90, 78, 92, 88])