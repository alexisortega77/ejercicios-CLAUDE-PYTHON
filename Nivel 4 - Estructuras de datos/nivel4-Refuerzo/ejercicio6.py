"""
Ejercicio 6 — Medio
Crea una función combinar_diccionarios que reciba dos diccionarios y devuelva uno nuevo con todas las claves. 
Si una clave existe en ambos, suma los valores.
dict1 = {"manzana": 5, "pera": 3, "uva": 8}
dict2 = {"pera": 2, "uva": 1, "mango": 4}

resultado = {"manzana": 5, "pera": 5, "uva": 9, "mango": 4}

💡 Tip: recorre el primer diccionario y cópialo al resultado. Luego recorre el segundo — si la clave ya existe suma, si no existe agrégala.


"""
dict1 = {"manzana": 5, "pera": 3, "uva": 8}
dict2 = {"pera": 2, "uva": 1, "mango": 4}

def combinar_diccionarios(dict1, dict2):
    resultado = {}

    for clave, valor in dict1.items():
        resultado[clave] = valor

    for clave, valor in dict2.items():
        resultado[clave] = resultado.get(clave, 0) + valor

    return resultado

print(combinar_diccionarios(dict1, dict2))
# {"manzana": 5, "pera": 5, "uva": 9, "mango": 4}

#Solución óptima — con .copy() y un solo loop:
def combinar_diccionarios(dict1, dict2):
    resultado = dict1.copy()   # copia dict1 de una vez, sin loop
    
    for clave, valor in dict2.items():
        resultado[clave] = resultado.get(clave, 0) + valor
    
    return resultado
"""
¿Por qué .copy() en vez del primer loop?
Tu primer for hace exactamente lo mismo que .copy() — 
copiar todas las claves y valores del dict1 al resultado. Python ya tiene una función para eso:
"""