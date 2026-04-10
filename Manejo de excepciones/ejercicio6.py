"""
Ejercicio 6 — Desafío
Crea un sistema de login con máximo 3 intentos. Usa excepciones para manejar credenciales incorrectas y cuenta bloqueada.
usuarios = {"manuel": "python123", "ana": "secret456"}

login("manuel", "wrongpass")  → AuthError: Wrong password. 2 attempts left.
login("manuel", "wrongpass")  → AuthError: Wrong password. 1 attempt left.
login("manuel", "wrongpass")  → AccountLockedError: Account locked after 3 failed attempts.
login("manuel", "python123")  → AccountLockedError: This account is locked.

"""
class AuthError(Exception):
    def __init__(self, attempts_left):
        self.attempts_left = attempts_left
        super().__init__(f"Wrong password. {attempts_left} attempts left.")


class AccountLockedError(Exception):
    def __init__(self, just_locked=False):
        msg = "Account locked after 3 failed attempts." if just_locked else "This account is locked."
        super().__init__(msg)


class AuthSystem:
    MAX_ATTEMPTS = 3

    def __init__(self, users):
        self.users           = users
        self.failed_attempts = {}
        self.locked_accounts = set()

    def login(self, username, password):
        # ¿ya estaba bloqueada?
        if username in self.locked_accounts:
            raise AccountLockedError(just_locked=False)

        # ¿contraseña correcta?
        if self.users.get(username) == password:
            self.failed_attempts[username] = 0
            return f"Welcome, {username}!"

        # incrementa intentos
        attempts      = self.failed_attempts.get(username, 0) + 1
        self.failed_attempts[username] = attempts
        attempts_left = self.MAX_ATTEMPTS - attempts

        # ¿se bloquea ahora?
        if attempts >= self.MAX_ATTEMPTS:
            self.locked_accounts.add(username)
            raise AccountLockedError(just_locked=True)

        raise AuthError(attempts_left)


sistema = AuthSystem({"manuel": "python123", "ana": "secret456"})

tests = [
    ("manuel", "wrongpass"),
    ("manuel", "wrongpass"),
    ("manuel", "wrongpass"),
    ("manuel", "python123"),
]

for username, password in tests:
    try:
        print(sistema.login(username, password))
    except AccountLockedError as e:
        print(f"AccountLockedError: {e}")
    except AuthError as e:
        print(f"AuthError: {e}")