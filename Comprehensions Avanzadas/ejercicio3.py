"""
Ejercicio 3 — Fácil
Usa any() y all() para validar una lista de transacciones.
pythontransactions = [
    {"type": "expense", "amount": 500,  "category": "Food"},
    {"type": "income",  "amount": 15000,"category": "Salary"},
    {"type": "expense", "amount": -100, "category": "Transport"},  # inválida
    {"type": "expense", "amount": 800,  "category": "Entertainment"},
]

# Preguntas:
all_valid        → False  # ¿todas tienen amount > 0?
has_income       → True   # ¿hay algún income?
all_expenses     → False  # ¿todas son expenses?
any_over_1000    → True   # ¿alguna tiene amount > 1000?
"""