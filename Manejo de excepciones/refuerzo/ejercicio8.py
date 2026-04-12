"""

Ejercicio 8 — Desafío
Crea un sistema de reintentos automáticos. La función retry(func, attempts, exceptions) 
ejecuta una función y la reintenta si lanza una excepción específica.
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
class MaxRetriesError(Exception):
    def __init__(self, attempts):
        super().__init__(f"Failed after {attempts} attempts.")


call_count = 0

def unstable_function():
    global call_count
    call_count += 1
    if call_count < 3:
        raise ConnectionError("Server unavailable")
    return "Success!"


def retry(func, attempts, exceptions):
    for attempt in range(1, attempts + 1):
        try:
            result = func()
            print(f"Attempt {attempt} succeeded!")
            return result
        except exceptions as e:
            if attempt == attempts:
                raise MaxRetriesError(attempts)
            print(f"Attempt {attempt} failed: {e}. Retrying...")


# Prueba 1 — funciona en el intento 3
print("--- Test 1 ---")
call_count = 0
try:
    result = retry(unstable_function, attempts=5, exceptions=(ConnectionError,))
    print(f"Result: {result}")
except MaxRetriesError as e:
    print(f"MaxRetriesError: {e}")

# Prueba 2 — se agotan los intentos
print("\n--- Test 2 ---")
call_count = 0
try:
    retry(unstable_function, attempts=2, exceptions=(ConnectionError,))
except MaxRetriesError as e:
    print(f"MaxRetriesError: {e}")