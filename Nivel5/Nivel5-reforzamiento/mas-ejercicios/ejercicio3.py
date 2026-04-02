"""
Ejercicio 3 — Fácil
Crea una clase Password que valide contraseñas. Métodos: is_valid(), strength() y __str__. Una contraseña es válida si tiene al menos 8 caracteres, una mayúscula y un número.
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