
"""
Ejercicio 1 — Fácil
Crea una clase Circle con atributo radius. Métodos: area(), perimeter(), is_bigger_than(other) y __str__. Usa pi = 3.14159.
c1 = Circle(5)
c1.area()                → 78.53975
c1.perimeter()           → 31.4159
c1.is_bigger_than(Circle(3)) → True
print(c1)                → Circle | Radius: 5 | Area: 78.54
"""
class Circle:
    PI = 3.14159

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self):
        return self.PI * self.radius ** 2

    def perimeter(self):
        return 2 * self.PI * self.radius

    def is_bigger_than(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.area() < other.area()

    def __str__(self):
        return f"Circle | Radius: {self.radius} | Area: {self.area():.2f}"


# Con __eq__ y __lt__ puedes usar operadores directamente
c1 = Circle(5)
c2 = Circle(3)
c3 = Circle(5)

print(c1 > c2)    # True  — usa __lt__ al revés
print(c1 == c3)   # True  — mismo radio
print(sorted([c1, c2, Circle(4)]))  # ordena por área automáticamente