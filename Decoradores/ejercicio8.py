"""
Ejercicio 8 — Desafío
Crea un decorador rate_limit(calls, period) que limite cuántas veces se puede llamar una función en un período de tiempo.
python@rate_limit(calls=3, period=10)
def api_call(endpoint):
    return f"Response from {endpoint}"

api_call("/users")    → "Response from /users"
api_call("/posts")    → "Response from /posts"
api_call("/data")     → "Response from /data"
api_call("/other")    → RateLimitError: Maximum 3 calls per 10 seconds exceeded.

💡 Guarda un registro de los timestamps de cada llamada. Filtra solo los que están dentro del período actual.
"""