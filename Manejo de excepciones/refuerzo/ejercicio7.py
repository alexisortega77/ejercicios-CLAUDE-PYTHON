"""
Ejercicio 7 — Desafío
Crea un sistema de registro de usuarios con estas validaciones encadenadas. Si cualquier validación falla, 
lanza una excepción específica.
register("Ma", "mail.com", "weak", -1)
→ [
    ValidationError: Name must be at least 3 characters,
    ValidationError: Invalid email,
    ValidationError: Password too weak,
    ValidationError: Invalid age
  ]

💡 En vez de lanzar al primer error, colecciona TODOS los errores 
y los lanzas juntos al final. Esto se llama "bulk validation".
"""
class ValidationError(Exception):
    def __init__(self, errors):
        self.errors = errors
        super().__init__(errors)

def register(name, email, password, age):
    errors = []

    if not name or len(name) < 3:
        errors.append("Name must be at least 3 characters")

    if email.count("@") != 1:
        errors.append("Invalid email")
    else:
        usuario, dominio = email.split("@")
        if "." not in dominio:
            errors.append("Invalid email")

    if len(password) < 8:
        errors.append("Password too weak")

    if age <= 0:
        errors.append("Invalid age")

    # 🔥 CLAVE DEL BULK VALIDATION
    if errors:
        raise ValidationError(errors)

    return f"User {name} registered!"

try:
    register("Ma", "mail.com", "weak", -1)
except ValidationError as e:
    for err in e.errors:
        print(f"ValidationError: {err}")

try:
   print(register("Manuel", "manuel@mail.com", "Python123!", 23))  # → "User Manuel registered!"
except ValidationError as e:
    for err in e.errors:
        print(f"ValidationError: {err}")