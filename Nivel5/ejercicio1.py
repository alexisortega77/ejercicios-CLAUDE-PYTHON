'''
**Ejercicio 1 — Fácil**
Crea una clase `Rectangle` con atributos `base` y `height`. Métodos: `area()`, `perimeter()`, `is_square()` y `__str__`.
```
r = Rectangle(5, 3)
r.area()         → 15
r.perimeter()    → 16
r.is_square()    → False
print(r)         → Rectangle 5x3 | Area: 15

r2 = Rectangle(4, 4)
r2.is_square()   → True
'''

class Rectangle:
    def __init__(self, base, height):
        self.base   = base
        self.height = height

    def area(self):
        return self.base * self.height

    def perimeter(self):
        return (self.base + self.height) * 2

    def is_square(self):
        return self.base == self.height

    def __str__(self):
        return f"Rectangle {self.base}x{self.height} | Area: {self.area()}"


r = Rectangle(5, 3)
print(r.area())        # 15
print(r.perimeter())   # 16
print(r.is_square())   # False
print(r)               # Rectangle 5x3 | Area: 15

r2 = Rectangle(4, 4)
print(r2.is_square())  # True

