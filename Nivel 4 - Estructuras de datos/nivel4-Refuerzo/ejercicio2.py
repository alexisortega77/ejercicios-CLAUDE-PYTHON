'''
Ejercicio 2 — Fácil
Tienes dos listas de estudiantes. Usando sets encuentra quiénes están en ambas listas, quiénes están solo en la primera y quiénes están solo en la segunda.
Lista A: ['Ana', 'Luis', 'María', 'Carlos', 'Pedro']
Lista B: ['Luis', 'Pedro', 'Sofía', 'María', 'Jorge']

En ambas listas:    {'Luis', 'María', 'Pedro'}
Solo en lista A:    {'Ana', 'Carlos'}
Solo en lista B:    {'Sofía', 'Jorge'}
'''
lista_a = ['Ana', 'Luis', 'María', 'Carlos', 'Pedro']
lista_b = ['Luis', 'Pedro', 'Sofía', 'María', 'Jorge']

set_lista_a=set(lista_a)
set_lista_b=set(lista_b)

print(f"Lista a: {lista_a}")
print(f"Lista a: {lista_b}")

print(f"En ambas listas: {set_lista_a&set_lista_b}")
print(f"Solo en lista A: {set_lista_a-set_lista_b}")
print(f"Solo en lista B: {set_lista_b-set_lista_a}")

'''
Solución más común:
python
lista_a = ['Ana', 'Luis', 'María', 'Carlos', 'Pedro']
lista_b = ['Luis', 'Pedro', 'Sofía', 'María', 'Jorge']

set_a = set(lista_a)
set_b = set(lista_b)

print(f"Lista A:         {lista_a}")
print(f"Lista B:         {lista_b}")
print(f"En ambas listas: {set_a & set_b}")
print(f"Solo en lista A: {set_a - set_b}")
print(f"Solo en lista B: {set_b - set_a}")
Solución óptima — con función reutilizable:
python
def comparar_listas(lista_a, lista_b):
    set_a = set(lista_a)
    set_b = set(lista_b)

    return {
        "en_ambas":    set_a & set_b,
        "solo_en_a":   set_a - set_b,
        "solo_en_b":   set_b - set_a,
        "en_ninguna":  set_a ^ set_b    # bonus — diferencia simétrica
    }

lista_a = ['Ana', 'Luis', 'María', 'Carlos', 'Pedro']
lista_b = ['Luis', 'Pedro', 'Sofía', 'María', 'Jorge']

resultado = comparar_listas(lista_a, lista_b)

print(f"En ambas listas: {resultado['en_ambas']}")
print(f"Solo en lista A: {resultado['solo_en_a']}")
print(f"Solo en lista B: {resultado['solo_en_b']}")
print(f"En ninguna:      {resultado['en_ninguna']}")
'''