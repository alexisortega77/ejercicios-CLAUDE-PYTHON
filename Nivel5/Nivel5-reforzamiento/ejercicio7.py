"""
Ejercicio 7 — Desafío
Crea un sistema de tienda online con clases Product, Cart y Order. 
El carrito puede agregar y quitar productos. 
Al confirmar la orden se crea un objeto Order con los productos, total y fecha.
cart = Cart("Manuel")
cart.add(Product("Laptop", 15000, stock=5))
cart.add(Product("Mouse", 350, stock=10))
cart.add(Product("Laptop", 15000, stock=5))  # agrega 2 laptops
cart.remove("Mouse")
cart.summary()
→ Cart: Manuel
→   2x Laptop  $30000
→ Total: $30000

order = cart.checkout()
→ Order confirmed!
→ Order #1 | Manuel | Total: $30000
"""
from datetime import date

class Product:
    def __init__(self, name, price, stock):
        self.name  = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} | ${self.price} | Stock: {self.stock}"


class Cart:
    def __init__(self, user_name):
        self.user_name = user_name
        self.items     = {}

    def add(self, product):
        current_qty = self.items.get(product.name, {}).get('quantity', 0)
        if current_qty >= product.stock:
            return f"Not enough stock for {product.name}"
        if product.name in self.items:
            self.items[product.name]['quantity'] += 1
        else:
            self.items[product.name] = {"product": product, "quantity": 1}
        return f"{product.name} added to cart."

    def remove(self, name):
        if name not in self.items:
            return f"'{name}' not found in cart."
        del self.items[name]
        return f"'{name}' removed from cart."

    def total(self):
        return sum(
            d['product'].price * d['quantity']
            for d in self.items.values()
        )

    def summary(self):
        print(f"Cart: {self.user_name}")
        for name, data in self.items.items():
            qty      = data['quantity']
            subtotal = data['product'].price * qty
            print(f"  {qty}x {name}  ${subtotal}")
        print(f"Total: ${self.total()}")

    def checkout(self):
        if not self.items:
            return "Cart is empty"
        order      = Order(self.user_name, self.items.copy(), self.total())
        self.items = {}
        print("Order confirmed!")
        print(order)
        return order


class Order:
    _next_id = 1

    def __init__(self, user_name, items, total):
        self.id        = Order._next_id
        Order._next_id += 1
        self.user_name = user_name
        self.items     = items
        self.total     = total
        self.date      = date.today()

    def __str__(self):
        return f"Order #{self.id} | {self.user_name} | Total: ${self.total} | Date: {self.date}"


cart = Cart("Manuel")
cart.add(Product("Laptop", 15000, stock=5))
cart.add(Product("Mouse",  350,   stock=10))
cart.add(Product("Laptop", 15000, stock=5))
cart.remove("Mouse")
cart.summary()

order = cart.checkout()