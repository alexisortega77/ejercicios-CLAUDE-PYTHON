"""
Ejercicio 5 — Medio
Mejora la clase BankAccount del Nivel 5 agregando excepciones personalizadas: InsufficientFundsError y InvalidAmountError.
account = BankAccount("Manuel", 1000)
account.deposit(-100)      → InvalidAmountError: Amount must be positive
account.withdraw(5000)     → InsufficientFundsError: Insufficieclassnt funds. Balance: $1000, Requested: $5000
account.withdraw(500)      → 500

"""
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount  = amount
        super().__init__(
            f"Insufficient funds. Balance: ${balance}, Requested: ${amount}"
        )

class InvalidAmountError(Exception):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(f"Amount must be positive, got: ${amount}")


class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise InvalidAmountError(balance)
        self.owner    = owner
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError(amount)
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError(amount)
        if amount > self._balance:
            raise InsufficientFundsError(self._balance, amount)
        self._balance -= amount
        return self._balance

    def __str__(self):
        return f"Account: {self.owner} | Balance: ${self._balance:.2f}"
account = BankAccount("Manuel", 1000)
try:
 account.deposit(-100)  
except InvalidAmountError as e:
    print(f"InvalidAmountError: {e}") #→ InvalidAmountError: Amount must be positive


try:
 account.withdraw(5000)  
except InsufficientFundsError as e:
    print(f"InsufficientFundsError: {e}")
try:
 account.withdraw(500)  
 print("Succesfull Withdrawal")
except InsufficientFundsError as e:
    print(f"InsufficientFundsError: {e}")

print(account)