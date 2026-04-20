"""
Ejercicio 7 — Desafío
Implementa un mini motor de búsqueda sobre una lista de artículos usando solo comprehensions y funciones de alto orden.
pythonarticles = [
    {"title": "Python basics",           "tags": ["python", "beginner"],          "views": 1500},
    {"title": "Advanced Python",         "tags": ["python", "advanced"],          "views": 800},
    {"title": "Data Science with Python","tags": ["python", "data", "science"],   "views": 3200},
    {"title": "Web dev with Django",     "tags": ["python", "web", "django"],     "views": 2100},
    {"title": "Machine Learning intro",  "tags": ["ml", "data", "science"],       "views": 4500},
]

# Búsqueda por tag
search("python")  → ["Python basics", "Advanced Python", "Data Science with Python", "Web dev with Django"]

# Ordenar por views
top_3()           → ["Machine Learning intro", "Data Science with Python", "Web dev with Django"]

# Artículos con múltiples tags en común
related("python", "data")  → ["Data Science with Python"]

# Estadísticas
stats()
→ {
    "total":        5,
    "avg_views":    2420.0,
    "most_viewed":  "Machine Learning intro",
    "all_tags":     {"python", "beginner", "advanced", "data", "science", "web", "django", "ml"}
  }
"""