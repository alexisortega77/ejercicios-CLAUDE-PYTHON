"""
Ejercicio 6 — Medio
Usa zip() para procesar datos paralelos y crear estructuras combinadas.
pythonnames      = ["Ana", "Luis", "María", "Carlos"]
salaries   = [25000, 30000, 28000, 35000]
depts      = ["Sistemas", "Ventas", "RRHH", "Sistemas"]

# Output esperado:
employees     → [{"name": "Ana", "salary": 25000, "dept": "Sistemas"}, ...]
by_dept       → {"Sistemas": ["Ana", "Carlos"], "Ventas": ["Luis"], "RRHH": ["María"]}
avg_by_dept   → {"Sistemas": 30000.0, "Ventas": 30000.0, "RRHH": 28000.0}
highest_paid  → ("Carlos", 35000)

"""