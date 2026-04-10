"""
Ejercicio 2 — Fácil
Crea una función safe_get(dictionary, key, default=None) que acceda a un diccionario de forma segura.
data = {"name": "Manuel", "age": 23}

safe_get(data, "name")          → "Manuel"
safe_get(data, "email")         → None
safe_get(data, "email", "N/A")  → "N/A"
safe_get(data, "age")           → 23

💡 Este ejercicio tiene trampa — ¿realmente necesitas try/except aquí?


"""
def safe_get(dictionary, key, default=None):
    return dictionary.get(key, default)

data = {"name": "Manuel", "age": 23}

print(safe_get(data, "name"))          # Manuel
print(safe_get(data, "email"))         # None
print(safe_get(data, "email", "N/A"))  # N/A
print(safe_get(data, "age"))           # 23