"""
Ejercicio 7 — Desafío
Crea un sistema de tienda online con clases Product, Cart y Order. El carrito puede agregar y quitar productos. Al confirmar la orden se crea un objeto Order con los productos, total y fecha.
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