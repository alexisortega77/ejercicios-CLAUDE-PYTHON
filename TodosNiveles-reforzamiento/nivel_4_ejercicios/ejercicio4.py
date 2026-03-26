# ------------------------------------------------------------
# EJERCICIO 4 — Medio
# Analiza una lista de ventas mensuales.
# Cada venta es una tupla (mes, vendedor, monto).
# ------------------------------------------------------------
ventas = [
    ("enero",   "Ana",    15000),
    ("enero",   "Luis",   12000),
    ("febrero", "Ana",    18000),
    ("febrero", "Luis",    9000),
    ("marzo",   "Ana",    21000),
    ("marzo",   "Luis",   16000),
    ("marzo",   "María",  14000),
]

# Output esperado:
# Total por vendedor:
#   Ana:   $54000
#   Luis:  $37000
#   María: $14000
#
# Total por mes:
#   enero:    $27000
#   febrero:  $27000
#   marzo:    $51000
#
# Mejor vendedor: Ana ($54000)
# Mejor mes:      marzo ($51000)

total_vendedor={}
total_por_mes={}
for mes,vendedor, monto in ventas:
    total_vendedor[vendedor]=total_vendedor.get(vendedor,0)+monto
    total_por_mes[mes]=total_por_mes.get(mes,0)+monto

print("Total por vendedor")
for v, p in total_vendedor.items():
    print(f"v: {v} p: {p}")

print("Total por mes")
for m, c in total_por_mes.items():
    print(f"{m}:  ${c}")

mejor_vendedor=max(total_vendedor, key=total_vendedor.get)
print(f"mejor vendedor: {mejor_vendedor} (${total_vendedor[mejor_vendedor]})")

mejor_mes=max(total_por_mes, key=total_por_mes.get)
print(f"Mejor mes: {mejor_mes} (${total_por_mes[mejor_mes]})")