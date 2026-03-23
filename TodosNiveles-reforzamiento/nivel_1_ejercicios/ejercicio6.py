# ------------------------------------------------------------
# EJERCICIO 6 — Medio
# Pide el radio de un círculo y calcula área y perímetro.
# Usa pi = 3.14159
# ------------------------------------------------------------
# Input del usuario: 7
# Output esperado:
# Radio:      7
# Área:       153.94 cm²
# Perímetro:  43.98 cm

radio=int(input("Ingresa Radio: "))
pi=3.1416
area=pi*radio**2
perimetro=2*pi*radio
print(f"Radio: {radio}")
print(f"Area: {area:.2f} cm2")
print(f"Perimetro: {perimetro:.2f} cm")