# ------------------------------------------------------------
# EJERCICIO 5 — Medio
# Pide una temperatura en Celsius y conviértela a Fahrenheit y Kelvin.
# Fórmulas: F = (C * 9/5) + 32   |   K = C + 273.15
# ------------------------------------------------------------
# Input del usuario: 100
# Output esperado:
# Celsius:    100°C
# Fahrenheit: 212.00°F
# Kelvin:     373.15K

celcius=int(input("ingresa Celsius: "))
f=(celcius*9/5)+32
k=celcius+273.15
print(f"Celsius: {celcius}°C")
print(f"Fahrenheit: {f:.2f}°F")
print(f"Kelvin: {k:.2f}K")

