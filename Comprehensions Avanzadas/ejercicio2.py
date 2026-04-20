"""
Ejercicio 2 — Fácil
Usa map() y filter() para procesar una lista de strings.
 Convierte a mayúsculas, filtra las que tienen más de 4 caracteres y crea un set de iniciales.
python

mayusculas  → ["PYTHON", "ES", "UN", "LENGUAJE", "MUY", "PODEROSO", "Y", "VERSATIL"]
largas      → ["python", "lenguaje", "poderoso", "versatil"]
iniciales   → {"p", "l", "v"}    # set de iniciales de las largas

"""
words = ["python", "es", "un", "lenguaje", "muy", "poderoso", "y", "versatil"]


# map() para transformar
mayusculas = list(map(str.upper, words))
# str.upper es la función directamente — sin lambda

# filter() para filtrar
long_words = list(filter(lambda w: len(w) > 4, words))

# set comprehension para iniciales
iniciales  = {w[0] for w in long_words}

print(mayusculas)   # ["PYTHON", "ES", "UN", "LENGUAJE", "MUY", "PODEROSO", "Y", "VERSATIL"]
print(long_words)   # ["python", "lenguaje", "poderoso", "versatil"]
print(iniciales)    # {"p", "l", "v"}