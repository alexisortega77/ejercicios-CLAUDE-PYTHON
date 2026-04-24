"""
Ejercicio 7 — Desafío
Crea un sistema de autenticación con decoradores. El decorador require_auth verifica que el usuario tenga permiso antes de ejecutar la función.
pythoncurrent_user = {"name": "Manuel", "role": "admin"}

@require_auth(roles=["admin"])
def delete_user(user_id):
    return f"User {user_id} deleted."

@require_auth(roles=["admin", "moderator"])
def ban_user(user_id):
    return f"User {user_id} banned."

delete_user(42)     → "User 42 deleted."

current_user["role"] = "guest"
delete_user(42)     → PermissionError: User Manuel does not have required role.
"""