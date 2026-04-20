"""
Ejercicio 4 — Medio
Dado una lista de estudiantes con calificaciones, usa comprehensions para generar estadísticas completas.
pythonstudents = [
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