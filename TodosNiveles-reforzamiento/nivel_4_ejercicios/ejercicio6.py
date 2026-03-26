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


indice={}
for i, word in enumerate(texto.split()):
    indice.setdefault(word, []).append(i)

for w, pos in indice.items():
    print(f"{w:<8}->{pos}")