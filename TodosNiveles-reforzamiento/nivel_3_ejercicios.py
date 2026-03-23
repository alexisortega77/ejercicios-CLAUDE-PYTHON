# ============================================================
# NIVEL 3 — FUNCIONES
# def, return, parámetros, scope, lambda, funciones anidadas
# ============================================================
# Instrucciones:
#   - Cada ejercicio DEBE resolverse con funciones
#   - Las funciones de cálculo deben usar return, no print
#   - El print va siempre fuera de la función
#   - Puedes combinar con lo aprendido en niveles anteriores
# ============================================================


# ------------------------------------------------------------
# EJERCICIO 1 — Fácil
# Crea una función que reciba un número y devuelva
# si es par, impar, positivo, negativo o cero.
# ------------------------------------------------------------
# Output esperado:
# clasificar(4)   → "positivo y par"
# clasificar(-3)  → "negativo e impar"
# clasificar(0)   → "cero"
# clasificar(-8)  → "negativo y par"


# ------------------------------------------------------------
# EJERCICIO 2 — Fácil
# Crea una función que reciba dos números y una operación
# como string y devuelva el resultado.
# Operaciones: "suma", "resta", "multiplica", "divide", "potencia"
# ------------------------------------------------------------
# Output esperado:
# operar(10, 3, "suma")      → 13
# operar(10, 3, "resta")     → 7
# operar(10, 3, "multiplica")→ 30
# operar(10, 3, "divide")    → 3.3333333333333335
# operar(10, 3, "potencia")  → 1000
# operar(10, 0, "divide")    → "Error: división entre cero"
# operar(10, 3, "modulo")    → "Operación no reconocida"


# ------------------------------------------------------------
# EJERCICIO 3 — Fácil
# Crea una función que reciba un texto y devuelva
# un diccionario con sus estadísticas básicas.
# ------------------------------------------------------------
# Output esperado:
# analizar("Hola Mundo Python")
# → {
#     "palabras": 3,
#     "caracteres": 18,
#     "vocales": 5,
#     "mayusculas": 3
#   }


# ------------------------------------------------------------
# EJERCICIO 4 — Medio
# Crea tres funciones:
# - es_bisiesto(año) → True/False
# - dias_en_mes(mes, año) → número de días
# - validar_fecha(dia, mes, año) → True/False
# ------------------------------------------------------------
# Output esperado:
# es_bisiesto(2024)  → True
# es_bisiesto(2023)  → False
# es_bisiesto(1900)  → False
# es_bisiesto(2000)  → True
#
# dias_en_mes(2, 2024) → 29
# dias_en_mes(2, 2023) → 28
# dias_en_mes(4, 2024) → 30
#
# validar_fecha(29, 2, 2024) → True
# validar_fecha(29, 2, 2023) → False
# validar_fecha(31, 4, 2024) → False
# validar_fecha(15, 6, 2024) → True
#
# Pista año bisiesto: divisible entre 4, excepto siglos
# a menos que sean divisibles entre 400.


# ------------------------------------------------------------
# EJERCICIO 5 — Medio
# Crea un sistema de calificaciones con estas funciones:
# - letra(promedio)  → A/B/C/D/F
# - esta_aprobado(promedio) → True/False (mínimo 60)
# - estadisticas(calificaciones) → dict con promedio, mayor, menor, letra
# - reporte(nombre, calificaciones) → imprime todo
# ------------------------------------------------------------
# Output esperado:
# reporte("Carlos", [85, 92, 78, 90, 88])
#
# Estudiante:     Carlos
# Calificaciones: 85, 92, 78, 90, 88
# Promedio:       86.60
# Mayor:          92
# Menor:          78
# Letra:          B
# Estado:         Aprobado


# ------------------------------------------------------------
# EJERCICIO 6 — Medio
# Crea una función recursiva factorial(n) que calcule n!
# sin usar bucles ni la función math.factorial.
# Luego úsala para calcular combinaciones C(n,r) = n! / (r! * (n-r)!)
# ------------------------------------------------------------
# Output esperado:
# factorial(0) → 1
# factorial(5) → 120
# factorial(10)→ 3628800
#
# combinaciones(5, 2) → 10
# combinaciones(10,3) → 120
# combinaciones(6, 6) → 1
#
# Pista: factorial(n) = n * factorial(n-1), caso base factorial(0) = 1


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


# ------------------------------------------------------------
# EJERCICIO 8 — Desafío
# Crea un mini banco con estas funciones:
# - crear_cuenta(nombre, saldo_inicial)  → dict cuenta
# - depositar(cuenta, monto)            → nuevo saldo
# - retirar(cuenta, monto)              → nuevo saldo o error
# - transferir(cuenta_origen, cuenta_destino, monto) → True/False
# - estado_cuenta(cuenta)               → imprime resumen
# ------------------------------------------------------------
# Output esperado:
# cuenta1 = crear_cuenta("Manuel", 1000)
# cuenta2 = crear_cuenta("Ana", 500)
#
# depositar(cuenta1, 500)     → 1500
# retirar(cuenta1, 200)       → 1300
# retirar(cuenta1, 9999)      → "Saldo insuficiente"
# transferir(cuenta1, cuenta2, 300) → True
#
# estado_cuenta(cuenta1)
# Titular: Manuel
# Saldo:   $1000.00
#
# estado_cuenta(cuenta2)
# Titular: Ana
# Saldo:   $800.00
