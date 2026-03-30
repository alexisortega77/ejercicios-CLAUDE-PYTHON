"""
Ejercicio 8 — Desafío
Crea un sistema de torneo con clases Player, Match y Tournament. Los jugadores tienen nombre y puntos (0 inicial). Cada partido tiene dos jugadores y un resultado. El torneo gestiona partidos y genera una tabla de posiciones.
tournament = Tournament("Python Cup")
p1 = Player("Ana")
p2 = Player("Luis")
p3 = Player("María")

tournament.add_player(p1)
tournament.add_player(p2)
tournament.add_player(p3)

tournament.play_match(p1, p2, "Ana")      # Ana gana → 3 pts
tournament.play_match(p2, p3, "draw")     # Empate → 1 pt cada uno
tournament.play_match(p1, p3, "Ana")      # Ana gana → 3 pts

tournament.standings()
→ Python Cup Standings:
→ 1. Ana   → 6 pts
→ 2. Luis  → 1 pts
→ 3. María → 1 pts

💡 Victoria = 3 puntos, Empate = 1 punto cada uno, Derrota = 0 puntos.
"""