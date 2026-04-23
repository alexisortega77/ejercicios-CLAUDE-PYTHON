class SearchEngine:
    def __init__(self, articles):
        self.articles = articles

    def search(self, tag):
        return [a["title"] for a in self.articles if tag.lower() in a["tags"]]

    def top_n(self, n=3):
        return [
            a["title"]
            for a in sorted(self.articles, key=lambda x: x["views"], reverse=True)[:n]
        ]

    def related(self, *tags):
        return [
            a["title"] for a in self.articles
            if all(tag in a["tags"] for tag in tags)
        ]

    def stats(self):
        total     = len(self.articles)
        avg_views = round(sum(a["views"] for a in self.articles) / total, 2)
        return {
            "total":       total,
            "avg_views":   avg_views,
            "most_viewed": max(self.articles, key=lambda x: x["views"])["title"],
            "all_tags":    {tag for a in self.articles for tag in a["tags"]},
        }

    def __str__(self):
        return f"SearchEngine | {len(self.articles)} articles"

articles = [
    {"title": "Python basics",            "tags": ["python", "beginner"],         "views": 1500},
    {"title": "Advanced Python",          "tags": ["python", "advanced"],         "views": 800},
    {"title": "Data Science with Python", "tags": ["python", "data", "science"],  "views": 3200},
    {"title": "Web dev with Django",      "tags": ["python", "web", "django"],    "views": 2100},
    {"title": "Machine Learning intro",   "tags": ["ml", "data", "science"],      "views": 4500},
]

engine = SearchEngine(articles)
print(engine.search("python"))
print(engine.top_n(3))
print(engine.related("python", "data"))
print(engine.stats())

"""
¿Por qué una clase es mejor aquí?
python# Sin clase — articles repetido en cada llamada
search(articles, "python")
top_n(articles, 3)
related(articles, "python", "data")
stats(articles)

# Con clase — articles se pasa una vez
engine = SearchEngine(articles)
engine.search("python")
engine.top_n(3)
engine.related("python", "data")
engine.stats()
Es el mismo principio de FinanceManager en el proyecto
 — los datos y las operaciones sobre esos datos van juntos en una clase.
"""