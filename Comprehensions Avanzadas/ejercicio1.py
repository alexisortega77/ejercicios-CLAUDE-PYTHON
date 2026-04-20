"""
Ejercicio 1 — Fácil
Dado un diccionario de productos y precios, usa dict comprehension
 para crear tres diccionarios nuevos: precios con IVA (16%), productos con 
 precio mayor a $500 y precios redondeados a 2 decimales.
con_iva      → {"Laptop": 17400.0, "Mouse": 406.0, ...}
caros        → {"Laptop": 15000, "Teclado": 800, "Monitor": 5000}
redondeados  → {"Laptop": 15000.00, "Mouse": 350.00, ...}
"""
prices = {"Laptop": 15000, "Mouse": 350, "Teclado": 800, "Monitor": 5000, "Audífonos": 450}

iva = {product: price * 1.16 for product, price in prices.items()}
expensives = {product: price  for product, price in prices.items() if price > 500 }
rounded = {p: round(price, 2) for p, price in prices.items()}
print(iva)
print(expensives)
print(rounded)


