"""
Ejercicio 1 — Fácil
Crea una función save_notes(notes, filename) que guarde una lista de notas en un archivo .txt, una por línea. 
Y load_notes(filename) que las recupere como lista.

"""
def save_notes(notes, filename):
    with open(filename, "w") as f:
        f.write("\n".join(notes) + "\n")

def load_notes(filename):
    try:
        with open(filename, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

notes = ["Estudiar Python", "Hacer ejercicio", "Leer libro"]
save_notes(notes, "notes.txt")

loaded = load_notes("notes.txt")
print(loaded)   # ["Estudiar Python", "Hacer ejercicio", "Leer libro"]