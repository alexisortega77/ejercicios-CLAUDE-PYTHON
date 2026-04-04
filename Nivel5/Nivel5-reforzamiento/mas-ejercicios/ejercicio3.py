"""
Ejercicio 3 — Fácil
Crea una clase Password que valide contraseñas. Métodos: is_valid(), strength() y __str__. 
Una contraseña es válida si tiene al menos 8 caracteres, una mayúscula y un número.
p1 = Password("abc123")
p1.is_valid()    → False
p1.strength()    → "Weak"

p2 = Password("MyPassword1")
p2.is_valid()    → True
p2.strength()    → "Medium"

p3 = Password("MyStr0ngP@ss!")
p3.is_valid()    → True
p3.strength()    → "Strong"
print(p3)        → Password: MyStr0ngP@ss! | Strength: Strong

💡 Weak: no válida. Medium: válida con 8-11 chars. Strong: válida con 12+ chars y símbolo especial.
"""
class Password:
    def __init__(self, password):
        self.password = password

    def is_valid(self):
        if len(self.password) <8:
            return False
        if not any(c.isupper() for c in self.password):
            return False
        if not any(n.isdigit() for n in self.password):
            return False
        return True
    
    def strength(self):
        if not self.is_valid():
            return "Weak"
        # aquí ya sabes que cumple lo básico
        if any(not c.isalnum() for c in self.password):
            return "Strong"
        return "Medium"
    
    def __str__(self):
        return f"Password: {self.password} | Strength: {self.strength()}"
        
p1 = Password("abc123")
print(p1.is_valid())    #→ False
print(p1.strength())   # → "Weak"

p2 = Password("MyPassword1")
print(p2.is_valid() )   #→ True
print(p2.strength() )   #→ "Medium"

p3 = Password("MyStr0ngP@ss!")
print(p3.is_valid() )   #→ True
print(p3.strength() )  # → "Strong"
print(p3)       # → Password: MyStr0ngP@ss! | Strength: Strong