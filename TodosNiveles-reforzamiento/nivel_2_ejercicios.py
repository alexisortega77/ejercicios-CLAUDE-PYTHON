# ============================================================
# NIVEL 2 — CONTROL DE FLUJO
# if/elif/else, for, while, break, continue, range
# ============================================================
# Instrucciones:
#   - Resuelve cada ejercicio en un archivo separado
#   - Verifica que tu output coincida exactamente con el esperado
#   - Puedes usar variables simples, no listas ni diccionarios
# ============================================================


# ------------------------------------------------------------
# EJERCICIO 1 — Fácil
# Pide un número y clasifícalo: positivo/negativo/cero Y par/impar.
# ------------------------------------------------------------
# Input: -4
# Output esperado:
# -4 es negativo y par.
#
# Input: 7
# Output esperado:
# 7 es positivo e impar.
#
# Input: 0
# Output esperado:
# 0 es cero.


# ------------------------------------------------------------
# EJERCICIO 2 — Fácil
# Imprime los múltiplos de 7 entre 1 y 100.
# Al final muestra cuántos encontraste.
# ------------------------------------------------------------
# Output esperado:
# 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98
# Total de múltiplos de 7 entre 1 y 100: 14


# ------------------------------------------------------------
# EJERCICIO 3 — Fácil
# Pide un número N e imprime su tabla de multiplicar del 1 al 10.
# Marca con (!) los resultados mayores a 50.
# ------------------------------------------------------------
# Input: 6
# Output esperado:
# Tabla del 6:
# 6 x 1  = 6
# 6 x 2  = 12
# 6 x 3  = 18
# 6 x 4  = 24
# 6 x 5  = 30
# 6 x 6  = 36
# 6 x 7  = 42
# 6 x 8  = 48
# 6 x 9  = 54  (!)
# 6 x 10 = 60  (!)


# ------------------------------------------------------------
# EJERCICIO 4 — Medio
# Pide números hasta que el usuario escriba 0.
# Muestra suma, promedio, positivos, negativos y el mayor.
# ------------------------------------------------------------
# Inputs: 5, -3, 8, -1, 4, 0
# Output esperado:
# Números ingresados: 5
# Suma:       13
# Promedio:   2.60
# Positivos:  3
# Negativos:  2
# Mayor:      8


# ------------------------------------------------------------
# EJERCICIO 5 — Medio
# Imprime los primeros N números de la secuencia de Fibonacci.
# (no hasta un límite, sino exactamente N números)
# ------------------------------------------------------------
# Input: 8
# Output esperado:
# Fibonacci (8 números):
# 0, 1, 1, 2, 3, 5, 8, 13


# ------------------------------------------------------------
# EJERCICIO 6 — Medio
# Pide una palabra y cuenta sin usar count() ni funciones de listas:
# vocales, consonantes, espacios y su longitud total.
# ------------------------------------------------------------
# Input: murcielago
# Output esperado:
# Palabra: murcielago
# Longitud:     10
# Vocales:      5
# Consonantes:  5
# Espacios:     0


# ------------------------------------------------------------
# EJERCICIO 7 — Desafío
# Juego de piedra, papel o tijera contra la computadora.
# La computadora "elige" según el turno: turno 1→piedra, 2→papel, 3→tijera, repite.
# El jugador tiene 3 rondas. Muestra el marcador final.
# ------------------------------------------------------------
# Inputs: piedra, tijera, papel
# Output esperado:
# Ronda 1: Tú=piedra   | PC=piedra → Empate
# Ronda 2: Tú=tijera   | PC=papel  → ¡Ganaste!
# Ronda 3: Tú=papel    | PC=tijera → Perdiste
# -------------------------
# Resultado: 1 victoria, 1 derrota, 1 empate


# ------------------------------------------------------------
# EJERCICIO 8 — Desafío
# Genera un triángulo de números. El usuario elige el tamaño.
# Cada fila muestra el número de fila repetido N veces.
# ------------------------------------------------------------
# Input: 5
# Output esperado:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
