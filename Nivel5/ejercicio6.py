"""

**Ejercicio 6 — Medio**
Crea clases `Product` e `Inventory`. `Product` tiene nombre, precio y stock. `Inventory` gestiona una colección de productos. Métodos: `add_product()`, `sell()`, `search()`, `total_value()`, `out_of_stock()`.
```
inv = Inventory()
inv.add_product(Product("Laptop", 15000, 5))
inv.add_product(Product("Mouse", 350, 0))
inv.total_value()       → 75000
inv.out_of_stock()      → ["Mouse"]
inv.sell("Laptop", 2)   → "Sale successful. Stock: 3"
inv.sell("Mouse", 1)    → "Out of stock"
```

"""