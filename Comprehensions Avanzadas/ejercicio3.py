"""
Ejercicio 3 — Fácil
Usa any() y all() para validar una lista de transacciones.
# Preguntas:
all_valid        → False  # ¿todas tienen amount > 0?
has_income       → True   # ¿hay algún income?
all_expenses     → False  # ¿todas son expenses?
any_over_1000    → True   # ¿alguna tiene amount > 1000?
"""
transactions = [
    {"type": "expense", "amount": 500,  "category": "Food"},
    {"type": "income",  "amount": 15000,"category": "Salary"},
    {"type": "expense", "amount": -100, "category": "Transport"},  # inválida
    {"type": "expense", "amount": 800,  "category": "Entertainment"},
]
all_valid = all(t["amount"] > 0 for t in transactions)
has_income = any(t["type"] == "income" for t in transactions)
all_expense = all(t["type"] == "expense" for t in transactions)
any_over_100 = any(t["amount"] > 1000 for t in transactions)
print(all_valid)
print(has_income)
print(all_expense)
print(any_over_100)

