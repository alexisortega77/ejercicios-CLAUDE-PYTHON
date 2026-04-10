from datetime import datetime
class TaskNotFoundError(Exception):
    def __init__(self, task):
        self.task = task
        super().__init__(f"'{task}' not found")
class TodoList:
    def __init__(self, name):
        self.name  = name
        self.tasks = []

    def add(self, title, priority=2):
        self.tasks.append({
            "title":     title,
            "priority":  priority,
            "done":      False,
            "created_at": datetime.now()
        })

    def complete(self, title):
        for task in self.tasks:
            if task["title"] == title:
                task["done"] = True
                return f"'{title}' completed."
            raise TaskNotFoundError(f"{title} not found")

    def pending(self):
        return [t for t in self.tasks if not t["done"]]
    def stats(self):
        total = len(self.tasks)
        completed = sum([1 for t in self.tasks if t["done"]])
        pending = total - completed
        return{
            "total":total,
            "completed": completed,
            "pending": pending
        }
         
    def by_priority(self, priority):
         return [t['title'] for t in self.tasks if t['priority']==priority]
    def delete(self, title):
         for task in self.tasks:
             if task['title'] == title:
                self.tasks.remove(task)
                return f"{title} has been deleted from tasks"
         raise TaskNotFoundError(title)
    def __str__(self):
        if not self.tasks:
            return f"'{self.name}' is empty."
        lines = [f"TodoList: {self.name}"]
        for t in sorted(self.tasks, key=lambda x: x["priority"]):
            status = "✓" if t["done"] else "✗"
            lines.append(f"  [{status}] [P{t['priority']}] {t['title']}")
        return "\n".join(lines)
    
    """
    Agrega estos tres métodos:

delete(title) — elimina una tarea por título. Si no existe lanza TaskNotFoundError.
stats() — devuelve un diccionario con total, completed y pending.
by_priority(level) — devuelve lista de tareas con esa prioridad, sin importar si están completadas.

todo = TodoList("Work")
todo.add("Write report", 1)
todo.add("Send email", 2)
todo.add("Review PR", 1)
todo.complete("Write report")

todo.stats()
→ {"total": 3, "completed": 1, "pending": 2}

todo.by_priority(1)
→ ["Write report", "Review PR"]

todo.delete("Send email")
→ "'Send email' deleted."

todo.delete("Nonexistent")
→ TaskNotFoundError: 'Nonexistent' not found

    """
todo = TodoList("Work")
todo.add("Write report", 1)
todo.add("Send email", 2)
todo.add("Review PR", 1)
print(todo.complete("Write report"))
print(todo.delete("Send email"))
try:
 print(todo.delete("Senda email"))
except TaskNotFoundError as e:
    print(f"TaskNotFoundError: {e}")
print(todo.stats())
print(todo.by_priority(1))

print(todo)
