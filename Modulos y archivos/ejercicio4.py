"""
Ejercicio 4 — Medio
Mejora la clase BankAccount del Nivel 5 para que persista los datos. Agrega métodos save(filename) y un constructor alternativo load(filename).
python# Primera ejecución
account = BankAccount("Manuel", 1000)
account.deposit(500)
account.save("account.json")

# Segunda ejecución
account = BankAccount.load("account.json")
print(account)    # Account: Manuel | Balance: $1500.00
account.withdraw(200)
account.save("account.json")
"""