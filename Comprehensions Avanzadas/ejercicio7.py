"""
Ejercicio 7 — Desafío
Implementa un mini motor de búsqueda sobre una lista de artículos usando solo comprehensions y funciones de alto orden.
python
articles = [
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
articles = [
    {"title": "Python basics",            "tags": ["python", "beginner"],         "views": 1500},
    {"title": "Advanced Python",          "tags": ["python", "advanced"],         "views": 800},
    {"title": "Data Science with Python", "tags": ["python", "data", "science"],  "views": 3200},
    {"title": "Web dev with Django",      "tags": ["python", "web", "django"],    "views": 2100},
    {"title": "Machine Learning intro",   "tags": ["ml", "data", "science"],      "views": 4500},
]

def search(articles, tag):
    return [a["title"] for a in articles if tag.lower() in a["tags"]]

def top_n(articles, n=3):
    return [a["title"] for a in sorted(articles, key=lambda x: x["views"], reverse=True)[:n]]

def related(articles, *tags):
    return [a["title"] for a in articles if all(tag in a["tags"] for tag in tags)]

def stats(articles):
    total     = len(articles)
    avg_views = round(sum(a["views"] for a in articles) / total, 2)
    all_tags  = {tag for a in articles for tag in a["tags"]}
    most_viewed = max(articles, key=lambda x: x["views"])["title"]
    return {
        "total":       total,
        "avg_views":   avg_views,
        "most_viewed": most_viewed,
        "all_tags":    all_tags,
    }

print(search(articles, "python"))
print(top_n(articles, 3))
print(related(articles, "python", "data"))
print(stats(articles))