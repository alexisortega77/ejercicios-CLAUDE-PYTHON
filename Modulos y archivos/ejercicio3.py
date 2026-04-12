"""
Ejercicio 3 — Fácil
Crea un programa que mantenga un contador persistente. Cada vez que lo ejecutes el contador debe incrementarse 
y mostrar el valor actual.
# Primera ejecución:
Counter: 1

# Segunda ejecución:
Counter: 2

# Tercera ejecución:
Counter: 3

💡 Guarda el contador en un archivo JSON. Al iniciar carga el valor, incrementa y guarda de nuevo.


"""
import json

def load_json(filename, default=None):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return default

def save_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def increment_counter(filename):
    data = load_json(filename, default={"counter": 0})
    data["counter"] += 1
    save_json(data, filename)
    return data["counter"]

print(f"Counter: {increment_counter('counter.json')}")