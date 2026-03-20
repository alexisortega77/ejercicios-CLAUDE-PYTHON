'''Ejercicio 1 — Fácil
Crea una lista de 8 números. Usando list comprehension crea tres listas nuevas: 
los números mayores a 10, los números elevados al cubo y los números convertidos a string con la palabra "número" adelante.
Original:  [3, 15, 7, 22, 1, 18, 9, 11]
Mayores a 10: [15, 22, 18, 11]
Cubos:     [27, 3375, 343, 10648, 1, 5832, 729, 1331]
Con texto: ['número 3', 'número 15', 'número 7'...]'''

lista_numeros= [3, 15, 7, 22, 1, 18, 9, 11]
mayores_a_10=[numero for numero in lista_numeros if numero>10]
cubos=[numero**3 for numero in lista_numeros]
numero_texto = [f"número {n}" for n in lista_numeros]
print(f"Original: {lista_numeros}")
print(f"Mayores a 10:{mayores_a_10}")
print(f"Cubos: {cubos}")
print(f"Con texto: {numero_texto}")

#SOLUCION OPTIMA
lista_numeros = [3, 15, 7, 22, 1, 18, 9, 11]

# zip() une tres listas en paralelo para recorrerlas juntas
resultados = {
    "Original":     lista_numeros,
    "Mayores a 10": [n for n in lista_numeros if n > 10],
    "Cubos":        [n ** 3 for n in lista_numeros],
    "Con texto":    [f"número {n}" for n in lista_numeros],
}

for etiqueta, valores in resultados.items():
    print(f"{etiqueta.ljust(14)}: {valores}")