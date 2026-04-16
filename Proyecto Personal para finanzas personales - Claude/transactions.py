import json
from datetime import datetime


class Transaction:
    VALID_TYPES = ("income", "expense")

    def __init__(self, transaction_type, category, amount, description):
        if transaction_type not in self.VALID_TYPES:
            raise ValueError(f"Type must be 'income' or 'expense', got: '{transaction_type}'")
        if amount <= 0:
            raise ValueError(f"Amount must be positive, got: {amount}")

        self.type        = transaction_type
        self.category    = category
        self.amount      = amount
        self.description = description
        self.date        = datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "date":        self.date,
            "type":        self.type,
            "category":    self.category,
            "amount":      self.amount,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data):
        t = cls(data["type"], data["category"], data["amount"], data["description"])
        t.date = data["date"]
        return t

    def __str__(self):
        return (
            f"[{self.date}] {self.type.upper():<7} | "
            f"{self.category:<14} | "
            f"${self.amount:>10,.2f} | "
            f"{self.description}"
        )

class Budget:
    def __init__(self, category, limit):
        if limit <= 0:
         raise ValueError ("Limit must be greater than 0")
        self.limit = limit
        self.category = category
        self.spent = 0

    def add_expense(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.spent+=amount
        return self.spent
    
    def remaining(self):
        return self.limit - self.spent
    
    def percentage_used(self):
        return (self.spent/self.limit)*100
    
    def is_over_budget(self):
        return self.spent > self.limit
    
   
    def to_dict(self):
        return {
            "category":self.category,
            "limit":self.limit,
            "spent":self.spent
        }
    @classmethod
    def from_dict(cls, data):
        t = cls(data["category"], data["limit"], data["spent"])
        t.spent = data["spent"]
        return t

    def __str__(self):
        return f"{self.category} | Limit: ${self.limit} | Spent: ${self.spent} | Remaining: ${self.remaining():.2f}"

def save_transactions(transactions, filename):
    with open(filename, "w") as f:
        json.dump([t.to_dict() for t in transactions], f, indent=4)


def load_transactions(filename):
    try:
        with open(filename, "r") as f:
            return [Transaction.from_dict(d) for d in json.load(f)]
    except FileNotFoundError:
        return []


# Uso
t1 = Transaction("income",  "Salary",        15000, "Monthly salary")
t2 = Transaction("expense", "Food",           500,  "Supermarket")
t3 = Transaction("expense", "Transport",      150,  "Gas")
t4 = Transaction("expense", "Entertainment",  800,  "Concert")

# Validaciones
try:
    Transaction("invalid", "Food", 500, "test")
except ValueError as e:
    print(f"ValueError: {e}")

try:
    Transaction("expense", "Food", -100, "test")
except ValueError as e:
    print(f"ValueError: {e}")

# Persistencia
transactions = [t1, t2, t3, t4]
save_transactions(transactions, "finances.json")

loaded = load_transactions("finances.json")
for t in loaded:
    print(t)