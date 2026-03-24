
# ------------------------------------------------------------
# EJERCICIO 8 — Desafío
# Crea un mini banco con estas funciones:
# - crear_cuenta(nombre, saldo_inicial)  → dict cuenta
# - depositar(cuenta, monto)            → nuevo saldo
# - retirar(cuenta, monto)              → nuevo saldo o error
# - transferir(cuenta_origen, cuenta_destino, monto) → True/False
# - estado_cuenta(cuenta)               → imprime resumen
# ------------------------------------------------------------
# Output esperado:
# cuenta1 = crear_cuenta("Manuel", 1000)
# cuenta2 = crear_cuenta("Ana", 500)
#
# depositar(cuenta1, 500)     → 1500
# retirar(cuenta1, 200)       → 1300
# retirar(cuenta1, 9999)      → "Saldo insuficiente"
# transferir(cuenta1, cuenta2, 300) → True
#
# estado_cuenta(cuenta1)
# Titular: Manuel
# Saldo:   $1000.00
#
# estado_cuenta(cuenta2)
# Titular: Ana
# Saldo:   $800.00
