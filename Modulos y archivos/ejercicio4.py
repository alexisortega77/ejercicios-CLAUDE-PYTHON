"""
Ejercicio 4 — Medio
Mejora la clase BankAccount del Nivel 5 para que persista los datos. Agrega métodos save(filename)
 y un constructor alternativo load(filename).
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
import json
from datetime import datetime

class BankAccount:
    def __init__(self, owner, balance):
        self.owner    = owner
        self._balance = balance
        self._history = []

    def deposit(self, amount):
        if amount <= 0:
            return "Amount must be positive"
        self._balance += amount
        self._history.append({
            "type":   "deposit",
            "amount": amount,
            "date":   datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        return self._balance

    def withdraw(self, amount):
        if amount > self._balance:
            return "Insufficient balance"
        self._balance -= amount
        self._history.append({
            "type":   "withdrawal",
            "amount": amount,
            "date":   datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        return self._balance

    def save(self, filename):
        data = {
            "owner":   self.owner,
            "balance": self._balance,
            "history": self._history
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    @classmethod
    def load(cls, filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            account          = cls(data["owner"], data["balance"])
            account._history = data.get("history", [])
            return account
        except FileNotFoundError:
            raise FileNotFoundError(f"'{filename}' not found.")

    def __str__(self):
        return f"Account: {self.owner} | Balance: ${self._balance:.2f}"

account = BankAccount("Manuel", 1000)
account.deposit(500)
account.save("account.json")


account = BankAccount.load("account.json")
print(account)    # Account: Manuel | Balance: $1500.00
account.withdraw(200)
account.save("account.json")