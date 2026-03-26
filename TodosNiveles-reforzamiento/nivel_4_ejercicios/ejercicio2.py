# ------------------------------------------------------------
# EJERCICIO 2 — Fácil
# Tienes dos listas de productos. Encuentra:
# - Productos en ambas tiendas
# - Productos exclusivos de cada tienda
# - Total de productos únicos entre ambas
# ------------------------------------------------------------
tienda_a = ["leche", "pan", "huevo", "queso", "jamón", "yogurt"]
tienda_b = ["pan", "huevo", "mantequilla", "leche", "cereal", "jamón"]
set_a=set(tienda_a)
set_b=set(tienda_b) #CONVERTIR UNA LISTA EN SET 
# Output esperado:
# En ambas tiendas:     {'leche', 'pan', 'huevo', 'jamón'}
# Solo en tienda A:     {'queso', 'yogurt'}
# Solo en tienda B:     {'mantequilla', 'cereal'}
# Total únicos:         8

#a | b   # Unión → {1,2,3,4,5,6}   — todo lo de ambos
#a & b   # Intersección → {3,4}     — solo lo que comparten
#a - b   # Diferencia → {1,2}       — lo que tiene a pero no b
#a ^ b   # Dif. simétrica → {1,2,5,6} — lo que NO comparten

print(f"En ambas tiendas: {set_a&set_b}" )
print(f"Solo en tienda A: {set_a-set_b}")
print(f"Solo en tienda B: {set_b-set_a}")
print(f"Total unicos: {len(set_a|set_b)}")