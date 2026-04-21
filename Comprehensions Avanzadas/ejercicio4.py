"""
Ejercicio 4 — Medio
Dado una lista de estudiantes con calificaciones, usa comprehensions para generar estadísticas completas.
python
students = [
    {"name": "Ana",    "grades": [90, 85, 92, 88]},
    {"name": "Luis",   "grades": [55, 62, 48, 70]},
    {"name": "María",  "grades": [78, 82, 75, 80]},
    {"name": "Carlos", "grades": [95, 98, 92, 97]},
]

# Output esperado:
averages  → {"Ana": 88.75, "Luis": 58.75, "María": 78.75, "Carlos": 95.5}
passing   → ["Ana", "María", "Carlos"]   # promedio >= 60
ranking   → [("Carlos", 95.5), ("Ana", 88.75), ("María", 78.75), ("Luis", 58.75)]
top_grade → ("Carlos", 98)               # estudiante con la calificación más alta
"""
students = [
    {"name": "Ana",    "grades": [90, 85, 92, 88]},
    {"name": "Luis",   "grades": [55, 62, 48, 70]},
    {"name": "María",  "grades": [78, 82, 75, 80]},
    {"name": "Carlos", "grades": [95, 98, 92, 97]},
]

averages  = {s["name"]: sum(s["grades"]) / len(s["grades"]) for s in students}
passing   = [name for name, avg in averages.items() if avg >= 60]
ranking   = sorted(averages.items(), key=lambda x: x[1], reverse=True)

best      = max(students, key=lambda s: max(s["grades"]))
top_grade = (best["name"], max(best["grades"]))
#Version optima 
"""top_grade = max(
    ((s["name"], max(s["grades"])) for s in students),
    key=lambda x: x[1]
)"""

print(averages)    # {"Ana": 88.75, "Luis": 58.75, "María": 78.75, "Carlos": 95.5}
print(passing)     # ["Ana", "María", "Carlos"]
print(ranking)     # [("Carlos", 95.5), ("Ana", 88.75), ("María", 78.75), ("Luis", 58.75)]
print(top_grade)   # ("Carlos", 98)