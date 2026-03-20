"""
Ejercicio 8 — Desafío
Crea un programa que analice un texto ingresado por el usuario y genere un reporte con las palabras más frecuentes.
 Usa un diccionario para contar las ocurrencias de cada palabra.
Ingresa un texto: el gato y el perro y el gato

Palabras encontradas: 7
Palabras únicas: 5
Frecuencia:
  el    → 3 veces
  gato  → 2 veces
  y     → 2 veces
  perro → 1 vez

💡 Tip: separa el texto en palabras con .split(), recorre la lista y usa un diccionario para llevar el conteo. 
Para ordenar por valor usa sorted(diccionario.items(), key=lambda x: x[1], reverse=True).
"""
def analizar_texto(texto):
    palabras = texto.lower().split()  # pasar a minúsculas y separar
    
    total_palabras = len(palabras)
    
    frecuencias = {}
    
    # contar palabras
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    
    palabras_unicas = len(frecuencias)
    
    # ordenar por frecuencia (de mayor a menor)
    ordenado = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)
    
    # mostrar resultados
    print(f"\nPalabras encontradas: {total_palabras}")
    print(f"Palabras únicas: {palabras_unicas}")
    print("Frecuencia:")
    
    for palabra, cantidad in ordenado:
        print(f"  {palabra} → {cantidad} veces")


# programa principal
texto = input("Ingresa un texto: ")
analizar_texto(texto)



"""
Solución más común:
def analizar_texto(texto):
    palabras  = texto.lower().split()
    frecuencias = {}

    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1

    ordenado = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)

    print(f"\nPalabras encontradas: {len(palabras)}")
    print(f"Palabras únicas:      {len(frecuencias)}")
    print("Frecuencia:")

    for palabra, cantidad in ordenado:
        vez_o_veces = "vez" if cantidad == 1 else "veces"
        print(f"  {palabra.ljust(10)} → {cantidad} {vez_o_veces}")


texto = input("Ingresa un texto: ")
analizar_texto(texto)
Solución óptima — con get() para simplificar el conteo:
def analizar_texto(texto):
    if not texto.strip():
        print("El texto está vacío.")
        return

    palabras    = texto.lower().split()
    frecuencias = {}

    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        # get(palabra, 0) devuelve el conteo actual o 0 si no existe aún
        # luego suma 1 — elimina el if/else completamente

    ordenado = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)

    print(f"\nPalabras encontradas: {len(palabras)}")
    print(f"Palabras únicas:      {len(frecuencias)}")
    print("Frecuencia:")

    for palabra, cantidad in ordenado:
        vez_o_veces = "vez" if cantidad == 1 else "veces"
        print(f"  {palabra.ljust(10)} → {cantidad} {vez_o_veces}")


texto = input("Ingresa un texto: ")
analizar_texto(texto)
¿Cómo funciona frecuencias.get(palabra, 0) + 1?
Es el patrón más común para contar con diccionarios. Reemplaza el if/else completo en una sola línea:
python# Tu versión — correcta pero más larga
if palabra in frecuencias:
    frecuencias[palabra] += 1
else:
    frecuencias[palabra] = 1

# Con get() — equivalente en una línea
frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
# Si "gato" no existe → get devuelve 0 → 0 + 1 = 1  (primera vez)
# Si "gato" existe con valor 1 → get devuelve 1 → 1 + 1 = 2 (segunda vez)
¿Cómo funciona sorted(..., key=lambda x: x[1], reverse=True)?
Ya lo usaste correctamente pero vale la pena entenderlo a fondo:
pythonfrecuencias.items()
# [("el", 3), ("gato", 2), ("y", 2), ("perro", 1)]
#      ↑ x[0]    ↑ x[1]
#      clave     valor

# key=lambda x: x[1] → ordena por el segundo elemento de cada tupla (el conteo)
# reverse=True        → de mayor a menor
La lambda recibe cada tupla ("el", 3) y devuelve 3. sorted() usa ese número para ordenar. Si quisieras ordenar alfabéticamente usarías key=lambda x: x[0].

"""