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


count={}

for voto in votos:
    count[voto]=count.get(voto, 0)+1

total=len(votos)

ordenado=sorted(count.items(), key=lambda x:x[1], reverse=True)

print(f"Total votes: {total}")


print("Results:")

for i, (candidate, votes) in enumerate(ordenado,1):
    percent= (votes/total)*100
    print(f"{i}. {candidate} -> {votes} ({percent:.2f})")

winner, winner_votes = ordenado[0]

print(f"Winner: {winner} with {winner_votes} votes")