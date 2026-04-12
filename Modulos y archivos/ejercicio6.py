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