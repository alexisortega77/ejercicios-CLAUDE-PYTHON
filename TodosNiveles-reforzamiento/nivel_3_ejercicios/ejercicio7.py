# ------------------------------------------------------------
# EJERCICIO 7 — Desafío
# Crea un sistema de conversión de unidades con estas funciones:
# - convertir(valor, de_unidad, a_unidad) → resultado
# - listar_unidades() → muestra todas las unidades disponibles
#
# Unidades de longitud: mm, cm, m, km
# Factores base en metros: mm=0.001, cm=0.01, m=1, km=1000
# ------------------------------------------------------------
# Output esperado:
# convertir(100, "cm", "m")   → 1.0
# convertir(5, "km", "m")     → 5000.0
# convertir(1500, "m", "km")  → 1.5
# convertir(30, "cm", "mm")   → 300.0
# convertir(1, "año", "m")    → "Unidad no reconocida"
#
# listar_unidades()
# Unidades disponibles: mm, cm, m, km
FACTORS = {
    "mm": 0.001,
    "cm": 0.01,
    "m":  1,
    "km": 1000
}

def convert(value, from_unit, to_unit):
    if from_unit not in FACTORS or to_unit not in FACTORS:
        return "Unidad no reconocida"
    return value * FACTORS[from_unit] / FACTORS[to_unit]

def list_units():
    print(f"Unidades disponibles: {', '.join(FACTORS.keys())}")

print(convert(100, "cm", "m"))    # 1.0
print(convert(5, "km", "m"))      # 5000.0
print(convert(1500, "m", "km"))   # 1.5
print(convert(30, "cm", "mm"))    # 300.0
print(convert(1, "año", "m"))     # Unidad no reconocida

list_units()

print(convert(100, "cm", "m"))   # 1.0
print(convert(5, "km", "m"))     # 5000.0
print(convert(1500, "m", "km"))  # 1.5
print(convert(30, "cm", "mm"))   # 300.0
print(convert(1, "año", "m"))    # Unidad no reconocida
