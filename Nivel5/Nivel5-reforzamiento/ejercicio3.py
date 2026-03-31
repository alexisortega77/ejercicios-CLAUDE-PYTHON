"""
Ejercicio 3 — Fácil
Crea una clase Queue que implemente la estructura FIFO (opuesto al Stack). 
Métodos: enqueue(), dequeue(), front(), is_empty(), size() y __str__.
q = Queue()
q.enqueue("Ana")
q.enqueue("Luis")
q.enqueue("María")
q.front()       → "Ana"
q.dequeue()     → "Ana"
q.size()        → 2
print(q)        → Queue: ['Luis', 'María'] | Front: Luis

💡 FIFO — el primero en entrar es el primero en salir. Como una fila del banco.
"""

class Queue:
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self._items.pop(0)

    def front(self):
        if self.is_empty():
            return "Queue is empty"
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def __str__(self):
        if self.is_empty():
            return "Queue: [] | Empty"
        return f"Queue: {self._items} | Front: {self.front()}"


q = Queue()
q.enqueue("Ana")
q.enqueue("Luis")
q.enqueue("María")
print(q.front())     # Ana
print(q.dequeue())   # Ana
print(q.size())      # 2
print(q)             # Queue: ['Luis', 'María'] | Front: Luis