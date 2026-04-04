"""
Ejercicio 2 — Fácil
Crea una función get_element(lista, index) que maneje índices fuera de rango.
get_element([1,2,3], 1)   → 2
get_element([1,2,3], 10)  → "Error: index 10 out of range"
get_element([1,2,3], "a") → "Error: index must be an integer"

"""
def get_element(lista, index):
    try:
       return lista[index]
    except IndexError:
        return f"Error: index {index} out of range"
    except TypeError:
         return "Error: Index must be an integer"
"""
#SOLUCION OPTIMA
def get_element(lista, index):
    if not isinstance(index, int):
        return "Error: index must be an integer"
    try:
        return lista[index]
    except IndexError:
        return f"Error: index {index} out of range"
Python favorece el estilo EAFP — intenta y maneja el error. 
Es más pythónico y generalmente más limpio. 
Tu versión con except TypeError es la forma más pythónica.
Sin embargo para validar tipos de entrada del usuario, isinstance es más explícito 
y deja claro que es una validación intencional, no un error inesperado.
"""

print(get_element([1,2,3], 1))   #→ 2
print(get_element([1,2,3], 10))  #→ "Error: index 10 out of range"
print(get_element([1,2,3], "a"))