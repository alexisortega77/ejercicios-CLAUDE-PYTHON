"""
Ejercicio 6 — Desafío
Crea un sistema de login con máximo 3 intentos. Usa excepciones para manejar credenciales incorrectas y cuenta bloqueada.
usuarios = {"manuel": "python123", "ana": "secret456"}

login("manuel", "wrongpass")  → AuthError: Wrong password. 2 attempts left.
login("manuel", "wrongpass")  → AuthError: Wrong password. 1 attempt left.
login("manuel", "wrongpass")  → AccountLockedError: Account locked after 3 failed attempts.
login("manuel", "python123")  → AccountLockedError: This account is locked.

"""