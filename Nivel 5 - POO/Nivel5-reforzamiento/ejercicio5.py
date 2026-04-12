"""
Ejercicio 5 — Medio
Crea una clase TodoList para gestionar tareas. 
Cada tarea tiene título, prioridad (1-3) y completada (False por defecto). 
Métodos: add_task(), complete_task(), pending(), by_priority() y __str__.
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
class TodoList:
    def __init__(self):
        self.tasks=[]
    
    def add_task(self,title,priority ):
        task={
            "title":title,
            "priority":priority,
            "complete":False
        }
        self.tasks.append(task)    
    # ✅ Devuelve confirmación
    def complete_task(self, title):
     for task in self.tasks:
        if task['title'] == title:
            task['complete'] = True
            return f"'{title}' marked as complete."
     return f"Task '{title}' not found."

    def pending(self):
        pendings = [task['title'] for task in self.tasks if not task['complete']]
        return pendings
         
    def by_priority(self):
        ordenadas = sorted(self.tasks, key=lambda x: x['priority'])
        for task in ordenadas:
            estado = "✓" if task['complete'] else "✗"
            print(f"[P{task['priority']}] {task['title']} {estado}")
    
    def __str__(self):
        resultado = ""
        for task in self.tasks:
            estado = "✓" if task['complete'] else "✗"
            resultado += f"[P{task['priority']}] {task['title']} {estado}\n"
        return resultado
    
todo = TodoList()
todo.add_task("Estudiar Python", 1)
todo.add_task("Hacer ejercicio", 2)
todo.add_task("Leer libro", 3)
print(todo.complete_task("Estudiar Python"))
print(todo.pending() )   #  → ["Hacer ejercicio", "Leer libro"]
print(todo.by_priority())
print(todo)