"""
Ejercicio 5 — Medio
Dado un texto, crea un diccionario que agrupe las palabras por su longitud.
 Luego muestra cuántas palabras hay de cada longitud, ordenado de menor a mayor longitud.
Texto: "el gato y el perro son animales muy lindos"

Longitud 1: ['y'] → 1 palabra
Longitud 2: ['el', 'el'] → 2 palabras
Longitud 3: ['son', 'muy'] → 2 palabras
Longitud 5: ['gato', 'perro'] → 2 palabras  ← ojo, gato tiene 4 letras, ajusta el ejemplo
Longitud 7: ['animales'] → 1 palabra
Longitud 6: ['lindos'] → 1 palabra

💡 Tip: recorre las palabras, usa len(palabra) como clave del diccionario y agrega la palabra a la lista de ese largo. 
Si la clave no existe aún, inicialízala con [].
"""
texto    = "el gato y el perro son animales muy lindos"
palabras = texto.split()
grupo    = {}

for palabra in palabras:
    longitud = len(palabra)
    if longitud not in grupo:
        grupo[longitud] = []
    grupo[longitud].append(palabra)    # ← append, no =

for longitud in sorted(grupo):
    cantidad = len(grupo[longitud])
    plural   = "palabra" if cantidad == 1 else "palabras"
    print(f"Longitud {longitud}: {grupo[longitud]} → {cantidad} {plural}")

   
   # Solución óptima — con setdefault():
texto    = "el gato y el perro son animales muy lindos"
palabras = texto.split()
grupo    = {}

for palabra in palabras:
    grupo.setdefault(len(palabra), []).append(palabra)
    # setdefault devuelve la lista si ya existe, o crea [] si no existe
    # luego append agrega la palabra — todo en una línea

for longitud, palabras_grupo in sorted(grupo.items()):
    cantidad = len(palabras_grupo)
    plural   = "palabra" if cantidad == 1 else "palabras"
    print(f"Longitud {longitud}: {palabras_grupo} → {cantidad} {plural}")

"""
¿Cómo funciona setdefault(clave, default)?
pythongrupo = {}

# Sin setdefault — dos pasos
if longitud not in grupo:
    grupo[longitud] = []
grupo[longitud].append(palabra)

# Con setdefault — un paso
grupo.setdefault(longitud, []).append(palabra)
# Si longitud no existe → crea [] y lo devuelve → append agrega
# Si longitud ya existe → devuelve la lista existente → append agrega
    """