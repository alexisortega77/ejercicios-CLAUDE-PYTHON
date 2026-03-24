# ------------------------------------------------------------
# EJERCICIO 2 — Fácil
# Crea una función que reciba dos números y una operación
# como string y devuelva el resultado.
# Operaciones: "suma", "resta", "multiplica", "divide", "potencia"
# ------------------------------------------------------------
# Output esperado:
# operar(10, 3, "suma")      → 13
# operar(10, 3, "resta")     → 7
# operar(10, 3, "multiplica")→ 30
# operar(10, 3, "divide")    → 3.3333333333333335
# operar(10, 3, "potencia")  → 1000
# operar(10, 0, "divide")    → "Error: división entre cero"
# operar(10, 3, "modulo")    → "Operación no reconocida"
def operar(num_1, num_2, operacion):
    if operacion == "divide" and num_2 == 0:
        return "Error: división entre cero"

    operaciones = {
        "suma":       lambda a, b: a + b,
        "resta":      lambda a, b: a - b,
        "multiplica": lambda a, b: a * b,
        "divide":     lambda a, b: a / b,
        "potencia":   lambda a, b: a ** b,
    }

    if operacion not in operaciones:
        return "Operación no reconocida"

    return operaciones[operacion](num_1, num_2)

print(operar(10, 3, "suma")) 
print(operar(10, 3, "resta"))  
print(operar(10, 3, "multiplica"))
print(operar(10, 3, "divide"))
print(operar(10, 3, "potencia"))
print(operar(10, 0, "divide"))
print(operar(10, 3, "modulo"))  
