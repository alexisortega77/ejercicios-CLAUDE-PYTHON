"""

**Ejercicio 4 — Medio**
Crea una jerarquía de vehículos. 
Clase base `Vehicle` con `brand`, `model`, `year` y `speed=0`. 
Métodos: `accelerate()`, `brake()`, `info()`. 
Clases hijas: `Car` (doors), `Motorcycle` (type), `Truck` (capacity).
```
car = Car("Toyota", "Corolla", 2022, 4)
car.accelerate(60)
car.info()   → Toyota Corolla 2022 | Speed: 60 km/h | Doors: 4

moto = Motorcycle("Honda", "CBR", 2023, "sport")
moto.accelerate(100)
moto.brake(30)
moto.info()  → Honda CBR 2023 | Speed: 70 km/h | Type: sport
```
"""

class Vehiculo:
    def __init__(self, brand, model, year):
        self.brand=brand
        self.model=model
        self.year=year
        self.speed=0
    
    def accelerate(self,acceleration):
        if acceleration <0:
           return "No hay aceleracion negativa"
        else:
             self.speed += acceleration
             return self.speed
    def brake(self, acceleration):
        if acceleration <0:
           return "No hay brake negativa"
        else:
             self.speed -= acceleration
             return self.speed
    def info(self):
        return f"{self.brand} {self.model} {self.year} | Speed: {self.speed} km/h | {self.extra()}"
    def extra(self):
        return ""
        
class Car(Vehiculo):
     def __init__(self, brand, model, year, doors):
         super().__init__(brand, model, year)
         self.doors=doors
    
     def extra(self):
        return f"Doors: {self.doors}"

class Motocycle(Vehiculo):
     def __init__(self, brand, model, year, type):
         super().__init__(brand, model, year)
         self.type=type
     def extra(self):
        return f"Type: {self.type}"

class Truck(Vehiculo):
     def __init__(self, brand, model, year, capacity):
         super().__init__(brand, model, year)
         self.capacity=capacity
     def extra(self):
        return f"Capacity: {self.capacity}"


car = Car("Toyota", "Corolla", 2022, 4)
print(car.accelerate(60))
print(car.info())   #→ Toyota Corolla 2022 | Speed: 60 km/h | Doors: 4

moto = Motocycle("Honda", "CBR", 2023, "sport")
print(moto.accelerate(100))
print(moto.brake(30))
print(moto.info()) # → Honda CBR 2023 | Speed: 70 km/h | Type: sport


camion = Truck("civic", "ltr", 2023, 10)
print(camion.accelerate(100))
print(camion.brake(30))
print(camion.info() )


"""
SOLUCION OPTIMA CON NUEVO METODO STR PARA LLEVAR MEJOR CONTROL DE INFORMACION AGREGADA DE CLASE HIJA

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year  = year
        self.speed = 0

    def accelerate(self, amount):
        if amount < 0:
            return "Acceleration cannot be negative"
        self.speed += amount
        return self.speed

    def brake(self, amount):
        if amount < 0:
            return "Brake value cannot be negative"
        self.speed = max(0, self.speed - amount)
        return self.speed

    def __str__(self):
        return f"{self.brand} {self.model} {self.year} | Speed: {self.speed} km/h"


class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def __str__(self):
        return f"{super().__str__()} | Doors: {self.doors}"


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, moto_type):
        super().__init__(brand, model, year)
        self.moto_type = moto_type

    def __str__(self):
        return f"{super().__str__()} | Type: {self.moto_type}"


class Truck(Vehicle):
    def __init__(self, brand, model, year, capacity):
        super().__init__(brand, model, year)
        self.capacity = capacity

    def __str__(self):
        return f"{super().__str__()} | Capacity: {self.capacity} tons"

"""