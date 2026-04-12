'''Ejercicio 3 — Fácil
Crea un diccionario que mapee los meses del año a su número de días. Luego implementa tres consultas: 
imprimir todos los meses con más de 30 días, el mes con menos días y la suma total de días del año.
Meses con más de 30 días: enero, marzo, mayo...
Mes con menos días: febrero (28)
Total de días: 365'''

meses = {
    "enero": 31,
    "febrero": 28,
    "marzo": 31,
    "abril": 30,
    "mayo": 31,
    "junio": 30,
    "julio": 31,
    "agosto": 31,
    "septiembre": 30,
    "octubre": 31,
    "noviembre": 30,
    "diciembre": 31
}
#meses_mayore=[mes for mes,dia in meses.items() if dia>=30]
#meses_menores=[mes for mes,dia in meses.items() if dia<30]
def meses_mayores(meses):
    calculo = [mes for mes, dia in meses.items() if dia > 30]
    return calculo

def meses_menores(meses):
    calculo = [f"{mes} ({dia})" for mes, dia in meses.items() if dia < 30]
    return calculo


print("Meses con más de 30 días:", ", ".join(meses_mayores(meses)))
print("Mes con menos días:", ", ".join(meses_menores(meses)))
print("Total de días:", sum(meses.values()))


#SOLUCION OPTIMA
"""
meses = {
    "enero": 31, "febrero": 28, "marzo": 31,
    "abril": 30, "mayo": 31,   "junio": 30,
    "julio": 31, "agosto": 31, "septiembre": 30,
    "octubre": 31, "noviembre": 30, "diciembre": 31
}

def reporte_meses(meses):
    mas_30    = [mes for mes, dias in meses.items() if dias > 30]
    menos_30  = [mes for mes, dias in meses.items() if dias < 30]
    mes_mayor = max(meses, key=lambda m: meses[m])
    mes_menor = min(meses, key=lambda m: meses[m])
    total     = sum(meses.values())

    print(f"Meses con más de 30 días:  {', '.join(mas_30)}")
    print(f"Meses con menos de 30 días:{', '.join(menos_30)}")
    print(f"Mes con más días:          {mes_mayor} ({meses[mes_mayor]})")
    print(f"Mes con menos días:        {mes_menor} ({meses[mes_menor]})")
    print(f"Total de días:             {total}")

reporte_meses(meses)
"""

"""
¿Cómo funciona min(meses, key=lambda m: meses[m])?
min() recorre las claves del diccionario y usa la lambda para saber qué valor comparar. 
En cada vuelta m es el nombre del mes, y meses[m] es su número de días. min() devuelve la clave cuyo valor es el menor:
           min(meses, key=lambda m: meses[m])
# Compara: enero→31, febrero→28, marzo→31...
# Devuelve: "febrero" porque 28 es el mínimo
"""