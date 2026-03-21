"""

Aquí van 5 ejercicios enfocados exactamente en lo que te cuesta. Van de menos a más:

---

**Ejercicio A — Contar letras**
Pide una palabra y cuenta cuántas veces aparece cada letra. Muestra el resultado ordenado de mayor a menor frecuencia.
```
Palabra: banana
b → 1
a → 3
n → 2

Ordenado:
a → 3
n → 2
b → 1
```
> 💡 Es el mismo patrón de contar palabras pero con letras.

---
"""
palabra=input("Ingresa una palabra: ").lower()
conteo={}
print(f"Palabra: {palabra}")
for letra in palabra:
    conteo[letra]=conteo.get(letra,0)+1

print("Ordenado:")
for letra, cantidad in sorted(conteo.items(), key=lambda x: x[1], reverse=True):
    print(f"{letra} -> {cantidad}")



"""
**Ejercicio B — Palabras únicas y repetidas**
Dado un texto, muestra las palabras que aparecen exactamente una vez y las que aparecen más de una vez.
```
Texto: "el sol sale y el sol brilla y el cielo es azul"

Aparecen una vez:  ['sale', 'brilla', 'cielo', 'es', 'azul']
Aparecen más de una vez: ['el', 'sol', 'y'] (el:3, sol:2, y:2)
```
"""
texto= "el sol sale y el sol brilla y el cielo es azul"
texto=texto.lower().split()
palabras=texto
conteo_palabras={}
for palabra in palabras:
    conteo_palabras[palabra]=conteo_palabras.get(palabra,0)+1

duplicados=[]
sin_duplicar=[]

for palabra,cantidad in conteo_palabras.items():
    if cantidad==1:
        sin_duplicar.append(palabra)
    else:
        duplicados.append((palabra,cantidad))

"""
¿Notaste algo?
Tu versión usaba un for con if/else para separar únicas y repetidas. 
La solución común usa dos list comprehensions. 
Mira cómo tu código se transforma directamente:
python# Tu versión — for con if/else
for palabra, cantidad in conteo.items():
    if cantidad == 1:
        sin_duplicar.append(palabra)
    else:
        duplicados.append((palabra, cantidad))

# Versión con comprehension — exactamente lo mismo comprimido
una_vez   = [p       for p, c in conteo.items() if c == 1]
repetidas = [(p, c)  for p, c in conteo.items() if c > 1]
Esta es exactamente la transformación que hablamos — primero tu versión funcional, 
luego la comprimes. Tu lógica era correcta, solo faltaba el paso de comprimir.
"""

print("aparecen una vez", sin_duplicar)
# ✅ Formato del ejercicio
info = ", ".join(f"{p}:{c}" for p, c in duplicados)
print(f"Aparecen más de una vez: [{info}]")

"""
---

**Ejercicio C — Longitud promedio**
Dado un texto calcula la longitud promedio de las palabras, la palabra más larga y la más corta.
```
Texto: "Python es un lenguaje de programacion"

Palabra más larga:  programacion (12 letras)
Palabra más corta:  es (2 letras)
Longitud promedio:  5.71 letras
```
"""
texto_longitud="Python es un lenguaje de programacion"
texto_longitud=texto_longitud.lower().split()

for longitud in texto_longitud:
    cantidad_texto=longitud.split()
    print(cantidad_texto)


"""
---

**Ejercicio D — Agrupar por longitud**
Dado un texto agrupa las palabras por su longitud y muestra los grupos ordenados.
```
Texto: "el gato y el perro son muy lindos"

1 letra:  ['y']
2 letras: ['el', 'el']
3 letras: ['son', 'muy']
4 letras: ['gato']
5 letras: ['perro']
6 letras: ['lindos']
```
"""


"""
---

**Ejercicio E — Top 3 palabras**
Dado un texto encuentra las 3 palabras más frecuentes e imprímelas en formato de ranking.
```
Texto: "el gato y el perro y el gato duerme y el perro juega"

Top 3 palabras más frecuentes:
1. el    → 4 veces
2. y     → 3 veces
3. perro → 2 veces

💡 Tip: después de ordenar usa [:3] para tomar solo los primeros 3 elementos de la lista.
"""