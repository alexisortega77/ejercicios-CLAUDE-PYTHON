"""
Ejercicio 5 — Medio
Crea una clase TodoList para gestionar tareas. Cada tarea tiene título, prioridad (1-3) y completada (False por defecto). Métodos: add_task(), complete_task(), pending(), by_priority() y __str__.
todo = TodoList()
todo.add_task("Estudiar Python", 1)
todo.add_task("Hacer ejercicio", 2)
todo.add_task("Leer libro", 3)
todo.complete_task("Estudiar Python")
todo.pending()      → ["Hacer ejercicio", "Leer libro"]
todo.by_priority()
→ [P1] Estudiar Python ✓
→ [P2] Hacer ejercicio ✗
→ [P3] Leer libro ✗
"""