"""
Ejercicio 5 — Medio
Mejora la clase BankAccount del Nivel 5 agregando excepciones personalizadas: InsufficientFundsError y InvalidAmountError.
account = BankAccount("Manuel", 1000)
account.deposit(-100)      → InvalidAmountError: Amount must be positive
account.withdraw(5000)     → InsufficientFundsError: Insufficient funds. Balance: $1000, Requested: $5000
account.withdraw(500)      → 500

"""