transacciones = [
    {"fecha": "2026-01-01", "tipo": "ingreso", "monto": 5000},
    {"fecha": "2026-01-05", "tipo": "gasto",   "monto": 1200},
    {"fecha": "2026-01-10", "tipo": "ingreso", "monto": 3000},
    {"fecha": "2026-01-15", "tipo": "gasto",   "monto": 800},
    {"fecha": "2026-01-20", "tipo": "ingreso", "monto": 2000},
    {"fecha": "2026-01-25", "tipo": "gasto",   "monto": 500},
]

def filtrar(transacciones, tipo):
    return [t for t in transacciones if t["tipo"] == tipo]

def reporte_financiero(transacciones):
    ingresos = filtrar(transacciones, "ingreso")
    gastos   = filtrar(transacciones, "gasto")

    total_ingresos = sum(t["monto"] for t in ingresos)
    total_gastos   = sum(t["monto"] for t in gastos)
    balance        = total_ingresos - total_gastos

    mayor_ingreso  = max(ingresos, key=lambda x: x["monto"])
    mayor_gasto    = max(gastos,   key=lambda x: x["monto"])

    signo = "+" if balance >= 0 else ""   # muestra + si es positivo

    print(f"Total ingresos:  ${total_ingresos:,}")   # :, agrega separador de miles
    print(f"Total gastos:    ${total_gastos:,}")
    print(f"Balance final:   {signo}${balance:,}")
    print(f"Mayor ingreso:   ${mayor_ingreso['monto']:,} ({mayor_ingreso['fecha']})")
    print(f"Mayor gasto:     ${mayor_gasto['monto']:,} ({mayor_gasto['fecha']})")

reporte_financiero(transacciones)


"""

¿Qué hace {valor:,}?
Es un formato de número que agrega separador de miles automáticamente:
pythonprint(f"{10000:,}")    # 10,000
print(f"{1200:,}")     # 1,200
print(f"{500:,}")      # 500
Muy útil para reportes financieros donde los números grandes son difíciles de leer sin separadores.
¿Por qué extraer filtrar() como función separada?
En la solución más común filtrar por "ingreso" y "gasto" son dos comprehensions casi idénticas. Cuando ves código repetido con solo un valor diferente, es señal de que se puede extraer una función:
python# Repetición — solo cambia el tipo
ingresos = [t for t in transacciones if t["tipo"] == "ingreso"]
gastos   = [t for t in transacciones if t["tipo"] == "gasto"]

# Función — elimina la repetición
def filtrar(transacciones, tipo):
    return [t for t in transacciones if t["tipo"] == tipo]

ingresos = filtrar(transacciones, "ingreso")
gastos   = filtrar(transacciones, "gasto")
"""