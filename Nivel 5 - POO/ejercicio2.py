"""

**Ejercicio 2 — Fácil**
Crea una clase `BankAccount` con atributos `owner` y `_balance` (privado). 
Métodos: `deposit()`, `withdraw()`, `get_balance()` y `__str__`.
```
account = BankAccount("Manuel", 1000)
account.deposit(500)       → 1500
account.withdraw(200)      → 1300
account.withdraw(9999)     → "Insufficient balance"
account.get_balance()      → 1300
print(account)             → Account: Manuel | Balance: $1300.00
```

"""
class BankAccount:
    def __init__(self, owner, balance):
        self.owner    = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount > self._balance:
            return "Insufficient balance"
        self._balance -= amount
        return self._balance

    def get_balance(self):
        return self._balance

    def __str__(self):
        return f"Account: {self.owner} | Balance: ${self._balance:.2f}"


account = BankAccount("Manuel", 1000)
print(account.deposit(500))      # 1500
print(account.withdraw(200))     # 1300
print(account.withdraw(9999))    # Insufficient balance
print(account.get_balance())     # 1300
print(account)                   # Account: Manuel | Balance: $1300.00