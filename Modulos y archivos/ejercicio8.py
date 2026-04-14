"""
Ejercicio 8 — Desafío
Crea un sistema de inventario persistente con historial de movimientos. 
Cada venta o compra se registra en un archivo movements.csv con fecha, producto, tipo y cantidad.
# inventory.json — estado actual
# movements.csv — historial de cambios

Date,Product,Type,Quantity,Stock_after
2026-04-07,Laptop,sale,2,3
2026-04-07,Mouse,purchase,10,10

"""
import csv
import json
import os
from datetime import datetime


class Product:
    def __init__(self, name, price, stock):
        self.name  = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} | ${self.price} | Stock: {self.stock}"


class Inventory:
    def __init__(self):
        self._products  = {}
        self._movements = []

    def add_product(self, product):
        self._products[product.name] = product

    def sell(self, name, quantity):
        if quantity <= 0:
            return "Invalid quantity"
        if name not in self._products:
            return "Product not found"
        product = self._products[name]
        if product.stock == 0:
            return "Out of stock"
        if product.stock < quantity:
            return f"Insufficient stock. Available: {product.stock}"
        product.stock -= quantity
        self._log_movement(name, "sale", quantity, product.stock)
        return f"Sale successful. Stock: {product.stock}"

    def purchase(self, name, quantity):
        if quantity <= 0:
            return "Invalid quantity"
        if name not in self._products:
            return "Product not found"
        product = self._products[name]
        product.stock += quantity
        self._log_movement(name, "purchase", quantity, product.stock)
        return f"Purchase successful. Stock: {product.stock}"

    def _log_movement(self, name, mov_type, quantity, stock_after):
        self._movements.append({
            "Date":        datetime.now().strftime("%Y-%m-%d"),
            "Product":     name,
            "Type":        mov_type,
            "Quantity":    quantity,
            "Stock_after": stock_after
        })

    def save_inventory(self, filename):
        data = {
            name: {"price": p.price, "stock": p.stock}
            for name, p in self._products.items()
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def save_movements(self, filename):
        file_exists = os.path.isfile(filename)
        with open(filename, "a", newline="") as f:
            writer = csv.DictWriter(
                f, fieldnames=["Date", "Product", "Type", "Quantity", "Stock_after"]
            )
            if not file_exists:
                writer.writeheader()
            writer.writerows(self._movements)
        self._movements.clear()

    @classmethod
    def load_inventory(cls, filename):
        inv = cls()
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            for name, info in data.items():
                inv._products[name] = Product(name, info["price"], info["stock"])
        except FileNotFoundError:
            pass
        return inv

    def search(self, name):
        product = self._products.get(name)
        return str(product) if product else "Product not found"

    def total_value(self):
        return sum(p.price * p.stock for p in self._products.values())

    def out_of_stock(self):
        return [n for n, p in self._products.items() if p.stock == 0]

    def __str__(self):
        if not self._products:
            return "Inventory is empty"
        lines = ["Inventory:"]
        lines += [f"  {p}" for p in self._products.values()]
        lines.append(f"Total value: ${self.total_value():,}")
        return "\n".join(lines)


# Primera ejecución
inv = Inventory()
inv.add_product(Product("Laptop",  15000, 5))
inv.add_product(Product("Mouse",   300,   10))
inv.add_product(Product("Teclado", 800,   0))

print(inv.sell("Laptop", 2))
print(inv.purchase("Mouse", 5))
print(inv)

inv.save_inventory("inventory.json")
inv.save_movements("movements.csv")

# Segunda ejecución
inv = Inventory.load_inventory("inventory.json")
print(inv.sell("Laptop", 1))
inv.save_inventory("inventory.json")
inv.save_movements("movements.csv")