"""
Ejercicio 6 — Medio
Usa zip() para procesar datos paralelos y crear estructuras combinadas.
python
names      = ["Ana", "Luis", "María", "Carlos"]
salaries   = [25000, 30000, 28000, 35000]
depts      = ["Sistemas", "Ventas", "RRHH", "Sistemas"]

# Output esperado:
employees     → [{"name": "Ana", "salary": 25000, "dept": "Sistemas"}, ...]
by_dept       → {"Sistemas": ["Ana", "Carlos"], "Ventas": ["Luis"], "RRHH": ["María"]}
avg_by_dept   → {"Sistemas": 30000.0, "Ventas": 30000.0, "RRHH": 28000.0}
highest_paid  → ("Carlos", 35000)

"""
names    = ["Ana", "Luis", "María", "Carlos"]
salaries = [25000, 30000, 28000, 35000]
depts    = ["Sistemas", "Ventas", "RRHH", "Sistemas"]

# Lista de diccionarios con zip
employees = [
    {"name": name, "salary": salary, "dept": dept}
    for name, salary, dept in zip(names, salaries, depts)
]

# Agrupar por departamento
by_dept = {}
for e in employees:
    by_dept.setdefault(e["dept"], []).append(e["name"])

# Promedio por departamento — dos pasos claros
dept_salaries = {
    dept: [e["salary"] for e in employees if e["dept"] == dept]
    for dept in {e["dept"] for e in employees}
}
avg_by_dept = {dept: sum(s) / len(s) for dept, s in dept_salaries.items()}

# El mejor pagado
highest_paid = max(employees, key=lambda e: e["salary"])
highest_paid = (highest_paid["name"], highest_paid["salary"])

print(employees)
print(by_dept)
print(avg_by_dept)
print(highest_paid)

"""
Solución óptima — con groupby conceptual y una sola pasada:
pythonfrom collections import defaultdict

names    = ["Ana", "Luis", "María", "Carlos"]
salaries = [25000, 30000, 28000, 35000]
depts    = ["Sistemas", "Ventas", "RRHH", "Sistemas"]

employees = [
    {"name": n, "salary": s, "dept": d}
    for n, s, d in zip(names, salaries, depts)
]

# Una sola pasada para agrupar nombres Y salarios
dept_data = defaultdict(lambda: {"names": [], "salaries": []})
for e in employees:
    dept_data[e["dept"]]["names"].append(e["name"])
    dept_data[e["dept"]]["salaries"].append(e["salary"])

by_dept     = {dept: data["names"]   for dept, data in dept_data.items()}
avg_by_dept = {dept: sum(data["salaries"]) / len(data["salaries"])
               for dept, data in dept_data.items()}

highest_paid = max(((e["name"], e["salary"]) for e in employees), key=lambda x: x[1])

print(employees)
print(by_dept)
print(avg_by_dept)
print(highest_paid)
¿Qué es defaultdict?
Es como un diccionario normal pero con un valor por defecto automático — elimina el if key not in dict o setdefault:
pythonfrom collections import defaultdict

# defaultdict(list) — si la clave no existe, crea [] automáticamente
grupos = defaultdict(list)
grupos["Sistemas"].append("Ana")    # no necesitas verificar si "Sistemas" existe
grupos["Sistemas"].append("Carlos")
grupos["Ventas"].append("Luis")
# {"Sistemas": ["Ana", "Carlos"], "Ventas": ["Luis"]}

# defaultdict(lambda: {"names": [], "salaries": []})
# — si la clave no existe, crea {"names": [], "salaries": []} automáticamente
"""