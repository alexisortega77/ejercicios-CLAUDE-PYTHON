
# ------------------------------------------------------------
# EJERCICIO 4 — Medio
# Pide el precio de un producto y calcula el precio con IVA (16%),
# el descuento del 10% y el precio final con descuento e IVA.
# ------------------------------------------------------------
# Input del usuario: 500
# Output esperado:
# Precio original:        $500.00
# IVA (16%):              $80.00
# Precio con IVA:         $580.00
# Descuento (10%):        $50.00
# Precio final:           $522.00

monto = int(input("Ingresa monto: "))

desc=monto*.10
iva=monto*.16
precio_iva=monto+iva
desc_sobre_iva=precio_iva*.10
precio_final=precio_iva-desc_sobre_iva

print(f"Precio original: ${monto:.2f}")
print(f"IVA (16%): ${iva:.2f}")
print(f"Precio con iva: ${precio_iva:.2f}")
print(f"Descuento: (10%): ${desc:.2f}")
print(f"Precio final: ${precio_final:.2f}")