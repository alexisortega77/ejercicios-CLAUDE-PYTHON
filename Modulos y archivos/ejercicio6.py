"""
Ejercicio 6 — Medio
Crea un sistema de logs simple. Cada evento se guarda en un archivo app.log con fecha, hora y mensaje.
pythonlog("INFO",  "Application started")
log("ERROR", "Database connection failed")
log("INFO",  "User Manuel logged in")

# app.log:
# [2026-04-07 14:32:10] INFO  - Application started
# [2026-04-07 14:32:11] ERROR - Database connection failed
# [2026-04-07 14:32:15] INFO  - User Manuel logged in

💡 Usa modo "a" para agregar sin borrar. Usa datetime.now().strftime() para el timestamp.
"""
from datetime import datetime

VALID_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}

def log(level, message, filename="app.log"):
    level = level.upper()
    if level not in VALID_LEVELS:
        raise ValueError(f"Invalid level '{level}'. Use: {VALID_LEVELS}")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry     = f"[{timestamp}] {level:<7} - {message}\n"

    with open(filename, "a") as f:
        f.write(entry)

    print(entry, end="")

def read_logs(filename="app.log", level=None):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
        if level:
            lines = [l for l in lines if level.upper() in l]
        return lines
    except FileNotFoundError:
        return []

def clear_logs(filename="app.log"):
    with open(filename, "w") as f:
        f.write("")
    print(f"Logs cleared.")


log("INFO",    "Application started")
log("ERROR",   "Database connection failed")
log("WARNING", "High memory usage")
log("INFO",    "User Manuel logged in")

print("\n--- ERROR logs only ---")
for line in read_logs(level="ERROR"):
    print(line, end="")