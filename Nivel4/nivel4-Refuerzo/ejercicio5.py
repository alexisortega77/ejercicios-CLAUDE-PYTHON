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