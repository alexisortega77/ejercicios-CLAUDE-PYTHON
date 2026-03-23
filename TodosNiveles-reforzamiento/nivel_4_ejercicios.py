# ============================================================
# NIVEL 4 — ESTRUCTURAS DE DATOS
# Listas, tuplas, diccionarios, sets, list comprehension
# ============================================================
# Instrucciones:
#   - Usa la estructura más adecuada para cada ejercicio
#   - Combina funciones del nivel 3 cuando sea necesario
#   - Aprovecha list comprehension donde tenga sentido
# ============================================================


# ------------------------------------------------------------
# EJERCICIO 1 — Fácil
# Dada una lista de números, crea con list comprehension:
# - Solo los impares
# - Los que son divisibles entre 3
# - Cada número multiplicado por su índice
# ------------------------------------------------------------
numeros = [4, 7, 12, 3, 18, 5, 21, 8, 9, 15]

# Output esperado:
# Original:          [4, 7, 12, 3, 18, 5, 21, 8, 9, 15]
# Impares:           [7, 3, 5, 21, 9, 15]
# Divisibles entre 3:[12, 3, 18, 21, 9, 15]
# Por su índice:     [0, 7, 24, 9, 72, 25, 126, 56, 72, 135]


# ------------------------------------------------------------
# EJERCICIO 2 — Fácil
# Tienes dos listas de productos. Encuentra:
# - Productos en ambas tiendas
# - Productos exclusivos de cada tienda
# - Total de productos únicos entre ambas
# ------------------------------------------------------------
tienda_a = ["leche", "pan", "huevo", "queso", "jamón", "yogurt"]
tienda_b = ["pan", "huevo", "mantequilla", "leche", "cereal", "jamón"]

# Output esperado:
# En ambas tiendas:     {'leche', 'pan', 'huevo', 'jamón'}
# Solo en tienda A:     {'queso', 'yogurt'}
# Solo en tienda B:     {'mantequilla', 'cereal'}
# Total únicos:         8


# ------------------------------------------------------------
# EJERCICIO 3 — Fácil
# Dado un diccionario de países y sus capitales,
# implementa búsqueda en ambas direcciones.
# ------------------------------------------------------------
paises = {
    "México": "Ciudad de México",
    "Francia": "París",
    "Japón": "Tokio",
    "Brasil": "Brasilia",
    "Australia": "Canberra"
}

# Output esperado:
# capital_de("México")    → Ciudad de México
# capital_de("Italia")    → País no encontrado
# pais_de("Tokio")        → Japón
# pais_de("Londres")      → Capital no encontrada


# ------------------------------------------------------------
# EJERCICIO 4 — Medio
# Analiza una lista de ventas mensuales.
# Cada venta es una tupla (mes, vendedor, monto).
# ------------------------------------------------------------
ventas = [
    ("enero",   "Ana",    15000),
    ("enero",   "Luis",   12000),
    ("febrero", "Ana",    18000),
    ("febrero", "Luis",    9000),
    ("marzo",   "Ana",    21000),
    ("marzo",   "Luis",   16000),
    ("marzo",   "María",  14000),
]

# Output esperado:
# Total por vendedor:
#   Ana:   $54000
#   Luis:  $37000
#   María: $14000
#
# Total por mes:
#   enero:    $27000
#   febrero:  $27000
#   marzo:    $51000
#
# Mejor vendedor: Ana ($54000)
# Mejor mes:      marzo ($51000)


# ------------------------------------------------------------
# EJERCICIO 5 — Medio
# Crea un sistema de votación.
# Recibe una lista de votos (strings con nombres de candidatos)
# y genera el reporte completo.
# ------------------------------------------------------------
votos = [
    "García", "López", "García", "Martínez", "López",
    "García", "López", "García", "Martínez", "García",
    "López",  "García", "Martínez", "López",  "García"
]

# Output esperado:
# Total de votos: 15
# Resultados:
# 1. García    → 7 votos  (46.67%)
# 2. López     → 5 votos  (33.33%)
# 3. Martínez  → 3 votos  (20.00%)
# Ganador: García con 7 votos


# ------------------------------------------------------------
# EJERCICIO 6 — Medio
# Dado un texto, genera un índice inverso:
# un diccionario donde cada palabra mapea a las posiciones
# donde aparece en el texto.
# ------------------------------------------------------------
texto = "el gato come el pescado y el gato duerme"

# Output esperado:
# el       → [0, 3, 6]
# gato     → [1, 7]
# come     → [2]
# pescado  → [4]
# y        → [5]
# duerme   → [8]


# ------------------------------------------------------------
# EJERCICIO 7 — Desafío
# Crea un sistema de estudiantes con:
# - agregar_estudiante(bd, nombre, calificaciones)
# - promedio_estudiante(bd, nombre)
# - ranking(bd) → lista ordenada de mejor a peor promedio
# - reprobados(bd) → estudiantes con promedio < 60
# - estadisticas_grupo(bd) → promedio del grupo, mejor, peor
# ------------------------------------------------------------
# Output esperado:
# bd = {}
# agregar_estudiante(bd, "Ana",    [90, 85, 92, 88])
# agregar_estudiante(bd, "Luis",   [55, 62, 48, 70])
# agregar_estudiante(bd, "María",  [78, 82, 75, 80])
# agregar_estudiante(bd, "Carlos", [95, 98, 92, 97])
#
# promedio_estudiante(bd, "Ana") → 88.75
#
# ranking(bd):
# 1. Carlos → 95.50
# 2. Ana    → 88.75
# 3. María  → 78.75
# 4. Luis   → 58.75
#
# reprobados(bd): ['Luis']
#
# estadisticas_grupo(bd):
# Promedio del grupo: 80.44
# Mejor estudiante:   Carlos (95.50)
# Peor estudiante:    Luis (58.75)


# ------------------------------------------------------------
# EJERCICIO 8 — Desafío
# Procesa un archivo de texto simulado (string multilínea)
# con datos de empleados y genera reportes.
# Formato de cada línea: "nombre,departamento,salario"
# ------------------------------------------------------------
datos_empleados = """Ana,Sistemas,25000
Luis,Ventas,18000
María,Sistemas,28000
Carlos,RRHH,20000
Pedro,Ventas,22000
Laura,Sistemas,30000
Jorge,RRHH,19000
Sofia,Ventas,21000"""

# Output esperado:
# Total empleados: 8
#
# Por departamento:
#   Sistemas: 3 empleados | Salario promedio: $27666.67
#   Ventas:   3 empleados | Salario promedio: $20333.33
#   RRHH:     2 empleados | Salario promedio: $19500.00
#
# Empleado mejor pagado:  Laura (Sistemas) - $30000
# Empleado menor salario: Luis (Ventas)    - $18000
# Masa salarial total:    $183000
