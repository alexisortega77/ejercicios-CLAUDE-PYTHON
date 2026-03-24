
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

victoria=0
derrota=0
empate=0
ronda=3
opciones_pc=["piedra", "papel", "tijera"]
for i in range(1,ronda+1):
    eleccion=input("elige que usaras: ").lower()
    pc = opciones_pc[i % 3]

    if eleccion==pc:
        resultado="empate"
        empate+=1
    elif eleccion=="piedra" and pc=="tijera" or \
    eleccion=="papel" and pc=="piedra" or \
    eleccion=="tijera" and pc=="papel":
        resultado="Ganaste"
        victoria+=1
    else:
        resultado="perdiste"
    print(f"Ronda {i}: Tú={eleccion}   | PC={pc} → {resultado}")

print(f"Resultado: victorias: {victoria}, derrotas: {derrota}, empates: {empate}")