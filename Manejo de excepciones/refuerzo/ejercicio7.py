"""
Ejercicio 7 — Desafío
Crea un sistema de registro de usuarios con estas validaciones encadenadas. Si cualquier validación falla, lanza una excepción específica.
register("Manuel", "manuel@mail.com", "Python123!", 23)   → "User Manuel registered!"
register("Ma", "mail.com", "weak", -1)
→ [
    ValidationError: Name must be at least 3 characters,
    ValidationError: Invalid email,
    ValidationError: Password too weak,
    ValidationError: Invalid age
  ]

💡 En vez de lanzar al primer error, colecciona TODOS los errores y los lanzas juntos al final. Esto se llama "bulk validation".
"""