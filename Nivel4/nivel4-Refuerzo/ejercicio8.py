"""
Ejercicio 8 — Desafío
Crea un programa que lea una lista de transacciones (cada una es un diccionario con fecha, tipo y monto) 
y genere un reporte financiero.
pythontransacciones = [
    {"fecha": "2026-01-01", "tipo": "ingreso",  "monto": 5000},
    {"fecha": "2026-01-05", "tipo": "gasto",    "monto": 1200},
    {"fecha": "2026-01-10", "tipo": "ingreso",  "monto": 3000},
    {"fecha": "2026-01-15", "tipo": "gasto",    "monto": 800},
    {"fecha": "2026-01-20", "tipo": "ingreso",  "monto": 2000},
    {"fecha": "2026-01-25", "tipo": "gasto",    "monto": 500},
]
```
```
Total ingresos:  $10000
Total gastos:    $2500
Balance final:   $7500
Mayor ingreso:   $5000 (2026-01-01)
Mayor gasto:     $1200 (2026-01-05)

💡 Tip: filtra las transacciones por tipo con list comprehension, luego usa max() con key=lambda x: x["monto"] para encontrar la mayor.
"""
transacciones = [
    {"fecha": "2026-01-01", "tipo": "ingreso", "monto": 5000},
    {"fecha": "2026-01-05", "tipo": "gasto",   "monto": 1200},
    {"fecha": "2026-01-10", "tipo": "ingreso", "monto": 3000},
    {"fecha": "2026-01-15", "tipo": "gasto",   "monto": 800},
    {"fecha": "2026-01-20", "tipo": "ingreso", "monto": 2000},
    {"fecha": "2026-01-25", "tipo": "gasto",   "monto": 500},
]

def reporte_financiero(transacciones):
    ingresos = [t for t in transacciones if t["tipo"] == "ingreso"]
    gastos   = [t for t in transacciones if t["tipo"] == "gasto"]

    total_ingresos = sum(t["monto"] for t in ingresos)
    total_gastos   = sum(t["monto"] for t in gastos)
    balance        = total_ingresos - total_gastos

    mayor_ingreso  = max(ingresos, key=lambda x: x["monto"])
    mayor_gasto    = max(gastos,   key=lambda x: x["monto"])

    print(f"Total ingresos: ${total_ingresos}")
    print(f"Total gastos:   ${total_gastos}")
    print(f"Balance final:  ${balance}")
    print(f"Mayor ingreso:  ${mayor_ingreso['monto']} ({mayor_ingreso['fecha']})")
    print(f"Mayor gasto:    ${mayor_gasto['monto']} ({mayor_gasto['fecha']})")

reporte_financiero(transacciones)