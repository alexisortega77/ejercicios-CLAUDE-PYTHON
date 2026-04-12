"""
Ejercicio 1 — Fácil
Crea una clase Person con nombre, edad y email. Métodos: is_adult(), greet() y __str__.
p = Person("Manuel", 23, "manuel@mail.com")
p.is_adult()   → True
p.greet()      → "Hi, my name is Manuel and I am 23 years old."
print(p)       → Person: Manuel | Age: 23 | Email: manuel@mail.com
"""
class Person:
    def __init__(self, name, age, email):
        self.name = name 
        self.age = age 
        self.email = email

    def is_adult (self):
        return self.age >= 18
    
    def greet(self):
        return f"Hi, my name is {self.name} and I am {self.age} years old."
    
    def __str__(self):
        return f"Person: {self.name} | Age: {self.age} | Email: {self.email}"
    
p = Person("Manuel", 23, "manuel@mail.com")
print(p.is_adult())   #→ True
print(p.greet() )    # → "Hi, my name is Manuel and I am 23 years old."
print(p)  