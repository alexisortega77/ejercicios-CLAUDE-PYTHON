"""
Ejercicio 2 — Fácil
Crea funciones save_json(data, filename)
 y load_json(filename, default=None) que sean una capa
   segura sobre json.dump y json.load. load_json
     debe devolver default si el archivo no existe.

"""
import json

def save_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def load_json(filename, default=None):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return default
    except json.JSONDecodeError:
        print(f"Warning: '{filename}' is corrupted.")
        return default

data = {"name": "Manuel", "scores": [90, 85, 92]}
save_json(data, "player.json")

loaded = load_json("player.json")
print(loaded["name"])              # Manuel

missing = load_json("noexiste.json", default={})
print(missing)                     # {}