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
print(len(dict2))
print(len(dict1))

def combinar_diccionario (dic1,dict2):
    resultado={}
    for clave,valor in dic1.items():
        resultado[clave]=valor

    for clave,valor in dict2.items():
        resultado[clave]=resultado.get(clave,0)+valor


    return resultado

print(combinar_diccionario(dict1,dict2))