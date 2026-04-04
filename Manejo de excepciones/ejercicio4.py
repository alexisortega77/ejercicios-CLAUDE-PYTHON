"""
Ejercicio 4 — Medio
Crea una excepción personalizada InvalidAgeError y úsala en una clase Person que valide la edad en el __init__.
p1 = Person("Manuel", 23)   → OK
p2 = Person("Ana", -5)      → InvalidAgeError: Age cannot be negative
p3 = Person("Luis", 200)    → InvalidAgeError: Age 200 is not realistic

"""
class InvalidAgeError(Exception):
    pass


class Person:
    def __init__(self, name, age):
        if age < 0:
            raise InvalidAgeError("Age cannot be negative")
        if age > 120:
            raise InvalidAgeError(f"Age {age} is not realistic")
        self.name = name
        self.age  = age

    def __str__(self):
        return f"Person: {self.name} | Age: {self.age}"

# Pruebas
try:
    p1 = Person("Manuel", 23)
    print(f"OK — {p1}")
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")

try:
    p2 = Person("Ana", -5)
    print(f"OK — {p2}")
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")

try:
    p3 = Person("Luis", 200)
    print(f"OK — {p3}")
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")

"""
class InvalidAgeError(Exception):
    def __init__(self, age, reason):
        self.age    = age
        self.reason = reason
        super().__init__(f"Invalid age {age}: {reason}")


class Person:
    MIN_AGE = 0
    MAX_AGE = 120

    def __init__(self, name, age):
        self._validate_age(age)
        self.name = name
        self.age  = age

    def _validate_age(self, age):
        if age < self.MIN_AGE:
            raise InvalidAgeError(age, "cannot be negative")
        if age > self.MAX_AGE:
            raise InvalidAgeError(age, "is not realistic")

    def __str__(self):
        return f"Person: {self.name} | Age: {self.age}"
"""