"""
Ejercicio 4 — Medio
Crea una jerarquía de figuras geométricas. Clase base Shape con método area() y perimeter(). 
Clases hijas: Rectangle, Circle, Triangle. 
Crea una función largest_shape(shapes) que reciba una lista de figuras y devuelva la de mayor área.
shapes = [Rectangle(4,5), Circle(3), Triangle(3,4,5)]
largest_shape(shapes)  → Rectangle 4x5 | Area: 20

"""
import math

class Shape:
    def area(self):
        return 0

    def perimeter(self):
        return 0


class Rectangle(Shape):
    def __init__(self, base, height):
        self.base   = base
        self.height = height

    def area(self):
        return self.base * self.height

    def perimeter(self):
        return 2 * (self.base + self.height)

    def __str__(self):
        return f"Rectangle {self.base}x{self.height} | Area: {self.area():.2f}"


class Circle(Shape):
    PI = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.PI * self.radius ** 2

    def perimeter(self):
        return 2 * self.PI * self.radius

    def __str__(self):
        return f"Circle radius: {self.radius} | Area: {self.area():.2f}"


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s-self.a) * (s-self.b) * (s-self.c))

    def perimeter(self):
        return self.a + self.b + self.c

    def __str__(self):
        return f"Triangle {self.a}x{self.b}x{self.c} | Area: {self.area():.2f}"


def largest_shape(shapes):
    return max(shapes, key=lambda s: s.area())


shapes = [Rectangle(4, 5), Circle(3), Triangle(3, 4, 5)]
print(largest_shape(shapes))   # Rectangle 4x5 | Area: 20.00