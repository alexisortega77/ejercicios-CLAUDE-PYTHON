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
texto = "Python es un lenguaje de programacion"
palabras = texto.lower().split()

# palabra más larga y corta
mas_larga = max(palabras, key=len)
mas_corta = min(palabras, key=len)

# promedio
total_letras = sum(len(p) for p in palabras)
promedio = total_letras / len(palabras)

print("Palabra más larga:", mas_larga, f"({len(mas_larga)} letras)")
print("Palabra más corta:", mas_corta, f"({len(mas_corta)} letras)")
print("Longitud promedio:", round(promedio, 2), "letras")

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
texto = "el gato y el perro son muy lindos"
palabras = texto.split()

grupos = {}

for palabra in palabras:
    longitud = len(palabra)
    
    if longitud not in grupos:
        grupos[longitud] = []
    
    grupos[longitud].append(palabra)

# mostrar ordenado
for longitud in sorted(grupos):
    print(f"{longitud} letras: {grupos[longitud]}")

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
texto = "el gato y el perro y el gato duerme y el perro juega"
palabras = texto.split()

frecuencia = {}

for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

# ordenar por frecuencia (de mayor a menor)
ordenado = sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)

top3 = ordenado[:3]

print("Top 3 palabras más frecuentes:")
for i, (palabra, veces) in enumerate(top3, 1):
    print(f"{i}. {palabra} → {veces} veces")