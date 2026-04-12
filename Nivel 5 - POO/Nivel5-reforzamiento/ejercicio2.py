"""
Ejercicio 2 — Fácil
Crea una clase Temperature que almacene una temperatura en Celsius. 
Métodos: to_fahrenheit(), to_kelvin(), is_freezing(), is_boiling() y __str__.
t = Temperature(100)
t.to_fahrenheit()  → 212.0
t.to_kelvin()      → 373.15
t.is_freezing()    → False
t.is_boiling()     → True
print(t)           → 100°C | 212.00°F | 373.15K
"""
class Temperature:
    def __init__(self, celsius):
        if not isinstance(celsius, (int, float)):
            raise ValueError("La temperatura debe ser numérica")
        self.celsius = celsius
    def to_fahrenheit(self):
        return self.celsius*1.8+32
    def to_kelvin(self):
        return self.celsius+273.15
    def is_freezing(self):
        return self.celsius<=0
    def is_boiling(self):
        return self.celsius>=100
    def __str__(self):
        return f"{self.celsius}°C | {self.to_fahrenheit():.2f}°F | {self.to_kelvin():.2f}°K"
    
t = Temperature(100)
t.to_fahrenheit()  #→ 212.0
t.to_kelvin()    # → 373.15
print(t.is_freezing() )   #→ False
print(t.is_boiling() )    #→ True
print(t)