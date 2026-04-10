"""

Ejercicio 8 — Desafío
Crea un sistema de reintentos automáticos. La función retry(func, attempts, exceptions) ejecuta una función y la reintenta si lanza una excepción específica.
python# Simula una función que falla las primeras 2 veces
call_count = 0
def unstable_function():
    global call_count
    call_count += 1
    if call_count < 3:
        raise ConnectionError("Server unavailable")
    return "Success!"

result = retry(unstable_function, attempts=5, exceptions=(ConnectionError,))
# Attempt 1 failed: Server unavailable. Retrying...
# Attempt 2 failed: Server unavailable. Retrying...
# Attempt 3 succeeded!
# result → "Success!"

result = retry(unstable_function, attempts=2, exceptions=(ConnectionError,))
# Attempt 1 failed: Server unavailable. Retrying...
# Attempt 2 failed: Server unavailable. Retrying...
# MaxRetriesError: Failed after 2 attempts.

"""