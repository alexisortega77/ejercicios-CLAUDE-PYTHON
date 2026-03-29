"""

**Ejercicio 6 — Medio**
Crea clases `Product` e `Inventory`. `Product` tiene nombre, precio y stock. 
`Inventory` gestiona una colección de productos.
 Métodos: `add_product()`, `sell()`, `search()`, `total_value()`, `out_of_stock()`.
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
class Product:
    def __init__(self, name, price, stock):
        self.name  = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} | ${self.price} | Stock: {self.stock}"


class Inventory:
    def __init__(self):
        self._products = {}

    def add_product(self, product):
        self._products[product.name] = product

    def sell(self, name, quantity):
        if name not in self._products:
            return "Product not found"
        product = self._products[name]
        if product.stock == 0:
            return "Out of stock"
        if product.stock < quantity:
            return f"Insufficient stock. Available: {product.stock}"
        product.stock -= quantity
        return f"Sale successful. Stock: {product.stock}"

    def search(self, name):
        product = self._products.get(name)
        if not product:
            return "Product not found"
        return str(product)

    def total_value(self):
        return sum(p.price * p.stock for p in self._products.values())

    def out_of_stock(self):
        return [name for name, p in self._products.items() if p.stock == 0]


inv = Inventory()
inv.add_product(Product("Laptop", 15000, 5))
inv.add_product(Product("Mouse", 350, 0))
inv.add_product(Product("Teclado", 800, 3))

print(inv.total_value())          # 77400
print(inv.out_of_stock())         # ['Mouse']
print(inv.sell("Laptop", 2))      # Sale successful. Stock: 3
print(inv.sell("Mouse", 1))       # Out of stock
print(inv.search("Laptop"))       # Laptop | $15000 | Stock: 3