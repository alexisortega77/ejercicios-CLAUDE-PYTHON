
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
def create_account(name, initial_balance):
    return {"name": name, "balance": initial_balance}

def deposit(account, amount):
    account['balance'] += amount
    return account['balance']

def withdraw(account, amount):
    if amount <= account['balance']:
        account['balance'] -= amount
        return account['balance']
    return "Insufficient balance"

def transfer(source_account, destination_account, amount):
    if amount <= 0 or amount > source_account['balance']:
        return False
    source_account['balance']      -= amount
    destination_account['balance'] += amount
    return True

def account_statement(account):
    print(f"Titular: {account['name']}")
    print(f"Saldo:   ${account['balance']:.2f}")


account1 = create_account("Manuel", 1000)
account2 = create_account("Ana", 500)

print(deposit(account1, 500))        # 1500
print(withdraw(account1, 200))       # 1300
print(withdraw(account1, 9999))      # Insufficient balance
print(transfer(account1, account2, 300))  # True

account_statement(account1)          # Saldo: $1000.00
account_statement(account2)          # Saldo: $800.00