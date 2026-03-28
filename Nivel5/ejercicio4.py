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
        return f"{self.brand} {self.model} {self.year} | Speed: {self.speed} km/h | Doors: {self.doors}"
        
class Car(Vehiculo):
     def __init__(self, brand, model, year, doors):
         super().__init__(brand, model, year,self.speed)
