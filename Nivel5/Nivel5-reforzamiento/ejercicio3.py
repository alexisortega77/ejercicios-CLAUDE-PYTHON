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