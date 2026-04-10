"""
Ejercicio 4 — Medio
Crea excepciones personalizadas para un sistema de inventario. 
OutOfStockError cuando no hay stock y InvalidQuantityError cuando la cantidad es inválida.
inventory = Inventory()
inventory.add("Laptop", 5)
inventory.add("Mouse", 0)

inventory.sell("Laptop", 2)      → "Sold 2 Laptop(s). Stock: 3"
inventory.sell("Mouse", 1)       → OutOfStockError: Mouse is out of stock
inventory.sell("Laptop", -1)     → InvalidQuantityError: Quantity must be positive
inventory.sell("Laptop", 10)     → OutOfStockError: Not enough stock. Available: 3, Requested: 10
inventory.sell("Keyboard", 1)    → KeyError: Keyboard not found in inventory

"""
class OutOfStockError(Exception):
    pass

class InvalidQuantityError(Exception):
    pass

class ProductNotFoundError(KeyError):
    pass


class Inventory:
    def __init__(self):
        self.products = {}

    def add(self, product_name, stock):
        self.products[product_name] = stock

    def sell(self, name, quantity):
        if name not in self.products:
            raise ProductNotFoundError(f"{name} not found in inventory")
        if quantity <= 0:
            raise InvalidQuantityError("Quantity must be positive")

        stock = self.products[name]

        if stock == 0:
            raise OutOfStockError(f"{name} is out of stock")
        if quantity > stock:
            raise OutOfStockError(
                f"Not enough stock. Available: {stock}, Requested: {quantity}"
            )

        self.products[name] -= quantity
        return f"Sold {quantity} {name}(s). Stock: {self.products[name]}"


def safe_sell(inventory, name, quantity):
    try:
        print(inventory.sell(name, quantity))
    except OutOfStockError as e:
        print(f"OutOfStockError: {e}")
    except InvalidQuantityError as e:
        print(f"InvalidQuantityError: {e}")
    except ProductNotFoundError as e:
        print(f"KeyError: {e}")


inventory = Inventory()
inventory.add("Laptop", 5)
inventory.add("Mouse", 0)

safe_sell(inventory, "Laptop", 2)     # Sold 2 Laptop(s). Stock: 3
safe_sell(inventory, "Mouse", 1)      # OutOfStockError: Mouse is out of stock
safe_sell(inventory, "Laptop", -1)    # InvalidQuantityError: Quantity must be positive
safe_sell(inventory, "Laptop", 10)    # OutOfStockError: Not enough stock. Available: 3, Requested: 10
safe_sell(inventory, "Keyboard", 1)   # KeyError: Keyboard not found in inventory