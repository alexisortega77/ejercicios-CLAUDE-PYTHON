"""
Ejercicio 1 — Fácil
Crea una función safe_int(value) que convierta cualquier valor a entero de forma segura.
safe_int("42")      → 42
safe_int("3.14")    → 3
safe_int("hello")   → None
safe_int(True)      → 1
safe_int(None)      → None

💡 int("3.14") lanza ValueError pero int(float("3.14")) funciona. Intenta primero directo, luego vía float.
"""
def safe_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        try: 
            return int(float(value))
        except (ValueError, TypeError):
            return None
        
print(safe_int("3.14")) 
print(safe_int("hello"))
print(safe_int(True))
print(safe_int(None))